# 00aed3bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0083.md#review-8a41e1dce0c31ee07b89da218e56c78a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0041.md#review-8a41e1dce0c31ee07b89da218e56c78a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed3bc",
  "name": "FUN_00aed3bc",
  "size": 476,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba8310597489924ac0468489ad9f44e95340398384a97ba368d6562236cf6e06",
  "source_text_sha256": "ba8310597489924ac0468489ad9f44e95340398384a97ba368d6562236cf6e06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed3bc",
        "00aed593"
      ],
      [
        "00aed5b8",
        "00aed5bb"
      ]
    ],
    "bytes_sha256": "891449989d7aeb64b5660d3655157f5e5353a789276edf07d6ff2eb168485c2b",
    "instruction_count": 119,
    "instruction_bytes": 476,
    "body_bytes": 476,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [0068c610](../0068c/0068c610.md)
- [006d1fe4](../006d1/006d1fe4.md)
- [008514f8](../00851/008514f8.md)
- [008b6f18](../008b6/008b6f18.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3639 bytes

~~~c

void FUN_00aed3bc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined4 uVar2;
  long lVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  long lVar7;
  undefined8 uVar8;
  undefined8 local_48;
  long *local_40;
  long local_38;
  
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    if (DAT_00ca4978 == 0) {
      lVar6 = 0;
    }
    else {
      lVar6 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
    }
    lVar7 = FUN_008514f8();
    if (*(int *)(&DAT_00477ddc + lVar7) != -1) {
      lVar7 = FUN_008514f8();
      uVar2 = *(undefined4 *)(&DAT_00477ddc + lVar7);
      lVar7 = FUN_008514f8();
      *(undefined4 *)(&DAT_00477dd8 + lVar7) = uVar2;
    }
    lVar7 = FUN_008514f8();
    iVar1 = *(int *)(&DAT_00477dd8 + lVar7);
    lVar7 = FUN_008514f8();
    if (iVar1 == 0) {
                    /* catch() { ... } // from try @ 00aed178 with catch @ 00aed56c */
                    /* catch() { ... } // from try @ 00aed304 with catch @ 00aed574
                       catch() { ... } // from try @ 00aed54c with catch @ 00aed574 */
      if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00aed1bc with catch @ 00aed578
                       catch() { ... } // from try @ 00aed538 with catch @ 00aed578 */
        FUN_006d1fe4(&DAT_00477730 + lVar7);
        return;
      }
      goto LAB_00aed5b8;
    }
    local_48 = *(undefined8 *)(lVar6 + 0x228);
    local_40 = *(long **)(lVar6 + 0x230);
    if (local_40 != (long *)0x0) {
      FUN_00c53cd0(1,local_40 + 1);
    }
    FUN_0068c610(lVar7 + 0x17d8,&local_48);
    plVar4 = local_40;
    if ((local_40 != (long *)0x0) &&
       (lVar6 = FUN_00c53d00(0xffffffffffffffff,local_40 + 1), lVar6 == 0)) {
                    /* try { // try from 00aed538 to 00bed53b has its CatchHandler @ 00aed578 */
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
  }
  else {
    if (iVar1 == 3) {
      uVar8 = *param_2;
      uVar5 = FUN_0047acf4();
      FUN_0047cdd4(uVar5,0xb,0);
      if (*(long *)(lVar3 + 0x28) == local_38) {
        FUN_008b6f18(uVar8,0);
        return;
      }
      goto LAB_00aed5b8;
    }
    if (iVar1 == 0) {
      uVar5 = FUN_0047acf4();
      if (*(long *)(lVar3 + 0x28) == local_38) {
        FUN_0047cdd4(uVar5,10,0);
        return;
      }
      goto LAB_00aed5b8;
    }
  }
                    /* try { // try from 00aed54c to 00bed54f has its CatchHandler @ 00aed574 */
                    /* catch() { ... } // from try @ 00aed394 with catch @ 00aed550
                       try { // try from 00aed550 to 00bed5b7 has its CatchHandler @ 00aed118 */
  if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00aed2bc with catch @ 00aed554 */
                    /* catch() { ... } // from try @ 00aed258 with catch @ 00aed55c */
    return;
  }
