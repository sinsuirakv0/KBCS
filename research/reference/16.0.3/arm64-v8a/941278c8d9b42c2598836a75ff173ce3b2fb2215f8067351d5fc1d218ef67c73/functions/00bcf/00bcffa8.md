# 00bcffa8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcefb4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bcefb4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-c22d9223b014f1c70b439eb187a3819f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcffa8",
  "name": "_ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_",
  "size": 568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52f06cb86f2c228da4148eea41ed16fb2f107c68c5f2a20a6e5db5d74d5a6135",
  "source_text_sha256": "52f06cb86f2c228da4148eea41ed16fb2f107c68c5f2a20a6e5db5d74d5a6135",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcffa8",
        "00bd01df"
      ]
    ],
    "bytes_sha256": "28d31f19945c15a9da4b1f12e072913ec0f2b6f9a6b9fb53c3b9f8994dcdd76e",
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

## 疑似コード / UTF-8 3683 bytes

~~~c

void _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_
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
            (auStack_70,lVar1,7);
  if ((((param_3 == (char *)0x0) || (sVar4 = strlen(param_3), param_4 == (char *)0x0)) ||
      (sVar4 == 0)) || (sVar4 = strlen(param_4), sVar4 == 0)) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
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
    uVar8 = FUN_00497b94(plVar5,*(undefined8 *)(*param_2 + 0x1f8),DAT_01127878,uVar6,uVar7);
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
                    /* try { // try from 00bd01dc to 00cd01e3 has its CatchHandler @ 00bd01e4 */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcffa8"></a> `00bcffa8` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcffac"></a> `00bcffac` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcffb0"></a> `00bcffb0` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcffb4"></a> `00bcffb4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcffb8"></a> `00bcffb8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcffbc"></a> `00bcffbc` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcffc0"></a> `00bcffc0` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcffc4"></a> `00bcffc4` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcffc8"></a> `00bcffc8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcffcc"></a> `00bcffcc` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcffd0"></a> `00bcffd0` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcffd4"></a> `00bcffd4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcffd8"></a> `00bcffd8` | `e1 00 80 52` | mov w1,#0x7 | `FALL_THROUGH`
