# 00bdfda0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdf978`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf978.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-2c0a0a307a88f1dbffe957ca95ef7eac)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdfe3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfe3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-0853697accafd364dbed3cefb98ef7e1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfda0",
  "name": "_ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d155173c8c7f9d834392d416373df0c37610d391417feed6646d33278c8256cc",
  "source_text_sha256": "d155173c8c7f9d834392d416373df0c37610d391417feed6646d33278c8256cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfda0",
        "00bdff2b"
      ]
    ],
    "bytes_sha256": "5e16addaf90c004cda10a3a1b0ee5eac7dd6bc1196074da2bcd64a5d7c14ca8a",
    "instruction_count": 99,
    "instruction_bytes": 396,
    "body_bytes": 396,
    "indirect": 1,
    "unresolved": 1
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
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dc00](../00c5d/00c5dc00.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dd30](../00c5d/00c5dd30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3999 bytes

~~~c

void _ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE
               (long param_1,long param_2,undefined8 *param_3)

{
  long lVar1;
  undefined *puVar2;
  long *plVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bdfdb8 to 00cdfdbf has its CatchHandler @ 00be06c0 */
  lVar1 = tpidr_el0;
                    /* try { // try from 00bdfdc0 to 00cdfdcb has its CatchHandler @ 00be06bc */
  local_58 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00bdfdcc to 00cdfddf has its CatchHandler @ 00be06a0 */
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
                    /* try { // try from 00bdfe88 to 00cdfe93 has its CatchHandler @ 00be055c */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bdfe94 to 00cdfea7 has its CatchHandler @ 00be053c */
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
              (auStack_68,lVar9,0x12);
                    /* try { // try from 00bdfdf8 to 00cdfe07 has its CatchHandler @ 00be0680 */
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar4 = FUN_00497834(plVar3,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126d60,
                         *param_3);
                    /* try { // try from 00bdfe20 to 00cdfe2b has its CatchHandler @ 00be0660 */
                    /* try { // try from 00bdfe2c to 00cdfe3b has its CatchHandler @ 00be0624 */
    uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,lVar9,auStack_68);
    if ((uVar5 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      puVar10 = *(undefined8 **)(param_2 + 0x98);
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar7 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_78);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9ba20
      ;
                    /* try { // try from 00bdfe68 to 00cdfe6f has its CatchHandler @ 00be0740 */
      *(undefined8 **)(lVar7 + 0x10) = puVar10;
      *(undefined **)(lVar7 + 0x18) = puVar2;
                    /* try { // try from 00bdfe78 to 00cdfe87 has its CatchHandler @ 00be0570 */
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
        lVar8 = (long)puVar10 + 0x141;
      }
      else {
        lVar8 = puVar10[0x2a];
      }
                    /* try { // try from 00bdfec0 to 00cdfecb has its CatchHandler @ 00be0508 */
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar4,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba00
                 ,lVar7,lVar8);
      _ZN8firebase12FutureHandleD2Ev(auStack_78);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
    }
                    /* try { // try from 00bdfeec to 00cdff13 has its CatchHandler @ 00be0740 */
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_68);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* try { // try from 00bdff18 to 00cdff1b has its CatchHandler @ 00be0778 */
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
<a id="insn-00bdfda0"></a> `00bdfda0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdfda4"></a> `00bdfda4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfda8"></a> `00bdfda8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfdac"></a> `00bdfdac` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfdb0"></a> `00bdfdb0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdfdb4"></a> `00bdfdb4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfdb8"></a> `00bdfdb8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bdfdbc"></a> `00bdfdbc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdfdc0"></a> `00bdfdc0` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfdc4"></a> `00bdfdc4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdfdc8"></a> `00bdfdc8` | `e9 17 00 f9` | str x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfdcc"></a> `00bdfdcc` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfdd0"></a> `00bdfdd0` | `c9 05 00 b4` | cbz x9,0x00bdfe88 | `CONDITIONAL_JUMP`
<a id="insn-00bdfdd4"></a> `00bdfdd4` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfdd8"></a> `00bdfdd8` | `88 05 00 b4` | cbz x8,0x00bdfe88 | `CONDITIONAL_JUMP`
<a id="insn-00bdfddc"></a> `00bdfddc` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfde0"></a> `00bdfde0` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bdfde4"></a> `00bdfde4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfde8"></a> `00bdfde8` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfdec"></a> `00bdfdec` | `41 02 80 52` | mov w1,#0x12 | `FALL_THROUGH`
<a id="insn-00bdfdf0"></a> `00bdfdf0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdfdf4"></a> `00bdfdf4` | `83 f7 01 94` | bl 0x00c5dc00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfdf8"></a> `00bdfdf8` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfdfc"></a> `00bdfdfc` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdfe00"></a> `00bdfe00` | `a0 ec 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe04"></a> `00bdfe04` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfe08"></a> `00bdfe08` | `29 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdfe0c"></a> `00bdfe0c` | `22 b1 46 f9` | ldr x2,[x9, #0xd60] | `FALL_THROUGH`
<a id="insn-00bdfe10"></a> `00bdfe10` | `c3 02 40 f9` | ldr x3,[x22] | `FALL_THROUGH`
<a id="insn-00bdfe14"></a> `00bdfe14` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfe18"></a> `00bdfe18` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdfe1c"></a> `00bdfe1c` | `86 de e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe20"></a> `00bdfe20` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdfe24"></a> `00bdfe24` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfe28"></a> `00bdfe28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfe2c"></a> `00bdfe2c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdfe30"></a> `00bdfe30` | `a8 f7 01 94` | bl 0x00c5dcd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe34"></a> `00bdfe34` | `80 05 00 37` | tbnz w0,#0x0,0x00bdfee4 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe38"></a> `00bdfe38` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfe3c"></a> `00bdfe3c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfe40"></a> `00bdfe40` | `f0 eb 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe44"></a> `00bdfe44` | `fa 4e 40 f9` | ldr x26,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfe48"></a> `00bdfe48` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bdfe4c"></a> `00bdfe4c` | `8d ec 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe50"></a> `00bdfe50` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfe54"></a> `00bdfe54` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfe58"></a> `00bdfe58` | `0e e0 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe5c"></a> `00bdfe5c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdfe60"></a> `00bdfe60` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfe64"></a> `00bdfe64` | `e7 eb 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe68"></a> `00bdfe68` | `e8 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdfe6c"></a> `00bdfe6c` | `08 11 45 f9` | ldr x8,[x8, #0xa20] | `FALL_THROUGH`
<a id="insn-00bdfe70"></a> `00bdfe70` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfe74"></a> `00bdfe74` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bdfe78"></a> `00bdfe78` | `a8 01 00 37` | tbnz w8,#0x0,0x00bdfeac | `CONDITIONAL_JUMP`
<a id="insn-00bdfe7c"></a> `00bdfe7c` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bdfe80"></a> `00bdfe80` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdfe84"></a> `00bdfe84` | `0b 00 00 14` | b 0x00bdfeb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdfe88"></a> `00bdfe88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdfe8c"></a> `00bdfe8c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bdfe90"></a> `00bdfe90` | `78 eb 01 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe94"></a> `00bdfe94` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bdfe98"></a> `00bdfe98` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfe9c"></a> `00bdfe9c` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bdfea0"></a> `00bdfea0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdfea4"></a> `00bdfea4` | `4f eb 01 94` | bl 0x00c5abe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfea8"></a> `00bdfea8` | `15 00 00 14` | b 0x00bdfefc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdfeac"></a> `00bdfeac` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bdfeb0"></a> `00bdfeb0` | `e2 05 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdfeb4"></a> `00bdfeb4` | `42 00 45 f9` | ldr x2,[x2, #0xa00] | `FALL_THROUGH`
<a id="insn-00bdfeb8"></a> `00bdfeb8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bdfebc"></a> `00bdfebc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdfec0"></a> `00bdfec0` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bdfec4"></a> `00bdfec4` | `1f ec 01 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfec8"></a> `00bdfec8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfecc"></a> `00bdfecc` | `f1 ea 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfed0"></a> `00bdfed0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdfed4"></a> `00bdfed4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdfed8"></a> `00bdfed8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfedc"></a> `00bdfedc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdfee0"></a> `00bdfee0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdfee4"></a> `00bdfee4` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfee8"></a> `00bdfee8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdfeec"></a> `00bdfeec` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdfef0"></a> `00bdfef0` | `90 f7 01 94` | bl 0x00c5dd30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfef4"></a> `00bdfef4` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfef8"></a> `00bdfef8` | `e6 ea 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfefc"></a> `00bdfefc` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdff00"></a> `00bdff00` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdff04"></a> `00bdff04` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdff08"></a> `00bdff08` | `01 01 00 54` | b.ne 0x00bdff28 | `CONDITIONAL_JUMP`
<a id="insn-00bdff0c"></a> `00bdff0c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdff10"></a> `00bdff10` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdff14"></a> `00bdff14` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdff18"></a> `00bdff18` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdff1c"></a> `00bdff1c` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdff20"></a> `00bdff20` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdff24"></a> `00bdff24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdff28"></a> `00bdff28` | `ee df 01 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfda0`](#insn-00bdfda0) 範囲 `[['00bdfda0', '00bdfdb7']]`
  - `FALL_THROUGH` [`00bdfdb4`](#insn-00bdfdb4) → [`00bdfdb8`](#insn-00bdfdb8)
- ブロック [`00bdfdb8`](#insn-00bdfdb8) 範囲 `[['00bdfdb8', '00bdfdbf']]`
  - `FALL_THROUGH` [`00bdfdbc`](#insn-00bdfdbc) → [`00bdfdc0`](#insn-00bdfdc0)
- ブロック [`00bdfdc0`](#insn-00bdfdc0) 範囲 `[['00bdfdc0', '00bdfdcb']]`
  - `FALL_THROUGH` [`00bdfdc8`](#insn-00bdfdc8) → [`00bdfdcc`](#insn-00bdfdcc)
- ブロック [`00bdfdcc`](#insn-00bdfdcc) 範囲 `[['00bdfdcc', '00bdfdd3']]`
  - `CONDITIONAL_JUMP` [`00bdfdd0`](#insn-00bdfdd0) → [`00bdfe88`](#insn-00bdfe88)
  - `FALL_THROUGH` [`00bdfdd0`](#insn-00bdfdd0) → [`00bdfdd4`](#insn-00bdfdd4)
- ブロック [`00bdfdd4`](#insn-00bdfdd4) 範囲 `[['00bdfdd4', '00bdfddb']]`
  - `CONDITIONAL_JUMP` [`00bdfdd8`](#insn-00bdfdd8) → [`00bdfe88`](#insn-00bdfe88)
  - `FALL_THROUGH` [`00bdfdd8`](#insn-00bdfdd8) → [`00bdfddc`](#insn-00bdfddc)
- ブロック [`00bdfddc`](#insn-00bdfddc) 範囲 `[['00bdfddc', '00bdfdf7']]`
  - `FALL_THROUGH` [`00bdfdf4`](#insn-00bdfdf4) → [`00bdfdf8`](#insn-00bdfdf8)
- ブロック [`00bdfdf8`](#insn-00bdfdf8) 範囲 `[['00bdfdf8', '00bdfe1f']]`
  - `FALL_THROUGH` [`00bdfe1c`](#insn-00bdfe1c) → [`00bdfe20`](#insn-00bdfe20)
- ブロック [`00bdfe20`](#insn-00bdfe20) 範囲 `[['00bdfe20', '00bdfe2b']]`
  - `FALL_THROUGH` [`00bdfe28`](#insn-00bdfe28) → [`00bdfe2c`](#insn-00bdfe2c)
- ブロック [`00bdfe2c`](#insn-00bdfe2c) 範囲 `[['00bdfe2c', '00bdfe37']]`
  - `CONDITIONAL_JUMP` [`00bdfe34`](#insn-00bdfe34) → [`00bdfee4`](#insn-00bdfee4)
  - `FALL_THROUGH` [`00bdfe34`](#insn-00bdfe34) → [`00bdfe38`](#insn-00bdfe38)
- ブロック [`00bdfe38`](#insn-00bdfe38) 範囲 `[['00bdfe38', '00bdfe67']]`
  - `FALL_THROUGH` [`00bdfe64`](#insn-00bdfe64) → [`00bdfe68`](#insn-00bdfe68)
- ブロック [`00bdfe68`](#insn-00bdfe68) 範囲 `[['00bdfe68', '00bdfe77']]`
  - `FALL_THROUGH` [`00bdfe74`](#insn-00bdfe74) → [`00bdfe78`](#insn-00bdfe78)
- ブロック [`00bdfe78`](#insn-00bdfe78) 範囲 `[['00bdfe78', '00bdfe7b']]`
  - `CONDITIONAL_JUMP` [`00bdfe78`](#insn-00bdfe78) → [`00bdfeac`](#insn-00bdfeac)
  - `FALL_THROUGH` [`00bdfe78`](#insn-00bdfe78) → [`00bdfe7c`](#insn-00bdfe7c)
- ブロック [`00bdfe7c`](#insn-00bdfe7c) 範囲 `[['00bdfe7c', '00bdfe87']]`
  - `UNCONDITIONAL_JUMP` [`00bdfe84`](#insn-00bdfe84) → [`00bdfeb0`](#insn-00bdfeb0)
- ブロック [`00bdfe88`](#insn-00bdfe88) 範囲 `[['00bdfe88', '00bdfe93']]`
  - `FALL_THROUGH` [`00bdfe90`](#insn-00bdfe90) → [`00bdfe94`](#insn-00bdfe94)
- ブロック [`00bdfe94`](#insn-00bdfe94) 範囲 `[['00bdfe94', '00bdfeab']]`
  - `UNCONDITIONAL_JUMP` [`00bdfea8`](#insn-00bdfea8) → [`00bdfefc`](#insn-00bdfefc)
- ブロック [`00bdfeac`](#insn-00bdfeac) 範囲 `[['00bdfeac', '00bdfeaf']]`
  - `FALL_THROUGH` [`00bdfeac`](#insn-00bdfeac) → [`00bdfeb0`](#insn-00bdfeb0)
- ブロック [`00bdfeb0`](#insn-00bdfeb0) 範囲 `[['00bdfeb0', '00bdfebf']]`
  - `FALL_THROUGH` [`00bdfebc`](#insn-00bdfebc) → [`00bdfec0`](#insn-00bdfec0)
- ブロック [`00bdfec0`](#insn-00bdfec0) 範囲 `[['00bdfec0', '00bdfee3']]`
  - `FALL_THROUGH` [`00bdfee0`](#insn-00bdfee0) → [`00bdfee4`](#insn-00bdfee4)
- ブロック [`00bdfee4`](#insn-00bdfee4) 範囲 `[['00bdfee4', '00bdfeeb']]`
  - `FALL_THROUGH` [`00bdfee8`](#insn-00bdfee8) → [`00bdfeec`](#insn-00bdfeec)
- ブロック [`00bdfeec`](#insn-00bdfeec) 範囲 `[['00bdfeec', '00bdfefb']]`
  - `FALL_THROUGH` [`00bdfef8`](#insn-00bdfef8) → [`00bdfefc`](#insn-00bdfefc)
- ブロック [`00bdfefc`](#insn-00bdfefc) 範囲 `[['00bdfefc', '00bdff0b']]`
  - `CONDITIONAL_JUMP` [`00bdff08`](#insn-00bdff08) → [`00bdff28`](#insn-00bdff28)
  - `FALL_THROUGH` [`00bdff08`](#insn-00bdff08) → [`00bdff0c`](#insn-00bdff0c)
- ブロック [`00bdff0c`](#insn-00bdff0c) 範囲 `[['00bdff0c', '00bdff17']]`
  - `FALL_THROUGH` [`00bdff14`](#insn-00bdff14) → [`00bdff18`](#insn-00bdff18)
- ブロック [`00bdff18`](#insn-00bdff18) 範囲 `[['00bdff18', '00bdff27']]`
- ブロック [`00bdff28`](#insn-00bdff28) 範囲 `[['00bdff28', '00bdff2b']]`

## 命令位置別の参照

- [`00bdfda4`](#insn-00bdfda4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfda8`](#insn-00bdfda8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdac`](#insn-00bdfdac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdb0`](#insn-00bdfdb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdb4`](#insn-00bdfdb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdc8`](#insn-00bdfdc8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdd0`](#insn-00bdfdd0) → [`00bdfe88`](#insn-00bdfe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdd8`](#insn-00bdfdd8) → [`00bdfe88`](#insn-00bdfe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdf4`](#insn-00bdfdf4) → [`00c5dc00`](../00c5d/00c5dc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc00` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe00`](#insn-00bdfe00) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe0c`](#insn-00bdfe0c) → `01126d60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdfe1c`](#insn-00bdfe1c) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe30`](#insn-00bdfe30) → [`00c5dcd0`](../00c5d/00c5dcd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dcd0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe34`](#insn-00bdfe34) → [`00bdfee4`](#insn-00bdfee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe40`](#insn-00bdfe40) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe4c`](#insn-00bdfe4c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe58`](#insn-00bdfe58) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe64`](#insn-00bdfe64) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe6c`](#insn-00bdfe6c) → `00c9ba20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfe70`](#insn-00bdfe70) → [`00bd482c`](../00bd4/00bd482c.md) · `DATA` · `ANALYSIS` · 関数 `00bd482c` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bdfe78`](#insn-00bdfe78) → [`00bdfeac`](#insn-00bdfeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe84`](#insn-00bdfe84) → [`00bdfeb0`](#insn-00bdfeb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe90`](#insn-00bdfe90) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bdfea4`](#insn-00bdfea4) → [`00c5abe0`](../00c5a/00c5abe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abe0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfea8`](#insn-00bdfea8) → [`00bdfefc`](#insn-00bdfefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfeb4`](#insn-00bdfeb4) → `00c9ba00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfeb4`](#insn-00bdfeb4) → [`00bcfd44`](../00bcf/00bcfd44.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfd44` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bdfec4`](#insn-00bdfec4) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bdfecc`](#insn-00bdfecc) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bdfef0`](#insn-00bdfef0) → [`00c5dd30`](../00c5d/00c5dd30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd30` · 推定シンボル `None` · 推定型 `None`
- [`00bdfef8`](#insn-00bdfef8) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bdff00`](#insn-00bdff00) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff08`](#insn-00bdff08) → [`00bdff28`](#insn-00bdff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff0c`](#insn-00bdff0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff10`](#insn-00bdff10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff14`](#insn-00bdff14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff18`](#insn-00bdff18) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff1c`](#insn-00bdff1c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff28`](#insn-00bdff28) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfda4`](#insn-00bdfda4)

~~~json
{
  "source": "00bdfda4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfda8`](#insn-00bdfda8)

~~~json
{
  "source": "00bdfda8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdac`](#insn-00bdfdac)

~~~json
{
  "source": "00bdfdac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdb0`](#insn-00bdfdb0)

~~~json
{
  "source": "00bdfdb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdb4`](#insn-00bdfdb4)

~~~json
{
  "source": "00bdfdb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdc8`](#insn-00bdfdc8)

~~~json
{
  "source": "00bdfdc8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdd0`](#insn-00bdfdd0)

~~~json
{
  "source": "00bdfdd0",
  "target": "00bdfe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdd8`](#insn-00bdfdd8)

~~~json
{
  "source": "00bdfdd8",
  "target": "00bdfe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdf4`](#insn-00bdfdf4)

~~~json
{
  "source": "00bdfdf4",
  "target": "00c5dc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe00`](#insn-00bdfe00)

~~~json
{
  "source": "00bdfe00",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe0c`](#insn-00bdfe0c)

~~~json
{
  "source": "00bdfe0c",
  "target": "01126d60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdfe1c`](#insn-00bdfe1c)

~~~json
{
  "source": "00bdfe1c",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe30`](#insn-00bdfe30)

~~~json
{
  "source": "00bdfe30",
  "target": "00c5dcd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe34`](#insn-00bdfe34)

~~~json
{
  "source": "00bdfe34",
  "target": "00bdfee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe40`](#insn-00bdfe40)

~~~json
{
  "source": "00bdfe40",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe4c`](#insn-00bdfe4c)

~~~json
{
  "source": "00bdfe4c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe58`](#insn-00bdfe58)

~~~json
{
  "source": "00bdfe58",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe64`](#insn-00bdfe64)

~~~json
{
  "source": "00bdfe64",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe6c`](#insn-00bdfe6c)

~~~json
{
  "source": "00bdfe6c",
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
- 参照命令 [`00bdfe70`](#insn-00bdfe70)

~~~json
{
  "source": "00bdfe70",
  "target": "00bd482c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe78`](#insn-00bdfe78)

~~~json
{
  "source": "00bdfe78",
  "target": "00bdfeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe84`](#insn-00bdfe84)

~~~json
{
  "source": "00bdfe84",
  "target": "00bdfeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe90`](#insn-00bdfe90)

~~~json
{
  "source": "00bdfe90",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfea4`](#insn-00bdfea4)

~~~json
{
  "source": "00bdfea4",
  "target": "00c5abe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfea8`](#insn-00bdfea8)

~~~json
{
  "source": "00bdfea8",
  "target": "00bdfefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfeb4`](#insn-00bdfeb4)

~~~json
{
  "source": "00bdfeb4",
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
- 参照命令 [`00bdfeb4`](#insn-00bdfeb4)

~~~json
{
  "source": "00bdfeb4",
  "target": "00bcfd44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfec4`](#insn-00bdfec4)

~~~json
{
  "source": "00bdfec4",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfecc`](#insn-00bdfecc)

~~~json
{
  "source": "00bdfecc",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfef0`](#insn-00bdfef0)

~~~json
{
  "source": "00bdfef0",
  "target": "00c5dd30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfef8`](#insn-00bdfef8)

~~~json
{
  "source": "00bdfef8",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff00`](#insn-00bdff00)

~~~json
{
  "source": "00bdff00",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff08`](#insn-00bdff08)

~~~json
{
  "source": "00bdff08",
  "target": "00bdff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff0c`](#insn-00bdff0c)

~~~json
{
  "source": "00bdff0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff10`](#insn-00bdff10)

~~~json
{
  "source": "00bdff10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff14`](#insn-00bdff14)

~~~json
{
  "source": "00bdff14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff18`](#insn-00bdff18)

~~~json
{
  "source": "00bdff18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff1c`](#insn-00bdff1c)

~~~json
{
  "source": "00bdff1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff28`](#insn-00bdff28)

~~~json
{
  "source": "00bdff28",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
