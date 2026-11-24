# 00bcdc4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcdbb0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-e0a5364cd0edd36a5d68f193d46539ba)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcec40`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcec40.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-fc52e2c30771ad4cbc3c760ecd6cb6e7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdc4c",
  "name": "_ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20a681cf97daebadd0f8382932a85d44d2e67d31239312dd7a987a3256383eb8",
  "source_text_sha256": "20a681cf97daebadd0f8382932a85d44d2e67d31239312dd7a987a3256383eb8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdc4c",
        "00bcde03"
      ]
    ],
    "bytes_sha256": "e50e44e9c447429f984c2b4ad5e32b77e5fc29e9dd36e14a6af8d334f10aa99b",
    "instruction_count": 110,
    "instruction_bytes": 440,
    "body_bytes": 440,
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
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5ddb0](../00c5d/00c5ddb0.md)
- [00c5de10](../00c5d/00c5de10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2727 bytes

~~~c

void _ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  long lVar1;
  long lVar2;
  undefined8 *puVar3;
  long *plVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  ulong uVar7;
  long lVar8;
  long lVar9;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  puVar3 = (undefined8 *)_Znwm(0x18);
  puVar3[1] = 0;
  puVar3[2] = 0;
  *puVar3 = 0;
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_68,lVar1,0,puVar3,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv_00c9bac0
            );
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_3);
  uVar6 = FUN_00497874(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_01126890,uVar5);
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  uVar7 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                    (plVar4,lVar1,auStack_78);
  if ((uVar7 & 1) == 0) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
    puVar3 = (undefined8 *)*param_2;
    uVar5 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
    lVar8 = _Znwm(0x20);
    _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_88);
    *(undefined8 **)(lVar8 + 0x10) = puVar3;
    *(code **)(lVar8 + 0x18) = FUN_00bcdf50;
    if ((*(byte *)(puVar3 + 0x28) & 1) == 0) {
      lVar9 = (long)puVar3 + 0x141;
    }
    else {
      lVar9 = puVar3[0x2a];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (uVar5,uVar6,
               PTR__ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bad8
               ,lVar8,lVar9);
    _ZN8firebase12FutureHandleD2Ev(auStack_88);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar6);
  }
  _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_78);
                    /* try { // try from 00bcddd0 to 00ccdde7 has its CatchHandler @ 00bcea84 */
  _ZN8firebase12FutureHandleD2Ev(auStack_78);
  if (*(long *)(lVar2 + 0x28) == local_58) {
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
<a id="insn-00bcdc4c"></a> `00bcdc4c` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcdc50"></a> `00bcdc50` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdc54"></a> `00bcdc54` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdc58"></a> `00bcdc58` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdc5c"></a> `00bcdc5c` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcdc60"></a> `00bcdc60` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcdc64"></a> `00bcdc64` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcdc68"></a> `00bcdc68` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcdc6c"></a> `00bcdc6c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcdc70"></a> `00bcdc70` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdc74"></a> `00bcdc74` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcdc78"></a> `00bcdc78` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcdc7c"></a> `00bcdc7c` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcdc80"></a> `00bcdc80` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcdc84"></a> `00bcdc84` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdc88"></a> `00bcdc88` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdc8c"></a> `00bcdc8c` | `b5 28 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc90"></a> `00bcdc90` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdc94"></a> `00bcdc94` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcdc98"></a> `00bcdc98` | `63 06 00 d0` | adrp x3,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcdc9c"></a> `00bcdc9c` | `63 60 45 f9` | ldr x3,[x3, #0xac0] | `FALL_THROUGH`
<a id="insn-00bcdca0"></a> `00bcdca0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bcdca4"></a> `00bcdca4` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdca8"></a> `00bcdca8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdcac"></a> `00bcdcac` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcdcb0"></a> `00bcdcb0` | `98 34 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcb4"></a> `00bcdcb4` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdcb8"></a> `00bcdcb8` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdcbc"></a> `00bcdcbc` | `85 34 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcc0"></a> `00bcdcc0` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdcc4"></a> `00bcdcc4` | `a7 33 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcc8"></a> `00bcdcc8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcdccc"></a> `00bcdccc` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcdcd0"></a> `00bcdcd0` | `20 35 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcd4"></a> `00bcdcd4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcdcd8"></a> `00bcdcd8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcdcdc"></a> `00bcdcdc` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcdce0"></a> `00bcdce0` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcdce4"></a> `00bcdce4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdce8"></a> `00bcdce8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcdcec"></a> `00bcdcec` | `c9 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcdcf0"></a> `00bcdcf0` | `22 49 44 f9` | ldr x2,[x9, #0x890] | `FALL_THROUGH`
<a id="insn-00bcdcf4"></a> `00bcdcf4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcdcf8"></a> `00bcdcf8` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcdcfc"></a> `00bcdcfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdd00"></a> `00bcdd00` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcdd04"></a> `00bcdd04` | `dc 26 e3 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd08"></a> `00bcdd08` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcdd0c"></a> `00bcdd0c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcdd10"></a> `00bcdd10` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcdd14"></a> `00bcdd14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdd18"></a> `00bcdd18` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcdd1c"></a> `00bcdd1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdd20"></a> `00bcdd20` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdd24"></a> `00bcdd24` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdd28"></a> `00bcdd28` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcdd2c"></a> `00bcdd2c` | `21 40 02 94` | bl 0x00c5ddb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd30"></a> `00bcdd30` | `60 04 00 37` | tbnz w0,#0x0,0x00bcddbc | `CONDITIONAL_JUMP`
<a id="insn-00bcdd34"></a> `00bcdd34` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdd38"></a> `00bcdd38` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdd3c"></a> `00bcdd3c` | `65 34 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd40"></a> `00bcdd40` | `da 02 40 f9` | ldr x26,[x22] | `FALL_THROUGH`
<a id="insn-00bcdd44"></a> `00bcdd44` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bcdd48"></a> `00bcdd48` | `02 35 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd4c"></a> `00bcdd4c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcdd50"></a> `00bcdd50` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdd54"></a> `00bcdd54` | `83 28 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd58"></a> `00bcdd58` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcdd5c"></a> `00bcdd5c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdd60"></a> `00bcdd60` | `5c 34 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd64"></a> `00bcdd64` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bcdd68"></a> `00bcdd68` | `48 0f 00 10` | adr x8,0xbcdf50 | `FALL_THROUGH`
<a id="insn-00bcdd6c"></a> `00bcdd6c` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdd70"></a> `00bcdd70` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bcdd74"></a> `00bcdd74` | `88 00 00 37` | tbnz w8,#0x0,0x00bcdd84 | `CONDITIONAL_JUMP`
<a id="insn-00bcdd78"></a> `00bcdd78` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bcdd7c"></a> `00bcdd7c` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdd80"></a> `00bcdd80` | `02 00 00 14` | b 0x00bcdd88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdd84"></a> `00bcdd84` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bcdd88"></a> `00bcdd88` | `62 06 00 d0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcdd8c"></a> `00bcdd8c` | `42 6c 45 f9` | ldr x2,[x2, #0xad8] | `FALL_THROUGH`
<a id="insn-00bcdd90"></a> `00bcdd90` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bcdd94"></a> `00bcdd94` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcdd98"></a> `00bcdd98` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcdd9c"></a> `00bcdd9c` | `9d 34 02 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdda0"></a> `00bcdda0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdda4"></a> `00bcdda4` | `6f 33 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdda8"></a> `00bcdda8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcddac"></a> `00bcddac` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcddb0"></a> `00bcddb0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcddb4"></a> `00bcddb4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcddb8"></a> `00bcddb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcddbc"></a> `00bcddbc` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcddc0"></a> `00bcddc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcddc4"></a> `00bcddc4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcddc8"></a> `00bcddc8` | `12 40 02 94` | bl 0x00c5de10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcddcc"></a> `00bcddcc` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcddd0"></a> `00bcddd0` | `64 33 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcddd4"></a> `00bcddd4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcddd8"></a> `00bcddd8` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcdddc"></a> `00bcdddc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdde0"></a> `00bcdde0` | `01 01 00 54` | b.ne 0x00bcde00 | `CONDITIONAL_JUMP`
<a id="insn-00bcdde4"></a> `00bcdde4` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcdde8"></a> `00bcdde8` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcddec"></a> `00bcddec` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcddf0"></a> `00bcddf0` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcddf4"></a> `00bcddf4` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcddf8"></a> `00bcddf8` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcddfc"></a> `00bcddfc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcde00"></a> `00bcde00` | `6c 28 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdc4c`](#insn-00bcdc4c) 範囲 `[['00bcdc4c', '00bcdd33']]`
  - `CONDITIONAL_JUMP` [`00bcdd30`](#insn-00bcdd30) → [`00bcddbc`](#insn-00bcddbc)
  - `FALL_THROUGH` [`00bcdd30`](#insn-00bcdd30) → [`00bcdd34`](#insn-00bcdd34)
- ブロック [`00bcdd34`](#insn-00bcdd34) 範囲 `[['00bcdd34', '00bcdd77']]`
  - `CONDITIONAL_JUMP` [`00bcdd74`](#insn-00bcdd74) → [`00bcdd84`](#insn-00bcdd84)
  - `FALL_THROUGH` [`00bcdd74`](#insn-00bcdd74) → [`00bcdd78`](#insn-00bcdd78)
- ブロック [`00bcdd78`](#insn-00bcdd78) 範囲 `[['00bcdd78', '00bcdd83']]`
  - `UNCONDITIONAL_JUMP` [`00bcdd80`](#insn-00bcdd80) → [`00bcdd88`](#insn-00bcdd88)
- ブロック [`00bcdd84`](#insn-00bcdd84) 範囲 `[['00bcdd84', '00bcdd87']]`
  - `FALL_THROUGH` [`00bcdd84`](#insn-00bcdd84) → [`00bcdd88`](#insn-00bcdd88)
- ブロック [`00bcdd88`](#insn-00bcdd88) 範囲 `[['00bcdd88', '00bcddbb']]`
  - `FALL_THROUGH` [`00bcddb8`](#insn-00bcddb8) → [`00bcddbc`](#insn-00bcddbc)
- ブロック [`00bcddbc`](#insn-00bcddbc) 範囲 `[['00bcddbc', '00bcddcf']]`
  - `FALL_THROUGH` [`00bcddcc`](#insn-00bcddcc) → [`00bcddd0`](#insn-00bcddd0)
- ブロック [`00bcddd0`](#insn-00bcddd0) 範囲 `[['00bcddd0', '00bcdde3']]`
  - `CONDITIONAL_JUMP` [`00bcdde0`](#insn-00bcdde0) → [`00bcde00`](#insn-00bcde00)
  - `FALL_THROUGH` [`00bcdde0`](#insn-00bcdde0) → [`00bcdde4`](#insn-00bcdde4)
- ブロック [`00bcdde4`](#insn-00bcdde4) 範囲 `[['00bcdde4', '00bcddff']]`
- ブロック [`00bcde00`](#insn-00bcde00) 範囲 `[['00bcde00', '00bcde03']]`

## 命令位置別の参照

- [`00bcdc50`](#insn-00bcdc50) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc54`](#insn-00bcdc54) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc58`](#insn-00bcdc58) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc5c`](#insn-00bcdc5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc60`](#insn-00bcdc60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc7c`](#insn-00bcdc7c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc8c`](#insn-00bcdc8c) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc9c`](#insn-00bcdc9c) → `00c9bac0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcdc9c`](#insn-00bcdc9c) → [`00bcf93c`](../00bcf/00bcf93c.md) · `PARAM` · `ANALYSIS` · 関数 `00bcf93c` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv` · 推定型 `None`
- [`00bcdcb0`](#insn-00bcdcb0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcbc`](#insn-00bcdcbc) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcc4`](#insn-00bcdcc4) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcd0`](#insn-00bcdcd0) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcf0`](#insn-00bcdcf0) → `01126890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdd04`](#insn-00bcdd04) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd2c`](#insn-00bcdd2c) → [`00c5ddb0`](../00c5d/00c5ddb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ddb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd30`](#insn-00bcdd30) → [`00bcddbc`](#insn-00bcddbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd3c`](#insn-00bcdd3c) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd48`](#insn-00bcdd48) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd54`](#insn-00bcdd54) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd60`](#insn-00bcdd60) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd6c`](#insn-00bcdd6c) → [`00bcdf50`](00bcdf50.md) · `DATA` · `ANALYSIS` · 関数 `00bcdf50` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd74`](#insn-00bcdd74) → [`00bcdd84`](#insn-00bcdd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd80`](#insn-00bcdd80) → [`00bcdd88`](#insn-00bcdd88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd8c`](#insn-00bcdd8c) → `00c9bad8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcdd8c`](#insn-00bcdd8c) → [`00bcfac8`](../00bcf/00bcfac8.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfac8` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcdd9c`](#insn-00bcdd9c) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bcdda4`](#insn-00bcdda4) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcddc8`](#insn-00bcddc8) → [`00c5de10`](../00c5d/00c5de10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de10` · 推定シンボル `None` · 推定型 `None`
- [`00bcddd0`](#insn-00bcddd0) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcddd8`](#insn-00bcddd8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdde0`](#insn-00bcdde0) → [`00bcde00`](#insn-00bcde00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdde4`](#insn-00bcdde4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdde8`](#insn-00bcdde8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddec`](#insn-00bcddec) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddf0`](#insn-00bcddf0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddf4`](#insn-00bcddf4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde00`](#insn-00bcde00) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdc50`](#insn-00bcdc50)

~~~json
{
  "source": "00bcdc50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc54`](#insn-00bcdc54)

~~~json
{
  "source": "00bcdc54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc58`](#insn-00bcdc58)

~~~json
{
  "source": "00bcdc58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc5c`](#insn-00bcdc5c)

~~~json
{
  "source": "00bcdc5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc60`](#insn-00bcdc60)

~~~json
{
  "source": "00bcdc60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc7c`](#insn-00bcdc7c)

~~~json
{
  "source": "00bcdc7c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc8c`](#insn-00bcdc8c)

~~~json
{
  "source": "00bcdc8c",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc9c`](#insn-00bcdc9c)

~~~json
{
  "source": "00bcdc9c",
  "target": "00c9bac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bac0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcdc9c`](#insn-00bcdc9c)

~~~json
{
  "source": "00bcdc9c",
  "target": "00bcf93c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcb0`](#insn-00bcdcb0)

~~~json
{
  "source": "00bcdcb0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcbc`](#insn-00bcdcbc)

~~~json
{
  "source": "00bcdcbc",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcc4`](#insn-00bcdcc4)

~~~json
{
  "source": "00bcdcc4",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcd0`](#insn-00bcdcd0)

~~~json
{
  "source": "00bcdcd0",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcf0`](#insn-00bcdcf0)

~~~json
{
  "source": "00bcdcf0",
  "target": "01126890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdd04`](#insn-00bcdd04)

~~~json
{
  "source": "00bcdd04",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd2c`](#insn-00bcdd2c)

~~~json
{
  "source": "00bcdd2c",
  "target": "00c5ddb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd30`](#insn-00bcdd30)

~~~json
{
  "source": "00bcdd30",
  "target": "00bcddbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd3c`](#insn-00bcdd3c)

~~~json
{
  "source": "00bcdd3c",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd48`](#insn-00bcdd48)

~~~json
{
  "source": "00bcdd48",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd54`](#insn-00bcdd54)

~~~json
{
  "source": "00bcdd54",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd60`](#insn-00bcdd60)

~~~json
{
  "source": "00bcdd60",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd6c`](#insn-00bcdd6c)

~~~json
{
  "source": "00bcdd6c",
  "target": "00bcdf50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd74`](#insn-00bcdd74)

~~~json
{
  "source": "00bcdd74",
  "target": "00bcdd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd80`](#insn-00bcdd80)

~~~json
{
  "source": "00bcdd80",
  "target": "00bcdd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd8c`](#insn-00bcdd8c)

~~~json
{
  "source": "00bcdd8c",
  "target": "00c9bad8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bad8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcdd8c`](#insn-00bcdd8c)

~~~json
{
  "source": "00bcdd8c",
  "target": "00bcfac8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd9c`](#insn-00bcdd9c)

~~~json
{
  "source": "00bcdd9c",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdda4`](#insn-00bcdda4)

~~~json
{
  "source": "00bcdda4",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddc8`](#insn-00bcddc8)

~~~json
{
  "source": "00bcddc8",
  "target": "00c5de10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddd0`](#insn-00bcddd0)

~~~json
{
  "source": "00bcddd0",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddd8`](#insn-00bcddd8)

~~~json
{
  "source": "00bcddd8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdde0`](#insn-00bcdde0)

~~~json
{
  "source": "00bcdde0",
  "target": "00bcde00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdde4`](#insn-00bcdde4)

~~~json
{
  "source": "00bcdde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdde8`](#insn-00bcdde8)

~~~json
{
  "source": "00bcdde8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddec`](#insn-00bcddec)

~~~json
{
  "source": "00bcddec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddf0`](#insn-00bcddf0)

~~~json
{
  "source": "00bcddf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddf4`](#insn-00bcddf4)

~~~json
{
  "source": "00bcddf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde00`](#insn-00bcde00)

~~~json
{
  "source": "00bcde00",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
