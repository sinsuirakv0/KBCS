# 00bdfe3c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdfda0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfda0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-0853697accafd364dbed3cefb98ef7e1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00be0e30`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0e30.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-a2a22a47993c719609753924199258a0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfe3c",
  "name": "_ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6def15d97b008ef90eee851e5d50a481d6ff3961a187182ff6d6cdc4e3e9cdb0",
  "source_text_sha256": "6def15d97b008ef90eee851e5d50a481d6ff3961a187182ff6d6cdc4e3e9cdb0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfe3c",
        "00bdffc7"
      ]
    ],
    "bytes_sha256": "64ed66cde95cfa3089521134468739aafc5ead1ec35257a3410c38c675344ced",
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

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dda0](../00c5d/00c5dda0.md)
- [00c5de00](../00c5d/00c5de00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3320 bytes

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
  
                    /* try { // try from 00bdfe50 to 00cdfe5b has its CatchHandler @ 00be0804 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
              (auStack_68,lVar9,0x12);
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar4 = FUN_00497874(plVar3,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126e60,
                         *param_3);
                    /* try { // try from 00bdfec0 to 00cdfeef has its CatchHandler @ 00be07a8 */
    uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,lVar9,auStack_68);
    if ((uVar5 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      puVar10 = *(undefined8 **)(param_2 + 0x98);
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar7 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_78);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9baf0
      ;
                    /* try { // try from 00bdff04 to 00cdff0f has its CatchHandler @ 00be07a4 */
      *(undefined8 **)(lVar7 + 0x10) = puVar10;
      *(undefined **)(lVar7 + 0x18) = puVar2;
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
                    /* try { // try from 00bdff1c to 00cdff4f has its CatchHandler @ 00be0590 */
        lVar8 = (long)puVar10 + 0x141;
      }
      else {
        lVar8 = puVar10[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar4,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bad0
                 ,lVar7,lVar8);
      _ZN8firebase12FutureHandleD2Ev(auStack_78);
                    /* try { // try from 00bdff7c to 00cdff87 has its CatchHandler @ 00be07a8 */
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_68);
                    /* try { // try from 00bdff94 to 00cdffc7 has its CatchHandler @ 00be0594 */
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
<a id="insn-00bdfe3c"></a> `00bdfe3c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdfe40"></a> `00bdfe40` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfe44"></a> `00bdfe44` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfe48"></a> `00bdfe48` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfe4c"></a> `00bdfe4c` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdfe50"></a> `00bdfe50` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfe54"></a> `00bdfe54` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bdfe58"></a> `00bdfe58` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdfe5c"></a> `00bdfe5c` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfe60"></a> `00bdfe60` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdfe64"></a> `00bdfe64` | `e9 17 00 f9` | str x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfe68"></a> `00bdfe68` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfe6c"></a> `00bdfe6c` | `c9 05 00 b4` | cbz x9,0x00bdff24 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe70"></a> `00bdfe70` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfe74"></a> `00bdfe74` | `88 05 00 b4` | cbz x8,0x00bdff24 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe78"></a> `00bdfe78` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfe7c"></a> `00bdfe7c` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bdfe80"></a> `00bdfe80` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfe84"></a> `00bdfe84` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfe88"></a> `00bdfe88` | `41 02 80 52` | mov w1,#0x12 | `FALL_THROUGH`
<a id="insn-00bdfe8c"></a> `00bdfe8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdfe90"></a> `00bdfe90` | `90 f7 01 94` | bl 0x00c5dcd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe94"></a> `00bdfe94` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfe98"></a> `00bdfe98` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdfe9c"></a> `00bdfe9c` | `ad ec 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfea0"></a> `00bdfea0` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfea4"></a> `00bdfea4` | `29 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdfea8"></a> `00bdfea8` | `22 31 47 f9` | ldr x2,[x9, #0xe60] | `FALL_THROUGH`
<a id="insn-00bdfeac"></a> `00bdfeac` | `c3 02 40 f9` | ldr x3,[x22] | `FALL_THROUGH`
<a id="insn-00bdfeb0"></a> `00bdfeb0` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfeb4"></a> `00bdfeb4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdfeb8"></a> `00bdfeb8` | `6f de e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfebc"></a> `00bdfebc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdfec0"></a> `00bdfec0` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfec4"></a> `00bdfec4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfec8"></a> `00bdfec8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdfecc"></a> `00bdfecc` | `b5 f7 01 94` | bl 0x00c5dda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfed0"></a> `00bdfed0` | `80 05 00 37` | tbnz w0,#0x0,0x00bdff80 | `CONDITIONAL_JUMP`
<a id="insn-00bdfed4"></a> `00bdfed4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfed8"></a> `00bdfed8` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfedc"></a> `00bdfedc` | `fd eb 01 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfee0"></a> `00bdfee0` | `fa 4e 40 f9` | ldr x26,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfee4"></a> `00bdfee4` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bdfee8"></a> `00bdfee8` | `9a ec 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfeec"></a> `00bdfeec` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfef0"></a> `00bdfef0` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfef4"></a> `00bdfef4` | `1b e0 01 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfef8"></a> `00bdfef8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdfefc"></a> `00bdfefc` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdff00"></a> `00bdff00` | `f4 eb 01 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff04"></a> `00bdff04` | `e8 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdff08"></a> `00bdff08` | `08 79 45 f9` | ldr x8,[x8, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bdff0c"></a> `00bdff0c` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bdff10"></a> `00bdff10` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bdff14"></a> `00bdff14` | `a8 01 00 37` | tbnz w8,#0x0,0x00bdff48 | `CONDITIONAL_JUMP`
<a id="insn-00bdff18"></a> `00bdff18` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bdff1c"></a> `00bdff1c` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdff20"></a> `00bdff20` | `0b 00 00 14` | b 0x00bdff4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdff24"></a> `00bdff24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdff28"></a> `00bdff28` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bdff2c"></a> `00bdff2c` | `85 eb 01 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff30"></a> `00bdff30` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bdff34"></a> `00bdff34` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdff38"></a> `00bdff38` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bdff3c"></a> `00bdff3c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdff40"></a> `00bdff40` | `5c eb 01 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff44"></a> `00bdff44` | `15 00 00 14` | b 0x00bdff98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdff48"></a> `00bdff48` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bdff4c"></a> `00bdff4c` | `e2 05 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdff50"></a> `00bdff50` | `42 68 45 f9` | ldr x2,[x2, #0xad0] | `FALL_THROUGH`
<a id="insn-00bdff54"></a> `00bdff54` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bdff58"></a> `00bdff58` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdff5c"></a> `00bdff5c` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bdff60"></a> `00bdff60` | `2c ec 01 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff64"></a> `00bdff64` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdff68"></a> `00bdff68` | `fe ea 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff6c"></a> `00bdff6c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdff70"></a> `00bdff70` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdff74"></a> `00bdff74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdff78"></a> `00bdff78` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdff7c"></a> `00bdff7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdff80"></a> `00bdff80` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdff84"></a> `00bdff84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdff88"></a> `00bdff88` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdff8c"></a> `00bdff8c` | `9d f7 01 94` | bl 0x00c5de00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff90"></a> `00bdff90` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdff94"></a> `00bdff94` | `f3 ea 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff98"></a> `00bdff98` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdff9c"></a> `00bdff9c` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdffa0"></a> `00bdffa0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdffa4"></a> `00bdffa4` | `01 01 00 54` | b.ne 0x00bdffc4 | `CONDITIONAL_JUMP`
<a id="insn-00bdffa8"></a> `00bdffa8` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdffac"></a> `00bdffac` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdffb0"></a> `00bdffb0` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdffb4"></a> `00bdffb4` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdffb8"></a> `00bdffb8` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdffbc"></a> `00bdffbc` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdffc0"></a> `00bdffc0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdffc4"></a> `00bdffc4` | `fb df 01 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfe3c`](#insn-00bdfe3c) 範囲 `[['00bdfe3c', '00bdfe4f']]`
  - `FALL_THROUGH` [`00bdfe4c`](#insn-00bdfe4c) → [`00bdfe50`](#insn-00bdfe50)
- ブロック [`00bdfe50`](#insn-00bdfe50) 範囲 `[['00bdfe50', '00bdfe6f']]`
  - `CONDITIONAL_JUMP` [`00bdfe6c`](#insn-00bdfe6c) → [`00bdff24`](#insn-00bdff24)
  - `FALL_THROUGH` [`00bdfe6c`](#insn-00bdfe6c) → [`00bdfe70`](#insn-00bdfe70)
- ブロック [`00bdfe70`](#insn-00bdfe70) 範囲 `[['00bdfe70', '00bdfe77']]`
  - `CONDITIONAL_JUMP` [`00bdfe74`](#insn-00bdfe74) → [`00bdff24`](#insn-00bdff24)
  - `FALL_THROUGH` [`00bdfe74`](#insn-00bdfe74) → [`00bdfe78`](#insn-00bdfe78)
- ブロック [`00bdfe78`](#insn-00bdfe78) 範囲 `[['00bdfe78', '00bdfebf']]`
  - `FALL_THROUGH` [`00bdfebc`](#insn-00bdfebc) → [`00bdfec0`](#insn-00bdfec0)
- ブロック [`00bdfec0`](#insn-00bdfec0) 範囲 `[['00bdfec0', '00bdfed3']]`
  - `CONDITIONAL_JUMP` [`00bdfed0`](#insn-00bdfed0) → [`00bdff80`](#insn-00bdff80)
  - `FALL_THROUGH` [`00bdfed0`](#insn-00bdfed0) → [`00bdfed4`](#insn-00bdfed4)
- ブロック [`00bdfed4`](#insn-00bdfed4) 範囲 `[['00bdfed4', '00bdff03']]`
  - `FALL_THROUGH` [`00bdff00`](#insn-00bdff00) → [`00bdff04`](#insn-00bdff04)
- ブロック [`00bdff04`](#insn-00bdff04) 範囲 `[['00bdff04', '00bdff17']]`
  - `CONDITIONAL_JUMP` [`00bdff14`](#insn-00bdff14) → [`00bdff48`](#insn-00bdff48)
  - `FALL_THROUGH` [`00bdff14`](#insn-00bdff14) → [`00bdff18`](#insn-00bdff18)
- ブロック [`00bdff18`](#insn-00bdff18) 範囲 `[['00bdff18', '00bdff1b']]`
  - `FALL_THROUGH` [`00bdff18`](#insn-00bdff18) → [`00bdff1c`](#insn-00bdff1c)
- ブロック [`00bdff1c`](#insn-00bdff1c) 範囲 `[['00bdff1c', '00bdff23']]`
  - `UNCONDITIONAL_JUMP` [`00bdff20`](#insn-00bdff20) → [`00bdff4c`](#insn-00bdff4c)
- ブロック [`00bdff24`](#insn-00bdff24) 範囲 `[['00bdff24', '00bdff47']]`
  - `UNCONDITIONAL_JUMP` [`00bdff44`](#insn-00bdff44) → [`00bdff98`](#insn-00bdff98)
- ブロック [`00bdff48`](#insn-00bdff48) 範囲 `[['00bdff48', '00bdff4b']]`
  - `FALL_THROUGH` [`00bdff48`](#insn-00bdff48) → [`00bdff4c`](#insn-00bdff4c)
- ブロック [`00bdff4c`](#insn-00bdff4c) 範囲 `[['00bdff4c', '00bdff7b']]`
  - `FALL_THROUGH` [`00bdff78`](#insn-00bdff78) → [`00bdff7c`](#insn-00bdff7c)
- ブロック [`00bdff7c`](#insn-00bdff7c) 範囲 `[['00bdff7c', '00bdff7f']]`
  - `FALL_THROUGH` [`00bdff7c`](#insn-00bdff7c) → [`00bdff80`](#insn-00bdff80)
- ブロック [`00bdff80`](#insn-00bdff80) 範囲 `[['00bdff80', '00bdff93']]`
  - `FALL_THROUGH` [`00bdff90`](#insn-00bdff90) → [`00bdff94`](#insn-00bdff94)
- ブロック [`00bdff94`](#insn-00bdff94) 範囲 `[['00bdff94', '00bdff97']]`
  - `FALL_THROUGH` [`00bdff94`](#insn-00bdff94) → [`00bdff98`](#insn-00bdff98)
- ブロック [`00bdff98`](#insn-00bdff98) 範囲 `[['00bdff98', '00bdffa7']]`
  - `CONDITIONAL_JUMP` [`00bdffa4`](#insn-00bdffa4) → [`00bdffc4`](#insn-00bdffc4)
  - `FALL_THROUGH` [`00bdffa4`](#insn-00bdffa4) → [`00bdffa8`](#insn-00bdffa8)
- ブロック [`00bdffa8`](#insn-00bdffa8) 範囲 `[['00bdffa8', '00bdffc3']]`
- ブロック [`00bdffc4`](#insn-00bdffc4) 範囲 `[['00bdffc4', '00bdffc7']]`

## 命令位置別の参照

- [`00bdfe40`](#insn-00bdfe40) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe44`](#insn-00bdfe44) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe48`](#insn-00bdfe48) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe4c`](#insn-00bdfe4c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe50`](#insn-00bdfe50) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe64`](#insn-00bdfe64) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe6c`](#insn-00bdfe6c) → [`00bdff24`](#insn-00bdff24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe74`](#insn-00bdfe74) → [`00bdff24`](#insn-00bdff24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe90`](#insn-00bdfe90) → [`00c5dcd0`](../00c5d/00c5dcd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dcd0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe9c`](#insn-00bdfe9c) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdfea8`](#insn-00bdfea8) → `01126e60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdfeb8`](#insn-00bdfeb8) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bdfecc`](#insn-00bdfecc) → [`00c5dda0`](../00c5d/00c5dda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dda0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfed0`](#insn-00bdfed0) → [`00bdff80`](#insn-00bdff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfedc`](#insn-00bdfedc) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfee8`](#insn-00bdfee8) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdfef4`](#insn-00bdfef4) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bdff00`](#insn-00bdff00) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bdff08`](#insn-00bdff08) → `00c9baf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdff0c`](#insn-00bdff0c) → [`00bd48c8`](../00bd4/00bd48c8.md) · `DATA` · `ANALYSIS` · 関数 `00bd48c8` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bdff14`](#insn-00bdff14) → [`00bdff48`](#insn-00bdff48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff20`](#insn-00bdff20) → [`00bdff4c`](#insn-00bdff4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff2c`](#insn-00bdff2c) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bdff40`](#insn-00bdff40) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdff44`](#insn-00bdff44) → [`00bdff98`](#insn-00bdff98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff50`](#insn-00bdff50) → `00c9bad0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdff50`](#insn-00bdff50) → [`00bcfde0`](../00bcf/00bcfde0.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfde0` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bdff60`](#insn-00bdff60) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bdff68`](#insn-00bdff68) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdff8c`](#insn-00bdff8c) → [`00c5de00`](../00c5d/00c5de00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de00` · 推定シンボル `None` · 推定型 `None`
- [`00bdff94`](#insn-00bdff94) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdff9c`](#insn-00bdff9c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffa4`](#insn-00bdffa4) → [`00bdffc4`](#insn-00bdffc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffa8`](#insn-00bdffa8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffac`](#insn-00bdffac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb0`](#insn-00bdffb0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb4`](#insn-00bdffb4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb8`](#insn-00bdffb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffc4`](#insn-00bdffc4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfe40`](#insn-00bdfe40)

~~~json
{
  "source": "00bdfe40",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe44`](#insn-00bdfe44)

~~~json
{
  "source": "00bdfe44",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe48`](#insn-00bdfe48)

~~~json
{
  "source": "00bdfe48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe4c`](#insn-00bdfe4c)

~~~json
{
  "source": "00bdfe4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe50`](#insn-00bdfe50)

~~~json
{
  "source": "00bdfe50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe64`](#insn-00bdfe64)

~~~json
{
  "source": "00bdfe64",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe6c`](#insn-00bdfe6c)

~~~json
{
  "source": "00bdfe6c",
  "target": "00bdff24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe74`](#insn-00bdfe74)

~~~json
{
  "source": "00bdfe74",
  "target": "00bdff24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe90`](#insn-00bdfe90)

~~~json
{
  "source": "00bdfe90",
  "target": "00c5dcd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe9c`](#insn-00bdfe9c)

~~~json
{
  "source": "00bdfe9c",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfea8`](#insn-00bdfea8)

~~~json
{
  "source": "00bdfea8",
  "target": "01126e60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdfeb8`](#insn-00bdfeb8)

~~~json
{
  "source": "00bdfeb8",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfecc`](#insn-00bdfecc)

~~~json
{
  "source": "00bdfecc",
  "target": "00c5dda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfed0`](#insn-00bdfed0)

~~~json
{
  "source": "00bdfed0",
  "target": "00bdff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfedc`](#insn-00bdfedc)

~~~json
{
  "source": "00bdfedc",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfee8`](#insn-00bdfee8)

~~~json
{
  "source": "00bdfee8",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfef4`](#insn-00bdfef4)

~~~json
{
  "source": "00bdfef4",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff00`](#insn-00bdff00)

~~~json
{
  "source": "00bdff00",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff08`](#insn-00bdff08)

~~~json
{
  "source": "00bdff08",
  "target": "00c9baf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9baf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdff0c`](#insn-00bdff0c)

~~~json
{
  "source": "00bdff0c",
  "target": "00bd48c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff14`](#insn-00bdff14)

~~~json
{
  "source": "00bdff14",
  "target": "00bdff48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff20`](#insn-00bdff20)

~~~json
{
  "source": "00bdff20",
  "target": "00bdff4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff2c`](#insn-00bdff2c)

~~~json
{
  "source": "00bdff2c",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff40`](#insn-00bdff40)

~~~json
{
  "source": "00bdff40",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff44`](#insn-00bdff44)

~~~json
{
  "source": "00bdff44",
  "target": "00bdff98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff50`](#insn-00bdff50)

~~~json
{
  "source": "00bdff50",
  "target": "00c9bad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bad0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdff50`](#insn-00bdff50)

~~~json
{
  "source": "00bdff50",
  "target": "00bcfde0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff60`](#insn-00bdff60)

~~~json
{
  "source": "00bdff60",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff68`](#insn-00bdff68)

~~~json
{
  "source": "00bdff68",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff8c`](#insn-00bdff8c)

~~~json
{
  "source": "00bdff8c",
  "target": "00c5de00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff94`](#insn-00bdff94)

~~~json
{
  "source": "00bdff94",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff9c`](#insn-00bdff9c)

~~~json
{
  "source": "00bdff9c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffa4`](#insn-00bdffa4)

~~~json
{
  "source": "00bdffa4",
  "target": "00bdffc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffa8`](#insn-00bdffa8)

~~~json
{
  "source": "00bdffa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffac`](#insn-00bdffac)

~~~json
{
  "source": "00bdffac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffb0`](#insn-00bdffb0)

~~~json
{
  "source": "00bdffb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffb4`](#insn-00bdffb4)

~~~json
{
  "source": "00bdffb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffb8`](#insn-00bdffb8)

~~~json
{
  "source": "00bdffb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffc4`](#insn-00bdffc4)

~~~json
{
  "source": "00bdffc4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
