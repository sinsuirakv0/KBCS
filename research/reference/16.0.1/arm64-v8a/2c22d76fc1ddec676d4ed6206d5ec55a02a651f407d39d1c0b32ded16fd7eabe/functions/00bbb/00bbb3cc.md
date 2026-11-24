# 00bbb3cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbafa4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbafa4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-f23c2d3e91b7faf7af3b667ae1d1ffec)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbb468`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-ce79b67b67826ffc0085b9f688d7bf2b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb3cc",
  "name": "_ZN8firebase9messaging9SubscribeEPKc",
  "size": 552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d8dfdd6345f581d08305a25a4e5eb5795d87f2b6c7725860c0554c94a7d4587",
  "source_text_sha256": "4d8dfdd6345f581d08305a25a4e5eb5795d87f2b6c7725860c0554c94a7d4587",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb3cc",
        "00bbb5f3"
      ]
    ],
    "bytes_sha256": "70bd7a654c6194bdce35a7fed796963b04dc08f554ffbca2f880819f5f0a2198",
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

- [00bbb69c](../00bbb/00bbb69c.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5ada0](../00c5a/00c5ada0.md)
- [00c5add0](../00c5a/00c5add0.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5ae40](../00c5a/00c5ae40.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b5c0](../00c5b/00c5b5c0.md)
- [00c5bc60](../00c5b/00c5bc60.md)
- [00c5d270](../00c5d/00c5d270.md)
- [00c5d5d0](../00c5d/00c5d5d0.md)

## 関連文字列（未確認候補）

~~~text
"Cannot update subscription for unknown reason."
"Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3727 bytes

~~~c

void _ZN8firebase9messaging9SubscribeEPKc(long param_1,undefined8 param_2)

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
  
  uVar3 = DAT_01126370;
  puVar6 = auStack_b0;
                    /* try { // try from 00bbb3e8 to 00cbb59b has its CatchHandler @ 00bbb20c */
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  if (DAT_01126360 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
    goto LAB_00bbb59c;
  }
  _ZN8firebase5Mutex7AcquireEv(DAT_01126370);
  uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(&local_a0,uVar5,1,0,0);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,&local_a0);
  _ZN8firebase12FutureHandleD2Ev(&local_a0);
  lVar4 = DAT_01126378;
  if (DAT_01126408 == '\x01') {
    FUN_00bbb69c(param_2,auStack_68);
  }
  else {
    if (DAT_01126400 == 2) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
                    /* catch() { ... } // from try @ 00bbb360 with catch @ 00bbb4cc */
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_78,3,
                 "Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
                 ,&local_a0);
      puVar6 = auStack_78;
    }
    else {
      if (DAT_01126378 != 0) {
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
          _ZN8firebase12FutureHandleC1EOS0_(puVar1 + 3,auStack_88);
          *(ulong **)(lVar4 + 8) = puVar1 + 5;
        }
        else {
          _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_
                    (lVar4,&local_a0);
        }
        _ZN8firebase12FutureHandleD2Ev(auStack_88);
        if ((local_a0 & 1) != 0) {
          _ZdlPv(local_90);
        }
        goto LAB_00bbb57c;
      }
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_b0,auStack_68);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_b0,4,"Cannot update subscription for unknown reason.",&local_a0);
    }
    _ZN8firebase12FutureHandleD2Ev(puVar6);
  }
LAB_00bbb57c:
  _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,uVar5,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