<a id="insn-00bcffdc"></a> `00bcffdc` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcffe0"></a> `00bcffe0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcffe4"></a> `00bcffe4` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bcffe8"></a> `00bcffe8` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcffec"></a> `00bcffec` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfff0"></a> `00bcfff0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcfff4"></a> `00bcfff4` | `2b 3b 02 94` | bl 0x00c5eca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfff8"></a> `00bcfff8` | `77 08 00 b4` | cbz x23,0x00bd0104 | `CONDITIONAL_JUMP`
<a id="insn-00bcfffc"></a> `00bcfffc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd0000"></a> `00bd0000` | `20 24 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0004"></a> `00bd0004` | `18 08 00 b4` | cbz x24,0x00bd0104 | `CONDITIONAL_JUMP`
<a id="insn-00bd0008"></a> `00bd0008` | `e0 07 00 b4` | cbz x0,0x00bd0104 | `CONDITIONAL_JUMP`
<a id="insn-00bd000c"></a> `00bd000c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bd0010"></a> `00bd0010` | `1c 24 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0014"></a> `00bd0014` | `80 07 00 b4` | cbz x0,0x00bd0104 | `CONDITIONAL_JUMP`
<a id="insn-00bd0018"></a> `00bd0018` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bd001c"></a> `00bd001c` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bd0020"></a> `00bd0020` | `40 30 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0024"></a> `00bd0024` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd0028"></a> `00bd0028` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd002c"></a> `00bd002c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bd0030"></a> `00bd0030` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bd0034"></a> `00bd0034` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0038"></a> `00bd0038` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd003c"></a> `00bd003c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bd0040"></a> `00bd0040` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bd0044"></a> `00bd0044` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd0048"></a> `00bd0048` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bd004c"></a> `00bd004c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0050"></a> `00bd0050` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bd0054"></a> `00bd0054` | `a9 2a 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd0058"></a> `00bd0058` | `22 3d 44 f9` | ldr x2,[x9, #0x878] | `FALL_THROUGH`
<a id="insn-00bd005c"></a> `00bd005c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bd0060"></a> `00bd0060` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bd0064"></a> `00bd0064` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd0068"></a> `00bd0068` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00bd006c"></a> `00bd006c` | `e4 03 18 aa` | mov x4,x24 | `FALL_THROUGH`
<a id="insn-00bd0070"></a> `00bd0070` | `c9 1e e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0074"></a> `00bd0074` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd0078"></a> `00bd0078` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bd007c"></a> `00bd007c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd0080"></a> `00bd0080` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd0084"></a> `00bd0084` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bd0088"></a> `00bd0088` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd008c"></a> `00bd008c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd0090"></a> `00bd0090` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd0094"></a> `00bd0094` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd0098"></a> `00bd0098` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bd009c"></a> `00bd009c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd00a0"></a> `00bd00a0` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd00a4"></a> `00bd00a4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd00a8"></a> `00bd00a8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd00ac"></a> `00bd00ac` | `31 3b 02 94` | bl 0x00c5ed70 | `UNCONDITIONAL_CALL`
<a id="insn-00bd00b0"></a> `00bd00b0` | `c0 08 00 37` | tbnz w0,#0x0,0x00bd01c8 | `CONDITIONAL_JUMP`
<a id="insn-00bd00b4"></a> `00bd00b4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bd00b8"></a> `00bd00b8` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd00bc"></a> `00bd00bc` | `79 2f 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd00c0"></a> `00bd00c0` | `d9 02 40 f9` | ldr x25,[x22] | `FALL_THROUGH`
<a id="insn-00bd00c4"></a> `00bd00c4` | `20 03 40 f9` | ldr x0,[x25] | `FALL_THROUGH`
<a id="insn-00bd00c8"></a> `00bd00c8` | `16 30 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bd00cc"></a> `00bd00cc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd00d0"></a> `00bd00d0` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bd00d4"></a> `00bd00d4` | `97 23 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bd00d8"></a> `00bd00d8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bd00dc"></a> `00bd00dc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bd00e0"></a> `00bd00e0` | `70 2f 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd00e4"></a> `00bd00e4` | `68 06 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bd00e8"></a> `00bd00e8` | `08 61 45 f9` | ldr x8,[x8, #0xac0] | `FALL_THROUGH`
<a id="insn-00bd00ec"></a> `00bd00ec` | `19 23 01 a9` | stp x25,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bd00f0"></a> `00bd00f0` | `28 03 45 39` | ldrb w8,[x25, #0x140] | `FALL_THROUGH`
<a id="insn-00bd00f4"></a> `00bd00f4` | `e8 04 00 37` | tbnz w8,#0x0,0x00bd0190 | `CONDITIONAL_JUMP`
<a id="insn-00bd00f8"></a> `00bd00f8` | `28 03 05 91` | add x8,x25,#0x140 | `FALL_THROUGH`
<a id="insn-00bd00fc"></a> `00bd00fc` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd0100"></a> `00bd0100` | `25 00 00 14` | b 0x00bd0194 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd0104"></a> `00bd0104` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0108"></a> `00bd0108` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd010c"></a> `00bd010c` | `65 2f 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0110"></a> `00bd0110` | `b5 04 80 52` | mov w21,#0x25 | `FALL_THROUGH`
<a id="insn-00bd0114"></a> `00bd0114` | `b7 00 00 b4` | cbz x23,0x00bd0128 | `CONDITIONAL_JUMP`
<a id="insn-00bd0118"></a> `00bd0118` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd011c"></a> `00bd011c` | `d9 23 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0120"></a> `00bd0120` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bd0124"></a> `00bd0124` | `b5 06 95 1a` | cinc w21,w21,ne | `FALL_THROUGH`
<a id="insn-00bd0128"></a> `00bd0128` | `e3 b6 ff 90` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bd012c"></a> `00bd012c` | `63 b8 0b 91` | add x3,x3,#0x2ee | `FALL_THROUGH`
<a id="insn-00bd0130"></a> `00bd0130` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0134"></a> `00bd0134` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bd0138"></a> `00bd0138` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd013c"></a> `00bd013c` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bd0140"></a> `00bd0140` | `c8 3a 02 94` | bl 0x00c5ec60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0144"></a> `00bd0144` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0148"></a> `00bd0148` | `7a 2e 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bd014c"></a> `00bd014c` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd0150"></a> `00bd0150` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0154"></a> `00bd0154` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd0158"></a> `00bd0158` | `1e 3b 02 94` | bl 0x00c5edd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd015c"></a> `00bd015c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd0160"></a> `00bd0160` | `74 2e 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0164"></a> `00bd0164` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bd0168"></a> `00bd0168` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bd016c"></a> `00bd016c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bd0170"></a> `00bd0170` | `61 03 00 54` | b.ne 0x00bd01dc | `CONDITIONAL_JUMP`
<a id="insn-00bd0174"></a> `00bd0174` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bd0178"></a> `00bd0178` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bd017c"></a> `00bd017c` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bd0180"></a> `00bd0180` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bd0184"></a> `00bd0184` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bd0188"></a> `00bd0188` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bd018c"></a> `00bd018c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd0190"></a> `00bd0190` | `24 ab 40 f9` | ldr x4,[x25, #0x150] | `FALL_THROUGH`
<a id="insn-00bd0194"></a> `00bd0194` | `62 06 00 90` | adrp x2,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bd0198"></a> `00bd0198` | `42 50 45 f9` | ldr x2,[x2, #0xaa0] | `FALL_THROUGH`
<a id="insn-00bd019c"></a> `00bd019c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bd01a0"></a> `00bd01a0` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bd01a4"></a> `00bd01a4` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bd01a8"></a> `00bd01a8` | `8e 2f 02 94` | bl 0x00c5bfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd01ac"></a> `00bd01ac` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bd01b0"></a> `00bd01b0` | `60 2e 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bd01b4"></a> `00bd01b4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd01b8"></a> `00bd01b8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd01bc"></a> `00bd01bc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd01c0"></a> `00bd01c0` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bd01c4"></a> `00bd01c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd01c8"></a> `00bd01c8` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd01cc"></a> `00bd01cc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd01d0"></a> `00bd01d0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd01d4"></a> `00bd01d4` | `ff 3a 02 94` | bl 0x00c5edd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd01d8"></a> `00bd01d8` | `e1 ff ff 17` | b 0x00bd015c | `UNCONDITIONAL_JUMP`
<a id="insn-00bd01dc"></a> `00bd01dc` | `69 23 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcffa8`](#insn-00bcffa8) 範囲 `[['00bcffa8', '00bcfffb']]`
  - `CONDITIONAL_JUMP` [`00bcfff8`](#insn-00bcfff8) → [`00bd0104`](#insn-00bd0104)
  - `FALL_THROUGH` [`00bcfff8`](#insn-00bcfff8) → [`00bcfffc`](#insn-00bcfffc)
- ブロック [`00bcfffc`](#insn-00bcfffc) 範囲 `[['00bcfffc', '00bd0007']]`
  - `CONDITIONAL_JUMP` [`00bd0004`](#insn-00bd0004) → [`00bd0104`](#insn-00bd0104)
  - `FALL_THROUGH` [`00bd0004`](#insn-00bd0004) → [`00bd0008`](#insn-00bd0008)
- ブロック [`00bd0008`](#insn-00bd0008) 範囲 `[['00bd0008', '00bd000b']]`
  - `CONDITIONAL_JUMP` [`00bd0008`](#insn-00bd0008) → [`00bd0104`](#insn-00bd0104)
  - `FALL_THROUGH` [`00bd0008`](#insn-00bd0008) → [`00bd000c`](#insn-00bd000c)
- ブロック [`00bd000c`](#insn-00bd000c) 範囲 `[['00bd000c', '00bd0017']]`
  - `CONDITIONAL_JUMP` [`00bd0014`](#insn-00bd0014) → [`00bd0104`](#insn-00bd0104)
  - `FALL_THROUGH` [`00bd0014`](#insn-00bd0014) → [`00bd0018`](#insn-00bd0018)
- ブロック [`00bd0018`](#insn-00bd0018) 範囲 `[['00bd0018', '00bd00b3']]`
  - `CONDITIONAL_JUMP` [`00bd00b0`](#insn-00bd00b0) → [`00bd01c8`](#insn-00bd01c8)
  - `FALL_THROUGH` [`00bd00b0`](#insn-00bd00b0) → [`00bd00b4`](#insn-00bd00b4)
- ブロック [`00bd00b4`](#insn-00bd00b4) 範囲 `[['00bd00b4', '00bd00f7']]`
  - `CONDITIONAL_JUMP` [`00bd00f4`](#insn-00bd00f4) → [`00bd0190`](#insn-00bd0190)
  - `FALL_THROUGH` [`00bd00f4`](#insn-00bd00f4) → [`00bd00f8`](#insn-00bd00f8)
- ブロック [`00bd00f8`](#insn-00bd00f8) 範囲 `[['00bd00f8', '00bd0103']]`
  - `UNCONDITIONAL_JUMP` [`00bd0100`](#insn-00bd0100) → [`00bd0194`](#insn-00bd0194)
- ブロック [`00bd0104`](#insn-00bd0104) 範囲 `[['00bd0104', '00bd0117']]`
  - `CONDITIONAL_JUMP` [`00bd0114`](#insn-00bd0114) → [`00bd0128`](#insn-00bd0128)
  - `FALL_THROUGH` [`00bd0114`](#insn-00bd0114) → [`00bd0118`](#insn-00bd0118)
- ブロック [`00bd0118`](#insn-00bd0118) 範囲 `[['00bd0118', '00bd0127']]`
  - `FALL_THROUGH` [`00bd0124`](#insn-00bd0124) → [`00bd0128`](#insn-00bd0128)
- ブロック [`00bd0128`](#insn-00bd0128) 範囲 `[['00bd0128', '00bd015b']]`
  - `FALL_THROUGH` [`00bd0158`](#insn-00bd0158) → [`00bd015c`](#insn-00bd015c)
- ブロック [`00bd015c`](#insn-00bd015c) 範囲 `[['00bd015c', '00bd0173']]`
  - `CONDITIONAL_JUMP` [`00bd0170`](#insn-00bd0170) → [`00bd01dc`](#insn-00bd01dc)
  - `FALL_THROUGH` [`00bd0170`](#insn-00bd0170) → [`00bd0174`](#insn-00bd0174)
- ブロック [`00bd0174`](#insn-00bd0174) 範囲 `[['00bd0174', '00bd018f']]`
- ブロック [`00bd0190`](#insn-00bd0190) 範囲 `[['00bd0190', '00bd0193']]`
  - `FALL_THROUGH` [`00bd0190`](#insn-00bd0190) → [`00bd0194`](#insn-00bd0194)
- ブロック [`00bd0194`](#insn-00bd0194) 範囲 `[['00bd0194', '00bd01c7']]`
  - `FALL_THROUGH` [`00bd01c4`](#insn-00bd01c4) → [`00bd01c8`](#insn-00bd01c8)
- ブロック [`00bd01c8`](#insn-00bd01c8) 範囲 `[['00bd01c8', '00bd01db']]`
  - `UNCONDITIONAL_JUMP` [`00bd01d8`](#insn-00bd01d8) → [`00bd015c`](#insn-00bd015c)
- ブロック [`00bd01dc`](#insn-00bd01dc) 範囲 `[['00bd01dc', '00bd01df']]`

## 命令位置別の参照

- [`00bcffac`](#insn-00bcffac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffb0`](#insn-00bcffb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffb4`](#insn-00bcffb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffb8`](#insn-00bcffb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffbc`](#insn-00bcffbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffdc`](#insn-00bcffdc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfff4`](#insn-00bcfff4) → [`00c5eca0`](../00c5e/00c5eca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eca0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfff8`](#insn-00bcfff8) → [`00bd0104`](#insn-00bd0104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0000`](#insn-00bd0000) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bd0004`](#insn-00bd0004) → [`00bd0104`](#insn-00bd0104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0008`](#insn-00bd0008) → [`00bd0104`](#insn-00bd0104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0010`](#insn-00bd0010) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bd0014`](#insn-00bd0014) → [`00bd0104`](#insn-00bd0104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0020`](#insn-00bd0020) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bd0058`](#insn-00bd0058) → `01127878`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0070`](#insn-00bd0070) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bd00ac`](#insn-00bd00ac) → [`00c5ed70`](../00c5e/00c5ed70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ed70` · 推定シンボル `None` · 推定型 `None`
- [`00bd00b0`](#insn-00bd00b0) → [`00bd01c8`](#insn-00bd01c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd00bc`](#insn-00bd00bc) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bd00c8`](#insn-00bd00c8) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bd00d4`](#insn-00bd00d4) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bd00e0`](#insn-00bd00e0) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bd00e8`](#insn-00bd00e8) → `00c9cac0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bd00ec`](#insn-00bd00ec) → [`00bd58bc`](../00bd5/00bd58bc.md) · `DATA` · `ANALYSIS` · 関数 `00bd58bc` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bd00f4`](#insn-00bd00f4) → [`00bd0190`](#insn-00bd0190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0100`](#insn-00bd0100) → [`00bd0194`](#insn-00bd0194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd010c`](#insn-00bd010c) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bd0114`](#insn-00bd0114) → [`00bd0128`](#insn-00bd0128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd011c`](#insn-00bd011c) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bd012c`](#insn-00bd012c) → `002ac2ee`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd0140`](#insn-00bd0140) → [`00c5ec60`](../00c5e/00c5ec60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ec60` · 推定シンボル `None` · 推定型 `None`
- [`00bd0148`](#insn-00bd0148) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bd0158`](#insn-00bd0158) → [`00c5edd0`](../00c5e/00c5edd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5edd0` · 推定シンボル `None` · 推定型 `None`
- [`00bd0160`](#insn-00bd0160) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bd0168`](#insn-00bd0168) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0170`](#insn-00bd0170) → [`00bd01dc`](#insn-00bd01dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0174`](#insn-00bd0174) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0178`](#insn-00bd0178) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd017c`](#insn-00bd017c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0180`](#insn-00bd0180) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0184`](#insn-00bd0184) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0198`](#insn-00bd0198) → `00c9caa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bd0198`](#insn-00bd0198) → [`00bd0dd4`](../00bd0/00bd0dd4.md) · `PARAM` · `ANALYSIS` · 関数 `00bd0dd4` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bd01a8`](#insn-00bd01a8) → [`00c5bfe0`](../00c5b/00c5bfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bd01b0`](#insn-00bd01b0) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bd01d4`](#insn-00bd01d4) → [`00c5edd0`](../00c5e/00c5edd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5edd0` · 推定シンボル `None` · 推定型 `None`
- [`00bd01d8`](#insn-00bd01d8) → [`00bd015c`](#insn-00bd015c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd01dc`](#insn-00bd01dc) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcffac`](#insn-00bcffac)

~~~json
{
  "source": "00bcffac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffb0`](#insn-00bcffb0)

~~~json
{
  "source": "00bcffb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffb4`](#insn-00bcffb4)

~~~json
{
  "source": "00bcffb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffb8`](#insn-00bcffb8)

~~~json
{
  "source": "00bcffb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffbc`](#insn-00bcffbc)

~~~json
{
  "source": "00bcffbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffdc`](#insn-00bcffdc)

~~~json
{
  "source": "00bcffdc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfff4`](#insn-00bcfff4)

~~~json
{
  "source": "00bcfff4",
  "target": "00c5eca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfff8`](#insn-00bcfff8)

~~~json
{
  "source": "00bcfff8",
  "target": "00bd0104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0000`](#insn-00bd0000)

~~~json
{
  "source": "00bd0000",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0004`](#insn-00bd0004)

~~~json
{
  "source": "00bd0004",
  "target": "00bd0104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0008`](#insn-00bd0008)

~~~json
{
  "source": "00bd0008",
  "target": "00bd0104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0010`](#insn-00bd0010)

~~~json
{
  "source": "00bd0010",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0014`](#insn-00bd0014)

~~~json
{
  "source": "00bd0014",
  "target": "00bd0104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0020`](#insn-00bd0020)

~~~json
{
  "source": "00bd0020",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0058`](#insn-00bd0058)

~~~json
{
  "source": "00bd0058",
  "target": "01127878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127878",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0070`](#insn-00bd0070)

~~~json
{
  "source": "00bd0070",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd00ac`](#insn-00bd00ac)

~~~json
{
  "source": "00bd00ac",
  "target": "00c5ed70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd00b0`](#insn-00bd00b0)

~~~json
{
  "source": "00bd00b0",
  "target": "00bd01c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd00bc`](#insn-00bd00bc)

~~~json
{
  "source": "00bd00bc",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd00c8`](#insn-00bd00c8)

~~~json
{
  "source": "00bd00c8",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd00d4`](#insn-00bd00d4)

~~~json
{
  "source": "00bd00d4",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd00e0`](#insn-00bd00e0)

~~~json
{
  "source": "00bd00e0",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd00e8`](#insn-00bd00e8)

~~~json
{
  "source": "00bd00e8",
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
- 参照命令 [`00bd00ec`](#insn-00bd00ec)

~~~json
{
  "source": "00bd00ec",
  "target": "00bd58bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd00f4`](#insn-00bd00f4)

~~~json
{
  "source": "00bd00f4",
  "target": "00bd0190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0100`](#insn-00bd0100)

~~~json
{
  "source": "00bd0100",
  "target": "00bd0194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd010c`](#insn-00bd010c)

~~~json
{
  "source": "00bd010c",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0114`](#insn-00bd0114)

~~~json
{
  "source": "00bd0114",
  "target": "00bd0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd011c`](#insn-00bd011c)

~~~json
{
  "source": "00bd011c",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd012c`](#insn-00bd012c)

~~~json
{
  "source": "00bd012c",
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
- 参照命令 [`00bd0140`](#insn-00bd0140)

~~~json
{
  "source": "00bd0140",
  "target": "00c5ec60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0148`](#insn-00bd0148)

~~~json
{
  "source": "00bd0148",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0158`](#insn-00bd0158)

~~~json
{
  "source": "00bd0158",
  "target": "00c5edd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0160`](#insn-00bd0160)

~~~json
{
  "source": "00bd0160",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0168`](#insn-00bd0168)

~~~json
{
  "source": "00bd0168",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0170`](#insn-00bd0170)

~~~json
{
  "source": "00bd0170",
  "target": "00bd01dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0174`](#insn-00bd0174)

~~~json
{
  "source": "00bd0174",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0178`](#insn-00bd0178)

~~~json
{
  "source": "00bd0178",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd017c`](#insn-00bd017c)

~~~json
{
  "source": "00bd017c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0180`](#insn-00bd0180)

~~~json
{
  "source": "00bd0180",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0184`](#insn-00bd0184)

~~~json
{
  "source": "00bd0184",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0198`](#insn-00bd0198)

~~~json
{
  "source": "00bd0198",
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
- 参照命令 [`00bd0198`](#insn-00bd0198)

~~~json
{
  "source": "00bd0198",
  "target": "00bd0dd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd01a8`](#insn-00bd01a8)

~~~json
{
  "source": "00bd01a8",
  "target": "00c5bfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd01b0`](#insn-00bd01b0)

~~~json
{
  "source": "00bd01b0",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd01d4`](#insn-00bd01d4)

~~~json
{
  "source": "00bd01d4",
  "target": "00c5edd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd01d8`](#insn-00bd01d8)

~~~json
{
  "source": "00bd01d8",
  "target": "00bd015c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd01dc`](#insn-00bd01dc)

~~~json
{
  "source": "00bd01dc",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
