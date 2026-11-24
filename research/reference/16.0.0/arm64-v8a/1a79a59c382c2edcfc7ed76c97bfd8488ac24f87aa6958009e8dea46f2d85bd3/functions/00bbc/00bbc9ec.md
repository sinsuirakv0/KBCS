# 00bbc9ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4e484`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e484.md) · 移動量 `+0x6e568`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-bcb0926d11221c95abfc5d30e99029bf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbce14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-7d3498731dfb9418b5b5b43680899af9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbc9ec",
  "name": "_ZN8firebase9messaging11DeleteTokenEv",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0458a94bfc36673b64c0faeed5bb391da1431e8a1cf3a38ef6dba405cc3fdaad",
  "source_text_sha256": "0458a94bfc36673b64c0faeed5bb391da1431e8a1cf3a38ef6dba405cc3fdaad",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbc9ec",
        "00bbcbbf"
      ]
    ],
    "bytes_sha256": "5f450d59f476756bbb79e2a815fcee016e91834688b89d153279a1ad81f9a257",
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

- [004977f4](../00497/004977f4.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5a7e0](../00c5a/00c5a7e0.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5a9a0](../00c5a/00c5a9a0.md)
- [00c5a9d0](../00c5a/00c5a9d0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa40](../00c5a/00c5aa40.md)
- [00c5ab40](../00c5a/00c5ab40.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ab70](../00c5a/00c5ab70.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5ce70](../00c5c/00c5ce70.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2969 bytes

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
  
  uVar4 = DAT_01125f70;
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  if (DAT_01125f60 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    _ZN8firebase5Mutex7AcquireEv(DAT_01125f70);
    uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* try { // try from 00bbca3c to 00cbca7f has its CatchHandler @ 00bbc6dc */
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(local_78,uVar5,4,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(local_60,local_78);
    _ZN8firebase12FutureHandleD2Ev(local_78);
    plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01125f60);
    uVar7 = FUN_004977f4(plVar6,DAT_01125f98,DAT_01125ef8);
                    /* try { // try from 00bbca80 to 00cbca83 has its CatchHandler @ 00bbcc2c */
    _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv(local_78,plVar6);
    uVar1 = (ulong)(local_78[0] >> 1);
    if ((local_78[0] & 1) != 0) {
      uVar1 = local_70;
    }
    if (uVar1 == 0) {
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar6,uVar7,FUN_00bbbe80,local_60[0],"Messaging");
    }
    else {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,local_60);
      pvVar2 = (void *)((ulong)local_78 | 1);
      if ((local_78[0] & 1) != 0) {
        pvVar2 = local_68;
      }
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_88,0xffffffff,pvVar2,auStack_50);
                    /* try { // try from 00bbcae0 to 00cbcae7 has its CatchHandler @ 00bbcc70 */
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
                    /* try { // try from 00bbcbac to 00cbcbb3 has its CatchHandler @ 00bbcc80 */
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
<a id="insn-00bbc9ec"></a> `00bbc9ec` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbc9f0"></a> `00bbc9f0` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbc9f4"></a> `00bbc9f4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbc9f8"></a> `00bbc9f8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbc9fc"></a> `00bbc9fc` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbca00"></a> `00bbca00` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbca04"></a> `00bbca04` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbca08"></a> `00bbca08` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbca0c"></a> `00bbca0c` | `56 2b 00 b0` | adrp x22,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbca10"></a> `00bbca10` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bbca14"></a> `00bbca14` | `a9 83 1c f8` | stur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbca18"></a> `00bbca18` | `c9 b2 47 f9` | ldr x9,[x22, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbca1c"></a> `00bbca1c` | `89 06 00 b4` | cbz x9,0x00bbcaec | `CONDITIONAL_JUMP`
<a id="insn-00bbca20"></a> `00bbca20` | `48 2b 00 b0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbca24"></a> `00bbca24` | `13 b9 47 f9` | ldr x19,[x8, #0xf70] | `FALL_THROUGH`
<a id="insn-00bbca28"></a> `00bbca28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbca2c"></a> `00bbca2c` | `f5 76 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca30"></a> `00bbca30` | `10 81 02 94` | bl 0x00c5ce70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca34"></a> `00bbca34` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbca38"></a> `00bbca38` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbca3c"></a> `00bbca3c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00bbca40"></a> `00bbca40` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbca44"></a> `00bbca44` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbca48"></a> `00bbca48` | `fe 77 02 94` | bl 0x00c5aa40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca4c"></a> `00bbca4c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbca50"></a> `00bbca50` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbca54"></a> `00bbca54` | `eb 77 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca58"></a> `00bbca58` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbca5c"></a> `00bbca5c` | `0d 77 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca60"></a> `00bbca60` | `c0 b2 47 f9` | ldr x0,[x22, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbca64"></a> `00bbca64` | `87 78 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca68"></a> `00bbca68` | `48 2b 00 b0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbca6c"></a> `00bbca6c` | `49 2b 00 b0` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbca70"></a> `00bbca70` | `01 cd 47 f9` | ldr x1,[x8, #0xf98] | `FALL_THROUGH`
<a id="insn-00bbca74"></a> `00bbca74` | `22 7d 47 f9` | ldr x2,[x9, #0xef8] | `FALL_THROUGH`
<a id="insn-00bbca78"></a> `00bbca78` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbca7c"></a> `00bbca7c` | `5e 6b e3 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca80"></a> `00bbca80` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbca84"></a> `00bbca84` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbca88"></a> `00bbca88` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbca8c"></a> `00bbca8c` | `39 78 02 94` | bl 0x00c5ab70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbca90"></a> `00bbca90` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbca94"></a> `00bbca94` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbca98"></a> `00bbca98` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbca9c"></a> `00bbca9c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcaa0"></a> `00bbcaa0` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbcaa4"></a> `00bbcaa4` | `28 04 00 b4` | cbz x8,0x00bbcb28 | `CONDITIONAL_JUMP`
<a id="insn-00bbcaa8"></a> `00bbcaa8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcaac"></a> `00bbcaac` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcab0"></a> `00bbcab0` | `d4 77 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcab4"></a> `00bbcab4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcab8"></a> `00bbcab8` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcabc"></a> `00bbcabc` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcac0"></a> `00bbcac0` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcac4"></a> `00bbcac4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcac8"></a> `00bbcac8` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbcacc"></a> `00bbcacc` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcad0"></a> `00bbcad0` | `e4 03 01 91` | add x4,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbcad4"></a> `00bbcad4` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbcad8"></a> `00bbcad8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbcadc"></a> `00bbcadc` | `b1 77 02 94` | bl 0x00c5a9a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcae0"></a> `00bbcae0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcae4"></a> `00bbcae4` | `eb 76 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcae8"></a> `00bbcae8` | `18 00 00 14` | b 0x00bbcb48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcaec"></a> `00bbcaec` | `20 b7 ff d0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbcaf0"></a> `00bbcaf0` | `00 20 21 91` | add x0,x0,#0x848 | `FALL_THROUGH`
<a id="insn-00bbcaf4"></a> `00bbcaf4` | `6b 77 02 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcaf8"></a> `00bbcaf8` | `a0 b7 ff 90` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbcafc"></a> `00bbcafc` | `00 dc 1c 91` | add x0,x0,#0x737 | `FALL_THROUGH`
<a id="insn-00bbcb00"></a> `00bbcb00` | `40 78 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb04"></a> `00bbcb04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbcb08"></a> `00bbcb08` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbcb0c"></a> `00bbcb0c` | `59 77 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb10"></a> `00bbcb10` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcb14"></a> `00bbcb14` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcb18"></a> `00bbcb18` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbcb1c"></a> `00bbcb1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbcb20"></a> `00bbcb20` | `30 77 02 94` | bl 0x00c5a7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb24"></a> `00bbcb24` | `1c 00 00 14` | b 0x00bbcb94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcb28"></a> `00bbcb28` | `e3 1b 40 f9` | ldr x3,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcb2c"></a> `00bbcb2c` | `e2 ff ff f0` | adrp x2,0xbbb000 | `FALL_THROUGH`
<a id="insn-00bbcb30"></a> `00bbcb30` | `84 ba ff d0` | adrp x4,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbcb34"></a> `00bbcb34` | `42 00 3a 91` | add x2,x2,#0xe80 | `FALL_THROUGH`
<a id="insn-00bbcb38"></a> `00bbcb38` | `84 04 1e 91` | add x4,x4,#0x781 | `FALL_THROUGH`
<a id="insn-00bbcb3c"></a> `00bbcb3c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbcb40"></a> `00bbcb40` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbcb44"></a> `00bbcb44` | `ff 77 02 94` | bl 0x00c5ab40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb48"></a> `00bbcb48` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbcb4c"></a> `00bbcb4c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbcb50"></a> `00bbcb50` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbcb54"></a> `00bbcb54` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbcb58"></a> `00bbcb58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbcb5c"></a> `00bbcb5c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbcb60"></a> `00bbcb60` | `00 78 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb64"></a> `00bbcb64` | `e2 c3 00 91` | add x2,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcb68"></a> `00bbcb68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbcb6c"></a> `00bbcb6c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbcb70"></a> `00bbcb70` | `98 77 02 94` | bl 0x00c5a9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb74"></a> `00bbcb74` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcb78"></a> `00bbcb78` | `68 00 00 36` | tbz w8,#0x0,0x00bbcb84 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb7c"></a> `00bbcb7c` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcb80"></a> `00bbcb80` | `cc 6b 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb84"></a> `00bbcb84` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcb88"></a> `00bbcb88` | `c2 76 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb8c"></a> `00bbcb8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcb90"></a> `00bbcb90` | `a0 76 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb94"></a> `00bbcb94` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcb98"></a> `00bbcb98` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbcb9c"></a> `00bbcb9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbcba0"></a> `00bbcba0` | `e1 00 00 54` | b.ne 0x00bbcbbc | `CONDITIONAL_JUMP`
<a id="insn-00bbcba4"></a> `00bbcba4` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbcba8"></a> `00bbcba8` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbcbac"></a> `00bbcbac` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbcbb0"></a> `00bbcbb0` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbcbb4"></a> `00bbcbb4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbcbb8"></a> `00bbcbb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbcbbc"></a> `00bbcbbc` | `c9 6b 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbc9ec`](#insn-00bbc9ec) 範囲 `[['00bbc9ec', '00bbca1f']]`
  - `CONDITIONAL_JUMP` [`00bbca1c`](#insn-00bbca1c) → [`00bbcaec`](#insn-00bbcaec)
  - `FALL_THROUGH` [`00bbca1c`](#insn-00bbca1c) → [`00bbca20`](#insn-00bbca20)
- ブロック [`00bbca20`](#insn-00bbca20) 範囲 `[['00bbca20', '00bbca3b']]`
  - `FALL_THROUGH` [`00bbca38`](#insn-00bbca38) → [`00bbca3c`](#insn-00bbca3c)
- ブロック [`00bbca3c`](#insn-00bbca3c) 範囲 `[['00bbca3c', '00bbca7f']]`
  - `FALL_THROUGH` [`00bbca7c`](#insn-00bbca7c) → [`00bbca80`](#insn-00bbca80)
- ブロック [`00bbca80`](#insn-00bbca80) 範囲 `[['00bbca80', '00bbcaa7']]`
  - `CONDITIONAL_JUMP` [`00bbcaa4`](#insn-00bbcaa4) → [`00bbcb28`](#insn-00bbcb28)
  - `FALL_THROUGH` [`00bbcaa4`](#insn-00bbcaa4) → [`00bbcaa8`](#insn-00bbcaa8)
- ブロック [`00bbcaa8`](#insn-00bbcaa8) 範囲 `[['00bbcaa8', '00bbcadf']]`
  - `FALL_THROUGH` [`00bbcadc`](#insn-00bbcadc) → [`00bbcae0`](#insn-00bbcae0)
- ブロック [`00bbcae0`](#insn-00bbcae0) 範囲 `[['00bbcae0', '00bbcaeb']]`
  - `UNCONDITIONAL_JUMP` [`00bbcae8`](#insn-00bbcae8) → [`00bbcb48`](#insn-00bbcb48)
- ブロック [`00bbcaec`](#insn-00bbcaec) 範囲 `[['00bbcaec', '00bbcb27']]`
  - `UNCONDITIONAL_JUMP` [`00bbcb24`](#insn-00bbcb24) → [`00bbcb94`](#insn-00bbcb94)
- ブロック [`00bbcb28`](#insn-00bbcb28) 範囲 `[['00bbcb28', '00bbcb47']]`
  - `FALL_THROUGH` [`00bbcb44`](#insn-00bbcb44) → [`00bbcb48`](#insn-00bbcb48)
- ブロック [`00bbcb48`](#insn-00bbcb48) 範囲 `[['00bbcb48', '00bbcb7b']]`
  - `CONDITIONAL_JUMP` [`00bbcb78`](#insn-00bbcb78) → [`00bbcb84`](#insn-00bbcb84)
  - `FALL_THROUGH` [`00bbcb78`](#insn-00bbcb78) → [`00bbcb7c`](#insn-00bbcb7c)
- ブロック [`00bbcb7c`](#insn-00bbcb7c) 範囲 `[['00bbcb7c', '00bbcb83']]`
  - `FALL_THROUGH` [`00bbcb80`](#insn-00bbcb80) → [`00bbcb84`](#insn-00bbcb84)
- ブロック [`00bbcb84`](#insn-00bbcb84) 範囲 `[['00bbcb84', '00bbcb93']]`
  - `FALL_THROUGH` [`00bbcb90`](#insn-00bbcb90) → [`00bbcb94`](#insn-00bbcb94)
- ブロック [`00bbcb94`](#insn-00bbcb94) 範囲 `[['00bbcb94', '00bbcba3']]`
  - `CONDITIONAL_JUMP` [`00bbcba0`](#insn-00bbcba0) → [`00bbcbbc`](#insn-00bbcbbc)
  - `FALL_THROUGH` [`00bbcba0`](#insn-00bbcba0) → [`00bbcba4`](#insn-00bbcba4)
- ブロック [`00bbcba4`](#insn-00bbcba4) 範囲 `[['00bbcba4', '00bbcbab']]`
  - `FALL_THROUGH` [`00bbcba8`](#insn-00bbcba8) → [`00bbcbac`](#insn-00bbcbac)
- ブロック [`00bbcbac`](#insn-00bbcbac) 範囲 `[['00bbcbac', '00bbcbbb']]`
- ブロック [`00bbcbbc`](#insn-00bbcbbc) 範囲 `[['00bbcbbc', '00bbcbbf']]`

## 命令位置別の参照

- [`00bbc9f0`](#insn-00bbc9f0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9f4`](#insn-00bbc9f4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9f8`](#insn-00bbc9f8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9fc`](#insn-00bbc9fc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbca14`](#insn-00bbca14) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbca18`](#insn-00bbca18) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbca1c`](#insn-00bbca1c) → [`00bbcaec`](#insn-00bbcaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbca24`](#insn-00bbca24) → `01125f70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbca2c`](#insn-00bbca2c) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bbca30`](#insn-00bbca30) → [`00c5ce70`](../00c5c/00c5ce70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ce70` · 推定シンボル `None` · 推定型 `None`
- [`00bbca48`](#insn-00bbca48) → [`00c5aa40`](../00c5a/00c5aa40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa40` · 推定シンボル `None` · 推定型 `None`
- [`00bbca54`](#insn-00bbca54) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbca5c`](#insn-00bbca5c) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bbca60`](#insn-00bbca60) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbca64`](#insn-00bbca64) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bbca70`](#insn-00bbca70) → `01125f98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbca74`](#insn-00bbca74) → `01125ef8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbca7c`](#insn-00bbca7c) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bbca8c`](#insn-00bbca8c) → [`00c5ab70`](../00c5a/00c5ab70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab70` · 推定シンボル `None` · 推定型 `None`
- [`00bbca90`](#insn-00bbca90) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbca94`](#insn-00bbca94) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcaa4`](#insn-00bbcaa4) → [`00bbcb28`](#insn-00bbcb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcab0`](#insn-00bbcab0) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbcab4`](#insn-00bbcab4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcab8`](#insn-00bbcab8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcadc`](#insn-00bbcadc) → [`00c5a9a0`](../00c5a/00c5a9a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcae4`](#insn-00bbcae4) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bbcae8`](#insn-00bbcae8) → [`00bbcb48`](#insn-00bbcb48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcaf0`](#insn-00bbcaf0) → `002a2848`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcaf4`](#insn-00bbcaf4) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcafc`](#insn-00bbcafc) → `002b0737`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcb00`](#insn-00bbcb00) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb0c`](#insn-00bbcb0c) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb20`](#insn-00bbcb20) → [`00c5a7e0`](../00c5a/00c5a7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7e0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb24`](#insn-00bbcb24) → [`00bbcb94`](#insn-00bbcb94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb28`](#insn-00bbcb28) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb34`](#insn-00bbcb34) → [`00bbbe80`](../00bbb/00bbbe80.md) · `PARAM` · `ANALYSIS` · 関数 `00bbbe80` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb38`](#insn-00bbcb38) → `0030e781`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcb44`](#insn-00bbcb44) → [`00c5ab40`](../00c5a/00c5ab40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab40` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb60`](#insn-00bbcb60) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb70`](#insn-00bbcb70) → [`00c5a9d0`](../00c5a/00c5a9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb74`](#insn-00bbcb74) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb78`](#insn-00bbcb78) → [`00bbcb84`](#insn-00bbcb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb7c`](#insn-00bbcb7c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb80`](#insn-00bbcb80) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb88`](#insn-00bbcb88) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb90`](#insn-00bbcb90) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb98`](#insn-00bbcb98) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba0`](#insn-00bbcba0) → [`00bbcbbc`](#insn-00bbcbbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba4`](#insn-00bbcba4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba8`](#insn-00bbcba8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbac`](#insn-00bbcbac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbb0`](#insn-00bbcbb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbbc`](#insn-00bbcbbc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbc9f0`](#insn-00bbc9f0)

~~~json
{
  "source": "00bbc9f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9f4`](#insn-00bbc9f4)

~~~json
{
  "source": "00bbc9f4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9f8`](#insn-00bbc9f8)

~~~json
{
  "source": "00bbc9f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9fc`](#insn-00bbc9fc)

~~~json
{
  "source": "00bbc9fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbca14`](#insn-00bbca14)

~~~json
{
  "source": "00bbca14",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbca18`](#insn-00bbca18)

~~~json
{
  "source": "00bbca18",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbca1c`](#insn-00bbca1c)

~~~json
{
  "source": "00bbca1c",
  "target": "00bbcaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbca24`](#insn-00bbca24)

~~~json
{
  "source": "00bbca24",
  "target": "01125f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbca2c`](#insn-00bbca2c)

~~~json
{
  "source": "00bbca2c",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca30`](#insn-00bbca30)

~~~json
{
  "source": "00bbca30",
  "target": "00c5ce70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca48`](#insn-00bbca48)

~~~json
{
  "source": "00bbca48",
  "target": "00c5aa40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca54`](#insn-00bbca54)

~~~json
{
  "source": "00bbca54",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca5c`](#insn-00bbca5c)

~~~json
{
  "source": "00bbca5c",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca60`](#insn-00bbca60)

~~~json
{
  "source": "00bbca60",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbca64`](#insn-00bbca64)

~~~json
{
  "source": "00bbca64",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca70`](#insn-00bbca70)

~~~json
{
  "source": "00bbca70",
  "target": "01125f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbca74`](#insn-00bbca74)

~~~json
{
  "source": "00bbca74",
  "target": "01125ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125ef8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbca7c`](#insn-00bbca7c)

~~~json
{
  "source": "00bbca7c",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca8c`](#insn-00bbca8c)

~~~json
{
  "source": "00bbca8c",
  "target": "00c5ab70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbca90`](#insn-00bbca90)

~~~json
{
  "source": "00bbca90",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbca94`](#insn-00bbca94)

~~~json
{
  "source": "00bbca94",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcaa4`](#insn-00bbcaa4)

~~~json
{
  "source": "00bbcaa4",
  "target": "00bbcb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcab0`](#insn-00bbcab0)

~~~json
{
  "source": "00bbcab0",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcab4`](#insn-00bbcab4)

~~~json
{
  "source": "00bbcab4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcab8`](#insn-00bbcab8)

~~~json
{
  "source": "00bbcab8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcadc`](#insn-00bbcadc)

~~~json
{
  "source": "00bbcadc",
  "target": "00c5a9a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcae4`](#insn-00bbcae4)

~~~json
{
  "source": "00bbcae4",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcae8`](#insn-00bbcae8)

~~~json
{
  "source": "00bbcae8",
  "target": "00bbcb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcaf0`](#insn-00bbcaf0)

~~~json
{
  "source": "00bbcaf0",
  "target": "002a2848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2848",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2848",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcaf4`](#insn-00bbcaf4)

~~~json
{
  "source": "00bbcaf4",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcafc`](#insn-00bbcafc)

~~~json
{
  "source": "00bbcafc",
  "target": "002b0737",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0737",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0737",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcb00`](#insn-00bbcb00)

~~~json
{
  "source": "00bbcb00",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb0c`](#insn-00bbcb0c)

~~~json
{
  "source": "00bbcb0c",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb20`](#insn-00bbcb20)

~~~json
{
  "source": "00bbcb20",
  "target": "00c5a7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb24`](#insn-00bbcb24)

~~~json
{
  "source": "00bbcb24",
  "target": "00bbcb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb28`](#insn-00bbcb28)

~~~json
{
  "source": "00bbcb28",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb34`](#insn-00bbcb34)

~~~json
{
  "source": "00bbcb34",
  "target": "00bbbe80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb38`](#insn-00bbcb38)

~~~json
{
  "source": "00bbcb38",
  "target": "0030e781",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e781",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4d6573736167696e6700",
  "capture_start": "0030e781",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcb44`](#insn-00bbcb44)

~~~json
{
  "source": "00bbcb44",
  "target": "00c5ab40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb60`](#insn-00bbcb60)

~~~json
{
  "source": "00bbcb60",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb70`](#insn-00bbcb70)

~~~json
{
  "source": "00bbcb70",
  "target": "00c5a9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb74`](#insn-00bbcb74)

~~~json
{
  "source": "00bbcb74",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb78`](#insn-00bbcb78)

~~~json
{
  "source": "00bbcb78",
  "target": "00bbcb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb7c`](#insn-00bbcb7c)

~~~json
{
  "source": "00bbcb7c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb80`](#insn-00bbcb80)

~~~json
{
  "source": "00bbcb80",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb88`](#insn-00bbcb88)

~~~json
{
  "source": "00bbcb88",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb90`](#insn-00bbcb90)

~~~json
{
  "source": "00bbcb90",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb98`](#insn-00bbcb98)

~~~json
{
  "source": "00bbcb98",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba0`](#insn-00bbcba0)

~~~json
{
  "source": "00bbcba0",
  "target": "00bbcbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba4`](#insn-00bbcba4)

~~~json
{
  "source": "00bbcba4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba8`](#insn-00bbcba8)

~~~json
{
  "source": "00bbcba8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbac`](#insn-00bbcbac)

~~~json
{
  "source": "00bbcbac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbb0`](#insn-00bbcbb0)

~~~json
{
  "source": "00bbcbb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbbc`](#insn-00bbcbbc)

~~~json
{
  "source": "00bbcbbc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
