# 00b5fedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5fab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0075.md#compare-3acb57bea86fdac7273719fef2d6dc07)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5ff78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5ff78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0075.md#compare-4011d109d211301d6763a5b459c207c4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5fedc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c78b314bbcd0279648d1c5a596262bedf428edaca61eb090ec4d2d1283c45766",
  "source_text_sha256": "c78b314bbcd0279648d1c5a596262bedf428edaca61eb090ec4d2d1283c45766",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5fedc",
        "00b6008f"
      ]
    ],
    "bytes_sha256": "059e4a2742cf6c16c32867b7be9927611937281190e66708284b8903f8f98201",
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

- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5ae90](../00c5a/00c5ae90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4122 bytes

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
  
                    /* try { // try from 00b5fef0 to 00c5feff has its CatchHandler @ 00b60068 */
  plVar4 = (long *)_Znwm(0x28);
  lVar1 = param_2 + 8;
                    /* try { // try from 00b5ff24 to 00c5ff3f has its CatchHandler @ 00b60070 */
  *plVar4 = (long)plVar4;
  plVar4[1] = (long)plVar4;
  plVar4[2] = param_4;
  plVar4[3] = param_5;
  plVar4[4] = param_6;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar9 = *param_3;
                    /* try { // try from 00b5ff40 to 00c60097 has its CatchHandler @ 00b5fce8 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar7 = (long *)(param_2 + 0x38);
  plVar8 = (long *)*plVar7;
  plVar5 = plVar7;
  if (plVar8 == (long *)0x0) {
LAB_00b5ff80:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar8[4] >= uVar9) {
        plVar5 = plVar8;
      }
      plVar8 = (long *)plVar8[(ulong)plVar8[4] < uVar9];
    } while (plVar8 != (long *)0x0);
    if ((plVar5 == plVar7) || (uVar9 < (ulong)plVar5[4])) goto LAB_00b5ff80;
    piVar10 = (int *)plVar5[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    if (piVar10 != (int *)0x0) {
      if ((param_7 & 1) == 0) {
        puVar3 = *(undefined8 **)(piVar10 + 0x16);
                    /* catch() { ... } // from try @ 00b5fd9c with catch @ 00b60034 */
                    /* catch() { ... } // from try @ 00b5fd70 with catch @ 00b60038 */
        plVar4 = (long *)((long)plVar4 + *(long *)(piVar10 + 0x18));
        piVar10[8] = piVar10[8] + 1;
        *puVar3 = plVar4;
        *plVar4 = (long)(piVar10 + 0x14);
        plVar4[1] = (long)puVar3;
        *(long **)(piVar10 + 0x16) = plVar4;
        iVar6 = *piVar10;
      }
      else {
        plVar5 = *(long **)(piVar10 + 0x12);
        if (plVar5 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00b5fef0 with catch @ 00b60068 */
          iVar6 = piVar10[8];
        }
        else {
          if ((code *)plVar5[4] == (code *)0x0) {
LAB_00b60000:
            lVar2 = *plVar5;
            *(long *)(lVar2 + 8) = plVar5[1];
            *(long *)plVar5[1] = lVar2;
            _ZdlPv(plVar5);
          }
          else {
            (*(code *)plVar5[4])(plVar5[3]);
            plVar5 = *(long **)(piVar10 + 0x12);
            if (plVar5 != (long *)0x0) goto LAB_00b60000;
          }
          piVar10[0x12] = 0;
          piVar10[0x13] = 0;
          iVar6 = piVar10[8] + -1;
          piVar10[8] = iVar6;
        }
                    /* catch() { ... } // from try @ 00b5fda8 with catch @ 00b6006c */
                    /* catch() { ... } // from try @ 00b5fe4c with catch @ 00b60070
                       catch() { ... } // from try @ 00b5fed0 with catch @ 00b60070
                       catch() { ... } // from try @ 00b5ff24 with catch @ 00b60070 */
        piVar10[8] = iVar6 + 1;
        *(long **)(piVar10 + 0x12) = plVar4;
        iVar6 = *piVar10;
      }
                    /* catch() { ... } // from try @ 00b5fd3c with catch @ 00b60050 */
      if (iVar6 != 0) {
                    /* catch() { ... } // from try @ 00b5fe18 with catch @ 00b60054 */
        _ZN8firebase5Mutex7ReleaseEv(lVar1);
        *param_1 = param_4;
        param_1[1] = param_5;
        param_1[2] = param_6;
        return;
                    /* catch() { ... } // from try @ 00b5fe9c with catch @ 00b60064 */
      }
      _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
                (param_2,param_3);
      goto LAB_00b5ffa8;
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  lVar1 = *plVar4;
  *(long *)(lVar1 + 8) = plVar4[1];
  *(long *)plVar4[1] = lVar1;
  _ZdlPv(plVar4);
