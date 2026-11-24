# 00abaadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5cb24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cb24.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-dbc752fb17da619326bf27a62c6ff545)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abacd8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aba/00abacd8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-be10c30061c00d88d0b54e5f31b6f001)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abaadc",
  "name": "FUN_00abaadc",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "149d6d557778f4dd1b4c1a315ec57e89799b9d6aa9375d6e030ce775f4abb50b",
  "source_text_sha256": "149d6d557778f4dd1b4c1a315ec57e89799b9d6aa9375d6e030ce775f4abb50b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abaadc",
        "00abad7f"
      ]
    ],
    "bytes_sha256": "c79d7472c7472508e803df8ed530fb18ca3b95250686832e0e62e3083ae8553b",
    "instruction_count": 169,
    "instruction_bytes": 676,
    "body_bytes": 676,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [00ab2fa8](../00ab2/00ab2fa8.md)
- [00ab6544](../00ab6/00ab6544.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [008514b8](../00851/008514b8.md)
- [00ab8fbc](../00ab8/00ab8fbc.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6279 bytes

~~~c

bool FUN_00abaadc(int param_1,undefined4 param_2)

{
  long lVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long lVar6;
  bool bVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  long lVar10;
  int iVar11;
  int local_98 [2];
  void *local_90;
  void *local_88;
  long local_68;
  
                    /* catch() { ... } // from try @ 00aba890 with catch @ 00abaadc */
                    /* catch() { ... } // from try @ 00aba90c with catch @ 00abaae4 */
                    /* catch() { ... } // from try @ 00aba9b8 with catch @ 00abaaec */
                    /* catch() { ... } // from try @ 00aba930 with catch @ 00abaaf4 */
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  if (param_1 == 3) {
    bVar7 = false;
  }
  else {
    lVar10 = 0;
    do {
      lVar2 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00abacb4 with catch @ 00abab64
                       catch() { ... } // from try @ 00abaed4 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb054 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb1c8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb31c with catch @ 00abab64
                       catch() { ... } // from try @ 00abb418 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb6c8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb7b8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb8a8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abbadc with catch @ 00abab64
                       catch() { ... } // from try @ 00abbc70 with catch @ 00abab64
                       catch() { ... } // from try @ 00abbd38 with catch @ 00abab64
                       catch() { ... } // from try @ 00abbdf0 with catch @ 00abab64 */
      FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
      lVar2 = (long)local_98[0];
      bVar7 = lVar2 <= lVar10;
      if (local_90 != (void *)0x0) {
        local_88 = local_90;
        _ZdlPv(local_90);
      }
      if (lVar2 <= lVar10) {
        bVar7 = true;
        break;
      }
      lVar2 = FUN_008514b8();
      FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
      iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      local_88 = local_90;
      _ZdlPv(local_90);
      if (iVar11 < 0x2e) {
        lVar2 = FUN_008514b8();
        FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = 0x2d - *(int *)((long)local_90 + lVar10 * 4);
      }
      else {
        lVar2 = FUN_008514b8();
                    /* try { // try from 00abac00 to 00bbac07 has its CatchHandler @ 00abcb58 */
        FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      }
      local_88 = local_90;
      _ZdlPv(local_90);
      lVar2 = FUN_008514b8();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2);
                    /* try { // try from 00abac24 to 00bbac2f has its CatchHandler @ 00abcb3c */
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar5, puVar9 = puVar3, param_1 < *(int *)(puVar3 + 4)) {
            puVar5 = (undefined8 *)*puVar3;
            puVar8 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abac60;
          }
          if (param_1 <= *(int *)(puVar3 + 4)) goto LAB_00abacbc;
          puVar5 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar8 = puVar3 + 1;
      }
LAB_00abac60:
      puVar3 = (undefined8 *)_Znwm(0x40);
      *(int *)(puVar3 + 4) = param_1;
      puVar3[7] = 0;
                    /* try { // try from 00abac7c to 00bbac87 has its CatchHandler @ 00abcaa4 */
      puVar3[6] = 0;
      puVar3[5] = puVar3 + 6;
                    /* try { // try from 00abac88 to 00bbac97 has its CatchHandler @ 00abc9f8 */
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = puVar9;
      *puVar8 = puVar3;
                    /* try { // try from 00abac98 to 00bbacb3 has its CatchHandler @ 00abc960 */
      lVar6 = **(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar2);
      puVar5 = puVar3;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar2) = lVar6;
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bb64(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2),puVar5);
                    /* try { // try from 00abacb4 to 00bbae17 has its CatchHandler @ 00abab64 */
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) + 1;
LAB_00abacbc:
      puVar8 = puVar3 + 6;
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar9 = puVar4, iVar11 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar8 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00abad00;
          }
          if (iVar11 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00abab48;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar8 = puVar4 + 1;
      }
