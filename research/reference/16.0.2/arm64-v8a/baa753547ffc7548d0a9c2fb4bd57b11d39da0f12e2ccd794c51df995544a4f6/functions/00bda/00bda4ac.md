# 00bda4ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bda410`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-80fcfd40dc0ac36d14b2d592880c20a3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdb4a0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb4a0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-4c2da828246bb0cbfeb2b251f7ee55ac)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda4ac",
  "name": "_ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e684b7a814888622a7641a9c9a1b9bcb7be0717675f8ce2c05cd72087a8df0e4",
  "source_text_sha256": "e684b7a814888622a7641a9c9a1b9bcb7be0717675f8ce2c05cd72087a8df0e4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda4ac",
        "00bda59b"
      ]
    ],
    "bytes_sha256": "469057af4df1d654c1d07eb6091c5985335bdcbdfbc4746df90cde62a0f5dbba",
    "instruction_count": 60,
    "instruction_bytes": 240,
    "body_bytes": 240,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5dc20](../00c5d/00c5dc20.md)
- [00c5dea0](../00c5d/00c5dea0.md)
- [00c5df20](../00c5d/00c5df20.md)

## 関連文字列（未確認候補）

~~~text
"GameCenter is not supported on Android."
"is_gamecenter_available_on_android"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1888 bytes

~~~c

