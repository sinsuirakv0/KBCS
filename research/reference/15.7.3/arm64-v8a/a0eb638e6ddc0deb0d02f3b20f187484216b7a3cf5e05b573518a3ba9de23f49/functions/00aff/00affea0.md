# 00affea0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00affdd8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affdd8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-7c239d1eed0edf952ede779009713033)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00affee4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affee4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-f96a3fbe24ee7b316a3fff42097c3052)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affea0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "222e032304dea08d8e5ae745c6164bfbd8b9b32ddc7e42803b792b77da34d3b6",
  "source_text_sha256": "222e032304dea08d8e5ae745c6164bfbd8b9b32ddc7e42803b792b77da34d3b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affea0",
        "00b00093"
      ]
    ],
    "bytes_sha256": "34c267858a322ae36c5da5cdc2d842f978ceb3ab7c42132fa15016eb8160ebdd",
    "instruction_count": 125,
    "instruction_bytes": 500,
    "body_bytes": 500,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6511 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE
               (long param_1,ulong *param_2,long *param_3)

{
  long lVar1;
  long lVar2;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long lVar7;
  ulong uVar8;
  undefined1 *local_70;
  undefined8 *local_68;
  long local_60;
  long lStack_58;
  code *local_50;
  long local_48;
  
                    /* catch() { ... } // from try @ 00af5914 with catch @ 00affea4 */
                    /* catch() { ... } // from try @ 00af5908 with catch @ 00affeac */
                    /* catch() { ... } // from try @ 00af58fc with catch @ 00affeb4 */
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00af58f0 with catch @ 00affebc */
  local_48 = *(long *)(lVar3 + 0x28);
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af58e4 with catch @ 00affec4 */
                    /* catch() { ... } // from try @ 00af58d8 with catch @ 00affecc */
                    /* catch() { ... } // from try @ 00af58cc with catch @ 00affed4 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af58c0 with catch @ 00affedc */
  uVar8 = *param_2;
                    /* catch() { ... } // from try @ 00af58b4 with catch @ 00affee4 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar6 = (long *)(param_1 + 0x38);
  plVar5 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00af58a8 with catch @ 00affeec */
  plVar4 = plVar6;
  if (plVar5 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af589c with catch @ 00affef4 */
                    /* catch() { ... } // from try @ 00af5828 with catch @ 00affefc */
      if ((ulong)plVar5[4] >= uVar8) {
        plVar4 = plVar5;
      }
                    /* catch() { ... } // from try @ 00af581c with catch @ 00afff04 */
      plVar5 = (long *)plVar5[(ulong)plVar5[4] < uVar8];
    } while (plVar5 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5810 with catch @ 00afff0c */
                    /* catch() { ... } // from try @ 00af5804 with catch @ 00afff14 */
                    /* catch() { ... } // from try @ 00af5750 with catch @ 00afff1c */
    if ((plVar4 != plVar6) && ((ulong)plVar4[4] <= uVar8)) {
      lVar7 = plVar4[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      if (lVar7 == 0) goto LAB_00afff28;
      local_60 = *param_3;
      lStack_58 = param_3[1];
      local_50 = (code *)param_3[2];
      plVar4 = *(long **)(lVar7 + 0x48);
      local_70 = (undefined1 *)&local_70;
      local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af5d2c with catch @ 00afff94 */
      if ((((plVar4 != (long *)0x0) &&
           (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[2] == local_60)) &&
          (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[3] == lStack_58)) &&
         (local_70 = (undefined1 *)&local_70, local_68 = &local_70, (code *)plVar4[4] == local_50))
      {
        local_70 = (undefined1 *)&local_70;
        local_68 = &local_70;
        if (local_50 == (code *)0x0) {
LAB_00afffc0:
          lVar2 = *plVar4;
          *(long *)(lVar2 + 8) = plVar4[1];
          *(long *)plVar4[1] = lVar2;
          _ZdlPv(plVar4);
        }
        else {
          local_70 = (undefined1 *)&local_70;
          local_68 = &local_70;
          (*local_50)(lStack_58);
          plVar4 = *(long **)(lVar7 + 0x48);
          if (plVar4 != (long *)0x0) goto LAB_00afffc0;
        }
                    /* catch() { ... } // from try @ 00af5d04 with catch @ 00afffd8 */
        *(undefined8 *)(lVar7 + 0x48) = 0;
        *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
      }
      plVar5 = (long *)(lVar7 + 0x50);
      plVar4 = (long *)*plVar5;
      if (plVar5 != plVar4) {
        do {
          plVar6 = (long *)((long)plVar4 - *(long *)(lVar7 + 0x60));
                    /* catch() { ... } // from try @ 00af5a38 with catch @ 00b0001c */
          if (((plVar6[2] == local_60) && (plVar6[3] == lStack_58)) &&
             ((code *)plVar6[4] == local_50)) {
            lVar2 = *plVar4;
            *(long *)(lVar2 + 8) = plVar4[1];
            *(long *)plVar4[1] = lVar2;
            *plVar4 = (long)plVar4;
            plVar4[1] = (long)plVar4;
            if (plVar6 != (long *)0x0) {
              if (local_50 != (code *)0x0) {
                (*local_50)();
              }
              lVar2 = *plVar6;
                    /* catch() { ... } // from try @ 00af60f0 with catch @ 00b00060 */
              *(long *)(lVar2 + 8) = plVar6[1];
              *(long *)plVar6[1] = lVar2;
              _ZdlPv(plVar6);
                    /* catch() { ... } // from try @ 00af5b5c with catch @ 00b00070 */
              *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
            }
            break;
          }
          plVar4 = (long *)*plVar4;
        } while (plVar5 != plVar4);
      }
      *(undefined8 **)(local_70 + 8) = local_68;
      *local_68 = local_70;
      goto LAB_00afff28;
    }
  }
                    /* catch() { ... } // from try @ 00af5724 with catch @ 00afff24 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
LAB_00afff28:
                    /* catch() { ... } // from try @ 00af56c0 with catch @ 00afff2c */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5660 with catch @ 00afff34 */
                    /* catch() { ... } // from try @ 00afac7c with catch @ 00afff3c */
  if (*(long *)(lVar3 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00afaab0 with catch @ 00afff40 */
                    /* catch() { ... } // from try @ 00afa888 with catch @ 00afff44
                       catch() { ... } // from try @ 00afa8f8 with catch @ 00afff44 */
                    /* catch() { ... } // from try @ 00afa874 with catch @ 00afff48
                       catch() { ... } // from try @ 00afa8e4 with catch @ 00afff48 */
                    /* catch() { ... } // from try @ 00afa83c with catch @ 00afff4c
                       catch() { ... } // from try @ 00afa8bc with catch @ 00afff4c */
                    /* catch() { ... } // from try @ 00af7398 with catch @ 00afff50 */
                    /* catch() { ... } // from try @ 00af6160 with catch @ 00afff54 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affea0"></a> `00affea0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00affea4"></a> `00affea4` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affea8"></a> `00affea8` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00affeac"></a> `00affeac` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00affeb0"></a> `00affeb0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00affeb4"></a> `00affeb4` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00affeb8"></a> `00affeb8` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00affebc"></a> `00affebc` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00affec0"></a> `00affec0` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affec4"></a> `00affec4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00affec8"></a> `00affec8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affecc"></a> `00affecc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00affed0"></a> `00affed0` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00affed4"></a> `00affed4` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00affed8"></a> `00affed8` | `3e 77 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affedc"></a> `00affedc` | `d6 02 40 f9` | ldr x22,[x22] | `FALL_THROUGH`
<a id="insn-00affee0"></a> `00affee0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affee4"></a> `00affee4` | `3b 77 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affee8"></a> `00affee8` | `a9 8e 43 f8` | ldr x9,[x21, #0x38]! | `FALL_THROUGH`
<a id="insn-00affeec"></a> `00affeec` | `a9 01 00 b4` | cbz x9,0x00afff20 | `CONDITIONAL_JUMP`
<a id="insn-00affef0"></a> `00affef0` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00affef4"></a> `00affef4` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affef8"></a> `00affef8` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00affefc"></a> `00affefc` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00afff00"></a> `00afff00` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00afff04"></a> `00afff04` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afff08"></a> `00afff08` | `69 ff ff b5` | cbnz x9,0x00affef4 | `CONDITIONAL_JUMP`
<a id="insn-00afff0c"></a> `00afff0c` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00afff10"></a> `00afff10` | `80 00 00 54` | b.eq 0x00afff20 | `CONDITIONAL_JUMP`
<a id="insn-00afff14"></a> `00afff14` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afff18"></a> `00afff18` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00afff1c"></a> `00afff1c` | `e9 01 00 54` | b.ls 0x00afff58 | `CONDITIONAL_JUMP`
<a id="insn-00afff20"></a> `00afff20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afff24"></a> `00afff24` | `2f 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afff28"></a> `00afff28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afff2c"></a> `00afff2c` | `2d 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afff30"></a> `00afff30` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00afff34"></a> `00afff34` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afff38"></a> `00afff38` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afff3c"></a> `00afff3c` | `a1 0a 00 54` | b.ne 0x00b00090 | `CONDITIONAL_JUMP`
<a id="insn-00afff40"></a> `00afff40` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afff44"></a> `00afff44` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afff48"></a> `00afff48` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afff4c"></a> `00afff4c` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afff50"></a> `00afff50` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afff54"></a> `00afff54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afff58"></a> `00afff58` | `15 15 40 f9` | ldr x21,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00afff5c"></a> `00afff5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afff60"></a> `00afff60` | `20 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afff64"></a> `00afff64` | `35 fe ff b4` | cbz x21,0x00afff28 | `CONDITIONAL_JUMP`
<a id="insn-00afff68"></a> `00afff68` | `8a 22 40 a9` | ldp x10,x8,[x20] | `FALL_THROUGH`
<a id="insn-00afff6c"></a> `00afff6c` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afff70"></a> `00afff70` | `eb 03 00 91` | mov x11,sp | `FALL_THROUGH`
<a id="insn-00afff74"></a> `00afff74` | `eb 2f 00 a9` | stp x11,x11,[sp] | `FALL_THROUGH`
<a id="insn-00afff78"></a> `00afff78` | `ea 23 01 a9` | stp x10,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afff7c"></a> `00afff7c` | `e9 13 00 f9` | str x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afff80"></a> `00afff80` | `a0 26 40 f9` | ldr x0,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00afff84"></a> `00afff84` | `00 03 00 b4` | cbz x0,0x00afffe4 | `CONDITIONAL_JUMP`
<a id="insn-00afff88"></a> `00afff88` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afff8c"></a> `00afff8c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00afff90"></a> `00afff90` | `a1 02 00 54` | b.ne 0x00afffe4 | `CONDITIONAL_JUMP`
<a id="insn-00afff94"></a> `00afff94` | `0a 0c 40 f9` | ldr x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00afff98"></a> `00afff98` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00afff9c"></a> `00afff9c` | `41 02 00 54` | b.ne 0x00afffe4 | `CONDITIONAL_JUMP`
<a id="insn-00afffa0"></a> `00afffa0` | `0a 10 40 f9` | ldr x10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00afffa4"></a> `00afffa4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00afffa8"></a> `00afffa8` | `e1 01 00 54` | b.ne 0x00afffe4 | `CONDITIONAL_JUMP`
<a id="insn-00afffac"></a> `00afffac` | `a9 00 00 b4` | cbz x9,0x00afffc0 | `CONDITIONAL_JUMP`
<a id="insn-00afffb0"></a> `00afffb0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00afffb4"></a> `00afffb4` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00afffb8"></a> `00afffb8` | `a0 26 40 f9` | ldr x0,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00afffbc"></a> `00afffbc` | `c0 00 00 b4` | cbz x0,0x00afffd4 | `CONDITIONAL_JUMP`
<a id="insn-00afffc0"></a> `00afffc0` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00afffc4"></a> `00afffc4` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afffc8"></a> `00afffc8` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afffcc"></a> `00afffcc` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00afffd0"></a> `00afffd0` | `10 6c 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afffd4"></a> `00afffd4` | `a8 22 40 b9` | ldr w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00afffd8"></a> `00afffd8` | `bf 26 00 f9` | str xzr,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00afffdc"></a> `00afffdc` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afffe0"></a> `00afffe0` | `a8 22 00 b9` | str w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00afffe4"></a> `00afffe4` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-00afffe8"></a> `00afffe8` | `48 0d 45 f8` | ldr x8,[x10, #0x50]! | `FALL_THROUGH`
<a id="insn-00afffec"></a> `00afffec` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00affff0"></a> `00affff0` | `60 04 00 54` | b.eq 0x00b0007c | `CONDITIONAL_JUMP`
<a id="insn-00affff4"></a> `00affff4` | `4b 09 40 f9` | ldr x11,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00affff8"></a> `00affff8` | `ec 03 41 a9` | ldp x12,x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affffc"></a> `00affffc` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b00000"></a> `00b00000` | `04 00 00 14` | b 0x00b00010 | `UNCONDITIONAL_JUMP`
<a id="insn-00b00004"></a> `00b00004` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b00008"></a> `00b00008` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b0000c"></a> `00b0000c` | `80 03 00 54` | b.eq 0x00b0007c | `CONDITIONAL_JUMP`
<a id="insn-00b00010"></a> `00b00010` | `14 01 0b cb` | sub x20,x8,x11 | `FALL_THROUGH`
<a id="insn-00b00014"></a> `00b00014` | `8d 0a 40 f9` | ldr x13,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b00018"></a> `00b00018` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0001c"></a> `00b0001c` | `41 ff ff 54` | b.ne 0x00b00004 | `CONDITIONAL_JUMP`
<a id="insn-00b00020"></a> `00b00020` | `8d 0e 40 f9` | ldr x13,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00b00024"></a> `00b00024` | `bf 01 00 eb` | cmp x13,x0 | `FALL_THROUGH`
<a id="insn-00b00028"></a> `00b00028` | `e1 fe ff 54` | b.ne 0x00b00004 | `CONDITIONAL_JUMP`
<a id="insn-00b0002c"></a> `00b0002c` | `8d 12 40 f9` | ldr x13,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b00030"></a> `00b00030` | `bf 01 09 eb` | cmp x13,x9 | `FALL_THROUGH`
<a id="insn-00b00034"></a> `00b00034` | `81 fe ff 54` | b.ne 0x00b00004 | `CONDITIONAL_JUMP`
<a id="insn-00b00038"></a> `00b00038` | `0a 2d 40 a9` | ldp x10,x11,[x8] | `FALL_THROUGH`
<a id="insn-00b0003c"></a> `00b0003c` | `4b 05 00 f9` | str x11,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00b00040"></a> `00b00040` | `0b 05 40 f9` | ldr x11,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b00044"></a> `00b00044` | `6a 01 00 f9` | str x10,[x11] | `FALL_THROUGH`
<a id="insn-00b00048"></a> `00b00048` | `08 21 00 a9` | stp x8,x8,[x8] | `FALL_THROUGH`
<a id="insn-00b0004c"></a> `00b0004c` | `94 01 00 b4` | cbz x20,0x00b0007c | `CONDITIONAL_JUMP`
<a id="insn-00b00050"></a> `00b00050` | `49 00 00 b4` | cbz x9,0x00b00058 | `CONDITIONAL_JUMP`
<a id="insn-00b00054"></a> `00b00054` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b00058"></a> `00b00058` | `88 26 40 a9` | ldp x8,x9,[x20] | `FALL_THROUGH`
<a id="insn-00b0005c"></a> `00b0005c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b00060"></a> `00b00060` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b00064"></a> `00b00064` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b00068"></a> `00b00068` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b0006c"></a> `00b0006c` | `e9 6b 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b00070"></a> `00b00070` | `a8 22 40 b9` | ldr w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00b00074"></a> `00b00074` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b00078"></a> `00b00078` | `a8 22 00 b9` | str w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00b0007c"></a> `00b0007c` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00b00080"></a> `00b00080` | `28 05 00 f9` | str x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00b00084"></a> `00b00084` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b00088"></a> `00b00088` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00b0008c"></a> `00b0008c` | `a7 ff ff 17` | b 0x00afff28 | `UNCONDITIONAL_JUMP`
<a id="insn-00b00090"></a> `00b00090` | `ec 6b 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affea0`](#insn-00affea0) 範囲 `[['00affea0', '00affea3']]`
  - `FALL_THROUGH` [`00affea0`](#insn-00affea0) → [`00affea4`](#insn-00affea4)
- ブロック [`00affea4`](#insn-00affea4) 範囲 `[['00affea4', '00affeab']]`
  - `FALL_THROUGH` [`00affea8`](#insn-00affea8) → [`00affeac`](#insn-00affeac)
- ブロック [`00affeac`](#insn-00affeac) 範囲 `[['00affeac', '00affeb3']]`
  - `FALL_THROUGH` [`00affeb0`](#insn-00affeb0) → [`00affeb4`](#insn-00affeb4)
- ブロック [`00affeb4`](#insn-00affeb4) 範囲 `[['00affeb4', '00affebb']]`
  - `FALL_THROUGH` [`00affeb8`](#insn-00affeb8) → [`00affebc`](#insn-00affebc)
- ブロック [`00affebc`](#insn-00affebc) 範囲 `[['00affebc', '00affec3']]`
  - `FALL_THROUGH` [`00affec0`](#insn-00affec0) → [`00affec4`](#insn-00affec4)
- ブロック [`00affec4`](#insn-00affec4) 範囲 `[['00affec4', '00affecb']]`
  - `FALL_THROUGH` [`00affec8`](#insn-00affec8) → [`00affecc`](#insn-00affecc)
- ブロック [`00affecc`](#insn-00affecc) 範囲 `[['00affecc', '00affed3']]`
  - `FALL_THROUGH` [`00affed0`](#insn-00affed0) → [`00affed4`](#insn-00affed4)
- ブロック [`00affed4`](#insn-00affed4) 範囲 `[['00affed4', '00affedb']]`
  - `FALL_THROUGH` [`00affed8`](#insn-00affed8) → [`00affedc`](#insn-00affedc)
- ブロック [`00affedc`](#insn-00affedc) 範囲 `[['00affedc', '00affee3']]`
  - `FALL_THROUGH` [`00affee0`](#insn-00affee0) → [`00affee4`](#insn-00affee4)
- ブロック [`00affee4`](#insn-00affee4) 範囲 `[['00affee4', '00affeeb']]`
  - `FALL_THROUGH` [`00affee8`](#insn-00affee8) → [`00affeec`](#insn-00affeec)
- ブロック [`00affeec`](#insn-00affeec) 範囲 `[['00affeec', '00affeef']]`
  - `CONDITIONAL_JUMP` [`00affeec`](#insn-00affeec) → [`00afff20`](#insn-00afff20)
  - `FALL_THROUGH` [`00affeec`](#insn-00affeec) → [`00affef0`](#insn-00affef0)
- ブロック [`00affef0`](#insn-00affef0) 範囲 `[['00affef0', '00affef3']]`
  - `FALL_THROUGH` [`00affef0`](#insn-00affef0) → [`00affef4`](#insn-00affef4)
- ブロック [`00affef4`](#insn-00affef4) 範囲 `[['00affef4', '00affefb']]`
  - `FALL_THROUGH` [`00affef8`](#insn-00affef8) → [`00affefc`](#insn-00affefc)
- ブロック [`00affefc`](#insn-00affefc) 範囲 `[['00affefc', '00afff03']]`
  - `FALL_THROUGH` [`00afff00`](#insn-00afff00) → [`00afff04`](#insn-00afff04)
- ブロック [`00afff04`](#insn-00afff04) 範囲 `[['00afff04', '00afff0b']]`
  - `CONDITIONAL_JUMP` [`00afff08`](#insn-00afff08) → [`00affef4`](#insn-00affef4)
  - `FALL_THROUGH` [`00afff08`](#insn-00afff08) → [`00afff0c`](#insn-00afff0c)
- ブロック [`00afff0c`](#insn-00afff0c) 範囲 `[['00afff0c', '00afff13']]`
  - `CONDITIONAL_JUMP` [`00afff10`](#insn-00afff10) → [`00afff20`](#insn-00afff20)
  - `FALL_THROUGH` [`00afff10`](#insn-00afff10) → [`00afff14`](#insn-00afff14)
- ブロック [`00afff14`](#insn-00afff14) 範囲 `[['00afff14', '00afff1b']]`
  - `FALL_THROUGH` [`00afff18`](#insn-00afff18) → [`00afff1c`](#insn-00afff1c)
- ブロック [`00afff1c`](#insn-00afff1c) 範囲 `[['00afff1c', '00afff1f']]`
  - `CONDITIONAL_JUMP` [`00afff1c`](#insn-00afff1c) → [`00afff58`](#insn-00afff58)
  - `FALL_THROUGH` [`00afff1c`](#insn-00afff1c) → [`00afff20`](#insn-00afff20)
- ブロック [`00afff20`](#insn-00afff20) 範囲 `[['00afff20', '00afff23']]`
  - `FALL_THROUGH` [`00afff20`](#insn-00afff20) → [`00afff24`](#insn-00afff24)
- ブロック [`00afff24`](#insn-00afff24) 範囲 `[['00afff24', '00afff27']]`
  - `FALL_THROUGH` [`00afff24`](#insn-00afff24) → [`00afff28`](#insn-00afff28)
- ブロック [`00afff28`](#insn-00afff28) 範囲 `[['00afff28', '00afff2b']]`
  - `FALL_THROUGH` [`00afff28`](#insn-00afff28) → [`00afff2c`](#insn-00afff2c)
- ブロック [`00afff2c`](#insn-00afff2c) 範囲 `[['00afff2c', '00afff33']]`
  - `FALL_THROUGH` [`00afff30`](#insn-00afff30) → [`00afff34`](#insn-00afff34)
- ブロック [`00afff34`](#insn-00afff34) 範囲 `[['00afff34', '00afff3b']]`
  - `FALL_THROUGH` [`00afff38`](#insn-00afff38) → [`00afff3c`](#insn-00afff3c)
- ブロック [`00afff3c`](#insn-00afff3c) 範囲 `[['00afff3c', '00afff3f']]`
  - `CONDITIONAL_JUMP` [`00afff3c`](#insn-00afff3c) → [`00b00090`](#insn-00b00090)
  - `FALL_THROUGH` [`00afff3c`](#insn-00afff3c) → [`00afff40`](#insn-00afff40)
- ブロック [`00afff40`](#insn-00afff40) 範囲 `[['00afff40', '00afff43']]`
  - `FALL_THROUGH` [`00afff40`](#insn-00afff40) → [`00afff44`](#insn-00afff44)
- ブロック [`00afff44`](#insn-00afff44) 範囲 `[['00afff44', '00afff47']]`
  - `FALL_THROUGH` [`00afff44`](#insn-00afff44) → [`00afff48`](#insn-00afff48)
- ブロック [`00afff48`](#insn-00afff48) 範囲 `[['00afff48', '00afff4b']]`
  - `FALL_THROUGH` [`00afff48`](#insn-00afff48) → [`00afff4c`](#insn-00afff4c)
- ブロック [`00afff4c`](#insn-00afff4c) 範囲 `[['00afff4c', '00afff4f']]`
  - `FALL_THROUGH` [`00afff4c`](#insn-00afff4c) → [`00afff50`](#insn-00afff50)
- ブロック [`00afff50`](#insn-00afff50) 範囲 `[['00afff50', '00afff53']]`
  - `FALL_THROUGH` [`00afff50`](#insn-00afff50) → [`00afff54`](#insn-00afff54)
- ブロック [`00afff54`](#insn-00afff54) 範囲 `[['00afff54', '00afff57']]`
- ブロック [`00afff58`](#insn-00afff58) 範囲 `[['00afff58', '00afff67']]`
  - `CONDITIONAL_JUMP` [`00afff64`](#insn-00afff64) → [`00afff28`](#insn-00afff28)
  - `FALL_THROUGH` [`00afff64`](#insn-00afff64) → [`00afff68`](#insn-00afff68)
- ブロック [`00afff68`](#insn-00afff68) 範囲 `[['00afff68', '00afff87']]`
  - `CONDITIONAL_JUMP` [`00afff84`](#insn-00afff84) → [`00afffe4`](#insn-00afffe4)
  - `FALL_THROUGH` [`00afff84`](#insn-00afff84) → [`00afff88`](#insn-00afff88)
- ブロック [`00afff88`](#insn-00afff88) 範囲 `[['00afff88', '00afff93']]`
  - `CONDITIONAL_JUMP` [`00afff90`](#insn-00afff90) → [`00afffe4`](#insn-00afffe4)
  - `FALL_THROUGH` [`00afff90`](#insn-00afff90) → [`00afff94`](#insn-00afff94)
- ブロック [`00afff94`](#insn-00afff94) 範囲 `[['00afff94', '00afff9f']]`
  - `CONDITIONAL_JUMP` [`00afff9c`](#insn-00afff9c) → [`00afffe4`](#insn-00afffe4)
  - `FALL_THROUGH` [`00afff9c`](#insn-00afff9c) → [`00afffa0`](#insn-00afffa0)
- ブロック [`00afffa0`](#insn-00afffa0) 範囲 `[['00afffa0', '00afffab']]`
  - `CONDITIONAL_JUMP` [`00afffa8`](#insn-00afffa8) → [`00afffe4`](#insn-00afffe4)
  - `FALL_THROUGH` [`00afffa8`](#insn-00afffa8) → [`00afffac`](#insn-00afffac)
- ブロック [`00afffac`](#insn-00afffac) 範囲 `[['00afffac', '00afffaf']]`
  - `CONDITIONAL_JUMP` [`00afffac`](#insn-00afffac) → [`00afffc0`](#insn-00afffc0)
  - `FALL_THROUGH` [`00afffac`](#insn-00afffac) → [`00afffb0`](#insn-00afffb0)
- ブロック [`00afffb0`](#insn-00afffb0) 範囲 `[['00afffb0', '00afffbf']]`
  - `CONDITIONAL_JUMP` [`00afffbc`](#insn-00afffbc) → [`00afffd4`](#insn-00afffd4)
  - `FALL_THROUGH` [`00afffbc`](#insn-00afffbc) → [`00afffc0`](#insn-00afffc0)
- ブロック [`00afffc0`](#insn-00afffc0) 範囲 `[['00afffc0', '00afffd3']]`
  - `FALL_THROUGH` [`00afffd0`](#insn-00afffd0) → [`00afffd4`](#insn-00afffd4)
- ブロック [`00afffd4`](#insn-00afffd4) 範囲 `[['00afffd4', '00afffd7']]`
  - `FALL_THROUGH` [`00afffd4`](#insn-00afffd4) → [`00afffd8`](#insn-00afffd8)
- ブロック [`00afffd8`](#insn-00afffd8) 範囲 `[['00afffd8', '00afffe3']]`
  - `FALL_THROUGH` [`00afffe0`](#insn-00afffe0) → [`00afffe4`](#insn-00afffe4)
- ブロック [`00afffe4`](#insn-00afffe4) 範囲 `[['00afffe4', '00affff3']]`
  - `CONDITIONAL_JUMP` [`00affff0`](#insn-00affff0) → [`00b0007c`](#insn-00b0007c)
  - `FALL_THROUGH` [`00affff0`](#insn-00affff0) → [`00affff4`](#insn-00affff4)
- ブロック [`00affff4`](#insn-00affff4) 範囲 `[['00affff4', '00b00003']]`
  - `UNCONDITIONAL_JUMP` [`00b00000`](#insn-00b00000) → [`00b00010`](#insn-00b00010)
- ブロック [`00b00004`](#insn-00b00004) 範囲 `[['00b00004', '00b0000f']]`
  - `CONDITIONAL_JUMP` [`00b0000c`](#insn-00b0000c) → [`00b0007c`](#insn-00b0007c)
  - `FALL_THROUGH` [`00b0000c`](#insn-00b0000c) → [`00b00010`](#insn-00b00010)
- ブロック [`00b00010`](#insn-00b00010) 範囲 `[['00b00010', '00b0001b']]`
  - `FALL_THROUGH` [`00b00018`](#insn-00b00018) → [`00b0001c`](#insn-00b0001c)
- ブロック [`00b0001c`](#insn-00b0001c) 範囲 `[['00b0001c', '00b0001f']]`
  - `CONDITIONAL_JUMP` [`00b0001c`](#insn-00b0001c) → [`00b00004`](#insn-00b00004)
  - `FALL_THROUGH` [`00b0001c`](#insn-00b0001c) → [`00b00020`](#insn-00b00020)
- ブロック [`00b00020`](#insn-00b00020) 範囲 `[['00b00020', '00b0002b']]`
  - `CONDITIONAL_JUMP` [`00b00028`](#insn-00b00028) → [`00b00004`](#insn-00b00004)
  - `FALL_THROUGH` [`00b00028`](#insn-00b00028) → [`00b0002c`](#insn-00b0002c)
- ブロック [`00b0002c`](#insn-00b0002c) 範囲 `[['00b0002c', '00b00037']]`
  - `CONDITIONAL_JUMP` [`00b00034`](#insn-00b00034) → [`00b00004`](#insn-00b00004)
  - `FALL_THROUGH` [`00b00034`](#insn-00b00034) → [`00b00038`](#insn-00b00038)
- ブロック [`00b00038`](#insn-00b00038) 範囲 `[['00b00038', '00b0004f']]`
  - `CONDITIONAL_JUMP` [`00b0004c`](#insn-00b0004c) → [`00b0007c`](#insn-00b0007c)
  - `FALL_THROUGH` [`00b0004c`](#insn-00b0004c) → [`00b00050`](#insn-00b00050)
- ブロック [`00b00050`](#insn-00b00050) 範囲 `[['00b00050', '00b00053']]`
  - `CONDITIONAL_JUMP` [`00b00050`](#insn-00b00050) → [`00b00058`](#insn-00b00058)
  - `FALL_THROUGH` [`00b00050`](#insn-00b00050) → [`00b00054`](#insn-00b00054)
- ブロック [`00b00054`](#insn-00b00054) 範囲 `[['00b00054', '00b00057']]`
  - `FALL_THROUGH` [`00b00054`](#insn-00b00054) → [`00b00058`](#insn-00b00058)
- ブロック [`00b00058`](#insn-00b00058) 範囲 `[['00b00058', '00b0005f']]`
  - `FALL_THROUGH` [`00b0005c`](#insn-00b0005c) → [`00b00060`](#insn-00b00060)
- ブロック [`00b00060`](#insn-00b00060) 範囲 `[['00b00060', '00b0006f']]`
  - `FALL_THROUGH` [`00b0006c`](#insn-00b0006c) → [`00b00070`](#insn-00b00070)
- ブロック [`00b00070`](#insn-00b00070) 範囲 `[['00b00070', '00b0007b']]`
  - `FALL_THROUGH` [`00b00078`](#insn-00b00078) → [`00b0007c`](#insn-00b0007c)
- ブロック [`00b0007c`](#insn-00b0007c) 範囲 `[['00b0007c', '00b0008f']]`
  - `UNCONDITIONAL_JUMP` [`00b0008c`](#insn-00b0008c) → [`00afff28`](#insn-00afff28)
- ブロック [`00b00090`](#insn-00b00090) 範囲 `[['00b00090', '00b00093']]`

## 命令位置別の参照

- [`00affea4`](#insn-00affea4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affea8`](#insn-00affea8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeac`](#insn-00affeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeb0`](#insn-00affeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affed4`](#insn-00affed4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affed8`](#insn-00affed8) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affee4`](#insn-00affee4) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affeec`](#insn-00affeec) → [`00afff20`](#insn-00afff20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff08`](#insn-00afff08) → [`00affef4`](#insn-00affef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff10`](#insn-00afff10) → [`00afff20`](#insn-00afff20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff1c`](#insn-00afff1c) → [`00afff58`](#insn-00afff58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff24`](#insn-00afff24) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afff2c`](#insn-00afff2c) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afff34`](#insn-00afff34) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff3c`](#insn-00afff3c) → [`00b00090`](#insn-00b00090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff40`](#insn-00afff40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff44`](#insn-00afff44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff48`](#insn-00afff48) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff4c`](#insn-00afff4c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff60`](#insn-00afff60) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afff64`](#insn-00afff64) → [`00afff28`](#insn-00afff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff74`](#insn-00afff74) → `Stack[-0x70]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff78`](#insn-00afff78) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff7c`](#insn-00afff7c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff84`](#insn-00afff84) → [`00afffe4`](#insn-00afffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff90`](#insn-00afff90) → [`00afffe4`](#insn-00afffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff9c`](#insn-00afff9c) → [`00afffe4`](#insn-00afffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffa8`](#insn-00afffa8) → [`00afffe4`](#insn-00afffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffac`](#insn-00afffac) → [`00afffc0`](#insn-00afffc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffbc`](#insn-00afffbc) → [`00afffd4`](#insn-00afffd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffd0`](#insn-00afffd0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00affff0`](#insn-00affff0) → [`00b0007c`](#insn-00b0007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affff8`](#insn-00affff8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affffc`](#insn-00affffc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00000`](#insn-00b00000) → [`00b00010`](#insn-00b00010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0000c`](#insn-00b0000c) → [`00b0007c`](#insn-00b0007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0001c`](#insn-00b0001c) → [`00b00004`](#insn-00b00004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00028`](#insn-00b00028) → [`00b00004`](#insn-00b00004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00034`](#insn-00b00034) → [`00b00004`](#insn-00b00004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0004c`](#insn-00b0004c) → [`00b0007c`](#insn-00b0007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00050`](#insn-00b00050) → [`00b00058`](#insn-00b00058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0006c`](#insn-00b0006c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b0007c`](#insn-00b0007c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00080`](#insn-00b00080) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00084`](#insn-00b00084) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00088`](#insn-00b00088) → `Stack[-0x70]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0008c`](#insn-00b0008c) → [`00afff28`](#insn-00afff28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00090`](#insn-00b00090) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affea4`](#insn-00affea4)

~~~json
{
  "source": "00affea4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affea8`](#insn-00affea8)

~~~json
{
  "source": "00affea8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeac`](#insn-00affeac)

~~~json
{
  "source": "00affeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeb0`](#insn-00affeb0)

~~~json
{
  "source": "00affeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affed4`](#insn-00affed4)

~~~json
{
  "source": "00affed4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affed8`](#insn-00affed8)

~~~json
{
  "source": "00affed8",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affee4`](#insn-00affee4)

~~~json
{
  "source": "00affee4",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affeec`](#insn-00affeec)

~~~json
{
  "source": "00affeec",
  "target": "00afff20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff08`](#insn-00afff08)

~~~json
{
  "source": "00afff08",
  "target": "00affef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff10`](#insn-00afff10)

~~~json
{
  "source": "00afff10",
  "target": "00afff20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff1c`](#insn-00afff1c)

~~~json
{
  "source": "00afff1c",
  "target": "00afff58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff24`](#insn-00afff24)

~~~json
{
  "source": "00afff24",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff2c`](#insn-00afff2c)

~~~json
{
  "source": "00afff2c",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff34`](#insn-00afff34)

~~~json
{
  "source": "00afff34",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff3c`](#insn-00afff3c)

~~~json
{
  "source": "00afff3c",
  "target": "00b00090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff40`](#insn-00afff40)

~~~json
{
  "source": "00afff40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff44`](#insn-00afff44)

~~~json
{
  "source": "00afff44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff48`](#insn-00afff48)

~~~json
{
  "source": "00afff48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff4c`](#insn-00afff4c)

~~~json
{
  "source": "00afff4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff60`](#insn-00afff60)

~~~json
{
  "source": "00afff60",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff64`](#insn-00afff64)

~~~json
{
  "source": "00afff64",
  "target": "00afff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff74`](#insn-00afff74)

~~~json
{
  "source": "00afff74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff78`](#insn-00afff78)

~~~json
{
  "source": "00afff78",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff7c`](#insn-00afff7c)

~~~json
{
  "source": "00afff7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff84`](#insn-00afff84)

~~~json
{
  "source": "00afff84",
  "target": "00afffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff90`](#insn-00afff90)

~~~json
{
  "source": "00afff90",
  "target": "00afffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff9c`](#insn-00afff9c)

~~~json
{
  "source": "00afff9c",
  "target": "00afffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffa8`](#insn-00afffa8)

~~~json
{
  "source": "00afffa8",
  "target": "00afffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffac`](#insn-00afffac)

~~~json
{
  "source": "00afffac",
  "target": "00afffc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffbc`](#insn-00afffbc)

~~~json
{
  "source": "00afffbc",
  "target": "00afffd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffd0`](#insn-00afffd0)

~~~json
{
  "source": "00afffd0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affff0`](#insn-00affff0)

~~~json
{
  "source": "00affff0",
  "target": "00b0007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affff8`](#insn-00affff8)

~~~json
{
  "source": "00affff8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affffc`](#insn-00affffc)

~~~json
{
  "source": "00affffc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00000`](#insn-00b00000)

~~~json
{
  "source": "00b00000",
  "target": "00b00010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0000c`](#insn-00b0000c)

~~~json
{
  "source": "00b0000c",
  "target": "00b0007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0001c`](#insn-00b0001c)

~~~json
{
  "source": "00b0001c",
  "target": "00b00004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00028`](#insn-00b00028)

~~~json
{
  "source": "00b00028",
  "target": "00b00004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00034`](#insn-00b00034)

~~~json
{
  "source": "00b00034",
  "target": "00b00004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0004c`](#insn-00b0004c)

~~~json
{
  "source": "00b0004c",
  "target": "00b0007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00050`](#insn-00b00050)

~~~json
{
  "source": "00b00050",
  "target": "00b00058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0006c`](#insn-00b0006c)

~~~json
{
  "source": "00b0006c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0007c`](#insn-00b0007c)

~~~json
{
  "source": "00b0007c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00080`](#insn-00b00080)

~~~json
{
  "source": "00b00080",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00084`](#insn-00b00084)

~~~json
{
  "source": "00b00084",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00088`](#insn-00b00088)

~~~json
{
  "source": "00b00088",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0008c`](#insn-00b0008c)

~~~json
{
  "source": "00b0008c",
  "target": "00afff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00090`](#insn-00b00090)

~~~json
{
  "source": "00b00090",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
