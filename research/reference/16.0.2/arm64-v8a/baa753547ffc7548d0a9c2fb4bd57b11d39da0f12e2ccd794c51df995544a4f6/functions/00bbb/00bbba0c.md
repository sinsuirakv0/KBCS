# 00bbba0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbb970`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-b8d4128530da96956478c9ed0f11b30d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbca00`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbca00.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-e1d67ed9e002b51e3bce280b6064b11f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbba0c",
  "name": "_ZN8firebase9messaging11UnsubscribeEPKc",
  "size": 552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92eb66a55f1eae08cd0d4e7f6c05219a45cd8aef6613b365cc53bba28558c869",
  "source_text_sha256": "92eb66a55f1eae08cd0d4e7f6c05219a45cd8aef6613b365cc53bba28558c869",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbba0c",
        "00bbbc33"
      ]
    ],
    "bytes_sha256": "33bb14ad11768dfc59c2e5b31cffe9d4bf06a429b689bcf99809f336e6a922a2",
    "instruction_count": 138,
    "instruction_bytes": 552,
    "body_bytes": 552,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbbcdc](../00bbb/00bbbcdc.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aea0](../00c5a/00c5aea0.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b690](../00c5b/00c5b690.md)
- [00c5bd30](../00c5b/00c5bd30.md)
- [00c5d340](../00c5d/00c5d340.md)
- [00c5d6a0](../00c5d/00c5d6a0.md)

## 関連文字列（未確認候補）

~~~text
"Cannot update subscription for unknown reason."
"Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4041 bytes

~~~c

void _ZN8firebase9messaging11UnsubscribeEPKc(long param_1,undefined8 param_2)

{
  ulong *puVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  undefined8 uVar5;
  undefined1 *puVar6;
  undefined1 auStack_b0 [16];
  ulong local_a0;
  ulong uStack_98;
  void *local_90;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  uVar3 = DAT_01126470;
  puVar6 = auStack_b0;
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  if (DAT_01126460 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bbbacc to 00cbbaf3 has its CatchHandler @ 00bbc804 */
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
    goto LAB_00bbbbdc;
  }
  _ZN8firebase5Mutex7AcquireEv(DAT_01126470);
  uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* try { // try from 00bbba64 to 00cbba6f has its CatchHandler @ 00bbc7dc */
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(&local_a0,uVar5,1,0,0);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,&local_a0);
  _ZN8firebase12FutureHandleD2Ev(&local_a0);
  lVar4 = DAT_01126480;
  if (DAT_01126508 == '\x01') {
    FUN_00bbbcdc(param_2,auStack_68);
  }
  else {
    if (DAT_01126500 == 2) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_78,3,
                 "Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
                 ,&local_a0);
      puVar6 = auStack_78;
    }
    else {
      if (DAT_01126480 != 0) {
                    /* try { // try from 00bbbb34 to 00cbbb3f has its CatchHandler @ 00bbc7d8 */
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
                  (&local_a0,param_2);
        _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_68);
        puVar1 = *(ulong **)(lVar4 + 8);
        if (puVar1 < *(ulong **)(lVar4 + 0x10)) {
          puVar1[2] = (ulong)local_90;
          puVar1[1] = uStack_98;
          *puVar1 = local_a0;
          uStack_98 = 0;
          local_90 = (void *)0x0;
          local_a0 = 0;
                    /* try { // try from 00bbbb7c to 00cbbba3 has its CatchHandler @ 00bbc800 */
          _ZN8firebase12FutureHandleC1EOS0_(puVar1 + 3,auStack_88);
          *(ulong **)(lVar4 + 8) = puVar1 + 5;
        }
        else {
          _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_
                    (lVar4,&local_a0);
        }
        _ZN8firebase12FutureHandleD2Ev(auStack_88);
                    /* try { // try from 00bbbc20 to 00cbbc47 has its CatchHandler @ 00bbc7fc */
        if ((local_a0 & 1) != 0) {
          _ZdlPv(local_90);
        }
        goto LAB_00bbbbbc;
      }
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_b0,auStack_68);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_b0,4,"Cannot update subscription for unknown reason.",&local_a0);
    }
    _ZN8firebase12FutureHandleD2Ev(puVar6);
  }