void _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv(undefined8 param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  undefined1 auStack_68 [16];
  undefined1 auStack_58 [16];
  undefined1 auStack_48 [16];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar2 = _ZN8firebase4auth23GetCredentialFutureImplEv();
  puVar3 = (undefined8 *)_Znwm(0x28);
  *puVar3 = 0;
  *(undefined4 *)(puVar3 + 1) = 0;
  puVar3[3] = 0;
  puVar3[4] = 0;
  puVar3[2] = 0;
                    /* try { // try from 00bda4f0 to 00cda4fb has its CatchHandler @ 00bdef30 */
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_48,uVar2,0,puVar3,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv_00c9bb00
            );
                    /* try { // try from 00bda510 to 00cda52f has its CatchHandler @ 00bdeef8 */
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_58,auStack_48);
  _ZN8firebase12FutureHandleD2Ev(auStack_48);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,auStack_58);
                    /* try { // try from 00bda530 to 00cdb763 has its CatchHandler @ 00bd6fbc */
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
            (uVar2,auStack_68,4,"GameCenter is not supported on Android.",auStack_48);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  _ZN8firebase9LogAssertEPKcz("is_gamecenter_available_on_android");
  _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,uVar2,auStack_58);
  _ZN8firebase12FutureHandleD2Ev(auStack_58);
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00bda4ac"></a> `00bda4ac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bda4b0"></a> `00bda4b0` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda4b4"></a> `00bda4b4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bda4b8"></a> `00bda4b8` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bda4bc"></a> `00bda4bc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bda4c0"></a> `00bda4c0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bda4c4"></a> `00bda4c4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bda4c8"></a> `00bda4c8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bda4cc"></a> `00bda4cc` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bda4d0"></a> `00bda4d0` | `d4 0d 02 94` | bl 0x00c5dc20 | `UNCONDITIONAL_CALL`
<a id="insn-00bda4d4"></a> `00bda4d4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda4d8"></a> `00bda4d8` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00bda4dc"></a> `00bda4dc` | `a1 f6 01 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bda4e0"></a> `00bda4e0` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bda4e4"></a> `00bda4e4` | `1f 08 00 b9` | str wzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bda4e8"></a> `00bda4e8` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bda4ec"></a> `00bda4ec` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bda4f0"></a> `00bda4f0` | `03 06 00 b0` | adrp x3,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bda4f4"></a> `00bda4f4` | `63 80 45 f9` | ldr x3,[x3, #0xb00] | `FALL_THROUGH`
<a id="insn-00bda4f8"></a> `00bda4f8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bda4fc"></a> `00bda4fc` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bda500"></a> `00bda500` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda504"></a> `00bda504` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bda508"></a> `00bda508` | `82 02 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bda50c"></a> `00bda50c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bda510"></a> `00bda510` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bda514"></a> `00bda514` | `6f 02 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda518"></a> `00bda518` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bda51c"></a> `00bda51c` | `91 01 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bda520"></a> `00bda520` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda524"></a> `00bda524` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bda528"></a> `00bda528` | `6a 02 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda52c"></a> `00bda52c` | `e3 b6 ff f0` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bda530"></a> `00bda530` | `63 70 32 91` | add x3,x3,#0xc9c | `FALL_THROUGH`
<a id="insn-00bda534"></a> `00bda534` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda538"></a> `00bda538` | `e4 a3 00 91` | add x4,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bda53c"></a> `00bda53c` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00bda540"></a> `00bda540` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda544"></a> `00bda544` | `57 0e 02 94` | bl 0x00c5dea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda548"></a> `00bda548` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda54c"></a> `00bda54c` | `85 01 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bda550"></a> `00bda550` | `c0 b6 ff d0` | adrp x0,0x2b4000 | `FALL_THROUGH`
<a id="insn-00bda554"></a> `00bda554` | `00 60 25 91` | add x0,x0,#0x958 | `FALL_THROUGH`
<a id="insn-00bda558"></a> `00bda558` | `de 02 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda55c"></a> `00bda55c` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bda560"></a> `00bda560` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bda564"></a> `00bda564` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bda568"></a> `00bda568` | `6e 0e 02 94` | bl 0x00c5df20 | `UNCONDITIONAL_CALL`
<a id="insn-00bda56c"></a> `00bda56c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bda570"></a> `00bda570` | `7c 01 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bda574"></a> `00bda574` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bda578"></a> `00bda578` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bda57c"></a> `00bda57c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bda580"></a> `00bda580` | `c1 00 00 54` | b.ne 0x00bda598 | `CONDITIONAL_JUMP`
<a id="insn-00bda584"></a> `00bda584` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bda588"></a> `00bda588` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bda58c"></a> `00bda58c` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda590"></a> `00bda590` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bda594"></a> `00bda594` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bda598"></a> `00bda598` | `86 f6 01 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bda4ac`](#insn-00bda4ac) 範囲 `[['00bda4ac', '00bda4ef']]`
  - `FALL_THROUGH` [`00bda4ec`](#insn-00bda4ec) → [`00bda4f0`](#insn-00bda4f0)
- ブロック [`00bda4f0`](#insn-00bda4f0) 範囲 `[['00bda4f0', '00bda50f']]`
  - `FALL_THROUGH` [`00bda50c`](#insn-00bda50c) → [`00bda510`](#insn-00bda510)
- ブロック [`00bda510`](#insn-00bda510) 範囲 `[['00bda510', '00bda52f']]`
  - `FALL_THROUGH` [`00bda52c`](#insn-00bda52c) → [`00bda530`](#insn-00bda530)
- ブロック [`00bda530`](#insn-00bda530) 範囲 `[['00bda530', '00bda583']]`
  - `CONDITIONAL_JUMP` [`00bda580`](#insn-00bda580) → [`00bda598`](#insn-00bda598)
  - `FALL_THROUGH` [`00bda580`](#insn-00bda580) → [`00bda584`](#insn-00bda584)
- ブロック [`00bda584`](#insn-00bda584) 範囲 `[['00bda584', '00bda597']]`
- ブロック [`00bda598`](#insn-00bda598) 範囲 `[['00bda598', '00bda59b']]`

## 命令位置別の参照

- [`00bda4b0`](#insn-00bda4b0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda4b4`](#insn-00bda4b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda4b8`](#insn-00bda4b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda4cc`](#insn-00bda4cc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda4d0`](#insn-00bda4d0) → [`00c5dc20`](../00c5d/00c5dc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc20` · 推定シンボル `None` · 推定型 `None`
- [`00bda4dc`](#insn-00bda4dc) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bda4f4`](#insn-00bda4f4) → `00c9bb00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bda4f4`](#insn-00bda4f4) → [`00bdc4c4`](../00bdc/00bdc4c4.md) · `PARAM` · `ANALYSIS` · 関数 `00bdc4c4` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv` · 推定型 `None`
- [`00bda508`](#insn-00bda508) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bda514`](#insn-00bda514) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bda51c`](#insn-00bda51c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bda528`](#insn-00bda528) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bda530`](#insn-00bda530) → `002b9c9c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda544`](#insn-00bda544) → [`00c5dea0`](../00c5d/00c5dea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dea0` · 推定シンボル `None` · 推定型 `None`
- [`00bda54c`](#insn-00bda54c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bda554`](#insn-00bda554) → `002b4958`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda558`](#insn-00bda558) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bda568`](#insn-00bda568) → [`00c5df20`](../00c5d/00c5df20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5df20` · 推定シンボル `None` · 推定型 `None`
- [`00bda570`](#insn-00bda570) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bda578`](#insn-00bda578) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda580`](#insn-00bda580) → [`00bda598`](#insn-00bda598) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda584`](#insn-00bda584) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda588`](#insn-00bda588) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda58c`](#insn-00bda58c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda598`](#insn-00bda598) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda4b0`](#insn-00bda4b0)

~~~json
{
  "source": "00bda4b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda4b4`](#insn-00bda4b4)

~~~json
{
  "source": "00bda4b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda4b8`](#insn-00bda4b8)

~~~json
{
  "source": "00bda4b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda4cc`](#insn-00bda4cc)

~~~json
{
  "source": "00bda4cc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda4d0`](#insn-00bda4d0)

~~~json
{
  "source": "00bda4d0",
  "target": "00c5dc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda4dc`](#insn-00bda4dc)

~~~json
{
  "source": "00bda4dc",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda4f4`](#insn-00bda4f4)

~~~json
{
  "source": "00bda4f4",
  "target": "00c9bb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bb00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bda4f4`](#insn-00bda4f4)

~~~json
{
  "source": "00bda4f4",
  "target": "00bdc4c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda508`](#insn-00bda508)

~~~json
{
  "source": "00bda508",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda514`](#insn-00bda514)

~~~json
{
  "source": "00bda514",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda51c`](#insn-00bda51c)

~~~json
{
  "source": "00bda51c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda528`](#insn-00bda528)

~~~json
{
  "source": "00bda528",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda530`](#insn-00bda530)

~~~json
{
  "source": "00bda530",
  "target": "002b9c9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9c9c",
  "offset": 0,
  "size": 40,
  "datatype": "string",
  "bytes": "47616d6543656e746572206973206e6f7420737570706f72746564206f6e2041",
  "capture_start": "002b9c9c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bda544`](#insn-00bda544)

~~~json
{
  "source": "00bda544",
  "target": "00c5dea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda54c`](#insn-00bda54c)

~~~json
{
  "source": "00bda54c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda554`](#insn-00bda554)

~~~json
{
  "source": "00bda554",
  "target": "002b4958",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4958",
  "offset": 0,
  "size": 35,
  "datatype": "string",
  "bytes": "69735f67616d6563656e7465725f617661696c61626c655f6f6e5f616e64726f",
  "capture_start": "002b4958",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bda558`](#insn-00bda558)

~~~json
{
  "source": "00bda558",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda568`](#insn-00bda568)

~~~json
{
  "source": "00bda568",
  "target": "00c5df20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda570`](#insn-00bda570)

~~~json
{
  "source": "00bda570",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda578`](#insn-00bda578)

~~~json
{
  "source": "00bda578",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda580`](#insn-00bda580)

~~~json
{
  "source": "00bda580",
  "target": "00bda598",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda584`](#insn-00bda584)

~~~json
{
  "source": "00bda584",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda588`](#insn-00bda588)

~~~json
{
  "source": "00bda588",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda58c`](#insn-00bda58c)

~~~json
{
  "source": "00bda58c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda598`](#insn-00bda598)

~~~json
{
  "source": "00bda598",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