LAB_00bbb59c:
                    /* catch() { ... } // from try @ 00bbb778 with catch @ 00bbb59c */
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
<a id="insn-00bbb3cc"></a> `00bbb3cc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbb3d0"></a> `00bbb3d0` | `f9 33 00 f9` | str x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb3d4"></a> `00bbb3d4` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbb3d8"></a> `00bbb3d8` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbb3dc"></a> `00bbb3dc` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbb3e0"></a> `00bbb3e0` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbb3e4"></a> `00bbb3e4` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbb3e8"></a> `00bbb3e8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbb3ec"></a> `00bbb3ec` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb3f0"></a> `00bbb3f0` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bbb3f4"></a> `00bbb3f4` | `a9 83 1b f8` | stur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bbb3f8"></a> `00bbb3f8` | `49 2b 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb3fc"></a> `00bbb3fc` | `29 b1 41 f9` | ldr x9,[x9, #0x360] | `FALL_THROUGH`
<a id="insn-00bbb400"></a> `00bbb400` | `49 03 00 b4` | cbz x9,0x00bbb468 | `CONDITIONAL_JUMP`
<a id="insn-00bbb404"></a> `00bbb404` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb408"></a> `00bbb408` | `13 b9 41 f9` | ldr x19,[x8, #0x370] | `FALL_THROUGH`
<a id="insn-00bbb40c"></a> `00bbb40c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbb410"></a> `00bbb410` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb414"></a> `00bbb414` | `7b 7d 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb418"></a> `00bbb418` | `96 87 02 94` | bl 0x00c5d270 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb41c"></a> `00bbb41c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbb420"></a> `00bbb420` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb424"></a> `00bbb424` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb428"></a> `00bbb428` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbb42c"></a> `00bbb42c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbb430"></a> `00bbb430` | `84 7e 02 94` | bl 0x00c5ae40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb434"></a> `00bbb434` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb438"></a> `00bbb438` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb43c"></a> `00bbb43c` | `71 7e 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb440"></a> `00bbb440` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb444"></a> `00bbb444` | `93 7d 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb448"></a> `00bbb448` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb44c"></a> `00bbb44c` | `08 21 50 39` | ldrb w8,[x8, #0x408] | `FALL_THROUGH`
<a id="insn-00bbb450"></a> `00bbb450` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb454"></a> `00bbb454` | `81 02 00 54` | b.ne 0x00bbb4a4 | `CONDITIONAL_JUMP`
<a id="insn-00bbb458"></a> `00bbb458` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb45c"></a> `00bbb45c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbb460"></a> `00bbb460` | `8f 00 00 94` | bl 0x00bbb69c | `UNCONDITIONAL_CALL`
<a id="insn-00bbb464"></a> `00bbb464` | `46 00 00 14` | b 0x00bbb57c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb468"></a> `00bbb468` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbb46c"></a> `00bbb46c` | `00 54 24 91` | add x0,x0,#0x915 | `FALL_THROUGH`
<a id="insn-00bbb470"></a> `00bbb470` | `0c 7e 02 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb474"></a> `00bbb474` | `a0 b7 ff b0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbb478"></a> `00bbb478` | `00 dc 1d 91` | add x0,x0,#0x777 | `FALL_THROUGH`
<a id="insn-00bbb47c"></a> `00bbb47c` | `e1 7e 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb480"></a> `00bbb480` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb484"></a> `00bbb484` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbb488"></a> `00bbb488` | `fa 7d 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb48c"></a> `00bbb48c` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bbb490"></a> `00bbb490` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb494"></a> `00bbb494` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbb498"></a> `00bbb498` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbb49c"></a> `00bbb49c` | `d1 7d 02 94` | bl 0x00c5abe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb4a0"></a> `00bbb4a0` | `3f 00 00 14` | b 0x00bbb59c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb4a4"></a> `00bbb4a4` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb4a8"></a> `00bbb4a8` | `08 01 44 b9` | ldr w8,[x8, #0x400] | `FALL_THROUGH`
<a id="insn-00bbb4ac"></a> `00bbb4ac` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb4b0"></a> `00bbb4b0` | `a1 01 00 54` | b.ne 0x00bbb4e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbb4b4"></a> `00bbb4b4` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbb4b8"></a> `00bbb4b8` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb4bc"></a> `00bbb4bc` | `51 7e 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb4c0"></a> `00bbb4c0` | `83 ba ff f0` | adrp x3,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb4c4"></a> `00bbb4c4` | `63 2c 1f 91` | add x3,x3,#0x7cb | `FALL_THROUGH`
<a id="insn-00bbb4c8"></a> `00bbb4c8` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbb4cc"></a> `00bbb4cc` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb4d0"></a> `00bbb4d0` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-00bbb4d4"></a> `00bbb4d4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbb4d8"></a> `00bbb4d8` | `32 7e 02 94` | bl 0x00c5ada0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb4dc"></a> `00bbb4dc` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbb4e0"></a> `00bbb4e0` | `26 00 00 14` | b 0x00bbb578 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb4e4"></a> `00bbb4e4` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb4e8"></a> `00bbb4e8` | `17 bd 41 f9` | ldr x23,[x8, #0x378] | `FALL_THROUGH`
<a id="insn-00bbb4ec"></a> `00bbb4ec` | `17 03 00 b4` | cbz x23,0x00bbb54c | `CONDITIONAL_JUMP`
<a id="insn-00bbb4f0"></a> `00bbb4f0` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb4f4"></a> `00bbb4f4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb4f8"></a> `00bbb4f8` | `f9 43 00 91` | add x25,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb4fc"></a> `00bbb4fc` | `31 80 02 94` | bl 0x00c5b5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb500"></a> `00bbb500` | `36 63 00 91` | add x22,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb504"></a> `00bbb504` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb508"></a> `00bbb508` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbb50c"></a> `00bbb50c` | `3d 7e 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb510"></a> `00bbb510` | `f9 a2 40 a9` | ldp x25,x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb514"></a> `00bbb514` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bbb518"></a> `00bbb518` | `82 05 00 54` | b.cs 0x00bbb5c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb51c"></a> `00bbb51c` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb520"></a> `00bbb520` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb524"></a> `00bbb524` | `20 63 00 91` | add x0,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb528"></a> `00bbb528` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb52c"></a> `00bbb52c` | `28 0b 00 f9` | str x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb530"></a> `00bbb530` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00bbb534"></a> `00bbb534` | `ff ff 01 a9` | stp xzr,xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbb538"></a> `00bbb538` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb53c"></a> `00bbb53c` | `c9 81 02 94` | bl 0x00c5bc60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb540"></a> `00bbb540` | `28 a3 00 91` | add x8,x25,#0x28 | `FALL_THROUGH`
<a id="insn-00bbb544"></a> `00bbb544` | `e8 06 00 f9` | str x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb548"></a> `00bbb548` | `23 00 00 14` | b 0x00bbb5d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb54c"></a> `00bbb54c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbb550"></a> `00bbb550` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb554"></a> `00bbb554` | `2b 7e 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb558"></a> `00bbb558` | `83 ba ff f0` | adrp x3,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb55c"></a> `00bbb55c` | `63 78 20 91` | add x3,x3,#0x81e | `FALL_THROUGH`
<a id="insn-00bbb560"></a> `00bbb560` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbb564"></a> `00bbb564` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb568"></a> `00bbb568` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00bbb56c"></a> `00bbb56c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbb570"></a> `00bbb570` | `0c 7e 02 94` | bl 0x00c5ada0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb574"></a> `00bbb574` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbb578"></a> `00bbb578` | `46 7d 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb57c"></a> `00bbb57c` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb580"></a> `00bbb580` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb584"></a> `00bbb584` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbb588"></a> `00bbb588` | `12 7e 02 94` | bl 0x00c5add0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb58c"></a> `00bbb58c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb590"></a> `00bbb590` | `40 7d 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb594"></a> `00bbb594` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb598"></a> `00bbb598` | `1e 7d 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb59c"></a> `00bbb59c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb5a0"></a> `00bbb5a0` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bbb5a4"></a> `00bbb5a4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbb5a8"></a> `00bbb5a8` | `41 02 00 54` | b.ne 0x00bbb5f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbb5ac"></a> `00bbb5ac` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbb5b0"></a> `00bbb5b0` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbb5b4"></a> `00bbb5b4` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbb5b8"></a> `00bbb5b8` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbb5bc"></a> `00bbb5bc` | `f9 33 40 f9` | ldr x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb5c0"></a> `00bbb5c0` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbb5c4"></a> `00bbb5c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb5c8"></a> `00bbb5c8` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb5cc"></a> `00bbb5cc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbb5d0"></a> `00bbb5d0` | `00 88 02 94` | bl 0x00c5d5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb5d4"></a> `00bbb5d4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbb5d8"></a> `00bbb5d8` | `2e 7d 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb5dc"></a> `00bbb5dc` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb5e0"></a> `00bbb5e0` | `e8 fc 07 36` | tbz w8,#0x0,0x00bbb57c | `CONDITIONAL_JUMP`
<a id="insn-00bbb5e4"></a> `00bbb5e4` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb5e8"></a> `00bbb5e8` | `32 72 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb5ec"></a> `00bbb5ec` | `e4 ff ff 17` | b 0x00bbb57c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb5f0"></a> `00bbb5f0` | `3c 72 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb3cc`](#insn-00bbb3cc) 範囲 `[['00bbb3cc', '00bbb3e7']]`
  - `FALL_THROUGH` [`00bbb3e4`](#insn-00bbb3e4) → [`00bbb3e8`](#insn-00bbb3e8)
- ブロック [`00bbb3e8`](#insn-00bbb3e8) 範囲 `[['00bbb3e8', '00bbb403']]`
  - `CONDITIONAL_JUMP` [`00bbb400`](#insn-00bbb400) → [`00bbb468`](#insn-00bbb468)
  - `FALL_THROUGH` [`00bbb400`](#insn-00bbb400) → [`00bbb404`](#insn-00bbb404)
- ブロック [`00bbb404`](#insn-00bbb404) 範囲 `[['00bbb404', '00bbb457']]`
  - `CONDITIONAL_JUMP` [`00bbb454`](#insn-00bbb454) → [`00bbb4a4`](#insn-00bbb4a4)
  - `FALL_THROUGH` [`00bbb454`](#insn-00bbb454) → [`00bbb458`](#insn-00bbb458)
- ブロック [`00bbb458`](#insn-00bbb458) 範囲 `[['00bbb458', '00bbb467']]`
  - `UNCONDITIONAL_JUMP` [`00bbb464`](#insn-00bbb464) → [`00bbb57c`](#insn-00bbb57c)
- ブロック [`00bbb468`](#insn-00bbb468) 範囲 `[['00bbb468', '00bbb4a3']]`
  - `UNCONDITIONAL_JUMP` [`00bbb4a0`](#insn-00bbb4a0) → [`00bbb59c`](#insn-00bbb59c)
- ブロック [`00bbb4a4`](#insn-00bbb4a4) 範囲 `[['00bbb4a4', '00bbb4b3']]`
  - `CONDITIONAL_JUMP` [`00bbb4b0`](#insn-00bbb4b0) → [`00bbb4e4`](#insn-00bbb4e4)
  - `FALL_THROUGH` [`00bbb4b0`](#insn-00bbb4b0) → [`00bbb4b4`](#insn-00bbb4b4)
- ブロック [`00bbb4b4`](#insn-00bbb4b4) 範囲 `[['00bbb4b4', '00bbb4cb']]`
  - `FALL_THROUGH` [`00bbb4c8`](#insn-00bbb4c8) → [`00bbb4cc`](#insn-00bbb4cc)
- ブロック [`00bbb4cc`](#insn-00bbb4cc) 範囲 `[['00bbb4cc', '00bbb4e3']]`
  - `UNCONDITIONAL_JUMP` [`00bbb4e0`](#insn-00bbb4e0) → [`00bbb578`](#insn-00bbb578)
- ブロック [`00bbb4e4`](#insn-00bbb4e4) 範囲 `[['00bbb4e4', '00bbb4ef']]`
  - `CONDITIONAL_JUMP` [`00bbb4ec`](#insn-00bbb4ec) → [`00bbb54c`](#insn-00bbb54c)
  - `FALL_THROUGH` [`00bbb4ec`](#insn-00bbb4ec) → [`00bbb4f0`](#insn-00bbb4f0)
- ブロック [`00bbb4f0`](#insn-00bbb4f0) 範囲 `[['00bbb4f0', '00bbb51b']]`
  - `CONDITIONAL_JUMP` [`00bbb518`](#insn-00bbb518) → [`00bbb5c8`](#insn-00bbb5c8)
  - `FALL_THROUGH` [`00bbb518`](#insn-00bbb518) → [`00bbb51c`](#insn-00bbb51c)
- ブロック [`00bbb51c`](#insn-00bbb51c) 範囲 `[['00bbb51c', '00bbb54b']]`
  - `UNCONDITIONAL_JUMP` [`00bbb548`](#insn-00bbb548) → [`00bbb5d4`](#insn-00bbb5d4)
- ブロック [`00bbb54c`](#insn-00bbb54c) 範囲 `[['00bbb54c', '00bbb577']]`
  - `FALL_THROUGH` [`00bbb574`](#insn-00bbb574) → [`00bbb578`](#insn-00bbb578)
- ブロック [`00bbb578`](#insn-00bbb578) 範囲 `[['00bbb578', '00bbb57b']]`
  - `FALL_THROUGH` [`00bbb578`](#insn-00bbb578) → [`00bbb57c`](#insn-00bbb57c)
- ブロック [`00bbb57c`](#insn-00bbb57c) 範囲 `[['00bbb57c', '00bbb59b']]`
  - `FALL_THROUGH` [`00bbb598`](#insn-00bbb598) → [`00bbb59c`](#insn-00bbb59c)
- ブロック [`00bbb59c`](#insn-00bbb59c) 範囲 `[['00bbb59c', '00bbb5ab']]`
  - `CONDITIONAL_JUMP` [`00bbb5a8`](#insn-00bbb5a8) → [`00bbb5f0`](#insn-00bbb5f0)
  - `FALL_THROUGH` [`00bbb5a8`](#insn-00bbb5a8) → [`00bbb5ac`](#insn-00bbb5ac)
- ブロック [`00bbb5ac`](#insn-00bbb5ac) 範囲 `[['00bbb5ac', '00bbb5c7']]`
- ブロック [`00bbb5c8`](#insn-00bbb5c8) 範囲 `[['00bbb5c8', '00bbb5d3']]`
  - `FALL_THROUGH` [`00bbb5d0`](#insn-00bbb5d0) → [`00bbb5d4`](#insn-00bbb5d4)
- ブロック [`00bbb5d4`](#insn-00bbb5d4) 範囲 `[['00bbb5d4', '00bbb5e3']]`
  - `CONDITIONAL_JUMP` [`00bbb5e0`](#insn-00bbb5e0) → [`00bbb57c`](#insn-00bbb57c)
  - `FALL_THROUGH` [`00bbb5e0`](#insn-00bbb5e0) → [`00bbb5e4`](#insn-00bbb5e4)
- ブロック [`00bbb5e4`](#insn-00bbb5e4) 範囲 `[['00bbb5e4', '00bbb5ef']]`
  - `UNCONDITIONAL_JUMP` [`00bbb5ec`](#insn-00bbb5ec) → [`00bbb57c`](#insn-00bbb57c)
- ブロック [`00bbb5f0`](#insn-00bbb5f0) 範囲 `[['00bbb5f0', '00bbb5f3']]`

## 命令位置別の参照

- [`00bbb3d0`](#insn-00bbb3d0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3d4`](#insn-00bbb3d4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3d8`](#insn-00bbb3d8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3dc`](#insn-00bbb3dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3e0`](#insn-00bbb3e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3f4`](#insn-00bbb3f4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3fc`](#insn-00bbb3fc) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb400`](#insn-00bbb400) → [`00bbb468`](#insn-00bbb468) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb408`](#insn-00bbb408) → `01126370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb414`](#insn-00bbb414) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb418`](#insn-00bbb418) → [`00c5d270`](../00c5d/00c5d270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d270` · 推定シンボル `None` · 推定型 `None`
- [`00bbb430`](#insn-00bbb430) → [`00c5ae40`](../00c5a/00c5ae40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae40` · 推定シンボル `None` · 推定型 `None`
- [`00bbb43c`](#insn-00bbb43c) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb444`](#insn-00bbb444) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bbb44c`](#insn-00bbb44c) → `01126408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbb454`](#insn-00bbb454) → [`00bbb4a4`](#insn-00bbb4a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb460`](#insn-00bbb460) → [`00bbb69c`](00bbb69c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb69c` · 推定シンボル `None` · 推定型 `None`
- [`00bbb464`](#insn-00bbb464) → [`00bbb57c`](#insn-00bbb57c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb46c`](#insn-00bbb46c) → `002a2915`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb470`](#insn-00bbb470) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb478`](#insn-00bbb478) → `002b0777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb47c`](#insn-00bbb47c) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbb488`](#insn-00bbb488) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bbb49c`](#insn-00bbb49c) → [`00c5abe0`](../00c5a/00c5abe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4a0`](#insn-00bbb4a0) → [`00bbb59c`](#insn-00bbb59c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4a8`](#insn-00bbb4a8) → `01126400`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbb4b0`](#insn-00bbb4b0) → [`00bbb4e4`](#insn-00bbb4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4bc`](#insn-00bbb4bc) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4c4`](#insn-00bbb4c4) → `0030e7cb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb4d8`](#insn-00bbb4d8) → [`00c5ada0`](../00c5a/00c5ada0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ada0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4e0`](#insn-00bbb4e0) → [`00bbb578`](#insn-00bbb578) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4e8`](#insn-00bbb4e8) → `01126378`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb4ec`](#insn-00bbb4ec) → [`00bbb54c`](#insn-00bbb54c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4fc`](#insn-00bbb4fc) → [`00c5b5c0`](../00c5b/00c5b5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb50c`](#insn-00bbb50c) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb518`](#insn-00bbb518) → [`00bbb5c8`](#insn-00bbb5c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb51c`](#insn-00bbb51c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb520`](#insn-00bbb520) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb534`](#insn-00bbb534) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb538`](#insn-00bbb538) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb53c`](#insn-00bbb53c) → [`00c5bc60`](../00c5b/00c5bc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc60` · 推定シンボル `None` · 推定型 `None`
- [`00bbb548`](#insn-00bbb548) → [`00bbb5d4`](#insn-00bbb5d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb554`](#insn-00bbb554) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb55c`](#insn-00bbb55c) → `0030e81e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb570`](#insn-00bbb570) → [`00c5ada0`](../00c5a/00c5ada0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ada0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb578`](#insn-00bbb578) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bbb588`](#insn-00bbb588) → [`00c5add0`](../00c5a/00c5add0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5add0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb590`](#insn-00bbb590) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bbb598`](#insn-00bbb598) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5a0`](#insn-00bbb5a0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5a8`](#insn-00bbb5a8) → [`00bbb5f0`](#insn-00bbb5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5ac`](#insn-00bbb5ac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5b0`](#insn-00bbb5b0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5b4`](#insn-00bbb5b4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5b8`](#insn-00bbb5b8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5bc`](#insn-00bbb5bc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5d0`](#insn-00bbb5d0) → [`00c5d5d0`](../00c5d/00c5d5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5d8`](#insn-00bbb5d8) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5dc`](#insn-00bbb5dc) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5e0`](#insn-00bbb5e0) → [`00bbb57c`](#insn-00bbb57c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5e4`](#insn-00bbb5e4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5e8`](#insn-00bbb5e8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5ec`](#insn-00bbb5ec) → [`00bbb57c`](#insn-00bbb57c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5f0`](#insn-00bbb5f0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb3d0`](#insn-00bbb3d0)

~~~json
{
  "source": "00bbb3d0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3d4`](#insn-00bbb3d4)

~~~json
{
  "source": "00bbb3d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3d8`](#insn-00bbb3d8)

~~~json
{
  "source": "00bbb3d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3dc`](#insn-00bbb3dc)

~~~json
{
  "source": "00bbb3dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3e0`](#insn-00bbb3e0)

~~~json
{
  "source": "00bbb3e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3f4`](#insn-00bbb3f4)

~~~json
{
  "source": "00bbb3f4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3fc`](#insn-00bbb3fc)

~~~json
{
  "source": "00bbb3fc",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb400`](#insn-00bbb400)

~~~json
{
  "source": "00bbb400",
  "target": "00bbb468",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb408`](#insn-00bbb408)

~~~json
{
  "source": "00bbb408",
  "target": "01126370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126370",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb414`](#insn-00bbb414)

~~~json
{
  "source": "00bbb414",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb418`](#insn-00bbb418)

~~~json
{
  "source": "00bbb418",
  "target": "00c5d270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb430`](#insn-00bbb430)

~~~json
{
  "source": "00bbb430",
  "target": "00c5ae40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb43c`](#insn-00bbb43c)

~~~json
{
  "source": "00bbb43c",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb444`](#insn-00bbb444)

~~~json
{
  "source": "00bbb444",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb44c`](#insn-00bbb44c)

~~~json
{
  "source": "00bbb44c",
  "target": "01126408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126408",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb454`](#insn-00bbb454)

~~~json
{
  "source": "00bbb454",
  "target": "00bbb4a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb460`](#insn-00bbb460)

~~~json
{
  "source": "00bbb460",
  "target": "00bbb69c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb464`](#insn-00bbb464)

~~~json
{
  "source": "00bbb464",
  "target": "00bbb57c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb46c`](#insn-00bbb46c)

~~~json
{
  "source": "00bbb46c",
  "target": "002a2915",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2915",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2915",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb470`](#insn-00bbb470)

~~~json
{
  "source": "00bbb470",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb478`](#insn-00bbb478)

~~~json
{
  "source": "00bbb478",
  "target": "002b0777",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0777",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0777",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb47c`](#insn-00bbb47c)

~~~json
{
  "source": "00bbb47c",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb488`](#insn-00bbb488)

~~~json
{
  "source": "00bbb488",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb49c`](#insn-00bbb49c)

~~~json
{
  "source": "00bbb49c",
  "target": "00c5abe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb4a0`](#insn-00bbb4a0)

~~~json
{
  "source": "00bbb4a0",
  "target": "00bbb59c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4a8`](#insn-00bbb4a8)

~~~json
{
  "source": "00bbb4a8",
  "target": "01126400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126400",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb4b0`](#insn-00bbb4b0)

~~~json
{
  "source": "00bbb4b0",
  "target": "00bbb4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4bc`](#insn-00bbb4bc)

~~~json
{
  "source": "00bbb4bc",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb4c4`](#insn-00bbb4c4)

~~~json
{
  "source": "00bbb4c4",
  "target": "0030e7cb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e7cb",
  "offset": 0,
  "size": 83,
  "datatype": "string",
  "bytes": "43616e6e6f742075706461746520737562736372697074696f6e207768656e20",
  "capture_start": "0030e7cb",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbb4d8`](#insn-00bbb4d8)

~~~json
{
  "source": "00bbb4d8",
  "target": "00c5ada0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb4e0`](#insn-00bbb4e0)

~~~json
{
  "source": "00bbb4e0",
  "target": "00bbb578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4e8`](#insn-00bbb4e8)

~~~json
{
  "source": "00bbb4e8",
  "target": "01126378",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126378",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb4ec`](#insn-00bbb4ec)

~~~json
{
  "source": "00bbb4ec",
  "target": "00bbb54c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4fc`](#insn-00bbb4fc)

~~~json
{
  "source": "00bbb4fc",
  "target": "00c5b5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb50c`](#insn-00bbb50c)

~~~json
{
  "source": "00bbb50c",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb518`](#insn-00bbb518)

~~~json
{
  "source": "00bbb518",
  "target": "00bbb5c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb51c`](#insn-00bbb51c)

~~~json
{
  "source": "00bbb51c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb520`](#insn-00bbb520)

~~~json
{
  "source": "00bbb520",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb534`](#insn-00bbb534)

~~~json
{
  "source": "00bbb534",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb538`](#insn-00bbb538)

~~~json
{
  "source": "00bbb538",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb53c`](#insn-00bbb53c)

~~~json
{
  "source": "00bbb53c",
  "target": "00c5bc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb548`](#insn-00bbb548)

~~~json
{
  "source": "00bbb548",
  "target": "00bbb5d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb554`](#insn-00bbb554)

~~~json
{
  "source": "00bbb554",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb55c`](#insn-00bbb55c)

~~~json
{
  "source": "00bbb55c",
  "target": "0030e81e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e81e",
  "offset": 0,
  "size": 47,
  "datatype": "string",
  "bytes": "43616e6e6f742075706461746520737562736372697074696f6e20666f722075",
  "capture_start": "0030e81e",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbb570`](#insn-00bbb570)

~~~json
{
  "source": "00bbb570",
  "target": "00c5ada0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb578`](#insn-00bbb578)

~~~json
{
  "source": "00bbb578",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb588`](#insn-00bbb588)

~~~json
{
  "source": "00bbb588",
  "target": "00c5add0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb590`](#insn-00bbb590)

~~~json
{
  "source": "00bbb590",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb598`](#insn-00bbb598)

~~~json
{
  "source": "00bbb598",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb5a0`](#insn-00bbb5a0)

~~~json
{
  "source": "00bbb5a0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5a8`](#insn-00bbb5a8)

~~~json
{
  "source": "00bbb5a8",
  "target": "00bbb5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5ac`](#insn-00bbb5ac)

~~~json
{
  "source": "00bbb5ac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5b0`](#insn-00bbb5b0)

~~~json
{
  "source": "00bbb5b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5b4`](#insn-00bbb5b4)

~~~json
{
  "source": "00bbb5b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5b8`](#insn-00bbb5b8)

~~~json
{
  "source": "00bbb5b8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5bc`](#insn-00bbb5bc)

~~~json
{
  "source": "00bbb5bc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5d0`](#insn-00bbb5d0)

~~~json
{
  "source": "00bbb5d0",
  "target": "00c5d5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb5d8`](#insn-00bbb5d8)

~~~json
{
  "source": "00bbb5d8",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb5dc`](#insn-00bbb5dc)

~~~json
{
  "source": "00bbb5dc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5e0`](#insn-00bbb5e0)

~~~json
{
  "source": "00bbb5e0",
  "target": "00bbb57c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5e4`](#insn-00bbb5e4)

~~~json
{
  "source": "00bbb5e4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5e8`](#insn-00bbb5e8)

~~~json
{
  "source": "00bbb5e8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb5ec`](#insn-00bbb5ec)

~~~json
{
  "source": "00bbb5ec",
  "target": "00bbb57c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5f0`](#insn-00bbb5f0)

~~~json
{
  "source": "00bbb5f0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