LAB_00b5ffa8:
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5fedc"></a> `00b5fedc` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00b5fee0"></a> `00b5fee0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5fee4"></a> `00b5fee4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5fee8"></a> `00b5fee8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5feec"></a> `00b5feec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5fef0"></a> `00b5fef0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5fef4"></a> `00b5fef4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b5fef8"></a> `00b5fef8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00b5fefc"></a> `00b5fefc` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00b5ff00"></a> `00b5ff00` | `fb 03 05 2a` | mov w27,w5 | `FALL_THROUGH`
<a id="insn-00b5ff04"></a> `00b5ff04` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00b5ff08"></a> `00b5ff08` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00b5ff0c"></a> `00b5ff0c` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00b5ff10"></a> `00b5ff10` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00b5ff14"></a> `00b5ff14` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b5ff18"></a> `00b5ff18` | `de df 03 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ff1c"></a> `00b5ff1c` | `1a 23 00 91` | add x26,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00b5ff20"></a> `00b5ff20` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00b5ff24"></a> `00b5ff24` | `00 00 00 a9` | stp x0,x0,[x0] | `FALL_THROUGH`
<a id="insn-00b5ff28"></a> `00b5ff28` | `16 54 01 a9` | stp x22,x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ff2c"></a> `00b5ff2c` | `14 10 00 f9` | str x20,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ff30"></a> `00b5ff30` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b5ff34"></a> `00b5ff34` | `b3 ea 03 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ff38"></a> `00b5ff38` | `fc 02 40 f9` | ldr x28,[x23] | `FALL_THROUGH`
<a id="insn-00b5ff3c"></a> `00b5ff3c` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b5ff40"></a> `00b5ff40` | `b0 ea 03 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ff44"></a> `00b5ff44` | `e9 03 18 aa` | mov x9,x24 | `FALL_THROUGH`
<a id="insn-00b5ff48"></a> `00b5ff48` | `2a 8d 43 f8` | ldr x10,[x9, #0x38]! | `FALL_THROUGH`
<a id="insn-00b5ff4c"></a> `00b5ff4c` | `aa 01 00 b4` | cbz x10,0x00b5ff80 | `CONDITIONAL_JUMP`
<a id="insn-00b5ff50"></a> `00b5ff50` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00b5ff54"></a> `00b5ff54` | `4b 11 40 f9` | ldr x11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ff58"></a> `00b5ff58` | `7f 01 1c eb` | cmp x11,x28 | `FALL_THROUGH`
<a id="insn-00b5ff5c"></a> `00b5ff5c` | `eb 27 9f 1a` | cset w11,cc | `FALL_THROUGH`
<a id="insn-00b5ff60"></a> `00b5ff60` | `08 31 8a 9a` | csel x8,x8,x10,cc | `FALL_THROUGH`
<a id="insn-00b5ff64"></a> `00b5ff64` | `4a 59 6b f8` | ldr x10,[x10, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b5ff68"></a> `00b5ff68` | `6a ff ff b5` | cbnz x10,0x00b5ff54 | `CONDITIONAL_JUMP`
<a id="insn-00b5ff6c"></a> `00b5ff6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5ff70"></a> `00b5ff70` | `80 00 00 54` | b.eq 0x00b5ff80 | `CONDITIONAL_JUMP`
<a id="insn-00b5ff74"></a> `00b5ff74` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ff78"></a> `00b5ff78` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-00b5ff7c"></a> `00b5ff7c` | `89 02 00 54` | b.ls 0x00b5ffcc | `CONDITIONAL_JUMP`
<a id="insn-00b5ff80"></a> `00b5ff80` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b5ff84"></a> `00b5ff84` | `a3 ea 03 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ff88"></a> `00b5ff88` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b5ff8c"></a> `00b5ff8c` | `a1 ea 03 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ff90"></a> `00b5ff90` | `28 27 40 a9` | ldp x8,x9,[x25] | `FALL_THROUGH`
<a id="insn-00b5ff94"></a> `00b5ff94` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00b5ff98"></a> `00b5ff98` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b5ff9c"></a> `00b5ff9c` | `29 07 40 f9` | ldr x9,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00b5ffa0"></a> `00b5ffa0` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b5ffa4"></a> `00b5ffa4` | `c3 df 03 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ffa8"></a> `00b5ffa8` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b5ffac"></a> `00b5ffac` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ffb0"></a> `00b5ffb0` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5ffb4"></a> `00b5ffb4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5ffb8"></a> `00b5ffb8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5ffbc"></a> `00b5ffbc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ffc0"></a> `00b5ffc0` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ffc4"></a> `00b5ffc4` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00b5ffc8"></a> `00b5ffc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5ffcc"></a> `00b5ffcc` | `1c 15 40 f9` | ldr x28,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ffd0"></a> `00b5ffd0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b5ffd4"></a> `00b5ffd4` | `8f ea 03 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ffd8"></a> `00b5ffd8` | `9c fd ff b4` | cbz x28,0x00b5ff88 | `CONDITIONAL_JUMP`
<a id="insn-00b5ffdc"></a> `00b5ffdc` | `7b 02 00 36` | tbz w27,#0x0,0x00b60028 | `CONDITIONAL_JUMP`
<a id="insn-00b5ffe0"></a> `00b5ffe0` | `80 27 40 f9` | ldr x0,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00b5ffe4"></a> `00b5ffe4` | `20 04 00 b4` | cbz x0,0x00b60068 | `CONDITIONAL_JUMP`
<a id="insn-00b5ffe8"></a> `00b5ffe8` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ffec"></a> `00b5ffec` | `a8 00 00 b4` | cbz x8,0x00b60000 | `CONDITIONAL_JUMP`
<a id="insn-00b5fff0"></a> `00b5fff0` | `00 0c 40 f9` | ldr x0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00b5fff4"></a> `00b5fff4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5fff8"></a> `00b5fff8` | `80 27 40 f9` | ldr x0,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00b5fffc"></a> `00b5fffc` | `c0 00 00 b4` | cbz x0,0x00b60014 | `CONDITIONAL_JUMP`
<a id="insn-00b60000"></a> `00b60000` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00b60004"></a> `00b60004` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b60008"></a> `00b60008` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b6000c"></a> `00b6000c` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b60010"></a> `00b60010` | `a8 df 03 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b60014"></a> `00b60014` | `88 23 40 b9` | ldr w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00b60018"></a> `00b60018` | `9f 27 00 f9` | str xzr,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00b6001c"></a> `00b6001c` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b60020"></a> `00b60020` | `88 23 00 b9` | str w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00b60024"></a> `00b60024` | `12 00 00 14` | b 0x00b6006c | `UNCONDITIONAL_JUMP`
<a id="insn-00b60028"></a> `00b60028` | `88 23 40 b9` | ldr w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00b6002c"></a> `00b6002c` | `8a a7 45 a9` | ldp x10,x9,[x28, #0x58] | `FALL_THROUGH`
<a id="insn-00b60030"></a> `00b60030` | `8b 43 01 91` | add x11,x28,#0x50 | `FALL_THROUGH`
<a id="insn-00b60034"></a> `00b60034` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b60038"></a> `00b60038` | `29 03 09 8b` | add x9,x25,x9 | `FALL_THROUGH`
<a id="insn-00b6003c"></a> `00b6003c` | `88 23 00 b9` | str w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00b60040"></a> `00b60040` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00b60044"></a> `00b60044` | `2b 29 00 a9` | stp x11,x10,[x9] | `FALL_THROUGH`
<a id="insn-00b60048"></a> `00b60048` | `89 2f 00 f9` | str x9,[x28, #0x58] | `FALL_THROUGH`
<a id="insn-00b6004c"></a> `00b6004c` | `88 03 40 b9` | ldr w8,[x28] | `FALL_THROUGH`
<a id="insn-00b60050"></a> `00b60050` | `88 01 00 34` | cbz w8,0x00b60080 | `CONDITIONAL_JUMP`
<a id="insn-00b60054"></a> `00b60054` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b60058"></a> `00b60058` | `6e ea 03 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00b6005c"></a> `00b6005c` | `76 56 00 a9` | stp x22,x21,[x19] | `FALL_THROUGH`
<a id="insn-00b60060"></a> `00b60060` | `74 0a 00 f9` | str x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b60064"></a> `00b60064` | `d3 ff ff 17` | b 0x00b5ffb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b60068"></a> `00b60068` | `88 23 40 b9` | ldr w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00b6006c"></a> `00b6006c` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b60070"></a> `00b60070` | `88 23 00 b9` | str w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00b60074"></a> `00b60074` | `99 27 00 f9` | str x25,[x28, #0x48] | `FALL_THROUGH`
<a id="insn-00b60078"></a> `00b60078` | `88 03 40 b9` | ldr w8,[x28] | `FALL_THROUGH`
<a id="insn-00b6007c"></a> `00b6007c` | `c8 fe ff 35` | cbnz w8,0x00b60054 | `CONDITIONAL_JUMP`
<a id="insn-00b60080"></a> `00b60080` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b60084"></a> `00b60084` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b60088"></a> `00b60088` | `82 eb 03 94` | bl 0x00c5ae90 | `UNCONDITIONAL_CALL`
<a id="insn-00b6008c"></a> `00b6008c` | `c7 ff ff 17` | b 0x00b5ffa8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b5fedc`](#insn-00b5fedc) 範囲 `[['00b5fedc', '00b5feef']]`
  - `FALL_THROUGH` [`00b5feec`](#insn-00b5feec) → [`00b5fef0`](#insn-00b5fef0)
- ブロック [`00b5fef0`](#insn-00b5fef0) 範囲 `[['00b5fef0', '00b5ff23']]`
  - `FALL_THROUGH` [`00b5ff20`](#insn-00b5ff20) → [`00b5ff24`](#insn-00b5ff24)
- ブロック [`00b5ff24`](#insn-00b5ff24) 範囲 `[['00b5ff24', '00b5ff3f']]`
  - `FALL_THROUGH` [`00b5ff3c`](#insn-00b5ff3c) → [`00b5ff40`](#insn-00b5ff40)
- ブロック [`00b5ff40`](#insn-00b5ff40) 範囲 `[['00b5ff40', '00b5ff4f']]`
  - `CONDITIONAL_JUMP` [`00b5ff4c`](#insn-00b5ff4c) → [`00b5ff80`](#insn-00b5ff80)
  - `FALL_THROUGH` [`00b5ff4c`](#insn-00b5ff4c) → [`00b5ff50`](#insn-00b5ff50)
- ブロック [`00b5ff50`](#insn-00b5ff50) 範囲 `[['00b5ff50', '00b5ff53']]`
  - `FALL_THROUGH` [`00b5ff50`](#insn-00b5ff50) → [`00b5ff54`](#insn-00b5ff54)
- ブロック [`00b5ff54`](#insn-00b5ff54) 範囲 `[['00b5ff54', '00b5ff6b']]`
  - `CONDITIONAL_JUMP` [`00b5ff68`](#insn-00b5ff68) → [`00b5ff54`](#insn-00b5ff54)
  - `FALL_THROUGH` [`00b5ff68`](#insn-00b5ff68) → [`00b5ff6c`](#insn-00b5ff6c)
- ブロック [`00b5ff6c`](#insn-00b5ff6c) 範囲 `[['00b5ff6c', '00b5ff73']]`
  - `CONDITIONAL_JUMP` [`00b5ff70`](#insn-00b5ff70) → [`00b5ff80`](#insn-00b5ff80)
  - `FALL_THROUGH` [`00b5ff70`](#insn-00b5ff70) → [`00b5ff74`](#insn-00b5ff74)
- ブロック [`00b5ff74`](#insn-00b5ff74) 範囲 `[['00b5ff74', '00b5ff7f']]`
  - `CONDITIONAL_JUMP` [`00b5ff7c`](#insn-00b5ff7c) → [`00b5ffcc`](#insn-00b5ffcc)
  - `FALL_THROUGH` [`00b5ff7c`](#insn-00b5ff7c) → [`00b5ff80`](#insn-00b5ff80)
- ブロック [`00b5ff80`](#insn-00b5ff80) 範囲 `[['00b5ff80', '00b5ff87']]`
  - `FALL_THROUGH` [`00b5ff84`](#insn-00b5ff84) → [`00b5ff88`](#insn-00b5ff88)
- ブロック [`00b5ff88`](#insn-00b5ff88) 範囲 `[['00b5ff88', '00b5ffa7']]`
  - `FALL_THROUGH` [`00b5ffa4`](#insn-00b5ffa4) → [`00b5ffa8`](#insn-00b5ffa8)
- ブロック [`00b5ffa8`](#insn-00b5ffa8) 範囲 `[['00b5ffa8', '00b5ffaf']]`
  - `FALL_THROUGH` [`00b5ffac`](#insn-00b5ffac) → [`00b5ffb0`](#insn-00b5ffb0)
- ブロック [`00b5ffb0`](#insn-00b5ffb0) 範囲 `[['00b5ffb0', '00b5ffcb']]`
- ブロック [`00b5ffcc`](#insn-00b5ffcc) 範囲 `[['00b5ffcc', '00b5ffdb']]`
  - `CONDITIONAL_JUMP` [`00b5ffd8`](#insn-00b5ffd8) → [`00b5ff88`](#insn-00b5ff88)
  - `FALL_THROUGH` [`00b5ffd8`](#insn-00b5ffd8) → [`00b5ffdc`](#insn-00b5ffdc)
- ブロック [`00b5ffdc`](#insn-00b5ffdc) 範囲 `[['00b5ffdc', '00b5ffdf']]`
  - `CONDITIONAL_JUMP` [`00b5ffdc`](#insn-00b5ffdc) → [`00b60028`](#insn-00b60028)
  - `FALL_THROUGH` [`00b5ffdc`](#insn-00b5ffdc) → [`00b5ffe0`](#insn-00b5ffe0)
- ブロック [`00b5ffe0`](#insn-00b5ffe0) 範囲 `[['00b5ffe0', '00b5ffe7']]`
  - `CONDITIONAL_JUMP` [`00b5ffe4`](#insn-00b5ffe4) → [`00b60068`](#insn-00b60068)
  - `FALL_THROUGH` [`00b5ffe4`](#insn-00b5ffe4) → [`00b5ffe8`](#insn-00b5ffe8)
- ブロック [`00b5ffe8`](#insn-00b5ffe8) 範囲 `[['00b5ffe8', '00b5ffef']]`
  - `CONDITIONAL_JUMP` [`00b5ffec`](#insn-00b5ffec) → [`00b60000`](#insn-00b60000)
  - `FALL_THROUGH` [`00b5ffec`](#insn-00b5ffec) → [`00b5fff0`](#insn-00b5fff0)
- ブロック [`00b5fff0`](#insn-00b5fff0) 範囲 `[['00b5fff0', '00b5ffff']]`
  - `CONDITIONAL_JUMP` [`00b5fffc`](#insn-00b5fffc) → [`00b60014`](#insn-00b60014)
  - `FALL_THROUGH` [`00b5fffc`](#insn-00b5fffc) → [`00b60000`](#insn-00b60000)
- ブロック [`00b60000`](#insn-00b60000) 範囲 `[['00b60000', '00b60013']]`
  - `FALL_THROUGH` [`00b60010`](#insn-00b60010) → [`00b60014`](#insn-00b60014)
- ブロック [`00b60014`](#insn-00b60014) 範囲 `[['00b60014', '00b60027']]`
  - `UNCONDITIONAL_JUMP` [`00b60024`](#insn-00b60024) → [`00b6006c`](#insn-00b6006c)
- ブロック [`00b60028`](#insn-00b60028) 範囲 `[['00b60028', '00b60033']]`
  - `FALL_THROUGH` [`00b60030`](#insn-00b60030) → [`00b60034`](#insn-00b60034)
- ブロック [`00b60034`](#insn-00b60034) 範囲 `[['00b60034', '00b60037']]`
  - `FALL_THROUGH` [`00b60034`](#insn-00b60034) → [`00b60038`](#insn-00b60038)
- ブロック [`00b60038`](#insn-00b60038) 範囲 `[['00b60038', '00b6004f']]`
  - `FALL_THROUGH` [`00b6004c`](#insn-00b6004c) → [`00b60050`](#insn-00b60050)
- ブロック [`00b60050`](#insn-00b60050) 範囲 `[['00b60050', '00b60053']]`
  - `CONDITIONAL_JUMP` [`00b60050`](#insn-00b60050) → [`00b60080`](#insn-00b60080)
  - `FALL_THROUGH` [`00b60050`](#insn-00b60050) → [`00b60054`](#insn-00b60054)
- ブロック [`00b60054`](#insn-00b60054) 範囲 `[['00b60054', '00b60063']]`
  - `FALL_THROUGH` [`00b60060`](#insn-00b60060) → [`00b60064`](#insn-00b60064)
- ブロック [`00b60064`](#insn-00b60064) 範囲 `[['00b60064', '00b60067']]`
  - `UNCONDITIONAL_JUMP` [`00b60064`](#insn-00b60064) → [`00b5ffb0`](#insn-00b5ffb0)
- ブロック [`00b60068`](#insn-00b60068) 範囲 `[['00b60068', '00b6006b']]`
  - `FALL_THROUGH` [`00b60068`](#insn-00b60068) → [`00b6006c`](#insn-00b6006c)
- ブロック [`00b6006c`](#insn-00b6006c) 範囲 `[['00b6006c', '00b6006f']]`
  - `FALL_THROUGH` [`00b6006c`](#insn-00b6006c) → [`00b60070`](#insn-00b60070)
- ブロック [`00b60070`](#insn-00b60070) 範囲 `[['00b60070', '00b6007f']]`
  - `CONDITIONAL_JUMP` [`00b6007c`](#insn-00b6007c) → [`00b60054`](#insn-00b60054)
  - `FALL_THROUGH` [`00b6007c`](#insn-00b6007c) → [`00b60080`](#insn-00b60080)
- ブロック [`00b60080`](#insn-00b60080) 範囲 `[['00b60080', '00b6008f']]`
  - `UNCONDITIONAL_JUMP` [`00b6008c`](#insn-00b6008c) → [`00b5ffa8`](#insn-00b5ffa8)

## 命令位置別の参照

- [`00b5fedc`](#insn-00b5fedc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fee0`](#insn-00b5fee0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fee4`](#insn-00b5fee4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fee8`](#insn-00b5fee8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5feec`](#insn-00b5feec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fef0`](#insn-00b5fef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff18`](#insn-00b5ff18) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff34`](#insn-00b5ff34) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff40`](#insn-00b5ff40) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff4c`](#insn-00b5ff4c) → [`00b5ff80`](#insn-00b5ff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff68`](#insn-00b5ff68) → [`00b5ff54`](#insn-00b5ff54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff70`](#insn-00b5ff70) → [`00b5ff80`](#insn-00b5ff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff7c`](#insn-00b5ff7c) → [`00b5ffcc`](#insn-00b5ffcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff84`](#insn-00b5ff84) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00b5ff8c`](#insn-00b5ff8c) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffa4`](#insn-00b5ffa4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffb0`](#insn-00b5ffb0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffb4`](#insn-00b5ffb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffb8`](#insn-00b5ffb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffbc`](#insn-00b5ffbc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffc0`](#insn-00b5ffc0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffd4`](#insn-00b5ffd4) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffd8`](#insn-00b5ffd8) → [`00b5ff88`](#insn-00b5ff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffdc`](#insn-00b5ffdc) → [`00b60028`](#insn-00b60028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffe4`](#insn-00b5ffe4) → [`00b60068`](#insn-00b60068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ffec`](#insn-00b5ffec) → [`00b60000`](#insn-00b60000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fffc`](#insn-00b5fffc) → [`00b60014`](#insn-00b60014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60010`](#insn-00b60010) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b60024`](#insn-00b60024) → [`00b6006c`](#insn-00b6006c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60050`](#insn-00b60050) → [`00b60080`](#insn-00b60080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60058`](#insn-00b60058) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00b60064`](#insn-00b60064) → [`00b5ffb0`](#insn-00b5ffb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6007c`](#insn-00b6007c) → [`00b60054`](#insn-00b60054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60088`](#insn-00b60088) → [`00c5ae90`](../00c5a/00c5ae90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae90` · 推定シンボル `None` · 推定型 `None`
- [`00b6008c`](#insn-00b6008c) → [`00b5ffa8`](#insn-00b5ffa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5fedc`](#insn-00b5fedc)

~~~json
{
  "source": "00b5fedc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fee0`](#insn-00b5fee0)

~~~json
{
  "source": "00b5fee0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fee4`](#insn-00b5fee4)

~~~json
{
  "source": "00b5fee4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fee8`](#insn-00b5fee8)

~~~json
{
  "source": "00b5fee8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5feec`](#insn-00b5feec)

~~~json
{
  "source": "00b5feec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fef0`](#insn-00b5fef0)

~~~json
{
  "source": "00b5fef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ff18`](#insn-00b5ff18)

~~~json
{
  "source": "00b5ff18",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ff34`](#insn-00b5ff34)

~~~json
{
  "source": "00b5ff34",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ff40`](#insn-00b5ff40)

~~~json
{
  "source": "00b5ff40",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ff4c`](#insn-00b5ff4c)

~~~json
{
  "source": "00b5ff4c",
  "target": "00b5ff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ff68`](#insn-00b5ff68)

~~~json
{
  "source": "00b5ff68",
  "target": "00b5ff54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ff70`](#insn-00b5ff70)

~~~json
{
  "source": "00b5ff70",
  "target": "00b5ff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ff7c`](#insn-00b5ff7c)

~~~json
{
  "source": "00b5ff7c",
  "target": "00b5ffcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ff84`](#insn-00b5ff84)

~~~json
{
  "source": "00b5ff84",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ff8c`](#insn-00b5ff8c)

~~~json
{
  "source": "00b5ff8c",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ffa4`](#insn-00b5ffa4)

~~~json
{
  "source": "00b5ffa4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ffb0`](#insn-00b5ffb0)

~~~json
{
  "source": "00b5ffb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffb4`](#insn-00b5ffb4)

~~~json
{
  "source": "00b5ffb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffb8`](#insn-00b5ffb8)

~~~json
{
  "source": "00b5ffb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffbc`](#insn-00b5ffbc)

~~~json
{
  "source": "00b5ffbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffc0`](#insn-00b5ffc0)

~~~json
{
  "source": "00b5ffc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffd4`](#insn-00b5ffd4)

~~~json
{
  "source": "00b5ffd4",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ffd8`](#insn-00b5ffd8)

~~~json
{
  "source": "00b5ffd8",
  "target": "00b5ff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffdc`](#insn-00b5ffdc)

~~~json
{
  "source": "00b5ffdc",
  "target": "00b60028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffe4`](#insn-00b5ffe4)

~~~json
{
  "source": "00b5ffe4",
  "target": "00b60068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ffec`](#insn-00b5ffec)

~~~json
{
  "source": "00b5ffec",
  "target": "00b60000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fffc`](#insn-00b5fffc)

~~~json
{
  "source": "00b5fffc",
  "target": "00b60014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60010`](#insn-00b60010)

~~~json
{
  "source": "00b60010",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b60024`](#insn-00b60024)

~~~json
{
  "source": "00b60024",
  "target": "00b6006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60050`](#insn-00b60050)

~~~json
{
  "source": "00b60050",
  "target": "00b60080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60058`](#insn-00b60058)

~~~json
{
  "source": "00b60058",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b60064`](#insn-00b60064)

~~~json
{
  "source": "00b60064",
  "target": "00b5ffb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6007c`](#insn-00b6007c)

~~~json
{
  "source": "00b6007c",
  "target": "00b60054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60088`](#insn-00b60088)

~~~json
{
  "source": "00b60088",
  "target": "00c5ae90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6008c`](#insn-00b6008c)

~~~json
{
  "source": "00b6008c",
  "target": "00b5ffa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
