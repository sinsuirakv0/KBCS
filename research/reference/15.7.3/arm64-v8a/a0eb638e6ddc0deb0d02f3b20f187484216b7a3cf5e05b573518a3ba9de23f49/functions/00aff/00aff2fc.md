# 00aff2fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aff234`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff234.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-d3afc1f67566376a536293ca7b913ea3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aff340`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff340.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-0285068fd8bd24a1c77e5fd9039ecc09)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aff2fc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acd864e0b7bbe72d954f88f327a88735d6575adda60d107883cd8922a434bcb3",
  "source_text_sha256": "acd864e0b7bbe72d954f88f327a88735d6575adda60d107883cd8922a434bcb3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aff2fc",
        "00aff3ab"
      ]
    ],
    "bytes_sha256": "c0e3418c3304c1c2eb98e88a1c8946cce7774ea04dcf7871a15f8ee56ac1b2fc",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddf90](../00bdd/00bddf90.md)

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"backing != nullptr"
"backing->status != kFutureStatusComplete"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2308 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE
               (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  int *piVar5;
  ulong uVar6;
  
                    /* catch() { ... } // from try @ 00af73fc with catch @ 00aff30c */
  uVar6 = *param_2;
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af74d0 with catch @ 00aff31c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 == (long *)0x0) {
LAB_00aff358:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
                    /* catch() { ... } // from try @ 00af73f0 with catch @ 00aff334 */
      if ((ulong)plVar3[4] >= uVar6) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar6];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00afd258 with catch @ 00aff34c */
    if ((plVar2 == plVar4) || (uVar6 < (ulong)plVar2[4])) goto LAB_00aff358;
    piVar5 = (int *)plVar2[5];
                    /* catch() { ... } // from try @ 00afcfb0 with catch @ 00aff39c */
                    /* catch() { ... } // from try @ 00afcf80 with catch @ 00aff3a0 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00afcf58 with catch @ 00aff3a4 */
    if (piVar5 != (int *)0x0) goto LAB_00aff370;
  }
                    /* catch() { ... } // from try @ 00afd178 with catch @ 00aff364 */
                    /* catch() { ... } // from try @ 00afd134 with catch @ 00aff368 */
  _ZN8firebase9LogAssertEPKcz("backing != nullptr");
  piVar5 = (int *)0x0;
