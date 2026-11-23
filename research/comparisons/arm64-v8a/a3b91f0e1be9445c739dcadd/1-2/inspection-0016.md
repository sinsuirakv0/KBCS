# v15.7.3 → v15.7.4 · 要調査の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-9adcaa8f2c9a880a04d0f7b9535aa8a1"></a>

### [`00b8b514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b514.md) → [`00b8b558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md) FUN_00b8b558

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8b50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b50c.md) · 呼出先 6件 [`00bb93e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)
- 新版 呼出元 1件 [`00b8b550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b550.md) · 呼出先 6件 [`00bb9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9424.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b514.md#insn-00b8b59c) · [`00b8b5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b514.md#insn-00b8b5b8) · [`00b8b63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b514.md#insn-00b8b63c)
- 新版 [`00b8b5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md#insn-00b8b5e0) · [`00b8b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md#insn-00b8b5fc) · [`00b8b680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md#insn-00b8b680)

~~~diff
- 00b8b59c ["INT_ADD", "register:40f0:8", ["const:b8b59c:8", "const:4:8"]]
- 00b8b59c ["CALL", null, ["callee:00be1520:8"]]
+ 00b8b5e0 ["INT_ADD", "register:40f0:8", ["const:b8b5e0:8", "const:4:8"]]
+ 00b8b5e0 ["CALL", null, ["callee:00be1520:8"]]
- 00b8b59c bytes cd570194
+ 00b8b5e0 bytes d0570194
- 00b8b5b8 ["INT_ADD", "register:40f0:8", ["const:b8b5b8:8", "const:4:8"]]
- 00b8b5b8 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8b5fc ["INT_ADD", "register:40f0:8", ["const:b8b5fc:8", "const:4:8"]]
+ 00b8b5fc ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8b5b8 bytes 6e4e0194
+ 00b8b5fc bytes 714e0194
- 00b8b63c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8b63c ["INT_ADD", "register:40f0:8", ["const:b8b63c:8", "const:4:8"]]
- 00b8b63c ["CALLIND", null, ["register:0:8"]]
+ 00b8b680 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8b680 ["INT_ADD", "register:40f0:8", ["const:b8b680:8", "const:4:8"]]
+ 00b8b680 ["CALLIND", null, ["register:0:8"]]
- 00b8b63c bytes 00013fd6
+ 00b8b680 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d90e8e0faa305d2f3665c3373ed977b3"></a>

### [`00b8b950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b950.md) → [`00b8b994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md) FUN_00b8b994

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b948.md) · 呼出先 6件 [`00bb9508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)
- 新版 呼出元 1件 [`00b8b98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b98c.md) · 呼出先 6件 [`00bb954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb954c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b950.md#insn-00b8b9d8) · [`00b8b9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b950.md#insn-00b8b9f4) · [`00b8ba78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b950.md#insn-00b8ba78)
- 新版 [`00b8ba1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md#insn-00b8ba1c) · [`00b8ba38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md#insn-00b8ba38) · [`00b8babc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md#insn-00b8babc)

~~~diff
- 00b8b9d8 ["INT_ADD", "register:40f0:8", ["const:b8b9d8:8", "const:4:8"]]
- 00b8b9d8 ["CALL", null, ["callee:00be1520:8"]]
+ 00b8ba1c ["INT_ADD", "register:40f0:8", ["const:b8ba1c:8", "const:4:8"]]
+ 00b8ba1c ["CALL", null, ["callee:00be1520:8"]]
- 00b8b9d8 bytes be560194
+ 00b8ba1c bytes c1560194
- 00b8b9f4 ["INT_ADD", "register:40f0:8", ["const:b8b9f4:8", "const:4:8"]]
- 00b8b9f4 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8ba38 ["INT_ADD", "register:40f0:8", ["const:b8ba38:8", "const:4:8"]]
+ 00b8ba38 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8b9f4 bytes 5f4d0194
+ 00b8ba38 bytes 624d0194
- 00b8ba78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8ba78 ["INT_ADD", "register:40f0:8", ["const:b8ba78:8", "const:4:8"]]
- 00b8ba78 ["CALLIND", null, ["register:0:8"]]
+ 00b8babc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8babc ["INT_ADD", "register:40f0:8", ["const:b8babc:8", "const:4:8"]]
+ 00b8babc ["CALLIND", null, ["register:0:8"]]
- 00b8ba78 bytes 00013fd6
+ 00b8babc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999e3fe02c64d021cc87d957b62c72e9"></a>

### [`00b8bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd8c.md) → [`00b8bdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md) FUN_00b8bdd0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8bd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd84.md) · 呼出先 6件 [`00bb9660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)
- 新版 呼出元 1件 [`00b8bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdc8.md) · 呼出先 6件 [`00bb96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb96a4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8be14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd8c.md#insn-00b8be14) · [`00b8be30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd8c.md#insn-00b8be30) · [`00b8beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd8c.md#insn-00b8beb4)
- 新版 [`00b8be58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md#insn-00b8be58) · [`00b8be74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md#insn-00b8be74) · [`00b8bef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md#insn-00b8bef8)

~~~diff
- 00b8be14 ["INT_ADD", "register:40f0:8", ["const:b8be14:8", "const:4:8"]]
- 00b8be14 ["CALL", null, ["callee:00be1520:8"]]
+ 00b8be58 ["INT_ADD", "register:40f0:8", ["const:b8be58:8", "const:4:8"]]
+ 00b8be58 ["CALL", null, ["callee:00be1520:8"]]
- 00b8be14 bytes af550194
+ 00b8be58 bytes b2550194
- 00b8be30 ["INT_ADD", "register:40f0:8", ["const:b8be30:8", "const:4:8"]]
- 00b8be30 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8be74 ["INT_ADD", "register:40f0:8", ["const:b8be74:8", "const:4:8"]]
+ 00b8be74 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8be30 bytes 504c0194
+ 00b8be74 bytes 534c0194
- 00b8beb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8beb4 ["INT_ADD", "register:40f0:8", ["const:b8beb4:8", "const:4:8"]]
- 00b8beb4 ["CALLIND", null, ["register:0:8"]]
+ 00b8bef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8bef8 ["INT_ADD", "register:40f0:8", ["const:b8bef8:8", "const:4:8"]]
+ 00b8bef8 ["CALLIND", null, ["register:0:8"]]
- 00b8beb4 bytes 00013fd6
+ 00b8bef8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-147120b37cdb9d6c3c8d218fb132a865"></a>

### [`00b8c1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c1c8.md) → [`00b8c20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md) FUN_00b8c20c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8c1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c1c0.md) · 呼出先 6件 [`00bb97b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)
- 新版 呼出元 1件 [`00b8c204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c204.md) · 呼出先 6件 [`00bb97f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb97f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8c250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c1c8.md#insn-00b8c250) · [`00b8c26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c1c8.md#insn-00b8c26c) · [`00b8c2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c1c8.md#insn-00b8c2f0)
- 新版 [`00b8c294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md#insn-00b8c294) · [`00b8c2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md#insn-00b8c2b0) · [`00b8c334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md#insn-00b8c334)

~~~diff
- 00b8c250 ["INT_ADD", "register:40f0:8", ["const:b8c250:8", "const:4:8"]]
- 00b8c250 ["CALL", null, ["callee:00be1520:8"]]
+ 00b8c294 ["INT_ADD", "register:40f0:8", ["const:b8c294:8", "const:4:8"]]
+ 00b8c294 ["CALL", null, ["callee:00be1520:8"]]
- 00b8c250 bytes a0540194
+ 00b8c294 bytes a3540194
- 00b8c26c ["INT_ADD", "register:40f0:8", ["const:b8c26c:8", "const:4:8"]]
- 00b8c26c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8c2b0 ["INT_ADD", "register:40f0:8", ["const:b8c2b0:8", "const:4:8"]]
+ 00b8c2b0 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8c26c bytes 414b0194
+ 00b8c2b0 bytes 444b0194
- 00b8c2f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8c2f0 ["INT_ADD", "register:40f0:8", ["const:b8c2f0:8", "const:4:8"]]
- 00b8c2f0 ["CALLIND", null, ["register:0:8"]]
+ 00b8c334 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8c334 ["INT_ADD", "register:40f0:8", ["const:b8c334:8", "const:4:8"]]
+ 00b8c334 ["CALLIND", null, ["register:0:8"]]
- 00b8c2f0 bytes 00013fd6
+ 00b8c334 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54c42200f4e50dff36dee3959dc9b36a"></a>

### [`00b8c604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c604.md) → [`00b8c648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md) FUN_00b8c648

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8c5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c5fc.md) · 呼出先 6件 [`00bb98fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)
- 新版 呼出元 1件 [`00b8c640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c640.md) · 呼出先 6件 [`00bb9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9940.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8c68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c604.md#insn-00b8c68c) · [`00b8c6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c604.md#insn-00b8c6a8) · [`00b8c72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c604.md#insn-00b8c72c)
- 新版 [`00b8c6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md#insn-00b8c6d0) · [`00b8c6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md#insn-00b8c6ec) · [`00b8c770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md#insn-00b8c770)

~~~diff
- 00b8c68c ["INT_ADD", "register:40f0:8", ["const:b8c68c:8", "const:4:8"]]
- 00b8c68c ["CALL", null, ["callee:00be1520:8"]]
+ 00b8c6d0 ["INT_ADD", "register:40f0:8", ["const:b8c6d0:8", "const:4:8"]]
+ 00b8c6d0 ["CALL", null, ["callee:00be1520:8"]]
- 00b8c68c bytes 91530194
+ 00b8c6d0 bytes 94530194
- 00b8c6a8 ["INT_ADD", "register:40f0:8", ["const:b8c6a8:8", "const:4:8"]]
- 00b8c6a8 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8c6ec ["INT_ADD", "register:40f0:8", ["const:b8c6ec:8", "const:4:8"]]
+ 00b8c6ec ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8c6a8 bytes 324a0194
+ 00b8c6ec bytes 354a0194
- 00b8c72c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8c72c ["INT_ADD", "register:40f0:8", ["const:b8c72c:8", "const:4:8"]]
- 00b8c72c ["CALLIND", null, ["register:0:8"]]
+ 00b8c770 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8c770 ["INT_ADD", "register:40f0:8", ["const:b8c770:8", "const:4:8"]]
+ 00b8c770 ["CALLIND", null, ["register:0:8"]]
- 00b8c72c bytes 00013fd6
+ 00b8c770 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2853ae2aa97965729f581396be112718"></a>

### [`00b8ca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca40.md) → [`00b8ca84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md) FUN_00b8ca84

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8ca38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca38.md) · 呼出先 6件 [`00bb9a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1500.md)
- 新版 呼出元 1件 [`00b8ca7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca7c.md) · 呼出先 6件 [`00bb9a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9a88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8ca8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca40.md#insn-00b8ca8c) · [`00b8caa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca40.md#insn-00b8caa8) · [`00b8cb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca40.md#insn-00b8cb38)
- 新版 [`00b8cad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md#insn-00b8cad0) · [`00b8caec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md#insn-00b8caec) · [`00b8cb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md#insn-00b8cb7c)

~~~diff
- 00b8ca8c ["INT_ADD", "register:40f0:8", ["const:b8ca8c:8", "const:4:8"]]
- 00b8ca8c ["CALL", null, ["callee:00be1550:8"]]
+ 00b8cad0 ["INT_ADD", "register:40f0:8", ["const:b8cad0:8", "const:4:8"]]
+ 00b8cad0 ["CALL", null, ["callee:00be1550:8"]]
- 00b8ca8c bytes 9d520194
+ 00b8cad0 bytes a0520194
- 00b8caa8 ["INT_ADD", "register:40f0:8", ["const:b8caa8:8", "const:4:8"]]
- 00b8caa8 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8caec ["INT_ADD", "register:40f0:8", ["const:b8caec:8", "const:4:8"]]
+ 00b8caec ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8caa8 bytes 32490194
+ 00b8caec bytes 35490194
- 00b8cb38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8cb38 ["INT_ADD", "register:40f0:8", ["const:b8cb38:8", "const:4:8"]]
- 00b8cb38 ["CALLIND", null, ["register:0:8"]]
+ 00b8cb7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8cb7c ["INT_ADD", "register:40f0:8", ["const:b8cb7c:8", "const:4:8"]]
+ 00b8cb7c ["CALLIND", null, ["register:0:8"]]
- 00b8cb38 bytes 00013fd6
+ 00b8cb7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02da6d2822681712beafe451f6917975"></a>

### [`00b8ce58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce58.md) → [`00b8ce9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md) FUN_00b8ce9c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8ce50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce50.md) · 呼出先 6件 [`00bb9b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1500.md)
- 新版 呼出元 1件 [`00b8ce94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce94.md) · 呼出先 6件 [`00bb9ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ba0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8cea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce58.md#insn-00b8cea4) · [`00b8cec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce58.md#insn-00b8cec0) · [`00b8cf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce58.md#insn-00b8cf50)
- 新版 [`00b8cee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md#insn-00b8cee8) · [`00b8cf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md#insn-00b8cf04) · [`00b8cf94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md#insn-00b8cf94)

~~~diff
- 00b8cea4 ["INT_ADD", "register:40f0:8", ["const:b8cea4:8", "const:4:8"]]
- 00b8cea4 ["CALL", null, ["callee:00be1550:8"]]
+ 00b8cee8 ["INT_ADD", "register:40f0:8", ["const:b8cee8:8", "const:4:8"]]
+ 00b8cee8 ["CALL", null, ["callee:00be1550:8"]]
- 00b8cea4 bytes 97510194
+ 00b8cee8 bytes 9a510194
- 00b8cec0 ["INT_ADD", "register:40f0:8", ["const:b8cec0:8", "const:4:8"]]
- 00b8cec0 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8cf04 ["INT_ADD", "register:40f0:8", ["const:b8cf04:8", "const:4:8"]]
+ 00b8cf04 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8cec0 bytes 2c480194
+ 00b8cf04 bytes 2f480194
- 00b8cf50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8cf50 ["INT_ADD", "register:40f0:8", ["const:b8cf50:8", "const:4:8"]]
- 00b8cf50 ["CALLIND", null, ["register:0:8"]]
+ 00b8cf94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8cf94 ["INT_ADD", "register:40f0:8", ["const:b8cf94:8", "const:4:8"]]
+ 00b8cf94 ["CALLIND", null, ["register:0:8"]]
- 00b8cf50 bytes 00013fd6
+ 00b8cf94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a952fba5f280e72336569defa5133814"></a>

### [`00b8d270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d270.md) → [`00b8d2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md) FUN_00b8d2b4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8d268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d268.md) · 呼出先 6件 [`00bb9c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1500.md)
- 新版 呼出元 1件 [`00b8d2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2ac.md) · 呼出先 6件 [`00bb9cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9cb8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8d2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d270.md#insn-00b8d2bc) · [`00b8d2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d270.md#insn-00b8d2d8) · [`00b8d368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d270.md#insn-00b8d368)
- 新版 [`00b8d300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md#insn-00b8d300) · [`00b8d31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md#insn-00b8d31c) · [`00b8d3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md#insn-00b8d3ac)

~~~diff
- 00b8d2bc ["INT_ADD", "register:40f0:8", ["const:b8d2bc:8", "const:4:8"]]
- 00b8d2bc ["CALL", null, ["callee:00be1550:8"]]
+ 00b8d300 ["INT_ADD", "register:40f0:8", ["const:b8d300:8", "const:4:8"]]
+ 00b8d300 ["CALL", null, ["callee:00be1550:8"]]
- 00b8d2bc bytes 91500194
+ 00b8d300 bytes 94500194
- 00b8d2d8 ["INT_ADD", "register:40f0:8", ["const:b8d2d8:8", "const:4:8"]]
- 00b8d2d8 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8d31c ["INT_ADD", "register:40f0:8", ["const:b8d31c:8", "const:4:8"]]
+ 00b8d31c ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8d2d8 bytes 26470194
+ 00b8d31c bytes 29470194
- 00b8d368 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8d368 ["INT_ADD", "register:40f0:8", ["const:b8d368:8", "const:4:8"]]
- 00b8d368 ["CALLIND", null, ["register:0:8"]]
+ 00b8d3ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8d3ac ["INT_ADD", "register:40f0:8", ["const:b8d3ac:8", "const:4:8"]]
+ 00b8d3ac ["CALLIND", null, ["register:0:8"]]
- 00b8d368 bytes 00013fd6
+ 00b8d3ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71d3d050645872be79b69d448cab0a83"></a>

### [`00b8dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dd74.md) → [`00b8ddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md) FUN_00b8ddb8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b8d680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md) [`00b90af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md) · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1540.md)
- 新版 呼出元 2件 [`00b8d6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md) [`00b90b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md) · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8ddd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dd74.md#insn-00b8ddd8) · [`00b8ddf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dd74.md#insn-00b8ddf4) · [`00b8de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dd74.md#insn-00b8de04)
- 新版 [`00b8de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md#insn-00b8de1c) · [`00b8de38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md#insn-00b8de38) · [`00b8de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md#insn-00b8de48)

~~~diff
- 00b8ddd8 ["INT_ADD", "register:40f0:8", ["const:b8ddd8:8", "const:4:8"]]
- 00b8ddd8 ["CALL", null, ["callee:00be1580:8"]]
+ 00b8de1c ["INT_ADD", "register:40f0:8", ["const:b8de1c:8", "const:4:8"]]
+ 00b8de1c ["CALL", null, ["callee:00be1580:8"]]
- 00b8ddd8 bytes d64d0194
+ 00b8de1c bytes d94d0194
- 00b8ddf4 ["INT_ADD", "register:40f0:8", ["const:b8ddf4:8", "const:4:8"]]
- 00b8ddf4 ["CALL", null, ["callee:00be1590:8"]]
+ 00b8de38 ["INT_ADD", "register:40f0:8", ["const:b8de38:8", "const:4:8"]]
+ 00b8de38 ["CALL", null, ["callee:00be1590:8"]]
- 00b8ddf4 bytes d34d0194
+ 00b8de38 bytes d64d0194
- 00b8de04 ["INT_ADD", "register:40f0:8", ["const:b8de04:8", "const:4:8"]]
- 00b8de04 ["CALL", null, ["callee:00be1580:8"]]
+ 00b8de48 ["INT_ADD", "register:40f0:8", ["const:b8de48:8", "const:4:8"]]
+ 00b8de48 ["CALL", null, ["callee:00be1580:8"]]
- 00b8de04 bytes cb4d0194
+ 00b8de48 bytes ce4d0194
~~~


<a id="compare-4c0f7dd26d77e75832fe833fd2cbc546"></a>

### [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md) → [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) FUN_00b8e180

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00b8deb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md) [`00b9830c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9830c.md) [`00b98464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98464.md) [`00b98520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98520.md) [`00b98670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98670.md) · 呼出先 3件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md)
- 新版 呼出元 7件 [`00b8def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md) [`00b98350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md) [`00b984a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md) [`00b98564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md) [`00b986b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md) · 呼出先 3件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8e19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md#insn-00b8e19c) · [`00b8e1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md#insn-00b8e1a8) · [`00b8e244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md#insn-00b8e244)
- 新版 [`00b8e1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md#insn-00b8e1e0) · [`00b8e1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md#insn-00b8e1ec) · [`00b8e288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md#insn-00b8e288)

~~~diff
- 00b8e19c ["INT_ADD", "register:40f0:8", ["const:b8e19c:8", "const:4:8"]]
- 00b8e19c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00b8e1e0 ["INT_ADD", "register:40f0:8", ["const:b8e1e0:8", "const:4:8"]]
+ 00b8e1e0 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00b8e19c bytes f93b0194
+ 00b8e1e0 bytes fc3b0194
- 00b8e1a8 ["INT_ADD", "register:40f0:8", ["const:b8e1a8:8", "const:4:8"]]
- 00b8e1a8 ["CALL", null, ["callee:00be0f80:8"]]
+ 00b8e1ec ["INT_ADD", "register:40f0:8", ["const:b8e1ec:8", "const:4:8"]]
+ 00b8e1ec ["CALL", null, ["callee:00be0f80:8"]]
- 00b8e1a8 bytes 624b0194
+ 00b8e1ec bytes 654b0194
- 00b8e244 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8e244 ["INT_ADD", "register:40f0:8", ["const:b8e244:8", "const:4:8"]]
- 00b8e244 ["CALLIND", null, ["register:0:8"]]
+ 00b8e288 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8e288 ["INT_ADD", "register:40f0:8", ["const:b8e288:8", "const:4:8"]]
+ 00b8e288 ["CALLIND", null, ["register:0:8"]]
- 00b8e244 bytes 00013fd6
+ 00b8e288 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19299c0c508f63d4880f20f564ade7af"></a>

### [`00b8e5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e5b8.md) → [`00b8e5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md) FUN_00b8e5fc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e5b0.md) · 呼出先 6件 [`00bb92b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00b8e5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5f4.md) · 呼出先 6件 [`00bb92fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8e640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e5b8.md#insn-00b8e640) · [`00b8e65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e5b8.md#insn-00b8e65c) · [`00b8e6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e5b8.md#insn-00b8e6cc)
- 新版 [`00b8e684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md#insn-00b8e684) · [`00b8e6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md#insn-00b8e6a0) · [`00b8e710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md#insn-00b8e710)

~~~diff
- 00b8e640 ["INT_ADD", "register:40f0:8", ["const:b8e640:8", "const:4:8"]]
- 00b8e640 ["CALL", null, ["callee:00be15a0:8"]]
+ 00b8e684 ["INT_ADD", "register:40f0:8", ["const:b8e684:8", "const:4:8"]]
+ 00b8e684 ["CALL", null, ["callee:00be15a0:8"]]
- 00b8e640 bytes c44b0194
+ 00b8e684 bytes c74b0194
- 00b8e65c ["INT_ADD", "register:40f0:8", ["const:b8e65c:8", "const:4:8"]]
- 00b8e65c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8e6a0 ["INT_ADD", "register:40f0:8", ["const:b8e6a0:8", "const:4:8"]]
+ 00b8e6a0 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8e65c bytes 45420194
+ 00b8e6a0 bytes 48420194
- 00b8e6cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8e6cc ["INT_ADD", "register:40f0:8", ["const:b8e6cc:8", "const:4:8"]]
- 00b8e6cc ["CALLIND", null, ["register:0:8"]]
+ 00b8e710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8e710 ["INT_ADD", "register:40f0:8", ["const:b8e710:8", "const:4:8"]]
+ 00b8e710 ["CALLIND", null, ["register:0:8"]]
- 00b8e6cc bytes 00013fd6
+ 00b8e710 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a095b556c24e6ef9c797ca46f99b7fc"></a>

### [`00b8e9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e9e8.md) → [`00b8ea2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md) FUN_00b8ea2c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8e9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e9e0.md) · 呼出先 6件 [`00bb93e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00b8ea24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea24.md) · 呼出先 6件 [`00bb9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9424.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8ea70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e9e8.md#insn-00b8ea70) · [`00b8ea8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e9e8.md#insn-00b8ea8c) · [`00b8eafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e9e8.md#insn-00b8eafc)
- 新版 [`00b8eab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md#insn-00b8eab4) · [`00b8ead0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md#insn-00b8ead0) · [`00b8eb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md#insn-00b8eb40)

~~~diff
- 00b8ea70 ["INT_ADD", "register:40f0:8", ["const:b8ea70:8", "const:4:8"]]
- 00b8ea70 ["CALL", null, ["callee:00be15a0:8"]]
+ 00b8eab4 ["INT_ADD", "register:40f0:8", ["const:b8eab4:8", "const:4:8"]]
+ 00b8eab4 ["CALL", null, ["callee:00be15a0:8"]]
- 00b8ea70 bytes b84a0194
+ 00b8eab4 bytes bb4a0194
- 00b8ea8c ["INT_ADD", "register:40f0:8", ["const:b8ea8c:8", "const:4:8"]]
- 00b8ea8c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8ead0 ["INT_ADD", "register:40f0:8", ["const:b8ead0:8", "const:4:8"]]
+ 00b8ead0 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8ea8c bytes 39410194
+ 00b8ead0 bytes 3c410194
- 00b8eafc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8eafc ["INT_ADD", "register:40f0:8", ["const:b8eafc:8", "const:4:8"]]
- 00b8eafc ["CALLIND", null, ["register:0:8"]]
+ 00b8eb40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8eb40 ["INT_ADD", "register:40f0:8", ["const:b8eb40:8", "const:4:8"]]
+ 00b8eb40 ["CALLIND", null, ["register:0:8"]]
- 00b8eafc bytes 00013fd6
+ 00b8eb40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d183bb162c89fa07c67bda58898235e2"></a>

### [`00b8ee18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8ee18.md) → [`00b8ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md) FUN_00b8ee5c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8ee10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8ee10.md) · 呼出先 6件 [`00bb9508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00b8ee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee54.md) · 呼出先 6件 [`00bb954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb954c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8eea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8ee18.md#insn-00b8eea0) · [`00b8eebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8ee18.md#insn-00b8eebc) · [`00b8ef2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8ee18.md#insn-00b8ef2c)
- 新版 [`00b8eee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md#insn-00b8eee4) · [`00b8ef00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md#insn-00b8ef00) · [`00b8ef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md#insn-00b8ef70)

~~~diff
- 00b8eea0 ["INT_ADD", "register:40f0:8", ["const:b8eea0:8", "const:4:8"]]
- 00b8eea0 ["CALL", null, ["callee:00be15a0:8"]]
+ 00b8eee4 ["INT_ADD", "register:40f0:8", ["const:b8eee4:8", "const:4:8"]]
+ 00b8eee4 ["CALL", null, ["callee:00be15a0:8"]]
- 00b8eea0 bytes ac490194
+ 00b8eee4 bytes af490194
- 00b8eebc ["INT_ADD", "register:40f0:8", ["const:b8eebc:8", "const:4:8"]]
- 00b8eebc ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8ef00 ["INT_ADD", "register:40f0:8", ["const:b8ef00:8", "const:4:8"]]
+ 00b8ef00 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8eebc bytes 2d400194
+ 00b8ef00 bytes 30400194
- 00b8ef2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8ef2c ["INT_ADD", "register:40f0:8", ["const:b8ef2c:8", "const:4:8"]]
- 00b8ef2c ["CALLIND", null, ["register:0:8"]]
+ 00b8ef70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8ef70 ["INT_ADD", "register:40f0:8", ["const:b8ef70:8", "const:4:8"]]
+ 00b8ef70 ["CALLIND", null, ["register:0:8"]]
- 00b8ef2c bytes 00013fd6
+ 00b8ef70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3feb0f19856d386a95f01a1ba207f4a5"></a>

### [`00b8f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f248.md) → [`00b8f28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md) FUN_00b8f28c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8f240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f240.md) · 呼出先 6件 [`00bb9660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00b8f284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f284.md) · 呼出先 6件 [`00bb96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb96a4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8f2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f248.md#insn-00b8f2d0) · [`00b8f2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f248.md#insn-00b8f2ec) · [`00b8f35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f248.md#insn-00b8f35c)
- 新版 [`00b8f314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md#insn-00b8f314) · [`00b8f330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md#insn-00b8f330) · [`00b8f3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md#insn-00b8f3a0)

~~~diff
- 00b8f2d0 ["INT_ADD", "register:40f0:8", ["const:b8f2d0:8", "const:4:8"]]
- 00b8f2d0 ["CALL", null, ["callee:00be15a0:8"]]
+ 00b8f314 ["INT_ADD", "register:40f0:8", ["const:b8f314:8", "const:4:8"]]
+ 00b8f314 ["CALL", null, ["callee:00be15a0:8"]]
- 00b8f2d0 bytes a0480194
+ 00b8f314 bytes a3480194
- 00b8f2ec ["INT_ADD", "register:40f0:8", ["const:b8f2ec:8", "const:4:8"]]
- 00b8f2ec ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8f330 ["INT_ADD", "register:40f0:8", ["const:b8f330:8", "const:4:8"]]
+ 00b8f330 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8f2ec bytes 213f0194
+ 00b8f330 bytes 243f0194
- 00b8f35c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8f35c ["INT_ADD", "register:40f0:8", ["const:b8f35c:8", "const:4:8"]]
- 00b8f35c ["CALLIND", null, ["register:0:8"]]
+ 00b8f3a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8f3a0 ["INT_ADD", "register:40f0:8", ["const:b8f3a0:8", "const:4:8"]]
+ 00b8f3a0 ["CALLIND", null, ["register:0:8"]]
- 00b8f35c bytes 00013fd6
+ 00b8f3a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f407a8f5f27b354f3e1c53f4d7820de4"></a>

### [`00b8f678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f678.md) → [`00b8f6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md) FUN_00b8f6bc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8f670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f670.md) · 呼出先 6件 [`00bb97b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00b8f6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6b4.md) · 呼出先 6件 [`00bb97f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb97f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8f700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f678.md#insn-00b8f700) · [`00b8f71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f678.md#insn-00b8f71c) · [`00b8f78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f678.md#insn-00b8f78c)
- 新版 [`00b8f744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md#insn-00b8f744) · [`00b8f760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md#insn-00b8f760) · [`00b8f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md#insn-00b8f7d0)

~~~diff
- 00b8f700 ["INT_ADD", "register:40f0:8", ["const:b8f700:8", "const:4:8"]]
- 00b8f700 ["CALL", null, ["callee:00be15a0:8"]]
+ 00b8f744 ["INT_ADD", "register:40f0:8", ["const:b8f744:8", "const:4:8"]]
+ 00b8f744 ["CALL", null, ["callee:00be15a0:8"]]
- 00b8f700 bytes 94470194
+ 00b8f744 bytes 97470194
- 00b8f71c ["INT_ADD", "register:40f0:8", ["const:b8f71c:8", "const:4:8"]]
- 00b8f71c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8f760 ["INT_ADD", "register:40f0:8", ["const:b8f760:8", "const:4:8"]]
+ 00b8f760 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8f71c bytes 153e0194
+ 00b8f760 bytes 183e0194
- 00b8f78c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8f78c ["INT_ADD", "register:40f0:8", ["const:b8f78c:8", "const:4:8"]]
- 00b8f78c ["CALLIND", null, ["register:0:8"]]
+ 00b8f7d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8f7d0 ["INT_ADD", "register:40f0:8", ["const:b8f7d0:8", "const:4:8"]]
+ 00b8f7d0 ["CALLIND", null, ["register:0:8"]]
- 00b8f78c bytes 00013fd6
+ 00b8f7d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93f6c71540fc73168ea5d3a11af561ae"></a>

### [`00b8faa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa8.md) → [`00b8faec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md) FUN_00b8faec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8faa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa0.md) · 呼出先 6件 [`00bb98fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00b8fae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8fae4.md) · 呼出先 6件 [`00bb9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9940.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8fb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa8.md#insn-00b8fb30) · [`00b8fb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa8.md#insn-00b8fb4c) · [`00b8fbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa8.md#insn-00b8fbbc)
- 新版 [`00b8fb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md#insn-00b8fb74) · [`00b8fb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md#insn-00b8fb90) · [`00b8fc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md#insn-00b8fc00)

~~~diff
- 00b8fb30 ["INT_ADD", "register:40f0:8", ["const:b8fb30:8", "const:4:8"]]
- 00b8fb30 ["CALL", null, ["callee:00be15a0:8"]]
+ 00b8fb74 ["INT_ADD", "register:40f0:8", ["const:b8fb74:8", "const:4:8"]]
+ 00b8fb74 ["CALL", null, ["callee:00be15a0:8"]]
- 00b8fb30 bytes 88460194
+ 00b8fb74 bytes 8b460194
- 00b8fb4c ["INT_ADD", "register:40f0:8", ["const:b8fb4c:8", "const:4:8"]]
- 00b8fb4c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8fb90 ["INT_ADD", "register:40f0:8", ["const:b8fb90:8", "const:4:8"]]
+ 00b8fb90 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8fb4c bytes 093d0194
+ 00b8fb90 bytes 0c3d0194
- 00b8fbbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8fbbc ["INT_ADD", "register:40f0:8", ["const:b8fbbc:8", "const:4:8"]]
- 00b8fbbc ["CALLIND", null, ["register:0:8"]]
+ 00b8fc00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8fc00 ["INT_ADD", "register:40f0:8", ["const:b8fc00:8", "const:4:8"]]
+ 00b8fc00 ["CALLIND", null, ["register:0:8"]]
- 00b8fbbc bytes 00013fd6
+ 00b8fc00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cc6dbf66ffda40c72683fee079302e3"></a>

### [`00b8fed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8fed8.md) → [`00b8ff1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md) FUN_00b8ff1c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8fed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8fed0.md) · 呼出先 6件 [`00bb9a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1570.md)
- 新版 呼出元 1件 [`00b8ff14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff14.md) · 呼出先 6件 [`00bb9a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9a88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8ff24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8fed8.md#insn-00b8ff24) · [`00b8ff40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8fed8.md#insn-00b8ff40) · [`00b8ffc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8fed8.md#insn-00b8ffc0)
- 新版 [`00b8ff68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md#insn-00b8ff68) · [`00b8ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md#insn-00b8ff84) · [`00b90004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md#insn-00b90004)

~~~diff
- 00b8ff24 ["INT_ADD", "register:40f0:8", ["const:b8ff24:8", "const:4:8"]]
- 00b8ff24 ["CALL", null, ["callee:00be15c0:8"]]
+ 00b8ff68 ["INT_ADD", "register:40f0:8", ["const:b8ff68:8", "const:4:8"]]
+ 00b8ff68 ["CALL", null, ["callee:00be15c0:8"]]
- 00b8ff24 bytes 93450194
+ 00b8ff68 bytes 96450194
- 00b8ff40 ["INT_ADD", "register:40f0:8", ["const:b8ff40:8", "const:4:8"]]
- 00b8ff40 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8ff84 ["INT_ADD", "register:40f0:8", ["const:b8ff84:8", "const:4:8"]]
+ 00b8ff84 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8ff40 bytes 0c3c0194
+ 00b8ff84 bytes 0f3c0194
- 00b8ffc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8ffc0 ["INT_ADD", "register:40f0:8", ["const:b8ffc0:8", "const:4:8"]]
- 00b8ffc0 ["CALLIND", null, ["register:0:8"]]
+ 00b90004 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b90004 ["INT_ADD", "register:40f0:8", ["const:b90004:8", "const:4:8"]]
+ 00b90004 ["CALLIND", null, ["register:0:8"]]
- 00b8ffc0 bytes 00013fd6
+ 00b90004 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06819bf8819b02a0458803a0e500dc2f"></a>

### [`00b902e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902e4.md) → [`00b90328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md) FUN_00b90328

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b902dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902dc.md) · 呼出先 6件 [`00bb9b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1570.md)
- 新版 呼出元 1件 [`00b90320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90320.md) · 呼出先 6件 [`00bb9ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ba0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b90330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902e4.md#insn-00b90330) · [`00b9034c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902e4.md#insn-00b9034c) · [`00b903cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902e4.md#insn-00b903cc)
- 新版 [`00b90374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md#insn-00b90374) · [`00b90390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md#insn-00b90390) · [`00b90410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md#insn-00b90410)

~~~diff
- 00b90330 ["INT_ADD", "register:40f0:8", ["const:b90330:8", "const:4:8"]]
- 00b90330 ["CALL", null, ["callee:00be15c0:8"]]
+ 00b90374 ["INT_ADD", "register:40f0:8", ["const:b90374:8", "const:4:8"]]
+ 00b90374 ["CALL", null, ["callee:00be15c0:8"]]
- 00b90330 bytes 90440194
+ 00b90374 bytes 93440194
- 00b9034c ["INT_ADD", "register:40f0:8", ["const:b9034c:8", "const:4:8"]]
- 00b9034c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b90390 ["INT_ADD", "register:40f0:8", ["const:b90390:8", "const:4:8"]]
+ 00b90390 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b9034c bytes 093b0194
+ 00b90390 bytes 0c3b0194
- 00b903cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b903cc ["INT_ADD", "register:40f0:8", ["const:b903cc:8", "const:4:8"]]
- 00b903cc ["CALLIND", null, ["register:0:8"]]
+ 00b90410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b90410 ["INT_ADD", "register:40f0:8", ["const:b90410:8", "const:4:8"]]
+ 00b90410 ["CALLIND", null, ["register:0:8"]]
- 00b903cc bytes 00013fd6
+ 00b90410 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a6c22c198601b930c2ed66defa9912"></a>

### [`00b906f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b906f0.md) → [`00b90734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md) FUN_00b90734

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b906e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b906e8.md) · 呼出先 6件 [`00bb9c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1570.md)
- 新版 呼出元 1件 [`00b9072c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b9072c.md) · 呼出先 6件 [`00bb9cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9cb8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9073c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b906f0.md#insn-00b9073c) · [`00b90758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b906f0.md#insn-00b90758) · [`00b907d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b906f0.md#insn-00b907d8)
- 新版 [`00b90780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md#insn-00b90780) · [`00b9079c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md#insn-00b9079c) · [`00b9081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md#insn-00b9081c)

~~~diff
- 00b9073c ["INT_ADD", "register:40f0:8", ["const:b9073c:8", "const:4:8"]]
- 00b9073c ["CALL", null, ["callee:00be15c0:8"]]
+ 00b90780 ["INT_ADD", "register:40f0:8", ["const:b90780:8", "const:4:8"]]
+ 00b90780 ["CALL", null, ["callee:00be15c0:8"]]
- 00b9073c bytes 8d430194
+ 00b90780 bytes 90430194
- 00b90758 ["INT_ADD", "register:40f0:8", ["const:b90758:8", "const:4:8"]]
- 00b90758 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b9079c ["INT_ADD", "register:40f0:8", ["const:b9079c:8", "const:4:8"]]
+ 00b9079c ["CALL", null, ["callee:00bdefc0:8"]]
- 00b90758 bytes 063a0194
+ 00b9079c bytes 093a0194
- 00b907d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b907d8 ["INT_ADD", "register:40f0:8", ["const:b907d8:8", "const:4:8"]]
- 00b907d8 ["CALLIND", null, ["register:0:8"]]
+ 00b9081c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9081c ["INT_ADD", "register:40f0:8", ["const:b9081c:8", "const:4:8"]]
+ 00b9081c ["CALLIND", null, ["register:0:8"]]
- 00b907d8 bytes 00013fd6
+ 00b9081c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-479bf2590ffa77c2f7b85d38c0bc1a97"></a>

### [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) → [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) FUN_00b93334

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`00b91ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91ecc.md) [`00b92118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92118.md) [`00b92364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92364.md) [`00b92594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92594.md) [`00b927c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md) · 呼出先 2件 [`00bde280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde280.md) [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md)
- 新版 呼出元 14件 [`00b91f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f10.md) [`00b9215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9215c.md) [`00b923a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b923a8.md) [`00b925d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md) [`00b92808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md) · 呼出先 2件 [`00bde2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2d0.md) [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b93358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md#insn-00b93358) · [`00b93378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md#insn-00b93378) · [`00b93388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md#insn-00b93388)
- 新版 [`00b9339c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md#insn-00b9339c) · [`00b933bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md#insn-00b933bc) · [`00b933cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md#insn-00b933cc)

~~~diff
- 00b93358 ["INT_ADD", "register:40f0:8", ["const:b93358:8", "const:4:8"]]
- 00b93358 ["CALL", null, ["callee:00be1580:8"]]
+ 00b9339c ["INT_ADD", "register:40f0:8", ["const:b9339c:8", "const:4:8"]]
+ 00b9339c ["CALL", null, ["callee:00be1580:8"]]
- 00b93358 bytes 76380194
+ 00b9339c bytes 79380194
- 00b93378 ["INT_ADD", "register:40f0:8", ["const:b93378:8", "const:4:8"]]
- 00b93378 ["CALL", null, ["callee:00bde2d0:8"]]
+ 00b933bc ["INT_ADD", "register:40f0:8", ["const:b933bc:8", "const:4:8"]]
+ 00b933bc ["CALL", null, ["callee:00bde2d0:8"]]
- 00b93378 bytes c22b0194
+ 00b933bc bytes c52b0194
- 00b93388 ["INT_ADD", "register:40f0:8", ["const:b93388:8", "const:4:8"]]
- 00b93388 ["CALL", null, ["callee:00be1580:8"]]
+ 00b933cc ["INT_ADD", "register:40f0:8", ["const:b933cc:8", "const:4:8"]]
+ 00b933cc ["CALL", null, ["callee:00be1580:8"]]
- 00b93388 bytes 6a380194
+ 00b933cc bytes 6d380194
~~~


<a id="compare-64cb90600438f0ef96988e373423cafe"></a>

### [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) → [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) FUN_00b94a74

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`00b93600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93600.md) [`00b9384c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b9384c.md) [`00b93a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93a98.md) [`00b93cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93cc8.md) [`00b93ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 9件 [`00b93644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93644.md) [`00b93890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93890.md) [`00b93adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93adc.md) [`00b93d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93d0c.md) [`00b93f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b94a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md#insn-00b94a9c) · [`00b94b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md#insn-00b94b00) · [`00b94b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md#insn-00b94b88)
- 新版 [`00b94ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md#insn-00b94ae0) · [`00b94b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md#insn-00b94b44) · [`00b94bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md#insn-00b94bcc)

~~~diff
- 00b94a9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b94a9c ["INT_ADD", "register:40f0:8", ["const:b94a9c:8", "const:4:8"]]
- 00b94a9c ["CALLIND", null, ["register:0:8"]]
+ 00b94ae0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b94ae0 ["INT_ADD", "register:40f0:8", ["const:b94ae0:8", "const:4:8"]]
+ 00b94ae0 ["CALLIND", null, ["register:0:8"]]
- 00b94a9c bytes 00013fd6
+ 00b94ae0 bytes 00013fd6
- 00b94b00 ["INT_ADD", "register:40f0:8", ["const:b94b00:8", "const:4:8"]]
- 00b94b00 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b94b44 ["INT_ADD", "register:40f0:8", ["const:b94b44:8", "const:4:8"]]
+ 00b94b44 ["CALL", null, ["callee:00bdb040:8"]]
- 00b94b00 bytes 3c190194
+ 00b94b44 bytes 3f190194
- 00b94b88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b94b88 ["INT_ADD", "register:40f0:8", ["const:b94b88:8", "const:4:8"]]
- 00b94b88 ["CALLIND", null, ["register:0:8"]]
+ 00b94bcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b94bcc ["INT_ADD", "register:40f0:8", ["const:b94bcc:8", "const:4:8"]]
+ 00b94bcc ["CALLIND", null, ["register:0:8"]]
- 00b94b88 bytes 00013fd6
+ 00b94bcc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe617eec635a2f2b0c7531324ebd525f"></a>

### [`00b964f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b964f4.md) → [`00b96538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96538.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b964f4.md#insn-00b96524)
- 新版 [`00b96568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96538.md#insn-00b96568)

~~~diff
- 00b96524 ["INT_ADD", "register:40f0:8", ["const:b96524:8", "const:4:8"]]
- 00b96524 ["CALL", null, ["callee:00bdd920:8"]]
+ 00b96568 ["INT_ADD", "register:40f0:8", ["const:b96568:8", "const:4:8"]]
+ 00b96568 ["CALL", null, ["callee:00bdd920:8"]]
- 00b96524 bytes eb1c0194
+ 00b96568 bytes ee1c0194
~~~


<a id="compare-35ec57640e69ed556370a9766f15ad41"></a>

### [`00b96538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96538.md) → [`00b9657c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9657c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96538.md#insn-00b96570)
- 新版 [`00b965b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9657c.md#insn-00b965b4)

~~~diff
- 00b96570 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b96570 ["INT_ADD", "register:40f0:8", ["const:b96570:8", "const:4:8"]]
- 00b96570 ["CALLIND", null, ["register:0:8"]]
+ 00b965b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b965b4 ["INT_ADD", "register:40f0:8", ["const:b965b4:8", "const:4:8"]]
+ 00b965b4 ["CALLIND", null, ["register:0:8"]]
- 00b96570 bytes 00013fd6
+ 00b965b4 bytes 00013fd6
~~~


<a id="compare-7626ff012135c9456a0ce8061a9e8a61"></a>

### [`00b9671c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md) → [`00b96760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md#insn-00b96750) · [`00b96774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md#insn-00b96774)
- 新版 [`00b96794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md#insn-00b96794) · [`00b967b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md#insn-00b967b8)

~~~diff
- 00b96750 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b96750 ["INT_ADD", "register:40f0:8", ["const:b96750:8", "const:4:8"]]
- 00b96750 ["CALLIND", null, ["register:0:8"]]
+ 00b96794 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b96794 ["INT_ADD", "register:40f0:8", ["const:b96794:8", "const:4:8"]]
+ 00b96794 ["CALLIND", null, ["register:0:8"]]
- 00b96750 bytes 00013fd6
+ 00b96794 bytes 00013fd6
- 00b96774 ["INT_ADD", "register:40f0:8", ["const:b96774:8", "const:4:8"]]
- 00b96774 ["CALL", null, ["callee:00b8aca8:8"]]
+ 00b967b8 ["INT_ADD", "register:40f0:8", ["const:b967b8:8", "const:4:8"]]
+ 00b967b8 ["CALL", null, ["callee:00b8aca8:8"]]
- 00b96774 bytes 3cd1ff97
+ 00b967b8 bytes 3cd1ff97
~~~


<a id="compare-c534d9d8c5918280e65b489ee3e1d47c"></a>

### [`00b96928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md) → [`00b9696c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9695c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md#insn-00b9695c) · [`00b96980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md#insn-00b96980)
- 新版 [`00b969a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md#insn-00b969a0) · [`00b969c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md#insn-00b969c4)

~~~diff
- 00b9695c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9695c ["INT_ADD", "register:40f0:8", ["const:b9695c:8", "const:4:8"]]
- 00b9695c ["CALLIND", null, ["register:0:8"]]
+ 00b969a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b969a0 ["INT_ADD", "register:40f0:8", ["const:b969a0:8", "const:4:8"]]
+ 00b969a0 ["CALLIND", null, ["register:0:8"]]
- 00b9695c bytes 00013fd6
+ 00b969a0 bytes 00013fd6
- 00b96980 ["INT_ADD", "register:40f0:8", ["const:b96980:8", "const:4:8"]]
- 00b96980 ["CALL", null, ["callee:00b8aca8:8"]]
+ 00b969c4 ["INT_ADD", "register:40f0:8", ["const:b969c4:8", "const:4:8"]]
+ 00b969c4 ["CALL", null, ["callee:00b8aca8:8"]]
- 00b96980 bytes b9d0ff97
+ 00b969c4 bytes b9d0ff97
~~~


<a id="compare-efe756c7ad49f63421dd163ec4391008"></a>

### [`00b96af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96af8.md) → [`00b96b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96b3c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96af8.md#insn-00b96b24)
- 新版 [`00b96b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96b3c.md#insn-00b96b68)

~~~diff
- 00b96b24 ["INT_ADD", "register:40f0:8", ["const:b96b24:8", "const:4:8"]]
- 00b96b24 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b96b68 ["INT_ADD", "register:40f0:8", ["const:b96b68:8", "const:4:8"]]
+ 00b96b68 ["CALL", null, ["callee:00b97a3c:8"]]
- 00b96b24 bytes b5030094
+ 00b96b68 bytes b5030094
~~~


<a id="compare-736ddcf6d7b8b0cbe39074f3ee90e4d3"></a>

### [`00b971e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b971e0.md) → [`00b97224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9720c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b971e0.md#insn-00b9720c)
- 新版 [`00b97250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md#insn-00b97250)

~~~diff
- 00b9720c ["INT_ADD", "register:40f0:8", ["const:b9720c:8", "const:4:8"]]
- 00b9720c ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b97250 ["INT_ADD", "register:40f0:8", ["const:b97250:8", "const:4:8"]]
+ 00b97250 ["CALL", null, ["callee:00b97a3c:8"]]
- 00b9720c bytes fb010094
+ 00b97250 bytes fb010094
~~~


<a id="compare-a4c02b77da0a7d26c9e826ca5000ebc9"></a>

### [`00b97244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97244.md) → [`00b97288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97288.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97244.md#insn-00b97270)
- 新版 [`00b972b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97288.md#insn-00b972b4)

~~~diff
- 00b97270 ["INT_ADD", "register:40f0:8", ["const:b97270:8", "const:4:8"]]
- 00b97270 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b972b4 ["INT_ADD", "register:40f0:8", ["const:b972b4:8", "const:4:8"]]
+ 00b972b4 ["CALL", null, ["callee:00b97a3c:8"]]
- 00b97270 bytes e2010094
+ 00b972b4 bytes e2010094
~~~


<a id="compare-f3f4ba3ca333b6fe48643c8416d89976"></a>

### [`00b972a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b972a4.md) → [`00b972e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b972e8.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b972d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b972a4.md#insn-00b972d0)
- 新版 [`00b97314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b972e8.md#insn-00b97314)

~~~diff
- 00b972d0 ["INT_ADD", "register:40f0:8", ["const:b972d0:8", "const:4:8"]]
- 00b972d0 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b97314 ["INT_ADD", "register:40f0:8", ["const:b97314:8", "const:4:8"]]
+ 00b97314 ["CALL", null, ["callee:00b97a3c:8"]]
- 00b972d0 bytes ca010094
+ 00b97314 bytes ca010094
~~~


<a id="compare-8bdaf7875ecbd263011633a8fccde07b"></a>

### [`00b97308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97308.md) → [`00b9734c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b9734c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97308.md#insn-00b97334)
- 新版 [`00b97378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b9734c.md#insn-00b97378)

~~~diff
- 00b97334 ["INT_ADD", "register:40f0:8", ["const:b97334:8", "const:4:8"]]
- 00b97334 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b97378 ["INT_ADD", "register:40f0:8", ["const:b97378:8", "const:4:8"]]
+ 00b97378 ["CALL", null, ["callee:00b97a3c:8"]]
- 00b97334 bytes b1010094
+ 00b97378 bytes b1010094
~~~


<a id="compare-9c3be0468747d4c84f8ad8b8d1c4f921"></a>

### [`00b97368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97368.md) → [`00b973ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b973ac.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97368.md#insn-00b97394)
- 新版 [`00b973d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b973ac.md#insn-00b973d8)

~~~diff
- 00b97394 ["INT_ADD", "register:40f0:8", ["const:b97394:8", "const:4:8"]]
- 00b97394 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b973d8 ["INT_ADD", "register:40f0:8", ["const:b973d8:8", "const:4:8"]]
+ 00b973d8 ["CALL", null, ["callee:00b97a3c:8"]]
- 00b97394 bytes 99010094
+ 00b973d8 bytes 99010094
~~~


<a id="compare-491e24f74114ecf163c4251c88e939ab"></a>

### [`00b973cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b973cc.md) → [`00b97410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97410.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b973f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b973cc.md#insn-00b973f8)
- 新版 [`00b9743c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97410.md#insn-00b9743c)

~~~diff
- 00b973f8 ["INT_ADD", "register:40f0:8", ["const:b973f8:8", "const:4:8"]]
- 00b973f8 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b9743c ["INT_ADD", "register:40f0:8", ["const:b9743c:8", "const:4:8"]]
+ 00b9743c ["CALL", null, ["callee:00b97a3c:8"]]
- 00b973f8 bytes 80010094
+ 00b9743c bytes 80010094
~~~


<a id="compare-0e6a7d8606b81258548647ae4b44110f"></a>

### [`00b9742c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md) → [`00b97470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be15d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1620.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md#insn-00b97490) · [`00b974e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md#insn-00b974e4) · [`00b97524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9742c.md#insn-00b97524)
- 新版 [`00b974d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md#insn-00b974d4) · [`00b97528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md#insn-00b97528) · [`00b97568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md#insn-00b97568)

~~~diff
- 00b97490 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97490 ["INT_ADD", "register:40f0:8", ["const:b97490:8", "const:4:8"]]
- 00b97490 ["CALLIND", null, ["register:0:8"]]
+ 00b974d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b974d4 ["INT_ADD", "register:40f0:8", ["const:b974d4:8", "const:4:8"]]
+ 00b974d4 ["CALLIND", null, ["register:0:8"]]
- 00b97490 bytes 00013fd6
+ 00b974d4 bytes 00013fd6
- 00b974e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b974e4 ["INT_ADD", "register:40f0:8", ["const:b974e4:8", "const:4:8"]]
- 00b974e4 ["CALLIND", null, ["register:0:8"]]
+ 00b97528 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97528 ["INT_ADD", "register:40f0:8", ["const:b97528:8", "const:4:8"]]
+ 00b97528 ["CALLIND", null, ["register:0:8"]]
- 00b974e4 bytes 00013fd6
+ 00b97528 bytes 00013fd6
- 00b97524 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97524 ["INT_ADD", "register:40f0:8", ["const:b97524:8", "const:4:8"]]
- 00b97524 ["CALLIND", null, ["register:0:8"]]
+ 00b97568 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97568 ["INT_ADD", "register:40f0:8", ["const:b97568:8", "const:4:8"]]
+ 00b97568 ["CALLIND", null, ["register:0:8"]]
- 00b97524 bytes 00013fd6
+ 00b97568 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfaa82b386b4ee6a19dfccbd82ff030f"></a>

### [`00b97614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97614.md) → [`00b97658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97658.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97614.md#insn-00b97648) · [`00b976ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97614.md#insn-00b976ac)
- 新版 [`00b9768c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97658.md#insn-00b9768c) · [`00b976f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97658.md#insn-00b976f0)

~~~diff
- 00b97648 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97648 ["INT_ADD", "register:40f0:8", ["const:b97648:8", "const:4:8"]]
- 00b97648 ["CALLIND", null, ["register:0:8"]]
+ 00b9768c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9768c ["INT_ADD", "register:40f0:8", ["const:b9768c:8", "const:4:8"]]
+ 00b9768c ["CALLIND", null, ["register:0:8"]]
- 00b97648 bytes 00013fd6
+ 00b9768c bytes 00013fd6
- 00b976ac ["INT_ADD", "register:40f0:8", ["const:b976ac:8", "const:4:8"]]
- 00b976ac ["CALL", null, ["callee:00b8aca8:8"]]
+ 00b976f0 ["INT_ADD", "register:40f0:8", ["const:b976f0:8", "const:4:8"]]
+ 00b976f0 ["CALL", null, ["callee:00b8aca8:8"]]
- 00b976ac bytes 6ecdff97
+ 00b976f0 bytes 6ecdff97
~~~


<a id="compare-bd720d0a246182e1be6f646eda387bc2"></a>

### [`00b976fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b976fc.md) → [`00b97740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97740.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b976fc.md#insn-00b97728)
- 新版 [`00b9776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97740.md#insn-00b9776c)

~~~diff
- 00b97728 ["INT_ADD", "register:40f0:8", ["const:b97728:8", "const:4:8"]]
- 00b97728 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b9776c ["INT_ADD", "register:40f0:8", ["const:b9776c:8", "const:4:8"]]
+ 00b9776c ["CALL", null, ["callee:00b97a3c:8"]]
- 00b97728 bytes b4000094
+ 00b9776c bytes b4000094
~~~


<a id="compare-cdc55d72e0bb79b84718b35e6cf0138b"></a>

### [`00b9775c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9775c.md) → [`00b977a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b977a0.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9775c.md#insn-00b97788)
- 新版 [`00b977cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b977a0.md#insn-00b977cc)

~~~diff
- 00b97788 ["INT_ADD", "register:40f0:8", ["const:b97788:8", "const:4:8"]]
- 00b97788 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b977cc ["INT_ADD", "register:40f0:8", ["const:b977cc:8", "const:4:8"]]
+ 00b977cc ["CALL", null, ["callee:00b97a3c:8"]]
- 00b97788 bytes 9c000094
+ 00b977cc bytes 9c000094
~~~


<a id="compare-268373a0152c1fe2f83561bc636e060b"></a>

### [`00b977bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b977bc.md) → [`00b97800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97800.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b977e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b977bc.md#insn-00b977e8)
- 新版 [`00b9782c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97800.md#insn-00b9782c)

~~~diff
- 00b977e8 ["INT_ADD", "register:40f0:8", ["const:b977e8:8", "const:4:8"]]
- 00b977e8 ["CALL", null, ["callee:00b97a3c:8"]]
+ 00b9782c ["INT_ADD", "register:40f0:8", ["const:b9782c:8", "const:4:8"]]
+ 00b9782c ["CALL", null, ["callee:00b97a3c:8"]]
- 00b977e8 bytes 84000094
+ 00b9782c bytes 84000094
~~~


<a id="compare-016ed03214e5e1fd94e8bb9ce0ce195b"></a>

### [`00b9780c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md) → [`00b97850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be15e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1630.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md#insn-00b97864) · [`00b978c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md#insn-00b978c4) · [`00b978ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b9780c.md#insn-00b978ec)
- 新版 [`00b978a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md#insn-00b978a8) · [`00b97908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md#insn-00b97908) · [`00b97930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md#insn-00b97930)

~~~diff
- 00b97864 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97864 ["INT_ADD", "register:40f0:8", ["const:b97864:8", "const:4:8"]]
- 00b97864 ["CALLIND", null, ["register:0:8"]]
+ 00b978a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b978a8 ["INT_ADD", "register:40f0:8", ["const:b978a8:8", "const:4:8"]]
+ 00b978a8 ["CALLIND", null, ["register:0:8"]]
- 00b97864 bytes 00013fd6
+ 00b978a8 bytes 00013fd6
- 00b978c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b978c4 ["INT_ADD", "register:40f0:8", ["const:b978c4:8", "const:4:8"]]
- 00b978c4 ["CALLIND", null, ["register:0:8"]]
+ 00b97908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97908 ["INT_ADD", "register:40f0:8", ["const:b97908:8", "const:4:8"]]
+ 00b97908 ["CALLIND", null, ["register:0:8"]]
- 00b978c4 bytes 00013fd6
+ 00b97908 bytes 00013fd6
- 00b978ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b978ec ["INT_ADD", "register:40f0:8", ["const:b978ec:8", "const:4:8"]]
- 00b978ec ["CALLIND", null, ["register:0:8"]]
+ 00b97930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97930 ["INT_ADD", "register:40f0:8", ["const:b97930:8", "const:4:8"]]
+ 00b97930 ["CALLIND", null, ["register:0:8"]]
- 00b978ec bytes 00013fd6
+ 00b97930 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-946147339c690004f5335882bbbe27b9"></a>

### [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md) → [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md) FUN_00b97a3c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`00b969dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b969dc.md) [`00b96af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96af8.md) [`00b96b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96b60.md) [`00b971e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b971e0.md) [`00b97244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97244.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00b96a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96a20.md) [`00b96b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96b3c.md) [`00b96ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96ba4.md) [`00b97224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md) [`00b97288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97288.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md#insn-00b97a50) · [`00b97abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md#insn-00b97abc) · [`00b97ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md#insn-00b97ae8)
- 新版 [`00b97a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md#insn-00b97a94) · [`00b97b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md#insn-00b97b00) · [`00b97b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md#insn-00b97b2c)

~~~diff
- 00b97a50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97a50 ["INT_ADD", "register:40f0:8", ["const:b97a50:8", "const:4:8"]]
- 00b97a50 ["CALLIND", null, ["register:0:8"]]
+ 00b97a94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97a94 ["INT_ADD", "register:40f0:8", ["const:b97a94:8", "const:4:8"]]
+ 00b97a94 ["CALLIND", null, ["register:0:8"]]
- 00b97a50 bytes 00013fd6
+ 00b97a94 bytes 00013fd6
- 00b97abc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97abc ["INT_ADD", "register:40f0:8", ["const:b97abc:8", "const:4:8"]]
- 00b97abc ["CALLIND", null, ["register:0:8"]]
+ 00b97b00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97b00 ["INT_ADD", "register:40f0:8", ["const:b97b00:8", "const:4:8"]]
+ 00b97b00 ["CALLIND", null, ["register:0:8"]]
- 00b97abc bytes 00013fd6
+ 00b97b00 bytes 00013fd6
- 00b97ae8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97ae8 ["INT_ADD", "register:40f0:8", ["const:b97ae8:8", "const:4:8"]]
- 00b97ae8 ["CALLIND", null, ["register:0:8"]]
+ 00b97b2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b97b2c ["INT_ADD", "register:40f0:8", ["const:b97b2c:8", "const:4:8"]]
+ 00b97b2c ["CALLIND", null, ["register:0:8"]]
- 00b97ae8 bytes 00013fd6
+ 00b97b2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a2a0c9d173ed4861eb79611fe015457"></a>

### [`00b9823c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9823c.md) → [`00b98280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98280.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be15f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9823c.md#insn-00b98268)
- 新版 [`00b982ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98280.md#insn-00b982ac)

~~~diff
- 00b98268 ["INT_ADD", "register:40f0:8", ["const:b98268:8", "const:4:8"]]
- 00b98268 ["CALL", null, ["callee:00be1640:8"]]
+ 00b982ac ["INT_ADD", "register:40f0:8", ["const:b982ac:8", "const:4:8"]]
+ 00b982ac ["CALL", null, ["callee:00be1640:8"]]
- 00b98268 bytes e2240194
+ 00b982ac bytes e5240194
~~~


<a id="compare-1e2814a62ff0c4e9826b142dd6ff39cc"></a>

### [`00b9827c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9827c.md) → [`00b982c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b982c0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be15f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b982b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9827c.md#insn-00b982b4)
- 新版 [`00b982f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b982c0.md#insn-00b982f8)

~~~diff
- 00b982b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b982b4 ["INT_ADD", "register:40f0:8", ["const:b982b4:8", "const:4:8"]]
- 00b982b4 ["CALLIND", null, ["register:0:8"]]
+ 00b982f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b982f8 ["INT_ADD", "register:40f0:8", ["const:b982f8:8", "const:4:8"]]
+ 00b982f8 ["CALLIND", null, ["register:0:8"]]
- 00b982b4 bytes 00013fd6
+ 00b982f8 bytes 00013fd6
~~~


<a id="compare-2664b5ec0fc12a4d4b8abfe5033aa704"></a>

### [`00b98464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98464.md) → [`00b984a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98464.md#insn-00b98498) · [`00b984bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98464.md#insn-00b984bc)
- 新版 [`00b984dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md#insn-00b984dc) · [`00b98500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md#insn-00b98500)

~~~diff
- 00b98498 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b98498 ["INT_ADD", "register:40f0:8", ["const:b98498:8", "const:4:8"]]
- 00b98498 ["CALLIND", null, ["register:0:8"]]
+ 00b984dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b984dc ["INT_ADD", "register:40f0:8", ["const:b984dc:8", "const:4:8"]]
+ 00b984dc ["CALLIND", null, ["register:0:8"]]
- 00b98498 bytes 00013fd6
+ 00b984dc bytes 00013fd6
- 00b984bc ["INT_ADD", "register:40f0:8", ["const:b984bc:8", "const:4:8"]]
- 00b984bc ["CALL", null, ["callee:00b8e180:8"]]
+ 00b98500 ["INT_ADD", "register:40f0:8", ["const:b98500:8", "const:4:8"]]
+ 00b98500 ["CALL", null, ["callee:00b8e180:8"]]
- 00b984bc bytes 20d7ff97
+ 00b98500 bytes 20d7ff97
~~~


<a id="compare-094bbe1d53436ad6c64f5cbdf17cdc02"></a>

### [`00b98670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98670.md) → [`00b986b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b986a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98670.md#insn-00b986a4) · [`00b986c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98670.md#insn-00b986c8)
- 新版 [`00b986e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md#insn-00b986e8) · [`00b9870c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md#insn-00b9870c)

~~~diff
- 00b986a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b986a4 ["INT_ADD", "register:40f0:8", ["const:b986a4:8", "const:4:8"]]
- 00b986a4 ["CALLIND", null, ["register:0:8"]]
+ 00b986e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b986e8 ["INT_ADD", "register:40f0:8", ["const:b986e8:8", "const:4:8"]]
+ 00b986e8 ["CALLIND", null, ["register:0:8"]]
- 00b986a4 bytes 00013fd6
+ 00b986e8 bytes 00013fd6
- 00b986c8 ["INT_ADD", "register:40f0:8", ["const:b986c8:8", "const:4:8"]]
- 00b986c8 ["CALL", null, ["callee:00b8e180:8"]]
+ 00b9870c ["INT_ADD", "register:40f0:8", ["const:b9870c:8", "const:4:8"]]
+ 00b9870c ["CALL", null, ["callee:00b8e180:8"]]
- 00b986c8 bytes 9dd6ff97
+ 00b9870c bytes 9dd6ff97
~~~


<a id="compare-eb7f1ba63db565da40cb910a4171a574"></a>

### [`00b98840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98840.md) → [`00b98884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98884.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98840.md#insn-00b9886c)
- 新版 [`00b988b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98884.md#insn-00b988b0)

~~~diff
- 00b9886c ["INT_ADD", "register:40f0:8", ["const:b9886c:8", "const:4:8"]]
- 00b9886c ["CALL", null, ["callee:00b99780:8"]]
+ 00b988b0 ["INT_ADD", "register:40f0:8", ["const:b988b0:8", "const:4:8"]]
+ 00b988b0 ["CALL", null, ["callee:00b99780:8"]]
- 00b9886c bytes b4030094
+ 00b988b0 bytes b4030094
~~~


<a id="compare-84f5f5472f07307c18f6b8825f5c7ccc"></a>

### [`00b98f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f18.md) → [`00b98f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98f5c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f18.md#insn-00b98f44)
- 新版 [`00b98f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98f5c.md#insn-00b98f88)

~~~diff
- 00b98f44 ["INT_ADD", "register:40f0:8", ["const:b98f44:8", "const:4:8"]]
- 00b98f44 ["CALL", null, ["callee:00b99780:8"]]
+ 00b98f88 ["INT_ADD", "register:40f0:8", ["const:b98f88:8", "const:4:8"]]
+ 00b98f88 ["CALL", null, ["callee:00b99780:8"]]
- 00b98f44 bytes fe010094
+ 00b98f88 bytes fe010094
~~~


<a id="compare-5c634071ec11be5df9cca019b5a503be"></a>

### [`00b98f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f7c.md) → [`00b98fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f7c.md#insn-00b98fa8)
- 新版 [`00b98fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md#insn-00b98fec)

~~~diff
- 00b98fa8 ["INT_ADD", "register:40f0:8", ["const:b98fa8:8", "const:4:8"]]
- 00b98fa8 ["CALL", null, ["callee:00b99780:8"]]
+ 00b98fec ["INT_ADD", "register:40f0:8", ["const:b98fec:8", "const:4:8"]]
+ 00b98fec ["CALL", null, ["callee:00b99780:8"]]
- 00b98fa8 bytes e5010094
+ 00b98fec bytes e5010094
~~~


<a id="compare-fb496d4a319a67de03017b8fa0b7809d"></a>

### [`00b98fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98fdc.md) → [`00b99020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99020.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98fdc.md#insn-00b99008)
- 新版 [`00b9904c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99020.md#insn-00b9904c)

~~~diff
- 00b99008 ["INT_ADD", "register:40f0:8", ["const:b99008:8", "const:4:8"]]
- 00b99008 ["CALL", null, ["callee:00b99780:8"]]
+ 00b9904c ["INT_ADD", "register:40f0:8", ["const:b9904c:8", "const:4:8"]]
+ 00b9904c ["CALL", null, ["callee:00b99780:8"]]
- 00b99008 bytes cd010094
+ 00b9904c bytes cd010094
~~~


<a id="compare-2a467912aad29ddd7ed438af0894676d"></a>

### [`00b99040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99040.md) → [`00b99084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99084.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9906c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99040.md#insn-00b9906c)
- 新版 [`00b990b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99084.md#insn-00b990b0)

~~~diff
- 00b9906c ["INT_ADD", "register:40f0:8", ["const:b9906c:8", "const:4:8"]]
- 00b9906c ["CALL", null, ["callee:00b99780:8"]]
+ 00b990b0 ["INT_ADD", "register:40f0:8", ["const:b990b0:8", "const:4:8"]]
+ 00b990b0 ["CALL", null, ["callee:00b99780:8"]]
- 00b9906c bytes b4010094
+ 00b990b0 bytes b4010094
~~~


<a id="compare-5e7974dd020e1989c2daef66b47b3177"></a>

### [`00b990a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b990a0.md) → [`00b990e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b990e4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b990cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b990a0.md#insn-00b990cc)
- 新版 [`00b99110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b990e4.md#insn-00b99110)

~~~diff
- 00b990cc ["INT_ADD", "register:40f0:8", ["const:b990cc:8", "const:4:8"]]
- 00b990cc ["CALL", null, ["callee:00b99780:8"]]
+ 00b99110 ["INT_ADD", "register:40f0:8", ["const:b99110:8", "const:4:8"]]
+ 00b99110 ["CALL", null, ["callee:00b99780:8"]]
- 00b990cc bytes 9c010094
+ 00b99110 bytes 9c010094
~~~


<a id="compare-06fb967a09ddd805e4f54e146779c837"></a>

### [`00b99104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99104.md) → [`00b99148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99148.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99104.md#insn-00b99130)
- 新版 [`00b99174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99148.md#insn-00b99174)

~~~diff
- 00b99130 ["INT_ADD", "register:40f0:8", ["const:b99130:8", "const:4:8"]]
- 00b99130 ["CALL", null, ["callee:00b99780:8"]]
+ 00b99174 ["INT_ADD", "register:40f0:8", ["const:b99174:8", "const:4:8"]]
+ 00b99174 ["CALL", null, ["callee:00b99780:8"]]
- 00b99130 bytes 83010094
+ 00b99174 bytes 83010094
~~~


<a id="compare-7f60b31ee54b3ca8c756b408c0a3eaa1"></a>

### [`00b99164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md) → [`00b991a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1600.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1650.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b991e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md#insn-00b991e0) · [`00b9921c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md#insn-00b9921c) · [`00b9925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99164.md#insn-00b9925c)
- 新版 [`00b99224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md#insn-00b99224) · [`00b99260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md#insn-00b99260) · [`00b992a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md#insn-00b992a0)

~~~diff
- 00b991e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b991e0 ["INT_ADD", "register:40f0:8", ["const:b991e0:8", "const:4:8"]]
- 00b991e0 ["CALLIND", null, ["register:0:8"]]
+ 00b99224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99224 ["INT_ADD", "register:40f0:8", ["const:b99224:8", "const:4:8"]]
+ 00b99224 ["CALLIND", null, ["register:0:8"]]
- 00b991e0 bytes 00013fd6
+ 00b99224 bytes 00013fd6
- 00b9921c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9921c ["INT_ADD", "register:40f0:8", ["const:b9921c:8", "const:4:8"]]
- 00b9921c ["CALLIND", null, ["register:0:8"]]
+ 00b99260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99260 ["INT_ADD", "register:40f0:8", ["const:b99260:8", "const:4:8"]]
+ 00b99260 ["CALLIND", null, ["register:0:8"]]
- 00b9921c bytes 00013fd6
+ 00b99260 bytes 00013fd6
- 00b9925c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9925c ["INT_ADD", "register:40f0:8", ["const:b9925c:8", "const:4:8"]]
- 00b9925c ["CALLIND", null, ["register:0:8"]]
+ 00b992a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b992a0 ["INT_ADD", "register:40f0:8", ["const:b992a0:8", "const:4:8"]]
+ 00b992a0 ["CALLIND", null, ["register:0:8"]]
- 00b9925c bytes 00013fd6
+ 00b992a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3740776dc82b478819786127a421b2"></a>

### [`00b99354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99354.md) → [`00b99398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99398.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99354.md#insn-00b99388) · [`00b993ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99354.md#insn-00b993ec)
- 新版 [`00b993cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99398.md#insn-00b993cc) · [`00b99430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99398.md#insn-00b99430)

~~~diff
- 00b99388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99388 ["INT_ADD", "register:40f0:8", ["const:b99388:8", "const:4:8"]]
- 00b99388 ["CALLIND", null, ["register:0:8"]]
+ 00b993cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b993cc ["INT_ADD", "register:40f0:8", ["const:b993cc:8", "const:4:8"]]
+ 00b993cc ["CALLIND", null, ["register:0:8"]]
- 00b99388 bytes 00013fd6
+ 00b993cc bytes 00013fd6
- 00b993ec ["INT_ADD", "register:40f0:8", ["const:b993ec:8", "const:4:8"]]
- 00b993ec ["CALL", null, ["callee:00b8e180:8"]]
+ 00b99430 ["INT_ADD", "register:40f0:8", ["const:b99430:8", "const:4:8"]]
+ 00b99430 ["CALL", null, ["callee:00b8e180:8"]]
- 00b993ec bytes 54d3ff97
+ 00b99430 bytes 54d3ff97
~~~


<a id="compare-b39204332277821945e0d88d869eec5b"></a>

### [`00b9943c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9943c.md) → [`00b99480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99480.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9943c.md#insn-00b99468)
- 新版 [`00b994ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99480.md#insn-00b994ac)

~~~diff
- 00b99468 ["INT_ADD", "register:40f0:8", ["const:b99468:8", "const:4:8"]]
- 00b99468 ["CALL", null, ["callee:00b99780:8"]]
+ 00b994ac ["INT_ADD", "register:40f0:8", ["const:b994ac:8", "const:4:8"]]
+ 00b994ac ["CALL", null, ["callee:00b99780:8"]]
- 00b99468 bytes b5000094
+ 00b994ac bytes b5000094
~~~


<a id="compare-1d94dfbbeb614b97cef3d722d713d0b5"></a>

### [`00b9949c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9949c.md) → [`00b994e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b994e0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b994c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9949c.md#insn-00b994c8)
- 新版 [`00b9950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b994e0.md#insn-00b9950c)

~~~diff
- 00b994c8 ["INT_ADD", "register:40f0:8", ["const:b994c8:8", "const:4:8"]]
- 00b994c8 ["CALL", null, ["callee:00b99780:8"]]
+ 00b9950c ["INT_ADD", "register:40f0:8", ["const:b9950c:8", "const:4:8"]]
+ 00b9950c ["CALL", null, ["callee:00b99780:8"]]
- 00b994c8 bytes 9d000094
+ 00b9950c bytes 9d000094
~~~


<a id="compare-b5048db1c117a81f24c942857c168c7a"></a>

### [`00b994fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b994fc.md) → [`00b99540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99540.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b994fc.md#insn-00b99528)
- 新版 [`00b9956c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99540.md#insn-00b9956c)

~~~diff
- 00b99528 ["INT_ADD", "register:40f0:8", ["const:b99528:8", "const:4:8"]]
- 00b99528 ["CALL", null, ["callee:00b99780:8"]]
+ 00b9956c ["INT_ADD", "register:40f0:8", ["const:b9956c:8", "const:4:8"]]
+ 00b9956c ["CALL", null, ["callee:00b99780:8"]]
- 00b99528 bytes 85000094
+ 00b9956c bytes 85000094
~~~


<a id="compare-f0610833f04dfd58a97d4e867a8d0714"></a>

### [`00b9954c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md) → [`00b99590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1610.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1660.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b995b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md#insn-00b995b8) · [`00b995f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md#insn-00b995f0) · [`00b99630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9954c.md#insn-00b99630)
- 新版 [`00b995fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md#insn-00b995fc) · [`00b99634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md#insn-00b99634) · [`00b99674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md#insn-00b99674)

~~~diff
- 00b995b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b995b8 ["INT_ADD", "register:40f0:8", ["const:b995b8:8", "const:4:8"]]
- 00b995b8 ["CALLIND", null, ["register:0:8"]]
+ 00b995fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b995fc ["INT_ADD", "register:40f0:8", ["const:b995fc:8", "const:4:8"]]
+ 00b995fc ["CALLIND", null, ["register:0:8"]]
- 00b995b8 bytes 00013fd6
+ 00b995fc bytes 00013fd6
- 00b995f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b995f0 ["INT_ADD", "register:40f0:8", ["const:b995f0:8", "const:4:8"]]
- 00b995f0 ["CALLIND", null, ["register:0:8"]]
+ 00b99634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99634 ["INT_ADD", "register:40f0:8", ["const:b99634:8", "const:4:8"]]
+ 00b99634 ["CALLIND", null, ["register:0:8"]]
- 00b995f0 bytes 00013fd6
+ 00b99634 bytes 00013fd6
- 00b99630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99630 ["INT_ADD", "register:40f0:8", ["const:b99630:8", "const:4:8"]]
- 00b99630 ["CALLIND", null, ["register:0:8"]]
+ 00b99674 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99674 ["INT_ADD", "register:40f0:8", ["const:b99674:8", "const:4:8"]]
+ 00b99674 ["CALLIND", null, ["register:0:8"]]
- 00b99630 bytes 00013fd6
+ 00b99674 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fb95308164300d41ce1bdd0a155e524"></a>

### [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md) → [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md) FUN_00b99780

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`00b98724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98724.md) [`00b98840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98840.md) [`00b988a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b988a8.md) [`00b98f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f18.md) [`00b98f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98f7c.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00b98768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98768.md) [`00b98884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98884.md) [`00b988ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b988ec.md) [`00b98f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98f5c.md) [`00b98fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b997b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md#insn-00b997b0) · [`00b997e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md#insn-00b997e8) · [`00b9982c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md#insn-00b9982c)
- 新版 [`00b997f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md#insn-00b997f4) · [`00b9982c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md#insn-00b9982c) · [`00b99870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md#insn-00b99870)

~~~diff
- 00b997b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b997b0 ["INT_ADD", "register:40f0:8", ["const:b997b0:8", "const:4:8"]]
- 00b997b0 ["CALLIND", null, ["register:0:8"]]
+ 00b997f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b997f4 ["INT_ADD", "register:40f0:8", ["const:b997f4:8", "const:4:8"]]
+ 00b997f4 ["CALLIND", null, ["register:0:8"]]
- 00b997b0 bytes 00013fd6
+ 00b997f4 bytes 00013fd6
- 00b997e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b997e8 ["INT_ADD", "register:40f0:8", ["const:b997e8:8", "const:4:8"]]
- 00b997e8 ["CALLIND", null, ["register:0:8"]]
+ 00b9982c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9982c ["INT_ADD", "register:40f0:8", ["const:b9982c:8", "const:4:8"]]
+ 00b9982c ["CALLIND", null, ["register:0:8"]]
- 00b997e8 bytes 00013fd6
+ 00b9982c bytes 00013fd6
- 00b9982c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9982c ["INT_ADD", "register:40f0:8", ["const:b9982c:8", "const:4:8"]]
- 00b9982c ["CALLIND", null, ["register:0:8"]]
+ 00b99870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99870 ["INT_ADD", "register:40f0:8", ["const:b99870:8", "const:4:8"]]
+ 00b99870 ["CALLIND", null, ["register:0:8"]]
- 00b9982c bytes 00013fd6
+ 00b99870 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9d19b54d9bf8de37aede73636ad032"></a>

### [`00b99d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99d38.md) → [`00b99d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99d7c.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPK2tmcc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99d38.md#insn-00b99d8c) · [`00b99dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99d38.md#insn-00b99dac)
- 新版 [`00b99dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99d7c.md#insn-00b99dd0) · [`00b99df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99d7c.md#insn-00b99df0)

~~~diff
- 00b99d8c ["INT_ADD", "register:40f0:8", ["const:b99d8c:8", "const:4:8"]]
- 00b99d8c ["CALL", null, ["callee:00be1670:8"]]
+ 00b99dd0 ["INT_ADD", "register:40f0:8", ["const:b99dd0:8", "const:4:8"]]
+ 00b99dd0 ["CALL", null, ["callee:00be1670:8"]]
- 00b99d8c bytes 251e0194
+ 00b99dd0 bytes 281e0194
- 00b99dac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99dac ["INT_ADD", "register:40f0:8", ["const:b99dac:8", "const:4:8"]]
- 00b99dac ["CALLIND", null, ["register:0:8"]]
+ 00b99df0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b99df0 ["INT_ADD", "register:40f0:8", ["const:b99df0:8", "const:4:8"]]
+ 00b99df0 ["CALLIND", null, ["register:0:8"]]
- 00b99dac bytes 00013fd6
+ 00b99df0 bytes 00013fd6
~~~


<a id="compare-9e78a8b339fcf3fe2870e0365be9917d"></a>

### [`00b99e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e04.md) → [`00b99e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99e48.md) _ZNKSt6__ndk110__time_put8__do_putEPcRS1_PK2tmcc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e04.md#insn-00b99e58)
- 新版 [`00b99e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99e48.md#insn-00b99e9c)

~~~diff
- 00b99e58 ["INT_ADD", "register:40f0:8", ["const:b99e58:8", "const:4:8"]]
- 00b99e58 ["CALL", null, ["callee:00be1670:8"]]
+ 00b99e9c ["INT_ADD", "register:40f0:8", ["const:b99e9c:8", "const:4:8"]]
+ 00b99e9c ["CALL", null, ["callee:00be1670:8"]]
- 00b99e58 bytes f21d0194
+ 00b99e9c bytes f51d0194
~~~


<a id="compare-130addd5d8fa81236f0797e1b341a526"></a>

### [`00b9a128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a128.md) → [`00b9a16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a16c.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPK2tmcc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a128.md#insn-00b9a168) · [`00b9a1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a128.md#insn-00b9a1bc)
- 新版 [`00b9a1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a16c.md#insn-00b9a1ac) · [`00b9a200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a16c.md#insn-00b9a200)

~~~diff
- 00b9a168 ["INT_ADD", "register:40f0:8", ["const:b9a168:8", "const:4:8"]]
- 00b9a168 ["CALL", null, ["callee:00be1680:8"]]
+ 00b9a1ac ["INT_ADD", "register:40f0:8", ["const:b9a1ac:8", "const:4:8"]]
+ 00b9a1ac ["CALL", null, ["callee:00be1680:8"]]
- 00b9a168 bytes 321d0194
+ 00b9a1ac bytes 351d0194
- 00b9a1bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9a1bc ["INT_ADD", "register:40f0:8", ["const:b9a1bc:8", "const:4:8"]]
- 00b9a1bc ["CALLIND", null, ["register:0:8"]]
+ 00b9a200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9a200 ["INT_ADD", "register:40f0:8", ["const:b9a200:8", "const:4:8"]]
+ 00b9a200 ["CALLIND", null, ["register:0:8"]]
- 00b9a1bc bytes 00013fd6
+ 00b9a200 bytes 00013fd6
~~~


<a id="compare-b40b9791f9bcdf17345f48827c6d698b"></a>

### [`00b9a1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md) → [`00b9a228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md) _ZNKSt6__ndk110__time_put8__do_putEPwRS1_PK2tmcc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1630.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md) [`00be1640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1640.md)
- 新版 呼出元 1件 [`00be1680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1680.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1670.md) [`00be1690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1690.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md#insn-00b9a244) · [`00b9a25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md#insn-00b9a25c) · [`00b9a278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a1e4.md#insn-00b9a278)
- 新版 [`00b9a288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md#insn-00b9a288) · [`00b9a2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md#insn-00b9a2a0) · [`00b9a2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md#insn-00b9a2bc)

~~~diff
- 00b9a244 ["INT_ADD", "register:40f0:8", ["const:b9a244:8", "const:4:8"]]
- 00b9a244 ["CALL", null, ["callee:00be1670:8"]]
+ 00b9a288 ["INT_ADD", "register:40f0:8", ["const:b9a288:8", "const:4:8"]]
+ 00b9a288 ["CALL", null, ["callee:00be1670:8"]]
- 00b9a244 bytes f71c0194
+ 00b9a288 bytes fa1c0194
- 00b9a25c ["INT_ADD", "register:40f0:8", ["const:b9a25c:8", "const:4:8"]]
- 00b9a25c ["CALL", null, ["callee:00be1580:8"]]
+ 00b9a2a0 ["INT_ADD", "register:40f0:8", ["const:b9a2a0:8", "const:4:8"]]
+ 00b9a2a0 ["CALL", null, ["callee:00be1580:8"]]
- 00b9a25c bytes b51c0194
+ 00b9a2a0 bytes b81c0194
- 00b9a278 ["INT_ADD", "register:40f0:8", ["const:b9a278:8", "const:4:8"]]
- 00b9a278 ["CALL", null, ["callee:00be1690:8"]]
+ 00b9a2bc ["INT_ADD", "register:40f0:8", ["const:b9a2bc:8", "const:4:8"]]
+ 00b9a2bc ["CALL", null, ["callee:00be1690:8"]]
- 00b9a278 bytes f21c0194
+ 00b9a2bc bytes f51c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe19114547355ad237c9cb6cabfc0069"></a>

### [`00b9c110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md) → [`00b9c154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md) FUN_00b9c154

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9be50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9b/00b9be50.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00b9be94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md#insn-00b9c248) · [`00b9c268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md#insn-00b9c268) · [`00b9c2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md#insn-00b9c2c4)
- 新版 [`00b9c28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md#insn-00b9c28c) · [`00b9c2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md#insn-00b9c2ac) · [`00b9c308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md#insn-00b9c308)

~~~diff
- 00b9c248 ["INT_ADD", "register:40f0:8", ["const:b9c248:8", "const:4:8"]]
- 00b9c248 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b9c28c ["INT_ADD", "register:40f0:8", ["const:b9c28c:8", "const:4:8"]]
+ 00b9c28c ["CALL", null, ["callee:00bdb040:8"]]
- 00b9c248 bytes 6afb0094
+ 00b9c28c bytes 6dfb0094
- 00b9c268 ["INT_ADD", "register:40f0:8", ["const:b9c268:8", "const:4:8"]]
- 00b9c268 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b9c2ac ["INT_ADD", "register:40f0:8", ["const:b9c2ac:8", "const:4:8"]]
+ 00b9c2ac ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b9c268 bytes befb0094
+ 00b9c2ac bytes c1fb0094
- 00b9c2c4 ["INT_ADD", "register:40f0:8", ["const:b9c2c4:8", "const:4:8"]]
- 00b9c2c4 ["CALL", null, ["callee:00bde220:8"]]
+ 00b9c308 ["INT_ADD", "register:40f0:8", ["const:b9c308:8", "const:4:8"]]
+ 00b9c308 ["CALL", null, ["callee:00bde220:8"]]
- 00b9c2c4 bytes c3070194
+ 00b9c308 bytes c6070194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d0811a72056bf9231a3c1b6471d0f3a"></a>

### [`00b9e138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md) → [`00b9e17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md) FUN_00b9e17c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b9de0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9d/00b9de0c.md) · 呼出先 8件 [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00b9de50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9d/00b9de50.md) · 呼出先 8件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9e228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md#insn-00b9e228) · [`00b9e2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md#insn-00b9e2a4) · [`00b9e2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md#insn-00b9e2d4)
- 新版 [`00b9e26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md#insn-00b9e26c) · [`00b9e2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md#insn-00b9e2e8) · [`00b9e318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md#insn-00b9e318)

~~~diff
- 00b9e228 ["INT_ADD", "register:40f0:8", ["const:b9e228:8", "const:4:8"]]
- 00b9e228 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b9e26c ["INT_ADD", "register:40f0:8", ["const:b9e26c:8", "const:4:8"]]
+ 00b9e26c ["CALL", null, ["callee:00bdda50:8"]]
- 00b9e228 bytes f6fd0094
+ 00b9e26c bytes f9fd0094
- 00b9e2a4 ["INT_ADD", "register:40f0:8", ["const:b9e2a4:8", "const:4:8"]]
- 00b9e2a4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b9e2e8 ["INT_ADD", "register:40f0:8", ["const:b9e2e8:8", "const:4:8"]]
+ 00b9e2e8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b9e2a4 bytes 53f30094
+ 00b9e2e8 bytes 56f30094
- 00b9e2d4 ["INT_ADD", "register:40f0:8", ["const:b9e2d4:8", "const:4:8"]]
- 00b9e2d4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b9e318 ["INT_ADD", "register:40f0:8", ["const:b9e318:8", "const:4:8"]]
+ 00b9e318 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b9e2d4 bytes a3f30094
+ 00b9e318 bytes a6f30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a076e8260f9c14207cdcf7c29f769734"></a>

### [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) → [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) FUN_00b9eb70

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00b927c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md) [`00b92c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92c54.md) [`00b93ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md) [`00b94388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94388.md) [`00b9e680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e680.md) · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be16c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16c0.md)
- 新版 呼出元 6件 [`00b92808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md) [`00b92c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c98.md) [`00b93f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md) [`00b943cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943cc.md) [`00b9e6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e6c4.md) · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9eb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md#insn-00b9eb90) · [`00b9ebb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md#insn-00b9ebb0) · [`00b9ebc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md#insn-00b9ebc0)
- 新版 [`00b9ebd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md#insn-00b9ebd4) · [`00b9ebf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md#insn-00b9ebf4) · [`00b9ec04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md#insn-00b9ec04)

~~~diff
- 00b9eb90 ["INT_ADD", "register:40f0:8", ["const:b9eb90:8", "const:4:8"]]
- 00b9eb90 ["CALL", null, ["callee:00be1580:8"]]
+ 00b9ebd4 ["INT_ADD", "register:40f0:8", ["const:b9ebd4:8", "const:4:8"]]
+ 00b9ebd4 ["CALL", null, ["callee:00be1580:8"]]
- 00b9eb90 bytes 680a0194
+ 00b9ebd4 bytes 6b0a0194
- 00b9ebb0 ["INT_ADD", "register:40f0:8", ["const:b9ebb0:8", "const:4:8"]]
- 00b9ebb0 ["CALL", null, ["callee:00be1710:8"]]
+ 00b9ebf4 ["INT_ADD", "register:40f0:8", ["const:b9ebf4:8", "const:4:8"]]
+ 00b9ebf4 ["CALL", null, ["callee:00be1710:8"]]
- 00b9ebb0 bytes c40a0194
+ 00b9ebf4 bytes c70a0194
- 00b9ebc0 ["INT_ADD", "register:40f0:8", ["const:b9ebc0:8", "const:4:8"]]
- 00b9ebc0 ["CALL", null, ["callee:00be1580:8"]]
+ 00b9ec04 ["INT_ADD", "register:40f0:8", ["const:b9ec04:8", "const:4:8"]]
+ 00b9ec04 ["CALL", null, ["callee:00be1580:8"]]
- 00b9ebc0 bytes 5c0a0194
+ 00b9ec04 bytes 5f0a0194
~~~


<a id="compare-178b01c30b5350fc7eda0315eb1ab9d2"></a>

### [`00b9ee0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md) → [`00b9ee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md) _ZNSt6__ndk111__money_putIcE8__formatEPcRS2_S3_jPKcS5_RKNS_5ctypeIcEEbRKNS_10money_base7patternEccRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be16b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16b0.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be1700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1700.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md#insn-00b9efa8) · [`00b9f004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md#insn-00b9f004) · [`00b9f068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9ee0c.md#insn-00b9f068)
- 新版 [`00b9efec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md#insn-00b9efec) · [`00b9f048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md#insn-00b9f048) · [`00b9f0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md#insn-00b9f0ac)

~~~diff
- 00b9efa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9efa8 ["INT_ADD", "register:40f0:8", ["const:b9efa8:8", "const:4:8"]]
- 00b9efa8 ["CALLIND", null, ["register:0:8"]]
+ 00b9efec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9efec ["INT_ADD", "register:40f0:8", ["const:b9efec:8", "const:4:8"]]
+ 00b9efec ["CALLIND", null, ["register:0:8"]]
- 00b9efa8 bytes 00013fd6
+ 00b9efec bytes 00013fd6
- 00b9f004 ["INT_ADD", "register:40f0:8", ["const:b9f004:8", "const:4:8"]]
- 00b9f004 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b9f048 ["INT_ADD", "register:40f0:8", ["const:b9f048:8", "const:4:8"]]
+ 00b9f048 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b9f004 bytes 27f00094
+ 00b9f048 bytes 2af00094
- 00b9f068 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9f068 ["INT_ADD", "register:40f0:8", ["const:b9f068:8", "const:4:8"]]
- 00b9f068 ["CALLIND", null, ["register:0:8"]]
+ 00b9f0ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9f0ac ["INT_ADD", "register:40f0:8", ["const:b9f0ac:8", "const:4:8"]]
+ 00b9f0ac ["CALLIND", null, ["register:0:8"]]
- 00b9f068 bytes 00013fd6
+ 00b9f0ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed54c39b864d973e3924c3301d620c4f"></a>

### [`00b9fcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md) → [`00b9fd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md) _ZNSt6__ndk111__money_putIwE8__formatEPwRS2_S3_jPKwS5_RKNS_5ctypeIwEEbRKNS_10money_base7patternEwwRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be16e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16e0.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be1730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1730.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9fdd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md#insn-00b9fdd4) · [`00b9fe5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md#insn-00b9fe5c) · [`00b9feb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9fcc8.md#insn-00b9feb4)
- 新版 [`00b9fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md#insn-00b9fe18) · [`00b9fea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md#insn-00b9fea0) · [`00b9fef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md#insn-00b9fef8)

~~~diff
- 00b9fdd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9fdd4 ["INT_ADD", "register:40f0:8", ["const:b9fdd4:8", "const:4:8"]]
- 00b9fdd4 ["CALLIND", null, ["register:0:8"]]
+ 00b9fe18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9fe18 ["INT_ADD", "register:40f0:8", ["const:b9fe18:8", "const:4:8"]]
+ 00b9fe18 ["CALLIND", null, ["register:0:8"]]
- 00b9fdd4 bytes 00013fd6
+ 00b9fe18 bytes 00013fd6
- 00b9fe5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9fe5c ["INT_ADD", "register:40f0:8", ["const:b9fe5c:8", "const:4:8"]]
- 00b9fe5c ["CALLIND", null, ["register:0:8"]]
+ 00b9fea0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9fea0 ["INT_ADD", "register:40f0:8", ["const:b9fea0:8", "const:4:8"]]
+ 00b9fea0 ["CALLIND", null, ["register:0:8"]]
- 00b9fe5c bytes 00013fd6
+ 00b9fea0 bytes 00013fd6
- 00b9feb4 ["INT_ADD", "register:40f0:8", ["const:b9feb4:8", "const:4:8"]]
- 00b9feb4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b9fef8 ["INT_ADD", "register:40f0:8", ["const:b9fef8:8", "const:4:8"]]
+ 00b9fef8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b9feb4 bytes 7bec0094
+ 00b9fef8 bytes 7eec0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a173ad18a9ef1e3ad78a19395ccb6a6"></a>

### [`00ba057c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba057c.md) → [`00ba05c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05c0.md) _ZNSt6__ndk114codecvt_bynameIcc9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1700.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba057c.md#insn-00ba0590)
- 新版 [`00ba05d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05c0.md#insn-00ba05d4)

~~~diff
- 00ba0590 ["INT_ADD", "register:40f0:8", ["const:ba0590:8", "const:4:8"]]
- 00ba0590 ["CALL", null, ["callee:00be1750:8"]]
+ 00ba05d4 ["INT_ADD", "register:40f0:8", ["const:ba05d4:8", "const:4:8"]]
+ 00ba05d4 ["CALL", null, ["callee:00be1750:8"]]
- 00ba0590 bytes 5c040194
+ 00ba05d4 bytes 5f040194
~~~


<a id="compare-6fc684f43b3bf970803b3a2bf2cfe719"></a>

### [`00ba05b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05b0.md) → [`00ba05f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05f4.md) _ZNSt6__ndk114codecvt_bynameIwc9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1710.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba05c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05b0.md#insn-00ba05c4)
- 新版 [`00ba0608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05f4.md#insn-00ba0608)

~~~diff
- 00ba05c4 ["INT_ADD", "register:40f0:8", ["const:ba05c4:8", "const:4:8"]]
- 00ba05c4 ["CALL", null, ["callee:00be1760:8"]]
+ 00ba0608 ["INT_ADD", "register:40f0:8", ["const:ba0608:8", "const:4:8"]]
+ 00ba0608 ["CALL", null, ["callee:00be1760:8"]]
- 00ba05c4 bytes 53040194
+ 00ba0608 bytes 56040194
~~~


<a id="compare-f99293a6753283c317c356935b38290f"></a>

### [`00ba05e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05e4.md) → [`00ba0628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0628.md) _ZNSt6__ndk114codecvt_bynameIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1730.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba05f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba05e4.md#insn-00ba05f8)
- 新版 [`00ba063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0628.md#insn-00ba063c)

~~~diff
- 00ba05f8 ["INT_ADD", "register:40f0:8", ["const:ba05f8:8", "const:4:8"]]
- 00ba05f8 ["CALL", null, ["callee:00be1780:8"]]
+ 00ba063c ["INT_ADD", "register:40f0:8", ["const:ba063c:8", "const:4:8"]]
+ 00ba063c ["CALL", null, ["callee:00be1780:8"]]
- 00ba05f8 bytes 4e040194
+ 00ba063c bytes 51040194
~~~


<a id="compare-62f26f6cfad236db12acb51035011ce9"></a>

### [`00ba0618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0618.md) → [`00ba065c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba065c.md) _ZNSt6__ndk114codecvt_bynameIDic9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1750.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be17a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0618.md#insn-00ba062c)
- 新版 [`00ba0670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba065c.md#insn-00ba0670)

~~~diff
- 00ba062c ["INT_ADD", "register:40f0:8", ["const:ba062c:8", "const:4:8"]]
- 00ba062c ["CALL", null, ["callee:00be17a0:8"]]
+ 00ba0670 ["INT_ADD", "register:40f0:8", ["const:ba0670:8", "const:4:8"]]
+ 00ba0670 ["CALL", null, ["callee:00be17a0:8"]]
- 00ba062c bytes 49040194
+ 00ba0670 bytes 4c040194
~~~


<a id="compare-2e453474a1fe17bf0067febaec714eae"></a>

### [`00ba064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba064c.md) → [`00ba0690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0690.md) _ZNSt6__ndk114codecvt_bynameIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1770.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be17c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba064c.md#insn-00ba0660)
- 新版 [`00ba06a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0690.md#insn-00ba06a4)

~~~diff
- 00ba0660 ["INT_ADD", "register:40f0:8", ["const:ba0660:8", "const:4:8"]]
- 00ba0660 ["CALL", null, ["callee:00be17c0:8"]]
+ 00ba06a4 ["INT_ADD", "register:40f0:8", ["const:ba06a4:8", "const:4:8"]]
+ 00ba06a4 ["CALL", null, ["callee:00be17c0:8"]]
- 00ba0660 bytes 44040194
+ 00ba06a4 bytes 47040194
~~~


<a id="compare-44d92abe553c310d46f4f82c899c6f79"></a>

### [`00ba0680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0680.md) → [`00ba06c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06c4.md) _ZNSt6__ndk114codecvt_bynameIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1790.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be17e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0680.md#insn-00ba0694)
- 新版 [`00ba06d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06c4.md#insn-00ba06d8)

~~~diff
- 00ba0694 ["INT_ADD", "register:40f0:8", ["const:ba0694:8", "const:4:8"]]
- 00ba0694 ["CALL", null, ["callee:00be17e0:8"]]
+ 00ba06d8 ["INT_ADD", "register:40f0:8", ["const:ba06d8:8", "const:4:8"]]
+ 00ba06d8 ["CALL", null, ["callee:00be17e0:8"]]
- 00ba0694 bytes 3f040194
+ 00ba06d8 bytes 42040194
~~~


<a id="compare-e0be4ce1cd321d3bda57f2d74e2b0ab0"></a>

### [`00ba06ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md) → [`00ba06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md) FUN_00ba06f0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba079c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md#insn-00ba079c)
- 新版 [`00ba07e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md#insn-00ba07e0)

~~~diff
- 00ba079c ["INT_ADD", "register:40f0:8", ["const:ba079c:8", "const:4:8"]]
- 00ba079c ["CALL", null, ["callee:00bdb200:8"]]
+ 00ba07e0 ["INT_ADD", "register:40f0:8", ["const:ba07e0:8", "const:4:8"]]
+ 00ba07e0 ["CALL", null, ["callee:00bdb200:8"]]
- 00ba079c bytes 85ea0094
+ 00ba07e0 bytes 88ea0094
~~~


<a id="compare-b1025a9f79ef36f5aa0a007e89d2bb8d"></a>

### [`00ba7dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7dc8.md) → [`00ba7e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7e0c.md) FUN_00ba7e0c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00ba7cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7cf4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00ba7d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7d38.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba7ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7dc8.md#insn-00ba7ddc)
- 新版 [`00ba7e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7e0c.md#insn-00ba7e20)

~~~diff
- 00ba7ddc ["INT_ADD", "register:40f0:8", ["const:ba7ddc:8", "const:4:8"]]
- 00ba7ddc ["CALL", null, ["callee:00ba7d38:8"]]
+ 00ba7e20 ["INT_ADD", "register:40f0:8", ["const:ba7e20:8", "const:4:8"]]
+ 00ba7e20 ["CALL", null, ["callee:00ba7d38:8"]]
- 00ba7ddc bytes c6ffff97
+ 00ba7e20 bytes c6ffff97
~~~


<a id="compare-5d634cafe53749de9d0f0e15b1ea3b29"></a>

### [`00ba8180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8180.md) → [`00ba81c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md) _ZNSt6__ndk16localeC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba81a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8180.md#insn-00ba81a0) · [`00ba81b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8180.md#insn-00ba81b0) · [`00ba81c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8180.md#insn-00ba81c0)
- 新版 [`00ba81e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md#insn-00ba81e4) · [`00ba81f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md#insn-00ba81f4) · [`00ba8204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md#insn-00ba8204)

~~~diff
- 00ba81a0 ["INT_ADD", "register:40f0:8", ["const:ba81a0:8", "const:4:8"]]
- 00ba81a0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba81e4 ["INT_ADD", "register:40f0:8", ["const:ba81e4:8", "const:4:8"]]
+ 00ba81e4 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba81a0 bytes 94cb0094
+ 00ba81e4 bytes 97cb0094
- 00ba81b0 ["INT_ADD", "register:40f0:8", ["const:ba81b0:8", "const:4:8"]]
- 00ba81b0 ["CALL", null, ["callee:00ba261c:8"]]
+ 00ba81f4 ["INT_ADD", "register:40f0:8", ["const:ba81f4:8", "const:4:8"]]
+ 00ba81f4 ["CALL", null, ["callee:00ba261c:8"]]
- 00ba81b0 bytes 0ae9ff97
+ 00ba81f4 bytes 0ae9ff97
- 00ba81c0 ["INT_ADD", "register:40f0:8", ["const:ba81c0:8", "const:4:8"]]
- 00ba81c0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba8204 ["INT_ADD", "register:40f0:8", ["const:ba8204:8", "const:4:8"]]
+ 00ba8204 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba81c0 bytes 18bb0094
+ 00ba8204 bytes 17bb0094
~~~


<a id="compare-e7a43c8905292d257e35061cd82b3455"></a>

### [`00ba833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba833c.md) → [`00ba8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8380.md) _ZNSt6__ndk16localeC1ERKS0_RKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba833c.md#insn-00ba8364) · [`00ba8378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba833c.md#insn-00ba8378) · [`00ba8388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba833c.md#insn-00ba8388)
- 新版 [`00ba83a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8380.md#insn-00ba83a8) · [`00ba83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8380.md#insn-00ba83bc) · [`00ba83cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8380.md#insn-00ba83cc)

~~~diff
- 00ba8364 ["INT_ADD", "register:40f0:8", ["const:ba8364:8", "const:4:8"]]
- 00ba8364 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba83a8 ["INT_ADD", "register:40f0:8", ["const:ba83a8:8", "const:4:8"]]
+ 00ba83a8 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba8364 bytes 23cb0094
+ 00ba83a8 bytes 26cb0094
- 00ba8378 ["INT_ADD", "register:40f0:8", ["const:ba8378:8", "const:4:8"]]
- 00ba8378 ["CALL", null, ["callee:00ba4ab8:8"]]
+ 00ba83bc ["INT_ADD", "register:40f0:8", ["const:ba83bc:8", "const:4:8"]]
+ 00ba83bc ["CALL", null, ["callee:00ba4ab8:8"]]
- 00ba8378 bytes bff1ff97
+ 00ba83bc bytes bff1ff97
- 00ba8388 ["INT_ADD", "register:40f0:8", ["const:ba8388:8", "const:4:8"]]
- 00ba8388 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba83cc ["INT_ADD", "register:40f0:8", ["const:ba83cc:8", "const:4:8"]]
+ 00ba83cc ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba8388 bytes a6ba0094
+ 00ba83cc bytes a5ba0094
~~~


<a id="compare-8f376d7363d2c07c727ee7b1e1cf1ad7"></a>

### [`00ba83b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba83b4.md) → [`00ba83f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba83f8.md) _ZNSt6__ndk16localeC2ERKS0_S2_i

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba83dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba83b4.md#insn-00ba83dc) · [`00ba83f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba83b4.md#insn-00ba83f0) · [`00ba8400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba83b4.md#insn-00ba8400)
- 新版 [`00ba8420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba83f8.md#insn-00ba8420) · [`00ba8434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba83f8.md#insn-00ba8434) · [`00ba8444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba83f8.md#insn-00ba8444)

~~~diff
- 00ba83dc ["INT_ADD", "register:40f0:8", ["const:ba83dc:8", "const:4:8"]]
- 00ba83dc ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba8420 ["INT_ADD", "register:40f0:8", ["const:ba8420:8", "const:4:8"]]
+ 00ba8420 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba83dc bytes 05cb0094
+ 00ba8420 bytes 08cb0094
- 00ba83f0 ["INT_ADD", "register:40f0:8", ["const:ba83f0:8", "const:4:8"]]
- 00ba83f0 ["CALL", null, ["callee:00ba5108:8"]]
+ 00ba8434 ["INT_ADD", "register:40f0:8", ["const:ba8434:8", "const:4:8"]]
+ 00ba8434 ["CALL", null, ["callee:00ba5108:8"]]
- 00ba83f0 bytes 35f3ff97
+ 00ba8434 bytes 35f3ff97
- 00ba8400 ["INT_ADD", "register:40f0:8", ["const:ba8400:8", "const:4:8"]]
- 00ba8400 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba8444 ["INT_ADD", "register:40f0:8", ["const:ba8444:8", "const:4:8"]]
+ 00ba8444 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba8400 bytes 88ba0094
+ 00ba8444 bytes 87ba0094
~~~


<a id="compare-af5b01e582807c31a12410448609d430"></a>

### [`00ba887c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba887c.md) → [`00ba88c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba88c0.md) _ZNKSt6__ndk16localeeqERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba887c.md#insn-00ba8928)
- 新版 [`00ba896c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba88c0.md#insn-00ba896c)

~~~diff
- 00ba8928 ["INT_ADD", "register:40f0:8", ["const:ba8928:8", "const:4:8"]]
- 00ba8928 ["CALL", null, ["callee:00bdb200:8"]]
+ 00ba896c ["INT_ADD", "register:40f0:8", ["const:ba896c:8", "const:4:8"]]
+ 00ba896c ["CALL", null, ["callee:00bdb200:8"]]
- 00ba8928 bytes 22ca0094
+ 00ba896c bytes 25ca0094
~~~


<a id="compare-49e7fcff3366914647a377d2d65272f8"></a>

### [`00ba896c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba896c.md) → [`00ba89b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba89b0.md) _ZNSt6__ndk16locale5facetD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be18d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba896c.md#insn-00ba8980)
- 新版 [`00ba89c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba89b0.md#insn-00ba89c4)

~~~diff
- 00ba8980 ["INT_ADD", "register:40f0:8", ["const:ba8980:8", "const:4:8"]]
- 00ba8980 ["CALL", null, ["callee:00be1920:8"]]
+ 00ba89c4 ["INT_ADD", "register:40f0:8", ["const:ba89c4:8", "const:4:8"]]
+ 00ba89c4 ["CALL", null, ["callee:00be1920:8"]]
- 00ba8980 bytes d4e30094
+ 00ba89c4 bytes d7e30094
~~~


<a id="compare-6421f13808d2bd81504f316a00cfc458"></a>

### [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) → [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) FUN_00ba8ac4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`00ba89a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba89a8.md) [`00ba8fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8fec.md) [`00baa2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa2e4.md) [`00baa85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa85c.md) [`00bab3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 13件 [`00ba89ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba89ec.md) [`00ba9030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9030.md) [`00baa328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa328.md) [`00baa8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa8a0.md) [`00bab43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab43c.md) · 呼出先 2件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md#insn-00ba8aa0) · [`00ba8ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md#insn-00ba8ab4)
- 新版 [`00ba8ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md#insn-00ba8ae4) · [`00ba8af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md#insn-00ba8af8)

~~~diff
- 00ba8aa0 ["INT_ADD", "register:40f0:8", ["const:ba8aa0:8", "const:4:8"]]
- 00ba8aa0 ["CALL", null, ["callee:00bdb190:8"]]
+ 00ba8ae4 ["INT_ADD", "register:40f0:8", ["const:ba8ae4:8", "const:4:8"]]
+ 00ba8ae4 ["CALL", null, ["callee:00bdb190:8"]]
- 00ba8aa0 bytes a8c90094
+ 00ba8ae4 bytes abc90094
- 00ba8ab4 ["INT_ADD", "register:40f0:8", ["const:ba8ab4:8", "const:4:8"]]
- 00ba8ab4 ["CALL", null, ["callee:00bdc180:8"]]
+ 00ba8af8 ["INT_ADD", "register:40f0:8", ["const:ba8af8:8", "const:4:8"]]
+ 00ba8af8 ["CALL", null, ["callee:00bdc180:8"]]
- 00ba8ab4 bytes 9fcd0094
+ 00ba8af8 bytes a2cd0094
~~~


<a id="compare-eaf1174c5282afdcbb4206c5c77b2406"></a>

### [`00ba8bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8bec.md) → [`00ba8c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c30.md) _ZNSt6__ndk114collate_bynameIcED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8bec.md#insn-00ba8c00)
- 新版 [`00ba8c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c30.md#insn-00ba8c44)

~~~diff
- 00ba8c00 ["INT_ADD", "register:40f0:8", ["const:ba8c00:8", "const:4:8"]]
- 00ba8c00 ["CALL", null, ["callee:00be1940:8"]]
+ 00ba8c44 ["INT_ADD", "register:40f0:8", ["const:ba8c44:8", "const:4:8"]]
+ 00ba8c44 ["CALL", null, ["callee:00be1940:8"]]
- 00ba8c00 bytes 3ce30094
+ 00ba8c44 bytes 3fe30094
~~~


<a id="compare-d1fbe627e16588b03f33220d7a2d56c5"></a>

### [`00ba8c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8c18.md) → [`00ba8c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c5c.md) _ZNKSt6__ndk114collate_bynameIcE10do_compareEPKcS3_S3_S3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00be1900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1900.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00be1950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8c18.md#insn-00ba8c98) · [`00ba8cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8c18.md#insn-00ba8cc0) · [`00ba8d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8c18.md#insn-00ba8d04)
- 新版 [`00ba8cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c5c.md#insn-00ba8cdc) · [`00ba8d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c5c.md#insn-00ba8d04) · [`00ba8d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c5c.md#insn-00ba8d48)

~~~diff
- 00ba8c98 ["INT_ADD", "register:40f0:8", ["const:ba8c98:8", "const:4:8"]]
- 00ba8c98 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba8cdc ["INT_ADD", "register:40f0:8", ["const:ba8cdc:8", "const:4:8"]]
+ 00ba8cdc ["CALL", null, ["callee:00bdb040:8"]]
- 00ba8c98 bytes d6c80094
+ 00ba8cdc bytes d9c80094
- 00ba8cc0 ["INT_ADD", "register:40f0:8", ["const:ba8cc0:8", "const:4:8"]]
- 00ba8cc0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ba8d04 ["INT_ADD", "register:40f0:8", ["const:ba8d04:8", "const:4:8"]]
+ 00ba8d04 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ba8cc0 bytes 28c90094
+ 00ba8d04 bytes 2bc90094
- 00ba8d04 ["INT_ADD", "register:40f0:8", ["const:ba8d04:8", "const:4:8"]]
- 00ba8d04 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ba8d48 ["INT_ADD", "register:40f0:8", ["const:ba8d48:8", "const:4:8"]]
+ 00ba8d48 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ba8d04 bytes 17c90094
+ 00ba8d48 bytes 1ac90094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a35b2f8b14d752ad9ec5fc155ae6ec2"></a>

### [`00ba8df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8df0.md) → [`00ba8e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8e34.md) _ZNKSt6__ndk114collate_bynameIcE12do_transformEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8df0.md#insn-00ba8e68) · [`00ba8e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8df0.md#insn-00ba8e90) · [`00ba8ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8df0.md#insn-00ba8ebc)
- 新版 [`00ba8eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8e34.md#insn-00ba8eac) · [`00ba8ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8e34.md#insn-00ba8ed4) · [`00ba8f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8e34.md#insn-00ba8f00)

~~~diff
- 00ba8e68 ["INT_ADD", "register:40f0:8", ["const:ba8e68:8", "const:4:8"]]
- 00ba8e68 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba8eac ["INT_ADD", "register:40f0:8", ["const:ba8eac:8", "const:4:8"]]
+ 00ba8eac ["CALL", null, ["callee:00bdb040:8"]]
- 00ba8e68 bytes 62c80094
+ 00ba8eac bytes 65c80094
- 00ba8e90 ["INT_ADD", "register:40f0:8", ["const:ba8e90:8", "const:4:8"]]
- 00ba8e90 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ba8ed4 ["INT_ADD", "register:40f0:8", ["const:ba8ed4:8", "const:4:8"]]
+ 00ba8ed4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ba8e90 bytes b4c80094
+ 00ba8ed4 bytes b7c80094
- 00ba8ebc ["INT_ADD", "register:40f0:8", ["const:ba8ebc:8", "const:4:8"]]
- 00ba8ebc ["CALL", null, ["callee:00be1960:8"]]
+ 00ba8f00 ["INT_ADD", "register:40f0:8", ["const:ba8f00:8", "const:4:8"]]
+ 00ba8f00 ["CALL", null, ["callee:00be1960:8"]]
- 00ba8ebc bytes 95e20094
+ 00ba8f00 bytes 98e20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8e2615f62e9a1111ef5bb9f6f0c5f7"></a>

### [`00ba91cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91cc.md) → [`00ba9210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9210.md) _ZNSt6__ndk114collate_bynameIwED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1920.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba91e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91cc.md#insn-00ba91e0)
- 新版 [`00ba9224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9210.md#insn-00ba9224)

~~~diff
- 00ba91e0 ["INT_ADD", "register:40f0:8", ["const:ba91e0:8", "const:4:8"]]
- 00ba91e0 ["CALL", null, ["callee:00be1970:8"]]
+ 00ba9224 ["INT_ADD", "register:40f0:8", ["const:ba9224:8", "const:4:8"]]
+ 00ba9224 ["CALL", null, ["callee:00be1970:8"]]
- 00ba91e0 bytes d0e10094
+ 00ba9224 bytes d3e10094
~~~


<a id="compare-c0ec72c3cc1d09a92306e921935f9ddd"></a>

### [`00ba91f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91f8.md) → [`00ba923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md) _ZNKSt6__ndk114collate_bynameIwE10do_compareEPKwS3_S3_S3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 6件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba928c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91f8.md#insn-00ba928c) · [`00ba92c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91f8.md#insn-00ba92c0) · [`00ba9318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91f8.md#insn-00ba9318)
- 新版 [`00ba92d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md#insn-00ba92d0) · [`00ba9304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md#insn-00ba9304) · [`00ba935c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md#insn-00ba935c)

~~~diff
- 00ba928c ["INT_ADD", "register:40f0:8", ["const:ba928c:8", "const:4:8"]]
- 00ba928c ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba92d0 ["INT_ADD", "register:40f0:8", ["const:ba92d0:8", "const:4:8"]]
+ 00ba92d0 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba928c bytes 59c70094
+ 00ba92d0 bytes 5cc70094
- 00ba92c0 ["INT_ADD", "register:40f0:8", ["const:ba92c0:8", "const:4:8"]]
- 00ba92c0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ba9304 ["INT_ADD", "register:40f0:8", ["const:ba9304:8", "const:4:8"]]
+ 00ba9304 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ba92c0 bytes a8c70094
+ 00ba9304 bytes abc70094
- 00ba9318 ["INT_ADD", "register:40f0:8", ["const:ba9318:8", "const:4:8"]]
- 00ba9318 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ba935c ["INT_ADD", "register:40f0:8", ["const:ba935c:8", "const:4:8"]]
+ 00ba935c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ba9318 bytes 92c70094
+ 00ba935c bytes 95c70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3409bb5337ee7592a2a442286b909ee2"></a>

### [`00ba9410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9410.md) → [`00ba9454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9454.md) _ZNKSt6__ndk114collate_bynameIwE12do_transformEPKwS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba949c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9410.md#insn-00ba949c) · [`00ba94d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9410.md#insn-00ba94d0) · [`00ba9500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9410.md#insn-00ba9500)
- 新版 [`00ba94e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9454.md#insn-00ba94e0) · [`00ba9514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9454.md#insn-00ba9514) · [`00ba9544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9454.md#insn-00ba9544)

~~~diff
- 00ba949c ["INT_ADD", "register:40f0:8", ["const:ba949c:8", "const:4:8"]]
- 00ba949c ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba94e0 ["INT_ADD", "register:40f0:8", ["const:ba94e0:8", "const:4:8"]]
+ 00ba94e0 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba949c bytes d5c60094
+ 00ba94e0 bytes d8c60094
- 00ba94d0 ["INT_ADD", "register:40f0:8", ["const:ba94d0:8", "const:4:8"]]
- 00ba94d0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ba9514 ["INT_ADD", "register:40f0:8", ["const:ba9514:8", "const:4:8"]]
+ 00ba9514 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ba94d0 bytes 24c70094
+ 00ba9514 bytes 27c70094
- 00ba9500 ["INT_ADD", "register:40f0:8", ["const:ba9500:8", "const:4:8"]]
- 00ba9500 ["CALL", null, ["callee:00be1990:8"]]
+ 00ba9544 ["INT_ADD", "register:40f0:8", ["const:ba9544:8", "const:4:8"]]
+ 00ba9544 ["CALL", null, ["callee:00be1990:8"]]
- 00ba9500 bytes 10e10094
+ 00ba9544 bytes 13e10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb537fd0aa4158cf4f8969e3bc39a34a"></a>

### [`00ba9644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9644.md) → [`00ba9688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md) _ZNSt6__ndk15ctypeIwED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be19a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9644.md#insn-00ba9658)
- 新版 [`00ba969c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md#insn-00ba969c)

~~~diff
- 00ba9658 ["INT_ADD", "register:40f0:8", ["const:ba9658:8", "const:4:8"]]
- 00ba9658 ["CALL", null, ["callee:00be19a0:8"]]
+ 00ba969c ["INT_ADD", "register:40f0:8", ["const:ba969c:8", "const:4:8"]]
+ 00ba969c ["CALL", null, ["callee:00be19a0:8"]]
- 00ba9658 bytes bee00094
+ 00ba969c bytes c1e00094
~~~


<a id="compare-79cbf8a9e98067bdf5df3762acd22982"></a>

### [`00ba9de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9de0.md) → [`00ba9e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9e24.md) _ZNSt6__ndk15ctypeIcED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1980.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be19d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9de0.md#insn-00ba9df4)
- 新版 [`00ba9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9e24.md#insn-00ba9e38)

~~~diff
- 00ba9df4 ["INT_ADD", "register:40f0:8", ["const:ba9df4:8", "const:4:8"]]
- 00ba9df4 ["CALL", null, ["callee:00be19d0:8"]]
+ 00ba9e38 ["INT_ADD", "register:40f0:8", ["const:ba9e38:8", "const:4:8"]]
+ 00ba9e38 ["CALL", null, ["callee:00be19d0:8"]]
- 00ba9df4 bytes e3de0094
+ 00ba9e38 bytes e6de0094
~~~


<a id="compare-4a03435ba2c70fde996f5ed16874e29b"></a>

### [`00baa4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa4a0.md) → [`00baa4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa4e4.md) _ZNSt6__ndk112ctype_bynameIcED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be19b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baa4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa4a0.md#insn-00baa4b4)
- 新版 [`00baa4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa4e4.md#insn-00baa4f8)

~~~diff
- 00baa4b4 ["INT_ADD", "register:40f0:8", ["const:baa4b4:8", "const:4:8"]]
- 00baa4b4 ["CALL", null, ["callee:00be1a00:8"]]
+ 00baa4f8 ["INT_ADD", "register:40f0:8", ["const:baa4f8:8", "const:4:8"]]
+ 00baa4f8 ["CALL", null, ["callee:00be1a00:8"]]
- 00baa4b4 bytes 3fdd0094
+ 00baa4f8 bytes 42dd0094
~~~


<a id="compare-dcc7374beb6ecb83c8bbf9e5b1b41785"></a>

### [`00baa9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa9f8.md) → [`00baaa3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa3c.md) _ZNSt6__ndk112ctype_bynameIwED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be19f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baaa0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa9f8.md#insn-00baaa0c)
- 新版 [`00baaa50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa3c.md#insn-00baaa50)

~~~diff
- 00baaa0c ["INT_ADD", "register:40f0:8", ["const:baaa0c:8", "const:4:8"]]
- 00baaa0c ["CALL", null, ["callee:00be1a40:8"]]
+ 00baaa50 ["INT_ADD", "register:40f0:8", ["const:baaa50:8", "const:4:8"]]
+ 00baaa50 ["CALL", null, ["callee:00be1a40:8"]]
- 00baaa0c bytes f9db0094
+ 00baaa50 bytes fcdb0094
~~~


<a id="compare-c360fba2e4e4873b27f49cbb1fddac08"></a>

### [`00baaa24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md) → [`00baaa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md) _ZNKSt6__ndk112ctype_bynameIwE5do_isEmw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be19b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19b0.md) [`00be1a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a50.md) [`00be1a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a60.md) [`00be1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a70.md) [`00be1a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baaa5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md#insn-00baaa5c) · [`00baaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md#insn-00baaa74) · [`00baaaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaa24.md#insn-00baaaa8)
- 新版 [`00baaaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md#insn-00baaaa0) · [`00baaab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md#insn-00baaab8) · [`00baaaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md#insn-00baaaec)

~~~diff
- 00baaa5c ["INT_ADD", "register:40f0:8", ["const:baaa5c:8", "const:4:8"]]
- 00baaa5c ["CALL", null, ["callee:00be1a50:8"]]
+ 00baaaa0 ["INT_ADD", "register:40f0:8", ["const:baaaa0:8", "const:4:8"]]
+ 00baaaa0 ["CALL", null, ["callee:00be1a50:8"]]
- 00baaa5c bytes e9db0094
+ 00baaaa0 bytes ecdb0094
- 00baaa74 ["INT_ADD", "register:40f0:8", ["const:baaa74:8", "const:4:8"]]
- 00baaa74 ["CALL", null, ["callee:00be1a60:8"]]
+ 00baaab8 ["INT_ADD", "register:40f0:8", ["const:baaab8:8", "const:4:8"]]
+ 00baaab8 ["CALL", null, ["callee:00be1a60:8"]]
- 00baaa74 bytes e7db0094
+ 00baaab8 bytes eadb0094
- 00baaaa8 ["INT_ADD", "register:40f0:8", ["const:baaaa8:8", "const:4:8"]]
- 00baaaa8 ["CALL", null, ["callee:00be1a70:8"]]
+ 00baaaec ["INT_ADD", "register:40f0:8", ["const:baaaec:8", "const:4:8"]]
+ 00baaaec ["CALL", null, ["callee:00be1a70:8"]]
- 00baaaa8 bytes dedb0094
+ 00baaaec bytes e1db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3431ca1f4f1685a0ba7f9837c3cece"></a>

### [`00baab78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md) → [`00baabbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baabbc.md) _ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be19b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19b0.md) [`00be1a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a50.md) [`00be1a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a60.md) [`00be1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a70.md) [`00be1a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baabe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md#insn-00baabe4) · [`00baac00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md#insn-00baac00) · [`00baac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md#insn-00baac1c)
- 新版 [`00baac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baabbc.md#insn-00baac28) · [`00baac44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baabbc.md#insn-00baac44) · [`00baac60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baabbc.md#insn-00baac60)

~~~diff
- 00baabe4 ["INT_ADD", "register:40f0:8", ["const:baabe4:8", "const:4:8"]]
- 00baabe4 ["CALL", null, ["callee:00be1a50:8"]]
+ 00baac28 ["INT_ADD", "register:40f0:8", ["const:baac28:8", "const:4:8"]]
+ 00baac28 ["CALL", null, ["callee:00be1a50:8"]]
- 00baabe4 bytes 87db0094
+ 00baac28 bytes 8adb0094
- 00baac00 ["INT_ADD", "register:40f0:8", ["const:baac00:8", "const:4:8"]]
- 00baac00 ["CALL", null, ["callee:00be1a60:8"]]
+ 00baac44 ["INT_ADD", "register:40f0:8", ["const:baac44:8", "const:4:8"]]
+ 00baac44 ["CALL", null, ["callee:00be1a60:8"]]
- 00baac00 bytes 84db0094
+ 00baac44 bytes 87db0094
- 00baac1c ["INT_ADD", "register:40f0:8", ["const:baac1c:8", "const:4:8"]]
- 00baac1c ["CALL", null, ["callee:00be1a80:8"]]
+ 00baac60 ["INT_ADD", "register:40f0:8", ["const:baac60:8", "const:4:8"]]
+ 00baac60 ["CALL", null, ["callee:00be1a80:8"]]
- 00baac1c bytes 85db0094
+ 00baac60 bytes 88db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12ef38242a7fc785848d2330be3a4744"></a>

### [`00baad14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md) → [`00baad58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baad58.md) _ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be19b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19b0.md) [`00be1a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a50.md) [`00be1a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a60.md) [`00be1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a70.md) [`00be1a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baad64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md#insn-00baad64) · [`00baad78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md#insn-00baad78) · [`00baad8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md#insn-00baad8c)
- 新版 [`00baada8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baad58.md#insn-00baada8) · [`00baadbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baad58.md#insn-00baadbc) · [`00baadd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baad58.md#insn-00baadd0)

~~~diff
- 00baad64 ["INT_ADD", "register:40f0:8", ["const:baad64:8", "const:4:8"]]
- 00baad64 ["CALL", null, ["callee:00be1a50:8"]]
+ 00baada8 ["INT_ADD", "register:40f0:8", ["const:baada8:8", "const:4:8"]]
+ 00baada8 ["CALL", null, ["callee:00be1a50:8"]]
- 00baad64 bytes 27db0094
+ 00baada8 bytes 2adb0094
- 00baad78 ["INT_ADD", "register:40f0:8", ["const:baad78:8", "const:4:8"]]
- 00baad78 ["CALL", null, ["callee:00be1a60:8"]]
+ 00baadbc ["INT_ADD", "register:40f0:8", ["const:baadbc:8", "const:4:8"]]
+ 00baadbc ["CALL", null, ["callee:00be1a60:8"]]
- 00baad78 bytes 26db0094
+ 00baadbc bytes 29db0094
- 00baad8c ["INT_ADD", "register:40f0:8", ["const:baad8c:8", "const:4:8"]]
- 00baad8c ["CALL", null, ["callee:00be1a80:8"]]
+ 00baadd0 ["INT_ADD", "register:40f0:8", ["const:baadd0:8", "const:4:8"]]
+ 00baadd0 ["CALL", null, ["callee:00be1a80:8"]]
- 00baad8c bytes 29db0094
+ 00baadd0 bytes 2cdb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b610cb73fe8c68c54d657273f1720dda"></a>

### [`00baae44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md) → [`00baae88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baae88.md) _ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md) [`00be1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a00.md) [`00be1a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00be19b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19b0.md) [`00be1a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a50.md) [`00be1a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a60.md) [`00be1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a70.md) [`00be1a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baae80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md#insn-00baae80) · [`00baaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md#insn-00baaea8) · [`00baaebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md#insn-00baaebc)
- 新版 [`00baaec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baae88.md#insn-00baaec4) · [`00baaeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baae88.md#insn-00baaeec) · [`00baaf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baae88.md#insn-00baaf00)

~~~diff
- 00baae80 ["INT_ADD", "register:40f0:8", ["const:baae80:8", "const:4:8"]]
- 00baae80 ["CALL", null, ["callee:00be1a50:8"]]
+ 00baaec4 ["INT_ADD", "register:40f0:8", ["const:baaec4:8", "const:4:8"]]
+ 00baaec4 ["CALL", null, ["callee:00be1a50:8"]]
- 00baae80 bytes e0da0094
+ 00baaec4 bytes e3da0094
- 00baaea8 ["INT_ADD", "register:40f0:8", ["const:baaea8:8", "const:4:8"]]
- 00baaea8 ["CALL", null, ["callee:00be1a60:8"]]
+ 00baaeec ["INT_ADD", "register:40f0:8", ["const:baaeec:8", "const:4:8"]]
+ 00baaeec ["CALL", null, ["callee:00be1a60:8"]]
- 00baaea8 bytes dada0094
+ 00baaeec bytes ddda0094
- 00baaebc ["INT_ADD", "register:40f0:8", ["const:baaebc:8", "const:4:8"]]
- 00baaebc ["CALL", null, ["callee:00be1a80:8"]]
+ 00baaf00 ["INT_ADD", "register:40f0:8", ["const:baaf00:8", "const:4:8"]]
+ 00baaf00 ["CALL", null, ["callee:00be1a80:8"]]
- 00baaebc bytes ddda0094
+ 00baaf00 bytes e0da0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2294eea507136f6f51529ea6f973a4bf"></a>

### [`00baaf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf88.md) → [`00baafcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baafcc.md) _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baafb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf88.md#insn-00baafb8)
- 新版 [`00baaffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baafcc.md#insn-00baaffc)

~~~diff
- 00baafb8 ["INT_ADD", "register:40f0:8", ["const:baafb8:8", "const:4:8"]]
- 00baafb8 ["CALL", null, ["callee:00be1ae0:8"]]
+ 00baaffc ["INT_ADD", "register:40f0:8", ["const:baaffc:8", "const:4:8"]]
+ 00baaffc ["CALL", null, ["callee:00be1ae0:8"]]
- 00baafb8 bytes b6da0094
+ 00baaffc bytes b9da0094
~~~


<a id="compare-56e4006805b19e884cead5758015945f"></a>

### [`00baaff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaff8.md) → [`00bab03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab03c.md) _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEPwPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1af0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaff8.md#insn-00bab028)
- 新版 [`00bab06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab03c.md#insn-00bab06c)

~~~diff
- 00bab028 ["INT_ADD", "register:40f0:8", ["const:bab028:8", "const:4:8"]]
- 00bab028 ["CALL", null, ["callee:00be1af0:8"]]
+ 00bab06c ["INT_ADD", "register:40f0:8", ["const:bab06c:8", "const:4:8"]]
+ 00bab06c ["CALL", null, ["callee:00be1af0:8"]]
- 00bab028 bytes 9eda0094
+ 00bab06c bytes a1da0094
~~~


<a id="compare-fa0188966fe8e5d2b76c5b72fbd48966"></a>

### [`00bab054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md) → [`00bab098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab098.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md#insn-00bab070) · [`00bab080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md#insn-00bab080) · [`00bab090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md#insn-00bab090)
- 新版 [`00bab0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab098.md#insn-00bab0b4) · [`00bab0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab098.md#insn-00bab0c4) · [`00bab0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab098.md#insn-00bab0d4)

~~~diff
- 00bab070 ["INT_ADD", "register:40f0:8", ["const:bab070:8", "const:4:8"]]
- 00bab070 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab0b4 ["INT_ADD", "register:40f0:8", ["const:bab0b4:8", "const:4:8"]]
+ 00bab0b4 ["CALL", null, ["callee:00be1580:8"]]
- 00bab070 bytes 30d90094
+ 00bab0b4 bytes 33d90094
- 00bab080 ["INT_ADD", "register:40f0:8", ["const:bab080:8", "const:4:8"]]
- 00bab080 ["CALL", null, ["callee:00be1b00:8"]]
+ 00bab0c4 ["INT_ADD", "register:40f0:8", ["const:bab0c4:8", "const:4:8"]]
+ 00bab0c4 ["CALL", null, ["callee:00be1b00:8"]]
- 00bab080 bytes 8cda0094
+ 00bab0c4 bytes 8fda0094
- 00bab090 ["INT_ADD", "register:40f0:8", ["const:bab090:8", "const:4:8"]]
- 00bab090 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab0d4 ["INT_ADD", "register:40f0:8", ["const:bab0d4:8", "const:4:8"]]
+ 00bab0d4 ["CALL", null, ["callee:00be1580:8"]]
- 00bab090 bytes 28d90094
+ 00bab0d4 bytes 2bd90094
~~~


<a id="compare-1d5f27aa3ba2f0a0b1aed148f19d7c2f"></a>

### [`00bab0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md) → [`00bab108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab108.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md#insn-00bab114) · [`00bab124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md#insn-00bab124) · [`00bab134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md#insn-00bab134)
- 新版 [`00bab158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab108.md#insn-00bab158) · [`00bab168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab108.md#insn-00bab168) · [`00bab178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab108.md#insn-00bab178)

~~~diff
- 00bab114 ["INT_ADD", "register:40f0:8", ["const:bab114:8", "const:4:8"]]
- 00bab114 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab158 ["INT_ADD", "register:40f0:8", ["const:bab158:8", "const:4:8"]]
+ 00bab158 ["CALL", null, ["callee:00be1580:8"]]
- 00bab114 bytes 07d90094
+ 00bab158 bytes 0ad90094
- 00bab124 ["INT_ADD", "register:40f0:8", ["const:bab124:8", "const:4:8"]]
- 00bab124 ["CALL", null, ["callee:00be1b00:8"]]
+ 00bab168 ["INT_ADD", "register:40f0:8", ["const:bab168:8", "const:4:8"]]
+ 00bab168 ["CALL", null, ["callee:00be1b00:8"]]
- 00bab124 bytes 63da0094
+ 00bab168 bytes 66da0094
- 00bab134 ["INT_ADD", "register:40f0:8", ["const:bab134:8", "const:4:8"]]
- 00bab134 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab178 ["INT_ADD", "register:40f0:8", ["const:bab178:8", "const:4:8"]]
+ 00bab178 ["CALL", null, ["callee:00be1580:8"]]
- 00bab134 bytes ffd80094
+ 00bab178 bytes 02d90094
~~~


<a id="compare-d2b1fc00ee923d02f33d779dfcac0bd1"></a>

### [`00bab178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md) → [`00bab1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab1bc.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md#insn-00bab198) · [`00bab1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md#insn-00bab1a8) · [`00bab1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md#insn-00bab1b8)
- 新版 [`00bab1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab1bc.md#insn-00bab1dc) · [`00bab1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab1bc.md#insn-00bab1ec) · [`00bab1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab1bc.md#insn-00bab1fc)

~~~diff
- 00bab198 ["INT_ADD", "register:40f0:8", ["const:bab198:8", "const:4:8"]]
- 00bab198 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab1dc ["INT_ADD", "register:40f0:8", ["const:bab1dc:8", "const:4:8"]]
+ 00bab1dc ["CALL", null, ["callee:00be1580:8"]]
- 00bab198 bytes e6d80094
+ 00bab1dc bytes e9d80094
- 00bab1a8 ["INT_ADD", "register:40f0:8", ["const:bab1a8:8", "const:4:8"]]
- 00bab1a8 ["CALL", null, ["callee:00be1b10:8"]]
+ 00bab1ec ["INT_ADD", "register:40f0:8", ["const:bab1ec:8", "const:4:8"]]
+ 00bab1ec ["CALL", null, ["callee:00be1b10:8"]]
- 00bab1a8 bytes 46da0094
+ 00bab1ec bytes 49da0094
- 00bab1b8 ["INT_ADD", "register:40f0:8", ["const:bab1b8:8", "const:4:8"]]
- 00bab1b8 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab1fc ["INT_ADD", "register:40f0:8", ["const:bab1fc:8", "const:4:8"]]
+ 00bab1fc ["CALL", null, ["callee:00be1580:8"]]
- 00bab1b8 bytes ded80094
+ 00bab1fc bytes e1d80094
~~~


<a id="compare-9aa7fc189a0b163658b768483a329334"></a>

### [`00bab1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md) → [`00bab234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab234.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEPKwS3_cPc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md#insn-00bab24c) · [`00bab25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md#insn-00bab25c) · [`00bab26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab1f0.md#insn-00bab26c)
- 新版 [`00bab290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab234.md#insn-00bab290) · [`00bab2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab234.md#insn-00bab2a0) · [`00bab2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab234.md#insn-00bab2b0)

~~~diff
- 00bab24c ["INT_ADD", "register:40f0:8", ["const:bab24c:8", "const:4:8"]]
- 00bab24c ["CALL", null, ["callee:00be1580:8"]]
+ 00bab290 ["INT_ADD", "register:40f0:8", ["const:bab290:8", "const:4:8"]]
+ 00bab290 ["CALL", null, ["callee:00be1580:8"]]
- 00bab24c bytes b9d80094
+ 00bab290 bytes bcd80094
- 00bab25c ["INT_ADD", "register:40f0:8", ["const:bab25c:8", "const:4:8"]]
- 00bab25c ["CALL", null, ["callee:00be1b10:8"]]
+ 00bab2a0 ["INT_ADD", "register:40f0:8", ["const:bab2a0:8", "const:4:8"]]
+ 00bab2a0 ["CALL", null, ["callee:00be1b10:8"]]
- 00bab25c bytes 19da0094
+ 00bab2a0 bytes 1cda0094
- 00bab26c ["INT_ADD", "register:40f0:8", ["const:bab26c:8", "const:4:8"]]
- 00bab26c ["CALL", null, ["callee:00be1580:8"]]
+ 00bab2b0 ["INT_ADD", "register:40f0:8", ["const:bab2b0:8", "const:4:8"]]
+ 00bab2b0 ["CALL", null, ["callee:00be1580:8"]]
- 00bab26c bytes b1d80094
+ 00bab2b0 bytes b4d80094
~~~


