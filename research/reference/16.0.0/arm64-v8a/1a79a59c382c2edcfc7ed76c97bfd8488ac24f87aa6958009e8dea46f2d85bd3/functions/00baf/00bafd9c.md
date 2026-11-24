# 00bafd9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b44464`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44464.md) · 移動量 `+0x6b938`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0063.md#compare-453d0dd2c295ad9aff2f2dbbd18d8634)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb01c4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb01c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-a796c222077ebfaa61714272d166deac)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafd9c",
  "name": "_ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2066b8c6d49944fe838a7ca06d54e4ba743aedb37aaa4d55496c3bc81bbbbaf",
  "source_text_sha256": "b2066b8c6d49944fe838a7ca06d54e4ba743aedb37aaa4d55496c3bc81bbbbaf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafd9c",
        "00bafebb"
      ]
    ],
    "bytes_sha256": "e327197599d37a1aed6adf172cdad1b5babc982ccb9fca1a36e5b8b9c194d210",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cbe0](../00c5c/00c5cbe0.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c5b1e0](../00c5b/00c5b1e0.md)
- [00c5b450](../00c5b/00c5b450.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2633 bytes

~~~c

undefined1  [16]
_ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
          (long *param_1,long *param_2,undefined8 *param_3)

{
  char *__s1;
  char *__s2;
  int iVar1;
  undefined8 *puVar2;
  undefined8 uVar3;
  undefined8 *puVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  long lVar9;
  undefined1 auVar10 [16];
  
  plVar5 = param_1 + 1;
  plVar6 = (long *)*plVar5;
  plVar8 = plVar5;
  if (plVar6 != (long *)0x0) {
    lVar9 = *(long *)param_1[3];
    __s1 = (char *)(lVar9 + *param_2);
    plVar5 = param_1 + 1;
    do {
      while( true ) {
        plVar7 = plVar6;
        __s2 = (char *)(lVar9 + plVar7[4]);
        iVar1 = strcmp(__s1,__s2);
        plVar8 = plVar7;
        if (-1 < iVar1) break;
                    /* try { // try from 00bafdf4 to 00cafe0f has its CatchHandler @ 00bafe2c */
        plVar5 = plVar7;
        plVar6 = (long *)*plVar7;
        if ((long *)*plVar7 == (long *)0x0) {
          puVar4 = (undefined8 *)*plVar7;
          goto joined_r0x00bafe34;
        }
      }
                    /* catch() { ... } // from try @ 00bafd14 with catch @ 00bafe10
                       try { // try from 00bafe10 to 00cafe67 has its CatchHandler @ 00baf838 */
      iVar1 = strcmp(__s2,__s1);
                    /* catch() { ... } // from try @ 00baf8e4 with catch @ 00bafe14 */
      if (-1 < iVar1) break;
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
    } while ((long *)*plVar5 != (long *)0x0);
  }
                    /* catch() { ... } // from try @ 00baf954 with catch @ 00bafe30 */
  puVar4 = (undefined8 *)*plVar5;
  plVar7 = plVar5;
joined_r0x00bafe34:
                    /* catch() { ... } // from try @ 00baf948 with catch @ 00bafe34 */
  if (puVar4 == (undefined8 *)0x0) {
    puVar4 = (undefined8 *)_Znwm(0x28);
    uVar3 = *param_3;
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = plVar8;
    puVar4[4] = uVar3;
    *plVar7 = (long)puVar4;
    puVar2 = puVar4;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar2 = (undefined8 *)*plVar7;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],puVar2)
    ;
    uVar3 = 1;
    param_1[2] = param_1[2] + 1;
  }
  else {
                    /* catch() { ... } // from try @ 00baf93c with catch @ 00bafe38 */
    uVar3 = 0;
                    /* catch() { ... } // from try @ 00baf964 with catch @ 00bafe3c */
  }
  auVar10._8_8_ = uVar3;
  auVar10._0_8_ = puVar4;
  return auVar10;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafd9c"></a> `00bafd9c` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bafda0"></a> `00bafda0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafda4"></a> `00bafda4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafda8"></a> `00bafda8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafdac"></a> `00bafdac` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafdb0"></a> `00bafdb0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bafdb4"></a> `00bafdb4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bafdb8"></a> `00bafdb8` | `f8 8e 40 f8` | ldr x24,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafdbc"></a> `00bafdbc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bafdc0"></a> `00bafdc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafdc4"></a> `00bafdc4` | `58 03 00 b4` | cbz x24,0x00bafe2c | `CONDITIONAL_JUMP`
