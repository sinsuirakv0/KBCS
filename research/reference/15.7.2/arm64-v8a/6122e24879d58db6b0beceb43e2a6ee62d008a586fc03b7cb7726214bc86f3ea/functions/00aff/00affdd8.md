# 00affdd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00affea0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affea0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-7c239d1eed0edf952ede779009713033)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affdd8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d3145cffe383b7a23f41376e208be744de3e194e346fc6a32a87c702e31f662",
  "source_text_sha256": "4d3145cffe383b7a23f41376e208be744de3e194e346fc6a32a87c702e31f662",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affdd8",
        "00afffcb"
      ]
    ],
    "bytes_sha256": "168565671ca49e1454e3fafd99179d159c36a49e476eaaa1b081cc637d2e629f",
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

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 8251 bytes

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
  
                    /* catch() { ... } // from try @ 00af5a50 with catch @ 00affddc */
                    /* catch() { ... } // from try @ 00af5a2c with catch @ 00affde8 */
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00af5a1c with catch @ 00affdf4 */
  local_48 = *(long *)(lVar3 + 0x28);
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5a10 with catch @ 00affdfc */
                    /* catch() { ... } // from try @ 00af5a04 with catch @ 00affe04 */
                    /* catch() { ... } // from try @ 00af59f8 with catch @ 00affe0c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af59ec with catch @ 00affe14 */
  uVar8 = *param_2;
                    /* catch() { ... } // from try @ 00af59e0 with catch @ 00affe1c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar6 = (long *)(param_1 + 0x38);
  plVar5 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00af59d4 with catch @ 00affe24 */
  plVar4 = plVar6;
  if (plVar5 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af59c8 with catch @ 00affe2c */
                    /* catch() { ... } // from try @ 00af59bc with catch @ 00affe34 */
      if ((ulong)plVar5[4] >= uVar8) {
        plVar4 = plVar5;
      }
                    /* catch() { ... } // from try @ 00af59b0 with catch @ 00affe3c */
      plVar5 = (long *)plVar5[(ulong)plVar5[4] < uVar8];
    } while (plVar5 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af59a4 with catch @ 00affe44 */
                    /* catch() { ... } // from try @ 00af5998 with catch @ 00affe4c */
                    /* catch() { ... } // from try @ 00af598c with catch @ 00affe54 */
    if ((plVar4 != plVar6) && ((ulong)plVar4[4] <= uVar8)) {
      lVar7 = plVar4[5];
                    /* catch() { ... } // from try @ 00af592c with catch @ 00affe94 */
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5920 with catch @ 00affe9c */
      if (lVar7 == 0) goto LAB_00affe60;
      local_60 = *param_3;
      lStack_58 = param_3[1];
                    /* catch() { ... } // from try @ 00af5914 with catch @ 00affea4 */
      local_50 = (code *)param_3[2];
                    /* catch() { ... } // from try @ 00af5908 with catch @ 00affeac */
                    /* catch() { ... } // from try @ 00af58fc with catch @ 00affeb4 */
      plVar4 = *(long **)(lVar7 + 0x48);
                    /* catch() { ... } // from try @ 00af58f0 with catch @ 00affebc */
      local_70 = (undefined1 *)&local_70;
      local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af58e4 with catch @ 00affec4 */
                    /* catch() { ... } // from try @ 00af58d8 with catch @ 00affecc */
                    /* catch() { ... } // from try @ 00af58cc with catch @ 00affed4 */
                    /* catch() { ... } // from try @ 00af58c0 with catch @ 00affedc */
      if ((((plVar4 != (long *)0x0) &&
           (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[2] == local_60)) &&
          (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[3] == lStack_58)) &&
         (local_70 = (undefined1 *)&local_70, local_68 = &local_70, (code *)plVar4[4] == local_50))
      {
                    /* catch() { ... } // from try @ 00af58b4 with catch @ 00affee4 */
        local_70 = (undefined1 *)&local_70;
        local_68 = &local_70;
        if (local_50 == (code *)0x0) {
LAB_00affef8:
          lVar2 = *plVar4;
                    /* catch() { ... } // from try @ 00af5828 with catch @ 00affefc */
          *(long *)(lVar2 + 8) = plVar4[1];
                    /* catch() { ... } // from try @ 00af581c with catch @ 00afff04 */
          *(long *)plVar4[1] = lVar2;
          _ZdlPv(plVar4);
        }
        else {
          local_70 = (undefined1 *)&local_70;
          local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af58a8 with catch @ 00affeec */
          (*local_50)(lStack_58);
          plVar4 = *(long **)(lVar7 + 0x48);
                    /* catch() { ... } // from try @ 00af589c with catch @ 00affef4 */
          if (plVar4 != (long *)0x0) goto LAB_00affef8;
        }
                    /* catch() { ... } // from try @ 00af5810 with catch @ 00afff0c */
        *(undefined8 *)(lVar7 + 0x48) = 0;
                    /* catch() { ... } // from try @ 00af5804 with catch @ 00afff14 */
        *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
      }
                    /* catch() { ... } // from try @ 00af5750 with catch @ 00afff1c */
      plVar5 = (long *)(lVar7 + 0x50);
      plVar4 = (long *)*plVar5;
                    /* catch() { ... } // from try @ 00af5724 with catch @ 00afff24 */
      if (plVar5 != plVar4) {
                    /* catch() { ... } // from try @ 00af56c0 with catch @ 00afff2c */
                    /* catch() { ... } // from try @ 00af5660 with catch @ 00afff34 */
        do {
                    /* catch() { ... } // from try @ 00afa874 with catch @ 00afff48
                       catch() { ... } // from try @ 00afa8e4 with catch @ 00afff48 */
          plVar6 = (long *)((long)plVar4 - *(long *)(lVar7 + 0x60));
                    /* catch() { ... } // from try @ 00afa83c with catch @ 00afff4c
                       catch() { ... } // from try @ 00afa8bc with catch @ 00afff4c */
                    /* catch() { ... } // from try @ 00af7398 with catch @ 00afff50 */
                    /* catch() { ... } // from try @ 00af6160 with catch @ 00afff54 */
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
                    /* catch() { ... } // from try @ 00af5d2c with catch @ 00afff94 */
              *(long *)(lVar2 + 8) = plVar6[1];
              *(long *)plVar6[1] = lVar2;
              _ZdlPv(plVar6);
              *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
            }
            break;
          }
                    /* catch() { ... } // from try @ 00afac7c with catch @ 00afff3c */
          plVar4 = (long *)*plVar4;
                    /* catch() { ... } // from try @ 00afaab0 with catch @ 00afff40 */
                    /* catch() { ... } // from try @ 00afa888 with catch @ 00afff44
                       catch() { ... } // from try @ 00afa8f8 with catch @ 00afff44 */
        } while (plVar5 != plVar4);
      }
      *(undefined8 **)(local_70 + 8) = local_68;
      *local_68 = local_70;
      goto LAB_00affe60;
    }
  }
                    /* catch() { ... } // from try @ 00af5980 with catch @ 00affe5c */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