LAB_00aff370:
  if (*piVar5 == 0) {
                    /* catch() { ... } // from try @ 00afd110 with catch @ 00aff37c */
                    /* catch() { ... } // from try @ 00afd0c0 with catch @ 00aff380 */
    _ZN8firebase9LogAssertEPKcz("backing->status != kFutureStatusComplete");
  }
                    /* catch() { ... } // from try @ 00afd070 with catch @ 00aff384 */
  *piVar5 = 0;
                    /* catch() { ... } // from try @ 00afd040 with catch @ 00aff388 */
                    /* catch() { ... } // from try @ 00afcff8 with catch @ 00aff38c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aff2fc"></a> `00aff2fc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aff300"></a> `00aff300` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff304"></a> `00aff304` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff308"></a> `00aff308` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aff30c"></a> `00aff30c` | `35 00 40 f9` | ldr x21,[x1] | `FALL_THROUGH`
<a id="insn-00aff310"></a> `00aff310` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00aff314"></a> `00aff314` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aff318"></a> `00aff318` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aff31c"></a> `00aff31c` | `2d 7a 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00aff320"></a> `00aff320` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00aff324"></a> `00aff324` | `a9 01 00 b4` | cbz x9,0x00aff358 | `CONDITIONAL_JUMP`
<a id="insn-00aff328"></a> `00aff328` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00aff32c"></a> `00aff32c` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00aff330"></a> `00aff330` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00aff334"></a> `00aff334` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00aff338"></a> `00aff338` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00aff33c"></a> `00aff33c` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aff340"></a> `00aff340` | `69 ff ff b5` | cbnz x9,0x00aff32c | `CONDITIONAL_JUMP`
<a id="insn-00aff344"></a> `00aff344` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00aff348"></a> `00aff348` | `80 00 00 54` | b.eq 0x00aff358 | `CONDITIONAL_JUMP`
<a id="insn-00aff34c"></a> `00aff34c` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aff350"></a> `00aff350` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00aff354"></a> `00aff354` | `29 02 00 54` | b.ls 0x00aff398 | `CONDITIONAL_JUMP`
<a id="insn-00aff358"></a> `00aff358` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aff35c"></a> `00aff35c` | `21 7a 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00aff360"></a> `00aff360` | `40 bd ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aff364"></a> `00aff364` | `00 38 01 91` | add x0,x0,#0x4e | `FALL_THROUGH`
<a id="insn-00aff368"></a> `00aff368` | `72 7b 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aff36c"></a> `00aff36c` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00aff370"></a> `00aff370` | `88 02 40 b9` | ldr w8,[x20] | `FALL_THROUGH`
<a id="insn-00aff374"></a> `00aff374` | `88 00 00 35` | cbnz w8,0x00aff384 | `CONDITIONAL_JUMP`
<a id="insn-00aff378"></a> `00aff378` | `00 bd ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00aff37c"></a> `00aff37c` | `00 f0 35 91` | add x0,x0,#0xd7c | `FALL_THROUGH`
<a id="insn-00aff380"></a> `00aff380` | `6c 7b 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aff384"></a> `00aff384` | `9f 02 00 b9` | str wzr,[x20] | `FALL_THROUGH`
<a id="insn-00aff388"></a> `00aff388` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff38c"></a> `00aff38c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff390"></a> `00aff390` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aff394"></a> `00aff394` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aff398"></a> `00aff398` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aff39c"></a> `00aff39c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aff3a0"></a> `00aff3a0` | `10 7a 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00aff3a4"></a> `00aff3a4` | `74 fe ff b5` | cbnz x20,0x00aff370 | `CONDITIONAL_JUMP`
<a id="insn-00aff3a8"></a> `00aff3a8` | `ee ff ff 17` | b 0x00aff360 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00aff2fc`](#insn-00aff2fc) 範囲 `[['00aff2fc', '00aff30b']]`
  - `FALL_THROUGH` [`00aff308`](#insn-00aff308) → [`00aff30c`](#insn-00aff30c)
- ブロック [`00aff30c`](#insn-00aff30c) 範囲 `[['00aff30c', '00aff31b']]`
  - `FALL_THROUGH` [`00aff318`](#insn-00aff318) → [`00aff31c`](#insn-00aff31c)
- ブロック [`00aff31c`](#insn-00aff31c) 範囲 `[['00aff31c', '00aff327']]`
  - `CONDITIONAL_JUMP` [`00aff324`](#insn-00aff324) → [`00aff358`](#insn-00aff358)
  - `FALL_THROUGH` [`00aff324`](#insn-00aff324) → [`00aff328`](#insn-00aff328)
- ブロック [`00aff328`](#insn-00aff328) 範囲 `[['00aff328', '00aff32b']]`
  - `FALL_THROUGH` [`00aff328`](#insn-00aff328) → [`00aff32c`](#insn-00aff32c)
- ブロック [`00aff32c`](#insn-00aff32c) 範囲 `[['00aff32c', '00aff333']]`
  - `FALL_THROUGH` [`00aff330`](#insn-00aff330) → [`00aff334`](#insn-00aff334)
- ブロック [`00aff334`](#insn-00aff334) 範囲 `[['00aff334', '00aff343']]`
  - `CONDITIONAL_JUMP` [`00aff340`](#insn-00aff340) → [`00aff32c`](#insn-00aff32c)
  - `FALL_THROUGH` [`00aff340`](#insn-00aff340) → [`00aff344`](#insn-00aff344)
- ブロック [`00aff344`](#insn-00aff344) 範囲 `[['00aff344', '00aff34b']]`
  - `CONDITIONAL_JUMP` [`00aff348`](#insn-00aff348) → [`00aff358`](#insn-00aff358)
  - `FALL_THROUGH` [`00aff348`](#insn-00aff348) → [`00aff34c`](#insn-00aff34c)
- ブロック [`00aff34c`](#insn-00aff34c) 範囲 `[['00aff34c', '00aff357']]`
  - `CONDITIONAL_JUMP` [`00aff354`](#insn-00aff354) → [`00aff398`](#insn-00aff398)
  - `FALL_THROUGH` [`00aff354`](#insn-00aff354) → [`00aff358`](#insn-00aff358)
- ブロック [`00aff358`](#insn-00aff358) 範囲 `[['00aff358', '00aff35f']]`
  - `FALL_THROUGH` [`00aff35c`](#insn-00aff35c) → [`00aff360`](#insn-00aff360)
- ブロック [`00aff360`](#insn-00aff360) 範囲 `[['00aff360', '00aff363']]`
  - `FALL_THROUGH` [`00aff360`](#insn-00aff360) → [`00aff364`](#insn-00aff364)
- ブロック [`00aff364`](#insn-00aff364) 範囲 `[['00aff364', '00aff367']]`
  - `FALL_THROUGH` [`00aff364`](#insn-00aff364) → [`00aff368`](#insn-00aff368)
- ブロック [`00aff368`](#insn-00aff368) 範囲 `[['00aff368', '00aff36f']]`
  - `FALL_THROUGH` [`00aff36c`](#insn-00aff36c) → [`00aff370`](#insn-00aff370)
- ブロック [`00aff370`](#insn-00aff370) 範囲 `[['00aff370', '00aff377']]`
  - `CONDITIONAL_JUMP` [`00aff374`](#insn-00aff374) → [`00aff384`](#insn-00aff384)
  - `FALL_THROUGH` [`00aff374`](#insn-00aff374) → [`00aff378`](#insn-00aff378)
- ブロック [`00aff378`](#insn-00aff378) 範囲 `[['00aff378', '00aff37b']]`
  - `FALL_THROUGH` [`00aff378`](#insn-00aff378) → [`00aff37c`](#insn-00aff37c)
- ブロック [`00aff37c`](#insn-00aff37c) 範囲 `[['00aff37c', '00aff37f']]`
  - `FALL_THROUGH` [`00aff37c`](#insn-00aff37c) → [`00aff380`](#insn-00aff380)
- ブロック [`00aff380`](#insn-00aff380) 範囲 `[['00aff380', '00aff383']]`
  - `FALL_THROUGH` [`00aff380`](#insn-00aff380) → [`00aff384`](#insn-00aff384)
- ブロック [`00aff384`](#insn-00aff384) 範囲 `[['00aff384', '00aff387']]`
  - `FALL_THROUGH` [`00aff384`](#insn-00aff384) → [`00aff388`](#insn-00aff388)
- ブロック [`00aff388`](#insn-00aff388) 範囲 `[['00aff388', '00aff38b']]`
  - `FALL_THROUGH` [`00aff388`](#insn-00aff388) → [`00aff38c`](#insn-00aff38c)
- ブロック [`00aff38c`](#insn-00aff38c) 範囲 `[['00aff38c', '00aff397']]`
- ブロック [`00aff398`](#insn-00aff398) 範囲 `[['00aff398', '00aff39b']]`
  - `FALL_THROUGH` [`00aff398`](#insn-00aff398) → [`00aff39c`](#insn-00aff39c)
- ブロック [`00aff39c`](#insn-00aff39c) 範囲 `[['00aff39c', '00aff39f']]`
  - `FALL_THROUGH` [`00aff39c`](#insn-00aff39c) → [`00aff3a0`](#insn-00aff3a0)
- ブロック [`00aff3a0`](#insn-00aff3a0) 範囲 `[['00aff3a0', '00aff3a3']]`
  - `FALL_THROUGH` [`00aff3a0`](#insn-00aff3a0) → [`00aff3a4`](#insn-00aff3a4)
- ブロック [`00aff3a4`](#insn-00aff3a4) 範囲 `[['00aff3a4', '00aff3a7']]`
  - `CONDITIONAL_JUMP` [`00aff3a4`](#insn-00aff3a4) → [`00aff370`](#insn-00aff370)
  - `FALL_THROUGH` [`00aff3a4`](#insn-00aff3a4) → [`00aff3a8`](#insn-00aff3a8)
- ブロック [`00aff3a8`](#insn-00aff3a8) 範囲 `[['00aff3a8', '00aff3ab']]`
  - `UNCONDITIONAL_JUMP` [`00aff3a8`](#insn-00aff3a8) → [`00aff360`](#insn-00aff360)

## 命令位置別の参照

- [`00aff2fc`](#insn-00aff2fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff300`](#insn-00aff300) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff304`](#insn-00aff304) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff31c`](#insn-00aff31c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00aff324`](#insn-00aff324) → [`00aff358`](#insn-00aff358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff340`](#insn-00aff340) → [`00aff32c`](#insn-00aff32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff348`](#insn-00aff348) → [`00aff358`](#insn-00aff358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff354`](#insn-00aff354) → [`00aff398`](#insn-00aff398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff35c`](#insn-00aff35c) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00aff364`](#insn-00aff364) → `002a704e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aff368`](#insn-00aff368) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aff374`](#insn-00aff374) → [`00aff384`](#insn-00aff384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff37c`](#insn-00aff37c) → `002a2d7c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aff380`](#insn-00aff380) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aff388`](#insn-00aff388) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff38c`](#insn-00aff38c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff3a0`](#insn-00aff3a0) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00aff3a4`](#insn-00aff3a4) → [`00aff370`](#insn-00aff370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff3a8`](#insn-00aff3a8) → [`00aff360`](#insn-00aff360) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aff2fc`](#insn-00aff2fc)

~~~json
{
  "source": "00aff2fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff300`](#insn-00aff300)

~~~json
{
  "source": "00aff300",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff304`](#insn-00aff304)

~~~json
{
  "source": "00aff304",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff31c`](#insn-00aff31c)

~~~json
{
  "source": "00aff31c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff324`](#insn-00aff324)

~~~json
{
  "source": "00aff324",
  "target": "00aff358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff340`](#insn-00aff340)

~~~json
{
  "source": "00aff340",
  "target": "00aff32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff348`](#insn-00aff348)

~~~json
{
  "source": "00aff348",
  "target": "00aff358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff354`](#insn-00aff354)

~~~json
{
  "source": "00aff354",
  "target": "00aff398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff35c`](#insn-00aff35c)

~~~json
{
  "source": "00aff35c",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff364`](#insn-00aff364)

~~~json
{
  "source": "00aff364",
  "target": "002a704e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a704e",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6261636b696e6720213d206e756c6c70747200",
  "capture_start": "002a704e",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aff368`](#insn-00aff368)

~~~json
{
  "source": "00aff368",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff374`](#insn-00aff374)

~~~json
{
  "source": "00aff374",
  "target": "00aff384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff37c`](#insn-00aff37c)

~~~json
{
  "source": "00aff37c",
  "target": "002a2d7c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2d7c",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "6261636b696e672d3e73746174757320213d206b467574757265537461747573",
  "capture_start": "002a2d7c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff380`](#insn-00aff380)

~~~json
{
  "source": "00aff380",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff388`](#insn-00aff388)

~~~json
{
  "source": "00aff388",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff38c`](#insn-00aff38c)

~~~json
{
  "source": "00aff38c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff3a0`](#insn-00aff3a0)

~~~json
{
  "source": "00aff3a0",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff3a4`](#insn-00aff3a4)

~~~json
{
  "source": "00aff3a4",
  "target": "00aff370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff3a8`](#insn-00aff3a8)

~~~json
{
  "source": "00aff3a8",
  "target": "00aff360",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
