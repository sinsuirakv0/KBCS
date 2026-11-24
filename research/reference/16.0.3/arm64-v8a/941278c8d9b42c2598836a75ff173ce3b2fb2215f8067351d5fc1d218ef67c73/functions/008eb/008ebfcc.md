# 008ebfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008eb020`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb020.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0054.md#compare-a9466c44992792aa6d43c5ff20204879)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008ebfcc",
  "name": "FUN_008ebfcc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7391e77aaa9f66185cf3ccc2b9b4ea694752e7e24787a2703f6749bc776d8ffa",
  "source_text_sha256": "7391e77aaa9f66185cf3ccc2b9b4ea694752e7e24787a2703f6749bc776d8ffa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008ebfcc",
        "008ec0cf"
      ]
    ],
    "bytes_sha256": "7c6c678610783bf876b53e7a0d6a30906fc5bdb8342a543014a9cf70617ed019",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [004692e8](../00469/004692e8.md)
- [00469f64](../00469/00469f64.md)
- [008524fc](../00852/008524fc.md)
- [008ba294](../008ba/008ba294.md)
- [008ba29c](../008ba/008ba29c.md)
- [00a83b64](../00a83/00a83b64.md)
- [00a845ec](../00a84/00a845ec.md)
- [00c596b0](../00c59/00c596b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1575 bytes

~~~c

void FUN_008ebfcc(long param_1,undefined8 *param_2)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  int iVar4;
  undefined8 uVar5;
  long lVar6;
  int iVar7;
  
  uVar5 = *param_2;
  lVar6 = *(long *)(param_1 + 8);
  iVar1 = FUN_008ba294(uVar5);
  if (iVar1 != 0) {
    uVar5 = FUN_008ba29c(uVar5);
                    /* try { // try from 008ebff8 to 009ec007 has its CatchHandler @ 008f00a8 */
    if (DAT_00ca5a38 == 0) {
      lVar2 = 0;
    }
    else {
                    /* try { // try from 008ec008 to 009ec06b has its CatchHandler @ 008e00a4 */
      lVar2 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c748b0,0);
    }
    uVar3 = FUN_00467bc0();
    iVar4 = (int)uVar5;
    iVar7 = (int)((ulong)uVar5 >> 0x20);
    FUN_004692e8(uVar3,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xb9,iVar7 + -0x34,0);
    uVar5 = FUN_00467bc0();
                    /* try { // try from 008ec06c to 009ec07b has its CatchHandler @ 008f00a8 */
                    /* try { // try from 008ec07c to 009ec0d3 has its CatchHandler @ 008e00a4 */
    FUN_00469f64(uVar5,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xca,iVar7 + 0x2a,0x120,0x57,
                 *(int *)(lVar6 + 0x2c0) + 4);
    lVar6 = FUN_008524fc();
    iVar1 = FUN_00a83b64(lVar6 + 0x3078,0xd);
    lVar6 = FUN_008524fc();
    if (iVar1 < 0) {
      iVar1 = iVar1 + 1;
    }
    FUN_00a845ec(0x3f800000,lVar6 + 0x3078,0xd,(iVar4 - (iVar1 >> 1)) + 0x159,iVar7 + 0x96,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008ebfcc"></a> `008ebfcc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-008ebfd0"></a> `008ebfd0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ebfd4"></a> `008ebfd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ebfd8"></a> `008ebfd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008ebfdc"></a> `008ebfdc` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-008ebfe0"></a> `008ebfe0` | `15 04 40 f9` | ldr x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008ebfe4"></a> `008ebfe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ebfe8"></a> `008ebfe8` | `ab 38 ff 97` | bl 0x008ba294 | `UNCONDITIONAL_CALL`
<a id="insn-008ebfec"></a> `008ebfec` | `00 02 00 34` | cbz w0,0x008ec02c | `CONDITIONAL_JUMP`
<a id="insn-008ebff0"></a> `008ebff0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ebff4"></a> `008ebff4` | `aa 38 ff 97` | bl 0x008ba29c | `UNCONDITIONAL_CALL`
<a id="insn-008ebff8"></a> `008ebff8` | `c8 1d 00 d0` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-008ebffc"></a> `008ebffc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008ec000"></a> `008ec000` | `08 1d 45 f9` | ldr x8,[x8, #0xa38] | `FALL_THROUGH`
<a id="insn-008ec004"></a> `008ec004` | `c8 01 00 b4` | cbz x8,0x008ec03c | `CONDITIONAL_JUMP`
<a id="insn-008ec008"></a> `008ec008` | `c1 1b 00 d0` | adrp x1,0xc66000 | `FALL_THROUGH`
<a id="insn-008ec00c"></a> `008ec00c` | `21 e0 3b 91` | add x1,x1,#0xef8 | `FALL_THROUGH`
<a id="insn-008ec010"></a> `008ec010` | `42 1c 00 90` | adrp x2,0xc74000 | `FALL_THROUGH`
<a id="insn-008ec014"></a> `008ec014` | `42 c0 22 91` | add x2,x2,#0x8b0 | `FALL_THROUGH`
<a id="insn-008ec018"></a> `008ec018` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-008ec01c"></a> `008ec01c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-008ec020"></a> `008ec020` | `a4 b5 0d 94` | bl 0x00c596b0 | `UNCONDITIONAL_CALL`
<a id="insn-008ec024"></a> `008ec024` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-008ec028"></a> `008ec028` | `06 00 00 14` | b 0x008ec040 | `UNCONDITIONAL_JUMP`
<a id="insn-008ec02c"></a> `008ec02c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ec030"></a> `008ec030` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ec034"></a> `008ec034` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-008ec038"></a> `008ec038` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008ec03c"></a> `008ec03c` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-008ec040"></a> `008ec040` | `e0 ee ed 97` | bl 0x00467bc0 | `UNCONDITIONAL_CALL`
<a id="insn-008ec044"></a> `008ec044` | `76 fe 60 d3` | lsr x22,x19,#0x20 | `FALL_THROUGH`
<a id="insn-008ec048"></a> `008ec048` | `81 ca 41 f9` | ldr x1,[x20, #0x390] | `FALL_THROUGH`
<a id="insn-008ec04c"></a> `008ec04c` | `62 e6 02 11` | add w2,w19,#0xb9 | `FALL_THROUGH`
<a id="insn-008ec050"></a> `008ec050` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-008ec054"></a> `008ec054` | `c3 d2 00 51` | sub w3,w22,#0x34 | `FALL_THROUGH`
<a id="insn-008ec058"></a> `008ec058` | `a4 f4 ed 97` | bl 0x004692e8 | `UNCONDITIONAL_CALL`
<a id="insn-008ec05c"></a> `008ec05c` | `d9 ee ed 97` | bl 0x00467bc0 | `UNCONDITIONAL_CALL`
<a id="insn-008ec060"></a> `008ec060` | `a8 c2 42 b9` | ldr w8,[x21, #0x2c0] | `FALL_THROUGH`
<a id="insn-008ec064"></a> `008ec064` | `81 ca 41 f9` | ldr x1,[x20, #0x390] | `FALL_THROUGH`
<a id="insn-008ec068"></a> `008ec068` | `62 2a 03 11` | add w2,w19,#0xca | `FALL_THROUGH`
<a id="insn-008ec06c"></a> `008ec06c` | `c3 aa 00 11` | add w3,w22,#0x2a | `FALL_THROUGH`
<a id="insn-008ec070"></a> `008ec070` | `04 24 80 52` | mov w4,#0x120 | `FALL_THROUGH`
<a id="insn-008ec074"></a> `008ec074` | `e5 0a 80 52` | mov w5,#0x57 | `FALL_THROUGH`
<a id="insn-008ec078"></a> `008ec078` | `06 11 00 11` | add w6,w8,#0x4 | `FALL_THROUGH`
<a id="insn-008ec07c"></a> `008ec07c` | `ba f7 ed 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-008ec080"></a> `008ec080` | `1f 99 fd 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008ec084"></a> `008ec084` | `15 0f 86 52` | mov w21,#0x3078 | `FALL_THROUGH`
<a id="insn-008ec088"></a> `008ec088` | `a1 01 80 52` | mov w1,#0xd | `FALL_THROUGH`
<a id="insn-008ec08c"></a> `008ec08c` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008ec090"></a> `008ec090` | `b5 5e 06 94` | bl 0x00a83b64 | `UNCONDITIONAL_CALL`
<a id="insn-008ec094"></a> `008ec094` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-008ec098"></a> `008ec098` | `19 99 fd 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008ec09c"></a> `008ec09c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-008ec0a0"></a> `008ec0a0` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-008ec0a4"></a> `008ec0a4` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008ec0a8"></a> `008ec0a8` | `88 a6 94 1a` | cinc w8,w20,lt | `FALL_THROUGH`
<a id="insn-008ec0ac"></a> `008ec0ac` | `c3 5a 02 11` | add w3,w22,#0x96 | `FALL_THROUGH`
<a id="insn-008ec0b0"></a> `008ec0b0` | `a1 01 80 52` | mov w1,#0xd | `FALL_THROUGH`
<a id="insn-008ec0b4"></a> `008ec0b4` | `68 06 88 4b` | sub w8,w19,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-008ec0b8"></a> `008ec0b8` | `02 65 05 11` | add w2,w8,#0x159 | `FALL_THROUGH`
<a id="insn-008ec0bc"></a> `008ec0bc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-008ec0c0"></a> `008ec0c0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ec0c4"></a> `008ec0c4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ec0c8"></a> `008ec0c8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-008ec0cc"></a> `008ec0cc` | `48 61 06 14` | b 0x00a845ec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008ebfcc`](#insn-008ebfcc) 範囲 `[['008ebfcc', '008ebfef']]`
  - `CONDITIONAL_JUMP` [`008ebfec`](#insn-008ebfec) → [`008ec02c`](#insn-008ec02c)
  - `FALL_THROUGH` [`008ebfec`](#insn-008ebfec) → [`008ebff0`](#insn-008ebff0)
- ブロック [`008ebff0`](#insn-008ebff0) 範囲 `[['008ebff0', '008ebff7']]`
  - `FALL_THROUGH` [`008ebff4`](#insn-008ebff4) → [`008ebff8`](#insn-008ebff8)
- ブロック [`008ebff8`](#insn-008ebff8) 範囲 `[['008ebff8', '008ec007']]`
  - `CONDITIONAL_JUMP` [`008ec004`](#insn-008ec004) → [`008ec03c`](#insn-008ec03c)
  - `FALL_THROUGH` [`008ec004`](#insn-008ec004) → [`008ec008`](#insn-008ec008)
- ブロック [`008ec008`](#insn-008ec008) 範囲 `[['008ec008', '008ec02b']]`
  - `UNCONDITIONAL_JUMP` [`008ec028`](#insn-008ec028) → [`008ec040`](#insn-008ec040)
- ブロック [`008ec02c`](#insn-008ec02c) 範囲 `[['008ec02c', '008ec03b']]`
- ブロック [`008ec03c`](#insn-008ec03c) 範囲 `[['008ec03c', '008ec03f']]`
  - `FALL_THROUGH` [`008ec03c`](#insn-008ec03c) → [`008ec040`](#insn-008ec040)
- ブロック [`008ec040`](#insn-008ec040) 範囲 `[['008ec040', '008ec06b']]`
  - `FALL_THROUGH` [`008ec068`](#insn-008ec068) → [`008ec06c`](#insn-008ec06c)
- ブロック [`008ec06c`](#insn-008ec06c) 範囲 `[['008ec06c', '008ec07b']]`
  - `FALL_THROUGH` [`008ec078`](#insn-008ec078) → [`008ec07c`](#insn-008ec07c)
- ブロック [`008ec07c`](#insn-008ec07c) 範囲 `[['008ec07c', '008ec0cf']]`

## 命令位置別の参照

- [`008ebfcc`](#insn-008ebfcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebfd0`](#insn-008ebfd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebfd4`](#insn-008ebfd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebfe8`](#insn-008ebfe8) → [`008ba294`](../008ba/008ba294.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba294` · 推定シンボル `None` · 推定型 `None`
- [`008ebfec`](#insn-008ebfec) → [`008ec02c`](#insn-008ec02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebff4`](#insn-008ebff4) → [`008ba29c`](../008ba/008ba29c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba29c` · 推定シンボル `None` · 推定型 `None`
- [`008ec000`](#insn-008ec000) → `00ca5a38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008ec004`](#insn-008ec004) → [`008ec03c`](#insn-008ec03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec00c`](#insn-008ec00c) → `00c66ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`008ec014`](#insn-008ec014) → `00c748b0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`008ec020`](#insn-008ec020) → [`00c596b0`](../00c59/00c596b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596b0` · 推定シンボル `None` · 推定型 `None`
- [`008ec028`](#insn-008ec028) → [`008ec040`](#insn-008ec040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec02c`](#insn-008ec02c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec030`](#insn-008ec030) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec034`](#insn-008ec034) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec040`](#insn-008ec040) → [`00467bc0`](../00467/00467bc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467bc0` · 推定シンボル `None` · 推定型 `None`
- [`008ec058`](#insn-008ec058) → [`004692e8`](../00469/004692e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004692e8` · 推定シンボル `None` · 推定型 `None`
- [`008ec05c`](#insn-008ec05c) → [`00467bc0`](../00467/00467bc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467bc0` · 推定シンボル `None` · 推定型 `None`
- [`008ec07c`](#insn-008ec07c) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`008ec080`](#insn-008ec080) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008ec090`](#insn-008ec090) → [`00a83b64`](../00a83/00a83b64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83b64` · 推定シンボル `None` · 推定型 `None`
- [`008ec098`](#insn-008ec098) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008ec0c0`](#insn-008ec0c0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec0c4`](#insn-008ec0c4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec0c8`](#insn-008ec0c8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ec0cc`](#insn-008ec0cc) → [`00a845ec`](../00a84/00a845ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a845ec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008ebfcc`](#insn-008ebfcc)

~~~json
{
  "source": "008ebfcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebfd0`](#insn-008ebfd0)

~~~json
{
  "source": "008ebfd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebfd4`](#insn-008ebfd4)

~~~json
{
  "source": "008ebfd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebfe8`](#insn-008ebfe8)

~~~json
{
  "source": "008ebfe8",
  "target": "008ba294",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebfec`](#insn-008ebfec)

~~~json
{
  "source": "008ebfec",
  "target": "008ec02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebff4`](#insn-008ebff4)

~~~json
{
  "source": "008ebff4",
  "target": "008ba29c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec000`](#insn-008ec000)

~~~json
{
  "source": "008ec000",
  "target": "00ca5a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5a38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008ec004`](#insn-008ec004)

~~~json
{
  "source": "008ec004",
  "target": "008ec03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec00c`](#insn-008ec00c)

~~~json
{
  "source": "008ec00c",
  "target": "00c66ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66ef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ec014`](#insn-008ec014)

~~~json
{
  "source": "008ec014",
  "target": "00c748b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c748b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ec020`](#insn-008ec020)

~~~json
{
  "source": "008ec020",
  "target": "00c596b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec028`](#insn-008ec028)

~~~json
{
  "source": "008ec028",
  "target": "008ec040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec02c`](#insn-008ec02c)

~~~json
{
  "source": "008ec02c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec030`](#insn-008ec030)

~~~json
{
  "source": "008ec030",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec034`](#insn-008ec034)

~~~json
{
  "source": "008ec034",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec040`](#insn-008ec040)

~~~json
{
  "source": "008ec040",
  "target": "00467bc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec058`](#insn-008ec058)

~~~json
{
  "source": "008ec058",
  "target": "004692e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec05c`](#insn-008ec05c)

~~~json
{
  "source": "008ec05c",
  "target": "00467bc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec07c`](#insn-008ec07c)

~~~json
{
  "source": "008ec07c",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec080`](#insn-008ec080)

~~~json
{
  "source": "008ec080",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec090`](#insn-008ec090)

~~~json
{
  "source": "008ec090",
  "target": "00a83b64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec098`](#insn-008ec098)

~~~json
{
  "source": "008ec098",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ec0c0`](#insn-008ec0c0)

~~~json
{
  "source": "008ec0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec0c4`](#insn-008ec0c4)

~~~json
{
  "source": "008ec0c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec0c8`](#insn-008ec0c8)

~~~json
{
  "source": "008ec0c8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ec0cc`](#insn-008ec0cc)

~~~json
{
  "source": "008ec0cc",
  "target": "00a845ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