LAB_00aed5b8:
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00aed5b8 to 00bed5fb has its CatchHandler @ 00aed5b8
                       catch() { ... } // from try @ 00aed5b8 with catch @ 00aed5b8
                       catch() { ... } // from try @ 00aed680 with catch @ 00aed5b8
                       catch() { ... } // from try @ 00aed92c with catch @ 00aed5b8
                       catch() { ... } // from try @ 00aeda6c with catch @ 00aed5b8 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed3bc"></a> `00aed3bc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aed3c0"></a> `00aed3c0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aed3c4"></a> `00aed3c4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aed3c8"></a> `00aed3c8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aed3cc"></a> `00aed3cc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aed3d0"></a> `00aed3d0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aed3d4"></a> `00aed3d4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aed3d8"></a> `00aed3d8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aed3dc"></a> `00aed3dc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aed3e0"></a> `00aed3e0` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aed3e4"></a> `00aed3e4` | `00 04 00 54` | b.eq 0x00aed464 | `CONDITIONAL_JUMP`
<a id="insn-00aed3e8"></a> `00aed3e8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aed3ec"></a> `00aed3ec` | `c0 01 00 54` | b.eq 0x00aed424 | `CONDITIONAL_JUMP`
<a id="insn-00aed3f0"></a> `00aed3f0` | `a8 0a 00 35` | cbnz w8,0x00aed544 | `CONDITIONAL_JUMP`
<a id="insn-00aed3f4"></a> `00aed3f4` | `40 36 e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aed3f8"></a> `00aed3f8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aed3fc"></a> `00aed3fc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aed400"></a> `00aed400` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aed404"></a> `00aed404` | `a1 0d 00 54` | b.ne 0x00aed5b8 | `CONDITIONAL_JUMP`
<a id="insn-00aed408"></a> `00aed408` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aed40c"></a> `00aed40c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aed410"></a> `00aed410` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aed414"></a> `00aed414` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aed418"></a> `00aed418` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aed41c"></a> `00aed41c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aed420"></a> `00aed420` | `6d 3e e6 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-00aed424"></a> `00aed424` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aed428"></a> `00aed428` | `33 36 e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aed42c"></a> `00aed42c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aed430"></a> `00aed430` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aed434"></a> `00aed434` | `68 3e e6 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-00aed438"></a> `00aed438` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aed43c"></a> `00aed43c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aed440"></a> `00aed440` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aed444"></a> `00aed444` | `a1 0b 00 54` | b.ne 0x00aed5b8 | `CONDITIONAL_JUMP`
<a id="insn-00aed448"></a> `00aed448` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed44c"></a> `00aed44c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aed450"></a> `00aed450` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aed454"></a> `00aed454` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aed458"></a> `00aed458` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aed45c"></a> `00aed45c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aed460"></a> `00aed460` | `ae 26 f7 17` | b 0x008b6f18 | `CALL_TERMINATOR`
<a id="insn-00aed464"></a> `00aed464` | `a8 0d 00 f0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00aed468"></a> `00aed468` | `00 bd 44 f9` | ldr x0,[x8, #0x978] | `FALL_THROUGH`
<a id="insn-00aed46c"></a> `00aed46c` | `20 01 00 b4` | cbz x0,0x00aed490 | `CONDITIONAL_JUMP`
<a id="insn-00aed470"></a> `00aed470` | `c1 0b 00 90` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00aed474"></a> `00aed474` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-00aed478"></a> `00aed478` | `02 0d 00 90` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aed47c"></a> `00aed47c` | `42 40 25 91` | add x2,x2,#0x950 | `FALL_THROUGH`
<a id="insn-00aed480"></a> `00aed480` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00aed484"></a> `00aed484` | `63 ac 05 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-00aed488"></a> `00aed488` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aed48c"></a> `00aed48c` | `02 00 00 14` | b 0x00aed494 | `UNCONDITIONAL_JUMP`
<a id="insn-00aed490"></a> `00aed490` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00aed494"></a> `00aed494` | `19 90 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aed498"></a> `00aed498` | `88 bb 8f 52` | mov w8,#0x7ddc | `FALL_THROUGH`
<a id="insn-00aed49c"></a> `00aed49c` | `e8 08 a0 72` | movk w8,#0x47, LSL #16 | `FALL_THROUGH`
<a id="insn-00aed4a0"></a> `00aed4a0` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aed4a4"></a> `00aed4a4` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aed4a8"></a> `00aed4a8` | `20 01 00 54` | b.eq 0x00aed4cc | `CONDITIONAL_JUMP`
<a id="insn-00aed4ac"></a> `00aed4ac` | `13 90 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aed4b0"></a> `00aed4b0` | `88 bb 8f 52` | mov w8,#0x7ddc | `FALL_THROUGH`
<a id="insn-00aed4b4"></a> `00aed4b4` | `e8 08 a0 72` | movk w8,#0x47, LSL #16 | `FALL_THROUGH`
<a id="insn-00aed4b8"></a> `00aed4b8` | `14 68 68 b8` | ldr w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aed4bc"></a> `00aed4bc` | `0f 90 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aed4c0"></a> `00aed4c0` | `08 bb 8f 52` | mov w8,#0x7dd8 | `FALL_THROUGH`
<a id="insn-00aed4c4"></a> `00aed4c4` | `e8 08 a0 72` | movk w8,#0x47, LSL #16 | `FALL_THROUGH`
<a id="insn-00aed4c8"></a> `00aed4c8` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aed4cc"></a> `00aed4cc` | `0b 90 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aed4d0"></a> `00aed4d0` | `08 bb 8f 52` | mov w8,#0x7dd8 | `FALL_THROUGH`
<a id="insn-00aed4d4"></a> `00aed4d4` | `e8 08 a0 72` | movk w8,#0x47, LSL #16 | `FALL_THROUGH`
<a id="insn-00aed4d8"></a> `00aed4d8` | `16 68 68 b8` | ldr w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aed4dc"></a> `00aed4dc` | `07 90 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aed4e0"></a> `00aed4e0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aed4e4"></a> `00aed4e4` | `36 04 00 34` | cbz w22,0x00aed568 | `CONDITIONAL_JUMP`
<a id="insn-00aed4e8"></a> `00aed4e8` | `69 16 41 f9` | ldr x9,[x19, #0x228] | `FALL_THROUGH`
<a id="insn-00aed4ec"></a> `00aed4ec` | `68 1a 41 f9` | ldr x8,[x19, #0x230] | `FALL_THROUGH`
<a id="insn-00aed4f0"></a> `00aed4f0` | `13 fb 82 52` | mov w19,#0x17d8 | `FALL_THROUGH`
<a id="insn-00aed4f4"></a> `00aed4f4` | `e9 a3 00 a9` | stp x9,x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aed4f8"></a> `00aed4f8` | `88 00 00 b4` | cbz x8,0x00aed508 | `CONDITIONAL_JUMP`
<a id="insn-00aed4fc"></a> `00aed4fc` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aed500"></a> `00aed500` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aed504"></a> `00aed504` | `f3 99 05 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00aed508"></a> `00aed508` | `80 02 13 8b` | add x0,x20,x19 | `FALL_THROUGH`
<a id="insn-00aed50c"></a> `00aed50c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aed510"></a> `00aed510` | `40 7c ee 97` | bl 0x0068c610 | `UNCONDITIONAL_CALL`
<a id="insn-00aed514"></a> `00aed514` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed518"></a> `00aed518` | `73 01 00 b4` | cbz x19,0x00aed544 | `CONDITIONAL_JUMP`
<a id="insn-00aed51c"></a> `00aed51c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aed520"></a> `00aed520` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aed524"></a> `00aed524` | `f7 99 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aed528"></a> `00aed528` | `e0 00 00 b5` | cbnz x0,0x00aed544 | `CONDITIONAL_JUMP`
<a id="insn-00aed52c"></a> `00aed52c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aed530"></a> `00aed530` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed534"></a> `00aed534` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aed538"></a> `00aed538` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aed53c"></a> `00aed53c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed540"></a> `00aed540` | `50 aa 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aed544"></a> `00aed544` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aed548"></a> `00aed548` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aed54c"></a> `00aed54c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aed550"></a> `00aed550` | `41 03 00 54` | b.ne 0x00aed5b8 | `CONDITIONAL_JUMP`
<a id="insn-00aed554"></a> `00aed554` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aed558"></a> `00aed558` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aed55c"></a> `00aed55c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aed560"></a> `00aed560` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aed564"></a> `00aed564` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aed568"></a> `00aed568` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aed56c"></a> `00aed56c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aed570"></a> `00aed570` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aed574"></a> `00aed574` | `21 02 00 54` | b.ne 0x00aed5b8 | `CONDITIONAL_JUMP`
<a id="insn-00aed578"></a> `00aed578` | `88 de 51 91` | add x8,x20,#0x477, LSL #12 | `FALL_THROUGH`
<a id="insn-00aed57c"></a> `00aed57c` | `00 c1 1c 91` | add x0,x8,#0x730 | `FALL_THROUGH`
<a id="insn-00aed580"></a> `00aed580` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aed584"></a> `00aed584` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aed588"></a> `00aed588` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aed58c"></a> `00aed58c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aed590"></a> `00aed590` | `95 92 ef 17` | b 0x006d1fe4 | `CALL_TERMINATOR`
<a id="insn-00aed5b8"></a> `00aed5b8` | `4a aa 05 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed3bc`](#insn-00aed3bc) 範囲 `[['00aed3bc', '00aed3e7']]`
  - `CONDITIONAL_JUMP` [`00aed3e4`](#insn-00aed3e4) → [`00aed464`](#insn-00aed464)
  - `FALL_THROUGH` [`00aed3e4`](#insn-00aed3e4) → [`00aed3e8`](#insn-00aed3e8)
- ブロック [`00aed3e8`](#insn-00aed3e8) 範囲 `[['00aed3e8', '00aed3ef']]`
  - `CONDITIONAL_JUMP` [`00aed3ec`](#insn-00aed3ec) → [`00aed424`](#insn-00aed424)
  - `FALL_THROUGH` [`00aed3ec`](#insn-00aed3ec) → [`00aed3f0`](#insn-00aed3f0)
- ブロック [`00aed3f0`](#insn-00aed3f0) 範囲 `[['00aed3f0', '00aed3f3']]`
  - `CONDITIONAL_JUMP` [`00aed3f0`](#insn-00aed3f0) → [`00aed544`](#insn-00aed544)
  - `FALL_THROUGH` [`00aed3f0`](#insn-00aed3f0) → [`00aed3f4`](#insn-00aed3f4)
- ブロック [`00aed3f4`](#insn-00aed3f4) 範囲 `[['00aed3f4', '00aed407']]`
  - `CONDITIONAL_JUMP` [`00aed404`](#insn-00aed404) → [`00aed5b8`](#insn-00aed5b8)
  - `FALL_THROUGH` [`00aed404`](#insn-00aed404) → [`00aed408`](#insn-00aed408)
- ブロック [`00aed408`](#insn-00aed408) 範囲 `[['00aed408', '00aed423']]`
- ブロック [`00aed424`](#insn-00aed424) 範囲 `[['00aed424', '00aed447']]`
  - `CONDITIONAL_JUMP` [`00aed444`](#insn-00aed444) → [`00aed5b8`](#insn-00aed5b8)
  - `FALL_THROUGH` [`00aed444`](#insn-00aed444) → [`00aed448`](#insn-00aed448)
- ブロック [`00aed448`](#insn-00aed448) 範囲 `[['00aed448', '00aed463']]`
- ブロック [`00aed464`](#insn-00aed464) 範囲 `[['00aed464', '00aed46f']]`
  - `CONDITIONAL_JUMP` [`00aed46c`](#insn-00aed46c) → [`00aed490`](#insn-00aed490)
  - `FALL_THROUGH` [`00aed46c`](#insn-00aed46c) → [`00aed470`](#insn-00aed470)
- ブロック [`00aed470`](#insn-00aed470) 範囲 `[['00aed470', '00aed48f']]`
  - `UNCONDITIONAL_JUMP` [`00aed48c`](#insn-00aed48c) → [`00aed494`](#insn-00aed494)
- ブロック [`00aed490`](#insn-00aed490) 範囲 `[['00aed490', '00aed493']]`
  - `FALL_THROUGH` [`00aed490`](#insn-00aed490) → [`00aed494`](#insn-00aed494)
- ブロック [`00aed494`](#insn-00aed494) 範囲 `[['00aed494', '00aed4ab']]`
  - `CONDITIONAL_JUMP` [`00aed4a8`](#insn-00aed4a8) → [`00aed4cc`](#insn-00aed4cc)
  - `FALL_THROUGH` [`00aed4a8`](#insn-00aed4a8) → [`00aed4ac`](#insn-00aed4ac)
- ブロック [`00aed4ac`](#insn-00aed4ac) 範囲 `[['00aed4ac', '00aed4cb']]`
  - `FALL_THROUGH` [`00aed4c8`](#insn-00aed4c8) → [`00aed4cc`](#insn-00aed4cc)
- ブロック [`00aed4cc`](#insn-00aed4cc) 範囲 `[['00aed4cc', '00aed4e7']]`
  - `CONDITIONAL_JUMP` [`00aed4e4`](#insn-00aed4e4) → [`00aed568`](#insn-00aed568)
  - `FALL_THROUGH` [`00aed4e4`](#insn-00aed4e4) → [`00aed4e8`](#insn-00aed4e8)
- ブロック [`00aed4e8`](#insn-00aed4e8) 範囲 `[['00aed4e8', '00aed4fb']]`
  - `CONDITIONAL_JUMP` [`00aed4f8`](#insn-00aed4f8) → [`00aed508`](#insn-00aed508)
  - `FALL_THROUGH` [`00aed4f8`](#insn-00aed4f8) → [`00aed4fc`](#insn-00aed4fc)
- ブロック [`00aed4fc`](#insn-00aed4fc) 範囲 `[['00aed4fc', '00aed507']]`
  - `FALL_THROUGH` [`00aed504`](#insn-00aed504) → [`00aed508`](#insn-00aed508)
- ブロック [`00aed508`](#insn-00aed508) 範囲 `[['00aed508', '00aed51b']]`
  - `CONDITIONAL_JUMP` [`00aed518`](#insn-00aed518) → [`00aed544`](#insn-00aed544)
  - `FALL_THROUGH` [`00aed518`](#insn-00aed518) → [`00aed51c`](#insn-00aed51c)
- ブロック [`00aed51c`](#insn-00aed51c) 範囲 `[['00aed51c', '00aed52b']]`
  - `CONDITIONAL_JUMP` [`00aed528`](#insn-00aed528) → [`00aed544`](#insn-00aed544)
  - `FALL_THROUGH` [`00aed528`](#insn-00aed528) → [`00aed52c`](#insn-00aed52c)
- ブロック [`00aed52c`](#insn-00aed52c) 範囲 `[['00aed52c', '00aed537']]`
  - `FALL_THROUGH` [`00aed534`](#insn-00aed534) → [`00aed538`](#insn-00aed538)
- ブロック [`00aed538`](#insn-00aed538) 範囲 `[['00aed538', '00aed543']]`
  - `FALL_THROUGH` [`00aed540`](#insn-00aed540) → [`00aed544`](#insn-00aed544)
- ブロック [`00aed544`](#insn-00aed544) 範囲 `[['00aed544', '00aed54b']]`
  - `FALL_THROUGH` [`00aed548`](#insn-00aed548) → [`00aed54c`](#insn-00aed54c)
- ブロック [`00aed54c`](#insn-00aed54c) 範囲 `[['00aed54c', '00aed54f']]`
  - `FALL_THROUGH` [`00aed54c`](#insn-00aed54c) → [`00aed550`](#insn-00aed550)
- ブロック [`00aed550`](#insn-00aed550) 範囲 `[['00aed550', '00aed553']]`
  - `CONDITIONAL_JUMP` [`00aed550`](#insn-00aed550) → [`00aed5b8`](#insn-00aed5b8)
  - `FALL_THROUGH` [`00aed550`](#insn-00aed550) → [`00aed554`](#insn-00aed554)
- ブロック [`00aed554`](#insn-00aed554) 範囲 `[['00aed554', '00aed55b']]`
  - `FALL_THROUGH` [`00aed558`](#insn-00aed558) → [`00aed55c`](#insn-00aed55c)
- ブロック [`00aed55c`](#insn-00aed55c) 範囲 `[['00aed55c', '00aed567']]`
- ブロック [`00aed568`](#insn-00aed568) 範囲 `[['00aed568', '00aed56b']]`
  - `FALL_THROUGH` [`00aed568`](#insn-00aed568) → [`00aed56c`](#insn-00aed56c)
- ブロック [`00aed56c`](#insn-00aed56c) 範囲 `[['00aed56c', '00aed573']]`
  - `FALL_THROUGH` [`00aed570`](#insn-00aed570) → [`00aed574`](#insn-00aed574)
- ブロック [`00aed574`](#insn-00aed574) 範囲 `[['00aed574', '00aed577']]`
  - `CONDITIONAL_JUMP` [`00aed574`](#insn-00aed574) → [`00aed5b8`](#insn-00aed5b8)
  - `FALL_THROUGH` [`00aed574`](#insn-00aed574) → [`00aed578`](#insn-00aed578)
- ブロック [`00aed578`](#insn-00aed578) 範囲 `[['00aed578', '00aed593']]`
- ブロック [`00aed5b8`](#insn-00aed5b8) 範囲 `[['00aed5b8', '00aed5bb']]`

## 命令位置別の参照

- [`00aed3c0`](#insn-00aed3c0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3c4`](#insn-00aed3c4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3c8`](#insn-00aed3c8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3d8`](#insn-00aed3d8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3e4`](#insn-00aed3e4) → [`00aed464`](#insn-00aed464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3ec`](#insn-00aed3ec) → [`00aed424`](#insn-00aed424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3f0`](#insn-00aed3f0) → [`00aed544`](#insn-00aed544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3f4`](#insn-00aed3f4) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aed3fc`](#insn-00aed3fc) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed404`](#insn-00aed404) → [`00aed5b8`](#insn-00aed5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed410`](#insn-00aed410) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed414`](#insn-00aed414) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed418`](#insn-00aed418) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed420`](#insn-00aed420) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aed428`](#insn-00aed428) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aed434`](#insn-00aed434) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aed43c`](#insn-00aed43c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed444`](#insn-00aed444) → [`00aed5b8`](#insn-00aed5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed450`](#insn-00aed450) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed454`](#insn-00aed454) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed458`](#insn-00aed458) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed460`](#insn-00aed460) → [`008b6f18`](../008b6/008b6f18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f18` · 推定シンボル `None` · 推定型 `None`
- [`00aed468`](#insn-00aed468) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed46c`](#insn-00aed46c) → [`00aed490`](#insn-00aed490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed474`](#insn-00aed474) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aed47c`](#insn-00aed47c) → `00c8d950`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aed484`](#insn-00aed484) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`00aed48c`](#insn-00aed48c) → [`00aed494`](#insn-00aed494) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed494`](#insn-00aed494) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aed4a0`](#insn-00aed4a0) → `00477ddc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4a8`](#insn-00aed4a8) → [`00aed4cc`](#insn-00aed4cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4ac`](#insn-00aed4ac) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aed4b8`](#insn-00aed4b8) → `00477ddc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4bc`](#insn-00aed4bc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aed4c8`](#insn-00aed4c8) → `00477dd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4cc`](#insn-00aed4cc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aed4d8`](#insn-00aed4d8) → `00477dd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4dc`](#insn-00aed4dc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aed4e4`](#insn-00aed4e4) → [`00aed568`](#insn-00aed568) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4f4`](#insn-00aed4f4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4f8`](#insn-00aed4f8) → [`00aed508`](#insn-00aed508) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed504`](#insn-00aed504) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00aed510`](#insn-00aed510) → [`0068c610`](../0068c/0068c610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0068c610` · 推定シンボル `None` · 推定型 `None`
- [`00aed514`](#insn-00aed514) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed518`](#insn-00aed518) → [`00aed544`](#insn-00aed544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed524`](#insn-00aed524) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aed528`](#insn-00aed528) → [`00aed544`](#insn-00aed544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed540`](#insn-00aed540) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aed548`](#insn-00aed548) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed550`](#insn-00aed550) → [`00aed5b8`](#insn-00aed5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed554`](#insn-00aed554) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed558`](#insn-00aed558) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed55c`](#insn-00aed55c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed56c`](#insn-00aed56c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed574`](#insn-00aed574) → [`00aed5b8`](#insn-00aed5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed580`](#insn-00aed580) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed584`](#insn-00aed584) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed588`](#insn-00aed588) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed590`](#insn-00aed590) → [`006d1fe4`](../006d1/006d1fe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d1fe4` · 推定シンボル `None` · 推定型 `None`
- [`00aed5b8`](#insn-00aed5b8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed3c0`](#insn-00aed3c0)

~~~json
{
  "source": "00aed3c0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3c4`](#insn-00aed3c4)

~~~json
{
  "source": "00aed3c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3c8`](#insn-00aed3c8)

~~~json
{
  "source": "00aed3c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3d8`](#insn-00aed3d8)

~~~json
{
  "source": "00aed3d8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3e4`](#insn-00aed3e4)

~~~json
{
  "source": "00aed3e4",
  "target": "00aed464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3ec`](#insn-00aed3ec)

~~~json
{
  "source": "00aed3ec",
  "target": "00aed424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3f0`](#insn-00aed3f0)

~~~json
{
  "source": "00aed3f0",
  "target": "00aed544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3f4`](#insn-00aed3f4)

~~~json
{
  "source": "00aed3f4",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed3fc`](#insn-00aed3fc)

~~~json
{
  "source": "00aed3fc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed404`](#insn-00aed404)

~~~json
{
  "source": "00aed404",
  "target": "00aed5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed410`](#insn-00aed410)

~~~json
{
  "source": "00aed410",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed414`](#insn-00aed414)

~~~json
{
  "source": "00aed414",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed418`](#insn-00aed418)

~~~json
{
  "source": "00aed418",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed420`](#insn-00aed420)

~~~json
{
  "source": "00aed420",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed428`](#insn-00aed428)

~~~json
{
  "source": "00aed428",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed434`](#insn-00aed434)

~~~json
{
  "source": "00aed434",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed43c`](#insn-00aed43c)

~~~json
{
  "source": "00aed43c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed444`](#insn-00aed444)

~~~json
{
  "source": "00aed444",
  "target": "00aed5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed450`](#insn-00aed450)

~~~json
{
  "source": "00aed450",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed454`](#insn-00aed454)

~~~json
{
  "source": "00aed454",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed458`](#insn-00aed458)

~~~json
{
  "source": "00aed458",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed460`](#insn-00aed460)

~~~json
{
  "source": "00aed460",
  "target": "008b6f18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed468`](#insn-00aed468)

~~~json
{
  "source": "00aed468",
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
- 参照命令 [`00aed46c`](#insn-00aed46c)

~~~json
{
  "source": "00aed46c",
  "target": "00aed490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed474`](#insn-00aed474)

~~~json
{
  "source": "00aed474",
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
- 参照命令 [`00aed47c`](#insn-00aed47c)

~~~json
{
  "source": "00aed47c",
  "target": "00c8d950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d950",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aed484`](#insn-00aed484)

~~~json
{
  "source": "00aed484",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed48c`](#insn-00aed48c)

~~~json
{
  "source": "00aed48c",
  "target": "00aed494",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed494`](#insn-00aed494)

~~~json
{
  "source": "00aed494",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed4a0`](#insn-00aed4a0)

~~~json
{
  "source": "00aed4a0",
  "target": "00477ddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4a8`](#insn-00aed4a8)

~~~json
{
  "source": "00aed4a8",
  "target": "00aed4cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4ac`](#insn-00aed4ac)

~~~json
{
  "source": "00aed4ac",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed4b8`](#insn-00aed4b8)

~~~json
{
  "source": "00aed4b8",
  "target": "00477ddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4bc`](#insn-00aed4bc)

~~~json
{
  "source": "00aed4bc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed4c8`](#insn-00aed4c8)

~~~json
{
  "source": "00aed4c8",
  "target": "00477dd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4cc`](#insn-00aed4cc)

~~~json
{
  "source": "00aed4cc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed4d8`](#insn-00aed4d8)

~~~json
{
  "source": "00aed4d8",
  "target": "00477dd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4dc`](#insn-00aed4dc)

~~~json
{
  "source": "00aed4dc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed4e4`](#insn-00aed4e4)

~~~json
{
  "source": "00aed4e4",
  "target": "00aed568",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4f4`](#insn-00aed4f4)

~~~json
{
  "source": "00aed4f4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4f8`](#insn-00aed4f8)

~~~json
{
  "source": "00aed4f8",
  "target": "00aed508",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed504`](#insn-00aed504)

~~~json
{
  "source": "00aed504",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed510`](#insn-00aed510)

~~~json
{
  "source": "00aed510",
  "target": "0068c610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed514`](#insn-00aed514)

~~~json
{
  "source": "00aed514",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed518`](#insn-00aed518)

~~~json
{
  "source": "00aed518",
  "target": "00aed544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed524`](#insn-00aed524)

~~~json
{
  "source": "00aed524",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed528`](#insn-00aed528)

~~~json
{
  "source": "00aed528",
  "target": "00aed544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed540`](#insn-00aed540)

~~~json
{
  "source": "00aed540",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed548`](#insn-00aed548)

~~~json
{
  "source": "00aed548",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed550`](#insn-00aed550)

~~~json
{
  "source": "00aed550",
  "target": "00aed5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed554`](#insn-00aed554)

~~~json
{
  "source": "00aed554",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed558`](#insn-00aed558)

~~~json
{
  "source": "00aed558",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed55c`](#insn-00aed55c)

~~~json
{
  "source": "00aed55c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed56c`](#insn-00aed56c)

~~~json
{
  "source": "00aed56c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed574`](#insn-00aed574)

~~~json
{
  "source": "00aed574",
  "target": "00aed5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed580`](#insn-00aed580)

~~~json
{
  "source": "00aed580",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed584`](#insn-00aed584)

~~~json
{
  "source": "00aed584",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed588`](#insn-00aed588)

~~~json
{
  "source": "00aed588",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed590`](#insn-00aed590)

~~~json
{
  "source": "00aed590",
  "target": "006d1fe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed5b8`](#insn-00aed5b8)

~~~json
{
  "source": "00aed5b8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