LAB_00affe60:
                    /* catch() { ... } // from try @ 00af5974 with catch @ 00affe64 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5968 with catch @ 00affe6c */
                    /* catch() { ... } // from try @ 00af595c with catch @ 00affe74 */
  if (*(long *)(lVar3 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00af5950 with catch @ 00affe7c */
                    /* catch() { ... } // from try @ 00af5944 with catch @ 00affe84 */
                    /* catch() { ... } // from try @ 00af5938 with catch @ 00affe8c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affdd8"></a> `00affdd8` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00affddc"></a> `00affddc` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affde0"></a> `00affde0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00affde4"></a> `00affde4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00affde8"></a> `00affde8` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00affdec"></a> `00affdec` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00affdf0"></a> `00affdf0` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00affdf4"></a> `00affdf4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00affdf8"></a> `00affdf8` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affdfc"></a> `00affdfc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00affe00"></a> `00affe00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affe04"></a> `00affe04` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00affe08"></a> `00affe08` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00affe0c"></a> `00affe0c` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00affe10"></a> `00affe10` | `44 77 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00affe14"></a> `00affe14` | `d6 02 40 f9` | ldr x22,[x22] | `FALL_THROUGH`
<a id="insn-00affe18"></a> `00affe18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affe1c"></a> `00affe1c` | `41 77 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00affe20"></a> `00affe20` | `a9 8e 43 f8` | ldr x9,[x21, #0x38]! | `FALL_THROUGH`
<a id="insn-00affe24"></a> `00affe24` | `a9 01 00 b4` | cbz x9,0x00affe58 | `CONDITIONAL_JUMP`
<a id="insn-00affe28"></a> `00affe28` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00affe2c"></a> `00affe2c` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affe30"></a> `00affe30` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00affe34"></a> `00affe34` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affe38"></a> `00affe38` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affe3c"></a> `00affe3c` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affe40"></a> `00affe40` | `69 ff ff b5` | cbnz x9,0x00affe2c | `CONDITIONAL_JUMP`
<a id="insn-00affe44"></a> `00affe44` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00affe48"></a> `00affe48` | `80 00 00 54` | b.eq 0x00affe58 | `CONDITIONAL_JUMP`
<a id="insn-00affe4c"></a> `00affe4c` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affe50"></a> `00affe50` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00affe54"></a> `00affe54` | `e9 01 00 54` | b.ls 0x00affe90 | `CONDITIONAL_JUMP`
<a id="insn-00affe58"></a> `00affe58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affe5c"></a> `00affe5c` | `35 77 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affe60"></a> `00affe60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affe64"></a> `00affe64` | `33 77 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affe68"></a> `00affe68` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00affe6c"></a> `00affe6c` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00affe70"></a> `00affe70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00affe74"></a> `00affe74` | `a1 0a 00 54` | b.ne 0x00afffc8 | `CONDITIONAL_JUMP`
<a id="insn-00affe78"></a> `00affe78` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00affe7c"></a> `00affe7c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00affe80"></a> `00affe80` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00affe84"></a> `00affe84` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affe88"></a> `00affe88` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00affe8c"></a> `00affe8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affe90"></a> `00affe90` | `15 15 40 f9` | ldr x21,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affe94"></a> `00affe94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affe98"></a> `00affe98` | `26 77 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affe9c"></a> `00affe9c` | `35 fe ff b4` | cbz x21,0x00affe60 | `CONDITIONAL_JUMP`
<a id="insn-00affea0"></a> `00affea0` | `8a 22 40 a9` | ldp x10,x8,[x20] | `FALL_THROUGH`
<a id="insn-00affea4"></a> `00affea4` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00affea8"></a> `00affea8` | `eb 03 00 91` | mov x11,sp | `FALL_THROUGH`
<a id="insn-00affeac"></a> `00affeac` | `eb 2f 00 a9` | stp x11,x11,[sp] | `FALL_THROUGH`
<a id="insn-00affeb0"></a> `00affeb0` | `ea 23 01 a9` | stp x10,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affeb4"></a> `00affeb4` | `e9 13 00 f9` | str x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affeb8"></a> `00affeb8` | `a0 26 40 f9` | ldr x0,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00affebc"></a> `00affebc` | `00 03 00 b4` | cbz x0,0x00afff1c | `CONDITIONAL_JUMP`
<a id="insn-00affec0"></a> `00affec0` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00affec4"></a> `00affec4` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00affec8"></a> `00affec8` | `a1 02 00 54` | b.ne 0x00afff1c | `CONDITIONAL_JUMP`
<a id="insn-00affecc"></a> `00affecc` | `0a 0c 40 f9` | ldr x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00affed0"></a> `00affed0` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00affed4"></a> `00affed4` | `41 02 00 54` | b.ne 0x00afff1c | `CONDITIONAL_JUMP`
<a id="insn-00affed8"></a> `00affed8` | `0a 10 40 f9` | ldr x10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00affedc"></a> `00affedc` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00affee0"></a> `00affee0` | `e1 01 00 54` | b.ne 0x00afff1c | `CONDITIONAL_JUMP`
<a id="insn-00affee4"></a> `00affee4` | `a9 00 00 b4` | cbz x9,0x00affef8 | `CONDITIONAL_JUMP`
<a id="insn-00affee8"></a> `00affee8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00affeec"></a> `00affeec` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00affef0"></a> `00affef0` | `a0 26 40 f9` | ldr x0,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00affef4"></a> `00affef4` | `c0 00 00 b4` | cbz x0,0x00afff0c | `CONDITIONAL_JUMP`
<a id="insn-00affef8"></a> `00affef8` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00affefc"></a> `00affefc` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afff00"></a> `00afff00` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afff04"></a> `00afff04` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00afff08"></a> `00afff08` | `16 6c 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afff0c"></a> `00afff0c` | `a8 22 40 b9` | ldr w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00afff10"></a> `00afff10` | `bf 26 00 f9` | str xzr,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00afff14"></a> `00afff14` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afff18"></a> `00afff18` | `a8 22 00 b9` | str w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00afff1c"></a> `00afff1c` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-00afff20"></a> `00afff20` | `48 0d 45 f8` | ldr x8,[x10, #0x50]! | `FALL_THROUGH`
<a id="insn-00afff24"></a> `00afff24` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00afff28"></a> `00afff28` | `60 04 00 54` | b.eq 0x00afffb4 | `CONDITIONAL_JUMP`
<a id="insn-00afff2c"></a> `00afff2c` | `4b 09 40 f9` | ldr x11,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00afff30"></a> `00afff30` | `ec 03 41 a9` | ldp x12,x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afff34"></a> `00afff34` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afff38"></a> `00afff38` | `04 00 00 14` | b 0x00afff48 | `UNCONDITIONAL_JUMP`
<a id="insn-00afff3c"></a> `00afff3c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afff40"></a> `00afff40` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00afff44"></a> `00afff44` | `80 03 00 54` | b.eq 0x00afffb4 | `CONDITIONAL_JUMP`
<a id="insn-00afff48"></a> `00afff48` | `14 01 0b cb` | sub x20,x8,x11 | `FALL_THROUGH`
<a id="insn-00afff4c"></a> `00afff4c` | `8d 0a 40 f9` | ldr x13,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afff50"></a> `00afff50` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00afff54"></a> `00afff54` | `41 ff ff 54` | b.ne 0x00afff3c | `CONDITIONAL_JUMP`
<a id="insn-00afff58"></a> `00afff58` | `8d 0e 40 f9` | ldr x13,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00afff5c"></a> `00afff5c` | `bf 01 00 eb` | cmp x13,x0 | `FALL_THROUGH`
<a id="insn-00afff60"></a> `00afff60` | `e1 fe ff 54` | b.ne 0x00afff3c | `CONDITIONAL_JUMP`
<a id="insn-00afff64"></a> `00afff64` | `8d 12 40 f9` | ldr x13,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00afff68"></a> `00afff68` | `bf 01 09 eb` | cmp x13,x9 | `FALL_THROUGH`
<a id="insn-00afff6c"></a> `00afff6c` | `81 fe ff 54` | b.ne 0x00afff3c | `CONDITIONAL_JUMP`
<a id="insn-00afff70"></a> `00afff70` | `0a 2d 40 a9` | ldp x10,x11,[x8] | `FALL_THROUGH`
<a id="insn-00afff74"></a> `00afff74` | `4b 05 00 f9` | str x11,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00afff78"></a> `00afff78` | `0b 05 40 f9` | ldr x11,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afff7c"></a> `00afff7c` | `6a 01 00 f9` | str x10,[x11] | `FALL_THROUGH`
<a id="insn-00afff80"></a> `00afff80` | `08 21 00 a9` | stp x8,x8,[x8] | `FALL_THROUGH`
<a id="insn-00afff84"></a> `00afff84` | `94 01 00 b4` | cbz x20,0x00afffb4 | `CONDITIONAL_JUMP`
<a id="insn-00afff88"></a> `00afff88` | `49 00 00 b4` | cbz x9,0x00afff90 | `CONDITIONAL_JUMP`
<a id="insn-00afff8c"></a> `00afff8c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00afff90"></a> `00afff90` | `88 26 40 a9` | ldp x8,x9,[x20] | `FALL_THROUGH`
<a id="insn-00afff94"></a> `00afff94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afff98"></a> `00afff98` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afff9c"></a> `00afff9c` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00afffa0"></a> `00afffa0` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00afffa4"></a> `00afffa4` | `ef 6b 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afffa8"></a> `00afffa8` | `a8 22 40 b9` | ldr w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00afffac"></a> `00afffac` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afffb0"></a> `00afffb0` | `a8 22 00 b9` | str w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00afffb4"></a> `00afffb4` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00afffb8"></a> `00afffb8` | `28 05 00 f9` | str x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00afffbc"></a> `00afffbc` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afffc0"></a> `00afffc0` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00afffc4"></a> `00afffc4` | `a7 ff ff 17` | b 0x00affe60 | `UNCONDITIONAL_JUMP`
<a id="insn-00afffc8"></a> `00afffc8` | `f2 6b 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affdd8`](#insn-00affdd8) 範囲 `[['00affdd8', '00affddb']]`
  - `FALL_THROUGH` [`00affdd8`](#insn-00affdd8) → [`00affddc`](#insn-00affddc)
- ブロック [`00affddc`](#insn-00affddc) 範囲 `[['00affddc', '00affde7']]`
  - `FALL_THROUGH` [`00affde4`](#insn-00affde4) → [`00affde8`](#insn-00affde8)
- ブロック [`00affde8`](#insn-00affde8) 範囲 `[['00affde8', '00affdf3']]`
  - `FALL_THROUGH` [`00affdf0`](#insn-00affdf0) → [`00affdf4`](#insn-00affdf4)
- ブロック [`00affdf4`](#insn-00affdf4) 範囲 `[['00affdf4', '00affdfb']]`
  - `FALL_THROUGH` [`00affdf8`](#insn-00affdf8) → [`00affdfc`](#insn-00affdfc)
- ブロック [`00affdfc`](#insn-00affdfc) 範囲 `[['00affdfc', '00affe03']]`
  - `FALL_THROUGH` [`00affe00`](#insn-00affe00) → [`00affe04`](#insn-00affe04)
- ブロック [`00affe04`](#insn-00affe04) 範囲 `[['00affe04', '00affe0b']]`
  - `FALL_THROUGH` [`00affe08`](#insn-00affe08) → [`00affe0c`](#insn-00affe0c)
- ブロック [`00affe0c`](#insn-00affe0c) 範囲 `[['00affe0c', '00affe13']]`
  - `FALL_THROUGH` [`00affe10`](#insn-00affe10) → [`00affe14`](#insn-00affe14)
- ブロック [`00affe14`](#insn-00affe14) 範囲 `[['00affe14', '00affe1b']]`
  - `FALL_THROUGH` [`00affe18`](#insn-00affe18) → [`00affe1c`](#insn-00affe1c)
- ブロック [`00affe1c`](#insn-00affe1c) 範囲 `[['00affe1c', '00affe23']]`
  - `FALL_THROUGH` [`00affe20`](#insn-00affe20) → [`00affe24`](#insn-00affe24)
- ブロック [`00affe24`](#insn-00affe24) 範囲 `[['00affe24', '00affe27']]`
  - `CONDITIONAL_JUMP` [`00affe24`](#insn-00affe24) → [`00affe58`](#insn-00affe58)
  - `FALL_THROUGH` [`00affe24`](#insn-00affe24) → [`00affe28`](#insn-00affe28)
- ブロック [`00affe28`](#insn-00affe28) 範囲 `[['00affe28', '00affe2b']]`
  - `FALL_THROUGH` [`00affe28`](#insn-00affe28) → [`00affe2c`](#insn-00affe2c)
- ブロック [`00affe2c`](#insn-00affe2c) 範囲 `[['00affe2c', '00affe33']]`
  - `FALL_THROUGH` [`00affe30`](#insn-00affe30) → [`00affe34`](#insn-00affe34)
- ブロック [`00affe34`](#insn-00affe34) 範囲 `[['00affe34', '00affe3b']]`
  - `FALL_THROUGH` [`00affe38`](#insn-00affe38) → [`00affe3c`](#insn-00affe3c)
- ブロック [`00affe3c`](#insn-00affe3c) 範囲 `[['00affe3c', '00affe43']]`
  - `CONDITIONAL_JUMP` [`00affe40`](#insn-00affe40) → [`00affe2c`](#insn-00affe2c)
  - `FALL_THROUGH` [`00affe40`](#insn-00affe40) → [`00affe44`](#insn-00affe44)
- ブロック [`00affe44`](#insn-00affe44) 範囲 `[['00affe44', '00affe4b']]`
  - `CONDITIONAL_JUMP` [`00affe48`](#insn-00affe48) → [`00affe58`](#insn-00affe58)
  - `FALL_THROUGH` [`00affe48`](#insn-00affe48) → [`00affe4c`](#insn-00affe4c)
- ブロック [`00affe4c`](#insn-00affe4c) 範囲 `[['00affe4c', '00affe53']]`
  - `FALL_THROUGH` [`00affe50`](#insn-00affe50) → [`00affe54`](#insn-00affe54)
- ブロック [`00affe54`](#insn-00affe54) 範囲 `[['00affe54', '00affe57']]`
  - `CONDITIONAL_JUMP` [`00affe54`](#insn-00affe54) → [`00affe90`](#insn-00affe90)
  - `FALL_THROUGH` [`00affe54`](#insn-00affe54) → [`00affe58`](#insn-00affe58)
- ブロック [`00affe58`](#insn-00affe58) 範囲 `[['00affe58', '00affe5b']]`
  - `FALL_THROUGH` [`00affe58`](#insn-00affe58) → [`00affe5c`](#insn-00affe5c)
- ブロック [`00affe5c`](#insn-00affe5c) 範囲 `[['00affe5c', '00affe5f']]`
  - `FALL_THROUGH` [`00affe5c`](#insn-00affe5c) → [`00affe60`](#insn-00affe60)
- ブロック [`00affe60`](#insn-00affe60) 範囲 `[['00affe60', '00affe63']]`
  - `FALL_THROUGH` [`00affe60`](#insn-00affe60) → [`00affe64`](#insn-00affe64)
- ブロック [`00affe64`](#insn-00affe64) 範囲 `[['00affe64', '00affe6b']]`
  - `FALL_THROUGH` [`00affe68`](#insn-00affe68) → [`00affe6c`](#insn-00affe6c)
- ブロック [`00affe6c`](#insn-00affe6c) 範囲 `[['00affe6c', '00affe73']]`
  - `FALL_THROUGH` [`00affe70`](#insn-00affe70) → [`00affe74`](#insn-00affe74)
- ブロック [`00affe74`](#insn-00affe74) 範囲 `[['00affe74', '00affe77']]`
  - `CONDITIONAL_JUMP` [`00affe74`](#insn-00affe74) → [`00afffc8`](#insn-00afffc8)
  - `FALL_THROUGH` [`00affe74`](#insn-00affe74) → [`00affe78`](#insn-00affe78)
- ブロック [`00affe78`](#insn-00affe78) 範囲 `[['00affe78', '00affe7b']]`
  - `FALL_THROUGH` [`00affe78`](#insn-00affe78) → [`00affe7c`](#insn-00affe7c)
- ブロック [`00affe7c`](#insn-00affe7c) 範囲 `[['00affe7c', '00affe83']]`
  - `FALL_THROUGH` [`00affe80`](#insn-00affe80) → [`00affe84`](#insn-00affe84)
- ブロック [`00affe84`](#insn-00affe84) 範囲 `[['00affe84', '00affe8b']]`
  - `FALL_THROUGH` [`00affe88`](#insn-00affe88) → [`00affe8c`](#insn-00affe8c)
- ブロック [`00affe8c`](#insn-00affe8c) 範囲 `[['00affe8c', '00affe8f']]`
- ブロック [`00affe90`](#insn-00affe90) 範囲 `[['00affe90', '00affe93']]`
  - `FALL_THROUGH` [`00affe90`](#insn-00affe90) → [`00affe94`](#insn-00affe94)
- ブロック [`00affe94`](#insn-00affe94) 範囲 `[['00affe94', '00affe9b']]`
  - `FALL_THROUGH` [`00affe98`](#insn-00affe98) → [`00affe9c`](#insn-00affe9c)
- ブロック [`00affe9c`](#insn-00affe9c) 範囲 `[['00affe9c', '00affe9f']]`
  - `CONDITIONAL_JUMP` [`00affe9c`](#insn-00affe9c) → [`00affe60`](#insn-00affe60)
  - `FALL_THROUGH` [`00affe9c`](#insn-00affe9c) → [`00affea0`](#insn-00affea0)
- ブロック [`00affea0`](#insn-00affea0) 範囲 `[['00affea0', '00affea3']]`
  - `FALL_THROUGH` [`00affea0`](#insn-00affea0) → [`00affea4`](#insn-00affea4)
- ブロック [`00affea4`](#insn-00affea4) 範囲 `[['00affea4', '00affeab']]`
  - `FALL_THROUGH` [`00affea8`](#insn-00affea8) → [`00affeac`](#insn-00affeac)
- ブロック [`00affeac`](#insn-00affeac) 範囲 `[['00affeac', '00affeb3']]`
  - `FALL_THROUGH` [`00affeb0`](#insn-00affeb0) → [`00affeb4`](#insn-00affeb4)
- ブロック [`00affeb4`](#insn-00affeb4) 範囲 `[['00affeb4', '00affebb']]`
  - `FALL_THROUGH` [`00affeb8`](#insn-00affeb8) → [`00affebc`](#insn-00affebc)
- ブロック [`00affebc`](#insn-00affebc) 範囲 `[['00affebc', '00affebf']]`
  - `CONDITIONAL_JUMP` [`00affebc`](#insn-00affebc) → [`00afff1c`](#insn-00afff1c)
  - `FALL_THROUGH` [`00affebc`](#insn-00affebc) → [`00affec0`](#insn-00affec0)
- ブロック [`00affec0`](#insn-00affec0) 範囲 `[['00affec0', '00affec3']]`
  - `FALL_THROUGH` [`00affec0`](#insn-00affec0) → [`00affec4`](#insn-00affec4)
- ブロック [`00affec4`](#insn-00affec4) 範囲 `[['00affec4', '00affecb']]`
  - `CONDITIONAL_JUMP` [`00affec8`](#insn-00affec8) → [`00afff1c`](#insn-00afff1c)
  - `FALL_THROUGH` [`00affec8`](#insn-00affec8) → [`00affecc`](#insn-00affecc)
- ブロック [`00affecc`](#insn-00affecc) 範囲 `[['00affecc', '00affed3']]`
  - `FALL_THROUGH` [`00affed0`](#insn-00affed0) → [`00affed4`](#insn-00affed4)
- ブロック [`00affed4`](#insn-00affed4) 範囲 `[['00affed4', '00affed7']]`
  - `CONDITIONAL_JUMP` [`00affed4`](#insn-00affed4) → [`00afff1c`](#insn-00afff1c)
  - `FALL_THROUGH` [`00affed4`](#insn-00affed4) → [`00affed8`](#insn-00affed8)
- ブロック [`00affed8`](#insn-00affed8) 範囲 `[['00affed8', '00affedb']]`
  - `FALL_THROUGH` [`00affed8`](#insn-00affed8) → [`00affedc`](#insn-00affedc)
- ブロック [`00affedc`](#insn-00affedc) 範囲 `[['00affedc', '00affee3']]`
  - `CONDITIONAL_JUMP` [`00affee0`](#insn-00affee0) → [`00afff1c`](#insn-00afff1c)
  - `FALL_THROUGH` [`00affee0`](#insn-00affee0) → [`00affee4`](#insn-00affee4)
- ブロック [`00affee4`](#insn-00affee4) 範囲 `[['00affee4', '00affee7']]`
  - `CONDITIONAL_JUMP` [`00affee4`](#insn-00affee4) → [`00affef8`](#insn-00affef8)
  - `FALL_THROUGH` [`00affee4`](#insn-00affee4) → [`00affee8`](#insn-00affee8)
- ブロック [`00affee8`](#insn-00affee8) 範囲 `[['00affee8', '00affeeb']]`
  - `FALL_THROUGH` [`00affee8`](#insn-00affee8) → [`00affeec`](#insn-00affeec)
- ブロック [`00affeec`](#insn-00affeec) 範囲 `[['00affeec', '00affef3']]`
  - `FALL_THROUGH` [`00affef0`](#insn-00affef0) → [`00affef4`](#insn-00affef4)
- ブロック [`00affef4`](#insn-00affef4) 範囲 `[['00affef4', '00affef7']]`
  - `CONDITIONAL_JUMP` [`00affef4`](#insn-00affef4) → [`00afff0c`](#insn-00afff0c)
  - `FALL_THROUGH` [`00affef4`](#insn-00affef4) → [`00affef8`](#insn-00affef8)
- ブロック [`00affef8`](#insn-00affef8) 範囲 `[['00affef8', '00affefb']]`
  - `FALL_THROUGH` [`00affef8`](#insn-00affef8) → [`00affefc`](#insn-00affefc)
- ブロック [`00affefc`](#insn-00affefc) 範囲 `[['00affefc', '00afff03']]`
  - `FALL_THROUGH` [`00afff00`](#insn-00afff00) → [`00afff04`](#insn-00afff04)
- ブロック [`00afff04`](#insn-00afff04) 範囲 `[['00afff04', '00afff0b']]`
  - `FALL_THROUGH` [`00afff08`](#insn-00afff08) → [`00afff0c`](#insn-00afff0c)
- ブロック [`00afff0c`](#insn-00afff0c) 範囲 `[['00afff0c', '00afff13']]`
  - `FALL_THROUGH` [`00afff10`](#insn-00afff10) → [`00afff14`](#insn-00afff14)
- ブロック [`00afff14`](#insn-00afff14) 範囲 `[['00afff14', '00afff1b']]`
  - `FALL_THROUGH` [`00afff18`](#insn-00afff18) → [`00afff1c`](#insn-00afff1c)
- ブロック [`00afff1c`](#insn-00afff1c) 範囲 `[['00afff1c', '00afff23']]`
  - `FALL_THROUGH` [`00afff20`](#insn-00afff20) → [`00afff24`](#insn-00afff24)
- ブロック [`00afff24`](#insn-00afff24) 範囲 `[['00afff24', '00afff2b']]`
  - `CONDITIONAL_JUMP` [`00afff28`](#insn-00afff28) → [`00afffb4`](#insn-00afffb4)
  - `FALL_THROUGH` [`00afff28`](#insn-00afff28) → [`00afff2c`](#insn-00afff2c)
- ブロック [`00afff2c`](#insn-00afff2c) 範囲 `[['00afff2c', '00afff33']]`
  - `FALL_THROUGH` [`00afff30`](#insn-00afff30) → [`00afff34`](#insn-00afff34)
- ブロック [`00afff34`](#insn-00afff34) 範囲 `[['00afff34', '00afff3b']]`
  - `UNCONDITIONAL_JUMP` [`00afff38`](#insn-00afff38) → [`00afff48`](#insn-00afff48)
- ブロック [`00afff3c`](#insn-00afff3c) 範囲 `[['00afff3c', '00afff3f']]`
  - `FALL_THROUGH` [`00afff3c`](#insn-00afff3c) → [`00afff40`](#insn-00afff40)
- ブロック [`00afff40`](#insn-00afff40) 範囲 `[['00afff40', '00afff43']]`
  - `FALL_THROUGH` [`00afff40`](#insn-00afff40) → [`00afff44`](#insn-00afff44)
- ブロック [`00afff44`](#insn-00afff44) 範囲 `[['00afff44', '00afff47']]`
  - `CONDITIONAL_JUMP` [`00afff44`](#insn-00afff44) → [`00afffb4`](#insn-00afffb4)
  - `FALL_THROUGH` [`00afff44`](#insn-00afff44) → [`00afff48`](#insn-00afff48)
- ブロック [`00afff48`](#insn-00afff48) 範囲 `[['00afff48', '00afff4b']]`
  - `FALL_THROUGH` [`00afff48`](#insn-00afff48) → [`00afff4c`](#insn-00afff4c)
- ブロック [`00afff4c`](#insn-00afff4c) 範囲 `[['00afff4c', '00afff4f']]`
  - `FALL_THROUGH` [`00afff4c`](#insn-00afff4c) → [`00afff50`](#insn-00afff50)
- ブロック [`00afff50`](#insn-00afff50) 範囲 `[['00afff50', '00afff53']]`
  - `FALL_THROUGH` [`00afff50`](#insn-00afff50) → [`00afff54`](#insn-00afff54)
- ブロック [`00afff54`](#insn-00afff54) 範囲 `[['00afff54', '00afff57']]`
  - `CONDITIONAL_JUMP` [`00afff54`](#insn-00afff54) → [`00afff3c`](#insn-00afff3c)
  - `FALL_THROUGH` [`00afff54`](#insn-00afff54) → [`00afff58`](#insn-00afff58)
- ブロック [`00afff58`](#insn-00afff58) 範囲 `[['00afff58', '00afff63']]`
  - `CONDITIONAL_JUMP` [`00afff60`](#insn-00afff60) → [`00afff3c`](#insn-00afff3c)
  - `FALL_THROUGH` [`00afff60`](#insn-00afff60) → [`00afff64`](#insn-00afff64)
- ブロック [`00afff64`](#insn-00afff64) 範囲 `[['00afff64', '00afff6f']]`
  - `CONDITIONAL_JUMP` [`00afff6c`](#insn-00afff6c) → [`00afff3c`](#insn-00afff3c)
  - `FALL_THROUGH` [`00afff6c`](#insn-00afff6c) → [`00afff70`](#insn-00afff70)
- ブロック [`00afff70`](#insn-00afff70) 範囲 `[['00afff70', '00afff87']]`
  - `CONDITIONAL_JUMP` [`00afff84`](#insn-00afff84) → [`00afffb4`](#insn-00afffb4)
  - `FALL_THROUGH` [`00afff84`](#insn-00afff84) → [`00afff88`](#insn-00afff88)
- ブロック [`00afff88`](#insn-00afff88) 範囲 `[['00afff88', '00afff8b']]`
  - `CONDITIONAL_JUMP` [`00afff88`](#insn-00afff88) → [`00afff90`](#insn-00afff90)
  - `FALL_THROUGH` [`00afff88`](#insn-00afff88) → [`00afff8c`](#insn-00afff8c)
- ブロック [`00afff8c`](#insn-00afff8c) 範囲 `[['00afff8c', '00afff8f']]`
  - `FALL_THROUGH` [`00afff8c`](#insn-00afff8c) → [`00afff90`](#insn-00afff90)
- ブロック [`00afff90`](#insn-00afff90) 範囲 `[['00afff90', '00afff93']]`
  - `FALL_THROUGH` [`00afff90`](#insn-00afff90) → [`00afff94`](#insn-00afff94)
- ブロック [`00afff94`](#insn-00afff94) 範囲 `[['00afff94', '00afffb3']]`
  - `FALL_THROUGH` [`00afffb0`](#insn-00afffb0) → [`00afffb4`](#insn-00afffb4)
- ブロック [`00afffb4`](#insn-00afffb4) 範囲 `[['00afffb4', '00afffc7']]`
  - `UNCONDITIONAL_JUMP` [`00afffc4`](#insn-00afffc4) → [`00affe60`](#insn-00affe60)
- ブロック [`00afffc8`](#insn-00afffc8) 範囲 `[['00afffc8', '00afffcb']]`

## 命令位置別の参照

- [`00affddc`](#insn-00affddc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affde0`](#insn-00affde0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affde4`](#insn-00affde4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affde8`](#insn-00affde8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe0c`](#insn-00affe0c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe10`](#insn-00affe10) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00affe1c`](#insn-00affe1c) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00affe24`](#insn-00affe24) → [`00affe58`](#insn-00affe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe40`](#insn-00affe40) → [`00affe2c`](#insn-00affe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe48`](#insn-00affe48) → [`00affe58`](#insn-00affe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe54`](#insn-00affe54) → [`00affe90`](#insn-00affe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe5c`](#insn-00affe5c) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affe64`](#insn-00affe64) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affe6c`](#insn-00affe6c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe74`](#insn-00affe74) → [`00afffc8`](#insn-00afffc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe78`](#insn-00affe78) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe7c`](#insn-00affe7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe80`](#insn-00affe80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe84`](#insn-00affe84) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe98`](#insn-00affe98) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affe9c`](#insn-00affe9c) → [`00affe60`](#insn-00affe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeac`](#insn-00affeac) → `Stack[-0x70]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeb0`](#insn-00affeb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeb4`](#insn-00affeb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affebc`](#insn-00affebc) → [`00afff1c`](#insn-00afff1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affec8`](#insn-00affec8) → [`00afff1c`](#insn-00afff1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affed4`](#insn-00affed4) → [`00afff1c`](#insn-00afff1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affee0`](#insn-00affee0) → [`00afff1c`](#insn-00afff1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affee4`](#insn-00affee4) → [`00affef8`](#insn-00affef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affef4`](#insn-00affef4) → [`00afff0c`](#insn-00afff0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff08`](#insn-00afff08) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afff28`](#insn-00afff28) → [`00afffb4`](#insn-00afffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff30`](#insn-00afff30) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff34`](#insn-00afff34) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff38`](#insn-00afff38) → [`00afff48`](#insn-00afff48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff44`](#insn-00afff44) → [`00afffb4`](#insn-00afffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff54`](#insn-00afff54) → [`00afff3c`](#insn-00afff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff60`](#insn-00afff60) → [`00afff3c`](#insn-00afff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff6c`](#insn-00afff6c) → [`00afff3c`](#insn-00afff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff84`](#insn-00afff84) → [`00afffb4`](#insn-00afffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff88`](#insn-00afff88) → [`00afff90`](#insn-00afff90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffa4`](#insn-00afffa4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afffb4`](#insn-00afffb4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffb8`](#insn-00afffb8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffbc`](#insn-00afffbc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffc0`](#insn-00afffc0) → `Stack[-0x70]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffc4`](#insn-00afffc4) → [`00affe60`](#insn-00affe60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afffc8`](#insn-00afffc8) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affddc`](#insn-00affddc)

~~~json
{
  "source": "00affddc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affde0`](#insn-00affde0)

~~~json
{
  "source": "00affde0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affde4`](#insn-00affde4)

~~~json
{
  "source": "00affde4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affde8`](#insn-00affde8)

~~~json
{
  "source": "00affde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe0c`](#insn-00affe0c)

~~~json
{
  "source": "00affe0c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe10`](#insn-00affe10)

~~~json
{
  "source": "00affe10",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe1c`](#insn-00affe1c)

~~~json
{
  "source": "00affe1c",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe24`](#insn-00affe24)

~~~json
{
  "source": "00affe24",
  "target": "00affe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe40`](#insn-00affe40)

~~~json
{
  "source": "00affe40",
  "target": "00affe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe48`](#insn-00affe48)

~~~json
{
  "source": "00affe48",
  "target": "00affe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe54`](#insn-00affe54)

~~~json
{
  "source": "00affe54",
  "target": "00affe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe5c`](#insn-00affe5c)

~~~json
{
  "source": "00affe5c",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe64`](#insn-00affe64)

~~~json
{
  "source": "00affe64",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe6c`](#insn-00affe6c)

~~~json
{
  "source": "00affe6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe74`](#insn-00affe74)

~~~json
{
  "source": "00affe74",
  "target": "00afffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe78`](#insn-00affe78)

~~~json
{
  "source": "00affe78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe7c`](#insn-00affe7c)

~~~json
{
  "source": "00affe7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe80`](#insn-00affe80)

~~~json
{
  "source": "00affe80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe84`](#insn-00affe84)

~~~json
{
  "source": "00affe84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe98`](#insn-00affe98)

~~~json
{
  "source": "00affe98",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe9c`](#insn-00affe9c)

~~~json
{
  "source": "00affe9c",
  "target": "00affe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeac`](#insn-00affeac)

~~~json
{
  "source": "00affeac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeb0`](#insn-00affeb0)

~~~json
{
  "source": "00affeb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeb4`](#insn-00affeb4)

~~~json
{
  "source": "00affeb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affebc`](#insn-00affebc)

~~~json
{
  "source": "00affebc",
  "target": "00afff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affec8`](#insn-00affec8)

~~~json
{
  "source": "00affec8",
  "target": "00afff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affed4`](#insn-00affed4)

~~~json
{
  "source": "00affed4",
  "target": "00afff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affee0`](#insn-00affee0)

~~~json
{
  "source": "00affee0",
  "target": "00afff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affee4`](#insn-00affee4)

~~~json
{
  "source": "00affee4",
  "target": "00affef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affef4`](#insn-00affef4)

~~~json
{
  "source": "00affef4",
  "target": "00afff0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff08`](#insn-00afff08)

~~~json
{
  "source": "00afff08",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff28`](#insn-00afff28)

~~~json
{
  "source": "00afff28",
  "target": "00afffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff30`](#insn-00afff30)

~~~json
{
  "source": "00afff30",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff34`](#insn-00afff34)

~~~json
{
  "source": "00afff34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff38`](#insn-00afff38)

~~~json
{
  "source": "00afff38",
  "target": "00afff48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff44`](#insn-00afff44)

~~~json
{
  "source": "00afff44",
  "target": "00afffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff54`](#insn-00afff54)

~~~json
{
  "source": "00afff54",
  "target": "00afff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff60`](#insn-00afff60)

~~~json
{
  "source": "00afff60",
  "target": "00afff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff6c`](#insn-00afff6c)

~~~json
{
  "source": "00afff6c",
  "target": "00afff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff84`](#insn-00afff84)

~~~json
{
  "source": "00afff84",
  "target": "00afffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff88`](#insn-00afff88)

~~~json
{
  "source": "00afff88",
  "target": "00afff90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffa4`](#insn-00afffa4)

~~~json
{
  "source": "00afffa4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afffb4`](#insn-00afffb4)

~~~json
{
  "source": "00afffb4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffb8`](#insn-00afffb8)

~~~json
{
  "source": "00afffb8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffbc`](#insn-00afffbc)

~~~json
{
  "source": "00afffbc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffc0`](#insn-00afffc0)

~~~json
{
  "source": "00afffc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffc4`](#insn-00afffc4)

~~~json
{
  "source": "00afffc4",
  "target": "00affe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afffc8`](#insn-00afffc8)

~~~json
{
  "source": "00afffc8",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
