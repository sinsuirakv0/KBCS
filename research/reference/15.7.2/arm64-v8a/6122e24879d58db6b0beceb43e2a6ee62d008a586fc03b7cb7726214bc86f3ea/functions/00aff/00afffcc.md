# 00afffcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b00094`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00094.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-3f32cd5435abb5c015fbfe3b002ac7a1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afffcc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl27AddCompletionCallbackLambdaERKNS_12FutureHandleENSt6__ndk18functionIFvRKNS_10FutureBaseEEEEb",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "746b748ed254e012116856fbe5849263c3db6c24d568d68ab2f8648a82481a72",
  "source_text_sha256": "746b748ed254e012116856fbe5849263c3db6c24d568d68ab2f8648a82481a72",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afffcc",
        "00b001db"
      ]
    ],
    "bytes_sha256": "f0dfea336a8b479db1799e467c77290dd2e264f73d13a06a95e6cde3a38b9d08",
    "instruction_count": 132,
    "instruction_bytes": 528,
    "body_bytes": 528,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddf10](../00bdd/00bddf10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4774 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl27AddCompletionCallbackLambdaERKNS_12FutureHandleENSt6__ndk18functionIFvRKNS_10FutureBaseEEEEb
               (long *param_1,long param_2,ulong *param_3,long *param_4,uint param_5)

{
  undefined8 *puVar1;
  long *__ptr;
  long lVar2;
  undefined8 uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  ulong uVar8;
  int *piVar9;
  long lVar10;
  
                    /* catch() { ... } // from try @ 00af5d04 with catch @ 00afffd8 */
  __ptr = (long *)_Znwm(0x28);
  lVar2 = _Znwm(0x30);
  plVar5 = (long *)param_4[4];
  if (plVar5 == (long *)0x0) {
    *(undefined8 *)(lVar2 + 0x20) = 0;
  }
  else {
                    /* catch() { ... } // from try @ 00af5a38 with catch @ 00b0001c */
    if (param_4 == plVar5) {
      *(long *)(lVar2 + 0x20) = lVar2;
      (**(code **)(*plVar5 + 0x18))(plVar5,lVar2);
    }
    else {
      uVar3 = (**(code **)(*plVar5 + 0x10))(plVar5);
      *(undefined8 *)(lVar2 + 0x20) = uVar3;
    }
  }
                    /* catch() { ... } // from try @ 00af60f0 with catch @ 00b00060 */
  __ptr[2] = (long)FUN_00b001dc;
  __ptr[3] = lVar2;
  lVar2 = param_2 + 8;
                    /* catch() { ... } // from try @ 00af5b5c with catch @ 00b00070 */
  *__ptr = (long)__ptr;
  __ptr[1] = (long)__ptr;
  __ptr[4] = (long)FUN_00b00214;
  _ZN8firebase5Mutex7AcquireEv(lVar2);
  uVar8 = *param_3;
  _ZN8firebase5Mutex7AcquireEv(lVar2);
  plVar6 = (long *)(param_2 + 0x38);
  plVar7 = (long *)*plVar6;
  plVar5 = plVar6;
  if (plVar7 == (long *)0x0) {
LAB_00b000c8:
    _ZN8firebase5Mutex7ReleaseEv(lVar2);
  }
  else {
    do {
      if ((ulong)plVar7[4] >= uVar8) {
        plVar5 = plVar7;
      }
      plVar7 = (long *)plVar7[(ulong)plVar7[4] < uVar8];
    } while (plVar7 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5730 with catch @ 00b000b4 */
    if ((plVar5 == plVar6) || (uVar8 < (ulong)plVar5[4])) goto LAB_00b000c8;
    piVar9 = (int *)plVar5[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar2);
    if (piVar9 != (int *)0x0) {
      if ((param_5 & 1) == 0) {
        puVar1 = *(undefined8 **)(piVar9 + 0x16);
                    /* catch() { ... } // from try @ 00af566c with catch @ 00b0017c */
        plVar5 = (long *)((long)__ptr + *(long *)(piVar9 + 0x18));
        piVar9[8] = piVar9[8] + 1;
        *puVar1 = plVar5;
        *plVar5 = (long)(piVar9 + 0x14);
        plVar5[1] = (long)puVar1;
        *(long **)(piVar9 + 0x16) = plVar5;
        iVar4 = *piVar9;
      }
      else {
        plVar5 = *(long **)(piVar9 + 0x12);
        if (plVar5 == (long *)0x0) {
          iVar4 = piVar9[8];
        }
        else {
          if ((code *)plVar5[4] == (code *)0x0) {
LAB_00b00144:
            lVar10 = *plVar5;
            *(long *)(lVar10 + 8) = plVar5[1];
                    /* catch() { ... } // from try @ 00af56cc with catch @ 00b0014c */
            *(long *)plVar5[1] = lVar10;
            _ZdlPv(plVar5);
          }
          else {
            (*(code *)plVar5[4])(plVar5[3]);
                    /* catch() { ... } // from try @ 00afd330 with catch @ 00b0013c */
            plVar5 = *(long **)(piVar9 + 0x12);
            if (plVar5 != (long *)0x0) goto LAB_00b00144;
          }
          piVar9[0x12] = 0;
          piVar9[0x13] = 0;
          iVar4 = piVar9[8] + -1;
          piVar9[8] = iVar4;
        }
        piVar9[8] = iVar4 + 1;
        *(long **)(piVar9 + 0x12) = __ptr;
        iVar4 = *piVar9;
      }
      if (iVar4 != 0) {
        _ZN8firebase5Mutex7ReleaseEv(lVar2);
        lVar10 = __ptr[2];
        lVar2 = __ptr[4];
        param_1[1] = __ptr[3];
        *param_1 = lVar10;
                    /* catch() { ... } // from try @ 00af575c with catch @ 00b001ac */
        param_1[2] = lVar2;
        return;
      }
                    /* catch() { ... } // from try @ 00afb528 with catch @ 00b001d4 */
      _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
                (param_2,param_3);
      goto LAB_00b000f0;
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar2);
  lVar2 = *__ptr;
  *(long *)(lVar2 + 8) = __ptr[1];
                    /* catch() { ... } // from try @ 00afd224 with catch @ 00b000e4 */
                    /* catch() { ... } // from try @ 00afba5c with catch @ 00b000e8 */
  *(long *)__ptr[1] = lVar2;
                    /* catch() { ... } // from try @ 00afb594 with catch @ 00b000ec */
  _ZdlPv(__ptr);
LAB_00b000f0:
                    /* catch() { ... } // from try @ 00afa7f8 with catch @ 00b000f0 */
  *param_1 = 0;
  param_1[1] = 0;
                    /* catch() { ... } // from try @ 00af8d44 with catch @ 00b000f4 */
  param_1[2] = 0;
                    /* catch() { ... } // from try @ 00af5a6c with catch @ 00b000f8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afffcc"></a> `00afffcc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afffd0"></a> `00afffd0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afffd4"></a> `00afffd4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afffd8"></a> `00afffd8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afffdc"></a> `00afffdc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afffe0"></a> `00afffe0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afffe4"></a> `00afffe4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00afffe8"></a> `00afffe8` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00afffec"></a> `00afffec` | `f8 03 03 2a` | mov w24,w3 | `FALL_THROUGH`
<a id="insn-00affff0"></a> `00affff0` | `f9 03 02 aa` | mov x25,x2 | `FALL_THROUGH`
<a id="insn-00affff4"></a> `00affff4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affff8"></a> `00affff8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00affffc"></a> `00affffc` | `d1 6b 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b00000"></a> `00b00000` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b00004"></a> `00b00004` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00b00008"></a> `00b00008` | `ce 6b 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b0000c"></a> `00b0000c` | `28 13 40 f9` | ldr x8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00b00010"></a> `00b00010` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b00014"></a> `00b00014` | `28 01 00 b4` | cbz x8,0x00b00038 | `CONDITIONAL_JUMP`
<a id="insn-00b00018"></a> `00b00018` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00b0001c"></a> `00b0001c` | `20 01 00 54` | b.eq 0x00b00040 | `CONDITIONAL_JUMP`
<a id="insn-00b00020"></a> `00b00020` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b00024"></a> `00b00024` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b00028"></a> `00b00028` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b0002c"></a> `00b0002c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b00030"></a> `00b00030` | `e0 12 00 f9` | str x0,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00b00034"></a> `00b00034` | `09 00 00 14` | b 0x00b00058 | `UNCONDITIONAL_JUMP`
<a id="insn-00b00038"></a> `00b00038` | `ff 12 00 f9` | str xzr,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00b0003c"></a> `00b0003c` | `07 00 00 14` | b 0x00b00058 | `UNCONDITIONAL_JUMP`
<a id="insn-00b00040"></a> `00b00040` | `f7 12 00 f9` | str x23,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00b00044"></a> `00b00044` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b00048"></a> `00b00048` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b0004c"></a> `00b0004c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b00050"></a> `00b00050` | `29 0d 40 f9` | ldr x9,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00b00054"></a> `00b00054` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b00058"></a> `00b00058` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00b0005c"></a> `00b0005c` | `08 0c 00 10` | adr x8,0xb001dc | `FALL_THROUGH`
<a id="insn-00b00060"></a> `00b00060` | `09 00 00 90` | adrp x9,0xb00000 | `FALL_THROUGH`
<a id="insn-00b00064"></a> `00b00064` | `88 5e 01 a9` | stp x8,x23,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b00068"></a> `00b00068` | `d7 22 00 91` | add x23,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00b0006c"></a> `00b0006c` | `29 51 08 91` | add x9,x9,#0x214 | `FALL_THROUGH`
<a id="insn-00b00070"></a> `00b00070` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b00074"></a> `00b00074` | `94 52 00 a9` | stp x20,x20,[x20] | `FALL_THROUGH`
<a id="insn-00b00078"></a> `00b00078` | `89 12 00 f9` | str x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b0007c"></a> `00b0007c` | `a9 76 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00b00080"></a> `00b00080` | `b9 02 40 f9` | ldr x25,[x21] | `FALL_THROUGH`
<a id="insn-00b00084"></a> `00b00084` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b00088"></a> `00b00088` | `a6 76 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00b0008c"></a> `00b0008c` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00b00090"></a> `00b00090` | `2a 8d 43 f8` | ldr x10,[x9, #0x38]! | `FALL_THROUGH`
<a id="insn-00b00094"></a> `00b00094` | `aa 01 00 b4` | cbz x10,0x00b000c8 | `CONDITIONAL_JUMP`
<a id="insn-00b00098"></a> `00b00098` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00b0009c"></a> `00b0009c` | `4b 11 40 f9` | ldr x11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00b000a0"></a> `00b000a0` | `7f 01 19 eb` | cmp x11,x25 | `FALL_THROUGH`
<a id="insn-00b000a4"></a> `00b000a4` | `eb 27 9f 1a` | cset w11,cc | `FALL_THROUGH`
<a id="insn-00b000a8"></a> `00b000a8` | `08 31 8a 9a` | csel x8,x8,x10,cc | `FALL_THROUGH`
<a id="insn-00b000ac"></a> `00b000ac` | `4a 59 6b f8` | ldr x10,[x10, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b000b0"></a> `00b000b0` | `6a ff ff b5` | cbnz x10,0x00b0009c | `CONDITIONAL_JUMP`
<a id="insn-00b000b4"></a> `00b000b4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b000b8"></a> `00b000b8` | `80 00 00 54` | b.eq 0x00b000c8 | `CONDITIONAL_JUMP`
<a id="insn-00b000bc"></a> `00b000bc` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b000c0"></a> `00b000c0` | `3f 01 19 eb` | cmp x9,x25 | `FALL_THROUGH`
<a id="insn-00b000c4"></a> `00b000c4` | `69 02 00 54` | b.ls 0x00b00110 | `CONDITIONAL_JUMP`
<a id="insn-00b000c8"></a> `00b000c8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b000cc"></a> `00b000cc` | `99 76 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b000d0"></a> `00b000d0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b000d4"></a> `00b000d4` | `97 76 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b000d8"></a> `00b000d8` | `88 26 40 a9` | ldp x8,x9,[x20] | `FALL_THROUGH`
<a id="insn-00b000dc"></a> `00b000dc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b000e0"></a> `00b000e0` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b000e4"></a> `00b000e4` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b000e8"></a> `00b000e8` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b000ec"></a> `00b000ec` | `9d 6b 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b000f0"></a> `00b000f0` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b000f4"></a> `00b000f4` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b000f8"></a> `00b000f8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b000fc"></a> `00b000fc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b00100"></a> `00b00100` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b00104"></a> `00b00104` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b00108"></a> `00b00108` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b0010c"></a> `00b0010c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b00110"></a> `00b00110` | `19 15 40 f9` | ldr x25,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00b00114"></a> `00b00114` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b00118"></a> `00b00118` | `86 76 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b0011c"></a> `00b0011c` | `b9 fd ff b4` | cbz x25,0x00b000d0 | `CONDITIONAL_JUMP`
<a id="insn-00b00120"></a> `00b00120` | `78 02 00 36` | tbz w24,#0x0,0x00b0016c | `CONDITIONAL_JUMP`
<a id="insn-00b00124"></a> `00b00124` | `20 27 40 f9` | ldr x0,[x25, #0x48] | `FALL_THROUGH`
<a id="insn-00b00128"></a> `00b00128` | `60 04 00 b4` | cbz x0,0x00b001b4 | `CONDITIONAL_JUMP`
<a id="insn-00b0012c"></a> `00b0012c` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b00130"></a> `00b00130` | `a8 00 00 b4` | cbz x8,0x00b00144 | `CONDITIONAL_JUMP`
<a id="insn-00b00134"></a> `00b00134` | `00 0c 40 f9` | ldr x0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00b00138"></a> `00b00138` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b0013c"></a> `00b0013c` | `20 27 40 f9` | ldr x0,[x25, #0x48] | `FALL_THROUGH`
<a id="insn-00b00140"></a> `00b00140` | `c0 00 00 b4` | cbz x0,0x00b00158 | `CONDITIONAL_JUMP`
<a id="insn-00b00144"></a> `00b00144` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00b00148"></a> `00b00148` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b0014c"></a> `00b0014c` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b00150"></a> `00b00150` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b00154"></a> `00b00154` | `83 6b 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b00158"></a> `00b00158` | `28 23 40 b9` | ldr w8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00b0015c"></a> `00b0015c` | `3f 27 00 f9` | str xzr,[x25, #0x48] | `FALL_THROUGH`
<a id="insn-00b00160"></a> `00b00160` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b00164"></a> `00b00164` | `28 23 00 b9` | str w8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00b00168"></a> `00b00168` | `14 00 00 14` | b 0x00b001b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0016c"></a> `00b0016c` | `28 23 40 b9` | ldr w8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00b00170"></a> `00b00170` | `2a a7 45 a9` | ldp x10,x9,[x25, #0x58] | `FALL_THROUGH`
<a id="insn-00b00174"></a> `00b00174` | `2b 43 01 91` | add x11,x25,#0x50 | `FALL_THROUGH`
<a id="insn-00b00178"></a> `00b00178` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0017c"></a> `00b0017c` | `89 02 09 8b` | add x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00b00180"></a> `00b00180` | `28 23 00 b9` | str w8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00b00184"></a> `00b00184` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00b00188"></a> `00b00188` | `2b 29 00 a9` | stp x11,x10,[x9] | `FALL_THROUGH`
<a id="insn-00b0018c"></a> `00b0018c` | `29 2f 00 f9` | str x9,[x25, #0x58] | `FALL_THROUGH`
<a id="insn-00b00190"></a> `00b00190` | `28 03 40 b9` | ldr w8,[x25] | `FALL_THROUGH`
<a id="insn-00b00194"></a> `00b00194` | `c8 01 00 34` | cbz w8,0x00b001cc | `CONDITIONAL_JUMP`
<a id="insn-00b00198"></a> `00b00198` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b0019c"></a> `00b0019c` | `65 76 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b001a0"></a> `00b001a0` | `80 06 c0 3d` | ldr q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b001a4"></a> `00b001a4` | `88 12 40 f9` | ldr x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b001a8"></a> `00b001a8` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00b001ac"></a> `00b001ac` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b001b0"></a> `00b001b0` | `d2 ff ff 17` | b 0x00b000f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b001b4"></a> `00b001b4` | `28 23 40 b9` | ldr w8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00b001b8"></a> `00b001b8` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b001bc"></a> `00b001bc` | `28 23 00 b9` | str w8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00b001c0"></a> `00b001c0` | `34 27 00 f9` | str x20,[x25, #0x48] | `FALL_THROUGH`
<a id="insn-00b001c4"></a> `00b001c4` | `28 03 40 b9` | ldr w8,[x25] | `FALL_THROUGH`
<a id="insn-00b001c8"></a> `00b001c8` | `88 fe ff 35` | cbnz w8,0x00b00198 | `CONDITIONAL_JUMP`
<a id="insn-00b001cc"></a> `00b001cc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b001d0"></a> `00b001d0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b001d4"></a> `00b001d4` | `4f 77 03 94` | bl 0x00bddf10 | `UNCONDITIONAL_CALL`
<a id="insn-00b001d8"></a> `00b001d8` | `c6 ff ff 17` | b 0x00b000f0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afffcc`](#insn-00afffcc) 範囲 `[['00afffcc', '00afffd7']]`
  - `FALL_THROUGH` [`00afffd4`](#insn-00afffd4) → [`00afffd8`](#insn-00afffd8)
- ブロック [`00afffd8`](#insn-00afffd8) 範囲 `[['00afffd8', '00b00017']]`
  - `CONDITIONAL_JUMP` [`00b00014`](#insn-00b00014) → [`00b00038`](#insn-00b00038)
  - `FALL_THROUGH` [`00b00014`](#insn-00b00014) → [`00b00018`](#insn-00b00018)
- ブロック [`00b00018`](#insn-00b00018) 範囲 `[['00b00018', '00b0001b']]`
  - `FALL_THROUGH` [`00b00018`](#insn-00b00018) → [`00b0001c`](#insn-00b0001c)
- ブロック [`00b0001c`](#insn-00b0001c) 範囲 `[['00b0001c', '00b0001f']]`
  - `CONDITIONAL_JUMP` [`00b0001c`](#insn-00b0001c) → [`00b00040`](#insn-00b00040)
  - `FALL_THROUGH` [`00b0001c`](#insn-00b0001c) → [`00b00020`](#insn-00b00020)
- ブロック [`00b00020`](#insn-00b00020) 範囲 `[['00b00020', '00b00037']]`
  - `UNCONDITIONAL_JUMP` [`00b00034`](#insn-00b00034) → [`00b00058`](#insn-00b00058)
- ブロック [`00b00038`](#insn-00b00038) 範囲 `[['00b00038', '00b0003f']]`
  - `UNCONDITIONAL_JUMP` [`00b0003c`](#insn-00b0003c) → [`00b00058`](#insn-00b00058)
- ブロック [`00b00040`](#insn-00b00040) 範囲 `[['00b00040', '00b00057']]`
  - `FALL_THROUGH` [`00b00054`](#insn-00b00054) → [`00b00058`](#insn-00b00058)
- ブロック [`00b00058`](#insn-00b00058) 範囲 `[['00b00058', '00b0005f']]`
  - `FALL_THROUGH` [`00b0005c`](#insn-00b0005c) → [`00b00060`](#insn-00b00060)
- ブロック [`00b00060`](#insn-00b00060) 範囲 `[['00b00060', '00b0006f']]`
  - `FALL_THROUGH` [`00b0006c`](#insn-00b0006c) → [`00b00070`](#insn-00b00070)
- ブロック [`00b00070`](#insn-00b00070) 範囲 `[['00b00070', '00b00097']]`
  - `CONDITIONAL_JUMP` [`00b00094`](#insn-00b00094) → [`00b000c8`](#insn-00b000c8)
  - `FALL_THROUGH` [`00b00094`](#insn-00b00094) → [`00b00098`](#insn-00b00098)
- ブロック [`00b00098`](#insn-00b00098) 範囲 `[['00b00098', '00b0009b']]`
  - `FALL_THROUGH` [`00b00098`](#insn-00b00098) → [`00b0009c`](#insn-00b0009c)
- ブロック [`00b0009c`](#insn-00b0009c) 範囲 `[['00b0009c', '00b000b3']]`
  - `CONDITIONAL_JUMP` [`00b000b0`](#insn-00b000b0) → [`00b0009c`](#insn-00b0009c)
  - `FALL_THROUGH` [`00b000b0`](#insn-00b000b0) → [`00b000b4`](#insn-00b000b4)
- ブロック [`00b000b4`](#insn-00b000b4) 範囲 `[['00b000b4', '00b000bb']]`
  - `CONDITIONAL_JUMP` [`00b000b8`](#insn-00b000b8) → [`00b000c8`](#insn-00b000c8)
  - `FALL_THROUGH` [`00b000b8`](#insn-00b000b8) → [`00b000bc`](#insn-00b000bc)
- ブロック [`00b000bc`](#insn-00b000bc) 範囲 `[['00b000bc', '00b000c7']]`
  - `CONDITIONAL_JUMP` [`00b000c4`](#insn-00b000c4) → [`00b00110`](#insn-00b00110)
  - `FALL_THROUGH` [`00b000c4`](#insn-00b000c4) → [`00b000c8`](#insn-00b000c8)
- ブロック [`00b000c8`](#insn-00b000c8) 範囲 `[['00b000c8', '00b000cf']]`
  - `FALL_THROUGH` [`00b000cc`](#insn-00b000cc) → [`00b000d0`](#insn-00b000d0)
- ブロック [`00b000d0`](#insn-00b000d0) 範囲 `[['00b000d0', '00b000e3']]`
  - `FALL_THROUGH` [`00b000e0`](#insn-00b000e0) → [`00b000e4`](#insn-00b000e4)
- ブロック [`00b000e4`](#insn-00b000e4) 範囲 `[['00b000e4', '00b000e7']]`
  - `FALL_THROUGH` [`00b000e4`](#insn-00b000e4) → [`00b000e8`](#insn-00b000e8)
- ブロック [`00b000e8`](#insn-00b000e8) 範囲 `[['00b000e8', '00b000eb']]`
  - `FALL_THROUGH` [`00b000e8`](#insn-00b000e8) → [`00b000ec`](#insn-00b000ec)
- ブロック [`00b000ec`](#insn-00b000ec) 範囲 `[['00b000ec', '00b000ef']]`
  - `FALL_THROUGH` [`00b000ec`](#insn-00b000ec) → [`00b000f0`](#insn-00b000f0)
- ブロック [`00b000f0`](#insn-00b000f0) 範囲 `[['00b000f0', '00b000f3']]`
  - `FALL_THROUGH` [`00b000f0`](#insn-00b000f0) → [`00b000f4`](#insn-00b000f4)
- ブロック [`00b000f4`](#insn-00b000f4) 範囲 `[['00b000f4', '00b000f7']]`
  - `FALL_THROUGH` [`00b000f4`](#insn-00b000f4) → [`00b000f8`](#insn-00b000f8)
- ブロック [`00b000f8`](#insn-00b000f8) 範囲 `[['00b000f8', '00b0010f']]`
- ブロック [`00b00110`](#insn-00b00110) 範囲 `[['00b00110', '00b0011f']]`
  - `CONDITIONAL_JUMP` [`00b0011c`](#insn-00b0011c) → [`00b000d0`](#insn-00b000d0)
  - `FALL_THROUGH` [`00b0011c`](#insn-00b0011c) → [`00b00120`](#insn-00b00120)
- ブロック [`00b00120`](#insn-00b00120) 範囲 `[['00b00120', '00b00123']]`
  - `CONDITIONAL_JUMP` [`00b00120`](#insn-00b00120) → [`00b0016c`](#insn-00b0016c)
  - `FALL_THROUGH` [`00b00120`](#insn-00b00120) → [`00b00124`](#insn-00b00124)
- ブロック [`00b00124`](#insn-00b00124) 範囲 `[['00b00124', '00b0012b']]`
  - `CONDITIONAL_JUMP` [`00b00128`](#insn-00b00128) → [`00b001b4`](#insn-00b001b4)
  - `FALL_THROUGH` [`00b00128`](#insn-00b00128) → [`00b0012c`](#insn-00b0012c)
- ブロック [`00b0012c`](#insn-00b0012c) 範囲 `[['00b0012c', '00b00133']]`
  - `CONDITIONAL_JUMP` [`00b00130`](#insn-00b00130) → [`00b00144`](#insn-00b00144)
  - `FALL_THROUGH` [`00b00130`](#insn-00b00130) → [`00b00134`](#insn-00b00134)
- ブロック [`00b00134`](#insn-00b00134) 範囲 `[['00b00134', '00b0013b']]`
  - `FALL_THROUGH` [`00b00138`](#insn-00b00138) → [`00b0013c`](#insn-00b0013c)
- ブロック [`00b0013c`](#insn-00b0013c) 範囲 `[['00b0013c', '00b00143']]`
  - `CONDITIONAL_JUMP` [`00b00140`](#insn-00b00140) → [`00b00158`](#insn-00b00158)
  - `FALL_THROUGH` [`00b00140`](#insn-00b00140) → [`00b00144`](#insn-00b00144)
- ブロック [`00b00144`](#insn-00b00144) 範囲 `[['00b00144', '00b0014b']]`
  - `FALL_THROUGH` [`00b00148`](#insn-00b00148) → [`00b0014c`](#insn-00b0014c)
- ブロック [`00b0014c`](#insn-00b0014c) 範囲 `[['00b0014c', '00b00157']]`
  - `FALL_THROUGH` [`00b00154`](#insn-00b00154) → [`00b00158`](#insn-00b00158)
- ブロック [`00b00158`](#insn-00b00158) 範囲 `[['00b00158', '00b0016b']]`
  - `UNCONDITIONAL_JUMP` [`00b00168`](#insn-00b00168) → [`00b001b8`](#insn-00b001b8)
- ブロック [`00b0016c`](#insn-00b0016c) 範囲 `[['00b0016c', '00b0017b']]`
  - `FALL_THROUGH` [`00b00178`](#insn-00b00178) → [`00b0017c`](#insn-00b0017c)
- ブロック [`00b0017c`](#insn-00b0017c) 範囲 `[['00b0017c', '00b00197']]`
  - `CONDITIONAL_JUMP` [`00b00194`](#insn-00b00194) → [`00b001cc`](#insn-00b001cc)
  - `FALL_THROUGH` [`00b00194`](#insn-00b00194) → [`00b00198`](#insn-00b00198)
- ブロック [`00b00198`](#insn-00b00198) 範囲 `[['00b00198', '00b001ab']]`
  - `FALL_THROUGH` [`00b001a8`](#insn-00b001a8) → [`00b001ac`](#insn-00b001ac)
- ブロック [`00b001ac`](#insn-00b001ac) 範囲 `[['00b001ac', '00b001b3']]`
  - `UNCONDITIONAL_JUMP` [`00b001b0`](#insn-00b001b0) → [`00b000f8`](#insn-00b000f8)
- ブロック [`00b001b4`](#insn-00b001b4) 範囲 `[['00b001b4', '00b001b7']]`
  - `FALL_THROUGH` [`00b001b4`](#insn-00b001b4) → [`00b001b8`](#insn-00b001b8)
- ブロック [`00b001b8`](#insn-00b001b8) 範囲 `[['00b001b8', '00b001cb']]`
  - `CONDITIONAL_JUMP` [`00b001c8`](#insn-00b001c8) → [`00b00198`](#insn-00b00198)
  - `FALL_THROUGH` [`00b001c8`](#insn-00b001c8) → [`00b001cc`](#insn-00b001cc)
- ブロック [`00b001cc`](#insn-00b001cc) 範囲 `[['00b001cc', '00b001d3']]`
  - `FALL_THROUGH` [`00b001d0`](#insn-00b001d0) → [`00b001d4`](#insn-00b001d4)
- ブロック [`00b001d4`](#insn-00b001d4) 範囲 `[['00b001d4', '00b001db']]`
  - `UNCONDITIONAL_JUMP` [`00b001d8`](#insn-00b001d8) → [`00b000f0`](#insn-00b000f0)

## 命令位置別の参照

- [`00afffcc`](#insn-00afffcc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffd0`](#insn-00afffd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffd4`](#insn-00afffd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffd8`](#insn-00afffd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffdc`](#insn-00afffdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affffc`](#insn-00affffc) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b00008`](#insn-00b00008) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b00014`](#insn-00b00014) → [`00b00038`](#insn-00b00038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0001c`](#insn-00b0001c) → [`00b00040`](#insn-00b00040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00034`](#insn-00b00034) → [`00b00058`](#insn-00b00058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0003c`](#insn-00b0003c) → [`00b00058`](#insn-00b00058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00064`](#insn-00b00064) → [`00b001dc`](../00b00/00b001dc.md) · `DATA` · `ANALYSIS` · 関数 `00b001dc` · 推定シンボル `None` · 推定型 `None`
- [`00b00078`](#insn-00b00078) → [`00b00214`](../00b00/00b00214.md) · `DATA` · `ANALYSIS` · 関数 `00b00214` · 推定シンボル `None` · 推定型 `None`
- [`00b0007c`](#insn-00b0007c) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00b00088`](#insn-00b00088) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00b00094`](#insn-00b00094) → [`00b000c8`](#insn-00b000c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000b0`](#insn-00b000b0) → [`00b0009c`](#insn-00b0009c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000b8`](#insn-00b000b8) → [`00b000c8`](#insn-00b000c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000c4`](#insn-00b000c4) → [`00b00110`](#insn-00b00110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000cc`](#insn-00b000cc) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00b000d4`](#insn-00b000d4) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00b000ec`](#insn-00b000ec) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b000f8`](#insn-00b000f8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000fc`](#insn-00b000fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00100`](#insn-00b00100) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00104`](#insn-00b00104) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00118`](#insn-00b00118) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00b0011c`](#insn-00b0011c) → [`00b000d0`](#insn-00b000d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00120`](#insn-00b00120) → [`00b0016c`](#insn-00b0016c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00128`](#insn-00b00128) → [`00b001b4`](#insn-00b001b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00130`](#insn-00b00130) → [`00b00144`](#insn-00b00144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00140`](#insn-00b00140) → [`00b00158`](#insn-00b00158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00154`](#insn-00b00154) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b00168`](#insn-00b00168) → [`00b001b8`](#insn-00b001b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00194`](#insn-00b00194) → [`00b001cc`](#insn-00b001cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0019c`](#insn-00b0019c) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00b001ac`](#insn-00b001ac) → [`00b00214`](../00b00/00b00214.md) · `DATA` · `ANALYSIS` · 関数 `00b00214` · 推定シンボル `None` · 推定型 `None`
- [`00b001b0`](#insn-00b001b0) → [`00b000f8`](#insn-00b000f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b001c8`](#insn-00b001c8) → [`00b00198`](#insn-00b00198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b001d4`](#insn-00b001d4) → [`00bddf10`](../00bdd/00bddf10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf10` · 推定シンボル `None` · 推定型 `None`
- [`00b001d8`](#insn-00b001d8) → [`00b000f0`](#insn-00b000f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afffcc`](#insn-00afffcc)

~~~json
{
  "source": "00afffcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffd0`](#insn-00afffd0)

~~~json
{
  "source": "00afffd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffd4`](#insn-00afffd4)

~~~json
{
  "source": "00afffd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffd8`](#insn-00afffd8)

~~~json
{
  "source": "00afffd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffdc`](#insn-00afffdc)

~~~json
{
  "source": "00afffdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affffc`](#insn-00affffc)

~~~json
{
  "source": "00affffc",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b00008`](#insn-00b00008)

~~~json
{
  "source": "00b00008",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b00014`](#insn-00b00014)

~~~json
{
  "source": "00b00014",
  "target": "00b00038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0001c`](#insn-00b0001c)

~~~json
{
  "source": "00b0001c",
  "target": "00b00040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00034`](#insn-00b00034)

~~~json
{
  "source": "00b00034",
  "target": "00b00058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0003c`](#insn-00b0003c)

~~~json
{
  "source": "00b0003c",
  "target": "00b00058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00064`](#insn-00b00064)

~~~json
{
  "source": "00b00064",
  "target": "00b001dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b00078`](#insn-00b00078)

~~~json
{
  "source": "00b00078",
  "target": "00b00214",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0007c`](#insn-00b0007c)

~~~json
{
  "source": "00b0007c",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b00088`](#insn-00b00088)

~~~json
{
  "source": "00b00088",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b00094`](#insn-00b00094)

~~~json
{
  "source": "00b00094",
  "target": "00b000c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000b0`](#insn-00b000b0)

~~~json
{
  "source": "00b000b0",
  "target": "00b0009c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000b8`](#insn-00b000b8)

~~~json
{
  "source": "00b000b8",
  "target": "00b000c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000c4`](#insn-00b000c4)

~~~json
{
  "source": "00b000c4",
  "target": "00b00110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000cc`](#insn-00b000cc)

~~~json
{
  "source": "00b000cc",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b000d4`](#insn-00b000d4)

~~~json
{
  "source": "00b000d4",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b000ec`](#insn-00b000ec)

~~~json
{
  "source": "00b000ec",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b000f8`](#insn-00b000f8)

~~~json
{
  "source": "00b000f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000fc`](#insn-00b000fc)

~~~json
{
  "source": "00b000fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00100`](#insn-00b00100)

~~~json
{
  "source": "00b00100",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00104`](#insn-00b00104)

~~~json
{
  "source": "00b00104",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00118`](#insn-00b00118)

~~~json
{
  "source": "00b00118",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0011c`](#insn-00b0011c)

~~~json
{
  "source": "00b0011c",
  "target": "00b000d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00120`](#insn-00b00120)

~~~json
{
  "source": "00b00120",
  "target": "00b0016c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00128`](#insn-00b00128)

~~~json
{
  "source": "00b00128",
  "target": "00b001b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00130`](#insn-00b00130)

~~~json
{
  "source": "00b00130",
  "target": "00b00144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00140`](#insn-00b00140)

~~~json
{
  "source": "00b00140",
  "target": "00b00158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00154`](#insn-00b00154)

~~~json
{
  "source": "00b00154",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b00168`](#insn-00b00168)

~~~json
{
  "source": "00b00168",
  "target": "00b001b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00194`](#insn-00b00194)

~~~json
{
  "source": "00b00194",
  "target": "00b001cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0019c`](#insn-00b0019c)

~~~json
{
  "source": "00b0019c",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b001ac`](#insn-00b001ac)

~~~json
{
  "source": "00b001ac",
  "target": "00b00214",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b001b0`](#insn-00b001b0)

~~~json
{
  "source": "00b001b0",
  "target": "00b000f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b001c8`](#insn-00b001c8)

~~~json
{
  "source": "00b001c8",
  "target": "00b00198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b001d4`](#insn-00b001d4)

~~~json
{
  "source": "00b001d4",
  "target": "00bddf10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b001d8`](#insn-00b001d8)

~~~json
{
  "source": "00b001d8",
  "target": "00b000f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
