# 00bbc0dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbc040`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-992bc10d832ead27591a47536c8690db)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbd0d0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd0d0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-81037c6d948dedb53d01fc9b42941072)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbc0dc",
  "name": "_ZN8firebase9messaging8RegisterEv",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "280bce1eab6b5d75f1c10ea20457ef94483df0c8b8cc845cef369a3e7c227806",
  "source_text_sha256": "280bce1eab6b5d75f1c10ea20457ef94483df0c8b8cc845cef369a3e7c227806",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbc0dc",
        "00bbc2af"
      ]
    ],
    "bytes_sha256": "b53aa9d9f2e4aed357bdb9de178dac4e47f048d3260fcc4cfcf824ba570e0310",
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

- [00497874](../00497/00497874.md)
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
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b040](../00c5b/00c5b040.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5d340](../00c5d/00c5d340.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3062 bytes

~~~c

void _ZN8firebase9messaging8RegisterEv(long param_1)

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
  
  uVar4 = DAT_01126470;
                    /* try { // try from 00bbc0e0 to 00cbc17b has its CatchHandler @ 00bbc850 */
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  if (DAT_01126460 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
                    /* try { // try from 00bbc1f8 to 00cbc21f has its CatchHandler @ 00bbc7f8 */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    _ZN8firebase5Mutex7AcquireEv(DAT_01126470);
    uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(local_78,uVar5,5,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(local_60,local_78);
    _ZN8firebase12FutureHandleD2Ev(local_78);
    plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01126460);
    uVar7 = FUN_00497874(plVar6,DAT_01126498,DAT_01126400);
                    /* try { // try from 00bbc17c to 00cbc1f7 has its CatchHandler @ 00bbb99c */
    _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv(local_78,plVar6);
    uVar1 = (ulong)(local_78[0] >> 1);
    if ((local_78[0] & 1) != 0) {
      uVar1 = local_70;
    }
    if (uVar1 == 0) {
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar6,uVar7,FUN_00bbc344,local_60[0],"Messaging");
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
                    /* try { // try from 00bbc254 to 00cbc25f has its CatchHandler @ 00bbc7c0 */
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
                    /* try { // try from 00bbc2ac to 00cbc2cf has its CatchHandler @ 00bbc7c8 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbc0dc"></a> `00bbc0dc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbc0e0"></a> `00bbc0e0` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbc0e4"></a> `00bbc0e4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbc0e8"></a> `00bbc0e8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbc0ec"></a> `00bbc0ec` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbc0f0"></a> `00bbc0f0` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbc0f4"></a> `00bbc0f4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbc0f8"></a> `00bbc0f8` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc0fc"></a> `00bbc0fc` | `56 2b 00 d0` | adrp x22,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbc100"></a> `00bbc100` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bbc104"></a> `00bbc104` | `a9 83 1c f8` | stur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbc108"></a> `00bbc108` | `c9 32 42 f9` | ldr x9,[x22, #0x460] | `FALL_THROUGH`
<a id="insn-00bbc10c"></a> `00bbc10c` | `89 06 00 b4` | cbz x9,0x00bbc1dc | `CONDITIONAL_JUMP`
<a id="insn-00bbc110"></a> `00bbc110` | `48 2b 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbc114"></a> `00bbc114` | `13 39 42 f9` | ldr x19,[x8, #0x470] | `FALL_THROUGH`
<a id="insn-00bbc118"></a> `00bbc118` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbc11c"></a> `00bbc11c` | `6d 7a 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc120"></a> `00bbc120` | `88 84 02 94` | bl 0x00c5d340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc124"></a> `00bbc124` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbc128"></a> `00bbc128` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc12c"></a> `00bbc12c` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00bbc130"></a> `00bbc130` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbc134"></a> `00bbc134` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbc138"></a> `00bbc138` | `76 7b 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc13c"></a> `00bbc13c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbc140"></a> `00bbc140` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc144"></a> `00bbc144` | `63 7b 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc148"></a> `00bbc148` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc14c"></a> `00bbc14c` | `85 7a 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc150"></a> `00bbc150` | `c0 32 42 f9` | ldr x0,[x22, #0x460] | `FALL_THROUGH`
<a id="insn-00bbc154"></a> `00bbc154` | `ff 7b 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc158"></a> `00bbc158` | `48 2b 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbc15c"></a> `00bbc15c` | `49 2b 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbc160"></a> `00bbc160` | `01 4d 42 f9` | ldr x1,[x8, #0x498] | `FALL_THROUGH`
<a id="insn-00bbc164"></a> `00bbc164` | `22 01 42 f9` | ldr x2,[x9, #0x400] | `FALL_THROUGH`
<a id="insn-00bbc168"></a> `00bbc168` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbc16c"></a> `00bbc16c` | `c2 6d e3 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc170"></a> `00bbc170` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbc174"></a> `00bbc174` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc178"></a> `00bbc178` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbc17c"></a> `00bbc17c` | `b1 7b 02 94` | bl 0x00c5b040 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc180"></a> `00bbc180` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc184"></a> `00bbc184` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc188"></a> `00bbc188` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc18c"></a> `00bbc18c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc190"></a> `00bbc190` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbc194"></a> `00bbc194` | `28 04 00 b4` | cbz x8,0x00bbc218 | `CONDITIONAL_JUMP`
<a id="insn-00bbc198"></a> `00bbc198` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbc19c"></a> `00bbc19c` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbc1a0"></a> `00bbc1a0` | `4c 7b 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc1a4"></a> `00bbc1a4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc1a8"></a> `00bbc1a8` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc1ac"></a> `00bbc1ac` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc1b0"></a> `00bbc1b0` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc1b4"></a> `00bbc1b4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc1b8"></a> `00bbc1b8` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbc1bc"></a> `00bbc1bc` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbc1c0"></a> `00bbc1c0` | `e4 03 01 91` | add x4,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbc1c4"></a> `00bbc1c4` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbc1c8"></a> `00bbc1c8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbc1cc"></a> `00bbc1cc` | `29 7b 02 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc1d0"></a> `00bbc1d0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbc1d4"></a> `00bbc1d4` | `63 7a 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc1d8"></a> `00bbc1d8` | `18 00 00 14` | b 0x00bbc238 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc1dc"></a> `00bbc1dc` | `20 b7 ff d0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbc1e0"></a> `00bbc1e0` | `00 20 23 91` | add x0,x0,#0x8c8 | `FALL_THROUGH`
<a id="insn-00bbc1e4"></a> `00bbc1e4` | `e3 7a 02 94` | bl 0x00c5ad70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc1e8"></a> `00bbc1e8` | `a0 b7 ff 90` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbc1ec"></a> `00bbc1ec` | `00 6c 1c 91` | add x0,x0,#0x71b | `FALL_THROUGH`
<a id="insn-00bbc1f0"></a> `00bbc1f0` | `b8 7b 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc1f4"></a> `00bbc1f4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbc1f8"></a> `00bbc1f8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbc1fc"></a> `00bbc1fc` | `d1 7a 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc200"></a> `00bbc200` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bbc204"></a> `00bbc204` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc208"></a> `00bbc208` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbc20c"></a> `00bbc20c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbc210"></a> `00bbc210` | `a8 7a 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc214"></a> `00bbc214` | `1c 00 00 14` | b 0x00bbc284 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc218"></a> `00bbc218` | `e3 1b 40 f9` | ldr x3,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc21c"></a> `00bbc21c` | `02 00 00 90` | adrp x2,0xbbc000 | `FALL_THROUGH`
<a id="insn-00bbc220"></a> `00bbc220` | `84 ba ff d0` | adrp x4,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbc224"></a> `00bbc224` | `42 10 0d 91` | add x2,x2,#0x344 | `FALL_THROUGH`
<a id="insn-00bbc228"></a> `00bbc228` | `84 04 20 91` | add x4,x4,#0x801 | `FALL_THROUGH`
<a id="insn-00bbc22c"></a> `00bbc22c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbc230"></a> `00bbc230` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbc234"></a> `00bbc234` | `77 7b 02 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc238"></a> `00bbc238` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbc23c"></a> `00bbc23c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbc240"></a> `00bbc240` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbc244"></a> `00bbc244` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbc248"></a> `00bbc248` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbc24c"></a> `00bbc24c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbc250"></a> `00bbc250` | `78 7b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc254"></a> `00bbc254` | `e2 c3 00 91` | add x2,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbc258"></a> `00bbc258` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbc25c"></a> `00bbc25c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbc260"></a> `00bbc260` | `10 7b 02 94` | bl 0x00c5aea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc264"></a> `00bbc264` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc268"></a> `00bbc268` | `68 00 00 36` | tbz w8,#0x0,0x00bbc274 | `CONDITIONAL_JUMP`
<a id="insn-00bbc26c"></a> `00bbc26c` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc270"></a> `00bbc270` | `44 6f 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc274"></a> `00bbc274` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbc278"></a> `00bbc278` | `3a 7a 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc27c"></a> `00bbc27c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbc280"></a> `00bbc280` | `18 7a 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc284"></a> `00bbc284` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc288"></a> `00bbc288` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbc28c"></a> `00bbc28c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbc290"></a> `00bbc290` | `e1 00 00 54` | b.ne 0x00bbc2ac | `CONDITIONAL_JUMP`
<a id="insn-00bbc294"></a> `00bbc294` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbc298"></a> `00bbc298` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbc29c"></a> `00bbc29c` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbc2a0"></a> `00bbc2a0` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbc2a4"></a> `00bbc2a4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbc2a8"></a> `00bbc2a8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbc2ac"></a> `00bbc2ac` | `41 6f 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbc0dc`](#insn-00bbc0dc) 範囲 `[['00bbc0dc', '00bbc0df']]`
  - `FALL_THROUGH` [`00bbc0dc`](#insn-00bbc0dc) → [`00bbc0e0`](#insn-00bbc0e0)
- ブロック [`00bbc0e0`](#insn-00bbc0e0) 範囲 `[['00bbc0e0', '00bbc10f']]`
  - `CONDITIONAL_JUMP` [`00bbc10c`](#insn-00bbc10c) → [`00bbc1dc`](#insn-00bbc1dc)
  - `FALL_THROUGH` [`00bbc10c`](#insn-00bbc10c) → [`00bbc110`](#insn-00bbc110)
- ブロック [`00bbc110`](#insn-00bbc110) 範囲 `[['00bbc110', '00bbc17b']]`
  - `FALL_THROUGH` [`00bbc178`](#insn-00bbc178) → [`00bbc17c`](#insn-00bbc17c)
- ブロック [`00bbc17c`](#insn-00bbc17c) 範囲 `[['00bbc17c', '00bbc197']]`
  - `CONDITIONAL_JUMP` [`00bbc194`](#insn-00bbc194) → [`00bbc218`](#insn-00bbc218)
  - `FALL_THROUGH` [`00bbc194`](#insn-00bbc194) → [`00bbc198`](#insn-00bbc198)
- ブロック [`00bbc198`](#insn-00bbc198) 範囲 `[['00bbc198', '00bbc1db']]`
  - `UNCONDITIONAL_JUMP` [`00bbc1d8`](#insn-00bbc1d8) → [`00bbc238`](#insn-00bbc238)
- ブロック [`00bbc1dc`](#insn-00bbc1dc) 範囲 `[['00bbc1dc', '00bbc1f7']]`
  - `FALL_THROUGH` [`00bbc1f4`](#insn-00bbc1f4) → [`00bbc1f8`](#insn-00bbc1f8)
- ブロック [`00bbc1f8`](#insn-00bbc1f8) 範囲 `[['00bbc1f8', '00bbc217']]`
  - `UNCONDITIONAL_JUMP` [`00bbc214`](#insn-00bbc214) → [`00bbc284`](#insn-00bbc284)
- ブロック [`00bbc218`](#insn-00bbc218) 範囲 `[['00bbc218', '00bbc237']]`
  - `FALL_THROUGH` [`00bbc234`](#insn-00bbc234) → [`00bbc238`](#insn-00bbc238)
- ブロック [`00bbc238`](#insn-00bbc238) 範囲 `[['00bbc238', '00bbc253']]`
  - `FALL_THROUGH` [`00bbc250`](#insn-00bbc250) → [`00bbc254`](#insn-00bbc254)
- ブロック [`00bbc254`](#insn-00bbc254) 範囲 `[['00bbc254', '00bbc26b']]`
  - `CONDITIONAL_JUMP` [`00bbc268`](#insn-00bbc268) → [`00bbc274`](#insn-00bbc274)
  - `FALL_THROUGH` [`00bbc268`](#insn-00bbc268) → [`00bbc26c`](#insn-00bbc26c)
- ブロック [`00bbc26c`](#insn-00bbc26c) 範囲 `[['00bbc26c', '00bbc273']]`
  - `FALL_THROUGH` [`00bbc270`](#insn-00bbc270) → [`00bbc274`](#insn-00bbc274)
- ブロック [`00bbc274`](#insn-00bbc274) 範囲 `[['00bbc274', '00bbc283']]`
  - `FALL_THROUGH` [`00bbc280`](#insn-00bbc280) → [`00bbc284`](#insn-00bbc284)
- ブロック [`00bbc284`](#insn-00bbc284) 範囲 `[['00bbc284', '00bbc293']]`
  - `CONDITIONAL_JUMP` [`00bbc290`](#insn-00bbc290) → [`00bbc2ac`](#insn-00bbc2ac)
  - `FALL_THROUGH` [`00bbc290`](#insn-00bbc290) → [`00bbc294`](#insn-00bbc294)
- ブロック [`00bbc294`](#insn-00bbc294) 範囲 `[['00bbc294', '00bbc2ab']]`
- ブロック [`00bbc2ac`](#insn-00bbc2ac) 範囲 `[['00bbc2ac', '00bbc2af']]`

## 命令位置別の参照

- [`00bbc0e0`](#insn-00bbc0e0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0e4`](#insn-00bbc0e4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0e8`](#insn-00bbc0e8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0ec`](#insn-00bbc0ec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc104`](#insn-00bbc104) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc108`](#insn-00bbc108) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc10c`](#insn-00bbc10c) → [`00bbc1dc`](#insn-00bbc1dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc114`](#insn-00bbc114) → `01126470`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc11c`](#insn-00bbc11c) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc120`](#insn-00bbc120) → [`00c5d340`](../00c5d/00c5d340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d340` · 推定シンボル `None` · 推定型 `None`
- [`00bbc138`](#insn-00bbc138) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bbc144`](#insn-00bbc144) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc14c`](#insn-00bbc14c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbc150`](#insn-00bbc150) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc154`](#insn-00bbc154) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bbc160`](#insn-00bbc160) → `01126498`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc164`](#insn-00bbc164) → `01126400`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc16c`](#insn-00bbc16c) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bbc17c`](#insn-00bbc17c) → [`00c5b040`](../00c5b/00c5b040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b040` · 推定シンボル `None` · 推定型 `None`
- [`00bbc180`](#insn-00bbc180) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc184`](#insn-00bbc184) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc194`](#insn-00bbc194) → [`00bbc218`](#insn-00bbc218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1a0`](#insn-00bbc1a0) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1a4`](#insn-00bbc1a4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1a8`](#insn-00bbc1a8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1cc`](#insn-00bbc1cc) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1d4`](#insn-00bbc1d4) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1d8`](#insn-00bbc1d8) → [`00bbc238`](#insn-00bbc238) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1e0`](#insn-00bbc1e0) → `002a28c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbc1e4`](#insn-00bbc1e4) → [`00c5ad70`](../00c5a/00c5ad70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad70` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1ec`](#insn-00bbc1ec) → `002b071b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbc1f0`](#insn-00bbc1f0) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc1fc`](#insn-00bbc1fc) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bbc210`](#insn-00bbc210) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc214`](#insn-00bbc214) → [`00bbc284`](#insn-00bbc284) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc218`](#insn-00bbc218) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc224`](#insn-00bbc224) → [`00bbc344`](00bbc344.md) · `PARAM` · `ANALYSIS` · 関数 `00bbc344` · 推定シンボル `None` · 推定型 `None`
- [`00bbc228`](#insn-00bbc228) → `0030e801`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbc234`](#insn-00bbc234) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bbc250`](#insn-00bbc250) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bbc260`](#insn-00bbc260) → [`00c5aea0`](../00c5a/00c5aea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc264`](#insn-00bbc264) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc268`](#insn-00bbc268) → [`00bbc274`](#insn-00bbc274) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc26c`](#insn-00bbc26c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc270`](#insn-00bbc270) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbc278`](#insn-00bbc278) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbc280`](#insn-00bbc280) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc288`](#insn-00bbc288) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc290`](#insn-00bbc290) → [`00bbc2ac`](#insn-00bbc2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc294`](#insn-00bbc294) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc298`](#insn-00bbc298) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc29c`](#insn-00bbc29c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc2a0`](#insn-00bbc2a0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc2ac`](#insn-00bbc2ac) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbc0e0`](#insn-00bbc0e0)

~~~json
{
  "source": "00bbc0e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0e4`](#insn-00bbc0e4)

~~~json
{
  "source": "00bbc0e4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0e8`](#insn-00bbc0e8)

~~~json
{
  "source": "00bbc0e8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0ec`](#insn-00bbc0ec)

~~~json
{
  "source": "00bbc0ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc104`](#insn-00bbc104)

~~~json
{
  "source": "00bbc104",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc108`](#insn-00bbc108)

~~~json
{
  "source": "00bbc108",
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
- 参照命令 [`00bbc10c`](#insn-00bbc10c)

~~~json
{
  "source": "00bbc10c",
  "target": "00bbc1dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc114`](#insn-00bbc114)

~~~json
{
  "source": "00bbc114",
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
- 参照命令 [`00bbc11c`](#insn-00bbc11c)

~~~json
{
  "source": "00bbc11c",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc120`](#insn-00bbc120)

~~~json
{
  "source": "00bbc120",
  "target": "00c5d340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc138`](#insn-00bbc138)

~~~json
{
  "source": "00bbc138",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc144`](#insn-00bbc144)

~~~json
{
  "source": "00bbc144",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc14c`](#insn-00bbc14c)

~~~json
{
  "source": "00bbc14c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc150`](#insn-00bbc150)

~~~json
{
  "source": "00bbc150",
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
- 参照命令 [`00bbc154`](#insn-00bbc154)

~~~json
{
  "source": "00bbc154",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc160`](#insn-00bbc160)

~~~json
{
  "source": "00bbc160",
  "target": "01126498",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126498",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbc164`](#insn-00bbc164)

~~~json
{
  "source": "00bbc164",
  "target": "01126400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126400",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbc16c`](#insn-00bbc16c)

~~~json
{
  "source": "00bbc16c",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc17c`](#insn-00bbc17c)

~~~json
{
  "source": "00bbc17c",
  "target": "00c5b040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc180`](#insn-00bbc180)

~~~json
{
  "source": "00bbc180",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc184`](#insn-00bbc184)

~~~json
{
  "source": "00bbc184",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc194`](#insn-00bbc194)

~~~json
{
  "source": "00bbc194",
  "target": "00bbc218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc1a0`](#insn-00bbc1a0)

~~~json
{
  "source": "00bbc1a0",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc1a4`](#insn-00bbc1a4)

~~~json
{
  "source": "00bbc1a4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc1a8`](#insn-00bbc1a8)

~~~json
{
  "source": "00bbc1a8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc1cc`](#insn-00bbc1cc)

~~~json
{
  "source": "00bbc1cc",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc1d4`](#insn-00bbc1d4)

~~~json
{
  "source": "00bbc1d4",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc1d8`](#insn-00bbc1d8)

~~~json
{
  "source": "00bbc1d8",
  "target": "00bbc238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc1e0`](#insn-00bbc1e0)

~~~json
{
  "source": "00bbc1e0",
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
- 参照命令 [`00bbc1e4`](#insn-00bbc1e4)

~~~json
{
  "source": "00bbc1e4",
  "target": "00c5ad70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc1ec`](#insn-00bbc1ec)

~~~json
{
  "source": "00bbc1ec",
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
- 参照命令 [`00bbc1f0`](#insn-00bbc1f0)

~~~json
{
  "source": "00bbc1f0",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc1fc`](#insn-00bbc1fc)

~~~json
{
  "source": "00bbc1fc",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc210`](#insn-00bbc210)

~~~json
{
  "source": "00bbc210",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc214`](#insn-00bbc214)

~~~json
{
  "source": "00bbc214",
  "target": "00bbc284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc218`](#insn-00bbc218)

~~~json
{
  "source": "00bbc218",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc224`](#insn-00bbc224)

~~~json
{
  "source": "00bbc224",
  "target": "00bbc344",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc228`](#insn-00bbc228)

~~~json
{
  "source": "00bbc228",
  "target": "0030e801",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e801",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4d6573736167696e6700",
  "capture_start": "0030e801",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbc234`](#insn-00bbc234)

~~~json
{
  "source": "00bbc234",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc250`](#insn-00bbc250)

~~~json
{
  "source": "00bbc250",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc260`](#insn-00bbc260)

~~~json
{
  "source": "00bbc260",
  "target": "00c5aea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc264`](#insn-00bbc264)

~~~json
{
  "source": "00bbc264",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc268`](#insn-00bbc268)

~~~json
{
  "source": "00bbc268",
  "target": "00bbc274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc26c`](#insn-00bbc26c)

~~~json
{
  "source": "00bbc26c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc270`](#insn-00bbc270)

~~~json
{
  "source": "00bbc270",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc278`](#insn-00bbc278)

~~~json
{
  "source": "00bbc278",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc280`](#insn-00bbc280)

~~~json
{
  "source": "00bbc280",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc288`](#insn-00bbc288)

~~~json
{
  "source": "00bbc288",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc290`](#insn-00bbc290)

~~~json
{
  "source": "00bbc290",
  "target": "00bbc2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc294`](#insn-00bbc294)

~~~json
{
  "source": "00bbc294",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc298`](#insn-00bbc298)

~~~json
{
  "source": "00bbc298",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc29c`](#insn-00bbc29c)

~~~json
{
  "source": "00bbc29c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc2a0`](#insn-00bbc2a0)

~~~json
{
  "source": "00bbc2a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc2ac`](#insn-00bbc2ac)

~~~json
{
  "source": "00bbc2ac",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
