# 00bdfffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdfbd4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfbd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-5081d77257dae35f12dbba92d775797a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00be0098`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0098.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-ff71f7905d93af65398419fb34b6cf7e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfffc",
  "name": "_ZN8firebase4auth4User6UnlinkEPKc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04bcee88af278c7d95f4883f60dec7f9f1ad41036382a2cb7255e0e00495407d",
  "source_text_sha256": "04bcee88af278c7d95f4883f60dec7f9f1ad41036382a2cb7255e0e00495407d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfffc",
        "00be01b3"
      ]
    ],
    "bytes_sha256": "e80c4a000ed04b94e6bc869aa303705de3d865e8e1d5eb02bcac045e304a020c",
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

## 疑似コード / UTF-8 3380 bytes

~~~c

void _ZN8firebase4auth4User6UnlinkEPKc(long param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  undefined *puVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00be0000 to 00ce001f has its CatchHandler @ 00be0614 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00be0024 to 00ce0033 has its CatchHandler @ 00be0608 */
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
                    /* try { // try from 00be0050 to 00ce0053 has its CatchHandler @ 00be0760 */
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
              (auStack_68,lVar9,0x15);
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar4 = (**(code **)(*plVar3 + 0x538))(plVar3,param_3);
                    /* try { // try from 00be0080 to 00ce008b has its CatchHandler @ 00be0768 */
    uVar5 = FUN_00497834(plVar3,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126d68,
                         uVar4);
    (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
    uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,lVar9,auStack_68);
    if ((uVar6 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      puVar10 = *(undefined8 **)(param_2 + 0x98);
      uVar4 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar7 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_78);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9ba20
      ;
      *(undefined8 **)(lVar7 + 0x10) = puVar10;
      *(undefined **)(lVar7 + 0x18) = puVar2;
                    /* try { // try from 00be00fc to 00ce0107 has its CatchHandler @ 00be04f4 */
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
        lVar8 = (long)puVar10 + 0x141;
      }
      else {
        lVar8 = puVar10[0x2a];
      }
                    /* try { // try from 00be0144 to 00ce01a3 has its CatchHandler @ 00be060c */
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar4,uVar5,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba00
                 ,lVar7,lVar8);
      _ZN8firebase12FutureHandleD2Ev(auStack_78);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar5);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_68);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
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
<a id="insn-00bdfffc"></a> `00bdfffc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00be0000"></a> `00be0000` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00be0004"></a> `00be0004` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00be0008"></a> `00be0008` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00be000c"></a> `00be000c` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00be0010"></a> `00be0010` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00be0014"></a> `00be0014` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00be0018"></a> `00be0018` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00be001c"></a> `00be001c` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00be0020"></a> `00be0020` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00be0024"></a> `00be0024` | `e9 17 00 f9` | str x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00be0028"></a> `00be0028` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00be002c"></a> `00be002c` | `29 07 00 b4` | cbz x9,0x00be0110 | `CONDITIONAL_JUMP`
<a id="insn-00be0030"></a> `00be0030` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00be0034"></a> `00be0034` | `e8 06 00 b4` | cbz x8,0x00be0110 | `CONDITIONAL_JUMP`
<a id="insn-00be0038"></a> `00be0038` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00be003c"></a> `00be003c` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00be0040"></a> `00be0040` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00be0044"></a> `00be0044` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be0048"></a> `00be0048` | `a1 02 80 52` | mov w1,#0x15 | `FALL_THROUGH`
<a id="insn-00be004c"></a> `00be004c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00be0050"></a> `00be0050` | `ec f6 01 94` | bl 0x00c5dc00 | `UNCONDITIONAL_CALL`
<a id="insn-00be0054"></a> `00be0054` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00be0058"></a> `00be0058` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00be005c"></a> `00be005c` | `09 ec 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00be0060"></a> `00be0060` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00be0064"></a> `00be0064` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00be0068"></a> `00be0068` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00be006c"></a> `00be006c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00be0070"></a> `00be0070` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00be0074"></a> `00be0074` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00be0078"></a> `00be0078` | `29 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00be007c"></a> `00be007c` | `22 b5 46 f9` | ldr x2,[x9, #0xd68] | `FALL_THROUGH`
<a id="insn-00be0080"></a> `00be0080` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00be0084"></a> `00be0084` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00be0088"></a> `00be0088` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00be008c"></a> `00be008c` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00be0090"></a> `00be0090` | `e9 dd e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00be0094"></a> `00be0094` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00be0098"></a> `00be0098` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00be009c"></a> `00be009c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00be00a0"></a> `00be00a0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00be00a4"></a> `00be00a4` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00be00a8"></a> `00be00a8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00be00ac"></a> `00be00ac` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be00b0"></a> `00be00b0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00be00b4"></a> `00be00b4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00be00b8"></a> `00be00b8` | `06 f7 01 94` | bl 0x00c5dcd0 | `UNCONDITIONAL_CALL`
<a id="insn-00be00bc"></a> `00be00bc` | `80 05 00 37` | tbnz w0,#0x0,0x00be016c | `CONDITIONAL_JUMP`
<a id="insn-00be00c0"></a> `00be00c0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00be00c4"></a> `00be00c4` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be00c8"></a> `00be00c8` | `4e eb 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00be00cc"></a> `00be00cc` | `fa 4e 40 f9` | ldr x26,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00be00d0"></a> `00be00d0` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00be00d4"></a> `00be00d4` | `eb eb 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00be00d8"></a> `00be00d8` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00be00dc"></a> `00be00dc` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00be00e0"></a> `00be00e0` | `6c df 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00be00e4"></a> `00be00e4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00be00e8"></a> `00be00e8` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00be00ec"></a> `00be00ec` | `45 eb 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00be00f0"></a> `00be00f0` | `c8 05 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00be00f4"></a> `00be00f4` | `08 11 45 f9` | ldr x8,[x8, #0xa20] | `FALL_THROUGH`
<a id="insn-00be00f8"></a> `00be00f8` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00be00fc"></a> `00be00fc` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00be0100"></a> `00be0100` | `a8 01 00 37` | tbnz w8,#0x0,0x00be0134 | `CONDITIONAL_JUMP`
<a id="insn-00be0104"></a> `00be0104` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00be0108"></a> `00be0108` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00be010c"></a> `00be010c` | `0b 00 00 14` | b 0x00be0138 | `UNCONDITIONAL_JUMP`
<a id="insn-00be0110"></a> `00be0110` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00be0114"></a> `00be0114` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00be0118"></a> `00be0118` | `d6 ea 01 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00be011c"></a> `00be011c` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00be0120"></a> `00be0120` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00be0124"></a> `00be0124` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00be0128"></a> `00be0128` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00be012c"></a> `00be012c` | `ad ea 01 94` | bl 0x00c5abe0 | `UNCONDITIONAL_CALL`
<a id="insn-00be0130"></a> `00be0130` | `15 00 00 14` | b 0x00be0184 | `UNCONDITIONAL_JUMP`
<a id="insn-00be0134"></a> `00be0134` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00be0138"></a> `00be0138` | `c2 05 00 f0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00be013c"></a> `00be013c` | `42 00 45 f9` | ldr x2,[x2, #0xa00] | `FALL_THROUGH`
<a id="insn-00be0140"></a> `00be0140` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00be0144"></a> `00be0144` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00be0148"></a> `00be0148` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00be014c"></a> `00be014c` | `7d eb 01 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00be0150"></a> `00be0150` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00be0154"></a> `00be0154` | `4f ea 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00be0158"></a> `00be0158` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00be015c"></a> `00be015c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00be0160"></a> `00be0160` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00be0164"></a> `00be0164` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00be0168"></a> `00be0168` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00be016c"></a> `00be016c` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be0170"></a> `00be0170` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00be0174"></a> `00be0174` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00be0178"></a> `00be0178` | `ee f6 01 94` | bl 0x00c5dd30 | `UNCONDITIONAL_CALL`
<a id="insn-00be017c"></a> `00be017c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be0180"></a> `00be0180` | `44 ea 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00be0184"></a> `00be0184` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00be0188"></a> `00be0188` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00be018c"></a> `00be018c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00be0190"></a> `00be0190` | `01 01 00 54` | b.ne 0x00be01b0 | `CONDITIONAL_JUMP`
<a id="insn-00be0194"></a> `00be0194` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00be0198"></a> `00be0198` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00be019c"></a> `00be019c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00be01a0"></a> `00be01a0` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00be01a4"></a> `00be01a4` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00be01a8"></a> `00be01a8` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00be01ac"></a> `00be01ac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00be01b0"></a> `00be01b0` | `4c df 01 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfffc`](#insn-00bdfffc) 範囲 `[['00bdfffc', '00bdffff']]`
  - `FALL_THROUGH` [`00bdfffc`](#insn-00bdfffc) → [`00be0000`](#insn-00be0000)
- ブロック [`00be0000`](#insn-00be0000) 範囲 `[['00be0000', '00be0023']]`
  - `FALL_THROUGH` [`00be0020`](#insn-00be0020) → [`00be0024`](#insn-00be0024)
- ブロック [`00be0024`](#insn-00be0024) 範囲 `[['00be0024', '00be002f']]`
  - `CONDITIONAL_JUMP` [`00be002c`](#insn-00be002c) → [`00be0110`](#insn-00be0110)
  - `FALL_THROUGH` [`00be002c`](#insn-00be002c) → [`00be0030`](#insn-00be0030)
- ブロック [`00be0030`](#insn-00be0030) 範囲 `[['00be0030', '00be0037']]`
  - `CONDITIONAL_JUMP` [`00be0034`](#insn-00be0034) → [`00be0110`](#insn-00be0110)
  - `FALL_THROUGH` [`00be0034`](#insn-00be0034) → [`00be0038`](#insn-00be0038)
- ブロック [`00be0038`](#insn-00be0038) 範囲 `[['00be0038', '00be004f']]`
  - `FALL_THROUGH` [`00be004c`](#insn-00be004c) → [`00be0050`](#insn-00be0050)
- ブロック [`00be0050`](#insn-00be0050) 範囲 `[['00be0050', '00be007f']]`
  - `FALL_THROUGH` [`00be007c`](#insn-00be007c) → [`00be0080`](#insn-00be0080)
- ブロック [`00be0080`](#insn-00be0080) 範囲 `[['00be0080', '00be00bf']]`
  - `CONDITIONAL_JUMP` [`00be00bc`](#insn-00be00bc) → [`00be016c`](#insn-00be016c)
  - `FALL_THROUGH` [`00be00bc`](#insn-00be00bc) → [`00be00c0`](#insn-00be00c0)
- ブロック [`00be00c0`](#insn-00be00c0) 範囲 `[['00be00c0', '00be00fb']]`
  - `FALL_THROUGH` [`00be00f8`](#insn-00be00f8) → [`00be00fc`](#insn-00be00fc)
- ブロック [`00be00fc`](#insn-00be00fc) 範囲 `[['00be00fc', '00be0103']]`
  - `CONDITIONAL_JUMP` [`00be0100`](#insn-00be0100) → [`00be0134`](#insn-00be0134)
  - `FALL_THROUGH` [`00be0100`](#insn-00be0100) → [`00be0104`](#insn-00be0104)
- ブロック [`00be0104`](#insn-00be0104) 範囲 `[['00be0104', '00be010f']]`
  - `UNCONDITIONAL_JUMP` [`00be010c`](#insn-00be010c) → [`00be0138`](#insn-00be0138)
- ブロック [`00be0110`](#insn-00be0110) 範囲 `[['00be0110', '00be0133']]`
  - `UNCONDITIONAL_JUMP` [`00be0130`](#insn-00be0130) → [`00be0184`](#insn-00be0184)
- ブロック [`00be0134`](#insn-00be0134) 範囲 `[['00be0134', '00be0137']]`
  - `FALL_THROUGH` [`00be0134`](#insn-00be0134) → [`00be0138`](#insn-00be0138)
- ブロック [`00be0138`](#insn-00be0138) 範囲 `[['00be0138', '00be0143']]`
  - `FALL_THROUGH` [`00be0140`](#insn-00be0140) → [`00be0144`](#insn-00be0144)
- ブロック [`00be0144`](#insn-00be0144) 範囲 `[['00be0144', '00be016b']]`
  - `FALL_THROUGH` [`00be0168`](#insn-00be0168) → [`00be016c`](#insn-00be016c)
- ブロック [`00be016c`](#insn-00be016c) 範囲 `[['00be016c', '00be0183']]`
  - `FALL_THROUGH` [`00be0180`](#insn-00be0180) → [`00be0184`](#insn-00be0184)
- ブロック [`00be0184`](#insn-00be0184) 範囲 `[['00be0184', '00be0193']]`
  - `CONDITIONAL_JUMP` [`00be0190`](#insn-00be0190) → [`00be01b0`](#insn-00be01b0)
  - `FALL_THROUGH` [`00be0190`](#insn-00be0190) → [`00be0194`](#insn-00be0194)
- ブロック [`00be0194`](#insn-00be0194) 範囲 `[['00be0194', '00be01af']]`
- ブロック [`00be01b0`](#insn-00be01b0) 範囲 `[['00be01b0', '00be01b3']]`

## 命令位置別の参照

- [`00be0000`](#insn-00be0000) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0004`](#insn-00be0004) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0008`](#insn-00be0008) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be000c`](#insn-00be000c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0010`](#insn-00be0010) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0024`](#insn-00be0024) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be002c`](#insn-00be002c) → [`00be0110`](#insn-00be0110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0034`](#insn-00be0034) → [`00be0110`](#insn-00be0110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0050`](#insn-00be0050) → [`00c5dc00`](../00c5d/00c5dc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc00` · 推定シンボル `None` · 推定型 `None`
- [`00be005c`](#insn-00be005c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00be007c`](#insn-00be007c) → `01126d68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00be0090`](#insn-00be0090) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00be00b8`](#insn-00be00b8) → [`00c5dcd0`](../00c5d/00c5dcd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dcd0` · 推定シンボル `None` · 推定型 `None`
- [`00be00bc`](#insn-00be00bc) → [`00be016c`](#insn-00be016c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00c8`](#insn-00be00c8) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00be00d4`](#insn-00be00d4) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00be00e0`](#insn-00be00e0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00be00ec`](#insn-00be00ec) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00be00f4`](#insn-00be00f4) → `00c9ba20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00be00f8`](#insn-00be00f8) → [`00bd482c`](../00bd4/00bd482c.md) · `DATA` · `ANALYSIS` · 関数 `00bd482c` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00be0100`](#insn-00be0100) → [`00be0134`](#insn-00be0134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be010c`](#insn-00be010c) → [`00be0138`](#insn-00be0138) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0118`](#insn-00be0118) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00be012c`](#insn-00be012c) → [`00c5abe0`](../00c5a/00c5abe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abe0` · 推定シンボル `None` · 推定型 `None`
- [`00be0130`](#insn-00be0130) → [`00be0184`](#insn-00be0184) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be013c`](#insn-00be013c) → `00c9ba00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00be013c`](#insn-00be013c) → [`00bcfd44`](../00bcf/00bcfd44.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfd44` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00be014c`](#insn-00be014c) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00be0154`](#insn-00be0154) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00be0178`](#insn-00be0178) → [`00c5dd30`](../00c5d/00c5dd30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd30` · 推定シンボル `None` · 推定型 `None`
- [`00be0180`](#insn-00be0180) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00be0188`](#insn-00be0188) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0190`](#insn-00be0190) → [`00be01b0`](#insn-00be01b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0194`](#insn-00be0194) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0198`](#insn-00be0198) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be019c`](#insn-00be019c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01a0`](#insn-00be01a0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01a4`](#insn-00be01a4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01b0`](#insn-00be01b0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00be0000`](#insn-00be0000)

~~~json
{
  "source": "00be0000",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0004`](#insn-00be0004)

~~~json
{
  "source": "00be0004",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0008`](#insn-00be0008)

~~~json
{
  "source": "00be0008",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be000c`](#insn-00be000c)

~~~json
{
  "source": "00be000c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0010`](#insn-00be0010)

~~~json
{
  "source": "00be0010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0024`](#insn-00be0024)

~~~json
{
  "source": "00be0024",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be002c`](#insn-00be002c)

~~~json
{
  "source": "00be002c",
  "target": "00be0110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0034`](#insn-00be0034)

~~~json
{
  "source": "00be0034",
  "target": "00be0110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0050`](#insn-00be0050)

~~~json
{
  "source": "00be0050",
  "target": "00c5dc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be005c`](#insn-00be005c)

~~~json
{
  "source": "00be005c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be007c`](#insn-00be007c)

~~~json
{
  "source": "00be007c",
  "target": "01126d68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00be0090`](#insn-00be0090)

~~~json
{
  "source": "00be0090",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00b8`](#insn-00be00b8)

~~~json
{
  "source": "00be00b8",
  "target": "00c5dcd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00bc`](#insn-00be00bc)

~~~json
{
  "source": "00be00bc",
  "target": "00be016c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00c8`](#insn-00be00c8)

~~~json
{
  "source": "00be00c8",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00d4`](#insn-00be00d4)

~~~json
{
  "source": "00be00d4",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00e0`](#insn-00be00e0)

~~~json
{
  "source": "00be00e0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00ec`](#insn-00be00ec)

~~~json
{
  "source": "00be00ec",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00f4`](#insn-00be00f4)

~~~json
{
  "source": "00be00f4",
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
- 参照命令 [`00be00f8`](#insn-00be00f8)

~~~json
{
  "source": "00be00f8",
  "target": "00bd482c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0100`](#insn-00be0100)

~~~json
{
  "source": "00be0100",
  "target": "00be0134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be010c`](#insn-00be010c)

~~~json
{
  "source": "00be010c",
  "target": "00be0138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0118`](#insn-00be0118)

~~~json
{
  "source": "00be0118",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be012c`](#insn-00be012c)

~~~json
{
  "source": "00be012c",
  "target": "00c5abe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0130`](#insn-00be0130)

~~~json
{
  "source": "00be0130",
  "target": "00be0184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be013c`](#insn-00be013c)

~~~json
{
  "source": "00be013c",
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
- 参照命令 [`00be013c`](#insn-00be013c)

~~~json
{
  "source": "00be013c",
  "target": "00bcfd44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be014c`](#insn-00be014c)

~~~json
{
  "source": "00be014c",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0154`](#insn-00be0154)

~~~json
{
  "source": "00be0154",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0178`](#insn-00be0178)

~~~json
{
  "source": "00be0178",
  "target": "00c5dd30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0180`](#insn-00be0180)

~~~json
{
  "source": "00be0180",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0188`](#insn-00be0188)

~~~json
{
  "source": "00be0188",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0190`](#insn-00be0190)

~~~json
{
  "source": "00be0190",
  "target": "00be01b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0194`](#insn-00be0194)

~~~json
{
  "source": "00be0194",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0198`](#insn-00be0198)

~~~json
{
  "source": "00be0198",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be019c`](#insn-00be019c)

~~~json
{
  "source": "00be019c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01a0`](#insn-00be01a0)

~~~json
{
  "source": "00be01a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01a4`](#insn-00be01a4)

~~~json
{
  "source": "00be01a4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01b0`](#insn-00be01b0)

~~~json
{
  "source": "00be01b0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
