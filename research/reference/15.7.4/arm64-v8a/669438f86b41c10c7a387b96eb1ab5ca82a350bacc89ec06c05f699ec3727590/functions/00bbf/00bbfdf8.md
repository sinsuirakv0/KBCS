# 00bbfdf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbfdb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-d9b71af5466806dc710052541da539f3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3c840`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-24f693dbfc2a67a8edea667f33d9d1a0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfdf8",
  "name": "FUN_00bbfdf8",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18133ecfa9ecf78487356c25d8054d1c1113ba80452cd2b036d7bbc8d295e988",
  "source_text_sha256": "18133ecfa9ecf78487356c25d8054d1c1113ba80452cd2b036d7bbc8d295e988",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfdf8",
        "00bbfecf"
      ]
    ],
    "bytes_sha256": "9982b20e7900ad0ac59b63ad70aae47dc33f83316537bc681ae195584fa5097f",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbde5c](../00bbd/00bbde5c.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)

## 呼び出し先

- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1415 bytes

~~~c

void FUN_00bbfdf8(undefined8 *param_1,undefined8 *param_2)

{
  void *__dest;
  undefined8 uVar1;
  size_t __n;
  undefined8 *__src;
  undefined8 *puVar2;
  
                    /* try { // try from 00bbfe08 to 00cbfe0f has its CatchHandler @ 00bc892c */
  puVar2 = (undefined8 *)param_1[1];
                    /* try { // try from 00bbfe14 to 00cbfe23 has its CatchHandler @ 00bc88ec */
  if (puVar2 == (undefined8 *)param_1[2]) {
    __src = (undefined8 *)*param_1;
    __n = (long)puVar2 - (long)__src;
                    /* try { // try from 00bbfe38 to 00cbfe6f has its CatchHandler @ 00bc8b2c */
    if (__src == param_1 + 3) {
      __dest = malloc(__n * 2);
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      if (puVar2 != __src) {
        memmove(__dest,__src,__n);
      }
      *param_1 = __dest;
    }
    else {
      __dest = realloc(__src,__n * 2);
      *param_1 = __dest;
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
    puVar2 = (undefined8 *)((long)__dest + __n);
    param_1[1] = puVar2;
    param_1[2] = (void *)((long)__dest + ((long)__n >> 2) * 8);
  }
  uVar1 = *param_2;
  param_1[1] = puVar2 + 1;
  *puVar2 = uVar1;
                    /* try { // try from 00bbfec0 to 00cbfed3 has its CatchHandler @ 00bc87e4 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbfdf8"></a> `00bbfdf8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfdfc"></a> `00bbfdfc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbfe00"></a> `00bbfe00` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfe04"></a> `00bbfe04` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfe08"></a> `00bbfe08` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfe0c"></a> `00bbfe0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfe10"></a> `00bbfe10` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfe14"></a> `00bbfe14` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfe18"></a> `00bbfe18` | `61 04 00 54` | b.ne 0x00bbfea4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe1c"></a> `00bbfe1c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfe20"></a> `00bbfe20` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bbfe24"></a> `00bbfe24` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbfe28"></a> `00bbfe28` | `14 85 41 f8` | ldr x20,[x8], #0x18 | `FALL_THROUGH`
<a id="insn-00bbfe2c"></a> `00bbfe2c` | `b3 02 14 cb` | sub x19,x21,x20 | `FALL_THROUGH`
<a id="insn-00bbfe30"></a> `00bbfe30` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbfe34"></a> `00bbfe34` | `61 fa 7f d3` | lsl x1,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfe38"></a> `00bbfe38` | `00 01 00 54` | b.eq 0x00bbfe58 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe3c"></a> `00bbfe3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbfe40"></a> `00bbfe40` | `04 75 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe44"></a> `00bbfe44` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfe48"></a> `00bbfe48` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfe4c"></a> `00bbfe4c` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bbfe50"></a> `00bbfe50` | `08 02 00 b5` | cbnz x8,0x00bbfe90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe54"></a> `00bbfe54` | `1b 79 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bbfe58"></a> `00bbfe58` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbfe5c"></a> `00bbfe5c` | `dd 74 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe60"></a> `00bbfe60` | `60 03 00 b4` | cbz x0,0x00bbfecc | `CONDITIONAL_JUMP`
<a id="insn-00bbfe64"></a> `00bbfe64` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfe68"></a> `00bbfe68` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00bbfe6c"></a> `00bbfe6c` | `e0 00 00 54` | b.eq 0x00bbfe88 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe70"></a> `00bbfe70` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfe74"></a> `00bbfe74` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbfe78"></a> `00bbfe78` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbfe7c"></a> `00bbfe7c` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfe80"></a> `00bbfe80` | `9c 6c 00 94` | bl 0x00bdb0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe84"></a> `00bbfe84` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbfe88"></a> `00bbfe88` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfe8c"></a> `00bbfe8c` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bbfe90"></a> `00bbfe90` | `69 fe 42 93` | asr x9,x19,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfe94"></a> `00bbfe94` | `15 01 13 8b` | add x21,x8,x19 | `FALL_THROUGH`
<a id="insn-00bbfe98"></a> `00bbfe98` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbfe9c"></a> `00bbfe9c` | `08 0d 09 8b` | add x8,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbfea0"></a> `00bbfea0` | `15 a0 00 a9` | stp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfea4"></a> `00bbfea4` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbfea8"></a> `00bbfea8` | `a9 22 00 91` | add x9,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bbfeac"></a> `00bbfeac` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfeb0"></a> `00bbfeb0` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00bbfeb4"></a> `00bbfeb4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfeb8"></a> `00bbfeb8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfebc"></a> `00bbfebc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfec0"></a> `00bbfec0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfec4"></a> `00bbfec4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfec8"></a> `00bbfec8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfecc"></a> `00bbfecc` | `fd 78 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfdf8`](#insn-00bbfdf8) 範囲 `[['00bbfdf8', '00bbfe07']]`
  - `FALL_THROUGH` [`00bbfe04`](#insn-00bbfe04) → [`00bbfe08`](#insn-00bbfe08)
- ブロック [`00bbfe08`](#insn-00bbfe08) 範囲 `[['00bbfe08', '00bbfe13']]`
  - `FALL_THROUGH` [`00bbfe10`](#insn-00bbfe10) → [`00bbfe14`](#insn-00bbfe14)
- ブロック [`00bbfe14`](#insn-00bbfe14) 範囲 `[['00bbfe14', '00bbfe1b']]`
  - `CONDITIONAL_JUMP` [`00bbfe18`](#insn-00bbfe18) → [`00bbfea4`](#insn-00bbfea4)
  - `FALL_THROUGH` [`00bbfe18`](#insn-00bbfe18) → [`00bbfe1c`](#insn-00bbfe1c)
- ブロック [`00bbfe1c`](#insn-00bbfe1c) 範囲 `[['00bbfe1c', '00bbfe37']]`
  - `FALL_THROUGH` [`00bbfe34`](#insn-00bbfe34) → [`00bbfe38`](#insn-00bbfe38)
- ブロック [`00bbfe38`](#insn-00bbfe38) 範囲 `[['00bbfe38', '00bbfe3b']]`
  - `CONDITIONAL_JUMP` [`00bbfe38`](#insn-00bbfe38) → [`00bbfe58`](#insn-00bbfe58)
  - `FALL_THROUGH` [`00bbfe38`](#insn-00bbfe38) → [`00bbfe3c`](#insn-00bbfe3c)
- ブロック [`00bbfe3c`](#insn-00bbfe3c) 範囲 `[['00bbfe3c', '00bbfe53']]`
  - `CONDITIONAL_JUMP` [`00bbfe50`](#insn-00bbfe50) → [`00bbfe90`](#insn-00bbfe90)
  - `FALL_THROUGH` [`00bbfe50`](#insn-00bbfe50) → [`00bbfe54`](#insn-00bbfe54)
- ブロック [`00bbfe54`](#insn-00bbfe54) 範囲 `[['00bbfe54', '00bbfe57']]`
- ブロック [`00bbfe58`](#insn-00bbfe58) 範囲 `[['00bbfe58', '00bbfe63']]`
  - `CONDITIONAL_JUMP` [`00bbfe60`](#insn-00bbfe60) → [`00bbfecc`](#insn-00bbfecc)
  - `FALL_THROUGH` [`00bbfe60`](#insn-00bbfe60) → [`00bbfe64`](#insn-00bbfe64)
- ブロック [`00bbfe64`](#insn-00bbfe64) 範囲 `[['00bbfe64', '00bbfe6f']]`
  - `CONDITIONAL_JUMP` [`00bbfe6c`](#insn-00bbfe6c) → [`00bbfe88`](#insn-00bbfe88)
  - `FALL_THROUGH` [`00bbfe6c`](#insn-00bbfe6c) → [`00bbfe70`](#insn-00bbfe70)
- ブロック [`00bbfe70`](#insn-00bbfe70) 範囲 `[['00bbfe70', '00bbfe87']]`
  - `FALL_THROUGH` [`00bbfe84`](#insn-00bbfe84) → [`00bbfe88`](#insn-00bbfe88)
- ブロック [`00bbfe88`](#insn-00bbfe88) 範囲 `[['00bbfe88', '00bbfe8f']]`
  - `FALL_THROUGH` [`00bbfe8c`](#insn-00bbfe8c) → [`00bbfe90`](#insn-00bbfe90)
- ブロック [`00bbfe90`](#insn-00bbfe90) 範囲 `[['00bbfe90', '00bbfea3']]`
  - `FALL_THROUGH` [`00bbfea0`](#insn-00bbfea0) → [`00bbfea4`](#insn-00bbfea4)
- ブロック [`00bbfea4`](#insn-00bbfea4) 範囲 `[['00bbfea4', '00bbfebf']]`
  - `FALL_THROUGH` [`00bbfebc`](#insn-00bbfebc) → [`00bbfec0`](#insn-00bbfec0)
- ブロック [`00bbfec0`](#insn-00bbfec0) 範囲 `[['00bbfec0', '00bbfecb']]`
- ブロック [`00bbfecc`](#insn-00bbfecc) 範囲 `[['00bbfecc', '00bbfecf']]`

## 命令位置別の参照

- [`00bbfdfc`](#insn-00bbfdfc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe00`](#insn-00bbfe00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe04`](#insn-00bbfe04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe08`](#insn-00bbfe08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe18`](#insn-00bbfe18) → [`00bbfea4`](#insn-00bbfea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe38`](#insn-00bbfe38) → [`00bbfe58`](#insn-00bbfe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe40`](#insn-00bbfe40) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe50`](#insn-00bbfe50) → [`00bbfe90`](#insn-00bbfe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe54`](#insn-00bbfe54) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe5c`](#insn-00bbfe5c) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe60`](#insn-00bbfe60) → [`00bbfecc`](#insn-00bbfecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe6c`](#insn-00bbfe6c) → [`00bbfe88`](#insn-00bbfe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe80`](#insn-00bbfe80) → [`00bdb0f0`](../00bdb/00bdb0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfeb4`](#insn-00bbfeb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfeb8`](#insn-00bbfeb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfebc`](#insn-00bbfebc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfec0`](#insn-00bbfec0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfecc`](#insn-00bbfecc) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfdfc`](#insn-00bbfdfc)

~~~json
{
  "source": "00bbfdfc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe00`](#insn-00bbfe00)

~~~json
{
  "source": "00bbfe00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe04`](#insn-00bbfe04)

~~~json
{
  "source": "00bbfe04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe08`](#insn-00bbfe08)

~~~json
{
  "source": "00bbfe08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe18`](#insn-00bbfe18)

~~~json
{
  "source": "00bbfe18",
  "target": "00bbfea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe38`](#insn-00bbfe38)

~~~json
{
  "source": "00bbfe38",
  "target": "00bbfe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe40`](#insn-00bbfe40)

~~~json
{
  "source": "00bbfe40",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe50`](#insn-00bbfe50)

~~~json
{
  "source": "00bbfe50",
  "target": "00bbfe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe54`](#insn-00bbfe54)

~~~json
{
  "source": "00bbfe54",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe5c`](#insn-00bbfe5c)

~~~json
{
  "source": "00bbfe5c",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe60`](#insn-00bbfe60)

~~~json
{
  "source": "00bbfe60",
  "target": "00bbfecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe6c`](#insn-00bbfe6c)

~~~json
{
  "source": "00bbfe6c",
  "target": "00bbfe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe80`](#insn-00bbfe80)

~~~json
{
  "source": "00bbfe80",
  "target": "00bdb0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfeb4`](#insn-00bbfeb4)

~~~json
{
  "source": "00bbfeb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfeb8`](#insn-00bbfeb8)

~~~json
{
  "source": "00bbfeb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfebc`](#insn-00bbfebc)

~~~json
{
  "source": "00bbfebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfec0`](#insn-00bbfec0)

~~~json
{
  "source": "00bbfec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfecc`](#insn-00bbfecc)

~~~json
{
  "source": "00bbfecc",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