LAB_00abad00:
      puVar4 = (undefined8 *)_Znwm(0x28);
      *(int *)((long)puVar4 + 0x1c) = iVar11;
      *(undefined1 *)(puVar4 + 4) = 0;
      *puVar4 = 0;
      puVar4[1] = 0;
      puVar4[2] = puVar9;
      *puVar8 = puVar4;
      puVar5 = puVar4;
      if (*(long *)puVar3[5] != 0) {
        puVar3[5] = *(long *)puVar3[5];
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bb64(puVar3[6],puVar5);
      puVar3[7] = puVar3[7] + 1;
LAB_00abab48:
      lVar10 = lVar10 + 1;
    } while ((*(byte *)(puVar4 + 4) & 1) != 0);
  }
  if (*(long *)(lVar1 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return bVar7;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abaadc"></a> `00abaadc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abaae0"></a> `00abaae0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abaae4"></a> `00abaae4` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abaae8"></a> `00abaae8` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abaaec"></a> `00abaaec` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abaaf0"></a> `00abaaf0` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abaaf4"></a> `00abaaf4` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abaaf8"></a> `00abaaf8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abaafc"></a> `00abaafc` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abab00"></a> `00abab00` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abab04"></a> `00abab04` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00abab08"></a> `00abab08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abab0c"></a> `00abab0c` | `61 00 00 54` | b.ne 0x00abab18 | `CONDITIONAL_JUMP`
<a id="insn-00abab10"></a> `00abab10` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00abab14"></a> `00abab14` | `8d 00 00 14` | b 0x00abad48 | `UNCONDITIONAL_JUMP`
<a id="insn-00abab18"></a> `00abab18` | `1a dc 94 52` | mov w26,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00abab1c"></a> `00abab1c` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00abab20"></a> `00abab20` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abab24"></a> `00abab24` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00abab28"></a> `00abab28` | `3a 05 a0 72` | movk w26,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00abab2c"></a> `00abab2c` | `e9 03 00 f9` | str x9,[sp] | `FALL_THROUGH`
<a id="insn-00abab30"></a> `00abab30` | `09 00 00 14` | b 0x00abab54 | `UNCONDITIONAL_JUMP`
<a id="insn-00abab34"></a> `00abab34` | `60 1b 40 f9` | ldr x0,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00abab38"></a> `00abab38` | `0b 04 e6 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-00abab3c"></a> `00abab3c` | `68 1f 40 f9` | ldr x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00abab40"></a> `00abab40` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abab44"></a> `00abab44` | `68 1f 00 f9` | str x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00abab48"></a> `00abab48` | `e8 82 40 39` | ldrb w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00abab4c"></a> `00abab4c` | `39 07 00 91` | add x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00abab50"></a> `00abab50` | `a8 0f 00 36` | tbz w8,#0x0,0x00abad44 | `CONDITIONAL_JUMP`
<a id="insn-00abab54"></a> `00abab54` | `59 5a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abab58"></a> `00abab58` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abab5c"></a> `00abab5c` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abab60"></a> `00abab60` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abab64"></a> `00abab64` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abab68"></a> `00abab68` | `15 f9 ff 97` | bl 0x00ab8fbc | `UNCONDITIONAL_CALL`
<a id="insn-00abab6c"></a> `00abab6c` | `f6 0b 80 b9` | ldrsw x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abab70"></a> `00abab70` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abab74"></a> `00abab74` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00abab78"></a> `00abab78` | `f5 b7 9f 1a` | cset w21,ge | `FALL_THROUGH`
<a id="insn-00abab7c"></a> `00abab7c` | `60 00 00 b4` | cbz x0,0x00abab88 | `CONDITIONAL_JUMP`
<a id="insn-00abab80"></a> `00abab80` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abab84"></a> `00abab84` | `cb 73 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abab88"></a> `00abab88` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00abab8c"></a> `00abab8c` | `aa 0d 00 54` | b.ge 0x00abad40 | `CONDITIONAL_JUMP`
<a id="insn-00abab90"></a> `00abab90` | `4a 5a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abab94"></a> `00abab94` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abab98"></a> `00abab98` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abab9c"></a> `00abab9c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ababa0"></a> `00ababa0` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00ababa4"></a> `00ababa4` | `06 f9 ff 97` | bl 0x00ab8fbc | `UNCONDITIONAL_CALL`
<a id="insn-00ababa8"></a> `00ababa8` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ababac"></a> `00ababac` | `16 78 79 b8` | ldr w22,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ababb0"></a> `00ababb0` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ababb4"></a> `00ababb4` | `bf 73 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00ababb8"></a> `00ababb8` | `df b6 00 71` | cmp w22,#0x2d | `FALL_THROUGH`
<a id="insn-00ababbc"></a> `00ababbc` | `ac 01 00 54` | b.gt 0x00ababf0 | `CONDITIONAL_JUMP`
<a id="insn-00ababc0"></a> `00ababc0` | `3e 5a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00ababc4"></a> `00ababc4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ababc8"></a> `00ababc8` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00ababcc"></a> `00ababcc` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ababd0"></a> `00ababd0` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00ababd4"></a> `00ababd4` | `fa f8 ff 97` | bl 0x00ab8fbc | `UNCONDITIONAL_CALL`
<a id="insn-00ababd8"></a> `00ababd8` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ababdc"></a> `00ababdc` | `a9 05 80 52` | mov w9,#0x2d | `FALL_THROUGH`
<a id="insn-00ababe0"></a> `00ababe0` | `08 78 79 b8` | ldr w8,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ababe4"></a> `00ababe4` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ababe8"></a> `00ababe8` | `3c 01 08 4b` | sub w28,w9,w8 | `FALL_THROUGH`
<a id="insn-00ababec"></a> `00ababec` | `0a 00 00 14` | b 0x00abac14 | `UNCONDITIONAL_JUMP`
<a id="insn-00ababf0"></a> `00ababf0` | `32 5a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00ababf4"></a> `00ababf4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ababf8"></a> `00ababf8` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00ababfc"></a> `00ababfc` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abac00"></a> `00abac00` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abac04"></a> `00abac04` | `ee f8 ff 97` | bl 0x00ab8fbc | `UNCONDITIONAL_CALL`
<a id="insn-00abac08"></a> `00abac08` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abac0c"></a> `00abac0c` | `1c 78 79 b8` | ldr w28,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abac10"></a> `00abac10` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abac14"></a> `00abac14` | `a7 73 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abac18"></a> `00abac18` | `28 5a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abac1c"></a> `00abac1c` | `17 e0 4c 91` | add x23,x0,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00abac20"></a> `00abac20` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00abac24"></a> `00abac24` | `c8 8e 4d f8` | ldr x8,[x22, #0xd8]! | `FALL_THROUGH`
<a id="insn-00abac28"></a> `00abac28` | `c8 00 00 b5` | cbnz x8,0x00abac40 | `CONDITIONAL_JUMP`
<a id="insn-00abac2c"></a> `00abac2c` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00abac30"></a> `00abac30` | `0c 00 00 14` | b 0x00abac60 | `UNCONDITIONAL_JUMP`
<a id="insn-00abac34"></a> `00abac34` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00abac38"></a> `00abac38` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00abac3c"></a> `00abac3c` | `28 01 00 b4` | cbz x8,0x00abac60 | `CONDITIONAL_JUMP`
<a id="insn-00abac40"></a> `00abac40` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00abac44"></a> `00abac44` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abac48"></a> `00abac48` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00abac4c"></a> `00abac4c` | `4c ff ff 54` | b.gt 0x00abac34 | `CONDITIONAL_JUMP`
<a id="insn-00abac50"></a> `00abac50` | `6a 03 00 54` | b.ge 0x00abacbc | `CONDITIONAL_JUMP`
<a id="insn-00abac54"></a> `00abac54` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00abac58"></a> `00abac58` | `48 ff ff b5` | cbnz x8,0x00abac40 | `CONDITIONAL_JUMP`
<a id="insn-00abac5c"></a> `00abac5c` | `76 23 00 91` | add x22,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00abac60"></a> `00abac60` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00abac64"></a> `00abac64` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00abac68"></a> `00abac68` | `8a 73 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abac6c"></a> `00abac6c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abac70"></a> `00abac70` | `14 20 00 b9` | str w20,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abac74"></a> `00abac74` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00abac78"></a> `00abac78` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abac7c"></a> `00abac7c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abac80"></a> `00abac80` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00abac84"></a> `00abac84` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00abac88"></a> `00abac88` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abac8c"></a> `00abac8c` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abac90"></a> `00abac90` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00abac94"></a> `00abac94` | `e8 6a 40 f9` | ldr x8,[x23, #0xd0] | `FALL_THROUGH`
<a id="insn-00abac98"></a> `00abac98` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abac9c"></a> `00abac9c` | `68 00 00 b4` | cbz x8,0x00abaca8 | `CONDITIONAL_JUMP`
<a id="insn-00abaca0"></a> `00abaca0` | `e8 6a 00 f9` | str x8,[x23, #0xd0] | `FALL_THROUGH`
<a id="insn-00abaca4"></a> `00abaca4` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00abaca8"></a> `00abaca8` | `e0 6e 40 f9` | ldr x0,[x23, #0xd8] | `FALL_THROUGH`
<a id="insn-00abacac"></a> `00abacac` | `ae 03 e6 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-00abacb0"></a> `00abacb0` | `e8 72 40 f9` | ldr x8,[x23, #0xe0] | `FALL_THROUGH`
<a id="insn-00abacb4"></a> `00abacb4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abacb8"></a> `00abacb8` | `e8 72 00 f9` | str x8,[x23, #0xe0] | `FALL_THROUGH`
<a id="insn-00abacbc"></a> `00abacbc` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00abacc0"></a> `00abacc0` | `c8 0e 43 f8` | ldr x8,[x22, #0x30]! | `FALL_THROUGH`
<a id="insn-00abacc4"></a> `00abacc4` | `c8 00 00 b5` | cbnz x8,0x00abacdc | `CONDITIONAL_JUMP`
<a id="insn-00abacc8"></a> `00abacc8` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00abaccc"></a> `00abaccc` | `0d 00 00 14` | b 0x00abad00 | `UNCONDITIONAL_JUMP`
<a id="insn-00abacd0"></a> `00abacd0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abacd4"></a> `00abacd4` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00abacd8"></a> `00abacd8` | `48 01 00 b4` | cbz x8,0x00abad00 | `CONDITIONAL_JUMP`
<a id="insn-00abacdc"></a> `00abacdc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00abace0"></a> `00abace0` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abace4"></a> `00abace4` | `9f 03 08 6b` | cmp w28,w8 | `FALL_THROUGH`
<a id="insn-00abace8"></a> `00abace8` | `4b ff ff 54` | b.lt 0x00abacd0 | `CONDITIONAL_JUMP`
<a id="insn-00abacec"></a> `00abacec` | `1f 01 1c 6b` | cmp w8,w28 | `FALL_THROUGH`
<a id="insn-00abacf0"></a> `00abacf0` | `ca f2 ff 54` | b.ge 0x00abab48 | `CONDITIONAL_JUMP`
<a id="insn-00abacf4"></a> `00abacf4` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00abacf8"></a> `00abacf8` | `28 ff ff b5` | cbnz x8,0x00abacdc | `CONDITIONAL_JUMP`
<a id="insn-00abacfc"></a> `00abacfc` | `f6 22 00 91` | add x22,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abad00"></a> `00abad00` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abad04"></a> `00abad04` | `f8 03 17 aa` | mov x24,x23 | `FALL_THROUGH`
<a id="insn-00abad08"></a> `00abad08` | `62 73 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abad0c"></a> `00abad0c` | `1c 1c 00 b9` | str w28,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abad10"></a> `00abad10` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abad14"></a> `00abad14` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abad18"></a> `00abad18` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abad1c"></a> `00abad1c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abad20"></a> `00abad20` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abad24"></a> `00abad24` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00abad28"></a> `00abad28` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00abad2c"></a> `00abad2c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abad30"></a> `00abad30` | `28 f0 ff b4` | cbz x8,0x00abab34 | `CONDITIONAL_JUMP`
<a id="insn-00abad34"></a> `00abad34` | `68 17 00 f9` | str x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00abad38"></a> `00abad38` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00abad3c"></a> `00abad3c` | `7e ff ff 17` | b 0x00abab34 | `UNCONDITIONAL_JUMP`
<a id="insn-00abad40"></a> `00abad40` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00abad44"></a> `00abad44` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00abad48"></a> `00abad48` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abad4c"></a> `00abad4c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abad50"></a> `00abad50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abad54"></a> `00abad54` | `41 01 00 54` | b.ne 0x00abad7c | `CONDITIONAL_JUMP`
<a id="insn-00abad58"></a> `00abad58` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abad5c"></a> `00abad5c` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abad60"></a> `00abad60` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abad64"></a> `00abad64` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abad68"></a> `00abad68` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abad6c"></a> `00abad6c` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abad70"></a> `00abad70` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abad74"></a> `00abad74` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abad78"></a> `00abad78` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abad7c"></a> `00abad7c` | `59 73 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abaadc`](#insn-00abaadc) 範囲 `[['00abaadc', '00abaae3']]`
  - `FALL_THROUGH` [`00abaae0`](#insn-00abaae0) → [`00abaae4`](#insn-00abaae4)
- ブロック [`00abaae4`](#insn-00abaae4) 範囲 `[['00abaae4', '00abaaeb']]`
  - `FALL_THROUGH` [`00abaae8`](#insn-00abaae8) → [`00abaaec`](#insn-00abaaec)
- ブロック [`00abaaec`](#insn-00abaaec) 範囲 `[['00abaaec', '00abaaf3']]`
  - `FALL_THROUGH` [`00abaaf0`](#insn-00abaaf0) → [`00abaaf4`](#insn-00abaaf4)
- ブロック [`00abaaf4`](#insn-00abaaf4) 範囲 `[['00abaaf4', '00abab0f']]`
  - `CONDITIONAL_JUMP` [`00abab0c`](#insn-00abab0c) → [`00abab18`](#insn-00abab18)
  - `FALL_THROUGH` [`00abab0c`](#insn-00abab0c) → [`00abab10`](#insn-00abab10)
- ブロック [`00abab10`](#insn-00abab10) 範囲 `[['00abab10', '00abab17']]`
  - `UNCONDITIONAL_JUMP` [`00abab14`](#insn-00abab14) → [`00abad48`](#insn-00abad48)
- ブロック [`00abab18`](#insn-00abab18) 範囲 `[['00abab18', '00abab33']]`
  - `UNCONDITIONAL_JUMP` [`00abab30`](#insn-00abab30) → [`00abab54`](#insn-00abab54)
- ブロック [`00abab34`](#insn-00abab34) 範囲 `[['00abab34', '00abab47']]`
  - `FALL_THROUGH` [`00abab44`](#insn-00abab44) → [`00abab48`](#insn-00abab48)
- ブロック [`00abab48`](#insn-00abab48) 範囲 `[['00abab48', '00abab53']]`
  - `CONDITIONAL_JUMP` [`00abab50`](#insn-00abab50) → [`00abad44`](#insn-00abad44)
  - `FALL_THROUGH` [`00abab50`](#insn-00abab50) → [`00abab54`](#insn-00abab54)
- ブロック [`00abab54`](#insn-00abab54) 範囲 `[['00abab54', '00abab63']]`
  - `FALL_THROUGH` [`00abab60`](#insn-00abab60) → [`00abab64`](#insn-00abab64)
- ブロック [`00abab64`](#insn-00abab64) 範囲 `[['00abab64', '00abab7f']]`
  - `CONDITIONAL_JUMP` [`00abab7c`](#insn-00abab7c) → [`00abab88`](#insn-00abab88)
  - `FALL_THROUGH` [`00abab7c`](#insn-00abab7c) → [`00abab80`](#insn-00abab80)
- ブロック [`00abab80`](#insn-00abab80) 範囲 `[['00abab80', '00abab87']]`
  - `FALL_THROUGH` [`00abab84`](#insn-00abab84) → [`00abab88`](#insn-00abab88)
- ブロック [`00abab88`](#insn-00abab88) 範囲 `[['00abab88', '00abab8f']]`
  - `CONDITIONAL_JUMP` [`00abab8c`](#insn-00abab8c) → [`00abad40`](#insn-00abad40)
  - `FALL_THROUGH` [`00abab8c`](#insn-00abab8c) → [`00abab90`](#insn-00abab90)
- ブロック [`00abab90`](#insn-00abab90) 範囲 `[['00abab90', '00ababbf']]`
  - `CONDITIONAL_JUMP` [`00ababbc`](#insn-00ababbc) → [`00ababf0`](#insn-00ababf0)
  - `FALL_THROUGH` [`00ababbc`](#insn-00ababbc) → [`00ababc0`](#insn-00ababc0)
- ブロック [`00ababc0`](#insn-00ababc0) 範囲 `[['00ababc0', '00ababef']]`
  - `UNCONDITIONAL_JUMP` [`00ababec`](#insn-00ababec) → [`00abac14`](#insn-00abac14)
- ブロック [`00ababf0`](#insn-00ababf0) 範囲 `[['00ababf0', '00ababff']]`
  - `FALL_THROUGH` [`00ababfc`](#insn-00ababfc) → [`00abac00`](#insn-00abac00)
- ブロック [`00abac00`](#insn-00abac00) 範囲 `[['00abac00', '00abac13']]`
  - `FALL_THROUGH` [`00abac10`](#insn-00abac10) → [`00abac14`](#insn-00abac14)
- ブロック [`00abac14`](#insn-00abac14) 範囲 `[['00abac14', '00abac23']]`
  - `FALL_THROUGH` [`00abac20`](#insn-00abac20) → [`00abac24`](#insn-00abac24)
- ブロック [`00abac24`](#insn-00abac24) 範囲 `[['00abac24', '00abac2b']]`
  - `CONDITIONAL_JUMP` [`00abac28`](#insn-00abac28) → [`00abac40`](#insn-00abac40)
  - `FALL_THROUGH` [`00abac28`](#insn-00abac28) → [`00abac2c`](#insn-00abac2c)
- ブロック [`00abac2c`](#insn-00abac2c) 範囲 `[['00abac2c', '00abac2f']]`
  - `FALL_THROUGH` [`00abac2c`](#insn-00abac2c) → [`00abac30`](#insn-00abac30)
- ブロック [`00abac30`](#insn-00abac30) 範囲 `[['00abac30', '00abac33']]`
  - `UNCONDITIONAL_JUMP` [`00abac30`](#insn-00abac30) → [`00abac60`](#insn-00abac60)
- ブロック [`00abac34`](#insn-00abac34) 範囲 `[['00abac34', '00abac3f']]`
  - `CONDITIONAL_JUMP` [`00abac3c`](#insn-00abac3c) → [`00abac60`](#insn-00abac60)
  - `FALL_THROUGH` [`00abac3c`](#insn-00abac3c) → [`00abac40`](#insn-00abac40)
- ブロック [`00abac40`](#insn-00abac40) 範囲 `[['00abac40', '00abac4f']]`
  - `CONDITIONAL_JUMP` [`00abac4c`](#insn-00abac4c) → [`00abac34`](#insn-00abac34)
  - `FALL_THROUGH` [`00abac4c`](#insn-00abac4c) → [`00abac50`](#insn-00abac50)
- ブロック [`00abac50`](#insn-00abac50) 範囲 `[['00abac50', '00abac53']]`
  - `CONDITIONAL_JUMP` [`00abac50`](#insn-00abac50) → [`00abacbc`](#insn-00abacbc)
  - `FALL_THROUGH` [`00abac50`](#insn-00abac50) → [`00abac54`](#insn-00abac54)
- ブロック [`00abac54`](#insn-00abac54) 範囲 `[['00abac54', '00abac5b']]`
  - `CONDITIONAL_JUMP` [`00abac58`](#insn-00abac58) → [`00abac40`](#insn-00abac40)
  - `FALL_THROUGH` [`00abac58`](#insn-00abac58) → [`00abac5c`](#insn-00abac5c)
- ブロック [`00abac5c`](#insn-00abac5c) 範囲 `[['00abac5c', '00abac5f']]`
  - `FALL_THROUGH` [`00abac5c`](#insn-00abac5c) → [`00abac60`](#insn-00abac60)
- ブロック [`00abac60`](#insn-00abac60) 範囲 `[['00abac60', '00abac7b']]`
  - `FALL_THROUGH` [`00abac78`](#insn-00abac78) → [`00abac7c`](#insn-00abac7c)
- ブロック [`00abac7c`](#insn-00abac7c) 範囲 `[['00abac7c', '00abac87']]`
  - `FALL_THROUGH` [`00abac84`](#insn-00abac84) → [`00abac88`](#insn-00abac88)
- ブロック [`00abac88`](#insn-00abac88) 範囲 `[['00abac88', '00abac97']]`
  - `FALL_THROUGH` [`00abac94`](#insn-00abac94) → [`00abac98`](#insn-00abac98)
- ブロック [`00abac98`](#insn-00abac98) 範囲 `[['00abac98', '00abac9f']]`
  - `CONDITIONAL_JUMP` [`00abac9c`](#insn-00abac9c) → [`00abaca8`](#insn-00abaca8)
  - `FALL_THROUGH` [`00abac9c`](#insn-00abac9c) → [`00abaca0`](#insn-00abaca0)
- ブロック [`00abaca0`](#insn-00abaca0) 範囲 `[['00abaca0', '00abaca7']]`
  - `FALL_THROUGH` [`00abaca4`](#insn-00abaca4) → [`00abaca8`](#insn-00abaca8)
- ブロック [`00abaca8`](#insn-00abaca8) 範囲 `[['00abaca8', '00abacb3']]`
  - `FALL_THROUGH` [`00abacb0`](#insn-00abacb0) → [`00abacb4`](#insn-00abacb4)
- ブロック [`00abacb4`](#insn-00abacb4) 範囲 `[['00abacb4', '00abacbb']]`
  - `FALL_THROUGH` [`00abacb8`](#insn-00abacb8) → [`00abacbc`](#insn-00abacbc)
- ブロック [`00abacbc`](#insn-00abacbc) 範囲 `[['00abacbc', '00abacc7']]`
  - `CONDITIONAL_JUMP` [`00abacc4`](#insn-00abacc4) → [`00abacdc`](#insn-00abacdc)
  - `FALL_THROUGH` [`00abacc4`](#insn-00abacc4) → [`00abacc8`](#insn-00abacc8)
- ブロック [`00abacc8`](#insn-00abacc8) 範囲 `[['00abacc8', '00abaccf']]`
  - `UNCONDITIONAL_JUMP` [`00abaccc`](#insn-00abaccc) → [`00abad00`](#insn-00abad00)
- ブロック [`00abacd0`](#insn-00abacd0) 範囲 `[['00abacd0', '00abacdb']]`
  - `CONDITIONAL_JUMP` [`00abacd8`](#insn-00abacd8) → [`00abad00`](#insn-00abad00)
  - `FALL_THROUGH` [`00abacd8`](#insn-00abacd8) → [`00abacdc`](#insn-00abacdc)
- ブロック [`00abacdc`](#insn-00abacdc) 範囲 `[['00abacdc', '00abaceb']]`
  - `CONDITIONAL_JUMP` [`00abace8`](#insn-00abace8) → [`00abacd0`](#insn-00abacd0)
  - `FALL_THROUGH` [`00abace8`](#insn-00abace8) → [`00abacec`](#insn-00abacec)
- ブロック [`00abacec`](#insn-00abacec) 範囲 `[['00abacec', '00abacf3']]`
  - `CONDITIONAL_JUMP` [`00abacf0`](#insn-00abacf0) → [`00abab48`](#insn-00abab48)
  - `FALL_THROUGH` [`00abacf0`](#insn-00abacf0) → [`00abacf4`](#insn-00abacf4)
- ブロック [`00abacf4`](#insn-00abacf4) 範囲 `[['00abacf4', '00abacfb']]`
  - `CONDITIONAL_JUMP` [`00abacf8`](#insn-00abacf8) → [`00abacdc`](#insn-00abacdc)
  - `FALL_THROUGH` [`00abacf8`](#insn-00abacf8) → [`00abacfc`](#insn-00abacfc)
- ブロック [`00abacfc`](#insn-00abacfc) 範囲 `[['00abacfc', '00abacff']]`
  - `FALL_THROUGH` [`00abacfc`](#insn-00abacfc) → [`00abad00`](#insn-00abad00)
- ブロック [`00abad00`](#insn-00abad00) 範囲 `[['00abad00', '00abad33']]`
  - `CONDITIONAL_JUMP` [`00abad30`](#insn-00abad30) → [`00abab34`](#insn-00abab34)
  - `FALL_THROUGH` [`00abad30`](#insn-00abad30) → [`00abad34`](#insn-00abad34)
- ブロック [`00abad34`](#insn-00abad34) 範囲 `[['00abad34', '00abad3f']]`
  - `UNCONDITIONAL_JUMP` [`00abad3c`](#insn-00abad3c) → [`00abab34`](#insn-00abab34)
- ブロック [`00abad40`](#insn-00abad40) 範囲 `[['00abad40', '00abad43']]`
  - `FALL_THROUGH` [`00abad40`](#insn-00abad40) → [`00abad44`](#insn-00abad44)
- ブロック [`00abad44`](#insn-00abad44) 範囲 `[['00abad44', '00abad47']]`
  - `FALL_THROUGH` [`00abad44`](#insn-00abad44) → [`00abad48`](#insn-00abad48)
- ブロック [`00abad48`](#insn-00abad48) 範囲 `[['00abad48', '00abad57']]`
  - `CONDITIONAL_JUMP` [`00abad54`](#insn-00abad54) → [`00abad7c`](#insn-00abad7c)
  - `FALL_THROUGH` [`00abad54`](#insn-00abad54) → [`00abad58`](#insn-00abad58)
- ブロック [`00abad58`](#insn-00abad58) 範囲 `[['00abad58', '00abad7b']]`
- ブロック [`00abad7c`](#insn-00abad7c) 範囲 `[['00abad7c', '00abad7f']]`

## 命令位置別の参照

- [`00abaae0`](#insn-00abaae0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaae4`](#insn-00abaae4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaae8`](#insn-00abaae8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaaec`](#insn-00abaaec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaaf0`](#insn-00abaaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaaf4`](#insn-00abaaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab08`](#insn-00abab08) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab0c`](#insn-00abab0c) → [`00abab18`](#insn-00abab18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab14`](#insn-00abab14) → [`00abad48`](#insn-00abad48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab2c`](#insn-00abab2c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab30`](#insn-00abab30) → [`00abab54`](#insn-00abab54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab38`](#insn-00abab38) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`00abab50`](#insn-00abab50) → [`00abad44`](#insn-00abad44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab54`](#insn-00abab54) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abab68`](#insn-00abab68) → [`00ab8fbc`](../00ab8/00ab8fbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab8fbc` · 推定シンボル `None` · 推定型 `None`
- [`00abab6c`](#insn-00abab6c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab70`](#insn-00abab70) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab7c`](#insn-00abab7c) → [`00abab88`](#insn-00abab88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab80`](#insn-00abab80) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab84`](#insn-00abab84) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abab8c`](#insn-00abab8c) → [`00abad40`](#insn-00abad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abab90`](#insn-00abab90) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00ababa4`](#insn-00ababa4) → [`00ab8fbc`](../00ab8/00ab8fbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab8fbc` · 推定シンボル `None` · 推定型 `None`
- [`00ababa8`](#insn-00ababa8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababb0`](#insn-00ababb0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababb4`](#insn-00ababb4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00ababbc`](#insn-00ababbc) → [`00ababf0`](#insn-00ababf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababc0`](#insn-00ababc0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00ababd4`](#insn-00ababd4) → [`00ab8fbc`](../00ab8/00ab8fbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab8fbc` · 推定シンボル `None` · 推定型 `None`
- [`00ababd8`](#insn-00ababd8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababe4`](#insn-00ababe4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababec`](#insn-00ababec) → [`00abac14`](#insn-00abac14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababf0`](#insn-00ababf0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abac04`](#insn-00abac04) → [`00ab8fbc`](../00ab8/00ab8fbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab8fbc` · 推定シンボル `None` · 推定型 `None`
- [`00abac08`](#insn-00abac08) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac10`](#insn-00abac10) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac14`](#insn-00abac14) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abac18`](#insn-00abac18) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abac24`](#insn-00abac24) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abac28`](#insn-00abac28) → [`00abac40`](#insn-00abac40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac30`](#insn-00abac30) → [`00abac60`](#insn-00abac60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac3c`](#insn-00abac3c) → [`00abac60`](#insn-00abac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac4c`](#insn-00abac4c) → [`00abac34`](#insn-00abac34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac50`](#insn-00abac50) → [`00abacbc`](#insn-00abacbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac58`](#insn-00abac58) → [`00abac40`](#insn-00abac40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac68`](#insn-00abac68) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abac90`](#insn-00abac90) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abac94`](#insn-00abac94) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abac9c`](#insn-00abac9c) → [`00abaca8`](#insn-00abaca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaca0`](#insn-00abaca0) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abaca4`](#insn-00abaca4) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abaca8`](#insn-00abaca8) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abacac`](#insn-00abacac) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`00abacb0`](#insn-00abacb0) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abacb8`](#insn-00abacb8) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abacc4`](#insn-00abacc4) → [`00abacdc`](#insn-00abacdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaccc`](#insn-00abaccc) → [`00abad00`](#insn-00abad00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacd8`](#insn-00abacd8) → [`00abad00`](#insn-00abad00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abace8`](#insn-00abace8) → [`00abacd0`](#insn-00abacd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacf0`](#insn-00abacf0) → [`00abab48`](#insn-00abab48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacf8`](#insn-00abacf8) → [`00abacdc`](#insn-00abacdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad08`](#insn-00abad08) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abad30`](#insn-00abad30) → [`00abab34`](#insn-00abab34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad3c`](#insn-00abad3c) → [`00abab34`](#insn-00abab34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad44`](#insn-00abad44) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad4c`](#insn-00abad4c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad54`](#insn-00abad54) → [`00abad7c`](#insn-00abad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad5c`](#insn-00abad5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad60`](#insn-00abad60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad64`](#insn-00abad64) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad68`](#insn-00abad68) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad6c`](#insn-00abad6c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad70`](#insn-00abad70) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad7c`](#insn-00abad7c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abaae0`](#insn-00abaae0)

~~~json
{
  "source": "00abaae0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaae4`](#insn-00abaae4)

~~~json
{
  "source": "00abaae4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaae8`](#insn-00abaae8)

~~~json
{
  "source": "00abaae8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaaec`](#insn-00abaaec)

~~~json
{
  "source": "00abaaec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaaf0`](#insn-00abaaf0)

~~~json
{
  "source": "00abaaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaaf4`](#insn-00abaaf4)

~~~json
{
  "source": "00abaaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab08`](#insn-00abab08)

~~~json
{
  "source": "00abab08",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab0c`](#insn-00abab0c)

~~~json
{
  "source": "00abab0c",
  "target": "00abab18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab14`](#insn-00abab14)

~~~json
{
  "source": "00abab14",
  "target": "00abad48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab2c`](#insn-00abab2c)

~~~json
{
  "source": "00abab2c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab30`](#insn-00abab30)

~~~json
{
  "source": "00abab30",
  "target": "00abab54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab38`](#insn-00abab38)

~~~json
{
  "source": "00abab38",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abab50`](#insn-00abab50)

~~~json
{
  "source": "00abab50",
  "target": "00abad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab54`](#insn-00abab54)

~~~json
{
  "source": "00abab54",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abab68`](#insn-00abab68)

~~~json
{
  "source": "00abab68",
  "target": "00ab8fbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abab6c`](#insn-00abab6c)

~~~json
{
  "source": "00abab6c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab70`](#insn-00abab70)

~~~json
{
  "source": "00abab70",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab7c`](#insn-00abab7c)

~~~json
{
  "source": "00abab7c",
  "target": "00abab88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab80`](#insn-00abab80)

~~~json
{
  "source": "00abab80",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab84`](#insn-00abab84)

~~~json
{
  "source": "00abab84",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abab8c`](#insn-00abab8c)

~~~json
{
  "source": "00abab8c",
  "target": "00abad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abab90`](#insn-00abab90)

~~~json
{
  "source": "00abab90",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ababa4`](#insn-00ababa4)

~~~json
{
  "source": "00ababa4",
  "target": "00ab8fbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ababa8`](#insn-00ababa8)

~~~json
{
  "source": "00ababa8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababb0`](#insn-00ababb0)

~~~json
{
  "source": "00ababb0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababb4`](#insn-00ababb4)

~~~json
{
  "source": "00ababb4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ababbc`](#insn-00ababbc)

~~~json
{
  "source": "00ababbc",
  "target": "00ababf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababc0`](#insn-00ababc0)

~~~json
{
  "source": "00ababc0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ababd4`](#insn-00ababd4)

~~~json
{
  "source": "00ababd4",
  "target": "00ab8fbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ababd8`](#insn-00ababd8)

~~~json
{
  "source": "00ababd8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababe4`](#insn-00ababe4)

~~~json
{
  "source": "00ababe4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababec`](#insn-00ababec)

~~~json
{
  "source": "00ababec",
  "target": "00abac14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababf0`](#insn-00ababf0)

~~~json
{
  "source": "00ababf0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac04`](#insn-00abac04)

~~~json
{
  "source": "00abac04",
  "target": "00ab8fbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac08`](#insn-00abac08)

~~~json
{
  "source": "00abac08",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac10`](#insn-00abac10)

~~~json
{
  "source": "00abac10",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac14`](#insn-00abac14)

~~~json
{
  "source": "00abac14",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac18`](#insn-00abac18)

~~~json
{
  "source": "00abac18",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac24`](#insn-00abac24)

~~~json
{
  "source": "00abac24",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f8c07d0018710a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abac28`](#insn-00abac28)

~~~json
{
  "source": "00abac28",
  "target": "00abac40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac30`](#insn-00abac30)

~~~json
{
  "source": "00abac30",
  "target": "00abac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac3c`](#insn-00abac3c)

~~~json
{
  "source": "00abac3c",
  "target": "00abac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac4c`](#insn-00abac4c)

~~~json
{
  "source": "00abac4c",
  "target": "00abac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac50`](#insn-00abac50)

~~~json
{
  "source": "00abac50",
  "target": "00abacbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac58`](#insn-00abac58)

~~~json
{
  "source": "00abac58",
  "target": "00abac40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac68`](#insn-00abac68)

~~~json
{
  "source": "00abac68",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac90`](#insn-00abac90)

~~~json
{
  "source": "00abac90",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f8c07d0018710a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abac94`](#insn-00abac94)

~~~json
{
  "source": "00abac94",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f4c07d0004710a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abac9c`](#insn-00abac9c)

~~~json
{
  "source": "00abac9c",
  "target": "00abaca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaca0`](#insn-00abaca0)

~~~json
{
  "source": "00abaca0",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f4c07d0004710a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaca4`](#insn-00abaca4)

~~~json
{
  "source": "00abaca4",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f8c07d0018710a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaca8`](#insn-00abaca8)

~~~json
{
  "source": "00abaca8",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f8c07d0018710a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abacac`](#insn-00abacac)

~~~json
{
  "source": "00abacac",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abacb0`](#insn-00abacb0)

~~~json
{
  "source": "00abacb0",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "40c17d0040710a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abacb8`](#insn-00abacb8)

~~~json
{
  "source": "00abacb8",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "40c17d0040710a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abacc4`](#insn-00abacc4)

~~~json
{
  "source": "00abacc4",
  "target": "00abacdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaccc`](#insn-00abaccc)

~~~json
{
  "source": "00abaccc",
  "target": "00abad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacd8`](#insn-00abacd8)

~~~json
{
  "source": "00abacd8",
  "target": "00abad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abace8`](#insn-00abace8)

~~~json
{
  "source": "00abace8",
  "target": "00abacd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacf0`](#insn-00abacf0)

~~~json
{
  "source": "00abacf0",
  "target": "00abab48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacf8`](#insn-00abacf8)

~~~json
{
  "source": "00abacf8",
  "target": "00abacdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad08`](#insn-00abad08)

~~~json
{
  "source": "00abad08",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad30`](#insn-00abad30)

~~~json
{
  "source": "00abad30",
  "target": "00abab34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad3c`](#insn-00abad3c)

~~~json
{
  "source": "00abad3c",
  "target": "00abab34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad44`](#insn-00abad44)

~~~json
{
  "source": "00abad44",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad4c`](#insn-00abad4c)

~~~json
{
  "source": "00abad4c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad54`](#insn-00abad54)

~~~json
{
  "source": "00abad54",
  "target": "00abad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad5c`](#insn-00abad5c)

~~~json
{
  "source": "00abad5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad60`](#insn-00abad60)

~~~json
{
  "source": "00abad60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad64`](#insn-00abad64)

~~~json
{
  "source": "00abad64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad68`](#insn-00abad68)

~~~json
{
  "source": "00abad68",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad6c`](#insn-00abad6c)

~~~json
{
  "source": "00abad6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad70`](#insn-00abad70)

~~~json
{
  "source": "00abad70",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad7c`](#insn-00abad7c)

~~~json
{
  "source": "00abad7c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
