# 00bafc4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4430c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md) · 移動量 `+0x6b940`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0063.md#compare-e7af31317c00cce9ad9aa0de5f91498b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb0074`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0074.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-0cf666136c6d2c21504897da2fa42fb5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafc4c",
  "name": "_ZN11flexbuffers7Builder3KeyEPKcm",
  "size": 336,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "856686002a95dcad79afd5d7bebac587d267c1a4b13760f4de3ee22584931245",
  "source_text_sha256": "856686002a95dcad79afd5d7bebac587d267c1a4b13760f4de3ee22584931245",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafc4c",
        "00bafd9b"
      ]
    ],
    "bytes_sha256": "58e83dc117ad591bb9f0a216a8ba5a53ae7900b9d8dda23157ca1515153a7cc0",
    "instruction_count": 84,
    "instruction_bytes": 336,
    "body_bytes": 336,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c4c0](../00c5c/00c5c4c0.md)

## 呼び出し先

- [00b994c4](../00b99/00b994c4.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5b260](../00c5b/00c5b260.md)
- [00c5b450](../00c5b/00c5b450.md)
- [00c5cbe0](../00c5c/00c5cbe0.md)
- [00c5cc80](../00c5c/00c5cc80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2474 bytes

~~~c

void _ZN11flexbuffers7Builder3KeyEPKcm(long *param_1,long param_2,long param_3)

{
  long lVar1;
  int iVar2;
  ulong uVar3;
  ulong uVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  long *plVar8;
  long lVar9;
  ulong local_70;
  undefined8 local_68;
  ulong local_60;
  long local_58;
  
                    /* try { // try from 00bafc5c to 00cafd13 has its CatchHandler @ 00baf838 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  uVar4 = param_1[1] - *param_1;
  local_60 = uVar4;
  _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8_
            (param_1,param_1[1],param_2,param_3 + param_2 + 1);
  uVar7 = uVar4;
  if ((*(byte *)((long)param_1 + 0x34) & 1) != 0) {
    plVar6 = param_1 + 9;
    plVar8 = (long *)*plVar6;
    if (plVar8 != (long *)0x0) {
      lVar9 = *(long *)param_1[0xb];
      plVar5 = plVar6;
      do {
        iVar2 = strcmp((char *)(lVar9 + plVar8[4]),(char *)(lVar9 + uVar4));
        if (iVar2 >= 0) {
          plVar5 = plVar8;
        }
        plVar8 = (long *)plVar8[iVar2 < 0];
      } while (plVar8 != (long *)0x0);
      if (plVar5 != plVar6) {
        uVar7 = plVar5[4];
        iVar2 = strcmp((char *)(lVar9 + uVar4),(char *)(lVar9 + uVar7));
        if (-1 < iVar2) {
          uVar3 = param_1[1] - *param_1;
          if (uVar4 < uVar3 || uVar4 - uVar3 == 0) {
            local_60 = uVar7;
            if (uVar4 < uVar3) {
              param_1[1] = *param_1 + uVar4;
            }
          }
          else {
            _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm(param_1,uVar4 - uVar3);
            uVar7 = plVar5[4];
            local_60 = uVar7;
          }
          goto LAB_00bafd14;
        }
      }
    }
    _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
              (param_1 + 8,&local_60,&local_60);
    uVar7 = local_60;
  }
LAB_00bafd14:
                    /* try { // try from 00bafd14 to 00cafd1b has its CatchHandler @ 00bafe10 */
  local_68 = DAT_002c42c0;
  local_70 = uVar7;
  FUN_00b994c4(param_1 + 3,&local_70);
  if (*(long *)(lVar1 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(local_60);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafc4c"></a> `00bafc4c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bafc50"></a> `00bafc50` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafc54"></a> `00bafc54` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafc58"></a> `00bafc58` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafc5c"></a> `00bafc5c` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafc60"></a> `00bafc60` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bafc64"></a> `00bafc64` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bafc68"></a> `00bafc68` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bafc6c"></a> `00bafc6c` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bafc70"></a> `00bafc70` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bafc74"></a> `00bafc74` | `4a 00 08 8b` | add x10,x2,x8 | `FALL_THROUGH`
<a id="insn-00bafc78"></a> `00bafc78` | `43 05 00 91` | add x3,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bafc7c"></a> `00bafc7c` | `e9 0f 00 f9` | str x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bafc80"></a> `00bafc80` | `09 04 40 a9` | ldp x9,x1,[x0] | `FALL_THROUGH`
<a id="insn-00bafc84"></a> `00bafc84` | `e2 03 08 aa` | mov x2,x8 | `FALL_THROUGH`
<a id="insn-00bafc88"></a> `00bafc88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafc8c"></a> `00bafc8c` | `36 00 09 cb` | sub x22,x1,x9 | `FALL_THROUGH`
<a id="insn-00bafc90"></a> `00bafc90` | `f6 0b 00 f9` | str x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafc94"></a> `00bafc94` | `fb b3 02 94` | bl 0x00c5cc80 | `UNCONDITIONAL_CALL`
<a id="insn-00bafc98"></a> `00bafc98` | `68 d2 40 39` | ldrb w8,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00bafc9c"></a> `00bafc9c` | `f8 03 16 aa` | mov x24,x22 | `FALL_THROUGH`
<a id="insn-00bafca0"></a> `00bafca0` | `a8 03 00 36` | tbz w8,#0x0,0x00bafd14 | `CONDITIONAL_JUMP`
<a id="insn-00bafca4"></a> `00bafca4` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00bafca8"></a> `00bafca8` | `19 8f 44 f8` | ldr x25,[x24, #0x48]! | `FALL_THROUGH`
<a id="insn-00bafcac"></a> `00bafcac` | `b9 02 00 b4` | cbz x25,0x00bafd00 | `CONDITIONAL_JUMP`
<a id="insn-00bafcb0"></a> `00bafcb0` | `68 2e 40 f9` | ldr x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bafcb4"></a> `00bafcb4` | `f7 03 18 aa` | mov x23,x24 | `FALL_THROUGH`
<a id="insn-00bafcb8"></a> `00bafcb8` | `1a 01 40 f9` | ldr x26,[x8] | `FALL_THROUGH`
<a id="insn-00bafcbc"></a> `00bafcbc` | `54 03 16 8b` | add x20,x26,x22 | `FALL_THROUGH`
<a id="insn-00bafcc0"></a> `00bafcc0` | `28 13 40 f9` | ldr x8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00bafcc4"></a> `00bafcc4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bafcc8"></a> `00bafcc8` | `40 03 08 8b` | add x0,x26,x8 | `FALL_THROUGH`
<a id="insn-00bafccc"></a> `00bafccc` | `e1 ad 02 94` | bl 0x00c5b450 | `UNCONDITIONAL_CALL`
<a id="insn-00bafcd0"></a> `00bafcd0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bafcd4"></a> `00bafcd4` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00bafcd8"></a> `00bafcd8` | `f7 b2 99 9a` | csel x23,x23,x25,lt | `FALL_THROUGH`
<a id="insn-00bafcdc"></a> `00bafcdc` | `39 5b 68 f8` | ldr x25,[x25, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bafce0"></a> `00bafce0` | `19 ff ff b5` | cbnz x25,0x00bafcc0 | `CONDITIONAL_JUMP`
<a id="insn-00bafce4"></a> `00bafce4` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00bafce8"></a> `00bafce8` | `c0 00 00 54` | b.eq 0x00bafd00 | `CONDITIONAL_JUMP`
<a id="insn-00bafcec"></a> `00bafcec` | `f8 12 40 f9` | ldr x24,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00bafcf0"></a> `00bafcf0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bafcf4"></a> `00bafcf4` | `41 03 18 8b` | add x1,x26,x24 | `FALL_THROUGH`
<a id="insn-00bafcf8"></a> `00bafcf8` | `d6 ad 02 94` | bl 0x00c5b450 | `UNCONDITIONAL_CALL`
<a id="insn-00bafcfc"></a> `00bafcfc` | `20 03 f8 36` | tbz w0,#0x1f,0x00bafd60 | `CONDITIONAL_JUMP`
<a id="insn-00bafd00"></a> `00bafd00` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00bafd04"></a> `00bafd04` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bafd08"></a> `00bafd08` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bafd0c"></a> `00bafd0c` | `b5 b3 02 94` | bl 0x00c5cbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bafd10"></a> `00bafd10` | `f8 0b 40 f9` | ldr x24,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafd14"></a> `00bafd14` | `a8 b8 ff b0` | adrp x8,0x2c4000 | `FALL_THROUGH`
<a id="insn-00bafd18"></a> `00bafd18` | `00 61 41 fd` | ldr d0,[x8, #0x2c0] | `FALL_THROUGH`
<a id="insn-00bafd1c"></a> `00bafd1c` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bafd20"></a> `00bafd20` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bafd24"></a> `00bafd24` | `f8 03 00 f9` | str x24,[sp] | `FALL_THROUGH`
<a id="insn-00bafd28"></a> `00bafd28` | `e0 07 00 fd` | str d0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bafd2c"></a> `00bafd2c` | `e6 a5 ff 97` | bl 0x00b994c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bafd30"></a> `00bafd30` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafd34"></a> `00bafd34` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bafd38"></a> `00bafd38` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bafd3c"></a> `00bafd3c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bafd40"></a> `00bafd40` | `c1 02 00 54` | b.ne 0x00bafd98 | `CONDITIONAL_JUMP`
<a id="insn-00bafd44"></a> `00bafd44` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bafd48"></a> `00bafd48` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafd4c"></a> `00bafd4c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafd50"></a> `00bafd50` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafd54"></a> `00bafd54` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafd58"></a> `00bafd58` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bafd5c"></a> `00bafd5c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafd60"></a> `00bafd60` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bafd64"></a> `00bafd64` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00bafd68"></a> `00bafd68` | `c1 02 09 eb` | subs x1,x22,x9 | `FALL_THROUGH`
<a id="insn-00bafd6c"></a> `00bafd6c` | `c9 00 00 54` | b.ls 0x00bafd84 | `CONDITIONAL_JUMP`
<a id="insn-00bafd70"></a> `00bafd70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bafd74"></a> `00bafd74` | `3b ad 02 94` | bl 0x00c5b260 | `UNCONDITIONAL_CALL`
<a id="insn-00bafd78"></a> `00bafd78` | `f8 12 40 f9` | ldr x24,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00bafd7c"></a> `00bafd7c` | `f8 0b 00 f9` | str x24,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafd80"></a> `00bafd80` | `e5 ff ff 17` | b 0x00bafd14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafd84"></a> `00bafd84` | `62 00 00 54` | b.cs 0x00bafd90 | `CONDITIONAL_JUMP`
<a id="insn-00bafd88"></a> `00bafd88` | `08 01 16 8b` | add x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00bafd8c"></a> `00bafd8c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bafd90"></a> `00bafd90` | `f8 0b 00 f9` | str x24,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafd94"></a> `00bafd94` | `e0 ff ff 17` | b 0x00bafd14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafd98"></a> `00bafd98` | `52 9f 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafc4c`](#insn-00bafc4c) 範囲 `[['00bafc4c', '00bafc5b']]`
  - `FALL_THROUGH` [`00bafc58`](#insn-00bafc58) → [`00bafc5c`](#insn-00bafc5c)
- ブロック [`00bafc5c`](#insn-00bafc5c) 範囲 `[['00bafc5c', '00bafca3']]`
  - `CONDITIONAL_JUMP` [`00bafca0`](#insn-00bafca0) → [`00bafd14`](#insn-00bafd14)
  - `FALL_THROUGH` [`00bafca0`](#insn-00bafca0) → [`00bafca4`](#insn-00bafca4)
- ブロック [`00bafca4`](#insn-00bafca4) 範囲 `[['00bafca4', '00bafcaf']]`
  - `CONDITIONAL_JUMP` [`00bafcac`](#insn-00bafcac) → [`00bafd00`](#insn-00bafd00)
  - `FALL_THROUGH` [`00bafcac`](#insn-00bafcac) → [`00bafcb0`](#insn-00bafcb0)
- ブロック [`00bafcb0`](#insn-00bafcb0) 範囲 `[['00bafcb0', '00bafcbf']]`
  - `FALL_THROUGH` [`00bafcbc`](#insn-00bafcbc) → [`00bafcc0`](#insn-00bafcc0)
- ブロック [`00bafcc0`](#insn-00bafcc0) 範囲 `[['00bafcc0', '00bafce3']]`
  - `CONDITIONAL_JUMP` [`00bafce0`](#insn-00bafce0) → [`00bafcc0`](#insn-00bafcc0)
  - `FALL_THROUGH` [`00bafce0`](#insn-00bafce0) → [`00bafce4`](#insn-00bafce4)
- ブロック [`00bafce4`](#insn-00bafce4) 範囲 `[['00bafce4', '00bafceb']]`
  - `CONDITIONAL_JUMP` [`00bafce8`](#insn-00bafce8) → [`00bafd00`](#insn-00bafd00)
  - `FALL_THROUGH` [`00bafce8`](#insn-00bafce8) → [`00bafcec`](#insn-00bafcec)
- ブロック [`00bafcec`](#insn-00bafcec) 範囲 `[['00bafcec', '00bafcff']]`
  - `CONDITIONAL_JUMP` [`00bafcfc`](#insn-00bafcfc) → [`00bafd60`](#insn-00bafd60)
  - `FALL_THROUGH` [`00bafcfc`](#insn-00bafcfc) → [`00bafd00`](#insn-00bafd00)
- ブロック [`00bafd00`](#insn-00bafd00) 範囲 `[['00bafd00', '00bafd13']]`
  - `FALL_THROUGH` [`00bafd10`](#insn-00bafd10) → [`00bafd14`](#insn-00bafd14)
- ブロック [`00bafd14`](#insn-00bafd14) 範囲 `[['00bafd14', '00bafd43']]`
  - `CONDITIONAL_JUMP` [`00bafd40`](#insn-00bafd40) → [`00bafd98`](#insn-00bafd98)
  - `FALL_THROUGH` [`00bafd40`](#insn-00bafd40) → [`00bafd44`](#insn-00bafd44)
- ブロック [`00bafd44`](#insn-00bafd44) 範囲 `[['00bafd44', '00bafd5f']]`
- ブロック [`00bafd60`](#insn-00bafd60) 範囲 `[['00bafd60', '00bafd6f']]`
  - `CONDITIONAL_JUMP` [`00bafd6c`](#insn-00bafd6c) → [`00bafd84`](#insn-00bafd84)
  - `FALL_THROUGH` [`00bafd6c`](#insn-00bafd6c) → [`00bafd70`](#insn-00bafd70)
- ブロック [`00bafd70`](#insn-00bafd70) 範囲 `[['00bafd70', '00bafd83']]`
  - `UNCONDITIONAL_JUMP` [`00bafd80`](#insn-00bafd80) → [`00bafd14`](#insn-00bafd14)
- ブロック [`00bafd84`](#insn-00bafd84) 範囲 `[['00bafd84', '00bafd87']]`
  - `CONDITIONAL_JUMP` [`00bafd84`](#insn-00bafd84) → [`00bafd90`](#insn-00bafd90)
  - `FALL_THROUGH` [`00bafd84`](#insn-00bafd84) → [`00bafd88`](#insn-00bafd88)
- ブロック [`00bafd88`](#insn-00bafd88) 範囲 `[['00bafd88', '00bafd8f']]`
  - `FALL_THROUGH` [`00bafd8c`](#insn-00bafd8c) → [`00bafd90`](#insn-00bafd90)
- ブロック [`00bafd90`](#insn-00bafd90) 範囲 `[['00bafd90', '00bafd97']]`
  - `UNCONDITIONAL_JUMP` [`00bafd94`](#insn-00bafd94) → [`00bafd14`](#insn-00bafd14)
- ブロック [`00bafd98`](#insn-00bafd98) 範囲 `[['00bafd98', '00bafd9b']]`

## 命令位置別の参照

- [`00bafc50`](#insn-00bafc50) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc54`](#insn-00bafc54) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc58`](#insn-00bafc58) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc5c`](#insn-00bafc5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc60`](#insn-00bafc60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc7c`](#insn-00bafc7c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc90`](#insn-00bafc90) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc94`](#insn-00bafc94) → [`00c5cc80`](../00c5c/00c5cc80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc80` · 推定シンボル `None` · 推定型 `None`
- [`00bafca0`](#insn-00bafca0) → [`00bafd14`](#insn-00bafd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcac`](#insn-00bafcac) → [`00bafd00`](#insn-00bafd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafccc`](#insn-00bafccc) → [`00c5b450`](../00c5b/00c5b450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b450` · 推定シンボル `None` · 推定型 `None`
- [`00bafce0`](#insn-00bafce0) → [`00bafcc0`](#insn-00bafcc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafce8`](#insn-00bafce8) → [`00bafd00`](#insn-00bafd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcf8`](#insn-00bafcf8) → [`00c5b450`](../00c5b/00c5b450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b450` · 推定シンボル `None` · 推定型 `None`
- [`00bafcfc`](#insn-00bafcfc) → [`00bafd60`](#insn-00bafd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd0c`](#insn-00bafd0c) → [`00c5cbe0`](../00c5c/00c5cbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cbe0` · 推定シンボル `None` · 推定型 `None`
- [`00bafd10`](#insn-00bafd10) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd18`](#insn-00bafd18) → `002c42c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafd24`](#insn-00bafd24) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd28`](#insn-00bafd28) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd2c`](#insn-00bafd2c) → [`00b994c4`](../00b99/00b994c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b994c4` · 推定シンボル `None` · 推定型 `None`
- [`00bafd30`](#insn-00bafd30) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd38`](#insn-00bafd38) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd40`](#insn-00bafd40) → [`00bafd98`](#insn-00bafd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd44`](#insn-00bafd44) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd48`](#insn-00bafd48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd4c`](#insn-00bafd4c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd50`](#insn-00bafd50) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd54`](#insn-00bafd54) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd6c`](#insn-00bafd6c) → [`00bafd84`](#insn-00bafd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd74`](#insn-00bafd74) → [`00c5b260`](../00c5b/00c5b260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b260` · 推定シンボル `None` · 推定型 `None`
- [`00bafd7c`](#insn-00bafd7c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd80`](#insn-00bafd80) → [`00bafd14`](#insn-00bafd14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd84`](#insn-00bafd84) → [`00bafd90`](#insn-00bafd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd90`](#insn-00bafd90) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd94`](#insn-00bafd94) → [`00bafd14`](#insn-00bafd14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd98`](#insn-00bafd98) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafc50`](#insn-00bafc50)

~~~json
{
  "source": "00bafc50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc54`](#insn-00bafc54)

~~~json
{
  "source": "00bafc54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc58`](#insn-00bafc58)

~~~json
{
  "source": "00bafc58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc5c`](#insn-00bafc5c)

~~~json
{
  "source": "00bafc5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc60`](#insn-00bafc60)

~~~json
{
  "source": "00bafc60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc7c`](#insn-00bafc7c)

~~~json
{
  "source": "00bafc7c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc90`](#insn-00bafc90)

~~~json
{
  "source": "00bafc90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc94`](#insn-00bafc94)

~~~json
{
  "source": "00bafc94",
  "target": "00c5cc80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafca0`](#insn-00bafca0)

~~~json
{
  "source": "00bafca0",
  "target": "00bafd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcac`](#insn-00bafcac)

~~~json
{
  "source": "00bafcac",
  "target": "00bafd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafccc`](#insn-00bafccc)

~~~json
{
  "source": "00bafccc",
  "target": "00c5b450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafce0`](#insn-00bafce0)

~~~json
{
  "source": "00bafce0",
  "target": "00bafcc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafce8`](#insn-00bafce8)

~~~json
{
  "source": "00bafce8",
  "target": "00bafd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcf8`](#insn-00bafcf8)

~~~json
{
  "source": "00bafcf8",
  "target": "00c5b450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafcfc`](#insn-00bafcfc)

~~~json
{
  "source": "00bafcfc",
  "target": "00bafd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd0c`](#insn-00bafd0c)

~~~json
{
  "source": "00bafd0c",
  "target": "00c5cbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafd10`](#insn-00bafd10)

~~~json
{
  "source": "00bafd10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd18`](#insn-00bafd18)

~~~json
{
  "source": "00bafd18",
  "target": "002c42c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c42c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0400000000000000",
  "capture_start": "002c42c0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bafd24`](#insn-00bafd24)

~~~json
{
  "source": "00bafd24",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd28`](#insn-00bafd28)

~~~json
{
  "source": "00bafd28",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd2c`](#insn-00bafd2c)

~~~json
{
  "source": "00bafd2c",
  "target": "00b994c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafd30`](#insn-00bafd30)

~~~json
{
  "source": "00bafd30",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd38`](#insn-00bafd38)

~~~json
{
  "source": "00bafd38",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd40`](#insn-00bafd40)

~~~json
{
  "source": "00bafd40",
  "target": "00bafd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd44`](#insn-00bafd44)

~~~json
{
  "source": "00bafd44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd48`](#insn-00bafd48)

~~~json
{
  "source": "00bafd48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd4c`](#insn-00bafd4c)

~~~json
{
  "source": "00bafd4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd50`](#insn-00bafd50)

~~~json
{
  "source": "00bafd50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd54`](#insn-00bafd54)

~~~json
{
  "source": "00bafd54",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd6c`](#insn-00bafd6c)

~~~json
{
  "source": "00bafd6c",
  "target": "00bafd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd74`](#insn-00bafd74)

~~~json
{
  "source": "00bafd74",
  "target": "00c5b260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafd7c`](#insn-00bafd7c)

~~~json
{
  "source": "00bafd7c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd80`](#insn-00bafd80)

~~~json
{
  "source": "00bafd80",
  "target": "00bafd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd84`](#insn-00bafd84)

~~~json
{
  "source": "00bafd84",
  "target": "00bafd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd90`](#insn-00bafd90)

~~~json
{
  "source": "00bafd90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd94`](#insn-00bafd94)

~~~json
{
  "source": "00bafd94",
  "target": "00bafd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd98`](#insn-00bafd98)

~~~json
{
  "source": "00bafd98",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
