# 00b4cdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4cda8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0068.md#compare-9001914785fb4b8f110ad0b928c59d8f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0092.md#review-91c3fbaa88638f7d90a77b5ee9fb00a9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cdec",
  "name": "FUN_00b4cdec",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b8cf8c57a9744ec295cd175bd91cb7630a2a9f9811284cd6ddf4a511a70832b",
  "source_text_sha256": "9b8cf8c57a9744ec295cd175bd91cb7630a2a9f9811284cd6ddf4a511a70832b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4cdec",
        "00b4cea7"
      ]
    ],
    "bytes_sha256": "12c8881203dcfbb6d3de4f98c3dbeae3215352d95ed9d86614737ab259c4d5f9",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00b4c4c4](../00b4c/00b4c4c4.md)
- [00b4cc40](../00b4c/00b4cc40.md)

## 呼び出し先

- [00848b34](../00848/00848b34.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bdde40](../00bdd/00bdde40.md)
- [00bde180](../00bde/00bde180.md)
- [00be05e0](../00be0/00be05e0.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1237 bytes

~~~c

void FUN_00b4cdec(void)

{
  long lVar1;
  undefined1 auStack_80 [24];
  undefined1 auStack_68 [40];
  long *local_40;
  undefined1 auStack_38 [16];
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_010a10a0 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
  }
  else {
                    /* try { // try from 00b4ce14 to 00c4ce1f has its CatchHandler @ 00b4d9dc */
    _ZN8firebase9messaging8GetTokenEv(auStack_68);
    _ZN8firebase5Mutex7AcquireEv(auStack_68);
    if (local_40 != (long *)0x0) {
                    /* try { // try from 00b4ce38 to 00c4ce43 has its CatchHandler @ 00b4d9cc */
      (**(code **)(*local_40 + 0x40))(auStack_80,local_40,auStack_38,FUN_00b4ea90,0,0,1);
    }
    _ZN8firebase5Mutex7ReleaseEv(auStack_68);
                    /* try { // try from 00b4ce64 to 00c4ce6f has its CatchHandler @ 00b4d980 */
    FUN_00848b34(auStack_68);
  }
                    /* try { // try from 00b4ce88 to 00c4ce93 has its CatchHandler @ 00b4d97c */
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4cdec"></a> `00b4cdec` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b4cdf0"></a> `00b4cdf0` | `f3 33 00 f9` | str x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b4cdf4"></a> `00b4cdf4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b4cdf8"></a> `00b4cdf8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b4cdfc"></a> `00b4cdfc` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b4ce00"></a> `00b4ce00` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b4ce04"></a> `00b4ce04` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00b4ce08"></a> `00b4ce08` | `a8 2a 00 b0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4ce0c"></a> `00b4ce0c` | `08 51 40 f9` | ldr x8,[x8, #0xa0] | `FALL_THROUGH`
<a id="insn-00b4ce10"></a> `00b4ce10` | `e8 02 00 b4` | cbz x8,0x00b4ce6c | `CONDITIONAL_JUMP`
<a id="insn-00b4ce14"></a> `00b4ce14` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4ce18"></a> `00b4ce18` | `f2 4d 02 94` | bl 0x00be05e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce1c"></a> `00b4ce1c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4ce20"></a> `00b4ce20` | `80 43 02 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce24"></a> `00b4ce24` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b4ce28"></a> `00b4ce28` | `80 01 00 b4` | cbz x0,0x00b4ce58 | `CONDITIONAL_JUMP`
<a id="insn-00b4ce2c"></a> `00b4ce2c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b4ce30"></a> `00b4ce30` | `09 21 40 f9` | ldr x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00b4ce34"></a> `00b4ce34` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4ce38"></a> `00b4ce38` | `01 c1 00 91` | add x1,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00b4ce3c"></a> `00b4ce3c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00b4ce40"></a> `00b4ce40` | `82 e2 00 10` | adr x2,0xb4ea90 | `FALL_THROUGH`
<a id="insn-00b4ce44"></a> `00b4ce44` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b4ce48"></a> `00b4ce48` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ce4c"></a> `00b4ce4c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00b4ce50"></a> `00b4ce50` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00b4ce54"></a> `00b4ce54` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b4ce58"></a> `00b4ce58` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4ce5c"></a> `00b4ce5c` | `75 43 02 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce60"></a> `00b4ce60` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4ce64"></a> `00b4ce64` | `34 ef f3 97` | bl 0x00848b34 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce68"></a> `00b4ce68` | `07 00 00 14` | b 0x00b4ce84 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4ce6c"></a> `00b4ce6c` | `20 ba ff f0` | adrp x0,0x293000 | `FALL_THROUGH`
<a id="insn-00b4ce70"></a> `00b4ce70` | `00 80 03 91` | add x0,x0,#0xe0 | `FALL_THROUGH`
<a id="insn-00b4ce74"></a> `00b4ce74` | `f3 43 02 94` | bl 0x00bdde40 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce78"></a> `00b4ce78` | `a0 ba ff 90` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00b4ce7c"></a> `00b4ce7c` | `00 84 06 91` | add x0,x0,#0x1a1 | `FALL_THROUGH`
<a id="insn-00b4ce80"></a> `00b4ce80` | `c0 44 02 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce84"></a> `00b4ce84` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b4ce88"></a> `00b4ce88` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00b4ce8c"></a> `00b4ce8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b4ce90"></a> `00b4ce90` | `a1 00 00 54` | b.ne 0x00b4cea4 | `CONDITIONAL_JUMP`
<a id="insn-00b4ce94"></a> `00b4ce94` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b4ce98"></a> `00b4ce98` | `f3 33 40 f9` | ldr x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b4ce9c"></a> `00b4ce9c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b4cea0"></a> `00b4cea0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b4cea4"></a> `00b4cea4` | `7b 38 02 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4cdec`](#insn-00b4cdec) 範囲 `[['00b4cdec', '00b4ce13']]`
  - `CONDITIONAL_JUMP` [`00b4ce10`](#insn-00b4ce10) → [`00b4ce6c`](#insn-00b4ce6c)
  - `FALL_THROUGH` [`00b4ce10`](#insn-00b4ce10) → [`00b4ce14`](#insn-00b4ce14)
- ブロック [`00b4ce14`](#insn-00b4ce14) 範囲 `[['00b4ce14', '00b4ce2b']]`
  - `CONDITIONAL_JUMP` [`00b4ce28`](#insn-00b4ce28) → [`00b4ce58`](#insn-00b4ce58)
  - `FALL_THROUGH` [`00b4ce28`](#insn-00b4ce28) → [`00b4ce2c`](#insn-00b4ce2c)
- ブロック [`00b4ce2c`](#insn-00b4ce2c) 範囲 `[['00b4ce2c', '00b4ce37']]`
  - `FALL_THROUGH` [`00b4ce34`](#insn-00b4ce34) → [`00b4ce38`](#insn-00b4ce38)
- ブロック [`00b4ce38`](#insn-00b4ce38) 範囲 `[['00b4ce38', '00b4ce57']]`
  - `FALL_THROUGH` [`00b4ce54`](#insn-00b4ce54) → [`00b4ce58`](#insn-00b4ce58)
- ブロック [`00b4ce58`](#insn-00b4ce58) 範囲 `[['00b4ce58', '00b4ce63']]`
  - `FALL_THROUGH` [`00b4ce60`](#insn-00b4ce60) → [`00b4ce64`](#insn-00b4ce64)
- ブロック [`00b4ce64`](#insn-00b4ce64) 範囲 `[['00b4ce64', '00b4ce6b']]`
  - `UNCONDITIONAL_JUMP` [`00b4ce68`](#insn-00b4ce68) → [`00b4ce84`](#insn-00b4ce84)
- ブロック [`00b4ce6c`](#insn-00b4ce6c) 範囲 `[['00b4ce6c', '00b4ce83']]`
  - `FALL_THROUGH` [`00b4ce80`](#insn-00b4ce80) → [`00b4ce84`](#insn-00b4ce84)
- ブロック [`00b4ce84`](#insn-00b4ce84) 範囲 `[['00b4ce84', '00b4ce87']]`
  - `FALL_THROUGH` [`00b4ce84`](#insn-00b4ce84) → [`00b4ce88`](#insn-00b4ce88)
- ブロック [`00b4ce88`](#insn-00b4ce88) 範囲 `[['00b4ce88', '00b4ce93']]`
  - `CONDITIONAL_JUMP` [`00b4ce90`](#insn-00b4ce90) → [`00b4cea4`](#insn-00b4cea4)
  - `FALL_THROUGH` [`00b4ce90`](#insn-00b4ce90) → [`00b4ce94`](#insn-00b4ce94)
- ブロック [`00b4ce94`](#insn-00b4ce94) 範囲 `[['00b4ce94', '00b4cea3']]`
- ブロック [`00b4cea4`](#insn-00b4cea4) 範囲 `[['00b4cea4', '00b4cea7']]`

## 命令位置別の参照

- [`00b4cdf0`](#insn-00b4cdf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cdf4`](#insn-00b4cdf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce04`](#insn-00b4ce04) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce0c`](#insn-00b4ce0c) → `010a10a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ce10`](#insn-00b4ce10) → [`00b4ce6c`](#insn-00b4ce6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce18`](#insn-00b4ce18) → [`00be05e0`](../00be0/00be05e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be05e0` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce20`](#insn-00b4ce20) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce24`](#insn-00b4ce24) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce28`](#insn-00b4ce28) → [`00b4ce58`](#insn-00b4ce58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce40`](#insn-00b4ce40) → [`00b4ea90`](../00b4e/00b4ea90.md) · `PARAM` · `ANALYSIS` · 関数 `00b4ea90` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce5c`](#insn-00b4ce5c) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce64`](#insn-00b4ce64) → [`00848b34`](../00848/00848b34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00848b34` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce68`](#insn-00b4ce68) → [`00b4ce84`](#insn-00b4ce84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce70`](#insn-00b4ce70) → `002930e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ce74`](#insn-00b4ce74) → [`00bdde40`](../00bdd/00bdde40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde40` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce7c`](#insn-00b4ce7c) → `002a01a1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ce80`](#insn-00b4ce80) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce88`](#insn-00b4ce88) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce90`](#insn-00b4ce90) → [`00b4cea4`](#insn-00b4cea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce94`](#insn-00b4ce94) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce98`](#insn-00b4ce98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cea4`](#insn-00b4cea4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4cdf0`](#insn-00b4cdf0)

~~~json
{
  "source": "00b4cdf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cdf4`](#insn-00b4cdf4)

~~~json
{
  "source": "00b4cdf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce04`](#insn-00b4ce04)

~~~json
{
  "source": "00b4ce04",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce0c`](#insn-00b4ce0c)

~~~json
{
  "source": "00b4ce0c",
  "target": "010a10a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a10a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ce10`](#insn-00b4ce10)

~~~json
{
  "source": "00b4ce10",
  "target": "00b4ce6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce18`](#insn-00b4ce18)

~~~json
{
  "source": "00b4ce18",
  "target": "00be05e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce20`](#insn-00b4ce20)

~~~json
{
  "source": "00b4ce20",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce24`](#insn-00b4ce24)

~~~json
{
  "source": "00b4ce24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce28`](#insn-00b4ce28)

~~~json
{
  "source": "00b4ce28",
  "target": "00b4ce58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce40`](#insn-00b4ce40)

~~~json
{
  "source": "00b4ce40",
  "target": "00b4ea90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce5c`](#insn-00b4ce5c)

~~~json
{
  "source": "00b4ce5c",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce64`](#insn-00b4ce64)

~~~json
{
  "source": "00b4ce64",
  "target": "00848b34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce68`](#insn-00b4ce68)

~~~json
{
  "source": "00b4ce68",
  "target": "00b4ce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce70`](#insn-00b4ce70)

~~~json
{
  "source": "00b4ce70",
  "target": "002930e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002930e0",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002930e0",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4ce74`](#insn-00b4ce74)

~~~json
{
  "source": "00b4ce74",
  "target": "00bdde40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce7c`](#insn-00b4ce7c)

~~~json
{
  "source": "00b4ce7c",
  "target": "002a01a1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a01a1",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002a01a1",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4ce80`](#insn-00b4ce80)

~~~json
{
  "source": "00b4ce80",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce88`](#insn-00b4ce88)

~~~json
{
  "source": "00b4ce88",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce90`](#insn-00b4ce90)

~~~json
{
  "source": "00b4ce90",
  "target": "00b4cea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce94`](#insn-00b4ce94)

~~~json
{
  "source": "00b4ce94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce98`](#insn-00b4ce98)

~~~json
{
  "source": "00b4ce98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cea4`](#insn-00b4cea4)

~~~json
{
  "source": "00b4cea4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
