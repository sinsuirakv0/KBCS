# 00bbdea4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbceb0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-2c47f789ce52762215fe761cede82ed5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbdea4",
  "name": "_ZN8firebase9messaging11DeleteTokenEv",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "668fdc6d5984dd876608a780fcb1b37d01f6718362593674e0e7e7a66e2b617e",
  "source_text_sha256": "668fdc6d5984dd876608a780fcb1b37d01f6718362593674e0e7e7a66e2b617e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbdea4",
        "00bbe077"
      ]
    ],
    "bytes_sha256": "431893d0948329b9fe4b7a17588fd976aa5c63ecbf86f5cc6b3e7d121b5ad2e1",
    "instruction_count": 117,
    "instruction_bytes": 468,
    "body_bytes": 468,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bc80](../00c5b/00c5bc80.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5be40](../00c5b/00c5be40.md)
- [00c5be70](../00c5b/00c5be70.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bee0](../00c5b/00c5bee0.md)
- [00c5bfe0](../00c5b/00c5bfe0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c010](../00c5c/00c5c010.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5e310](../00c5e/00c5e310.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3539 bytes

~~~c

void _ZN8firebase9messaging11DeleteTokenEv(long param_1)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long *plVar6;
  undefined8 uVar7;
  undefined1 auStack_88 [16];
  byte local_78 [8];
  ulong local_70;
  void *local_68;
  undefined8 local_60 [2];
  undefined1 auStack_50 [8];
  long local_48;
  
                    /* catch() { ... } // from try @ 00bbdbec with catch @ 00bbdea4 */
  uVar4 = DAT_01127430;
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00bbd974 with catch @ 00bbdec0 */
  local_48 = *(long *)(lVar3 + 0x28);
                    /* catch() { ... } // from try @ 00bbdd40 with catch @ 00bbded0 */
                    /* catch() { ... } // from try @ 00bbde40 with catch @ 00bbded4 */
  if (DAT_01127420 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
                    /* catch() { ... } // from try @ 00bbde28 with catch @ 00bbded8 */
                    /* catch() { ... } // from try @ 00bbdc34 with catch @ 00bbdedc */
                    /* catch() { ... } // from try @ 00bbde0c with catch @ 00bbdee0
                       catch() { ... } // from try @ 00bbde5c with catch @ 00bbdee0 */
    _ZN8firebase5Mutex7AcquireEv(DAT_01127430);
    uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(local_78,uVar5,4,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(local_60,local_78);
    _ZN8firebase12FutureHandleD2Ev(local_78);
    plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01127420);
    uVar7 = FUN_00497b94(plVar6,DAT_01127458,DAT_011273b8);
    _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv(local_78,plVar6);
    uVar1 = (ulong)(local_78[0] >> 1);
    if ((local_78[0] & 1) != 0) {
      uVar1 = local_70;
    }
    if (uVar1 == 0) {
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar6,uVar7,FUN_00bbd338,local_60[0],"Messaging");
    }
    else {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,local_60);
      pvVar2 = (void *)((ulong)local_78 | 1);
      if ((local_78[0] & 1) != 0) {
        pvVar2 = local_68;
      }
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_88,0xffffffff,pvVar2,auStack_50);
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
    }
    (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,uVar5,local_60);
    if ((local_78[0] & 1) != 0) {
      _ZdlPv(local_68);
    }
    _ZN8firebase12FutureHandleD2Ev(local_60);
    _ZN8firebase5Mutex7ReleaseEv(uVar4);
  }
  if (*(long *)(lVar3 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bbe074 to 00cbe29b has its CatchHandler @ 00bbe074
                       catch() { ... } // from try @ 00bbe074 with catch @ 00bbe074
                       catch() { ... } // from try @ 00bbe2c0 with catch @ 00bbe074 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbdea4"></a> `00bbdea4` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbdea8"></a> `00bbdea8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbdeac"></a> `00bbdeac` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbdeb0"></a> `00bbdeb0` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbdeb4"></a> `00bbdeb4` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbdeb8"></a> `00bbdeb8` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbdebc"></a> `00bbdebc` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbdec0"></a> `00bbdec0` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbdec4"></a> `00bbdec4` | `56 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbdec8"></a> `00bbdec8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdecc"></a> `00bbdecc` | `a9 83 1c f8` | stur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbded0"></a> `00bbded0` | `c9 12 42 f9` | ldr x9,[x22, #0x420] | `FALL_THROUGH`
<a id="insn-00bbded4"></a> `00bbded4` | `89 06 00 b4` | cbz x9,0x00bbdfa4 | `CONDITIONAL_JUMP`
<a id="insn-00bbded8"></a> `00bbded8` | `48 2b 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbdedc"></a> `00bbdedc` | `13 19 42 f9` | ldr x19,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bbdee0"></a> `00bbdee0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbdee4"></a> `00bbdee4` | `ef 76 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdee8"></a> `00bbdee8` | `0a 81 02 94` | bl 0x00c5e310 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdeec"></a> `00bbdeec` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbdef0"></a> `00bbdef0` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdef4"></a> `00bbdef4` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdef8"></a> `00bbdef8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbdefc"></a> `00bbdefc` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbdf00"></a> `00bbdf00` | `f8 77 02 94` | bl 0x00c5bee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf04"></a> `00bbdf04` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbdf08"></a> `00bbdf08` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdf0c"></a> `00bbdf0c` | `e5 77 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf10"></a> `00bbdf10` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdf14"></a> `00bbdf14` | `07 77 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf18"></a> `00bbdf18` | `c0 12 42 f9` | ldr x0,[x22, #0x420] | `FALL_THROUGH`
<a id="insn-00bbdf1c"></a> `00bbdf1c` | `81 78 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf20"></a> `00bbdf20` | `48 2b 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbdf24"></a> `00bbdf24` | `49 2b 00 d0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbdf28"></a> `00bbdf28` | `01 2d 42 f9` | ldr x1,[x8, #0x458] | `FALL_THROUGH`
<a id="insn-00bbdf2c"></a> `00bbdf2c` | `22 dd 41 f9` | ldr x2,[x9, #0x3b8] | `FALL_THROUGH`
<a id="insn-00bbdf30"></a> `00bbdf30` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbdf34"></a> `00bbdf34` | `18 67 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf38"></a> `00bbdf38` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbdf3c"></a> `00bbdf3c` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdf40"></a> `00bbdf40` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdf44"></a> `00bbdf44` | `33 78 02 94` | bl 0x00c5c010 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf48"></a> `00bbdf48` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbdf4c"></a> `00bbdf4c` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdf50"></a> `00bbdf50` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf54"></a> `00bbdf54` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf58"></a> `00bbdf58` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdf5c"></a> `00bbdf5c` | `28 04 00 b4` | cbz x8,0x00bbdfe0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf60"></a> `00bbdf60` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbdf64"></a> `00bbdf64` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbdf68"></a> `00bbdf68` | `ce 77 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf6c"></a> `00bbdf6c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbdf70"></a> `00bbdf70` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbdf74"></a> `00bbdf74` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdf78"></a> `00bbdf78` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf7c"></a> `00bbdf7c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf80"></a> `00bbdf80` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdf84"></a> `00bbdf84` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbdf88"></a> `00bbdf88` | `e4 03 01 91` | add x4,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbdf8c"></a> `00bbdf8c` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbdf90"></a> `00bbdf90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbdf94"></a> `00bbdf94` | `ab 77 02 94` | bl 0x00c5be40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf98"></a> `00bbdf98` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbdf9c"></a> `00bbdf9c` | `e5 76 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfa0"></a> `00bbdfa0` | `18 00 00 14` | b 0x00bbe000 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdfa4"></a> `00bbdfa4` | `20 b7 ff b0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbdfa8"></a> `00bbdfa8` | `00 4c 26 91` | add x0,x0,#0x993 | `FALL_THROUGH`
<a id="insn-00bbdfac"></a> `00bbdfac` | `65 77 02 94` | bl 0x00c5bd40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfb0"></a> `00bbdfb0` | `80 b7 ff f0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbdfb4"></a> `00bbdfb4` | `00 c8 1f 91` | add x0,x0,#0x7f2 | `FALL_THROUGH`
<a id="insn-00bbdfb8"></a> `00bbdfb8` | `3a 78 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfbc"></a> `00bbdfbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbdfc0"></a> `00bbdfc0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbdfc4"></a> `00bbdfc4` | `53 77 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfc8"></a> `00bbdfc8` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bbdfcc"></a> `00bbdfcc` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbdfd0"></a> `00bbdfd0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbdfd4"></a> `00bbdfd4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbdfd8"></a> `00bbdfd8` | `2a 77 02 94` | bl 0x00c5bc80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfdc"></a> `00bbdfdc` | `1c 00 00 14` | b 0x00bbe04c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdfe0"></a> `00bbdfe0` | `e3 1b 40 f9` | ldr x3,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdfe4"></a> `00bbdfe4` | `02 00 00 90` | adrp x2,0xbbd000 | `FALL_THROUGH`
<a id="insn-00bbdfe8"></a> `00bbdfe8` | `84 ba ff b0` | adrp x4,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbdfec"></a> `00bbdfec` | `42 e0 0c 91` | add x2,x2,#0x338 | `FALL_THROUGH`
<a id="insn-00bbdff0"></a> `00bbdff0` | `84 04 21 91` | add x4,x4,#0x841 | `FALL_THROUGH`
<a id="insn-00bbdff4"></a> `00bbdff4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdff8"></a> `00bbdff8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbdffc"></a> `00bbdffc` | `f9 77 02 94` | bl 0x00c5bfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe000"></a> `00bbe000` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe004"></a> `00bbe004` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbe008"></a> `00bbe008` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe00c"></a> `00bbe00c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbe010"></a> `00bbe010` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbe014"></a> `00bbe014` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe018"></a> `00bbe018` | `fa 77 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe01c"></a> `00bbe01c` | `e2 c3 00 91` | add x2,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe020"></a> `00bbe020` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe024"></a> `00bbe024` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe028"></a> `00bbe028` | `92 77 02 94` | bl 0x00c5be70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe02c"></a> `00bbe02c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbe030"></a> `00bbe030` | `68 00 00 36` | tbz w8,#0x0,0x00bbe03c | `CONDITIONAL_JUMP`
<a id="insn-00bbe034"></a> `00bbe034` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbe038"></a> `00bbe038` | `c6 6b 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe03c"></a> `00bbe03c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe040"></a> `00bbe040` | `bc 76 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe044"></a> `00bbe044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe048"></a> `00bbe048` | `9a 76 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe04c"></a> `00bbe04c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbe050"></a> `00bbe050` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbe054"></a> `00bbe054` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe058"></a> `00bbe058` | `e1 00 00 54` | b.ne 0x00bbe074 | `CONDITIONAL_JUMP`
<a id="insn-00bbe05c"></a> `00bbe05c` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbe060"></a> `00bbe060` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbe064"></a> `00bbe064` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbe068"></a> `00bbe068` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbe06c"></a> `00bbe06c` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbe070"></a> `00bbe070` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbe074"></a> `00bbe074` | `c3 6b 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbdea4`](#insn-00bbdea4) 範囲 `[['00bbdea4', '00bbdebf']]`
  - `FALL_THROUGH` [`00bbdebc`](#insn-00bbdebc) → [`00bbdec0`](#insn-00bbdec0)
- ブロック [`00bbdec0`](#insn-00bbdec0) 範囲 `[['00bbdec0', '00bbdecf']]`
  - `FALL_THROUGH` [`00bbdecc`](#insn-00bbdecc) → [`00bbded0`](#insn-00bbded0)
- ブロック [`00bbded0`](#insn-00bbded0) 範囲 `[['00bbded0', '00bbded3']]`
  - `FALL_THROUGH` [`00bbded0`](#insn-00bbded0) → [`00bbded4`](#insn-00bbded4)
- ブロック [`00bbded4`](#insn-00bbded4) 範囲 `[['00bbded4', '00bbded7']]`
  - `CONDITIONAL_JUMP` [`00bbded4`](#insn-00bbded4) → [`00bbdfa4`](#insn-00bbdfa4)
  - `FALL_THROUGH` [`00bbded4`](#insn-00bbded4) → [`00bbded8`](#insn-00bbded8)
- ブロック [`00bbded8`](#insn-00bbded8) 範囲 `[['00bbded8', '00bbdedb']]`
  - `FALL_THROUGH` [`00bbded8`](#insn-00bbded8) → [`00bbdedc`](#insn-00bbdedc)
- ブロック [`00bbdedc`](#insn-00bbdedc) 範囲 `[['00bbdedc', '00bbdedf']]`
  - `FALL_THROUGH` [`00bbdedc`](#insn-00bbdedc) → [`00bbdee0`](#insn-00bbdee0)
- ブロック [`00bbdee0`](#insn-00bbdee0) 範囲 `[['00bbdee0', '00bbdf5f']]`
  - `CONDITIONAL_JUMP` [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdfe0`](#insn-00bbdfe0)
  - `FALL_THROUGH` [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdf60`](#insn-00bbdf60)
- ブロック [`00bbdf60`](#insn-00bbdf60) 範囲 `[['00bbdf60', '00bbdfa3']]`
  - `UNCONDITIONAL_JUMP` [`00bbdfa0`](#insn-00bbdfa0) → [`00bbe000`](#insn-00bbe000)
- ブロック [`00bbdfa4`](#insn-00bbdfa4) 範囲 `[['00bbdfa4', '00bbdfdf']]`
  - `UNCONDITIONAL_JUMP` [`00bbdfdc`](#insn-00bbdfdc) → [`00bbe04c`](#insn-00bbe04c)
- ブロック [`00bbdfe0`](#insn-00bbdfe0) 範囲 `[['00bbdfe0', '00bbdfff']]`
  - `FALL_THROUGH` [`00bbdffc`](#insn-00bbdffc) → [`00bbe000`](#insn-00bbe000)
- ブロック [`00bbe000`](#insn-00bbe000) 範囲 `[['00bbe000', '00bbe033']]`
  - `CONDITIONAL_JUMP` [`00bbe030`](#insn-00bbe030) → [`00bbe03c`](#insn-00bbe03c)
  - `FALL_THROUGH` [`00bbe030`](#insn-00bbe030) → [`00bbe034`](#insn-00bbe034)
- ブロック [`00bbe034`](#insn-00bbe034) 範囲 `[['00bbe034', '00bbe03b']]`
  - `FALL_THROUGH` [`00bbe038`](#insn-00bbe038) → [`00bbe03c`](#insn-00bbe03c)
- ブロック [`00bbe03c`](#insn-00bbe03c) 範囲 `[['00bbe03c', '00bbe04b']]`
  - `FALL_THROUGH` [`00bbe048`](#insn-00bbe048) → [`00bbe04c`](#insn-00bbe04c)
- ブロック [`00bbe04c`](#insn-00bbe04c) 範囲 `[['00bbe04c', '00bbe05b']]`
  - `CONDITIONAL_JUMP` [`00bbe058`](#insn-00bbe058) → [`00bbe074`](#insn-00bbe074)
  - `FALL_THROUGH` [`00bbe058`](#insn-00bbe058) → [`00bbe05c`](#insn-00bbe05c)
- ブロック [`00bbe05c`](#insn-00bbe05c) 範囲 `[['00bbe05c', '00bbe073']]`
- ブロック [`00bbe074`](#insn-00bbe074) 範囲 `[['00bbe074', '00bbe077']]`

## 命令位置別の参照

- [`00bbdea8`](#insn-00bbdea8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdeac`](#insn-00bbdeac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdeb4`](#insn-00bbdeb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdecc`](#insn-00bbdecc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbded0`](#insn-00bbded0) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbded4`](#insn-00bbded4) → [`00bbdfa4`](#insn-00bbdfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdedc`](#insn-00bbdedc) → `01127430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbdee4`](#insn-00bbdee4) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdee8`](#insn-00bbdee8) → [`00c5e310`](../00c5e/00c5e310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e310` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf00`](#insn-00bbdf00) → [`00c5bee0`](../00c5b/00c5bee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bee0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf0c`](#insn-00bbdf0c) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf14`](#insn-00bbdf14) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf18`](#insn-00bbdf18) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbdf1c`](#insn-00bbdf1c) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf28`](#insn-00bbdf28) → `01127458`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbdf2c`](#insn-00bbdf2c) → `011273b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbdf34`](#insn-00bbdf34) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf44`](#insn-00bbdf44) → [`00c5c010`](../00c5c/00c5c010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c010` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf48`](#insn-00bbdf48) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf4c`](#insn-00bbdf4c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdfe0`](#insn-00bbdfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf68`](#insn-00bbdf68) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf6c`](#insn-00bbdf6c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf70`](#insn-00bbdf70) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf94`](#insn-00bbdf94) → [`00c5be40`](../00c5b/00c5be40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be40` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf9c`](#insn-00bbdf9c) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfa0`](#insn-00bbdfa0) → [`00bbe000`](#insn-00bbe000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfa8`](#insn-00bbdfa8) → `002a2993`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbdfac`](#insn-00bbdfac) → [`00c5bd40`](../00c5b/00c5bd40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd40` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfb4`](#insn-00bbdfb4) → `002b07f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbdfb8`](#insn-00bbdfb8) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfc4`](#insn-00bbdfc4) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfd8`](#insn-00bbdfd8) → [`00c5bc80`](../00c5b/00c5bc80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc80` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfdc`](#insn-00bbdfdc) → [`00bbe04c`](#insn-00bbe04c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfe0`](#insn-00bbdfe0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfec`](#insn-00bbdfec) → [`00bbd338`](00bbd338.md) · `PARAM` · `ANALYSIS` · 関数 `00bbd338` · 推定シンボル `None` · 推定型 `None`
- [`00bbdff0`](#insn-00bbdff0) → `0030e841`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbdffc`](#insn-00bbdffc) → [`00c5bfe0`](../00c5b/00c5bfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe018`](#insn-00bbe018) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bbe028`](#insn-00bbe028) → [`00c5be70`](../00c5b/00c5be70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be70` · 推定シンボル `None` · 推定型 `None`
- [`00bbe02c`](#insn-00bbe02c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe030`](#insn-00bbe030) → [`00bbe03c`](#insn-00bbe03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe034`](#insn-00bbe034) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe038`](#insn-00bbe038) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbe040`](#insn-00bbe040) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bbe048`](#insn-00bbe048) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe050`](#insn-00bbe050) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe058`](#insn-00bbe058) → [`00bbe074`](#insn-00bbe074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe05c`](#insn-00bbe05c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe060`](#insn-00bbe060) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe064`](#insn-00bbe064) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe068`](#insn-00bbe068) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe074`](#insn-00bbe074) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbdea8`](#insn-00bbdea8)

~~~json
{
  "source": "00bbdea8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeac`](#insn-00bbdeac)

~~~json
{
  "source": "00bbdeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb4`](#insn-00bbdeb4)

~~~json
{
  "source": "00bbdeb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdecc`](#insn-00bbdecc)

~~~json
{
  "source": "00bbdecc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbded0`](#insn-00bbded0)

~~~json
{
  "source": "00bbded0",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbded4`](#insn-00bbded4)

~~~json
{
  "source": "00bbded4",
  "target": "00bbdfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdedc`](#insn-00bbdedc)

~~~json
{
  "source": "00bbdedc",
  "target": "01127430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127430",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbdee4`](#insn-00bbdee4)

~~~json
{
  "source": "00bbdee4",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdee8`](#insn-00bbdee8)

~~~json
{
  "source": "00bbdee8",
  "target": "00c5e310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf00`](#insn-00bbdf00)

~~~json
{
  "source": "00bbdf00",
  "target": "00c5bee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf0c`](#insn-00bbdf0c)

~~~json
{
  "source": "00bbdf0c",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf14`](#insn-00bbdf14)

~~~json
{
  "source": "00bbdf14",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf18`](#insn-00bbdf18)

~~~json
{
  "source": "00bbdf18",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbdf1c`](#insn-00bbdf1c)

~~~json
{
  "source": "00bbdf1c",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf28`](#insn-00bbdf28)

~~~json
{
  "source": "00bbdf28",
  "target": "01127458",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127458",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbdf2c`](#insn-00bbdf2c)

~~~json
{
  "source": "00bbdf2c",
  "target": "011273b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbdf34`](#insn-00bbdf34)

~~~json
{
  "source": "00bbdf34",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf44`](#insn-00bbdf44)

~~~json
{
  "source": "00bbdf44",
  "target": "00c5c010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf48`](#insn-00bbdf48)

~~~json
{
  "source": "00bbdf48",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf4c`](#insn-00bbdf4c)

~~~json
{
  "source": "00bbdf4c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf5c`](#insn-00bbdf5c)

~~~json
{
  "source": "00bbdf5c",
  "target": "00bbdfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf68`](#insn-00bbdf68)

~~~json
{
  "source": "00bbdf68",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf6c`](#insn-00bbdf6c)

~~~json
{
  "source": "00bbdf6c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf70`](#insn-00bbdf70)

~~~json
{
  "source": "00bbdf70",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf94`](#insn-00bbdf94)

~~~json
{
  "source": "00bbdf94",
  "target": "00c5be40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf9c`](#insn-00bbdf9c)

~~~json
{
  "source": "00bbdf9c",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfa0`](#insn-00bbdfa0)

~~~json
{
  "source": "00bbdfa0",
  "target": "00bbe000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfa8`](#insn-00bbdfa8)

~~~json
{
  "source": "00bbdfa8",
  "target": "002a2993",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2993",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2993",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdfac`](#insn-00bbdfac)

~~~json
{
  "source": "00bbdfac",
  "target": "00c5bd40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfb4`](#insn-00bbdfb4)

~~~json
{
  "source": "00bbdfb4",
  "target": "002b07f2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b07f2",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b07f2",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdfb8`](#insn-00bbdfb8)

~~~json
{
  "source": "00bbdfb8",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfc4`](#insn-00bbdfc4)

~~~json
{
  "source": "00bbdfc4",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfd8`](#insn-00bbdfd8)

~~~json
{
  "source": "00bbdfd8",
  "target": "00c5bc80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfdc`](#insn-00bbdfdc)

~~~json
{
  "source": "00bbdfdc",
  "target": "00bbe04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfe0`](#insn-00bbdfe0)

~~~json
{
  "source": "00bbdfe0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfec`](#insn-00bbdfec)

~~~json
{
  "source": "00bbdfec",
  "target": "00bbd338",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdff0`](#insn-00bbdff0)

~~~json
{
  "source": "00bbdff0",
  "target": "0030e841",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e841",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4d6573736167696e6700",
  "capture_start": "0030e841",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdffc`](#insn-00bbdffc)

~~~json
{
  "source": "00bbdffc",
  "target": "00c5bfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe018`](#insn-00bbe018)

~~~json
{
  "source": "00bbe018",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe028`](#insn-00bbe028)

~~~json
{
  "source": "00bbe028",
  "target": "00c5be70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe02c`](#insn-00bbe02c)

~~~json
{
  "source": "00bbe02c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe030`](#insn-00bbe030)

~~~json
{
  "source": "00bbe030",
  "target": "00bbe03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe034`](#insn-00bbe034)

~~~json
{
  "source": "00bbe034",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe038`](#insn-00bbe038)

~~~json
{
  "source": "00bbe038",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe040`](#insn-00bbe040)

~~~json
{
  "source": "00bbe040",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe048`](#insn-00bbe048)

~~~json
{
  "source": "00bbe048",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe050`](#insn-00bbe050)

~~~json
{
  "source": "00bbe050",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe058`](#insn-00bbe058)

~~~json
{
  "source": "00bbe058",
  "target": "00bbe074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe05c`](#insn-00bbe05c)

~~~json
{
  "source": "00bbe05c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe060`](#insn-00bbe060)

~~~json
{
  "source": "00bbe060",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe064`](#insn-00bbe064)

~~~json
{
  "source": "00bbe064",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe068`](#insn-00bbe068)

~~~json
{
  "source": "00bbe068",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe074`](#insn-00bbe074)

~~~json
{
  "source": "00bbe074",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