<a id="insn-00bafdc8"></a> `00bafdc8` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bafdcc"></a> `00bafdcc` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bafdd0"></a> `00bafdd0` | `77 22 00 91` | add x23,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bafdd4"></a> `00bafdd4` | `19 01 40 f9` | ldr x25,[x8] | `FALL_THROUGH`
<a id="insn-00bafdd8"></a> `00bafdd8` | `35 03 09 8b` | add x21,x25,x9 | `FALL_THROUGH`
<a id="insn-00bafddc"></a> `00bafddc` | `08 13 40 f9` | ldr x8,[x24, #0x20] | `FALL_THROUGH`
<a id="insn-00bafde0"></a> `00bafde0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafde4"></a> `00bafde4` | `36 03 08 8b` | add x22,x25,x8 | `FALL_THROUGH`
<a id="insn-00bafde8"></a> `00bafde8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bafdec"></a> `00bafdec` | `99 ad 02 94` | bl 0x00c5b450 | `UNCONDITIONAL_CALL`
<a id="insn-00bafdf0"></a> `00bafdf0` | `c0 00 f8 36` | tbz w0,#0x1f,0x00bafe08 | `CONDITIONAL_JUMP`
<a id="insn-00bafdf4"></a> `00bafdf4` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00bafdf8"></a> `00bafdf8` | `48 02 00 b4` | cbz x8,0x00bafe40 | `CONDITIONAL_JUMP`
<a id="insn-00bafdfc"></a> `00bafdfc` | `f7 03 18 aa` | mov x23,x24 | `FALL_THROUGH`
<a id="insn-00bafe00"></a> `00bafe00` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00bafe04"></a> `00bafe04` | `f6 ff ff 17` | b 0x00bafddc | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe08"></a> `00bafe08` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bafe0c"></a> `00bafe0c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafe10"></a> `00bafe10` | `90 ad 02 94` | bl 0x00c5b450 | `UNCONDITIONAL_CALL`
<a id="insn-00bafe14"></a> `00bafe14` | `e0 00 f8 36` | tbz w0,#0x1f,0x00bafe30 | `CONDITIONAL_JUMP`
<a id="insn-00bafe18"></a> `00bafe18` | `f7 03 18 aa` | mov x23,x24 | `FALL_THROUGH`
<a id="insn-00bafe1c"></a> `00bafe1c` | `e8 8e 40 f8` | ldr x8,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafe20"></a> `00bafe20` | `88 00 00 b4` | cbz x8,0x00bafe30 | `CONDITIONAL_JUMP`
<a id="insn-00bafe24"></a> `00bafe24` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00bafe28"></a> `00bafe28` | `ed ff ff 17` | b 0x00bafddc | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe2c"></a> `00bafe2c` | `f8 03 17 aa` | mov x24,x23 | `FALL_THROUGH`
<a id="insn-00bafe30"></a> `00bafe30` | `f5 02 40 f9` | ldr x21,[x23] | `FALL_THROUGH`
<a id="insn-00bafe34"></a> `00bafe34` | `d5 00 00 b4` | cbz x21,0x00bafe4c | `CONDITIONAL_JUMP`
<a id="insn-00bafe38"></a> `00bafe38` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bafe3c"></a> `00bafe3c` | `19 00 00 14` | b 0x00bafea0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe40"></a> `00bafe40` | `f7 03 18 aa` | mov x23,x24 | `FALL_THROUGH`
<a id="insn-00bafe44"></a> `00bafe44` | `f5 02 40 f9` | ldr x21,[x23] | `FALL_THROUGH`
<a id="insn-00bafe48"></a> `00bafe48` | `95 ff ff b5` | cbnz x21,0x00bafe38 | `CONDITIONAL_JUMP`
<a id="insn-00bafe4c"></a> `00bafe4c` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00bafe50"></a> `00bafe50` | `10 9f 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bafe54"></a> `00bafe54` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bafe58"></a> `00bafe58` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bafe5c"></a> `00bafe5c` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bafe60"></a> `00bafe60` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bafe64"></a> `00bafe64` | `08 10 00 f9` | str x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bafe68"></a> `00bafe68` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00bafe6c"></a> `00bafe6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bafe70"></a> `00bafe70` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bafe74"></a> `00bafe74` | `88 00 00 b4` | cbz x8,0x00bafe84 | `CONDITIONAL_JUMP`
<a id="insn-00bafe78"></a> `00bafe78` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bafe7c"></a> `00bafe7c` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00bafe80"></a> `00bafe80` | `02 00 00 14` | b 0x00bafe88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe84"></a> `00bafe84` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafe88"></a> `00bafe88` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bafe8c"></a> `00bafe8c` | `d5 ac 02 94` | bl 0x00c5b1e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bafe90"></a> `00bafe90` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bafe94"></a> `00bafe94` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe98"></a> `00bafe98` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe9c"></a> `00bafe9c` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bafea0"></a> `00bafea0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafea4"></a> `00bafea4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafea8"></a> `00bafea8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafeac"></a> `00bafeac` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafeb0"></a> `00bafeb0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafeb4"></a> `00bafeb4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bafeb8"></a> `00bafeb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafd9c`](#insn-00bafd9c) 範囲 `[['00bafd9c', '00bafdc7']]`
  - `CONDITIONAL_JUMP` [`00bafdc4`](#insn-00bafdc4) → [`00bafe2c`](#insn-00bafe2c)
  - `FALL_THROUGH` [`00bafdc4`](#insn-00bafdc4) → [`00bafdc8`](#insn-00bafdc8)
- ブロック [`00bafdc8`](#insn-00bafdc8) 範囲 `[['00bafdc8', '00bafddb']]`
  - `FALL_THROUGH` [`00bafdd8`](#insn-00bafdd8) → [`00bafddc`](#insn-00bafddc)
- ブロック [`00bafddc`](#insn-00bafddc) 範囲 `[['00bafddc', '00bafdf3']]`
  - `CONDITIONAL_JUMP` [`00bafdf0`](#insn-00bafdf0) → [`00bafe08`](#insn-00bafe08)
  - `FALL_THROUGH` [`00bafdf0`](#insn-00bafdf0) → [`00bafdf4`](#insn-00bafdf4)
- ブロック [`00bafdf4`](#insn-00bafdf4) 範囲 `[['00bafdf4', '00bafdfb']]`
  - `CONDITIONAL_JUMP` [`00bafdf8`](#insn-00bafdf8) → [`00bafe40`](#insn-00bafe40)
  - `FALL_THROUGH` [`00bafdf8`](#insn-00bafdf8) → [`00bafdfc`](#insn-00bafdfc)
- ブロック [`00bafdfc`](#insn-00bafdfc) 範囲 `[['00bafdfc', '00bafe07']]`
  - `UNCONDITIONAL_JUMP` [`00bafe04`](#insn-00bafe04) → [`00bafddc`](#insn-00bafddc)
- ブロック [`00bafe08`](#insn-00bafe08) 範囲 `[['00bafe08', '00bafe0f']]`
  - `FALL_THROUGH` [`00bafe0c`](#insn-00bafe0c) → [`00bafe10`](#insn-00bafe10)
- ブロック [`00bafe10`](#insn-00bafe10) 範囲 `[['00bafe10', '00bafe13']]`
  - `FALL_THROUGH` [`00bafe10`](#insn-00bafe10) → [`00bafe14`](#insn-00bafe14)
- ブロック [`00bafe14`](#insn-00bafe14) 範囲 `[['00bafe14', '00bafe17']]`
  - `CONDITIONAL_JUMP` [`00bafe14`](#insn-00bafe14) → [`00bafe30`](#insn-00bafe30)
  - `FALL_THROUGH` [`00bafe14`](#insn-00bafe14) → [`00bafe18`](#insn-00bafe18)
- ブロック [`00bafe18`](#insn-00bafe18) 範囲 `[['00bafe18', '00bafe23']]`
  - `CONDITIONAL_JUMP` [`00bafe20`](#insn-00bafe20) → [`00bafe30`](#insn-00bafe30)
  - `FALL_THROUGH` [`00bafe20`](#insn-00bafe20) → [`00bafe24`](#insn-00bafe24)
- ブロック [`00bafe24`](#insn-00bafe24) 範囲 `[['00bafe24', '00bafe2b']]`
  - `UNCONDITIONAL_JUMP` [`00bafe28`](#insn-00bafe28) → [`00bafddc`](#insn-00bafddc)
- ブロック [`00bafe2c`](#insn-00bafe2c) 範囲 `[['00bafe2c', '00bafe2f']]`
  - `FALL_THROUGH` [`00bafe2c`](#insn-00bafe2c) → [`00bafe30`](#insn-00bafe30)
- ブロック [`00bafe30`](#insn-00bafe30) 範囲 `[['00bafe30', '00bafe33']]`
  - `FALL_THROUGH` [`00bafe30`](#insn-00bafe30) → [`00bafe34`](#insn-00bafe34)
- ブロック [`00bafe34`](#insn-00bafe34) 範囲 `[['00bafe34', '00bafe37']]`
  - `CONDITIONAL_JUMP` [`00bafe34`](#insn-00bafe34) → [`00bafe4c`](#insn-00bafe4c)
  - `FALL_THROUGH` [`00bafe34`](#insn-00bafe34) → [`00bafe38`](#insn-00bafe38)
- ブロック [`00bafe38`](#insn-00bafe38) 範囲 `[['00bafe38', '00bafe3b']]`
  - `FALL_THROUGH` [`00bafe38`](#insn-00bafe38) → [`00bafe3c`](#insn-00bafe3c)
- ブロック [`00bafe3c`](#insn-00bafe3c) 範囲 `[['00bafe3c', '00bafe3f']]`
  - `UNCONDITIONAL_JUMP` [`00bafe3c`](#insn-00bafe3c) → [`00bafea0`](#insn-00bafea0)
- ブロック [`00bafe40`](#insn-00bafe40) 範囲 `[['00bafe40', '00bafe4b']]`
  - `CONDITIONAL_JUMP` [`00bafe48`](#insn-00bafe48) → [`00bafe38`](#insn-00bafe38)
  - `FALL_THROUGH` [`00bafe48`](#insn-00bafe48) → [`00bafe4c`](#insn-00bafe4c)
- ブロック [`00bafe4c`](#insn-00bafe4c) 範囲 `[['00bafe4c', '00bafe77']]`
  - `CONDITIONAL_JUMP` [`00bafe74`](#insn-00bafe74) → [`00bafe84`](#insn-00bafe84)
  - `FALL_THROUGH` [`00bafe74`](#insn-00bafe74) → [`00bafe78`](#insn-00bafe78)
- ブロック [`00bafe78`](#insn-00bafe78) 範囲 `[['00bafe78', '00bafe83']]`
  - `UNCONDITIONAL_JUMP` [`00bafe80`](#insn-00bafe80) → [`00bafe88`](#insn-00bafe88)
- ブロック [`00bafe84`](#insn-00bafe84) 範囲 `[['00bafe84', '00bafe87']]`
  - `FALL_THROUGH` [`00bafe84`](#insn-00bafe84) → [`00bafe88`](#insn-00bafe88)
- ブロック [`00bafe88`](#insn-00bafe88) 範囲 `[['00bafe88', '00bafe9f']]`
  - `FALL_THROUGH` [`00bafe9c`](#insn-00bafe9c) → [`00bafea0`](#insn-00bafea0)
- ブロック [`00bafea0`](#insn-00bafea0) 範囲 `[['00bafea0', '00bafebb']]`

## 命令位置別の参照

- [`00bafd9c`](#insn-00bafd9c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafda0`](#insn-00bafda0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafda4`](#insn-00bafda4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafda8`](#insn-00bafda8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdac`](#insn-00bafdac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdc4`](#insn-00bafdc4) → [`00bafe2c`](#insn-00bafe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdec`](#insn-00bafdec) → [`00c5b450`](../00c5b/00c5b450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b450` · 推定シンボル `None` · 推定型 `None`
- [`00bafdf0`](#insn-00bafdf0) → [`00bafe08`](#insn-00bafe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdf8`](#insn-00bafdf8) → [`00bafe40`](#insn-00bafe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe04`](#insn-00bafe04) → [`00bafddc`](#insn-00bafddc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe10`](#insn-00bafe10) → [`00c5b450`](../00c5b/00c5b450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b450` · 推定シンボル `None` · 推定型 `None`
- [`00bafe14`](#insn-00bafe14) → [`00bafe30`](#insn-00bafe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe20`](#insn-00bafe20) → [`00bafe30`](#insn-00bafe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe28`](#insn-00bafe28) → [`00bafddc`](#insn-00bafddc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe34`](#insn-00bafe34) → [`00bafe4c`](#insn-00bafe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe3c`](#insn-00bafe3c) → [`00bafea0`](#insn-00bafea0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe48`](#insn-00bafe48) → [`00bafe38`](#insn-00bafe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe50`](#insn-00bafe50) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bafe74`](#insn-00bafe74) → [`00bafe84`](#insn-00bafe84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe80`](#insn-00bafe80) → [`00bafe88`](#insn-00bafe88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe8c`](#insn-00bafe8c) → [`00c5b1e0`](../00c5b/00c5b1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1e0` · 推定シンボル `None` · 推定型 `None`
- [`00bafea4`](#insn-00bafea4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafea8`](#insn-00bafea8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafeac`](#insn-00bafeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafeb0`](#insn-00bafeb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafd9c`](#insn-00bafd9c)

~~~json
{
  "source": "00bafd9c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafda0`](#insn-00bafda0)

~~~json
{
  "source": "00bafda0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafda4`](#insn-00bafda4)

~~~json
{
  "source": "00bafda4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafda8`](#insn-00bafda8)

~~~json
{
  "source": "00bafda8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdac`](#insn-00bafdac)

~~~json
{
  "source": "00bafdac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdc4`](#insn-00bafdc4)

~~~json
{
  "source": "00bafdc4",
  "target": "00bafe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdec`](#insn-00bafdec)

~~~json
{
  "source": "00bafdec",
  "target": "00c5b450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafdf0`](#insn-00bafdf0)

~~~json
{
  "source": "00bafdf0",
  "target": "00bafe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdf8`](#insn-00bafdf8)

~~~json
{
  "source": "00bafdf8",
  "target": "00bafe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe04`](#insn-00bafe04)

~~~json
{
  "source": "00bafe04",
  "target": "00bafddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe10`](#insn-00bafe10)

~~~json
{
  "source": "00bafe10",
  "target": "00c5b450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafe14`](#insn-00bafe14)

~~~json
{
  "source": "00bafe14",
  "target": "00bafe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe20`](#insn-00bafe20)

~~~json
{
  "source": "00bafe20",
  "target": "00bafe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe28`](#insn-00bafe28)

~~~json
{
  "source": "00bafe28",
  "target": "00bafddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe34`](#insn-00bafe34)

~~~json
{
  "source": "00bafe34",
  "target": "00bafe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe3c`](#insn-00bafe3c)

~~~json
{
  "source": "00bafe3c",
  "target": "00bafea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe48`](#insn-00bafe48)

~~~json
{
  "source": "00bafe48",
  "target": "00bafe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe50`](#insn-00bafe50)

~~~json
{
  "source": "00bafe50",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafe74`](#insn-00bafe74)

~~~json
{
  "source": "00bafe74",
  "target": "00bafe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe80`](#insn-00bafe80)

~~~json
{
  "source": "00bafe80",
  "target": "00bafe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe8c`](#insn-00bafe8c)

~~~json
{
  "source": "00bafe8c",
  "target": "00c5b1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafea4`](#insn-00bafea4)

~~~json
{
  "source": "00bafea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafea8`](#insn-00bafea8)

~~~json
{
  "source": "00bafea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafeac`](#insn-00bafeac)

~~~json
{
  "source": "00bafeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafeb0`](#insn-00bafeb0)

~~~json
{
  "source": "00bafeb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