LAB_00bbbbbc:
  _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,uVar5,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
LAB_00bbbbdc:
                    /* try { // try from 00bbbbe4 to 00cbbbef has its CatchHandler @ 00bbc7d4 */
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
<a id="insn-00bbba0c"></a> `00bbba0c` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbba10"></a> `00bbba10` | `f9 33 00 f9` | str x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbba14"></a> `00bbba14` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbba18"></a> `00bbba18` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbba1c"></a> `00bbba1c` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbba20"></a> `00bbba20` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbba24"></a> `00bbba24` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbba28"></a> `00bbba28` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbba2c"></a> `00bbba2c` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbba30"></a> `00bbba30` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bbba34"></a> `00bbba34` | `a9 83 1b f8` | stur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bbba38"></a> `00bbba38` | `49 2b 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbba3c"></a> `00bbba3c` | `29 31 42 f9` | ldr x9,[x9, #0x460] | `FALL_THROUGH`
<a id="insn-00bbba40"></a> `00bbba40` | `49 03 00 b4` | cbz x9,0x00bbbaa8 | `CONDITIONAL_JUMP`
<a id="insn-00bbba44"></a> `00bbba44` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbba48"></a> `00bbba48` | `13 39 42 f9` | ldr x19,[x8, #0x470] | `FALL_THROUGH`
<a id="insn-00bbba4c"></a> `00bbba4c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbba50"></a> `00bbba50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbba54"></a> `00bbba54` | `1f 7c 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbba58"></a> `00bbba58` | `3a 86 02 94` | bl 0x00c5d340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbba5c"></a> `00bbba5c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbba60"></a> `00bbba60` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbba64"></a> `00bbba64` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bbba68"></a> `00bbba68` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbba6c"></a> `00bbba6c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbba70"></a> `00bbba70` | `28 7d 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbba74"></a> `00bbba74` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbba78"></a> `00bbba78` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbba7c"></a> `00bbba7c` | `15 7d 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbba80"></a> `00bbba80` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbba84"></a> `00bbba84` | `37 7c 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbba88"></a> `00bbba88` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbba8c"></a> `00bbba8c` | `08 21 54 39` | ldrb w8,[x8, #0x508] | `FALL_THROUGH`
<a id="insn-00bbba90"></a> `00bbba90` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbba94"></a> `00bbba94` | `81 02 00 54` | b.ne 0x00bbbae4 | `CONDITIONAL_JUMP`
<a id="insn-00bbba98"></a> `00bbba98` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbba9c"></a> `00bbba9c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbaa0"></a> `00bbbaa0` | `8f 00 00 94` | bl 0x00bbbcdc | `UNCONDITIONAL_CALL`
<a id="insn-00bbbaa4"></a> `00bbbaa4` | `46 00 00 14` | b 0x00bbbbbc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbaa8"></a> `00bbbaa8` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbbaac"></a> `00bbbaac` | `00 20 23 91` | add x0,x0,#0x8c8 | `FALL_THROUGH`
<a id="insn-00bbbab0"></a> `00bbbab0` | `b0 7c 02 94` | bl 0x00c5ad70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbab4"></a> `00bbbab4` | `a0 b7 ff b0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbbab8"></a> `00bbbab8` | `00 6c 1c 91` | add x0,x0,#0x71b | `FALL_THROUGH`
<a id="insn-00bbbabc"></a> `00bbbabc` | `85 7d 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbac0"></a> `00bbbac0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbac4"></a> `00bbbac4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbbac8"></a> `00bbbac8` | `9e 7c 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbacc"></a> `00bbbacc` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bbbad0"></a> `00bbbad0` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbad4"></a> `00bbbad4` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbbad8"></a> `00bbbad8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbbadc"></a> `00bbbadc` | `75 7c 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbae0"></a> `00bbbae0` | `3f 00 00 14` | b 0x00bbbbdc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbae4"></a> `00bbbae4` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbae8"></a> `00bbbae8` | `08 01 45 b9` | ldr w8,[x8, #0x500] | `FALL_THROUGH`
<a id="insn-00bbbaec"></a> `00bbbaec` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbbaf0"></a> `00bbbaf0` | `a1 01 00 54` | b.ne 0x00bbbb24 | `CONDITIONAL_JUMP`
<a id="insn-00bbbaf4"></a> `00bbbaf4` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbbaf8"></a> `00bbbaf8` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbbafc"></a> `00bbbafc` | `f5 7c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb00"></a> `00bbbb00` | `83 ba ff f0` | adrp x3,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbbb04"></a> `00bbbb04` | `63 2c 20 91` | add x3,x3,#0x80b | `FALL_THROUGH`
<a id="insn-00bbbb08"></a> `00bbbb08` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbbb0c"></a> `00bbbb0c` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbb10"></a> `00bbbb10` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-00bbbb14"></a> `00bbbb14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbb18"></a> `00bbbb18` | `d6 7c 02 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb1c"></a> `00bbbb1c` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbbb20"></a> `00bbbb20` | `26 00 00 14` | b 0x00bbbbb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbb24"></a> `00bbbb24` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbb28"></a> `00bbbb28` | `17 41 42 f9` | ldr x23,[x8, #0x480] | `FALL_THROUGH`
<a id="insn-00bbbb2c"></a> `00bbbb2c` | `17 03 00 b4` | cbz x23,0x00bbbb8c | `CONDITIONAL_JUMP`
<a id="insn-00bbbb30"></a> `00bbbb30` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbb34"></a> `00bbbb34` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbbb38"></a> `00bbbb38` | `f9 43 00 91` | add x25,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbb3c"></a> `00bbbb3c` | `d5 7e 02 94` | bl 0x00c5b690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb40"></a> `00bbbb40` | `36 63 00 91` | add x22,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbb44"></a> `00bbbb44` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbbb48"></a> `00bbbb48` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbb4c"></a> `00bbbb4c` | `e1 7c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb50"></a> `00bbbb50` | `f9 a2 40 a9` | ldp x25,x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbb54"></a> `00bbbb54` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bbbb58"></a> `00bbbb58` | `82 05 00 54` | b.cs 0x00bbbc08 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb5c"></a> `00bbbb5c` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbb60"></a> `00bbbb60` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbb64"></a> `00bbbb64` | `20 63 00 91` | add x0,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbb68"></a> `00bbbb68` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbbb6c"></a> `00bbbb6c` | `28 0b 00 f9` | str x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbb70"></a> `00bbbb70` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00bbbb74"></a> `00bbbb74` | `ff ff 01 a9` | stp xzr,xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbb78"></a> `00bbbb78` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbb7c"></a> `00bbbb7c` | `6d 80 02 94` | bl 0x00c5bd30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb80"></a> `00bbbb80` | `28 a3 00 91` | add x8,x25,#0x28 | `FALL_THROUGH`
<a id="insn-00bbbb84"></a> `00bbbb84` | `e8 06 00 f9` | str x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbb88"></a> `00bbbb88` | `23 00 00 14` | b 0x00bbbc14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbb8c"></a> `00bbbb8c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbbb90"></a> `00bbbb90` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbbb94"></a> `00bbbb94` | `cf 7c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb98"></a> `00bbbb98` | `83 ba ff f0` | adrp x3,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbbb9c"></a> `00bbbb9c` | `63 78 21 91` | add x3,x3,#0x85e | `FALL_THROUGH`
<a id="insn-00bbbba0"></a> `00bbbba0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbbba4"></a> `00bbbba4` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbba8"></a> `00bbbba8` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00bbbbac"></a> `00bbbbac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbbb0"></a> `00bbbbb0` | `b0 7c 02 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbb4"></a> `00bbbbb4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbbbb8"></a> `00bbbbb8` | `ea 7b 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbbc"></a> `00bbbbbc` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbbbc0"></a> `00bbbbc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbbc4"></a> `00bbbbc4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbbbc8"></a> `00bbbbc8` | `b6 7c 02 94` | bl 0x00c5aea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbcc"></a> `00bbbbcc` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbbbd0"></a> `00bbbbd0` | `e4 7b 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbd4"></a> `00bbbbd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbbd8"></a> `00bbbbd8` | `c2 7b 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbdc"></a> `00bbbbdc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbbe0"></a> `00bbbbe0` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bbbbe4"></a> `00bbbbe4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbbe8"></a> `00bbbbe8` | `41 02 00 54` | b.ne 0x00bbbc30 | `CONDITIONAL_JUMP`
<a id="insn-00bbbbec"></a> `00bbbbec` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbbbf0"></a> `00bbbbf0` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbbbf4"></a> `00bbbbf4` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbbbf8"></a> `00bbbbf8` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbbfc"></a> `00bbbbfc` | `f9 33 40 f9` | ldr x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbc00"></a> `00bbbc00` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbbc04"></a> `00bbbc04` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbc08"></a> `00bbbc08` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbc0c"></a> `00bbbc0c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbbc10"></a> `00bbbc10` | `a4 86 02 94` | bl 0x00c5d6a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbc14"></a> `00bbbc14` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbc18"></a> `00bbbc18` | `d2 7b 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbc1c"></a> `00bbbc1c` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbc20"></a> `00bbbc20` | `e8 fc 07 36` | tbz w8,#0x0,0x00bbbbbc | `CONDITIONAL_JUMP`
<a id="insn-00bbbc24"></a> `00bbbc24` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbc28"></a> `00bbbc28` | `d6 70 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbc2c"></a> `00bbbc2c` | `e4 ff ff 17` | b 0x00bbbbbc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbc30"></a> `00bbbc30` | `e0 70 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbba0c`](#insn-00bbba0c) 範囲 `[['00bbba0c', '00bbba43']]`
  - `CONDITIONAL_JUMP` [`00bbba40`](#insn-00bbba40) → [`00bbbaa8`](#insn-00bbbaa8)
  - `FALL_THROUGH` [`00bbba40`](#insn-00bbba40) → [`00bbba44`](#insn-00bbba44)
- ブロック [`00bbba44`](#insn-00bbba44) 範囲 `[['00bbba44', '00bbba63']]`
  - `FALL_THROUGH` [`00bbba60`](#insn-00bbba60) → [`00bbba64`](#insn-00bbba64)
- ブロック [`00bbba64`](#insn-00bbba64) 範囲 `[['00bbba64', '00bbba97']]`
  - `CONDITIONAL_JUMP` [`00bbba94`](#insn-00bbba94) → [`00bbbae4`](#insn-00bbbae4)
  - `FALL_THROUGH` [`00bbba94`](#insn-00bbba94) → [`00bbba98`](#insn-00bbba98)
- ブロック [`00bbba98`](#insn-00bbba98) 範囲 `[['00bbba98', '00bbbaa7']]`
  - `UNCONDITIONAL_JUMP` [`00bbbaa4`](#insn-00bbbaa4) → [`00bbbbbc`](#insn-00bbbbbc)
- ブロック [`00bbbaa8`](#insn-00bbbaa8) 範囲 `[['00bbbaa8', '00bbbacb']]`
  - `FALL_THROUGH` [`00bbbac8`](#insn-00bbbac8) → [`00bbbacc`](#insn-00bbbacc)
- ブロック [`00bbbacc`](#insn-00bbbacc) 範囲 `[['00bbbacc', '00bbbae3']]`
  - `UNCONDITIONAL_JUMP` [`00bbbae0`](#insn-00bbbae0) → [`00bbbbdc`](#insn-00bbbbdc)
- ブロック [`00bbbae4`](#insn-00bbbae4) 範囲 `[['00bbbae4', '00bbbaf3']]`
  - `CONDITIONAL_JUMP` [`00bbbaf0`](#insn-00bbbaf0) → [`00bbbb24`](#insn-00bbbb24)
  - `FALL_THROUGH` [`00bbbaf0`](#insn-00bbbaf0) → [`00bbbaf4`](#insn-00bbbaf4)
- ブロック [`00bbbaf4`](#insn-00bbbaf4) 範囲 `[['00bbbaf4', '00bbbb23']]`
  - `UNCONDITIONAL_JUMP` [`00bbbb20`](#insn-00bbbb20) → [`00bbbbb8`](#insn-00bbbbb8)
- ブロック [`00bbbb24`](#insn-00bbbb24) 範囲 `[['00bbbb24', '00bbbb2f']]`
  - `CONDITIONAL_JUMP` [`00bbbb2c`](#insn-00bbbb2c) → [`00bbbb8c`](#insn-00bbbb8c)
  - `FALL_THROUGH` [`00bbbb2c`](#insn-00bbbb2c) → [`00bbbb30`](#insn-00bbbb30)
- ブロック [`00bbbb30`](#insn-00bbbb30) 範囲 `[['00bbbb30', '00bbbb33']]`
  - `FALL_THROUGH` [`00bbbb30`](#insn-00bbbb30) → [`00bbbb34`](#insn-00bbbb34)
- ブロック [`00bbbb34`](#insn-00bbbb34) 範囲 `[['00bbbb34', '00bbbb5b']]`
  - `CONDITIONAL_JUMP` [`00bbbb58`](#insn-00bbbb58) → [`00bbbc08`](#insn-00bbbc08)
  - `FALL_THROUGH` [`00bbbb58`](#insn-00bbbb58) → [`00bbbb5c`](#insn-00bbbb5c)
- ブロック [`00bbbb5c`](#insn-00bbbb5c) 範囲 `[['00bbbb5c', '00bbbb7b']]`
  - `FALL_THROUGH` [`00bbbb78`](#insn-00bbbb78) → [`00bbbb7c`](#insn-00bbbb7c)
- ブロック [`00bbbb7c`](#insn-00bbbb7c) 範囲 `[['00bbbb7c', '00bbbb8b']]`
  - `UNCONDITIONAL_JUMP` [`00bbbb88`](#insn-00bbbb88) → [`00bbbc14`](#insn-00bbbc14)
- ブロック [`00bbbb8c`](#insn-00bbbb8c) 範囲 `[['00bbbb8c', '00bbbbb7']]`
  - `FALL_THROUGH` [`00bbbbb4`](#insn-00bbbbb4) → [`00bbbbb8`](#insn-00bbbbb8)
- ブロック [`00bbbbb8`](#insn-00bbbbb8) 範囲 `[['00bbbbb8', '00bbbbbb']]`
  - `FALL_THROUGH` [`00bbbbb8`](#insn-00bbbbb8) → [`00bbbbbc`](#insn-00bbbbbc)
- ブロック [`00bbbbbc`](#insn-00bbbbbc) 範囲 `[['00bbbbbc', '00bbbbdb']]`
  - `FALL_THROUGH` [`00bbbbd8`](#insn-00bbbbd8) → [`00bbbbdc`](#insn-00bbbbdc)
- ブロック [`00bbbbdc`](#insn-00bbbbdc) 範囲 `[['00bbbbdc', '00bbbbe3']]`
  - `FALL_THROUGH` [`00bbbbe0`](#insn-00bbbbe0) → [`00bbbbe4`](#insn-00bbbbe4)
- ブロック [`00bbbbe4`](#insn-00bbbbe4) 範囲 `[['00bbbbe4', '00bbbbeb']]`
  - `CONDITIONAL_JUMP` [`00bbbbe8`](#insn-00bbbbe8) → [`00bbbc30`](#insn-00bbbc30)
  - `FALL_THROUGH` [`00bbbbe8`](#insn-00bbbbe8) → [`00bbbbec`](#insn-00bbbbec)
- ブロック [`00bbbbec`](#insn-00bbbbec) 範囲 `[['00bbbbec', '00bbbc07']]`
- ブロック [`00bbbc08`](#insn-00bbbc08) 範囲 `[['00bbbc08', '00bbbc13']]`
  - `FALL_THROUGH` [`00bbbc10`](#insn-00bbbc10) → [`00bbbc14`](#insn-00bbbc14)
- ブロック [`00bbbc14`](#insn-00bbbc14) 範囲 `[['00bbbc14', '00bbbc1f']]`
  - `FALL_THROUGH` [`00bbbc1c`](#insn-00bbbc1c) → [`00bbbc20`](#insn-00bbbc20)
- ブロック [`00bbbc20`](#insn-00bbbc20) 範囲 `[['00bbbc20', '00bbbc23']]`
  - `CONDITIONAL_JUMP` [`00bbbc20`](#insn-00bbbc20) → [`00bbbbbc`](#insn-00bbbbbc)
  - `FALL_THROUGH` [`00bbbc20`](#insn-00bbbc20) → [`00bbbc24`](#insn-00bbbc24)
- ブロック [`00bbbc24`](#insn-00bbbc24) 範囲 `[['00bbbc24', '00bbbc2f']]`
  - `UNCONDITIONAL_JUMP` [`00bbbc2c`](#insn-00bbbc2c) → [`00bbbbbc`](#insn-00bbbbbc)
- ブロック [`00bbbc30`](#insn-00bbbc30) 範囲 `[['00bbbc30', '00bbbc33']]`

## 命令位置別の参照

- [`00bbba10`](#insn-00bbba10) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbba14`](#insn-00bbba14) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbba18`](#insn-00bbba18) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbba1c`](#insn-00bbba1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbba20`](#insn-00bbba20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbba34`](#insn-00bbba34) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbba3c`](#insn-00bbba3c) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbba40`](#insn-00bbba40) → [`00bbbaa8`](#insn-00bbbaa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbba48`](#insn-00bbba48) → `01126470`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbba54`](#insn-00bbba54) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbba58`](#insn-00bbba58) → [`00c5d340`](../00c5d/00c5d340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d340` · 推定シンボル `None` · 推定型 `None`
- [`00bbba70`](#insn-00bbba70) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bbba7c`](#insn-00bbba7c) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbba84`](#insn-00bbba84) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbba8c`](#insn-00bbba8c) → `01126508`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbba94`](#insn-00bbba94) → [`00bbbae4`](#insn-00bbbae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbaa0`](#insn-00bbbaa0) → [`00bbbcdc`](00bbbcdc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbbcdc` · 推定シンボル `None` · 推定型 `None`
- [`00bbbaa4`](#insn-00bbbaa4) → [`00bbbbbc`](#insn-00bbbbbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbaac`](#insn-00bbbaac) → `002a28c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbab0`](#insn-00bbbab0) → [`00c5ad70`](../00c5a/00c5ad70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad70` · 推定シンボル `None` · 推定型 `None`
- [`00bbbab8`](#insn-00bbbab8) → `002b071b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbabc`](#insn-00bbbabc) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbac8`](#insn-00bbbac8) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bbbadc`](#insn-00bbbadc) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbae0`](#insn-00bbbae0) → [`00bbbbdc`](#insn-00bbbbdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbae8`](#insn-00bbbae8) → `01126500`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbbaf0`](#insn-00bbbaf0) → [`00bbbb24`](#insn-00bbbb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbafc`](#insn-00bbbafc) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb04`](#insn-00bbbb04) → `0030e80b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbb18`](#insn-00bbbb18) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb20`](#insn-00bbbb20) → [`00bbbbb8`](#insn-00bbbbb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb28`](#insn-00bbbb28) → `01126480`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbb2c`](#insn-00bbbb2c) → [`00bbbb8c`](#insn-00bbbb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb3c`](#insn-00bbbb3c) → [`00c5b690`](../00c5b/00c5b690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b690` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb4c`](#insn-00bbbb4c) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb58`](#insn-00bbbb58) → [`00bbbc08`](#insn-00bbbc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb5c`](#insn-00bbbb5c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb60`](#insn-00bbbb60) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb74`](#insn-00bbbb74) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb78`](#insn-00bbbb78) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb7c`](#insn-00bbbb7c) → [`00c5bd30`](../00c5b/00c5bd30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd30` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb88`](#insn-00bbbb88) → [`00bbbc14`](#insn-00bbbc14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb94`](#insn-00bbbb94) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb9c`](#insn-00bbbb9c) → `0030e85e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbbb0`](#insn-00bbbbb0) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbb8`](#insn-00bbbbb8) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbc8`](#insn-00bbbbc8) → [`00c5aea0`](../00c5a/00c5aea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbd0`](#insn-00bbbbd0) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbd8`](#insn-00bbbbd8) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbe0`](#insn-00bbbbe0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbe8`](#insn-00bbbbe8) → [`00bbbc30`](#insn-00bbbc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbec`](#insn-00bbbbec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbf0`](#insn-00bbbbf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbf4`](#insn-00bbbbf4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbf8`](#insn-00bbbbf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbfc`](#insn-00bbbbfc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc10`](#insn-00bbbc10) → [`00c5d6a0`](../00c5d/00c5d6a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc18`](#insn-00bbbc18) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc1c`](#insn-00bbbc1c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc20`](#insn-00bbbc20) → [`00bbbbbc`](#insn-00bbbbbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc24`](#insn-00bbbc24) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc28`](#insn-00bbbc28) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc2c`](#insn-00bbbc2c) → [`00bbbbbc`](#insn-00bbbbbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc30`](#insn-00bbbc30) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbba10`](#insn-00bbba10)

~~~json
{
  "source": "00bbba10",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbba14`](#insn-00bbba14)

~~~json
{
  "source": "00bbba14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbba18`](#insn-00bbba18)

~~~json
{
  "source": "00bbba18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbba1c`](#insn-00bbba1c)

~~~json
{
  "source": "00bbba1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbba20`](#insn-00bbba20)

~~~json
{
  "source": "00bbba20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbba34`](#insn-00bbba34)

~~~json
{
  "source": "00bbba34",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbba3c`](#insn-00bbba3c)

~~~json
{
  "source": "00bbba3c",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbba40`](#insn-00bbba40)

~~~json
{
  "source": "00bbba40",
  "target": "00bbbaa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbba48`](#insn-00bbba48)

~~~json
{
  "source": "00bbba48",
  "target": "01126470",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126470",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbba54`](#insn-00bbba54)

~~~json
{
  "source": "00bbba54",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbba58`](#insn-00bbba58)

~~~json
{
  "source": "00bbba58",
  "target": "00c5d340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbba70`](#insn-00bbba70)

~~~json
{
  "source": "00bbba70",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbba7c`](#insn-00bbba7c)

~~~json
{
  "source": "00bbba7c",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbba84`](#insn-00bbba84)

~~~json
{
  "source": "00bbba84",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbba8c`](#insn-00bbba8c)

~~~json
{
  "source": "00bbba8c",
  "target": "01126508",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126508",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbba94`](#insn-00bbba94)

~~~json
{
  "source": "00bbba94",
  "target": "00bbbae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbaa0`](#insn-00bbbaa0)

~~~json
{
  "source": "00bbbaa0",
  "target": "00bbbcdc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbaa4`](#insn-00bbbaa4)

~~~json
{
  "source": "00bbbaa4",
  "target": "00bbbbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbaac`](#insn-00bbbaac)

~~~json
{
  "source": "00bbbaac",
  "target": "002a28c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a28c8",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a28c8",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbab0`](#insn-00bbbab0)

~~~json
{
  "source": "00bbbab0",
  "target": "00c5ad70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbab8`](#insn-00bbbab8)

~~~json
{
  "source": "00bbbab8",
  "target": "002b071b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b071b",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b071b",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbabc`](#insn-00bbbabc)

~~~json
{
  "source": "00bbbabc",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbac8`](#insn-00bbbac8)

~~~json
{
  "source": "00bbbac8",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbadc`](#insn-00bbbadc)

~~~json
{
  "source": "00bbbadc",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbae0`](#insn-00bbbae0)

~~~json
{
  "source": "00bbbae0",
  "target": "00bbbbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbae8`](#insn-00bbbae8)

~~~json
{
  "source": "00bbbae8",
  "target": "01126500",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126500",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbaf0`](#insn-00bbbaf0)

~~~json
{
  "source": "00bbbaf0",
  "target": "00bbbb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbafc`](#insn-00bbbafc)

~~~json
{
  "source": "00bbbafc",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb04`](#insn-00bbbb04)

~~~json
{
  "source": "00bbbb04",
  "target": "0030e80b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e80b",
  "offset": 0,
  "size": 83,
  "datatype": "string",
  "bytes": "43616e6e6f742075706461746520737562736372697074696f6e207768656e20",
  "capture_start": "0030e80b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbbb18`](#insn-00bbbb18)

~~~json
{
  "source": "00bbbb18",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb20`](#insn-00bbbb20)

~~~json
{
  "source": "00bbbb20",
  "target": "00bbbbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb28`](#insn-00bbbb28)

~~~json
{
  "source": "00bbbb28",
  "target": "01126480",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126480",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbb2c`](#insn-00bbbb2c)

~~~json
{
  "source": "00bbbb2c",
  "target": "00bbbb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb3c`](#insn-00bbbb3c)

~~~json
{
  "source": "00bbbb3c",
  "target": "00c5b690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb4c`](#insn-00bbbb4c)

~~~json
{
  "source": "00bbbb4c",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb58`](#insn-00bbbb58)

~~~json
{
  "source": "00bbbb58",
  "target": "00bbbc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb5c`](#insn-00bbbb5c)

~~~json
{
  "source": "00bbbb5c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb60`](#insn-00bbbb60)

~~~json
{
  "source": "00bbbb60",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb74`](#insn-00bbbb74)

~~~json
{
  "source": "00bbbb74",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb78`](#insn-00bbbb78)

~~~json
{
  "source": "00bbbb78",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb7c`](#insn-00bbbb7c)

~~~json
{
  "source": "00bbbb7c",
  "target": "00c5bd30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb88`](#insn-00bbbb88)

~~~json
{
  "source": "00bbbb88",
  "target": "00bbbc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb94`](#insn-00bbbb94)

~~~json
{
  "source": "00bbbb94",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb9c`](#insn-00bbbb9c)

~~~json
{
  "source": "00bbbb9c",
  "target": "0030e85e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e85e",
  "offset": 0,
  "size": 47,
  "datatype": "string",
  "bytes": "43616e6e6f742075706461746520737562736372697074696f6e20666f722075",
  "capture_start": "0030e85e",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbbbb0`](#insn-00bbbbb0)

~~~json
{
  "source": "00bbbbb0",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbb8`](#insn-00bbbbb8)

~~~json
{
  "source": "00bbbbb8",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbc8`](#insn-00bbbbc8)

~~~json
{
  "source": "00bbbbc8",
  "target": "00c5aea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbd0`](#insn-00bbbbd0)

~~~json
{
  "source": "00bbbbd0",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbd8`](#insn-00bbbbd8)

~~~json
{
  "source": "00bbbbd8",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbe0`](#insn-00bbbbe0)

~~~json
{
  "source": "00bbbbe0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbe8`](#insn-00bbbbe8)

~~~json
{
  "source": "00bbbbe8",
  "target": "00bbbc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbec`](#insn-00bbbbec)

~~~json
{
  "source": "00bbbbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbf0`](#insn-00bbbbf0)

~~~json
{
  "source": "00bbbbf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbf4`](#insn-00bbbbf4)

~~~json
{
  "source": "00bbbbf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbf8`](#insn-00bbbbf8)

~~~json
{
  "source": "00bbbbf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbfc`](#insn-00bbbbfc)

~~~json
{
  "source": "00bbbbfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc10`](#insn-00bbbc10)

~~~json
{
  "source": "00bbbc10",
  "target": "00c5d6a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc18`](#insn-00bbbc18)

~~~json
{
  "source": "00bbbc18",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc1c`](#insn-00bbbc1c)

~~~json
{
  "source": "00bbbc1c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc20`](#insn-00bbbc20)

~~~json
{
  "source": "00bbbc20",
  "target": "00bbbbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc24`](#insn-00bbbc24)

~~~json
{
  "source": "00bbbc24",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc28`](#insn-00bbbc28)

~~~json
{
  "source": "00bbbc28",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc2c`](#insn-00bbbc2c)

~~~json
{
  "source": "00bbbc2c",
  "target": "00bbbbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc30`](#insn-00bbbc30)

~~~json
{
  "source": "00bbbc30",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
