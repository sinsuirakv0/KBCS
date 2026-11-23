# 00affcec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00affc24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affc24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-fa1347b7d553fbdaa2407b04951e8a05)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00affd30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affd30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-4d159c757bb458a807a55301a3e32928)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affcec",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5cd43394f437014435c5adaab58c15818b0f8cb6b242b328b6cb4ab763c78eb",
  "source_text_sha256": "c5cd43394f437014435c5adaab58c15818b0f8cb6b242b328b6cb4ab763c78eb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affcec",
        "00affe9f"
      ]
    ],
    "bytes_sha256": "4d4e3a5f6f0deb3681bbf2012950f159b0cf0958ca14367959c3e7355ad13571",
    "instruction_count": 109,
    "instruction_bytes": 436,
    "body_bytes": 436,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddfc0](../00bdd/00bddfc0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6273 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb
               (long *param_1,long param_2,ulong *param_3,long param_4,long param_5,long param_6,
               uint param_7)

{
  long lVar1;
  long lVar2;
  undefined8 *puVar3;
  long *plVar4;
  long *plVar5;
  int iVar6;
  long *plVar7;
  long *plVar8;
  ulong uVar9;
  int *piVar10;
  
                    /* catch() { ... } // from try @ 00af5b40 with catch @ 00affcec */
                    /* catch() { ... } // from try @ 00af5b34 with catch @ 00affd04 */
                    /* catch() { ... } // from try @ 00af5b28 with catch @ 00affd10 */
                    /* catch() { ... } // from try @ 00af5b1c with catch @ 00affd28 */
  plVar4 = (long *)_Znwm(0x28);
  lVar1 = param_2 + 8;
                    /* catch() { ... } // from try @ 00af5b10 with catch @ 00affd34 */
  *plVar4 = (long)plVar4;
  plVar4[1] = (long)plVar4;
  plVar4[2] = param_4;
  plVar4[3] = param_5;
  plVar4[4] = param_6;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar9 = *param_3;
                    /* catch() { ... } // from try @ 00af5b04 with catch @ 00affd4c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af5ae4 with catch @ 00affd58 */
  plVar7 = (long *)(param_2 + 0x38);
  plVar8 = (long *)*plVar7;
  plVar5 = plVar7;
  if (plVar8 == (long *)0x0) {
LAB_00affd90:
                    /* catch() { ... } // from try @ 00af5ac0 with catch @ 00affd94 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
                    /* catch() { ... } // from try @ 00af5ad8 with catch @ 00affd70 */
      if ((ulong)plVar8[4] >= uVar9) {
        plVar5 = plVar8;
      }
      plVar8 = (long *)plVar8[(ulong)plVar8[4] < uVar9];
    } while (plVar8 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5acc with catch @ 00affd7c */
    if ((plVar5 == plVar7) || (uVar9 < (ulong)plVar5[4])) goto LAB_00affd90;
                    /* catch() { ... } // from try @ 00af5a50 with catch @ 00affddc */
    piVar10 = (int *)plVar5[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5a2c with catch @ 00affde8 */
    if (piVar10 != (int *)0x0) {
      if ((param_7 & 1) == 0) {
                    /* catch() { ... } // from try @ 00af59b0 with catch @ 00affe3c */
        puVar3 = *(undefined8 **)(piVar10 + 0x16);
                    /* catch() { ... } // from try @ 00af59a4 with catch @ 00affe44 */
        plVar4 = (long *)((long)plVar4 + *(long *)(piVar10 + 0x18));
                    /* catch() { ... } // from try @ 00af5998 with catch @ 00affe4c */
        piVar10[8] = piVar10[8] + 1;
        *puVar3 = plVar4;
                    /* catch() { ... } // from try @ 00af598c with catch @ 00affe54 */
        *plVar4 = (long)(piVar10 + 0x14);
        plVar4[1] = (long)puVar3;
        *(long **)(piVar10 + 0x16) = plVar4;
                    /* catch() { ... } // from try @ 00af5980 with catch @ 00affe5c */
        iVar6 = *piVar10;
      }
      else {
        plVar5 = *(long **)(piVar10 + 0x12);
                    /* catch() { ... } // from try @ 00af5a1c with catch @ 00affdf4 */
        if (plVar5 == (long *)0x0) {
          iVar6 = piVar10[8];
        }
        else {
                    /* catch() { ... } // from try @ 00af5a10 with catch @ 00affdfc */
          if ((code *)plVar5[4] == (code *)0x0) {
LAB_00affe10:
            lVar2 = *plVar5;
                    /* catch() { ... } // from try @ 00af59ec with catch @ 00affe14 */
            *(long *)(lVar2 + 8) = plVar5[1];
                    /* catch() { ... } // from try @ 00af59e0 with catch @ 00affe1c */
            *(long *)plVar5[1] = lVar2;
            _ZdlPv(plVar5);
          }
          else {
                    /* catch() { ... } // from try @ 00af5a04 with catch @ 00affe04 */
            (*(code *)plVar5[4])(plVar5[3]);
            plVar5 = *(long **)(piVar10 + 0x12);
                    /* catch() { ... } // from try @ 00af59f8 with catch @ 00affe0c */
            if (plVar5 != (long *)0x0) goto LAB_00affe10;
          }
                    /* catch() { ... } // from try @ 00af59d4 with catch @ 00affe24 */
          piVar10[0x12] = 0;
          piVar10[0x13] = 0;
                    /* catch() { ... } // from try @ 00af59c8 with catch @ 00affe2c */
          iVar6 = piVar10[8] + -1;
          piVar10[8] = iVar6;
                    /* catch() { ... } // from try @ 00af59bc with catch @ 00affe34 */
        }
                    /* catch() { ... } // from try @ 00af5950 with catch @ 00affe7c */
        piVar10[8] = iVar6 + 1;
                    /* catch() { ... } // from try @ 00af5944 with catch @ 00affe84 */
        *(long **)(piVar10 + 0x12) = plVar4;
        iVar6 = *piVar10;
                    /* catch() { ... } // from try @ 00af5938 with catch @ 00affe8c */
      }
      if (iVar6 != 0) {
                    /* catch() { ... } // from try @ 00af5974 with catch @ 00affe64 */
        _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5968 with catch @ 00affe6c */
        *param_1 = param_4;
        param_1[1] = param_5;
        param_1[2] = param_6;
        return;
                    /* catch() { ... } // from try @ 00af595c with catch @ 00affe74 */
      }
                    /* catch() { ... } // from try @ 00af592c with catch @ 00affe94 */
      _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
                (param_2,param_3);
                    /* catch() { ... } // from try @ 00af5920 with catch @ 00affe9c */
      goto LAB_00affdb8;
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5ab4 with catch @ 00affda0 */
  lVar1 = *plVar4;
  *(long *)(lVar1 + 8) = plVar4[1];
  *(long *)plVar4[1] = lVar1;
  _ZdlPv(plVar4);
LAB_00affdb8:
                    /* catch() { ... } // from try @ 00af5aa8 with catch @ 00affdb8 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* catch() { ... } // from try @ 00af5a9c with catch @ 00affdc4 */
                    /* catch() { ... } // from try @ 00af5a60 with catch @ 00affdd0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affcec"></a> `00affcec` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00affcf0"></a> `00affcf0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affcf4"></a> `00affcf4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affcf8"></a> `00affcf8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affcfc"></a> `00affcfc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00affd00"></a> `00affd00` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00affd04"></a> `00affd04` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00affd08"></a> `00affd08` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00affd0c"></a> `00affd0c` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00affd10"></a> `00affd10` | `fb 03 05 2a` | mov w27,w5 | `FALL_THROUGH`
<a id="insn-00affd14"></a> `00affd14` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00affd18"></a> `00affd18` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00affd1c"></a> `00affd1c` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00affd20"></a> `00affd20` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00affd24"></a> `00affd24` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00affd28"></a> `00affd28` | `b2 6c 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00affd2c"></a> `00affd2c` | `1a 23 00 91` | add x26,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00affd30"></a> `00affd30` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00affd34"></a> `00affd34` | `00 00 00 a9` | stp x0,x0,[x0] | `FALL_THROUGH`
<a id="insn-00affd38"></a> `00affd38` | `16 54 01 a9` | stp x22,x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00affd3c"></a> `00affd3c` | `14 10 00 f9` | str x20,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00affd40"></a> `00affd40` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00affd44"></a> `00affd44` | `a3 77 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affd48"></a> `00affd48` | `fc 02 40 f9` | ldr x28,[x23] | `FALL_THROUGH`
<a id="insn-00affd4c"></a> `00affd4c` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00affd50"></a> `00affd50` | `a0 77 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affd54"></a> `00affd54` | `e9 03 18 aa` | mov x9,x24 | `FALL_THROUGH`
<a id="insn-00affd58"></a> `00affd58` | `2a 8d 43 f8` | ldr x10,[x9, #0x38]! | `FALL_THROUGH`
<a id="insn-00affd5c"></a> `00affd5c` | `aa 01 00 b4` | cbz x10,0x00affd90 | `CONDITIONAL_JUMP`
<a id="insn-00affd60"></a> `00affd60` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00affd64"></a> `00affd64` | `4b 11 40 f9` | ldr x11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00affd68"></a> `00affd68` | `7f 01 1c eb` | cmp x11,x28 | `FALL_THROUGH`
<a id="insn-00affd6c"></a> `00affd6c` | `eb 27 9f 1a` | cset w11,cc | `FALL_THROUGH`
<a id="insn-00affd70"></a> `00affd70` | `08 31 8a 9a` | csel x8,x8,x10,cc | `FALL_THROUGH`
<a id="insn-00affd74"></a> `00affd74` | `4a 59 6b f8` | ldr x10,[x10, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affd78"></a> `00affd78` | `6a ff ff b5` | cbnz x10,0x00affd64 | `CONDITIONAL_JUMP`
<a id="insn-00affd7c"></a> `00affd7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00affd80"></a> `00affd80` | `80 00 00 54` | b.eq 0x00affd90 | `CONDITIONAL_JUMP`
<a id="insn-00affd84"></a> `00affd84` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affd88"></a> `00affd88` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-00affd8c"></a> `00affd8c` | `89 02 00 54` | b.ls 0x00affddc | `CONDITIONAL_JUMP`
<a id="insn-00affd90"></a> `00affd90` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00affd94"></a> `00affd94` | `93 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affd98"></a> `00affd98` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00affd9c"></a> `00affd9c` | `91 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affda0"></a> `00affda0` | `28 27 40 a9` | ldp x8,x9,[x25] | `FALL_THROUGH`
<a id="insn-00affda4"></a> `00affda4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00affda8"></a> `00affda8` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00affdac"></a> `00affdac` | `29 07 40 f9` | ldr x9,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00affdb0"></a> `00affdb0` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00affdb4"></a> `00affdb4` | `97 6c 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00affdb8"></a> `00affdb8` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00affdbc"></a> `00affdbc` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00affdc0"></a> `00affdc0` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00affdc4"></a> `00affdc4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00affdc8"></a> `00affdc8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affdcc"></a> `00affdcc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affdd0"></a> `00affdd0` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affdd4"></a> `00affdd4` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00affdd8"></a> `00affdd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affddc"></a> `00affddc` | `1c 15 40 f9` | ldr x28,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affde0"></a> `00affde0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00affde4"></a> `00affde4` | `7f 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affde8"></a> `00affde8` | `9c fd ff b4` | cbz x28,0x00affd98 | `CONDITIONAL_JUMP`
<a id="insn-00affdec"></a> `00affdec` | `7b 02 00 36` | tbz w27,#0x0,0x00affe38 | `CONDITIONAL_JUMP`
<a id="insn-00affdf0"></a> `00affdf0` | `80 27 40 f9` | ldr x0,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00affdf4"></a> `00affdf4` | `20 04 00 b4` | cbz x0,0x00affe78 | `CONDITIONAL_JUMP`
<a id="insn-00affdf8"></a> `00affdf8` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00affdfc"></a> `00affdfc` | `a8 00 00 b4` | cbz x8,0x00affe10 | `CONDITIONAL_JUMP`
<a id="insn-00affe00"></a> `00affe00` | `00 0c 40 f9` | ldr x0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00affe04"></a> `00affe04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00affe08"></a> `00affe08` | `80 27 40 f9` | ldr x0,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00affe0c"></a> `00affe0c` | `c0 00 00 b4` | cbz x0,0x00affe24 | `CONDITIONAL_JUMP`
<a id="insn-00affe10"></a> `00affe10` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00affe14"></a> `00affe14` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00affe18"></a> `00affe18` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00affe1c"></a> `00affe1c` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00affe20"></a> `00affe20` | `7c 6c 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00affe24"></a> `00affe24` | `88 23 40 b9` | ldr w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00affe28"></a> `00affe28` | `9f 27 00 f9` | str xzr,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00affe2c"></a> `00affe2c` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00affe30"></a> `00affe30` | `88 23 00 b9` | str w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00affe34"></a> `00affe34` | `12 00 00 14` | b 0x00affe7c | `UNCONDITIONAL_JUMP`
<a id="insn-00affe38"></a> `00affe38` | `88 23 40 b9` | ldr w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00affe3c"></a> `00affe3c` | `8a a7 45 a9` | ldp x10,x9,[x28, #0x58] | `FALL_THROUGH`
<a id="insn-00affe40"></a> `00affe40` | `8b 43 01 91` | add x11,x28,#0x50 | `FALL_THROUGH`
<a id="insn-00affe44"></a> `00affe44` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00affe48"></a> `00affe48` | `29 03 09 8b` | add x9,x25,x9 | `FALL_THROUGH`
<a id="insn-00affe4c"></a> `00affe4c` | `88 23 00 b9` | str w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00affe50"></a> `00affe50` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00affe54"></a> `00affe54` | `2b 29 00 a9` | stp x11,x10,[x9] | `FALL_THROUGH`
<a id="insn-00affe58"></a> `00affe58` | `89 2f 00 f9` | str x9,[x28, #0x58] | `FALL_THROUGH`
<a id="insn-00affe5c"></a> `00affe5c` | `88 03 40 b9` | ldr w8,[x28] | `FALL_THROUGH`
<a id="insn-00affe60"></a> `00affe60` | `88 01 00 34` | cbz w8,0x00affe90 | `CONDITIONAL_JUMP`
<a id="insn-00affe64"></a> `00affe64` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00affe68"></a> `00affe68` | `5e 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affe6c"></a> `00affe6c` | `76 56 00 a9` | stp x22,x21,[x19] | `FALL_THROUGH`
<a id="insn-00affe70"></a> `00affe70` | `74 0a 00 f9` | str x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00affe74"></a> `00affe74` | `d3 ff ff 17` | b 0x00affdc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00affe78"></a> `00affe78` | `88 23 40 b9` | ldr w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00affe7c"></a> `00affe7c` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00affe80"></a> `00affe80` | `88 23 00 b9` | str w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00affe84"></a> `00affe84` | `99 27 00 f9` | str x25,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00affe88"></a> `00affe88` | `88 03 40 b9` | ldr w8,[x28] | `FALL_THROUGH`
<a id="insn-00affe8c"></a> `00affe8c` | `c8 fe ff 35` | cbnz w8,0x00affe64 | `CONDITIONAL_JUMP`
<a id="insn-00affe90"></a> `00affe90` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00affe94"></a> `00affe94` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00affe98"></a> `00affe98` | `4a 78 03 94` | bl 0x00bddfc0 | `UNCONDITIONAL_CALL`
<a id="insn-00affe9c"></a> `00affe9c` | `c7 ff ff 17` | b 0x00affdb8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affcec`](#insn-00affcec) 範囲 `[['00affcec', '00affd03']]`
  - `FALL_THROUGH` [`00affd00`](#insn-00affd00) → [`00affd04`](#insn-00affd04)
- ブロック [`00affd04`](#insn-00affd04) 範囲 `[['00affd04', '00affd0f']]`
  - `FALL_THROUGH` [`00affd0c`](#insn-00affd0c) → [`00affd10`](#insn-00affd10)
- ブロック [`00affd10`](#insn-00affd10) 範囲 `[['00affd10', '00affd27']]`
  - `FALL_THROUGH` [`00affd24`](#insn-00affd24) → [`00affd28`](#insn-00affd28)
- ブロック [`00affd28`](#insn-00affd28) 範囲 `[['00affd28', '00affd33']]`
  - `FALL_THROUGH` [`00affd30`](#insn-00affd30) → [`00affd34`](#insn-00affd34)
- ブロック [`00affd34`](#insn-00affd34) 範囲 `[['00affd34', '00affd4b']]`
  - `FALL_THROUGH` [`00affd48`](#insn-00affd48) → [`00affd4c`](#insn-00affd4c)
- ブロック [`00affd4c`](#insn-00affd4c) 範囲 `[['00affd4c', '00affd57']]`
  - `FALL_THROUGH` [`00affd54`](#insn-00affd54) → [`00affd58`](#insn-00affd58)
- ブロック [`00affd58`](#insn-00affd58) 範囲 `[['00affd58', '00affd5f']]`
  - `CONDITIONAL_JUMP` [`00affd5c`](#insn-00affd5c) → [`00affd90`](#insn-00affd90)
  - `FALL_THROUGH` [`00affd5c`](#insn-00affd5c) → [`00affd60`](#insn-00affd60)
- ブロック [`00affd60`](#insn-00affd60) 範囲 `[['00affd60', '00affd63']]`
  - `FALL_THROUGH` [`00affd60`](#insn-00affd60) → [`00affd64`](#insn-00affd64)
- ブロック [`00affd64`](#insn-00affd64) 範囲 `[['00affd64', '00affd6f']]`
  - `FALL_THROUGH` [`00affd6c`](#insn-00affd6c) → [`00affd70`](#insn-00affd70)
- ブロック [`00affd70`](#insn-00affd70) 範囲 `[['00affd70', '00affd7b']]`
  - `CONDITIONAL_JUMP` [`00affd78`](#insn-00affd78) → [`00affd64`](#insn-00affd64)
  - `FALL_THROUGH` [`00affd78`](#insn-00affd78) → [`00affd7c`](#insn-00affd7c)
- ブロック [`00affd7c`](#insn-00affd7c) 範囲 `[['00affd7c', '00affd83']]`
  - `CONDITIONAL_JUMP` [`00affd80`](#insn-00affd80) → [`00affd90`](#insn-00affd90)
  - `FALL_THROUGH` [`00affd80`](#insn-00affd80) → [`00affd84`](#insn-00affd84)
- ブロック [`00affd84`](#insn-00affd84) 範囲 `[['00affd84', '00affd8f']]`
  - `CONDITIONAL_JUMP` [`00affd8c`](#insn-00affd8c) → [`00affddc`](#insn-00affddc)
  - `FALL_THROUGH` [`00affd8c`](#insn-00affd8c) → [`00affd90`](#insn-00affd90)
- ブロック [`00affd90`](#insn-00affd90) 範囲 `[['00affd90', '00affd93']]`
  - `FALL_THROUGH` [`00affd90`](#insn-00affd90) → [`00affd94`](#insn-00affd94)
- ブロック [`00affd94`](#insn-00affd94) 範囲 `[['00affd94', '00affd97']]`
  - `FALL_THROUGH` [`00affd94`](#insn-00affd94) → [`00affd98`](#insn-00affd98)
- ブロック [`00affd98`](#insn-00affd98) 範囲 `[['00affd98', '00affd9f']]`
  - `FALL_THROUGH` [`00affd9c`](#insn-00affd9c) → [`00affda0`](#insn-00affda0)
- ブロック [`00affda0`](#insn-00affda0) 範囲 `[['00affda0', '00affdb7']]`
  - `FALL_THROUGH` [`00affdb4`](#insn-00affdb4) → [`00affdb8`](#insn-00affdb8)
- ブロック [`00affdb8`](#insn-00affdb8) 範囲 `[['00affdb8', '00affdbf']]`
  - `FALL_THROUGH` [`00affdbc`](#insn-00affdbc) → [`00affdc0`](#insn-00affdc0)
- ブロック [`00affdc0`](#insn-00affdc0) 範囲 `[['00affdc0', '00affdc3']]`
  - `FALL_THROUGH` [`00affdc0`](#insn-00affdc0) → [`00affdc4`](#insn-00affdc4)
- ブロック [`00affdc4`](#insn-00affdc4) 範囲 `[['00affdc4', '00affdcf']]`
  - `FALL_THROUGH` [`00affdcc`](#insn-00affdcc) → [`00affdd0`](#insn-00affdd0)
- ブロック [`00affdd0`](#insn-00affdd0) 範囲 `[['00affdd0', '00affddb']]`
- ブロック [`00affddc`](#insn-00affddc) 範囲 `[['00affddc', '00affde7']]`
  - `FALL_THROUGH` [`00affde4`](#insn-00affde4) → [`00affde8`](#insn-00affde8)
- ブロック [`00affde8`](#insn-00affde8) 範囲 `[['00affde8', '00affdeb']]`
  - `CONDITIONAL_JUMP` [`00affde8`](#insn-00affde8) → [`00affd98`](#insn-00affd98)
  - `FALL_THROUGH` [`00affde8`](#insn-00affde8) → [`00affdec`](#insn-00affdec)
- ブロック [`00affdec`](#insn-00affdec) 範囲 `[['00affdec', '00affdef']]`
  - `CONDITIONAL_JUMP` [`00affdec`](#insn-00affdec) → [`00affe38`](#insn-00affe38)
  - `FALL_THROUGH` [`00affdec`](#insn-00affdec) → [`00affdf0`](#insn-00affdf0)
- ブロック [`00affdf0`](#insn-00affdf0) 範囲 `[['00affdf0', '00affdf3']]`
  - `FALL_THROUGH` [`00affdf0`](#insn-00affdf0) → [`00affdf4`](#insn-00affdf4)
- ブロック [`00affdf4`](#insn-00affdf4) 範囲 `[['00affdf4', '00affdf7']]`
  - `CONDITIONAL_JUMP` [`00affdf4`](#insn-00affdf4) → [`00affe78`](#insn-00affe78)
  - `FALL_THROUGH` [`00affdf4`](#insn-00affdf4) → [`00affdf8`](#insn-00affdf8)
- ブロック [`00affdf8`](#insn-00affdf8) 範囲 `[['00affdf8', '00affdfb']]`
  - `FALL_THROUGH` [`00affdf8`](#insn-00affdf8) → [`00affdfc`](#insn-00affdfc)
- ブロック [`00affdfc`](#insn-00affdfc) 範囲 `[['00affdfc', '00affdff']]`
  - `CONDITIONAL_JUMP` [`00affdfc`](#insn-00affdfc) → [`00affe10`](#insn-00affe10)
  - `FALL_THROUGH` [`00affdfc`](#insn-00affdfc) → [`00affe00`](#insn-00affe00)
- ブロック [`00affe00`](#insn-00affe00) 範囲 `[['00affe00', '00affe03']]`
  - `FALL_THROUGH` [`00affe00`](#insn-00affe00) → [`00affe04`](#insn-00affe04)
- ブロック [`00affe04`](#insn-00affe04) 範囲 `[['00affe04', '00affe0b']]`
  - `FALL_THROUGH` [`00affe08`](#insn-00affe08) → [`00affe0c`](#insn-00affe0c)
- ブロック [`00affe0c`](#insn-00affe0c) 範囲 `[['00affe0c', '00affe0f']]`
  - `CONDITIONAL_JUMP` [`00affe0c`](#insn-00affe0c) → [`00affe24`](#insn-00affe24)
  - `FALL_THROUGH` [`00affe0c`](#insn-00affe0c) → [`00affe10`](#insn-00affe10)
- ブロック [`00affe10`](#insn-00affe10) 範囲 `[['00affe10', '00affe13']]`
  - `FALL_THROUGH` [`00affe10`](#insn-00affe10) → [`00affe14`](#insn-00affe14)
- ブロック [`00affe14`](#insn-00affe14) 範囲 `[['00affe14', '00affe1b']]`
  - `FALL_THROUGH` [`00affe18`](#insn-00affe18) → [`00affe1c`](#insn-00affe1c)
- ブロック [`00affe1c`](#insn-00affe1c) 範囲 `[['00affe1c', '00affe23']]`
  - `FALL_THROUGH` [`00affe20`](#insn-00affe20) → [`00affe24`](#insn-00affe24)
- ブロック [`00affe24`](#insn-00affe24) 範囲 `[['00affe24', '00affe2b']]`
  - `FALL_THROUGH` [`00affe28`](#insn-00affe28) → [`00affe2c`](#insn-00affe2c)
- ブロック [`00affe2c`](#insn-00affe2c) 範囲 `[['00affe2c', '00affe33']]`
  - `FALL_THROUGH` [`00affe30`](#insn-00affe30) → [`00affe34`](#insn-00affe34)
- ブロック [`00affe34`](#insn-00affe34) 範囲 `[['00affe34', '00affe37']]`
  - `UNCONDITIONAL_JUMP` [`00affe34`](#insn-00affe34) → [`00affe7c`](#insn-00affe7c)
- ブロック [`00affe38`](#insn-00affe38) 範囲 `[['00affe38', '00affe3b']]`
  - `FALL_THROUGH` [`00affe38`](#insn-00affe38) → [`00affe3c`](#insn-00affe3c)
- ブロック [`00affe3c`](#insn-00affe3c) 範囲 `[['00affe3c', '00affe43']]`
  - `FALL_THROUGH` [`00affe40`](#insn-00affe40) → [`00affe44`](#insn-00affe44)
- ブロック [`00affe44`](#insn-00affe44) 範囲 `[['00affe44', '00affe4b']]`
  - `FALL_THROUGH` [`00affe48`](#insn-00affe48) → [`00affe4c`](#insn-00affe4c)
- ブロック [`00affe4c`](#insn-00affe4c) 範囲 `[['00affe4c', '00affe53']]`
  - `FALL_THROUGH` [`00affe50`](#insn-00affe50) → [`00affe54`](#insn-00affe54)
- ブロック [`00affe54`](#insn-00affe54) 範囲 `[['00affe54', '00affe5b']]`
  - `FALL_THROUGH` [`00affe58`](#insn-00affe58) → [`00affe5c`](#insn-00affe5c)
- ブロック [`00affe5c`](#insn-00affe5c) 範囲 `[['00affe5c', '00affe63']]`
  - `CONDITIONAL_JUMP` [`00affe60`](#insn-00affe60) → [`00affe90`](#insn-00affe90)
  - `FALL_THROUGH` [`00affe60`](#insn-00affe60) → [`00affe64`](#insn-00affe64)
- ブロック [`00affe64`](#insn-00affe64) 範囲 `[['00affe64', '00affe6b']]`
  - `FALL_THROUGH` [`00affe68`](#insn-00affe68) → [`00affe6c`](#insn-00affe6c)
- ブロック [`00affe6c`](#insn-00affe6c) 範囲 `[['00affe6c', '00affe73']]`
  - `FALL_THROUGH` [`00affe70`](#insn-00affe70) → [`00affe74`](#insn-00affe74)
- ブロック [`00affe74`](#insn-00affe74) 範囲 `[['00affe74', '00affe77']]`
  - `UNCONDITIONAL_JUMP` [`00affe74`](#insn-00affe74) → [`00affdc0`](#insn-00affdc0)
- ブロック [`00affe78`](#insn-00affe78) 範囲 `[['00affe78', '00affe7b']]`
  - `FALL_THROUGH` [`00affe78`](#insn-00affe78) → [`00affe7c`](#insn-00affe7c)
- ブロック [`00affe7c`](#insn-00affe7c) 範囲 `[['00affe7c', '00affe83']]`
  - `FALL_THROUGH` [`00affe80`](#insn-00affe80) → [`00affe84`](#insn-00affe84)
- ブロック [`00affe84`](#insn-00affe84) 範囲 `[['00affe84', '00affe8b']]`
  - `FALL_THROUGH` [`00affe88`](#insn-00affe88) → [`00affe8c`](#insn-00affe8c)
- ブロック [`00affe8c`](#insn-00affe8c) 範囲 `[['00affe8c', '00affe8f']]`
  - `CONDITIONAL_JUMP` [`00affe8c`](#insn-00affe8c) → [`00affe64`](#insn-00affe64)
  - `FALL_THROUGH` [`00affe8c`](#insn-00affe8c) → [`00affe90`](#insn-00affe90)
- ブロック [`00affe90`](#insn-00affe90) 範囲 `[['00affe90', '00affe93']]`
  - `FALL_THROUGH` [`00affe90`](#insn-00affe90) → [`00affe94`](#insn-00affe94)
- ブロック [`00affe94`](#insn-00affe94) 範囲 `[['00affe94', '00affe9b']]`
  - `FALL_THROUGH` [`00affe98`](#insn-00affe98) → [`00affe9c`](#insn-00affe9c)
- ブロック [`00affe9c`](#insn-00affe9c) 範囲 `[['00affe9c', '00affe9f']]`
  - `UNCONDITIONAL_JUMP` [`00affe9c`](#insn-00affe9c) → [`00affdb8`](#insn-00affdb8)

## 命令位置別の参照

- [`00affcec`](#insn-00affcec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affcf0`](#insn-00affcf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affcf4`](#insn-00affcf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affcf8`](#insn-00affcf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affcfc`](#insn-00affcfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd00`](#insn-00affd00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd28`](#insn-00affd28) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00affd44`](#insn-00affd44) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affd50`](#insn-00affd50) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affd5c`](#insn-00affd5c) → [`00affd90`](#insn-00affd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd78`](#insn-00affd78) → [`00affd64`](#insn-00affd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd80`](#insn-00affd80) → [`00affd90`](#insn-00affd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd8c`](#insn-00affd8c) → [`00affddc`](#insn-00affddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd94`](#insn-00affd94) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affd9c`](#insn-00affd9c) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affdb4`](#insn-00affdb4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00affdc0`](#insn-00affdc0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdc4`](#insn-00affdc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdc8`](#insn-00affdc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdcc`](#insn-00affdcc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdd0`](#insn-00affdd0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affde4`](#insn-00affde4) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affde8`](#insn-00affde8) → [`00affd98`](#insn-00affd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdec`](#insn-00affdec) → [`00affe38`](#insn-00affe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdf4`](#insn-00affdf4) → [`00affe78`](#insn-00affe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdfc`](#insn-00affdfc) → [`00affe10`](#insn-00affe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe0c`](#insn-00affe0c) → [`00affe24`](#insn-00affe24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe20`](#insn-00affe20) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00affe34`](#insn-00affe34) → [`00affe7c`](#insn-00affe7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe60`](#insn-00affe60) → [`00affe90`](#insn-00affe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe68`](#insn-00affe68) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affe74`](#insn-00affe74) → [`00affdc0`](#insn-00affdc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe8c`](#insn-00affe8c) → [`00affe64`](#insn-00affe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe98`](#insn-00affe98) → [`00bddfc0`](../00bdd/00bddfc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfc0` · 推定シンボル `None` · 推定型 `None`
- [`00affe9c`](#insn-00affe9c) → [`00affdb8`](#insn-00affdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affcec`](#insn-00affcec)

~~~json
{
  "source": "00affcec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affcf0`](#insn-00affcf0)

~~~json
{
  "source": "00affcf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affcf4`](#insn-00affcf4)

~~~json
{
  "source": "00affcf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affcf8`](#insn-00affcf8)

~~~json
{
  "source": "00affcf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affcfc`](#insn-00affcfc)

~~~json
{
  "source": "00affcfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd00`](#insn-00affd00)

~~~json
{
  "source": "00affd00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd28`](#insn-00affd28)

~~~json
{
  "source": "00affd28",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd44`](#insn-00affd44)

~~~json
{
  "source": "00affd44",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd50`](#insn-00affd50)

~~~json
{
  "source": "00affd50",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd5c`](#insn-00affd5c)

~~~json
{
  "source": "00affd5c",
  "target": "00affd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd78`](#insn-00affd78)

~~~json
{
  "source": "00affd78",
  "target": "00affd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd80`](#insn-00affd80)

~~~json
{
  "source": "00affd80",
  "target": "00affd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd8c`](#insn-00affd8c)

~~~json
{
  "source": "00affd8c",
  "target": "00affddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd94`](#insn-00affd94)

~~~json
{
  "source": "00affd94",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd9c`](#insn-00affd9c)

~~~json
{
  "source": "00affd9c",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affdb4`](#insn-00affdb4)

~~~json
{
  "source": "00affdb4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affdc0`](#insn-00affdc0)

~~~json
{
  "source": "00affdc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdc4`](#insn-00affdc4)

~~~json
{
  "source": "00affdc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdc8`](#insn-00affdc8)

~~~json
{
  "source": "00affdc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdcc`](#insn-00affdcc)

~~~json
{
  "source": "00affdcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdd0`](#insn-00affdd0)

~~~json
{
  "source": "00affdd0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affde4`](#insn-00affde4)

~~~json
{
  "source": "00affde4",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affde8`](#insn-00affde8)

~~~json
{
  "source": "00affde8",
  "target": "00affd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdec`](#insn-00affdec)

~~~json
{
  "source": "00affdec",
  "target": "00affe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdf4`](#insn-00affdf4)

~~~json
{
  "source": "00affdf4",
  "target": "00affe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdfc`](#insn-00affdfc)

~~~json
{
  "source": "00affdfc",
  "target": "00affe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe0c`](#insn-00affe0c)

~~~json
{
  "source": "00affe0c",
  "target": "00affe24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe20`](#insn-00affe20)

~~~json
{
  "source": "00affe20",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe34`](#insn-00affe34)

~~~json
{
  "source": "00affe34",
  "target": "00affe7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe60`](#insn-00affe60)

~~~json
{
  "source": "00affe60",
  "target": "00affe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe68`](#insn-00affe68)

~~~json
{
  "source": "00affe68",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe74`](#insn-00affe74)

~~~json
{
  "source": "00affe74",
  "target": "00affdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe8c`](#insn-00affe8c)

~~~json
{
  "source": "00affe8c",
  "target": "00affe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe98`](#insn-00affe98)

~~~json
{
  "source": "00affe98",
  "target": "00bddfc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe9c`](#insn-00affe9c)

~~~json
{
  "source": "00affe9c",
  "target": "00affdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
