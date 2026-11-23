# 00bbfdb4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbfcec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfcec.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-bced895da71b3b1dc634f2a3b8218d21)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbfdf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-d9b71af5466806dc710052541da539f3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfdb4",
  "name": "FUN_00bbfdb4",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1be3bcd01121e394c6776b19d8287bfb175c62effe7a1f28d0ade1ab66f085e8",
  "source_text_sha256": "1be3bcd01121e394c6776b19d8287bfb175c62effe7a1f28d0ade1ab66f085e8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfdb4",
        "00bbfe8b"
      ]
    ],
    "bytes_sha256": "59aa06b2910ff4df4de982b7749e556339b6fd2b7f9f502dc7df8de283a36ded",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbde18](../00bbd/00bbde18.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdd180](../00bdd/00bdd180.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1415 bytes

~~~c

void FUN_00bbfdb4(undefined8 *param_1,undefined8 *param_2)

{
  void *__dest;
  undefined8 uVar1;
  size_t __n;
  undefined8 *__src;
  undefined8 *puVar2;
  
                    /* try { // try from 00bbfdc4 to 00cbfdcb has its CatchHandler @ 00bc88e8 */
  puVar2 = (undefined8 *)param_1[1];
                    /* try { // try from 00bbfdd0 to 00cbfddf has its CatchHandler @ 00bc88a8 */
  if (puVar2 == (undefined8 *)param_1[2]) {
    __src = (undefined8 *)*param_1;
    __n = (long)puVar2 - (long)__src;
                    /* try { // try from 00bbfdf4 to 00cbfe2b has its CatchHandler @ 00bc8ae8 */
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
                    /* try { // try from 00bbfe7c to 00cbfe8f has its CatchHandler @ 00bc87a0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbfdb4"></a> `00bbfdb4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfdb8"></a> `00bbfdb8` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbfdbc"></a> `00bbfdbc` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfdc0"></a> `00bbfdc0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfdc4"></a> `00bbfdc4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfdc8"></a> `00bbfdc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfdcc"></a> `00bbfdcc` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfdd0"></a> `00bbfdd0` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfdd4"></a> `00bbfdd4` | `61 04 00 54` | b.ne 0x00bbfe60 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdd8"></a> `00bbfdd8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfddc"></a> `00bbfddc` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bbfde0"></a> `00bbfde0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbfde4"></a> `00bbfde4` | `14 85 41 f8` | ldr x20,[x8], #0x18 | `FALL_THROUGH`
<a id="insn-00bbfde8"></a> `00bbfde8` | `b3 02 14 cb` | sub x19,x21,x20 | `FALL_THROUGH`
<a id="insn-00bbfdec"></a> `00bbfdec` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbfdf0"></a> `00bbfdf0` | `61 fa 7f d3` | lsl x1,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfdf4"></a> `00bbfdf4` | `00 01 00 54` | b.eq 0x00bbfe14 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdf8"></a> `00bbfdf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbfdfc"></a> `00bbfdfc` | `01 75 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe00"></a> `00bbfe00` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfe04"></a> `00bbfe04` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfe08"></a> `00bbfe08` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bbfe0c"></a> `00bbfe0c` | `08 02 00 b5` | cbnz x8,0x00bbfe4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfe10"></a> `00bbfe10` | `18 79 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bbfe14"></a> `00bbfe14` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbfe18"></a> `00bbfe18` | `da 74 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe1c"></a> `00bbfe1c` | `60 03 00 b4` | cbz x0,0x00bbfe88 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe20"></a> `00bbfe20` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfe24"></a> `00bbfe24` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00bbfe28"></a> `00bbfe28` | `e0 00 00 54` | b.eq 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe2c"></a> `00bbfe2c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfe30"></a> `00bbfe30` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbfe34"></a> `00bbfe34` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbfe38"></a> `00bbfe38` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfe3c"></a> `00bbfe3c` | `99 6c 00 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe40"></a> `00bbfe40` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbfe44"></a> `00bbfe44` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfe48"></a> `00bbfe48` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bbfe4c"></a> `00bbfe4c` | `69 fe 42 93` | asr x9,x19,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfe50"></a> `00bbfe50` | `15 01 13 8b` | add x21,x8,x19 | `FALL_THROUGH`
<a id="insn-00bbfe54"></a> `00bbfe54` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbfe58"></a> `00bbfe58` | `08 0d 09 8b` | add x8,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbfe5c"></a> `00bbfe5c` | `15 a0 00 a9` | stp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfe60"></a> `00bbfe60` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbfe64"></a> `00bbfe64` | `a9 22 00 91` | add x9,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bbfe68"></a> `00bbfe68` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfe6c"></a> `00bbfe6c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00bbfe70"></a> `00bbfe70` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfe74"></a> `00bbfe74` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfe78"></a> `00bbfe78` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfe7c"></a> `00bbfe7c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfe80"></a> `00bbfe80` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfe84"></a> `00bbfe84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfe88"></a> `00bbfe88` | `fa 78 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfdb4`](#insn-00bbfdb4) 範囲 `[['00bbfdb4', '00bbfdc3']]`
  - `FALL_THROUGH` [`00bbfdc0`](#insn-00bbfdc0) → [`00bbfdc4`](#insn-00bbfdc4)
- ブロック [`00bbfdc4`](#insn-00bbfdc4) 範囲 `[['00bbfdc4', '00bbfdcf']]`
  - `FALL_THROUGH` [`00bbfdcc`](#insn-00bbfdcc) → [`00bbfdd0`](#insn-00bbfdd0)
- ブロック [`00bbfdd0`](#insn-00bbfdd0) 範囲 `[['00bbfdd0', '00bbfdd7']]`
  - `CONDITIONAL_JUMP` [`00bbfdd4`](#insn-00bbfdd4) → [`00bbfe60`](#insn-00bbfe60)
  - `FALL_THROUGH` [`00bbfdd4`](#insn-00bbfdd4) → [`00bbfdd8`](#insn-00bbfdd8)
- ブロック [`00bbfdd8`](#insn-00bbfdd8) 範囲 `[['00bbfdd8', '00bbfdf3']]`
  - `FALL_THROUGH` [`00bbfdf0`](#insn-00bbfdf0) → [`00bbfdf4`](#insn-00bbfdf4)
- ブロック [`00bbfdf4`](#insn-00bbfdf4) 範囲 `[['00bbfdf4', '00bbfdf7']]`
  - `CONDITIONAL_JUMP` [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfe14`](#insn-00bbfe14)
  - `FALL_THROUGH` [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfdf8`](#insn-00bbfdf8)
- ブロック [`00bbfdf8`](#insn-00bbfdf8) 範囲 `[['00bbfdf8', '00bbfe0f']]`
  - `CONDITIONAL_JUMP` [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe4c`](#insn-00bbfe4c)
  - `FALL_THROUGH` [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe10`](#insn-00bbfe10)
- ブロック [`00bbfe10`](#insn-00bbfe10) 範囲 `[['00bbfe10', '00bbfe13']]`
- ブロック [`00bbfe14`](#insn-00bbfe14) 範囲 `[['00bbfe14', '00bbfe1f']]`
  - `CONDITIONAL_JUMP` [`00bbfe1c`](#insn-00bbfe1c) → [`00bbfe88`](#insn-00bbfe88)
  - `FALL_THROUGH` [`00bbfe1c`](#insn-00bbfe1c) → [`00bbfe20`](#insn-00bbfe20)
- ブロック [`00bbfe20`](#insn-00bbfe20) 範囲 `[['00bbfe20', '00bbfe2b']]`
  - `CONDITIONAL_JUMP` [`00bbfe28`](#insn-00bbfe28) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfe28`](#insn-00bbfe28) → [`00bbfe2c`](#insn-00bbfe2c)
- ブロック [`00bbfe2c`](#insn-00bbfe2c) 範囲 `[['00bbfe2c', '00bbfe43']]`
  - `FALL_THROUGH` [`00bbfe40`](#insn-00bbfe40) → [`00bbfe44`](#insn-00bbfe44)
- ブロック [`00bbfe44`](#insn-00bbfe44) 範囲 `[['00bbfe44', '00bbfe4b']]`
  - `FALL_THROUGH` [`00bbfe48`](#insn-00bbfe48) → [`00bbfe4c`](#insn-00bbfe4c)
- ブロック [`00bbfe4c`](#insn-00bbfe4c) 範囲 `[['00bbfe4c', '00bbfe5f']]`
  - `FALL_THROUGH` [`00bbfe5c`](#insn-00bbfe5c) → [`00bbfe60`](#insn-00bbfe60)
- ブロック [`00bbfe60`](#insn-00bbfe60) 範囲 `[['00bbfe60', '00bbfe7b']]`
  - `FALL_THROUGH` [`00bbfe78`](#insn-00bbfe78) → [`00bbfe7c`](#insn-00bbfe7c)
- ブロック [`00bbfe7c`](#insn-00bbfe7c) 範囲 `[['00bbfe7c', '00bbfe87']]`
- ブロック [`00bbfe88`](#insn-00bbfe88) 範囲 `[['00bbfe88', '00bbfe8b']]`

## 命令位置別の参照

- [`00bbfdb8`](#insn-00bbfdb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdbc`](#insn-00bbfdbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdc0`](#insn-00bbfdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdc4`](#insn-00bbfdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdd4`](#insn-00bbfdd4) → [`00bbfe60`](#insn-00bbfe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfe14`](#insn-00bbfe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdfc`](#insn-00bbfdfc) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe4c`](#insn-00bbfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe10`](#insn-00bbfe10) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe18`](#insn-00bbfe18) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe1c`](#insn-00bbfe1c) → [`00bbfe88`](#insn-00bbfe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe28`](#insn-00bbfe28) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe3c`](#insn-00bbfe3c) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe70`](#insn-00bbfe70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe74`](#insn-00bbfe74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe78`](#insn-00bbfe78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe7c`](#insn-00bbfe7c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe88`](#insn-00bbfe88) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfdb8`](#insn-00bbfdb8)

~~~json
{
  "source": "00bbfdb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdbc`](#insn-00bbfdbc)

~~~json
{
  "source": "00bbfdbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdc0`](#insn-00bbfdc0)

~~~json
{
  "source": "00bbfdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdc4`](#insn-00bbfdc4)

~~~json
{
  "source": "00bbfdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdd4`](#insn-00bbfdd4)

~~~json
{
  "source": "00bbfdd4",
  "target": "00bbfe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdf4`](#insn-00bbfdf4)

~~~json
{
  "source": "00bbfdf4",
  "target": "00bbfe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdfc`](#insn-00bbfdfc)

~~~json
{
  "source": "00bbfdfc",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe0c`](#insn-00bbfe0c)

~~~json
{
  "source": "00bbfe0c",
  "target": "00bbfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe10`](#insn-00bbfe10)

~~~json
{
  "source": "00bbfe10",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe18`](#insn-00bbfe18)

~~~json
{
  "source": "00bbfe18",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe1c`](#insn-00bbfe1c)

~~~json
{
  "source": "00bbfe1c",
  "target": "00bbfe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe28`](#insn-00bbfe28)

~~~json
{
  "source": "00bbfe28",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe3c`](#insn-00bbfe3c)

~~~json
{
  "source": "00bbfe3c",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe70`](#insn-00bbfe70)

~~~json
{
  "source": "00bbfe70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe74`](#insn-00bbfe74)

~~~json
{
  "source": "00bbfe74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe78`](#insn-00bbfe78)

~~~json
{
  "source": "00bbfe78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe7c`](#insn-00bbfe7c)

~~~json
{
  "source": "00bbfe7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe88`](#insn-00bbfe88)

~~~json
{
  "source": "00bbfe88",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
