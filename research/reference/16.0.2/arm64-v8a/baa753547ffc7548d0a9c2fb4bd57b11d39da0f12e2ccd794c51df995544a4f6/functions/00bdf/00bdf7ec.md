# 00bdf7ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdf750`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf750.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-77f696b2b36730f12fdd328254819afb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00be07e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be07e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-92aea837b664ee3a76d1deb311c0e1f0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf7ec",
  "name": "_ZN8firebase4auth4User14UpdatePasswordEPKc",
  "size": 460,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a5ec702ef1c31e7882254916b93b99160bfde5633922650f3f9c7b094ead7fa",
  "source_text_sha256": "8a5ec702ef1c31e7882254916b93b99160bfde5633922650f3f9c7b094ead7fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf7ec",
        "00bdf9b7"
      ]
    ],
    "bytes_sha256": "8268e07ef82e8fa13e91c3ab6b4945b86fc0ac5bf2f6ed1198904a3f7e5c3038",
    "instruction_count": 115,
    "instruction_bytes": 460,
    "body_bytes": 460,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5aea0](../00c5a/00c5aea0.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5ddd0](../00c5d/00c5ddd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3165 bytes

~~~c

void _ZN8firebase4auth4User14UpdatePasswordEPKc(long param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  ulong uVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  undefined8 *puVar9;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar8 = *(long *)(param_2 + 0x98);
  if ((lVar8 == 0) || (*(long *)(lVar8 + 0x200) == 0)) {
                    /* try { // try from 00bdf91c to 00cdf96b has its CatchHandler @ 00be0864 */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar8 = lVar8 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(auStack_68,lVar8,0xb,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
                    /* try { // try from 00bdf858 to 00cdf86f has its CatchHandler @ 00be0840 */
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar3 = (**(code **)(*plVar2 + 0x538))(plVar2,param_3);
                    /* try { // try from 00bdf880 to 00cdf893 has its CatchHandler @ 00be07a8 */
    uVar4 = FUN_00497874(plVar2,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126e50,
                         uVar3);
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
    uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar2,lVar8,auStack_78);
    if ((uVar5 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
      puVar9 = *(undefined8 **)(param_2 + 0x98);
      uVar3 = _ZNK8firebase3App9GetJNIEnvEv(*puVar9);
      lVar6 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar6,auStack_88);
      *(undefined8 **)(lVar6 + 0x10) = puVar9;
      *(undefined8 *)(lVar6 + 0x18) = 0;
      if ((*(byte *)(puVar9 + 0x28) & 1) == 0) {
        lVar7 = (long)puVar9 + 0x141;
      }
      else {
        lVar7 = puVar9[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar3,uVar4,
                 PTR__ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bae8
                 ,lVar6,lVar7);
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
      (**(code **)(*plVar2 + 0xb8))(plVar2,uVar4);
    }
                    /* try { // try from 00bdf97c to 00cdf9a7 has its CatchHandler @ 00be07a0 */
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar8,auStack_78);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bdf9b4 to 00cdf9e7 has its CatchHandler @ 00be058c */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdf7ec"></a> `00bdf7ec` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bdf7f0"></a> `00bdf7f0` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdf7f4"></a> `00bdf7f4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdf7f8"></a> `00bdf7f8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdf7fc"></a> `00bdf7fc` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdf800"></a> `00bdf800` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdf804"></a> `00bdf804` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdf808"></a> `00bdf808` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdf80c"></a> `00bdf80c` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdf810"></a> `00bdf810` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdf814"></a> `00bdf814` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdf818"></a> `00bdf818` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf81c"></a> `00bdf81c` | `c9 07 00 b4` | cbz x9,0x00bdf914 | `CONDITIONAL_JUMP`
<a id="insn-00bdf820"></a> `00bdf820` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bdf824"></a> `00bdf824` | `88 07 00 b4` | cbz x8,0x00bdf914 | `CONDITIONAL_JUMP`
<a id="insn-00bdf828"></a> `00bdf828` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bdf82c"></a> `00bdf82c` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bdf830"></a> `00bdf830` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdf834"></a> `00bdf834` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bdf838"></a> `00bdf838` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00bdf83c"></a> `00bdf83c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf840"></a> `00bdf840` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdf844"></a> `00bdf844` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bdf848"></a> `00bdf848` | `b2 ed 01 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf84c"></a> `00bdf84c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdf850"></a> `00bdf850` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bdf854"></a> `00bdf854` | `9f ed 01 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf858"></a> `00bdf858` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bdf85c"></a> `00bdf85c` | `c1 ec 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf860"></a> `00bdf860` | `c8 4e 40 f9` | ldr x8,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf864"></a> `00bdf864` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdf868"></a> `00bdf868` | `3a ee 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf86c"></a> `00bdf86c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdf870"></a> `00bdf870` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdf874"></a> `00bdf874` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdf878"></a> `00bdf878` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdf87c"></a> `00bdf87c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf880"></a> `00bdf880` | `c8 4e 40 f9` | ldr x8,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf884"></a> `00bdf884` | `29 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdf888"></a> `00bdf888` | `22 29 47 f9` | ldr x2,[x9, #0xe50] | `FALL_THROUGH`
<a id="insn-00bdf88c"></a> `00bdf88c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdf890"></a> `00bdf890` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdf894"></a> `00bdf894` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdf898"></a> `00bdf898` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bdf89c"></a> `00bdf89c` | `f6 df e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf8a0"></a> `00bdf8a0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdf8a4"></a> `00bdf8a4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdf8a8"></a> `00bdf8a8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdf8ac"></a> `00bdf8ac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdf8b0"></a> `00bdf8b0` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bdf8b4"></a> `00bdf8b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf8b8"></a> `00bdf8b8` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdf8bc"></a> `00bdf8bc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdf8c0"></a> `00bdf8c0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdf8c4"></a> `00bdf8c4` | `43 f9 01 94` | bl 0x00c5ddd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf8c8"></a> `00bdf8c8` | `40 05 00 37` | tbnz w0,#0x0,0x00bdf970 | `CONDITIONAL_JUMP`
<a id="insn-00bdf8cc"></a> `00bdf8cc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdf8d0"></a> `00bdf8d0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdf8d4"></a> `00bdf8d4` | `7f ed 01 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf8d8"></a> `00bdf8d8` | `da 4e 40 f9` | ldr x26,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf8dc"></a> `00bdf8dc` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bdf8e0"></a> `00bdf8e0` | `1c ee 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf8e4"></a> `00bdf8e4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdf8e8"></a> `00bdf8e8` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bdf8ec"></a> `00bdf8ec` | `9d e1 01 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf8f0"></a> `00bdf8f0` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdf8f4"></a> `00bdf8f4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdf8f8"></a> `00bdf8f8` | `76 ed 01 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf8fc"></a> `00bdf8fc` | `1a 7f 01 a9` | stp x26,xzr,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf900"></a> `00bdf900` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bdf904"></a> `00bdf904` | `a8 01 00 37` | tbnz w8,#0x0,0x00bdf938 | `CONDITIONAL_JUMP`
<a id="insn-00bdf908"></a> `00bdf908` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bdf90c"></a> `00bdf90c` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdf910"></a> `00bdf910` | `0b 00 00 14` | b 0x00bdf93c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdf914"></a> `00bdf914` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf918"></a> `00bdf918` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bdf91c"></a> `00bdf91c` | `09 ed 01 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf920"></a> `00bdf920` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bdf924"></a> `00bdf924` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdf928"></a> `00bdf928` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bdf92c"></a> `00bdf92c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdf930"></a> `00bdf930` | `e0 ec 01 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf934"></a> `00bdf934` | `15 00 00 14` | b 0x00bdf988 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdf938"></a> `00bdf938` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bdf93c"></a> `00bdf93c` | `e2 05 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdf940"></a> `00bdf940` | `42 74 45 f9` | ldr x2,[x2, #0xae8] | `FALL_THROUGH`
<a id="insn-00bdf944"></a> `00bdf944` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdf948"></a> `00bdf948` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdf94c"></a> `00bdf94c` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bdf950"></a> `00bdf950` | `b0 ed 01 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf954"></a> `00bdf954` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdf958"></a> `00bdf958` | `82 ec 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf95c"></a> `00bdf95c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdf960"></a> `00bdf960` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdf964"></a> `00bdf964` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdf968"></a> `00bdf968` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdf96c"></a> `00bdf96c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf970"></a> `00bdf970` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdf974"></a> `00bdf974` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf978"></a> `00bdf978` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdf97c"></a> `00bdf97c` | `49 ed 01 94` | bl 0x00c5aea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf980"></a> `00bdf980` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdf984"></a> `00bdf984` | `77 ec 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf988"></a> `00bdf988` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdf98c"></a> `00bdf98c` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdf990"></a> `00bdf990` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdf994"></a> `00bdf994` | `01 01 00 54` | b.ne 0x00bdf9b4 | `CONDITIONAL_JUMP`
<a id="insn-00bdf998"></a> `00bdf998` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdf99c"></a> `00bdf99c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdf9a0"></a> `00bdf9a0` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdf9a4"></a> `00bdf9a4` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdf9a8"></a> `00bdf9a8` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdf9ac"></a> `00bdf9ac` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bdf9b0"></a> `00bdf9b0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdf9b4"></a> `00bdf9b4` | `7f e1 01 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf7ec`](#insn-00bdf7ec) 範囲 `[['00bdf7ec', '00bdf81f']]`
  - `CONDITIONAL_JUMP` [`00bdf81c`](#insn-00bdf81c) → [`00bdf914`](#insn-00bdf914)
  - `FALL_THROUGH` [`00bdf81c`](#insn-00bdf81c) → [`00bdf820`](#insn-00bdf820)
- ブロック [`00bdf820`](#insn-00bdf820) 範囲 `[['00bdf820', '00bdf827']]`
  - `CONDITIONAL_JUMP` [`00bdf824`](#insn-00bdf824) → [`00bdf914`](#insn-00bdf914)
  - `FALL_THROUGH` [`00bdf824`](#insn-00bdf824) → [`00bdf828`](#insn-00bdf828)
- ブロック [`00bdf828`](#insn-00bdf828) 範囲 `[['00bdf828', '00bdf857']]`
  - `FALL_THROUGH` [`00bdf854`](#insn-00bdf854) → [`00bdf858`](#insn-00bdf858)
- ブロック [`00bdf858`](#insn-00bdf858) 範囲 `[['00bdf858', '00bdf87f']]`
  - `FALL_THROUGH` [`00bdf87c`](#insn-00bdf87c) → [`00bdf880`](#insn-00bdf880)
- ブロック [`00bdf880`](#insn-00bdf880) 範囲 `[['00bdf880', '00bdf8cb']]`
  - `CONDITIONAL_JUMP` [`00bdf8c8`](#insn-00bdf8c8) → [`00bdf970`](#insn-00bdf970)
  - `FALL_THROUGH` [`00bdf8c8`](#insn-00bdf8c8) → [`00bdf8cc`](#insn-00bdf8cc)
- ブロック [`00bdf8cc`](#insn-00bdf8cc) 範囲 `[['00bdf8cc', '00bdf907']]`
  - `CONDITIONAL_JUMP` [`00bdf904`](#insn-00bdf904) → [`00bdf938`](#insn-00bdf938)
  - `FALL_THROUGH` [`00bdf904`](#insn-00bdf904) → [`00bdf908`](#insn-00bdf908)
- ブロック [`00bdf908`](#insn-00bdf908) 範囲 `[['00bdf908', '00bdf913']]`
  - `UNCONDITIONAL_JUMP` [`00bdf910`](#insn-00bdf910) → [`00bdf93c`](#insn-00bdf93c)
- ブロック [`00bdf914`](#insn-00bdf914) 範囲 `[['00bdf914', '00bdf91b']]`
  - `FALL_THROUGH` [`00bdf918`](#insn-00bdf918) → [`00bdf91c`](#insn-00bdf91c)
- ブロック [`00bdf91c`](#insn-00bdf91c) 範囲 `[['00bdf91c', '00bdf937']]`
  - `UNCONDITIONAL_JUMP` [`00bdf934`](#insn-00bdf934) → [`00bdf988`](#insn-00bdf988)
- ブロック [`00bdf938`](#insn-00bdf938) 範囲 `[['00bdf938', '00bdf93b']]`
  - `FALL_THROUGH` [`00bdf938`](#insn-00bdf938) → [`00bdf93c`](#insn-00bdf93c)
- ブロック [`00bdf93c`](#insn-00bdf93c) 範囲 `[['00bdf93c', '00bdf96f']]`
  - `FALL_THROUGH` [`00bdf96c`](#insn-00bdf96c) → [`00bdf970`](#insn-00bdf970)
- ブロック [`00bdf970`](#insn-00bdf970) 範囲 `[['00bdf970', '00bdf97b']]`
  - `FALL_THROUGH` [`00bdf978`](#insn-00bdf978) → [`00bdf97c`](#insn-00bdf97c)
- ブロック [`00bdf97c`](#insn-00bdf97c) 範囲 `[['00bdf97c', '00bdf987']]`
  - `FALL_THROUGH` [`00bdf984`](#insn-00bdf984) → [`00bdf988`](#insn-00bdf988)
- ブロック [`00bdf988`](#insn-00bdf988) 範囲 `[['00bdf988', '00bdf997']]`
  - `CONDITIONAL_JUMP` [`00bdf994`](#insn-00bdf994) → [`00bdf9b4`](#insn-00bdf9b4)
  - `FALL_THROUGH` [`00bdf994`](#insn-00bdf994) → [`00bdf998`](#insn-00bdf998)
- ブロック [`00bdf998`](#insn-00bdf998) 範囲 `[['00bdf998', '00bdf9b3']]`
- ブロック [`00bdf9b4`](#insn-00bdf9b4) 範囲 `[['00bdf9b4', '00bdf9b7']]`

## 命令位置別の参照

- [`00bdf7f0`](#insn-00bdf7f0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf7f4`](#insn-00bdf7f4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf7f8`](#insn-00bdf7f8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf7fc`](#insn-00bdf7fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf800`](#insn-00bdf800) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf814`](#insn-00bdf814) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf81c`](#insn-00bdf81c) → [`00bdf914`](#insn-00bdf914) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf824`](#insn-00bdf824) → [`00bdf914`](#insn-00bdf914) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf848`](#insn-00bdf848) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bdf854`](#insn-00bdf854) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf85c`](#insn-00bdf85c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdf868`](#insn-00bdf868) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdf888`](#insn-00bdf888) → `01126e50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf89c`](#insn-00bdf89c) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bdf8c4`](#insn-00bdf8c4) → [`00c5ddd0`](../00c5d/00c5ddd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ddd0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf8c8`](#insn-00bdf8c8) → [`00bdf970`](#insn-00bdf970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf8d4`](#insn-00bdf8d4) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf8e0`](#insn-00bdf8e0) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdf8ec`](#insn-00bdf8ec) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bdf8f8`](#insn-00bdf8f8) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf904`](#insn-00bdf904) → [`00bdf938`](#insn-00bdf938) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf910`](#insn-00bdf910) → [`00bdf93c`](#insn-00bdf93c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf91c`](#insn-00bdf91c) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bdf930`](#insn-00bdf930) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf934`](#insn-00bdf934) → [`00bdf988`](#insn-00bdf988) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf940`](#insn-00bdf940) → `00c9bae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdf940`](#insn-00bdf940) → [`00bd055c`](../00bd0/00bd055c.md) · `PARAM` · `ANALYSIS` · 関数 `00bd055c` · 推定シンボル `_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bdf950`](#insn-00bdf950) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bdf958`](#insn-00bdf958) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdf97c`](#insn-00bdf97c) → [`00c5aea0`](../00c5a/00c5aea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aea0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf984`](#insn-00bdf984) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdf98c`](#insn-00bdf98c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf994`](#insn-00bdf994) → [`00bdf9b4`](#insn-00bdf9b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf998`](#insn-00bdf998) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf99c`](#insn-00bdf99c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf9a0`](#insn-00bdf9a0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf9a4`](#insn-00bdf9a4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf9a8`](#insn-00bdf9a8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf9b4`](#insn-00bdf9b4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf7f0`](#insn-00bdf7f0)

~~~json
{
  "source": "00bdf7f0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf7f4`](#insn-00bdf7f4)

~~~json
{
  "source": "00bdf7f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf7f8`](#insn-00bdf7f8)

~~~json
{
  "source": "00bdf7f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf7fc`](#insn-00bdf7fc)

~~~json
{
  "source": "00bdf7fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf800`](#insn-00bdf800)

~~~json
{
  "source": "00bdf800",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf814`](#insn-00bdf814)

~~~json
{
  "source": "00bdf814",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf81c`](#insn-00bdf81c)

~~~json
{
  "source": "00bdf81c",
  "target": "00bdf914",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf824`](#insn-00bdf824)

~~~json
{
  "source": "00bdf824",
  "target": "00bdf914",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf848`](#insn-00bdf848)

~~~json
{
  "source": "00bdf848",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf854`](#insn-00bdf854)

~~~json
{
  "source": "00bdf854",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf85c`](#insn-00bdf85c)

~~~json
{
  "source": "00bdf85c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf868`](#insn-00bdf868)

~~~json
{
  "source": "00bdf868",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf888`](#insn-00bdf888)

~~~json
{
  "source": "00bdf888",
  "target": "01126e50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf89c`](#insn-00bdf89c)

~~~json
{
  "source": "00bdf89c",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf8c4`](#insn-00bdf8c4)

~~~json
{
  "source": "00bdf8c4",
  "target": "00c5ddd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf8c8`](#insn-00bdf8c8)

~~~json
{
  "source": "00bdf8c8",
  "target": "00bdf970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf8d4`](#insn-00bdf8d4)

~~~json
{
  "source": "00bdf8d4",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf8e0`](#insn-00bdf8e0)

~~~json
{
  "source": "00bdf8e0",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf8ec`](#insn-00bdf8ec)

~~~json
{
  "source": "00bdf8ec",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf8f8`](#insn-00bdf8f8)

~~~json
{
  "source": "00bdf8f8",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf904`](#insn-00bdf904)

~~~json
{
  "source": "00bdf904",
  "target": "00bdf938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf910`](#insn-00bdf910)

~~~json
{
  "source": "00bdf910",
  "target": "00bdf93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf91c`](#insn-00bdf91c)

~~~json
{
  "source": "00bdf91c",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf930`](#insn-00bdf930)

~~~json
{
  "source": "00bdf930",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf934`](#insn-00bdf934)

~~~json
{
  "source": "00bdf934",
  "target": "00bdf988",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf940`](#insn-00bdf940)

~~~json
{
  "source": "00bdf940",
  "target": "00c9bae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bae8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdf940`](#insn-00bdf940)

~~~json
{
  "source": "00bdf940",
  "target": "00bd055c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf950`](#insn-00bdf950)

~~~json
{
  "source": "00bdf950",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf958`](#insn-00bdf958)

~~~json
{
  "source": "00bdf958",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf97c`](#insn-00bdf97c)

~~~json
{
  "source": "00bdf97c",
  "target": "00c5aea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf984`](#insn-00bdf984)

~~~json
{
  "source": "00bdf984",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf98c`](#insn-00bdf98c)

~~~json
{
  "source": "00bdf98c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf994`](#insn-00bdf994)

~~~json
{
  "source": "00bdf994",
  "target": "00bdf9b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf998`](#insn-00bdf998)

~~~json
{
  "source": "00bdf998",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf99c`](#insn-00bdf99c)

~~~json
{
  "source": "00bdf99c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf9a0`](#insn-00bdf9a0)

~~~json
{
  "source": "00bdf9a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf9a4`](#insn-00bdf9a4)

~~~json
{
  "source": "00bdf9a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf9a8`](#insn-00bdf9a8)

~~~json
{
  "source": "00bdf9a8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf9b4`](#insn-00bdf9b4)

~~~json
{
  "source": "00bdf9b4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
