# 008eafcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `008eae30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0051.md#compare-ca283427f78e14ea58a60fdcbc9f05d3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `008eb020`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb020.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0053.md#compare-d006108770e1e1126c41e0adca303bbb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008eafcc",
  "name": "FUN_008eafcc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc1889f46a44a67d15200758d6c8d29a673108cfb8579cba496667359cfea59e",
  "source_text_sha256": "bc1889f46a44a67d15200758d6c8d29a673108cfb8579cba496667359cfea59e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008eafcc",
        "008eb0cf"
      ]
    ],
    "bytes_sha256": "bb98dd5545bf5aaae7a103698fc26250465ebb5ead9a62030c080bb21ace3b4c",
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

- [00467860](../00467/00467860.md)
- [00468f88](../00468/00468f88.md)
- [00469c04](../00469/00469c04.md)
- [008514f8](../00851/008514f8.md)
- [008b9290](../008b9/008b9290.md)
- [008b9298](../008b9/008b9298.md)
- [00a82b00](../00a82/00a82b00.md)
- [00a83588](../00a83/00a83588.md)
- [00c58610](../00c58/00c58610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1575 bytes

~~~c

void FUN_008eafcc(long param_1,undefined8 *param_2)

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
  iVar1 = FUN_008b9290(uVar5);
  if (iVar1 != 0) {
    uVar5 = FUN_008b9298(uVar5);
    if (DAT_00ca4978 == 0) {
                    /* try { // try from 008eb03c to 009eb04b has its CatchHandler @ 008ef0ec */
      lVar2 = 0;
    }
    else {
      lVar2 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c73810,0);
    }
    uVar3 = FUN_00467860();
    iVar4 = (int)uVar5;
                    /* try { // try from 008eb04c to 009eb0af has its CatchHandler @ 008df0e8 */
    iVar7 = (int)((ulong)uVar5 >> 0x20);
    FUN_00468f88(uVar3,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xb9,iVar7 + -0x34,0);
    uVar5 = FUN_00467860();
    FUN_00469c04(uVar5,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xca,iVar7 + 0x2a,0x120,0x57,
                 *(int *)(lVar6 + 0x2c0) + 4);
    lVar6 = FUN_008514f8();
    iVar1 = FUN_00a82b00(lVar6 + 0x3078,0xd);
    lVar6 = FUN_008514f8();
    if (iVar1 < 0) {
      iVar1 = iVar1 + 1;
    }
                    /* try { // try from 008eb0b0 to 009eb0bf has its CatchHandler @ 008ef0ec */
                    /* try { // try from 008eb0c0 to 009eb117 has its CatchHandler @ 008df0e8 */
    FUN_00a83588(0x3f800000,lVar6 + 0x3078,0xd,(iVar4 - (iVar1 >> 1)) + 0x159,iVar7 + 0x96,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008eafcc"></a> `008eafcc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-008eafd0"></a> `008eafd0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008eafd4"></a> `008eafd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008eafd8"></a> `008eafd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008eafdc"></a> `008eafdc` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-008eafe0"></a> `008eafe0` | `15 04 40 f9` | ldr x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008eafe4"></a> `008eafe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008eafe8"></a> `008eafe8` | `aa 38 ff 97` | bl 0x008b9290 | `UNCONDITIONAL_CALL`
<a id="insn-008eafec"></a> `008eafec` | `00 02 00 34` | cbz w0,0x008eb02c | `CONDITIONAL_JUMP`
<a id="insn-008eaff0"></a> `008eaff0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008eaff4"></a> `008eaff4` | `a9 38 ff 97` | bl 0x008b9298 | `UNCONDITIONAL_CALL`
<a id="insn-008eaff8"></a> `008eaff8` | `c8 1d 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-008eaffc"></a> `008eaffc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008eb000"></a> `008eb000` | `08 bd 44 f9` | ldr x8,[x8, #0x978] | `FALL_THROUGH`
<a id="insn-008eb004"></a> `008eb004` | `c8 01 00 b4` | cbz x8,0x008eb03c | `CONDITIONAL_JUMP`
<a id="insn-008eb008"></a> `008eb008` | `c1 1b 00 d0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-008eb00c"></a> `008eb00c` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-008eb010"></a> `008eb010` | `42 1c 00 90` | adrp x2,0xc73000 | `FALL_THROUGH`
<a id="insn-008eb014"></a> `008eb014` | `42 40 20 91` | add x2,x2,#0x810 | `FALL_THROUGH`
<a id="insn-008eb018"></a> `008eb018` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-008eb01c"></a> `008eb01c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-008eb020"></a> `008eb020` | `7c b5 0d 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-008eb024"></a> `008eb024` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-008eb028"></a> `008eb028` | `06 00 00 14` | b 0x008eb040 | `UNCONDITIONAL_JUMP`
<a id="insn-008eb02c"></a> `008eb02c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008eb030"></a> `008eb030` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008eb034"></a> `008eb034` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-008eb038"></a> `008eb038` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008eb03c"></a> `008eb03c` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-008eb040"></a> `008eb040` | `08 f2 ed 97` | bl 0x00467860 | `UNCONDITIONAL_CALL`
<a id="insn-008eb044"></a> `008eb044` | `76 fe 60 d3` | lsr x22,x19,#0x20 | `FALL_THROUGH`
<a id="insn-008eb048"></a> `008eb048` | `81 ca 41 f9` | ldr x1,[x20, #0x390] | `FALL_THROUGH`
<a id="insn-008eb04c"></a> `008eb04c` | `62 e6 02 11` | add w2,w19,#0xb9 | `FALL_THROUGH`
<a id="insn-008eb050"></a> `008eb050` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-008eb054"></a> `008eb054` | `c3 d2 00 51` | sub w3,w22,#0x34 | `FALL_THROUGH`
<a id="insn-008eb058"></a> `008eb058` | `cc f7 ed 97` | bl 0x00468f88 | `UNCONDITIONAL_CALL`
<a id="insn-008eb05c"></a> `008eb05c` | `01 f2 ed 97` | bl 0x00467860 | `UNCONDITIONAL_CALL`
<a id="insn-008eb060"></a> `008eb060` | `a8 c2 42 b9` | ldr w8,[x21, #0x2c0] | `FALL_THROUGH`
<a id="insn-008eb064"></a> `008eb064` | `81 ca 41 f9` | ldr x1,[x20, #0x390] | `FALL_THROUGH`
<a id="insn-008eb068"></a> `008eb068` | `62 2a 03 11` | add w2,w19,#0xca | `FALL_THROUGH`
<a id="insn-008eb06c"></a> `008eb06c` | `c3 aa 00 11` | add w3,w22,#0x2a | `FALL_THROUGH`
<a id="insn-008eb070"></a> `008eb070` | `04 24 80 52` | mov w4,#0x120 | `FALL_THROUGH`
<a id="insn-008eb074"></a> `008eb074` | `e5 0a 80 52` | mov w5,#0x57 | `FALL_THROUGH`
<a id="insn-008eb078"></a> `008eb078` | `06 11 00 11` | add w6,w8,#0x4 | `FALL_THROUGH`
<a id="insn-008eb07c"></a> `008eb07c` | `e2 fa ed 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-008eb080"></a> `008eb080` | `1e 99 fd 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-008eb084"></a> `008eb084` | `15 0f 86 52` | mov w21,#0x3078 | `FALL_THROUGH`
<a id="insn-008eb088"></a> `008eb088` | `a1 01 80 52` | mov w1,#0xd | `FALL_THROUGH`
<a id="insn-008eb08c"></a> `008eb08c` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008eb090"></a> `008eb090` | `9c 5e 06 94` | bl 0x00a82b00 | `UNCONDITIONAL_CALL`
<a id="insn-008eb094"></a> `008eb094` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-008eb098"></a> `008eb098` | `18 99 fd 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-008eb09c"></a> `008eb09c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-008eb0a0"></a> `008eb0a0` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-008eb0a4"></a> `008eb0a4` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008eb0a8"></a> `008eb0a8` | `88 a6 94 1a` | cinc w8,w20,lt | `FALL_THROUGH`
<a id="insn-008eb0ac"></a> `008eb0ac` | `c3 5a 02 11` | add w3,w22,#0x96 | `FALL_THROUGH`
<a id="insn-008eb0b0"></a> `008eb0b0` | `a1 01 80 52` | mov w1,#0xd | `FALL_THROUGH`
<a id="insn-008eb0b4"></a> `008eb0b4` | `68 06 88 4b` | sub w8,w19,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-008eb0b8"></a> `008eb0b8` | `02 65 05 11` | add w2,w8,#0x159 | `FALL_THROUGH`
<a id="insn-008eb0bc"></a> `008eb0bc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-008eb0c0"></a> `008eb0c0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008eb0c4"></a> `008eb0c4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008eb0c8"></a> `008eb0c8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-008eb0cc"></a> `008eb0cc` | `2f 61 06 14` | b 0x00a83588 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008eafcc`](#insn-008eafcc) 範囲 `[['008eafcc', '008eafef']]`
  - `CONDITIONAL_JUMP` [`008eafec`](#insn-008eafec) → [`008eb02c`](#insn-008eb02c)
  - `FALL_THROUGH` [`008eafec`](#insn-008eafec) → [`008eaff0`](#insn-008eaff0)
- ブロック [`008eaff0`](#insn-008eaff0) 範囲 `[['008eaff0', '008eb007']]`
  - `CONDITIONAL_JUMP` [`008eb004`](#insn-008eb004) → [`008eb03c`](#insn-008eb03c)
  - `FALL_THROUGH` [`008eb004`](#insn-008eb004) → [`008eb008`](#insn-008eb008)
- ブロック [`008eb008`](#insn-008eb008) 範囲 `[['008eb008', '008eb02b']]`
  - `UNCONDITIONAL_JUMP` [`008eb028`](#insn-008eb028) → [`008eb040`](#insn-008eb040)
- ブロック [`008eb02c`](#insn-008eb02c) 範囲 `[['008eb02c', '008eb03b']]`
- ブロック [`008eb03c`](#insn-008eb03c) 範囲 `[['008eb03c', '008eb03f']]`
  - `FALL_THROUGH` [`008eb03c`](#insn-008eb03c) → [`008eb040`](#insn-008eb040)
- ブロック [`008eb040`](#insn-008eb040) 範囲 `[['008eb040', '008eb04b']]`
  - `FALL_THROUGH` [`008eb048`](#insn-008eb048) → [`008eb04c`](#insn-008eb04c)
- ブロック [`008eb04c`](#insn-008eb04c) 範囲 `[['008eb04c', '008eb0af']]`
  - `FALL_THROUGH` [`008eb0ac`](#insn-008eb0ac) → [`008eb0b0`](#insn-008eb0b0)
- ブロック [`008eb0b0`](#insn-008eb0b0) 範囲 `[['008eb0b0', '008eb0bf']]`
  - `FALL_THROUGH` [`008eb0bc`](#insn-008eb0bc) → [`008eb0c0`](#insn-008eb0c0)
- ブロック [`008eb0c0`](#insn-008eb0c0) 範囲 `[['008eb0c0', '008eb0cf']]`

## 命令位置別の参照

- [`008eafcc`](#insn-008eafcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eafd0`](#insn-008eafd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eafd4`](#insn-008eafd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eafe8`](#insn-008eafe8) → [`008b9290`](../008b9/008b9290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9290` · 推定シンボル `None` · 推定型 `None`
- [`008eafec`](#insn-008eafec) → [`008eb02c`](#insn-008eb02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eaff4`](#insn-008eaff4) → [`008b9298`](../008b9/008b9298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9298` · 推定シンボル `None` · 推定型 `None`
- [`008eb000`](#insn-008eb000) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008eb004`](#insn-008eb004) → [`008eb03c`](#insn-008eb03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb00c`](#insn-008eb00c) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`008eb014`](#insn-008eb014) → `00c73810`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`008eb020`](#insn-008eb020) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`008eb028`](#insn-008eb028) → [`008eb040`](#insn-008eb040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb02c`](#insn-008eb02c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb030`](#insn-008eb030) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb034`](#insn-008eb034) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb040`](#insn-008eb040) → [`00467860`](../00467/00467860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467860` · 推定シンボル `None` · 推定型 `None`
- [`008eb058`](#insn-008eb058) → [`00468f88`](../00468/00468f88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f88` · 推定シンボル `None` · 推定型 `None`
- [`008eb05c`](#insn-008eb05c) → [`00467860`](../00467/00467860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467860` · 推定シンボル `None` · 推定型 `None`
- [`008eb07c`](#insn-008eb07c) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`008eb080`](#insn-008eb080) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`008eb090`](#insn-008eb090) → [`00a82b00`](../00a82/00a82b00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a82b00` · 推定シンボル `None` · 推定型 `None`
- [`008eb098`](#insn-008eb098) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`008eb0c0`](#insn-008eb0c0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb0c4`](#insn-008eb0c4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb0c8`](#insn-008eb0c8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eb0cc`](#insn-008eb0cc) → [`00a83588`](../00a83/00a83588.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83588` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008eafcc`](#insn-008eafcc)

~~~json
{
  "source": "008eafcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eafd0`](#insn-008eafd0)

~~~json
{
  "source": "008eafd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eafd4`](#insn-008eafd4)

~~~json
{
  "source": "008eafd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eafe8`](#insn-008eafe8)

~~~json
{
  "source": "008eafe8",
  "target": "008b9290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eafec`](#insn-008eafec)

~~~json
{
  "source": "008eafec",
  "target": "008eb02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eaff4`](#insn-008eaff4)

~~~json
{
  "source": "008eaff4",
  "target": "008b9298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb000`](#insn-008eb000)

~~~json
{
  "source": "008eb000",
  "target": "00ca4978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008eb004`](#insn-008eb004)

~~~json
{
  "source": "008eb004",
  "target": "008eb03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb00c`](#insn-008eb00c)

~~~json
{
  "source": "008eb00c",
  "target": "00c65e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65e58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008eb014`](#insn-008eb014)

~~~json
{
  "source": "008eb014",
  "target": "00c73810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c73810",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008eb020`](#insn-008eb020)

~~~json
{
  "source": "008eb020",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb028`](#insn-008eb028)

~~~json
{
  "source": "008eb028",
  "target": "008eb040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb02c`](#insn-008eb02c)

~~~json
{
  "source": "008eb02c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb030`](#insn-008eb030)

~~~json
{
  "source": "008eb030",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb034`](#insn-008eb034)

~~~json
{
  "source": "008eb034",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb040`](#insn-008eb040)

~~~json
{
  "source": "008eb040",
  "target": "00467860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb058`](#insn-008eb058)

~~~json
{
  "source": "008eb058",
  "target": "00468f88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb05c`](#insn-008eb05c)

~~~json
{
  "source": "008eb05c",
  "target": "00467860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb07c`](#insn-008eb07c)

~~~json
{
  "source": "008eb07c",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb080`](#insn-008eb080)

~~~json
{
  "source": "008eb080",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb090`](#insn-008eb090)

~~~json
{
  "source": "008eb090",
  "target": "00a82b00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb098`](#insn-008eb098)

~~~json
{
  "source": "008eb098",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eb0c0`](#insn-008eb0c0)

~~~json
{
  "source": "008eb0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb0c4`](#insn-008eb0c4)

~~~json
{
  "source": "008eb0c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb0c8`](#insn-008eb0c8)

~~~json
{
  "source": "008eb0c8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eb0cc`](#insn-008eb0cc)

~~~json
{
  "source": "008eb0cc",
  "target": "00a83588",
  "target_space": "ram",
  "resolution": "function"
}
~~~
