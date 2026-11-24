# 00affee4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00affea0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affea0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-f96a3fbe24ee7b316a3fff42097c3052)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5fc68`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fc68.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0061.md#compare-cb2b6ab693adad1dce8a92843c4b1286)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affee4",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b80094f26639ed2b8dfa719ee08010211de3de40361d3b38c4c86b49a805d1bf",
  "source_text_sha256": "b80094f26639ed2b8dfa719ee08010211de3de40361d3b38c4c86b49a805d1bf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affee4",
        "00b000d7"
      ]
    ],
    "bytes_sha256": "71b4d90dd76dd3f9171e92b720bc8454cff9d2fee003184da50476a37dbafb48",
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

- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)

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
  
                    /* catch() { ... } // from try @ 00af5958 with catch @ 00affee8 */
                    /* catch() { ... } // from try @ 00af594c with catch @ 00affef0 */
                    /* catch() { ... } // from try @ 00af5940 with catch @ 00affef8 */
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00af5934 with catch @ 00afff00 */
  local_48 = *(long *)(lVar3 + 0x28);
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5928 with catch @ 00afff08 */
                    /* catch() { ... } // from try @ 00af591c with catch @ 00afff10 */
                    /* catch() { ... } // from try @ 00af5910 with catch @ 00afff18 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af5904 with catch @ 00afff20 */
  uVar8 = *param_2;
                    /* catch() { ... } // from try @ 00af58f8 with catch @ 00afff28 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar6 = (long *)(param_1 + 0x38);
  plVar5 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00af58ec with catch @ 00afff30 */
  plVar4 = plVar6;
  if (plVar5 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af58e0 with catch @ 00afff38 */
                    /* catch() { ... } // from try @ 00af586c with catch @ 00afff40 */
      if ((ulong)plVar5[4] >= uVar8) {
        plVar4 = plVar5;
      }
                    /* catch() { ... } // from try @ 00af5860 with catch @ 00afff48 */
      plVar5 = (long *)plVar5[(ulong)plVar5[4] < uVar8];
    } while (plVar5 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5854 with catch @ 00afff50 */
                    /* catch() { ... } // from try @ 00af5848 with catch @ 00afff58 */
                    /* catch() { ... } // from try @ 00af5794 with catch @ 00afff60 */
    if ((plVar4 != plVar6) && ((ulong)plVar4[4] <= uVar8)) {
      lVar7 = plVar4[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      if (lVar7 == 0) goto LAB_00afff6c;
      local_60 = *param_3;
      lStack_58 = param_3[1];
      local_50 = (code *)param_3[2];
      plVar4 = *(long **)(lVar7 + 0x48);
      local_70 = (undefined1 *)&local_70;
      local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af5d70 with catch @ 00afffd8 */
      if ((((plVar4 != (long *)0x0) &&
           (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[2] == local_60)) &&
          (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[3] == lStack_58)) &&
         (local_70 = (undefined1 *)&local_70, local_68 = &local_70, (code *)plVar4[4] == local_50))
      {
        local_70 = (undefined1 *)&local_70;
        local_68 = &local_70;
        if (local_50 == (code *)0x0) {
LAB_00b00004:
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
          if (plVar4 != (long *)0x0) goto LAB_00b00004;
        }
                    /* catch() { ... } // from try @ 00af5d48 with catch @ 00b0001c */
        *(undefined8 *)(lVar7 + 0x48) = 0;
        *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
      }
      plVar5 = (long *)(lVar7 + 0x50);
      plVar4 = (long *)*plVar5;
      if (plVar5 != plVar4) {
        do {
          plVar6 = (long *)((long)plVar4 - *(long *)(lVar7 + 0x60));
                    /* catch() { ... } // from try @ 00af5a7c with catch @ 00b00060 */
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
                    /* catch() { ... } // from try @ 00af6134 with catch @ 00b000a4 */
              *(long *)(lVar2 + 8) = plVar6[1];
              *(long *)plVar6[1] = lVar2;
              _ZdlPv(plVar6);
                    /* catch() { ... } // from try @ 00af5ba0 with catch @ 00b000b4 */
              *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
            }
            break;
          }
          plVar4 = (long *)*plVar4;
        } while (plVar5 != plVar4);
      }
      *(undefined8 **)(local_70 + 8) = local_68;
      *local_68 = local_70;
      goto LAB_00afff6c;
    }
  }
                    /* catch() { ... } // from try @ 00af5768 with catch @ 00afff68 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
LAB_00afff6c:
                    /* catch() { ... } // from try @ 00af5704 with catch @ 00afff70 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af56a4 with catch @ 00afff78 */
                    /* catch() { ... } // from try @ 00afacc0 with catch @ 00afff80 */
  if (*(long *)(lVar3 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00afaaf4 with catch @ 00afff84 */
                    /* catch() { ... } // from try @ 00afa8cc with catch @ 00afff88
                       catch() { ... } // from try @ 00afa93c with catch @ 00afff88 */
                    /* catch() { ... } // from try @ 00afa8b8 with catch @ 00afff8c
                       catch() { ... } // from try @ 00afa928 with catch @ 00afff8c */
                    /* catch() { ... } // from try @ 00afa880 with catch @ 00afff90
                       catch() { ... } // from try @ 00afa900 with catch @ 00afff90 */
                    /* catch() { ... } // from try @ 00af73dc with catch @ 00afff94 */
                    /* catch() { ... } // from try @ 00af61a4 with catch @ 00afff98 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affee4"></a> `00affee4` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00affee8"></a> `00affee8` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affeec"></a> `00affeec` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00affef0"></a> `00affef0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00affef4"></a> `00affef4` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00affef8"></a> `00affef8` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00affefc"></a> `00affefc` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afff00"></a> `00afff00` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00afff04"></a> `00afff04` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00afff08"></a> `00afff08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afff0c"></a> `00afff0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afff10"></a> `00afff10` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00afff14"></a> `00afff14` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00afff18"></a> `00afff18` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afff1c"></a> `00afff1c` | `41 77 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00afff20"></a> `00afff20` | `d6 02 40 f9` | ldr x22,[x22] | `FALL_THROUGH`
<a id="insn-00afff24"></a> `00afff24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afff28"></a> `00afff28` | `3e 77 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00afff2c"></a> `00afff2c` | `a9 8e 43 f8` | ldr x9,[x21, #0x38]! | `FALL_THROUGH`
<a id="insn-00afff30"></a> `00afff30` | `a9 01 00 b4` | cbz x9,0x00afff64 | `CONDITIONAL_JUMP`
<a id="insn-00afff34"></a> `00afff34` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00afff38"></a> `00afff38` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00afff3c"></a> `00afff3c` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00afff40"></a> `00afff40` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00afff44"></a> `00afff44` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00afff48"></a> `00afff48` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afff4c"></a> `00afff4c` | `69 ff ff b5` | cbnz x9,0x00afff38 | `CONDITIONAL_JUMP`
<a id="insn-00afff50"></a> `00afff50` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00afff54"></a> `00afff54` | `80 00 00 54` | b.eq 0x00afff64 | `CONDITIONAL_JUMP`
<a id="insn-00afff58"></a> `00afff58` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afff5c"></a> `00afff5c` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00afff60"></a> `00afff60` | `e9 01 00 54` | b.ls 0x00afff9c | `CONDITIONAL_JUMP`
<a id="insn-00afff64"></a> `00afff64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afff68"></a> `00afff68` | `32 77 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00afff6c"></a> `00afff6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afff70"></a> `00afff70` | `30 77 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00afff74"></a> `00afff74` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00afff78"></a> `00afff78` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afff7c"></a> `00afff7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afff80"></a> `00afff80` | `a1 0a 00 54` | b.ne 0x00b000d4 | `CONDITIONAL_JUMP`
<a id="insn-00afff84"></a> `00afff84` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afff88"></a> `00afff88` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afff8c"></a> `00afff8c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afff90"></a> `00afff90` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afff94"></a> `00afff94` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afff98"></a> `00afff98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afff9c"></a> `00afff9c` | `15 15 40 f9` | ldr x21,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00afffa0"></a> `00afffa0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afffa4"></a> `00afffa4` | `23 77 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00afffa8"></a> `00afffa8` | `35 fe ff b4` | cbz x21,0x00afff6c | `CONDITIONAL_JUMP`
<a id="insn-00afffac"></a> `00afffac` | `8a 22 40 a9` | ldp x10,x8,[x20] | `FALL_THROUGH`
<a id="insn-00afffb0"></a> `00afffb0` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afffb4"></a> `00afffb4` | `eb 03 00 91` | mov x11,sp | `FALL_THROUGH`
<a id="insn-00afffb8"></a> `00afffb8` | `eb 2f 00 a9` | stp x11,x11,[sp] | `FALL_THROUGH`
<a id="insn-00afffbc"></a> `00afffbc` | `ea 23 01 a9` | stp x10,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afffc0"></a> `00afffc0` | `e9 13 00 f9` | str x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afffc4"></a> `00afffc4` | `a0 26 40 f9` | ldr x0,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00afffc8"></a> `00afffc8` | `00 03 00 b4` | cbz x0,0x00b00028 | `CONDITIONAL_JUMP`
<a id="insn-00afffcc"></a> `00afffcc` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afffd0"></a> `00afffd0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00afffd4"></a> `00afffd4` | `a1 02 00 54` | b.ne 0x00b00028 | `CONDITIONAL_JUMP`
<a id="insn-00afffd8"></a> `00afffd8` | `0a 0c 40 f9` | ldr x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00afffdc"></a> `00afffdc` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00afffe0"></a> `00afffe0` | `41 02 00 54` | b.ne 0x00b00028 | `CONDITIONAL_JUMP`
<a id="insn-00afffe4"></a> `00afffe4` | `0a 10 40 f9` | ldr x10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00afffe8"></a> `00afffe8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00afffec"></a> `00afffec` | `e1 01 00 54` | b.ne 0x00b00028 | `CONDITIONAL_JUMP`
<a id="insn-00affff0"></a> `00affff0` | `a9 00 00 b4` | cbz x9,0x00b00004 | `CONDITIONAL_JUMP`
<a id="insn-00affff4"></a> `00affff4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00affff8"></a> `00affff8` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00affffc"></a> `00affffc` | `a0 26 40 f9` | ldr x0,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00b00000"></a> `00b00000` | `c0 00 00 b4` | cbz x0,0x00b00018 | `CONDITIONAL_JUMP`
<a id="insn-00b00004"></a> `00b00004` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00b00008"></a> `00b00008` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b0000c"></a> `00b0000c` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b00010"></a> `00b00010` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b00014"></a> `00b00014` | `13 6c 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b00018"></a> `00b00018` | `a8 22 40 b9` | ldr w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00b0001c"></a> `00b0001c` | `bf 26 00 f9` | str xzr,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00b00020"></a> `00b00020` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b00024"></a> `00b00024` | `a8 22 00 b9` | str w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00b00028"></a> `00b00028` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-00b0002c"></a> `00b0002c` | `48 0d 45 f8` | ldr x8,[x10, #0x50]! | `FALL_THROUGH`
<a id="insn-00b00030"></a> `00b00030` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b00034"></a> `00b00034` | `60 04 00 54` | b.eq 0x00b000c0 | `CONDITIONAL_JUMP`
<a id="insn-00b00038"></a> `00b00038` | `4b 09 40 f9` | ldr x11,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00b0003c"></a> `00b0003c` | `ec 03 41 a9` | ldp x12,x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b00040"></a> `00b00040` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b00044"></a> `00b00044` | `04 00 00 14` | b 0x00b00054 | `UNCONDITIONAL_JUMP`
<a id="insn-00b00048"></a> `00b00048` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b0004c"></a> `00b0004c` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b00050"></a> `00b00050` | `80 03 00 54` | b.eq 0x00b000c0 | `CONDITIONAL_JUMP`
<a id="insn-00b00054"></a> `00b00054` | `14 01 0b cb` | sub x20,x8,x11 | `FALL_THROUGH`
<a id="insn-00b00058"></a> `00b00058` | `8d 0a 40 f9` | ldr x13,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b0005c"></a> `00b0005c` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b00060"></a> `00b00060` | `41 ff ff 54` | b.ne 0x00b00048 | `CONDITIONAL_JUMP`
<a id="insn-00b00064"></a> `00b00064` | `8d 0e 40 f9` | ldr x13,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00b00068"></a> `00b00068` | `bf 01 00 eb` | cmp x13,x0 | `FALL_THROUGH`
<a id="insn-00b0006c"></a> `00b0006c` | `e1 fe ff 54` | b.ne 0x00b00048 | `CONDITIONAL_JUMP`
<a id="insn-00b00070"></a> `00b00070` | `8d 12 40 f9` | ldr x13,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b00074"></a> `00b00074` | `bf 01 09 eb` | cmp x13,x9 | `FALL_THROUGH`
<a id="insn-00b00078"></a> `00b00078` | `81 fe ff 54` | b.ne 0x00b00048 | `CONDITIONAL_JUMP`
<a id="insn-00b0007c"></a> `00b0007c` | `0a 2d 40 a9` | ldp x10,x11,[x8] | `FALL_THROUGH`
<a id="insn-00b00080"></a> `00b00080` | `4b 05 00 f9` | str x11,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00b00084"></a> `00b00084` | `0b 05 40 f9` | ldr x11,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b00088"></a> `00b00088` | `6a 01 00 f9` | str x10,[x11] | `FALL_THROUGH`
<a id="insn-00b0008c"></a> `00b0008c` | `08 21 00 a9` | stp x8,x8,[x8] | `FALL_THROUGH`
<a id="insn-00b00090"></a> `00b00090` | `94 01 00 b4` | cbz x20,0x00b000c0 | `CONDITIONAL_JUMP`
<a id="insn-00b00094"></a> `00b00094` | `49 00 00 b4` | cbz x9,0x00b0009c | `CONDITIONAL_JUMP`
<a id="insn-00b00098"></a> `00b00098` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b0009c"></a> `00b0009c` | `88 26 40 a9` | ldp x8,x9,[x20] | `FALL_THROUGH`
<a id="insn-00b000a0"></a> `00b000a0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b000a4"></a> `00b000a4` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b000a8"></a> `00b000a8` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b000ac"></a> `00b000ac` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b000b0"></a> `00b000b0` | `ec 6b 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b000b4"></a> `00b000b4` | `a8 22 40 b9` | ldr w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00b000b8"></a> `00b000b8` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b000bc"></a> `00b000bc` | `a8 22 00 b9` | str w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00b000c0"></a> `00b000c0` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00b000c4"></a> `00b000c4` | `28 05 00 f9` | str x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00b000c8"></a> `00b000c8` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b000cc"></a> `00b000cc` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00b000d0"></a> `00b000d0` | `a7 ff ff 17` | b 0x00afff6c | `UNCONDITIONAL_JUMP`
<a id="insn-00b000d4"></a> `00b000d4` | `ef 6b 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affee4`](#insn-00affee4) 範囲 `[['00affee4', '00affee7']]`
  - `FALL_THROUGH` [`00affee4`](#insn-00affee4) → [`00affee8`](#insn-00affee8)
- ブロック [`00affee8`](#insn-00affee8) 範囲 `[['00affee8', '00affeef']]`
  - `FALL_THROUGH` [`00affeec`](#insn-00affeec) → [`00affef0`](#insn-00affef0)
- ブロック [`00affef0`](#insn-00affef0) 範囲 `[['00affef0', '00affef7']]`
  - `FALL_THROUGH` [`00affef4`](#insn-00affef4) → [`00affef8`](#insn-00affef8)
- ブロック [`00affef8`](#insn-00affef8) 範囲 `[['00affef8', '00affeff']]`
  - `FALL_THROUGH` [`00affefc`](#insn-00affefc) → [`00afff00`](#insn-00afff00)
- ブロック [`00afff00`](#insn-00afff00) 範囲 `[['00afff00', '00afff07']]`
  - `FALL_THROUGH` [`00afff04`](#insn-00afff04) → [`00afff08`](#insn-00afff08)
- ブロック [`00afff08`](#insn-00afff08) 範囲 `[['00afff08', '00afff0f']]`
  - `FALL_THROUGH` [`00afff0c`](#insn-00afff0c) → [`00afff10`](#insn-00afff10)
- ブロック [`00afff10`](#insn-00afff10) 範囲 `[['00afff10', '00afff17']]`
  - `FALL_THROUGH` [`00afff14`](#insn-00afff14) → [`00afff18`](#insn-00afff18)
- ブロック [`00afff18`](#insn-00afff18) 範囲 `[['00afff18', '00afff1f']]`
  - `FALL_THROUGH` [`00afff1c`](#insn-00afff1c) → [`00afff20`](#insn-00afff20)
- ブロック [`00afff20`](#insn-00afff20) 範囲 `[['00afff20', '00afff27']]`
  - `FALL_THROUGH` [`00afff24`](#insn-00afff24) → [`00afff28`](#insn-00afff28)
- ブロック [`00afff28`](#insn-00afff28) 範囲 `[['00afff28', '00afff2f']]`
  - `FALL_THROUGH` [`00afff2c`](#insn-00afff2c) → [`00afff30`](#insn-00afff30)
- ブロック [`00afff30`](#insn-00afff30) 範囲 `[['00afff30', '00afff33']]`
  - `CONDITIONAL_JUMP` [`00afff30`](#insn-00afff30) → [`00afff64`](#insn-00afff64)
  - `FALL_THROUGH` [`00afff30`](#insn-00afff30) → [`00afff34`](#insn-00afff34)
- ブロック [`00afff34`](#insn-00afff34) 範囲 `[['00afff34', '00afff37']]`
  - `FALL_THROUGH` [`00afff34`](#insn-00afff34) → [`00afff38`](#insn-00afff38)
- ブロック [`00afff38`](#insn-00afff38) 範囲 `[['00afff38', '00afff3f']]`
  - `FALL_THROUGH` [`00afff3c`](#insn-00afff3c) → [`00afff40`](#insn-00afff40)
- ブロック [`00afff40`](#insn-00afff40) 範囲 `[['00afff40', '00afff47']]`
  - `FALL_THROUGH` [`00afff44`](#insn-00afff44) → [`00afff48`](#insn-00afff48)
- ブロック [`00afff48`](#insn-00afff48) 範囲 `[['00afff48', '00afff4f']]`
  - `CONDITIONAL_JUMP` [`00afff4c`](#insn-00afff4c) → [`00afff38`](#insn-00afff38)
  - `FALL_THROUGH` [`00afff4c`](#insn-00afff4c) → [`00afff50`](#insn-00afff50)
- ブロック [`00afff50`](#insn-00afff50) 範囲 `[['00afff50', '00afff57']]`
  - `CONDITIONAL_JUMP` [`00afff54`](#insn-00afff54) → [`00afff64`](#insn-00afff64)
  - `FALL_THROUGH` [`00afff54`](#insn-00afff54) → [`00afff58`](#insn-00afff58)
- ブロック [`00afff58`](#insn-00afff58) 範囲 `[['00afff58', '00afff5f']]`
  - `FALL_THROUGH` [`00afff5c`](#insn-00afff5c) → [`00afff60`](#insn-00afff60)
- ブロック [`00afff60`](#insn-00afff60) 範囲 `[['00afff60', '00afff63']]`
  - `CONDITIONAL_JUMP` [`00afff60`](#insn-00afff60) → [`00afff9c`](#insn-00afff9c)
  - `FALL_THROUGH` [`00afff60`](#insn-00afff60) → [`00afff64`](#insn-00afff64)
- ブロック [`00afff64`](#insn-00afff64) 範囲 `[['00afff64', '00afff67']]`
  - `FALL_THROUGH` [`00afff64`](#insn-00afff64) → [`00afff68`](#insn-00afff68)
- ブロック [`00afff68`](#insn-00afff68) 範囲 `[['00afff68', '00afff6b']]`
  - `FALL_THROUGH` [`00afff68`](#insn-00afff68) → [`00afff6c`](#insn-00afff6c)
- ブロック [`00afff6c`](#insn-00afff6c) 範囲 `[['00afff6c', '00afff6f']]`
  - `FALL_THROUGH` [`00afff6c`](#insn-00afff6c) → [`00afff70`](#insn-00afff70)
- ブロック [`00afff70`](#insn-00afff70) 範囲 `[['00afff70', '00afff77']]`
  - `FALL_THROUGH` [`00afff74`](#insn-00afff74) → [`00afff78`](#insn-00afff78)
- ブロック [`00afff78`](#insn-00afff78) 範囲 `[['00afff78', '00afff7f']]`
  - `FALL_THROUGH` [`00afff7c`](#insn-00afff7c) → [`00afff80`](#insn-00afff80)
- ブロック [`00afff80`](#insn-00afff80) 範囲 `[['00afff80', '00afff83']]`
  - `CONDITIONAL_JUMP` [`00afff80`](#insn-00afff80) → [`00b000d4`](#insn-00b000d4)
  - `FALL_THROUGH` [`00afff80`](#insn-00afff80) → [`00afff84`](#insn-00afff84)
- ブロック [`00afff84`](#insn-00afff84) 範囲 `[['00afff84', '00afff87']]`
  - `FALL_THROUGH` [`00afff84`](#insn-00afff84) → [`00afff88`](#insn-00afff88)
- ブロック [`00afff88`](#insn-00afff88) 範囲 `[['00afff88', '00afff8b']]`
  - `FALL_THROUGH` [`00afff88`](#insn-00afff88) → [`00afff8c`](#insn-00afff8c)
- ブロック [`00afff8c`](#insn-00afff8c) 範囲 `[['00afff8c', '00afff8f']]`
  - `FALL_THROUGH` [`00afff8c`](#insn-00afff8c) → [`00afff90`](#insn-00afff90)
- ブロック [`00afff90`](#insn-00afff90) 範囲 `[['00afff90', '00afff93']]`
  - `FALL_THROUGH` [`00afff90`](#insn-00afff90) → [`00afff94`](#insn-00afff94)
- ブロック [`00afff94`](#insn-00afff94) 範囲 `[['00afff94', '00afff97']]`
  - `FALL_THROUGH` [`00afff94`](#insn-00afff94) → [`00afff98`](#insn-00afff98)
- ブロック [`00afff98`](#insn-00afff98) 範囲 `[['00afff98', '00afff9b']]`
- ブロック [`00afff9c`](#insn-00afff9c) 範囲 `[['00afff9c', '00afffab']]`
  - `CONDITIONAL_JUMP` [`00afffa8`](#insn-00afffa8) → [`00afff6c`](#insn-00afff6c)
  - `FALL_THROUGH` [`00afffa8`](#insn-00afffa8) → [`00afffac`](#insn-00afffac)
- ブロック [`00afffac`](#insn-00afffac) 範囲 `[['00afffac', '00afffcb']]`
  - `CONDITIONAL_JUMP` [`00afffc8`](#insn-00afffc8) → [`00b00028`](#insn-00b00028)
  - `FALL_THROUGH` [`00afffc8`](#insn-00afffc8) → [`00afffcc`](#insn-00afffcc)
- ブロック [`00afffcc`](#insn-00afffcc) 範囲 `[['00afffcc', '00afffd7']]`
  - `CONDITIONAL_JUMP` [`00afffd4`](#insn-00afffd4) → [`00b00028`](#insn-00b00028)
  - `FALL_THROUGH` [`00afffd4`](#insn-00afffd4) → [`00afffd8`](#insn-00afffd8)
- ブロック [`00afffd8`](#insn-00afffd8) 範囲 `[['00afffd8', '00afffe3']]`
  - `CONDITIONAL_JUMP` [`00afffe0`](#insn-00afffe0) → [`00b00028`](#insn-00b00028)
  - `FALL_THROUGH` [`00afffe0`](#insn-00afffe0) → [`00afffe4`](#insn-00afffe4)
- ブロック [`00afffe4`](#insn-00afffe4) 範囲 `[['00afffe4', '00afffef']]`
  - `CONDITIONAL_JUMP` [`00afffec`](#insn-00afffec) → [`00b00028`](#insn-00b00028)
  - `FALL_THROUGH` [`00afffec`](#insn-00afffec) → [`00affff0`](#insn-00affff0)
- ブロック [`00affff0`](#insn-00affff0) 範囲 `[['00affff0', '00affff3']]`
  - `CONDITIONAL_JUMP` [`00affff0`](#insn-00affff0) → [`00b00004`](#insn-00b00004)
  - `FALL_THROUGH` [`00affff0`](#insn-00affff0) → [`00affff4`](#insn-00affff4)
- ブロック [`00affff4`](#insn-00affff4) 範囲 `[['00affff4', '00b00003']]`
  - `CONDITIONAL_JUMP` [`00b00000`](#insn-00b00000) → [`00b00018`](#insn-00b00018)
  - `FALL_THROUGH` [`00b00000`](#insn-00b00000) → [`00b00004`](#insn-00b00004)
- ブロック [`00b00004`](#insn-00b00004) 範囲 `[['00b00004', '00b00017']]`
  - `FALL_THROUGH` [`00b00014`](#insn-00b00014) → [`00b00018`](#insn-00b00018)
- ブロック [`00b00018`](#insn-00b00018) 範囲 `[['00b00018', '00b0001b']]`
  - `FALL_THROUGH` [`00b00018`](#insn-00b00018) → [`00b0001c`](#insn-00b0001c)
- ブロック [`00b0001c`](#insn-00b0001c) 範囲 `[['00b0001c', '00b00027']]`
  - `FALL_THROUGH` [`00b00024`](#insn-00b00024) → [`00b00028`](#insn-00b00028)
- ブロック [`00b00028`](#insn-00b00028) 範囲 `[['00b00028', '00b00037']]`
  - `CONDITIONAL_JUMP` [`00b00034`](#insn-00b00034) → [`00b000c0`](#insn-00b000c0)
  - `FALL_THROUGH` [`00b00034`](#insn-00b00034) → [`00b00038`](#insn-00b00038)
- ブロック [`00b00038`](#insn-00b00038) 範囲 `[['00b00038', '00b00047']]`
  - `UNCONDITIONAL_JUMP` [`00b00044`](#insn-00b00044) → [`00b00054`](#insn-00b00054)
- ブロック [`00b00048`](#insn-00b00048) 範囲 `[['00b00048', '00b00053']]`
  - `CONDITIONAL_JUMP` [`00b00050`](#insn-00b00050) → [`00b000c0`](#insn-00b000c0)
  - `FALL_THROUGH` [`00b00050`](#insn-00b00050) → [`00b00054`](#insn-00b00054)
- ブロック [`00b00054`](#insn-00b00054) 範囲 `[['00b00054', '00b0005f']]`
  - `FALL_THROUGH` [`00b0005c`](#insn-00b0005c) → [`00b00060`](#insn-00b00060)
- ブロック [`00b00060`](#insn-00b00060) 範囲 `[['00b00060', '00b00063']]`
  - `CONDITIONAL_JUMP` [`00b00060`](#insn-00b00060) → [`00b00048`](#insn-00b00048)
  - `FALL_THROUGH` [`00b00060`](#insn-00b00060) → [`00b00064`](#insn-00b00064)
- ブロック [`00b00064`](#insn-00b00064) 範囲 `[['00b00064', '00b0006f']]`
  - `CONDITIONAL_JUMP` [`00b0006c`](#insn-00b0006c) → [`00b00048`](#insn-00b00048)
  - `FALL_THROUGH` [`00b0006c`](#insn-00b0006c) → [`00b00070`](#insn-00b00070)
- ブロック [`00b00070`](#insn-00b00070) 範囲 `[['00b00070', '00b0007b']]`
  - `CONDITIONAL_JUMP` [`00b00078`](#insn-00b00078) → [`00b00048`](#insn-00b00048)
  - `FALL_THROUGH` [`00b00078`](#insn-00b00078) → [`00b0007c`](#insn-00b0007c)
- ブロック [`00b0007c`](#insn-00b0007c) 範囲 `[['00b0007c', '00b00093']]`
  - `CONDITIONAL_JUMP` [`00b00090`](#insn-00b00090) → [`00b000c0`](#insn-00b000c0)
  - `FALL_THROUGH` [`00b00090`](#insn-00b00090) → [`00b00094`](#insn-00b00094)
- ブロック [`00b00094`](#insn-00b00094) 範囲 `[['00b00094', '00b00097']]`
  - `CONDITIONAL_JUMP` [`00b00094`](#insn-00b00094) → [`00b0009c`](#insn-00b0009c)
  - `FALL_THROUGH` [`00b00094`](#insn-00b00094) → [`00b00098`](#insn-00b00098)
- ブロック [`00b00098`](#insn-00b00098) 範囲 `[['00b00098', '00b0009b']]`
  - `FALL_THROUGH` [`00b00098`](#insn-00b00098) → [`00b0009c`](#insn-00b0009c)
- ブロック [`00b0009c`](#insn-00b0009c) 範囲 `[['00b0009c', '00b000a3']]`
  - `FALL_THROUGH` [`00b000a0`](#insn-00b000a0) → [`00b000a4`](#insn-00b000a4)
- ブロック [`00b000a4`](#insn-00b000a4) 範囲 `[['00b000a4', '00b000b3']]`
  - `FALL_THROUGH` [`00b000b0`](#insn-00b000b0) → [`00b000b4`](#insn-00b000b4)
- ブロック [`00b000b4`](#insn-00b000b4) 範囲 `[['00b000b4', '00b000bf']]`
  - `FALL_THROUGH` [`00b000bc`](#insn-00b000bc) → [`00b000c0`](#insn-00b000c0)
- ブロック [`00b000c0`](#insn-00b000c0) 範囲 `[['00b000c0', '00b000d3']]`
  - `UNCONDITIONAL_JUMP` [`00b000d0`](#insn-00b000d0) → [`00afff6c`](#insn-00afff6c)
- ブロック [`00b000d4`](#insn-00b000d4) 範囲 `[['00b000d4', '00b000d7']]`

## 命令位置別の参照

- [`00affee8`](#insn-00affee8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeec`](#insn-00affeec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affef0`](#insn-00affef0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affef4`](#insn-00affef4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff18`](#insn-00afff18) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff1c`](#insn-00afff1c) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00afff28`](#insn-00afff28) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00afff30`](#insn-00afff30) → [`00afff64`](#insn-00afff64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff4c`](#insn-00afff4c) → [`00afff38`](#insn-00afff38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff54`](#insn-00afff54) → [`00afff64`](#insn-00afff64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff60`](#insn-00afff60) → [`00afff9c`](#insn-00afff9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff68`](#insn-00afff68) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00afff70`](#insn-00afff70) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00afff78`](#insn-00afff78) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff80`](#insn-00afff80) → [`00b000d4`](#insn-00b000d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff84`](#insn-00afff84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff88`](#insn-00afff88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff8c`](#insn-00afff8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff90`](#insn-00afff90) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffa4`](#insn-00afffa4) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00afffa8`](#insn-00afffa8) → [`00afff6c`](#insn-00afff6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffb8`](#insn-00afffb8) → `Stack[-0x70]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffbc`](#insn-00afffbc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffc0`](#insn-00afffc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffc8`](#insn-00afffc8) → [`00b00028`](#insn-00b00028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffd4`](#insn-00afffd4) → [`00b00028`](#insn-00b00028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffe0`](#insn-00afffe0) → [`00b00028`](#insn-00b00028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffec`](#insn-00afffec) → [`00b00028`](#insn-00b00028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affff0`](#insn-00affff0) → [`00b00004`](#insn-00b00004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00000`](#insn-00b00000) → [`00b00018`](#insn-00b00018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00014`](#insn-00b00014) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b00034`](#insn-00b00034) → [`00b000c0`](#insn-00b000c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0003c`](#insn-00b0003c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00040`](#insn-00b00040) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00044`](#insn-00b00044) → [`00b00054`](#insn-00b00054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00050`](#insn-00b00050) → [`00b000c0`](#insn-00b000c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00060`](#insn-00b00060) → [`00b00048`](#insn-00b00048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0006c`](#insn-00b0006c) → [`00b00048`](#insn-00b00048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00078`](#insn-00b00078) → [`00b00048`](#insn-00b00048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00090`](#insn-00b00090) → [`00b000c0`](#insn-00b000c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b00094`](#insn-00b00094) → [`00b0009c`](#insn-00b0009c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000b0`](#insn-00b000b0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b000c0`](#insn-00b000c0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000c4`](#insn-00b000c4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000c8`](#insn-00b000c8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000cc`](#insn-00b000cc) → `Stack[-0x70]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000d0`](#insn-00b000d0) → [`00afff6c`](#insn-00afff6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b000d4`](#insn-00b000d4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affee8`](#insn-00affee8)

~~~json
{
  "source": "00affee8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeec`](#insn-00affeec)

~~~json
{
  "source": "00affeec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affef0`](#insn-00affef0)

~~~json
{
  "source": "00affef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affef4`](#insn-00affef4)

~~~json
{
  "source": "00affef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff18`](#insn-00afff18)

~~~json
{
  "source": "00afff18",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff1c`](#insn-00afff1c)

~~~json
{
  "source": "00afff1c",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff28`](#insn-00afff28)

~~~json
{
  "source": "00afff28",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff30`](#insn-00afff30)

~~~json
{
  "source": "00afff30",
  "target": "00afff64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff4c`](#insn-00afff4c)

~~~json
{
  "source": "00afff4c",
  "target": "00afff38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff54`](#insn-00afff54)

~~~json
{
  "source": "00afff54",
  "target": "00afff64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff60`](#insn-00afff60)

~~~json
{
  "source": "00afff60",
  "target": "00afff9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff68`](#insn-00afff68)

~~~json
{
  "source": "00afff68",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff70`](#insn-00afff70)

~~~json
{
  "source": "00afff70",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff78`](#insn-00afff78)

~~~json
{
  "source": "00afff78",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff80`](#insn-00afff80)

~~~json
{
  "source": "00afff80",
  "target": "00b000d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff84`](#insn-00afff84)

~~~json
{
  "source": "00afff84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff88`](#insn-00afff88)

~~~json
{
  "source": "00afff88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff8c`](#insn-00afff8c)

~~~json
{
  "source": "00afff8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff90`](#insn-00afff90)

~~~json
{
  "source": "00afff90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffa4`](#insn-00afffa4)

~~~json
{
  "source": "00afffa4",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afffa8`](#insn-00afffa8)

~~~json
{
  "source": "00afffa8",
  "target": "00afff6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffb8`](#insn-00afffb8)

~~~json
{
  "source": "00afffb8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffbc`](#insn-00afffbc)

~~~json
{
  "source": "00afffbc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffc0`](#insn-00afffc0)

~~~json
{
  "source": "00afffc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffc8`](#insn-00afffc8)

~~~json
{
  "source": "00afffc8",
  "target": "00b00028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffd4`](#insn-00afffd4)

~~~json
{
  "source": "00afffd4",
  "target": "00b00028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffe0`](#insn-00afffe0)

~~~json
{
  "source": "00afffe0",
  "target": "00b00028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffec`](#insn-00afffec)

~~~json
{
  "source": "00afffec",
  "target": "00b00028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affff0`](#insn-00affff0)

~~~json
{
  "source": "00affff0",
  "target": "00b00004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00000`](#insn-00b00000)

~~~json
{
  "source": "00b00000",
  "target": "00b00018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00014`](#insn-00b00014)

~~~json
{
  "source": "00b00014",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b00034`](#insn-00b00034)

~~~json
{
  "source": "00b00034",
  "target": "00b000c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0003c`](#insn-00b0003c)

~~~json
{
  "source": "00b0003c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00040`](#insn-00b00040)

~~~json
{
  "source": "00b00040",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00044`](#insn-00b00044)

~~~json
{
  "source": "00b00044",
  "target": "00b00054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00050`](#insn-00b00050)

~~~json
{
  "source": "00b00050",
  "target": "00b000c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00060`](#insn-00b00060)

~~~json
{
  "source": "00b00060",
  "target": "00b00048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0006c`](#insn-00b0006c)

~~~json
{
  "source": "00b0006c",
  "target": "00b00048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00078`](#insn-00b00078)

~~~json
{
  "source": "00b00078",
  "target": "00b00048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00090`](#insn-00b00090)

~~~json
{
  "source": "00b00090",
  "target": "00b000c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b00094`](#insn-00b00094)

~~~json
{
  "source": "00b00094",
  "target": "00b0009c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000b0`](#insn-00b000b0)

~~~json
{
  "source": "00b000b0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b000c0`](#insn-00b000c0)

~~~json
{
  "source": "00b000c0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000c4`](#insn-00b000c4)

~~~json
{
  "source": "00b000c4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000c8`](#insn-00b000c8)

~~~json
{
  "source": "00b000c8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000cc`](#insn-00b000cc)

~~~json
{
  "source": "00b000cc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000d0`](#insn-00b000d0)

~~~json
{
  "source": "00b000d0",
  "target": "00afff6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b000d4`](#insn-00b000d4)

~~~json
{
  "source": "00b000d4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
