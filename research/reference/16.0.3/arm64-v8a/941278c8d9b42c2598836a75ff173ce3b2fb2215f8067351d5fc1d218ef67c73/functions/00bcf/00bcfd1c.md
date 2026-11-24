# 00bcfd1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bced28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-f514a3fb8a7df8c5cedf8ca020542612)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfd1c",
  "name": "_ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_",
  "size": 568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "066f24d4d1a36283dd59b19b04c81826fb21582b9cf0d035f217c95acf5cdfeb",
  "source_text_sha256": "066f24d4d1a36283dd59b19b04c81826fb21582b9cf0d035f217c95acf5cdfeb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfd1c",
        "00bcff53"
      ]
    ],
    "bytes_sha256": "48a8282fd002b2ef6682a6eae3a42cb3875a772d7613ac9c44435946061cc104",
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

- [00497b94](../00497/00497b94.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59080](../00c59/00c59080.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bfe0](../00c5b/00c5bfe0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5ec60](../00c5e/00c5ec60.md)
- [00c5eca0](../00c5e/00c5eca0.md)
- [00c5ed70](../00c5e/00c5ed70.md)
- [00c5edd0](../00c5e/00c5edd0.md)

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
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
                    /* try { // try from 00bcfe84 to 00cd01db has its CatchHandler @ 00bcfe84
                       catch() { ... } // from try @ 00bcfe84 with catch @ 00bcfe84
                       catch() { ... } // from try @ 00bd01e4 with catch @ 00bcfe84 */
    uVar12 = 0x25;
    if (param_3 != (char *)0x0) {
      sVar4 = strlen(param_3);
      uVar12 = 0x25;
      if (sVar4 != 0) {
        uVar12 = 0x26;
      }
    }
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
    uVar8 = FUN_00497b94(plVar5,*(undefined8 *)(*param_2 + 0x1f8),DAT_01127870,uVar6,uVar7);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar6);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar7);
    uVar9 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar5,lVar1,auStack_70);
    if ((uVar9 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      puVar13 = (undefined8 *)*param_2;
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar13);
                    /* try { // try from 00bcfe48 to 00ccfe4f has its CatchHandler @ 00bcfe50 */
      lVar10 = _Znwm(0x20);
                    /* catch() { ... } // from try @ 00bcfe48 with catch @ 00bcfe50
                       try { // try from 00bcfe50 to 00ccfe83 has its CatchHandler @ 00bcfcb8 */
      _ZN8firebase12FutureHandleC1ERKS0_(lVar10,auStack_90);
      puVar3 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9cac0
      ;
      *(undefined8 **)(lVar10 + 0x10) = puVar13;
      *(undefined **)(lVar10 + 0x18) = puVar3;
      if ((*(byte *)(puVar13 + 0x28) & 1) == 0) {
        lVar11 = (long)puVar13 + 0x141;
      }
      else {
        lVar11 = puVar13[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar8,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9caa0
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
<a id="insn-00bcfd1c"></a> `00bcfd1c` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcfd20"></a> `00bcfd20` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfd24"></a> `00bcfd24` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfd28"></a> `00bcfd28` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfd2c"></a> `00bcfd2c` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfd30"></a> `00bcfd30` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcfd34"></a> `00bcfd34` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfd38"></a> `00bcfd38` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcfd3c"></a> `00bcfd3c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcfd40"></a> `00bcfd40` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfd44"></a> `00bcfd44` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcfd48"></a> `00bcfd48` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcfd4c"></a> `00bcfd4c` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00bcfd50"></a> `00bcfd50` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfd54"></a> `00bcfd54` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcfd58"></a> `00bcfd58` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bcfd5c"></a> `00bcfd5c` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfd60"></a> `00bcfd60` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfd64"></a> `00bcfd64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcfd68"></a> `00bcfd68` | `ce 3b 02 94` | bl 0x00c5eca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd6c"></a> `00bcfd6c` | `77 08 00 b4` | cbz x23,0x00bcfe78 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd70"></a> `00bcfd70` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcfd74"></a> `00bcfd74` | `c3 24 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd78"></a> `00bcfd78` | `18 08 00 b4` | cbz x24,0x00bcfe78 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd7c"></a> `00bcfd7c` | `e0 07 00 b4` | cbz x0,0x00bcfe78 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd80"></a> `00bcfd80` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcfd84"></a> `00bcfd84` | `bf 24 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd88"></a> `00bcfd88` | `80 07 00 b4` | cbz x0,0x00bcfe78 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd8c"></a> `00bcfd8c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcfd90"></a> `00bcfd90` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcfd94"></a> `00bcfd94` | `e3 30 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd98"></a> `00bcfd98` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcfd9c"></a> `00bcfd9c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcfda0"></a> `00bcfda0` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcfda4"></a> `00bcfda4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcfda8"></a> `00bcfda8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfdac"></a> `00bcfdac` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcfdb0"></a> `00bcfdb0` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bcfdb4"></a> `00bcfdb4` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcfdb8"></a> `00bcfdb8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcfdbc"></a> `00bcfdbc` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcfdc0"></a> `00bcfdc0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfdc4"></a> `00bcfdc4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcfdc8"></a> `00bcfdc8` | `c9 2a 00 90` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcfdcc"></a> `00bcfdcc` | `22 39 44 f9` | ldr x2,[x9, #0x870] | `FALL_THROUGH`
<a id="insn-00bcfdd0"></a> `00bcfdd0` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcfdd4"></a> `00bcfdd4` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcfdd8"></a> `00bcfdd8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcfddc"></a> `00bcfddc` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00bcfde0"></a> `00bcfde0` | `e4 03 18 aa` | mov x4,x24 | `FALL_THROUGH`
<a id="insn-00bcfde4"></a> `00bcfde4` | `6c 1f e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfde8"></a> `00bcfde8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcfdec"></a> `00bcfdec` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcfdf0"></a> `00bcfdf0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcfdf4"></a> `00bcfdf4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcfdf8"></a> `00bcfdf8` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bcfdfc"></a> `00bcfdfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfe00"></a> `00bcfe00` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcfe04"></a> `00bcfe04` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcfe08"></a> `00bcfe08` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcfe0c"></a> `00bcfe0c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcfe10"></a> `00bcfe10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfe14"></a> `00bcfe14` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfe18"></a> `00bcfe18` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcfe1c"></a> `00bcfe1c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfe20"></a> `00bcfe20` | `d4 3b 02 94` | bl 0x00c5ed70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe24"></a> `00bcfe24` | `c0 08 00 37` | tbnz w0,#0x0,0x00bcff3c | `CONDITIONAL_JUMP`
<a id="insn-00bcfe28"></a> `00bcfe28` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcfe2c"></a> `00bcfe2c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfe30"></a> `00bcfe30` | `1c 30 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe34"></a> `00bcfe34` | `d9 02 40 f9` | ldr x25,[x22] | `FALL_THROUGH`
<a id="insn-00bcfe38"></a> `00bcfe38` | `20 03 40 f9` | ldr x0,[x25] | `FALL_THROUGH`
<a id="insn-00bcfe3c"></a> `00bcfe3c` | `b9 30 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe40"></a> `00bcfe40` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcfe44"></a> `00bcfe44` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfe48"></a> `00bcfe48` | `3a 24 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe4c"></a> `00bcfe4c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcfe50"></a> `00bcfe50` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bcfe54"></a> `00bcfe54` | `13 30 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe58"></a> `00bcfe58` | `68 06 00 b0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bcfe5c"></a> `00bcfe5c` | `08 61 45 f9` | ldr x8,[x8, #0xac0] | `FALL_THROUGH`
<a id="insn-00bcfe60"></a> `00bcfe60` | `19 23 01 a9` | stp x25,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfe64"></a> `00bcfe64` | `28 03 45 39` | ldrb w8,[x25, #0x140] | `FALL_THROUGH`
<a id="insn-00bcfe68"></a> `00bcfe68` | `e8 04 00 37` | tbnz w8,#0x0,0x00bcff04 | `CONDITIONAL_JUMP`
<a id="insn-00bcfe6c"></a> `00bcfe6c` | `28 03 05 91` | add x8,x25,#0x140 | `FALL_THROUGH`
<a id="insn-00bcfe70"></a> `00bcfe70` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfe74"></a> `00bcfe74` | `25 00 00 14` | b 0x00bcff08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcfe78"></a> `00bcfe78` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfe7c"></a> `00bcfe7c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfe80"></a> `00bcfe80` | `08 30 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe84"></a> `00bcfe84` | `b5 04 80 52` | mov w21,#0x25 | `FALL_THROUGH`
<a id="insn-00bcfe88"></a> `00bcfe88` | `b7 00 00 b4` | cbz x23,0x00bcfe9c | `CONDITIONAL_JUMP`
<a id="insn-00bcfe8c"></a> `00bcfe8c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcfe90"></a> `00bcfe90` | `7c 24 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe94"></a> `00bcfe94` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bcfe98"></a> `00bcfe98` | `b5 06 95 1a` | cinc w21,w21,ne | `FALL_THROUGH`
<a id="insn-00bcfe9c"></a> `00bcfe9c` | `e3 b6 ff b0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcfea0"></a> `00bcfea0` | `63 b8 0b 91` | add x3,x3,#0x2ee | `FALL_THROUGH`
<a id="insn-00bcfea4"></a> `00bcfea4` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfea8"></a> `00bcfea8` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcfeac"></a> `00bcfeac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcfeb0"></a> `00bcfeb0` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bcfeb4"></a> `00bcfeb4` | `6b 3b 02 94` | bl 0x00c5ec60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfeb8"></a> `00bcfeb8` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfebc"></a> `00bcfebc` | `1d 2f 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfec0"></a> `00bcfec0` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfec4"></a> `00bcfec4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfec8"></a> `00bcfec8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfecc"></a> `00bcfecc` | `c1 3b 02 94` | bl 0x00c5edd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfed0"></a> `00bcfed0` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfed4"></a> `00bcfed4` | `17 2f 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfed8"></a> `00bcfed8` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfedc"></a> `00bcfedc` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfee0"></a> `00bcfee0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcfee4"></a> `00bcfee4` | `61 03 00 54` | b.ne 0x00bcff50 | `CONDITIONAL_JUMP`
<a id="insn-00bcfee8"></a> `00bcfee8` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcfeec"></a> `00bcfeec` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfef0"></a> `00bcfef0` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfef4"></a> `00bcfef4` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfef8"></a> `00bcfef8` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfefc"></a> `00bcfefc` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcff00"></a> `00bcff00` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcff04"></a> `00bcff04` | `24 ab 40 f9` | ldr x4,[x25, #0x150] | `FALL_THROUGH`
<a id="insn-00bcff08"></a> `00bcff08` | `62 06 00 b0` | adrp x2,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bcff0c"></a> `00bcff0c` | `42 50 45 f9` | ldr x2,[x2, #0xaa0] | `FALL_THROUGH`
<a id="insn-00bcff10"></a> `00bcff10` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bcff14"></a> `00bcff14` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcff18"></a> `00bcff18` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcff1c"></a> `00bcff1c` | `31 30 02 94` | bl 0x00c5bfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff20"></a> `00bcff20` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcff24"></a> `00bcff24` | `03 2f 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff28"></a> `00bcff28` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcff2c"></a> `00bcff2c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcff30"></a> `00bcff30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcff34"></a> `00bcff34` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcff38"></a> `00bcff38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcff3c"></a> `00bcff3c` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcff40"></a> `00bcff40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff44"></a> `00bcff44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcff48"></a> `00bcff48` | `a2 3b 02 94` | bl 0x00c5edd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff4c"></a> `00bcff4c` | `e1 ff ff 17` | b 0x00bcfed0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcff50"></a> `00bcff50` | `0c 24 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfd1c`](#insn-00bcfd1c) 範囲 `[['00bcfd1c', '00bcfd6f']]`
  - `CONDITIONAL_JUMP` [`00bcfd6c`](#insn-00bcfd6c) → [`00bcfe78`](#insn-00bcfe78)
  - `FALL_THROUGH` [`00bcfd6c`](#insn-00bcfd6c) → [`00bcfd70`](#insn-00bcfd70)
- ブロック [`00bcfd70`](#insn-00bcfd70) 範囲 `[['00bcfd70', '00bcfd7b']]`
  - `CONDITIONAL_JUMP` [`00bcfd78`](#insn-00bcfd78) → [`00bcfe78`](#insn-00bcfe78)
  - `FALL_THROUGH` [`00bcfd78`](#insn-00bcfd78) → [`00bcfd7c`](#insn-00bcfd7c)
- ブロック [`00bcfd7c`](#insn-00bcfd7c) 範囲 `[['00bcfd7c', '00bcfd7f']]`
  - `CONDITIONAL_JUMP` [`00bcfd7c`](#insn-00bcfd7c) → [`00bcfe78`](#insn-00bcfe78)
  - `FALL_THROUGH` [`00bcfd7c`](#insn-00bcfd7c) → [`00bcfd80`](#insn-00bcfd80)
- ブロック [`00bcfd80`](#insn-00bcfd80) 範囲 `[['00bcfd80', '00bcfd8b']]`
  - `CONDITIONAL_JUMP` [`00bcfd88`](#insn-00bcfd88) → [`00bcfe78`](#insn-00bcfe78)
  - `FALL_THROUGH` [`00bcfd88`](#insn-00bcfd88) → [`00bcfd8c`](#insn-00bcfd8c)
- ブロック [`00bcfd8c`](#insn-00bcfd8c) 範囲 `[['00bcfd8c', '00bcfe27']]`
  - `CONDITIONAL_JUMP` [`00bcfe24`](#insn-00bcfe24) → [`00bcff3c`](#insn-00bcff3c)
  - `FALL_THROUGH` [`00bcfe24`](#insn-00bcfe24) → [`00bcfe28`](#insn-00bcfe28)
- ブロック [`00bcfe28`](#insn-00bcfe28) 範囲 `[['00bcfe28', '00bcfe47']]`
  - `FALL_THROUGH` [`00bcfe44`](#insn-00bcfe44) → [`00bcfe48`](#insn-00bcfe48)
- ブロック [`00bcfe48`](#insn-00bcfe48) 範囲 `[['00bcfe48', '00bcfe4f']]`
  - `FALL_THROUGH` [`00bcfe4c`](#insn-00bcfe4c) → [`00bcfe50`](#insn-00bcfe50)
- ブロック [`00bcfe50`](#insn-00bcfe50) 範囲 `[['00bcfe50', '00bcfe6b']]`
  - `CONDITIONAL_JUMP` [`00bcfe68`](#insn-00bcfe68) → [`00bcff04`](#insn-00bcff04)
  - `FALL_THROUGH` [`00bcfe68`](#insn-00bcfe68) → [`00bcfe6c`](#insn-00bcfe6c)
- ブロック [`00bcfe6c`](#insn-00bcfe6c) 範囲 `[['00bcfe6c', '00bcfe77']]`
  - `UNCONDITIONAL_JUMP` [`00bcfe74`](#insn-00bcfe74) → [`00bcff08`](#insn-00bcff08)
- ブロック [`00bcfe78`](#insn-00bcfe78) 範囲 `[['00bcfe78', '00bcfe83']]`
  - `FALL_THROUGH` [`00bcfe80`](#insn-00bcfe80) → [`00bcfe84`](#insn-00bcfe84)
- ブロック [`00bcfe84`](#insn-00bcfe84) 範囲 `[['00bcfe84', '00bcfe8b']]`
  - `CONDITIONAL_JUMP` [`00bcfe88`](#insn-00bcfe88) → [`00bcfe9c`](#insn-00bcfe9c)
  - `FALL_THROUGH` [`00bcfe88`](#insn-00bcfe88) → [`00bcfe8c`](#insn-00bcfe8c)
- ブロック [`00bcfe8c`](#insn-00bcfe8c) 範囲 `[['00bcfe8c', '00bcfe9b']]`
  - `FALL_THROUGH` [`00bcfe98`](#insn-00bcfe98) → [`00bcfe9c`](#insn-00bcfe9c)
- ブロック [`00bcfe9c`](#insn-00bcfe9c) 範囲 `[['00bcfe9c', '00bcfecf']]`
  - `FALL_THROUGH` [`00bcfecc`](#insn-00bcfecc) → [`00bcfed0`](#insn-00bcfed0)
- ブロック [`00bcfed0`](#insn-00bcfed0) 範囲 `[['00bcfed0', '00bcfee7']]`
  - `CONDITIONAL_JUMP` [`00bcfee4`](#insn-00bcfee4) → [`00bcff50`](#insn-00bcff50)
  - `FALL_THROUGH` [`00bcfee4`](#insn-00bcfee4) → [`00bcfee8`](#insn-00bcfee8)
- ブロック [`00bcfee8`](#insn-00bcfee8) 範囲 `[['00bcfee8', '00bcff03']]`
- ブロック [`00bcff04`](#insn-00bcff04) 範囲 `[['00bcff04', '00bcff07']]`
  - `FALL_THROUGH` [`00bcff04`](#insn-00bcff04) → [`00bcff08`](#insn-00bcff08)
- ブロック [`00bcff08`](#insn-00bcff08) 範囲 `[['00bcff08', '00bcff3b']]`
  - `FALL_THROUGH` [`00bcff38`](#insn-00bcff38) → [`00bcff3c`](#insn-00bcff3c)
- ブロック [`00bcff3c`](#insn-00bcff3c) 範囲 `[['00bcff3c', '00bcff4f']]`
  - `UNCONDITIONAL_JUMP` [`00bcff4c`](#insn-00bcff4c) → [`00bcfed0`](#insn-00bcfed0)
- ブロック [`00bcff50`](#insn-00bcff50) 範囲 `[['00bcff50', '00bcff53']]`

## 命令位置別の参照

- [`00bcfd20`](#insn-00bcfd20) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd24`](#insn-00bcfd24) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd28`](#insn-00bcfd28) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd2c`](#insn-00bcfd2c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd30`](#insn-00bcfd30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd50`](#insn-00bcfd50) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd68`](#insn-00bcfd68) → [`00c5eca0`](../00c5e/00c5eca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eca0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd6c`](#insn-00bcfd6c) → [`00bcfe78`](#insn-00bcfe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd74`](#insn-00bcfd74) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd78`](#insn-00bcfd78) → [`00bcfe78`](#insn-00bcfe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd7c`](#insn-00bcfd7c) → [`00bcfe78`](#insn-00bcfe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd84`](#insn-00bcfd84) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd88`](#insn-00bcfd88) → [`00bcfe78`](#insn-00bcfe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd94`](#insn-00bcfd94) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdcc`](#insn-00bcfdcc) → `01127870`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcfde4`](#insn-00bcfde4) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe20`](#insn-00bcfe20) → [`00c5ed70`](../00c5e/00c5ed70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ed70` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe24`](#insn-00bcfe24) → [`00bcff3c`](#insn-00bcff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe30`](#insn-00bcfe30) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe3c`](#insn-00bcfe3c) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe48`](#insn-00bcfe48) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe54`](#insn-00bcfe54) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe5c`](#insn-00bcfe5c) → `00c9cac0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcfe60`](#insn-00bcfe60) → [`00bd58bc`](../00bd5/00bd58bc.md) · `DATA` · `ANALYSIS` · 関数 `00bd58bc` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bcfe68`](#insn-00bcfe68) → [`00bcff04`](#insn-00bcff04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe74`](#insn-00bcfe74) → [`00bcff08`](#insn-00bcff08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe80`](#insn-00bcfe80) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe88`](#insn-00bcfe88) → [`00bcfe9c`](#insn-00bcfe9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe90`](#insn-00bcfe90) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bcfea0`](#insn-00bcfea0) → `002ac2ee`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcfeb4`](#insn-00bcfeb4) → [`00c5ec60`](../00c5e/00c5ec60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ec60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfebc`](#insn-00bcfebc) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bcfecc`](#insn-00bcfecc) → [`00c5edd0`](../00c5e/00c5edd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5edd0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfed4`](#insn-00bcfed4) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bcfedc`](#insn-00bcfedc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee4`](#insn-00bcfee4) → [`00bcff50`](#insn-00bcff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee8`](#insn-00bcfee8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfeec`](#insn-00bcfeec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfef0`](#insn-00bcfef0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfef4`](#insn-00bcfef4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfef8`](#insn-00bcfef8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff0c`](#insn-00bcff0c) → `00c9caa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcff0c`](#insn-00bcff0c) → [`00bd0dd4`](../00bd0/00bd0dd4.md) · `PARAM` · `ANALYSIS` · 関数 `00bd0dd4` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcff1c`](#insn-00bcff1c) → [`00c5bfe0`](../00c5b/00c5bfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bcff24`](#insn-00bcff24) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bcff48`](#insn-00bcff48) → [`00c5edd0`](../00c5e/00c5edd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5edd0` · 推定シンボル `None` · 推定型 `None`
- [`00bcff4c`](#insn-00bcff4c) → [`00bcfed0`](#insn-00bcfed0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff50`](#insn-00bcff50) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfd20`](#insn-00bcfd20)

~~~json
{
  "source": "00bcfd20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd24`](#insn-00bcfd24)

~~~json
{
  "source": "00bcfd24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd28`](#insn-00bcfd28)

~~~json
{
  "source": "00bcfd28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd2c`](#insn-00bcfd2c)

~~~json
{
  "source": "00bcfd2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd30`](#insn-00bcfd30)

~~~json
{
  "source": "00bcfd30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd50`](#insn-00bcfd50)

~~~json
{
  "source": "00bcfd50",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd68`](#insn-00bcfd68)

~~~json
{
  "source": "00bcfd68",
  "target": "00c5eca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd6c`](#insn-00bcfd6c)

~~~json
{
  "source": "00bcfd6c",
  "target": "00bcfe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd74`](#insn-00bcfd74)

~~~json
{
  "source": "00bcfd74",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd78`](#insn-00bcfd78)

~~~json
{
  "source": "00bcfd78",
  "target": "00bcfe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd7c`](#insn-00bcfd7c)

~~~json
{
  "source": "00bcfd7c",
  "target": "00bcfe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd84`](#insn-00bcfd84)

~~~json
{
  "source": "00bcfd84",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd88`](#insn-00bcfd88)

~~~json
{
  "source": "00bcfd88",
  "target": "00bcfe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd94`](#insn-00bcfd94)

~~~json
{
  "source": "00bcfd94",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfdcc`](#insn-00bcfdcc)

~~~json
{
  "source": "00bcfdcc",
  "target": "01127870",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127870",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcfde4`](#insn-00bcfde4)

~~~json
{
  "source": "00bcfde4",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe20`](#insn-00bcfe20)

~~~json
{
  "source": "00bcfe20",
  "target": "00c5ed70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe24`](#insn-00bcfe24)

~~~json
{
  "source": "00bcfe24",
  "target": "00bcff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe30`](#insn-00bcfe30)

~~~json
{
  "source": "00bcfe30",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe3c`](#insn-00bcfe3c)

~~~json
{
  "source": "00bcfe3c",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe48`](#insn-00bcfe48)

~~~json
{
  "source": "00bcfe48",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe54`](#insn-00bcfe54)

~~~json
{
  "source": "00bcfe54",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe5c`](#insn-00bcfe5c)

~~~json
{
  "source": "00bcfe5c",
  "target": "00c9cac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cac0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcfe60`](#insn-00bcfe60)

~~~json
{
  "source": "00bcfe60",
  "target": "00bd58bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe68`](#insn-00bcfe68)

~~~json
{
  "source": "00bcfe68",
  "target": "00bcff04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe74`](#insn-00bcfe74)

~~~json
{
  "source": "00bcfe74",
  "target": "00bcff08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe80`](#insn-00bcfe80)

~~~json
{
  "source": "00bcfe80",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe88`](#insn-00bcfe88)

~~~json
{
  "source": "00bcfe88",
  "target": "00bcfe9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe90`](#insn-00bcfe90)

~~~json
{
  "source": "00bcfe90",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfea0`](#insn-00bcfea0)

~~~json
{
  "source": "00bcfea0",
  "target": "002ac2ee",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac2ee",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "456d70747920656d61696c206f722070617373776f726420617265206e6f7420",
  "capture_start": "002ac2ee",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcfeb4`](#insn-00bcfeb4)

~~~json
{
  "source": "00bcfeb4",
  "target": "00c5ec60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfebc`](#insn-00bcfebc)

~~~json
{
  "source": "00bcfebc",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfecc`](#insn-00bcfecc)

~~~json
{
  "source": "00bcfecc",
  "target": "00c5edd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfed4`](#insn-00bcfed4)

~~~json
{
  "source": "00bcfed4",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfedc`](#insn-00bcfedc)

~~~json
{
  "source": "00bcfedc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee4`](#insn-00bcfee4)

~~~json
{
  "source": "00bcfee4",
  "target": "00bcff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee8`](#insn-00bcfee8)

~~~json
{
  "source": "00bcfee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfeec`](#insn-00bcfeec)

~~~json
{
  "source": "00bcfeec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfef0`](#insn-00bcfef0)

~~~json
{
  "source": "00bcfef0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfef4`](#insn-00bcfef4)

~~~json
{
  "source": "00bcfef4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfef8`](#insn-00bcfef8)

~~~json
{
  "source": "00bcfef8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff0c`](#insn-00bcff0c)

~~~json
{
  "source": "00bcff0c",
  "target": "00c9caa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9caa0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcff0c`](#insn-00bcff0c)

~~~json
{
  "source": "00bcff0c",
  "target": "00bd0dd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff1c`](#insn-00bcff1c)

~~~json
{
  "source": "00bcff1c",
  "target": "00c5bfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff24`](#insn-00bcff24)

~~~json
{
  "source": "00bcff24",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff48`](#insn-00bcff48)

~~~json
{
  "source": "00bcff48",
  "target": "00c5edd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff4c`](#insn-00bcff4c)

~~~json
{
  "source": "00bcff4c",
  "target": "00bcfed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff50`](#insn-00bcff50)

~~~json
{
  "source": "00bcff50",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
