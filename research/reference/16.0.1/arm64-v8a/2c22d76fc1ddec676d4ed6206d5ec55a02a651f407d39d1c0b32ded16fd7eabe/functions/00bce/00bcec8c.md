# 00bcec8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bce864`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-7a80b2849c7579847628e9fa2c805ed3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bced28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-d0b673e7401fdc50dafd8639a43a1126)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcec8c",
  "name": "_ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_",
  "size": 568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "656ca3d50ca5d92cec7df9a8e4334f84a54db9b69702d4578e6963109e9df6ec",
  "source_text_sha256": "656ca3d50ca5d92cec7df9a8e4334f84a54db9b69702d4578e6963109e9df6ec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcec8c",
        "00bceec3"
      ]
    ],
    "bytes_sha256": "22543da6147a775bc0aee99bdaa054bb396a6e75c5aa6d2e6072a73a4e013298",
    "instruction_count": 142,
    "instruction_bytes": 568,
    "body_bytes": 568,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dbc0](../00c5d/00c5dbc0.md)
- [00c5dc00](../00c5d/00c5dc00.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dd30](../00c5d/00c5dd30.md)

## 関連文字列（未確認候補）

~~~text
"Empty email or password are not allowed."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4125 bytes

~~~c

void _ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_
               (undefined8 param_1,long *param_2,char *param_3,char *param_4)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  size_t sVar4;
  long *plVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  long lVar11;
  undefined4 uVar12;
  undefined8 *puVar13;
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_70,lVar1,5);
  if ((((param_3 == (char *)0x0) || (sVar4 = strlen(param_3), param_4 == (char *)0x0)) ||
      (sVar4 == 0)) || (sVar4 = strlen(param_4), sVar4 == 0)) {
                    /* catch() { ... } // from try @ 00bcede4 with catch @ 00bcedec
                       try { // try from 00bcedec to 00ccee1f has its CatchHandler @ 00bcec54 */
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
    uVar12 = 0x25;
    if (param_3 != (char *)0x0) {
      sVar4 = strlen(param_3);
      uVar12 = 0x25;
      if (sVar4 != 0) {
        uVar12 = 0x26;
      }
    }
                    /* try { // try from 00bcee20 to 00ccf177 has its CatchHandler @ 00bcee20
                       catch() { ... } // from try @ 00bcee20 with catch @ 00bcee20
                       catch() { ... } // from try @ 00bcf180 with catch @ 00bcee20 */
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (lVar1,auStack_80,uVar12,"Empty email or password are not allowed.",auStack_60);
    _ZN8firebase12FutureHandleD2Ev(auStack_80);
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  else {
    plVar5 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
    uVar6 = (**(code **)(*plVar5 + 0x538))(plVar5,param_3);
    uVar7 = (**(code **)(*plVar5 + 0x538))(plVar5,param_4);
    uVar8 = FUN_00497834(plVar5,*(undefined8 *)(*param_2 + 0x1f8),DAT_011267b0,uVar6,uVar7);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar6);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar7);
    uVar9 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar5,lVar1,auStack_70);
    if ((uVar9 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      puVar13 = (undefined8 *)*param_2;
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar13);
      lVar10 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar10,auStack_90);
      puVar3 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9ba20
      ;
      *(undefined8 **)(lVar10 + 0x10) = puVar13;
      *(undefined **)(lVar10 + 0x18) = puVar3;
      if ((*(byte *)(puVar13 + 0x28) & 1) == 0) {
        lVar11 = (long)puVar13 + 0x141;
                    /* try { // try from 00bcede4 to 00ccedeb has its CatchHandler @ 00bcedec */
      }
      else {
        lVar11 = puVar13[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar8,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba00
                 ,lVar10,lVar11);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
      (**(code **)(*plVar5 + 0xb8))(plVar5,uVar8);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  if (*(long *)(lVar2 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcec8c"></a> `00bcec8c` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcec90"></a> `00bcec90` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcec94"></a> `00bcec94` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcec98"></a> `00bcec98` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcec9c"></a> `00bcec9c` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bceca0"></a> `00bceca0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bceca4"></a> `00bceca4` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bceca8"></a> `00bceca8` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcecac"></a> `00bcecac` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcecb0"></a> `00bcecb0` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcecb4"></a> `00bcecb4` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcecb8"></a> `00bcecb8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcecbc"></a> `00bcecbc` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00bcecc0"></a> `00bcecc0` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcecc4"></a> `00bcecc4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcecc8"></a> `00bcecc8` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bceccc"></a> `00bceccc` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcecd0"></a> `00bcecd0` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcecd4"></a> `00bcecd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcecd8"></a> `00bcecd8` | `ca 3b 02 94` | bl 0x00c5dc00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecdc"></a> `00bcecdc` | `77 08 00 b4` | cbz x23,0x00bcede8 | `CONDITIONAL_JUMP`
<a id="insn-00bcece0"></a> `00bcece0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcece4"></a> `00bcece4` | `bf 24 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcece8"></a> `00bcece8` | `18 08 00 b4` | cbz x24,0x00bcede8 | `CONDITIONAL_JUMP`
<a id="insn-00bcecec"></a> `00bcecec` | `e0 07 00 b4` | cbz x0,0x00bcede8 | `CONDITIONAL_JUMP`
<a id="insn-00bcecf0"></a> `00bcecf0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcecf4"></a> `00bcecf4` | `bb 24 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecf8"></a> `00bcecf8` | `80 07 00 b4` | cbz x0,0x00bcede8 | `CONDITIONAL_JUMP`
<a id="insn-00bcecfc"></a> `00bcecfc` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bced00"></a> `00bced00` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bced04"></a> `00bced04` | `df 30 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bced08"></a> `00bced08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bced0c"></a> `00bced0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bced10"></a> `00bced10` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bced14"></a> `00bced14` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bced18"></a> `00bced18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bced1c"></a> `00bced1c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bced20"></a> `00bced20` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bced24"></a> `00bced24` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bced28"></a> `00bced28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bced2c"></a> `00bced2c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bced30"></a> `00bced30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bced34"></a> `00bced34` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bced38"></a> `00bced38` | `c9 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bced3c"></a> `00bced3c` | `22 d9 43 f9` | ldr x2,[x9, #0x7b0] | `FALL_THROUGH`
<a id="insn-00bced40"></a> `00bced40` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bced44"></a> `00bced44` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bced48"></a> `00bced48` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bced4c"></a> `00bced4c` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00bced50"></a> `00bced50` | `e4 03 18 aa` | mov x4,x24 | `FALL_THROUGH`
<a id="insn-00bced54"></a> `00bced54` | `b8 22 e3 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bced58"></a> `00bced58` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bced5c"></a> `00bced5c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bced60"></a> `00bced60` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bced64"></a> `00bced64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bced68"></a> `00bced68` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bced6c"></a> `00bced6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bced70"></a> `00bced70` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bced74"></a> `00bced74` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bced78"></a> `00bced78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bced7c"></a> `00bced7c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bced80"></a> `00bced80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bced84"></a> `00bced84` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bced88"></a> `00bced88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bced8c"></a> `00bced8c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bced90"></a> `00bced90` | `d0 3b 02 94` | bl 0x00c5dcd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bced94"></a> `00bced94` | `c0 08 00 37` | tbnz w0,#0x0,0x00bceeac | `CONDITIONAL_JUMP`
<a id="insn-00bced98"></a> `00bced98` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bced9c"></a> `00bced9c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bceda0"></a> `00bceda0` | `18 30 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bceda4"></a> `00bceda4` | `d9 02 40 f9` | ldr x25,[x22] | `FALL_THROUGH`
<a id="insn-00bceda8"></a> `00bceda8` | `20 03 40 f9` | ldr x0,[x25] | `FALL_THROUGH`
<a id="insn-00bcedac"></a> `00bcedac` | `b5 30 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcedb0"></a> `00bcedb0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcedb4"></a> `00bcedb4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcedb8"></a> `00bcedb8` | `36 24 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcedbc"></a> `00bcedbc` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcedc0"></a> `00bcedc0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bcedc4"></a> `00bcedc4` | `0f 30 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcedc8"></a> `00bcedc8` | `68 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcedcc"></a> `00bcedcc` | `08 11 45 f9` | ldr x8,[x8, #0xa20] | `FALL_THROUGH`
<a id="insn-00bcedd0"></a> `00bcedd0` | `19 23 01 a9` | stp x25,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcedd4"></a> `00bcedd4` | `28 03 45 39` | ldrb w8,[x25, #0x140] | `FALL_THROUGH`
<a id="insn-00bcedd8"></a> `00bcedd8` | `e8 04 00 37` | tbnz w8,#0x0,0x00bcee74 | `CONDITIONAL_JUMP`
<a id="insn-00bceddc"></a> `00bceddc` | `28 03 05 91` | add x8,x25,#0x140 | `FALL_THROUGH`
<a id="insn-00bcede0"></a> `00bcede0` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcede4"></a> `00bcede4` | `25 00 00 14` | b 0x00bcee78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcede8"></a> `00bcede8` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcedec"></a> `00bcedec` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcedf0"></a> `00bcedf0` | `04 30 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcedf4"></a> `00bcedf4` | `b5 04 80 52` | mov w21,#0x25 | `FALL_THROUGH`
<a id="insn-00bcedf8"></a> `00bcedf8` | `b7 00 00 b4` | cbz x23,0x00bcee0c | `CONDITIONAL_JUMP`
<a id="insn-00bcedfc"></a> `00bcedfc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcee00"></a> `00bcee00` | `78 24 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee04"></a> `00bcee04` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bcee08"></a> `00bcee08` | `b5 06 95 1a` | cinc w21,w21,ne | `FALL_THROUGH`
<a id="insn-00bcee0c"></a> `00bcee0c` | `e3 b6 ff d0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcee10"></a> `00bcee10` | `63 f4 09 91` | add x3,x3,#0x27d | `FALL_THROUGH`
<a id="insn-00bcee14"></a> `00bcee14` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcee18"></a> `00bcee18` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcee1c"></a> `00bcee1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcee20"></a> `00bcee20` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bcee24"></a> `00bcee24` | `67 3b 02 94` | bl 0x00c5dbc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee28"></a> `00bcee28` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcee2c"></a> `00bcee2c` | `19 2f 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee30"></a> `00bcee30` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcee34"></a> `00bcee34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcee38"></a> `00bcee38` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcee3c"></a> `00bcee3c` | `bd 3b 02 94` | bl 0x00c5dd30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee40"></a> `00bcee40` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcee44"></a> `00bcee44` | `13 2f 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee48"></a> `00bcee48` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcee4c"></a> `00bcee4c` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcee50"></a> `00bcee50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcee54"></a> `00bcee54` | `61 03 00 54` | b.ne 0x00bceec0 | `CONDITIONAL_JUMP`
<a id="insn-00bcee58"></a> `00bcee58` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcee5c"></a> `00bcee5c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcee60"></a> `00bcee60` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcee64"></a> `00bcee64` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcee68"></a> `00bcee68` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcee6c"></a> `00bcee6c` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcee70"></a> `00bcee70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcee74"></a> `00bcee74` | `24 ab 40 f9` | ldr x4,[x25, #0x150] | `FALL_THROUGH`
<a id="insn-00bcee78"></a> `00bcee78` | `62 06 00 b0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcee7c"></a> `00bcee7c` | `42 00 45 f9` | ldr x2,[x2, #0xa00] | `FALL_THROUGH`
<a id="insn-00bcee80"></a> `00bcee80` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bcee84"></a> `00bcee84` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcee88"></a> `00bcee88` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcee8c"></a> `00bcee8c` | `2d 30 02 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee90"></a> `00bcee90` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcee94"></a> `00bcee94` | `ff 2e 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee98"></a> `00bcee98` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcee9c"></a> `00bcee9c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bceea0"></a> `00bceea0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bceea4"></a> `00bceea4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bceea8"></a> `00bceea8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bceeac"></a> `00bceeac` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bceeb0"></a> `00bceeb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bceeb4"></a> `00bceeb4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bceeb8"></a> `00bceeb8` | `9e 3b 02 94` | bl 0x00c5dd30 | `UNCONDITIONAL_CALL`
<a id="insn-00bceebc"></a> `00bceebc` | `e1 ff ff 17` | b 0x00bcee40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bceec0"></a> `00bceec0` | `08 24 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcec8c`](#insn-00bcec8c) 範囲 `[['00bcec8c', '00bcecdf']]`
  - `CONDITIONAL_JUMP` [`00bcecdc`](#insn-00bcecdc) → [`00bcede8`](#insn-00bcede8)
  - `FALL_THROUGH` [`00bcecdc`](#insn-00bcecdc) → [`00bcece0`](#insn-00bcece0)
- ブロック [`00bcece0`](#insn-00bcece0) 範囲 `[['00bcece0', '00bceceb']]`
  - `CONDITIONAL_JUMP` [`00bcece8`](#insn-00bcece8) → [`00bcede8`](#insn-00bcede8)
  - `FALL_THROUGH` [`00bcece8`](#insn-00bcece8) → [`00bcecec`](#insn-00bcecec)
- ブロック [`00bcecec`](#insn-00bcecec) 範囲 `[['00bcecec', '00bcecef']]`
  - `CONDITIONAL_JUMP` [`00bcecec`](#insn-00bcecec) → [`00bcede8`](#insn-00bcede8)
  - `FALL_THROUGH` [`00bcecec`](#insn-00bcecec) → [`00bcecf0`](#insn-00bcecf0)
- ブロック [`00bcecf0`](#insn-00bcecf0) 範囲 `[['00bcecf0', '00bcecfb']]`
  - `CONDITIONAL_JUMP` [`00bcecf8`](#insn-00bcecf8) → [`00bcede8`](#insn-00bcede8)
  - `FALL_THROUGH` [`00bcecf8`](#insn-00bcecf8) → [`00bcecfc`](#insn-00bcecfc)
- ブロック [`00bcecfc`](#insn-00bcecfc) 範囲 `[['00bcecfc', '00bced97']]`
  - `CONDITIONAL_JUMP` [`00bced94`](#insn-00bced94) → [`00bceeac`](#insn-00bceeac)
  - `FALL_THROUGH` [`00bced94`](#insn-00bced94) → [`00bced98`](#insn-00bced98)
- ブロック [`00bced98`](#insn-00bced98) 範囲 `[['00bced98', '00bceddb']]`
  - `CONDITIONAL_JUMP` [`00bcedd8`](#insn-00bcedd8) → [`00bcee74`](#insn-00bcee74)
  - `FALL_THROUGH` [`00bcedd8`](#insn-00bcedd8) → [`00bceddc`](#insn-00bceddc)
- ブロック [`00bceddc`](#insn-00bceddc) 範囲 `[['00bceddc', '00bcede3']]`
  - `FALL_THROUGH` [`00bcede0`](#insn-00bcede0) → [`00bcede4`](#insn-00bcede4)
- ブロック [`00bcede4`](#insn-00bcede4) 範囲 `[['00bcede4', '00bcede7']]`
  - `UNCONDITIONAL_JUMP` [`00bcede4`](#insn-00bcede4) → [`00bcee78`](#insn-00bcee78)
- ブロック [`00bcede8`](#insn-00bcede8) 範囲 `[['00bcede8', '00bcedeb']]`
  - `FALL_THROUGH` [`00bcede8`](#insn-00bcede8) → [`00bcedec`](#insn-00bcedec)
- ブロック [`00bcedec`](#insn-00bcedec) 範囲 `[['00bcedec', '00bcedfb']]`
  - `CONDITIONAL_JUMP` [`00bcedf8`](#insn-00bcedf8) → [`00bcee0c`](#insn-00bcee0c)
  - `FALL_THROUGH` [`00bcedf8`](#insn-00bcedf8) → [`00bcedfc`](#insn-00bcedfc)
- ブロック [`00bcedfc`](#insn-00bcedfc) 範囲 `[['00bcedfc', '00bcee0b']]`
  - `FALL_THROUGH` [`00bcee08`](#insn-00bcee08) → [`00bcee0c`](#insn-00bcee0c)
- ブロック [`00bcee0c`](#insn-00bcee0c) 範囲 `[['00bcee0c', '00bcee1f']]`
  - `FALL_THROUGH` [`00bcee1c`](#insn-00bcee1c) → [`00bcee20`](#insn-00bcee20)
- ブロック [`00bcee20`](#insn-00bcee20) 範囲 `[['00bcee20', '00bcee3f']]`
  - `FALL_THROUGH` [`00bcee3c`](#insn-00bcee3c) → [`00bcee40`](#insn-00bcee40)
- ブロック [`00bcee40`](#insn-00bcee40) 範囲 `[['00bcee40', '00bcee57']]`
  - `CONDITIONAL_JUMP` [`00bcee54`](#insn-00bcee54) → [`00bceec0`](#insn-00bceec0)
  - `FALL_THROUGH` [`00bcee54`](#insn-00bcee54) → [`00bcee58`](#insn-00bcee58)
- ブロック [`00bcee58`](#insn-00bcee58) 範囲 `[['00bcee58', '00bcee73']]`
- ブロック [`00bcee74`](#insn-00bcee74) 範囲 `[['00bcee74', '00bcee77']]`
  - `FALL_THROUGH` [`00bcee74`](#insn-00bcee74) → [`00bcee78`](#insn-00bcee78)
- ブロック [`00bcee78`](#insn-00bcee78) 範囲 `[['00bcee78', '00bceeab']]`
  - `FALL_THROUGH` [`00bceea8`](#insn-00bceea8) → [`00bceeac`](#insn-00bceeac)
- ブロック [`00bceeac`](#insn-00bceeac) 範囲 `[['00bceeac', '00bceebf']]`
  - `UNCONDITIONAL_JUMP` [`00bceebc`](#insn-00bceebc) → [`00bcee40`](#insn-00bcee40)
- ブロック [`00bceec0`](#insn-00bceec0) 範囲 `[['00bceec0', '00bceec3']]`

## 命令位置別の参照

- [`00bcec90`](#insn-00bcec90) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec94`](#insn-00bcec94) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec98`](#insn-00bcec98) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec9c`](#insn-00bcec9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceca0`](#insn-00bceca0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecc0`](#insn-00bcecc0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecd8`](#insn-00bcecd8) → [`00c5dc00`](../00c5d/00c5dc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc00` · 推定シンボル `None` · 推定型 `None`
- [`00bcecdc`](#insn-00bcecdc) → [`00bcede8`](#insn-00bcede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcece4`](#insn-00bcece4) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bcece8`](#insn-00bcece8) → [`00bcede8`](#insn-00bcede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecec`](#insn-00bcecec) → [`00bcede8`](#insn-00bcede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf4`](#insn-00bcecf4) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf8`](#insn-00bcecf8) → [`00bcede8`](#insn-00bcede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced04`](#insn-00bced04) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bced3c`](#insn-00bced3c) → `011267b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bced54`](#insn-00bced54) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bced90`](#insn-00bced90) → [`00c5dcd0`](../00c5d/00c5dcd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dcd0` · 推定シンボル `None` · 推定型 `None`
- [`00bced94`](#insn-00bced94) → [`00bceeac`](#insn-00bceeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceda0`](#insn-00bceda0) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcedac`](#insn-00bcedac) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bcedb8`](#insn-00bcedb8) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bcedc4`](#insn-00bcedc4) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcedcc`](#insn-00bcedcc) → `00c9ba20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcedd0`](#insn-00bcedd0) → [`00bd482c`](../00bd4/00bd482c.md) · `DATA` · `ANALYSIS` · 関数 `00bd482c` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bcedd8`](#insn-00bcedd8) → [`00bcee74`](#insn-00bcee74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcede4`](#insn-00bcede4) → [`00bcee78`](#insn-00bcee78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedf0`](#insn-00bcedf0) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcedf8`](#insn-00bcedf8) → [`00bcee0c`](#insn-00bcee0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee00`](#insn-00bcee00) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bcee10`](#insn-00bcee10) → `002ac27d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcee24`](#insn-00bcee24) → [`00c5dbc0`](../00c5d/00c5dbc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dbc0` · 推定シンボル `None` · 推定型 `None`
- [`00bcee2c`](#insn-00bcee2c) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcee3c`](#insn-00bcee3c) → [`00c5dd30`](../00c5d/00c5dd30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd30` · 推定シンボル `None` · 推定型 `None`
- [`00bcee44`](#insn-00bcee44) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcee4c`](#insn-00bcee4c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee54`](#insn-00bcee54) → [`00bceec0`](#insn-00bceec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee58`](#insn-00bcee58) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee5c`](#insn-00bcee5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee60`](#insn-00bcee60) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee64`](#insn-00bcee64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee68`](#insn-00bcee68) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee7c`](#insn-00bcee7c) → `00c9ba00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcee7c`](#insn-00bcee7c) → [`00bcfd44`](../00bcf/00bcfd44.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfd44` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcee8c`](#insn-00bcee8c) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bcee94`](#insn-00bcee94) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bceeb8`](#insn-00bceeb8) → [`00c5dd30`](../00c5d/00c5dd30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd30` · 推定シンボル `None` · 推定型 `None`
- [`00bceebc`](#insn-00bceebc) → [`00bcee40`](#insn-00bcee40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceec0`](#insn-00bceec0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcec90`](#insn-00bcec90)

~~~json
{
  "source": "00bcec90",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec94`](#insn-00bcec94)

~~~json
{
  "source": "00bcec94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec98`](#insn-00bcec98)

~~~json
{
  "source": "00bcec98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec9c`](#insn-00bcec9c)

~~~json
{
  "source": "00bcec9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceca0`](#insn-00bceca0)

~~~json
{
  "source": "00bceca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecc0`](#insn-00bcecc0)

~~~json
{
  "source": "00bcecc0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecd8`](#insn-00bcecd8)

~~~json
{
  "source": "00bcecd8",
  "target": "00c5dc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecdc`](#insn-00bcecdc)

~~~json
{
  "source": "00bcecdc",
  "target": "00bcede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcece4`](#insn-00bcece4)

~~~json
{
  "source": "00bcece4",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcece8`](#insn-00bcece8)

~~~json
{
  "source": "00bcece8",
  "target": "00bcede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecec`](#insn-00bcecec)

~~~json
{
  "source": "00bcecec",
  "target": "00bcede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecf4`](#insn-00bcecf4)

~~~json
{
  "source": "00bcecf4",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecf8`](#insn-00bcecf8)

~~~json
{
  "source": "00bcecf8",
  "target": "00bcede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced04`](#insn-00bced04)

~~~json
{
  "source": "00bced04",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bced3c`](#insn-00bced3c)

~~~json
{
  "source": "00bced3c",
  "target": "011267b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bced54`](#insn-00bced54)

~~~json
{
  "source": "00bced54",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bced90`](#insn-00bced90)

~~~json
{
  "source": "00bced90",
  "target": "00c5dcd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bced94`](#insn-00bced94)

~~~json
{
  "source": "00bced94",
  "target": "00bceeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceda0`](#insn-00bceda0)

~~~json
{
  "source": "00bceda0",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedac`](#insn-00bcedac)

~~~json
{
  "source": "00bcedac",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedb8`](#insn-00bcedb8)

~~~json
{
  "source": "00bcedb8",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedc4`](#insn-00bcedc4)

~~~json
{
  "source": "00bcedc4",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedcc`](#insn-00bcedcc)

~~~json
{
  "source": "00bcedcc",
  "target": "00c9ba20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcedd0`](#insn-00bcedd0)

~~~json
{
  "source": "00bcedd0",
  "target": "00bd482c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedd8`](#insn-00bcedd8)

~~~json
{
  "source": "00bcedd8",
  "target": "00bcee74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcede4`](#insn-00bcede4)

~~~json
{
  "source": "00bcede4",
  "target": "00bcee78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedf0`](#insn-00bcedf0)

~~~json
{
  "source": "00bcedf0",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedf8`](#insn-00bcedf8)

~~~json
{
  "source": "00bcedf8",
  "target": "00bcee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee00`](#insn-00bcee00)

~~~json
{
  "source": "00bcee00",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee10`](#insn-00bcee10)

~~~json
{
  "source": "00bcee10",
  "target": "002ac27d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac27d",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "456d70747920656d61696c206f722070617373776f726420617265206e6f7420",
  "capture_start": "002ac27d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcee24`](#insn-00bcee24)

~~~json
{
  "source": "00bcee24",
  "target": "00c5dbc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee2c`](#insn-00bcee2c)

~~~json
{
  "source": "00bcee2c",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee3c`](#insn-00bcee3c)

~~~json
{
  "source": "00bcee3c",
  "target": "00c5dd30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee44`](#insn-00bcee44)

~~~json
{
  "source": "00bcee44",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee4c`](#insn-00bcee4c)

~~~json
{
  "source": "00bcee4c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee54`](#insn-00bcee54)

~~~json
{
  "source": "00bcee54",
  "target": "00bceec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee58`](#insn-00bcee58)

~~~json
{
  "source": "00bcee58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee5c`](#insn-00bcee5c)

~~~json
{
  "source": "00bcee5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee60`](#insn-00bcee60)

~~~json
{
  "source": "00bcee60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee64`](#insn-00bcee64)

~~~json
{
  "source": "00bcee64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee68`](#insn-00bcee68)

~~~json
{
  "source": "00bcee68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee7c`](#insn-00bcee7c)

~~~json
{
  "source": "00bcee7c",
  "target": "00c9ba00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcee7c`](#insn-00bcee7c)

~~~json
{
  "source": "00bcee7c",
  "target": "00bcfd44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee8c`](#insn-00bcee8c)

~~~json
{
  "source": "00bcee8c",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee94`](#insn-00bcee94)

~~~json
{
  "source": "00bcee94",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceeb8`](#insn-00bceeb8)

~~~json
{
  "source": "00bceeb8",
  "target": "00c5dd30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceebc`](#insn-00bceebc)

~~~json
{
  "source": "00bceebc",
  "target": "00bcee40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceec0`](#insn-00bceec0)

~~~json
{
  "source": "00bceec0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
