# 00bcdbb0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcd788`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-599bc100b9f085b74d76cb7e133ea150)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcdc4c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc4c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-e0a5364cd0edd36a5d68f193d46539ba)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdbb0",
  "name": "_ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35a8f2510d1530af8852371f307dac7724d58a1865a9564e95f87346de29f849",
  "source_text_sha256": "35a8f2510d1530af8852371f307dac7724d58a1865a9564e95f87346de29f849",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdbb0",
        "00bcdd67"
      ]
    ],
    "bytes_sha256": "4937ea99ff66e3c3e603626b69dd258723c55cb3c332ff011b49045e237d700e",
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

- [00497834](../00497/00497834.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5ae40](../00c5a/00c5ae40.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dce0](../00c5d/00c5dce0.md)
- [00c5dd40](../00c5d/00c5dd40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2921 bytes

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
  
                    /* try { // try from 00bcdbb4 to 00ccdbbb has its CatchHandler @ 00bcea1c */
                    /* try { // try from 00bcdbbc to 00ccdd5f has its CatchHandler @ 00bcc5d0 */
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  puVar3 = (undefined8 *)_Znwm(0x18);
  puVar3[1] = 0;
  puVar3[2] = 0;
  *puVar3 = 0;
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_68,lVar1,0,puVar3,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv_00c9b9f0
            );
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_3);
  uVar6 = FUN_00497834(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_01126790,uVar5);
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
    *(code **)(lVar8 + 0x18) = FUN_00bcdeb4;
    if ((*(byte *)(puVar3 + 0x28) & 1) == 0) {
      lVar9 = (long)puVar3 + 0x141;
    }
    else {
      lVar9 = puVar3[0x2a];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (uVar5,uVar6,
               PTR__ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba08
               ,lVar8,lVar9);
    _ZN8firebase12FutureHandleD2Ev(auStack_88);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar6);
  }
  _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_78);
  _ZN8firebase12FutureHandleD2Ev(auStack_78);
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* try { // try from 00bcdd60 to 00ccdd77 has its CatchHandler @ 00bcea14 */
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
<a id="insn-00bcdbb0"></a> `00bcdbb0` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcdbb4"></a> `00bcdbb4` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdbb8"></a> `00bcdbb8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdbbc"></a> `00bcdbbc` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdbc0"></a> `00bcdbc0` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcdbc4"></a> `00bcdbc4` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcdbc8"></a> `00bcdbc8` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcdbcc"></a> `00bcdbcc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcdbd0"></a> `00bcdbd0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcdbd4"></a> `00bcdbd4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdbd8"></a> `00bcdbd8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcdbdc"></a> `00bcdbdc` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcdbe0"></a> `00bcdbe0` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcdbe4"></a> `00bcdbe4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcdbe8"></a> `00bcdbe8` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdbec"></a> `00bcdbec` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdbf0"></a> `00bcdbf0` | `a8 28 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdbf4"></a> `00bcdbf4` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdbf8"></a> `00bcdbf8` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcdbfc"></a> `00bcdbfc` | `63 06 00 d0` | adrp x3,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcdc00"></a> `00bcdc00` | `63 f8 44 f9` | ldr x3,[x3, #0x9f0] | `FALL_THROUGH`
<a id="insn-00bcdc04"></a> `00bcdc04` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bcdc08"></a> `00bcdc08` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdc0c"></a> `00bcdc0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdc10"></a> `00bcdc10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcdc14"></a> `00bcdc14` | `8b 34 02 94` | bl 0x00c5ae40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc18"></a> `00bcdc18` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdc1c"></a> `00bcdc1c` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdc20"></a> `00bcdc20` | `78 34 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc24"></a> `00bcdc24` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdc28"></a> `00bcdc28` | `9a 33 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc2c"></a> `00bcdc2c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcdc30"></a> `00bcdc30` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcdc34"></a> `00bcdc34` | `13 35 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc38"></a> `00bcdc38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcdc3c"></a> `00bcdc3c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcdc40"></a> `00bcdc40` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcdc44"></a> `00bcdc44` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcdc48"></a> `00bcdc48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdc4c"></a> `00bcdc4c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcdc50"></a> `00bcdc50` | `c9 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcdc54"></a> `00bcdc54` | `22 c9 43 f9` | ldr x2,[x9, #0x790] | `FALL_THROUGH`
<a id="insn-00bcdc58"></a> `00bcdc58` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcdc5c"></a> `00bcdc5c` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcdc60"></a> `00bcdc60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdc64"></a> `00bcdc64` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcdc68"></a> `00bcdc68` | `f3 26 e3 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc6c"></a> `00bcdc6c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcdc70"></a> `00bcdc70` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcdc74"></a> `00bcdc74` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcdc78"></a> `00bcdc78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdc7c"></a> `00bcdc7c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcdc80"></a> `00bcdc80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdc84"></a> `00bcdc84` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdc88"></a> `00bcdc88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdc8c"></a> `00bcdc8c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcdc90"></a> `00bcdc90` | `14 40 02 94` | bl 0x00c5dce0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc94"></a> `00bcdc94` | `60 04 00 37` | tbnz w0,#0x0,0x00bcdd20 | `CONDITIONAL_JUMP`
<a id="insn-00bcdc98"></a> `00bcdc98` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdc9c"></a> `00bcdc9c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdca0"></a> `00bcdca0` | `58 34 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdca4"></a> `00bcdca4` | `da 02 40 f9` | ldr x26,[x22] | `FALL_THROUGH`
<a id="insn-00bcdca8"></a> `00bcdca8` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bcdcac"></a> `00bcdcac` | `f5 34 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcb0"></a> `00bcdcb0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcdcb4"></a> `00bcdcb4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdcb8"></a> `00bcdcb8` | `76 28 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcbc"></a> `00bcdcbc` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcdcc0"></a> `00bcdcc0` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdcc4"></a> `00bcdcc4` | `4f 34 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcc8"></a> `00bcdcc8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bcdccc"></a> `00bcdccc` | `48 0f 00 10` | adr x8,0xbcdeb4 | `FALL_THROUGH`
<a id="insn-00bcdcd0"></a> `00bcdcd0` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdcd4"></a> `00bcdcd4` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bcdcd8"></a> `00bcdcd8` | `88 00 00 37` | tbnz w8,#0x0,0x00bcdce8 | `CONDITIONAL_JUMP`
<a id="insn-00bcdcdc"></a> `00bcdcdc` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bcdce0"></a> `00bcdce0` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdce4"></a> `00bcdce4` | `02 00 00 14` | b 0x00bcdcec | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdce8"></a> `00bcdce8` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bcdcec"></a> `00bcdcec` | `62 06 00 d0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcdcf0"></a> `00bcdcf0` | `42 04 45 f9` | ldr x2,[x2, #0xa08] | `FALL_THROUGH`
<a id="insn-00bcdcf4"></a> `00bcdcf4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bcdcf8"></a> `00bcdcf8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcdcfc"></a> `00bcdcfc` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcdd00"></a> `00bcdd00` | `90 34 02 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd04"></a> `00bcdd04` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdd08"></a> `00bcdd08` | `62 33 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd0c"></a> `00bcdd0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcdd10"></a> `00bcdd10` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcdd14"></a> `00bcdd14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdd18"></a> `00bcdd18` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcdd1c"></a> `00bcdd1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdd20"></a> `00bcdd20` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdd24"></a> `00bcdd24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdd28"></a> `00bcdd28` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcdd2c"></a> `00bcdd2c` | `05 40 02 94` | bl 0x00c5dd40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd30"></a> `00bcdd30` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdd34"></a> `00bcdd34` | `57 33 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd38"></a> `00bcdd38` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdd3c"></a> `00bcdd3c` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcdd40"></a> `00bcdd40` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdd44"></a> `00bcdd44` | `01 01 00 54` | b.ne 0x00bcdd64 | `CONDITIONAL_JUMP`
<a id="insn-00bcdd48"></a> `00bcdd48` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcdd4c"></a> `00bcdd4c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcdd50"></a> `00bcdd50` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdd54"></a> `00bcdd54` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdd58"></a> `00bcdd58` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdd5c"></a> `00bcdd5c` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcdd60"></a> `00bcdd60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcdd64"></a> `00bcdd64` | `5f 28 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdbb0`](#insn-00bcdbb0) 範囲 `[['00bcdbb0', '00bcdbb3']]`
  - `FALL_THROUGH` [`00bcdbb0`](#insn-00bcdbb0) → [`00bcdbb4`](#insn-00bcdbb4)
- ブロック [`00bcdbb4`](#insn-00bcdbb4) 範囲 `[['00bcdbb4', '00bcdbbb']]`
  - `FALL_THROUGH` [`00bcdbb8`](#insn-00bcdbb8) → [`00bcdbbc`](#insn-00bcdbbc)
- ブロック [`00bcdbbc`](#insn-00bcdbbc) 範囲 `[['00bcdbbc', '00bcdc97']]`
  - `CONDITIONAL_JUMP` [`00bcdc94`](#insn-00bcdc94) → [`00bcdd20`](#insn-00bcdd20)
  - `FALL_THROUGH` [`00bcdc94`](#insn-00bcdc94) → [`00bcdc98`](#insn-00bcdc98)
- ブロック [`00bcdc98`](#insn-00bcdc98) 範囲 `[['00bcdc98', '00bcdcdb']]`
  - `CONDITIONAL_JUMP` [`00bcdcd8`](#insn-00bcdcd8) → [`00bcdce8`](#insn-00bcdce8)
  - `FALL_THROUGH` [`00bcdcd8`](#insn-00bcdcd8) → [`00bcdcdc`](#insn-00bcdcdc)
- ブロック [`00bcdcdc`](#insn-00bcdcdc) 範囲 `[['00bcdcdc', '00bcdce7']]`
  - `UNCONDITIONAL_JUMP` [`00bcdce4`](#insn-00bcdce4) → [`00bcdcec`](#insn-00bcdcec)
- ブロック [`00bcdce8`](#insn-00bcdce8) 範囲 `[['00bcdce8', '00bcdceb']]`
  - `FALL_THROUGH` [`00bcdce8`](#insn-00bcdce8) → [`00bcdcec`](#insn-00bcdcec)
- ブロック [`00bcdcec`](#insn-00bcdcec) 範囲 `[['00bcdcec', '00bcdd1f']]`
  - `FALL_THROUGH` [`00bcdd1c`](#insn-00bcdd1c) → [`00bcdd20`](#insn-00bcdd20)
- ブロック [`00bcdd20`](#insn-00bcdd20) 範囲 `[['00bcdd20', '00bcdd47']]`
  - `CONDITIONAL_JUMP` [`00bcdd44`](#insn-00bcdd44) → [`00bcdd64`](#insn-00bcdd64)
  - `FALL_THROUGH` [`00bcdd44`](#insn-00bcdd44) → [`00bcdd48`](#insn-00bcdd48)
- ブロック [`00bcdd48`](#insn-00bcdd48) 範囲 `[['00bcdd48', '00bcdd5f']]`
  - `FALL_THROUGH` [`00bcdd5c`](#insn-00bcdd5c) → [`00bcdd60`](#insn-00bcdd60)
- ブロック [`00bcdd60`](#insn-00bcdd60) 範囲 `[['00bcdd60', '00bcdd63']]`
- ブロック [`00bcdd64`](#insn-00bcdd64) 範囲 `[['00bcdd64', '00bcdd67']]`

## 命令位置別の参照

- [`00bcdbb4`](#insn-00bcdbb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbb8`](#insn-00bcdbb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbbc`](#insn-00bcdbbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbc0`](#insn-00bcdbc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbc4`](#insn-00bcdbc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbe0`](#insn-00bcdbe0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbf0`](#insn-00bcdbf0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc00`](#insn-00bcdc00) → `00c9b9f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcdc00`](#insn-00bcdc00) → [`00bcf8a0`](../00bcf/00bcf8a0.md) · `PARAM` · `ANALYSIS` · 関数 `00bcf8a0` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv` · 推定型 `None`
- [`00bcdc14`](#insn-00bcdc14) → [`00c5ae40`](../00c5a/00c5ae40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae40` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc20`](#insn-00bcdc20) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc28`](#insn-00bcdc28) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc34`](#insn-00bcdc34) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc54`](#insn-00bcdc54) → `01126790`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdc68`](#insn-00bcdc68) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc90`](#insn-00bcdc90) → [`00c5dce0`](../00c5d/00c5dce0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dce0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc94`](#insn-00bcdc94) → [`00bcdd20`](#insn-00bcdd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdca0`](#insn-00bcdca0) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcac`](#insn-00bcdcac) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcb8`](#insn-00bcdcb8) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcc4`](#insn-00bcdcc4) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcd0`](#insn-00bcdcd0) → [`00bcdeb4`](00bcdeb4.md) · `DATA` · `ANALYSIS` · 関数 `00bcdeb4` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcd8`](#insn-00bcdcd8) → [`00bcdce8`](#insn-00bcdce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdce4`](#insn-00bcdce4) → [`00bcdcec`](#insn-00bcdcec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcf0`](#insn-00bcdcf0) → `00c9ba08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcdcf0`](#insn-00bcdcf0) → [`00bcfa2c`](../00bcf/00bcfa2c.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfa2c` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcdd00`](#insn-00bcdd00) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd08`](#insn-00bcdd08) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd2c`](#insn-00bcdd2c) → [`00c5dd40`](../00c5d/00c5dd40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd40` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd34`](#insn-00bcdd34) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd3c`](#insn-00bcdd3c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd44`](#insn-00bcdd44) → [`00bcdd64`](#insn-00bcdd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd48`](#insn-00bcdd48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd4c`](#insn-00bcdd4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd50`](#insn-00bcdd50) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd54`](#insn-00bcdd54) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd58`](#insn-00bcdd58) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd64`](#insn-00bcdd64) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdbb4`](#insn-00bcdbb4)

~~~json
{
  "source": "00bcdbb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbb8`](#insn-00bcdbb8)

~~~json
{
  "source": "00bcdbb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbbc`](#insn-00bcdbbc)

~~~json
{
  "source": "00bcdbbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbc0`](#insn-00bcdbc0)

~~~json
{
  "source": "00bcdbc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbc4`](#insn-00bcdbc4)

~~~json
{
  "source": "00bcdbc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbe0`](#insn-00bcdbe0)

~~~json
{
  "source": "00bcdbe0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbf0`](#insn-00bcdbf0)

~~~json
{
  "source": "00bcdbf0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc00`](#insn-00bcdc00)

~~~json
{
  "source": "00bcdc00",
  "target": "00c9b9f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcdc00`](#insn-00bcdc00)

~~~json
{
  "source": "00bcdc00",
  "target": "00bcf8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc14`](#insn-00bcdc14)

~~~json
{
  "source": "00bcdc14",
  "target": "00c5ae40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc20`](#insn-00bcdc20)

~~~json
{
  "source": "00bcdc20",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc28`](#insn-00bcdc28)

~~~json
{
  "source": "00bcdc28",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc34`](#insn-00bcdc34)

~~~json
{
  "source": "00bcdc34",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc54`](#insn-00bcdc54)

~~~json
{
  "source": "00bcdc54",
  "target": "01126790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126790",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdc68`](#insn-00bcdc68)

~~~json
{
  "source": "00bcdc68",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc90`](#insn-00bcdc90)

~~~json
{
  "source": "00bcdc90",
  "target": "00c5dce0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc94`](#insn-00bcdc94)

~~~json
{
  "source": "00bcdc94",
  "target": "00bcdd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdca0`](#insn-00bcdca0)

~~~json
{
  "source": "00bcdca0",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcac`](#insn-00bcdcac)

~~~json
{
  "source": "00bcdcac",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcb8`](#insn-00bcdcb8)

~~~json
{
  "source": "00bcdcb8",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcc4`](#insn-00bcdcc4)

~~~json
{
  "source": "00bcdcc4",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcd0`](#insn-00bcdcd0)

~~~json
{
  "source": "00bcdcd0",
  "target": "00bcdeb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcd8`](#insn-00bcdcd8)

~~~json
{
  "source": "00bcdcd8",
  "target": "00bcdce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdce4`](#insn-00bcdce4)

~~~json
{
  "source": "00bcdce4",
  "target": "00bcdcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcf0`](#insn-00bcdcf0)

~~~json
{
  "source": "00bcdcf0",
  "target": "00c9ba08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcdcf0`](#insn-00bcdcf0)

~~~json
{
  "source": "00bcdcf0",
  "target": "00bcfa2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd00`](#insn-00bcdd00)

~~~json
{
  "source": "00bcdd00",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd08`](#insn-00bcdd08)

~~~json
{
  "source": "00bcdd08",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd2c`](#insn-00bcdd2c)

~~~json
{
  "source": "00bcdd2c",
  "target": "00c5dd40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd34`](#insn-00bcdd34)

~~~json
{
  "source": "00bcdd34",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd3c`](#insn-00bcdd3c)

~~~json
{
  "source": "00bcdd3c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd44`](#insn-00bcdd44)

~~~json
{
  "source": "00bcdd44",
  "target": "00bcdd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd48`](#insn-00bcdd48)

~~~json
{
  "source": "00bcdd48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd4c`](#insn-00bcdd4c)

~~~json
{
  "source": "00bcdd4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd50`](#insn-00bcdd50)

~~~json
{
  "source": "00bcdd50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd54`](#insn-00bcdd54)

~~~json
{
  "source": "00bcdd54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd58`](#insn-00bcdd58)

~~~json
{
  "source": "00bcdd58",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd64`](#insn-00bcdd64)

~~~json
{
  "source": "00bcdd64",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
