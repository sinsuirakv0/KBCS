# 00abacd8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abaadc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abaadc.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-be10c30061c00d88d0b54e5f31b6f001)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abad48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aba/00abad48.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-ab074a0b6d56a2f45f51c80b6eefa4f7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abacd8",
  "name": "FUN_00abacd8",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0530739e7b858a956d419e5ec4cd78167c038cdbc03dd73dc470b5fbf43a307",
  "source_text_sha256": "b0530739e7b858a956d419e5ec4cd78167c038cdbc03dd73dc470b5fbf43a307",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abacd8",
        "00abaf7b"
      ]
    ],
    "bytes_sha256": "08e1c44d63d303165431097a14a8625fbfaf418695646afc69f5e558792542f1",
    "instruction_count": 169,
    "instruction_bytes": 676,
    "body_bytes": 676,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fe66c](../005fe/005fe66c.md)
- [00ab31a4](../00ab3/00ab31a4.md)
- [00ab6740](../00ab6/00ab6740.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [008514f8](../00851/008514f8.md)
- [00ab91b8](../00ab9/00ab91b8.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6052 bytes

~~~c

bool FUN_00abacd8(int param_1,undefined4 param_2)

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
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00abae50 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb070 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb1f0 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb364 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb4b8 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb5b4 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb864 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb954 with catch @ 00abad00
                       catch() { ... } // from try @ 00abba44 with catch @ 00abad00
                       catch() { ... } // from try @ 00abbc78 with catch @ 00abad00
                       catch() { ... } // from try @ 00abbe0c with catch @ 00abad00
                       catch() { ... } // from try @ 00abbed4 with catch @ 00abad00
                       catch() { ... } // from try @ 00abbf8c with catch @ 00abad00 */
  if (param_1 == 3) {
    bVar7 = false;
  }
  else {
    lVar10 = 0;
    do {
      lVar2 = FUN_008514f8();
      FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
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
      lVar2 = FUN_008514f8();
                    /* try { // try from 00abad9c to 00bbada3 has its CatchHandler @ 00abccf4 */
      FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
      iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      local_88 = local_90;
      _ZdlPv(local_90);
      if (iVar11 < 0x2e) {
        lVar2 = FUN_008514f8();
                    /* try { // try from 00abadc0 to 00bbadcb has its CatchHandler @ 00abccd8 */
                    /* try { // try from 00abadcc to 00bbaddf has its CatchHandler @ 00abccb4 */
        FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = 0x2d - *(int *)((long)local_90 + lVar10 * 4);
      }
      else {
        lVar2 = FUN_008514f8();
        FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      }
      local_88 = local_90;
      _ZdlPv(local_90);
      lVar2 = FUN_008514f8();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2);
                    /* try { // try from 00abae18 to 00bbae23 has its CatchHandler @ 00abcc40 */
                    /* try { // try from 00abae24 to 00bbae33 has its CatchHandler @ 00abcb94 */
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar5, puVar9 = puVar3, param_1 < *(int *)(puVar3 + 4)) {
                    /* try { // try from 00abae34 to 00bbae4f has its CatchHandler @ 00abcafc */
            puVar5 = (undefined8 *)*puVar3;
            puVar8 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abae5c;
          }
          if (param_1 <= *(int *)(puVar3 + 4)) goto LAB_00abaeb8;
                    /* try { // try from 00abae50 to 00bbafb3 has its CatchHandler @ 00abad00 */
          puVar5 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar8 = puVar3 + 1;
      }
LAB_00abae5c:
      puVar3 = (undefined8 *)_Znwm(0x40);
      *(int *)(puVar3 + 4) = param_1;
      puVar3[7] = 0;
      puVar3[6] = 0;
      puVar3[5] = puVar3 + 6;
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = puVar9;
      *puVar8 = puVar3;
      lVar6 = **(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar2);
      puVar5 = puVar3;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar2) = lVar6;
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bba4(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2),puVar5);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) + 1;
LAB_00abaeb8:
      puVar8 = puVar3 + 6;
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar9 = puVar4, iVar11 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar8 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00abaefc;
          }
          if (iVar11 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00abad44;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar8 = puVar4 + 1;
      }
LAB_00abaefc:
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
      FUN_0043bba4(puVar3[6],puVar5);
      puVar3[7] = puVar3[7] + 1;
LAB_00abad44:
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
<a id="insn-00abacd8"></a> `00abacd8` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abacdc"></a> `00abacdc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abace0"></a> `00abace0` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abace4"></a> `00abace4` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abace8"></a> `00abace8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abacec"></a> `00abacec` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abacf0"></a> `00abacf0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abacf4"></a> `00abacf4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abacf8"></a> `00abacf8` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abacfc"></a> `00abacfc` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abad00"></a> `00abad00` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00abad04"></a> `00abad04` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abad08"></a> `00abad08` | `61 00 00 54` | b.ne 0x00abad14 | `CONDITIONAL_JUMP`
<a id="insn-00abad0c"></a> `00abad0c` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00abad10"></a> `00abad10` | `8d 00 00 14` | b 0x00abaf44 | `UNCONDITIONAL_JUMP`
<a id="insn-00abad14"></a> `00abad14` | `1a dc 94 52` | mov w26,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00abad18"></a> `00abad18` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00abad1c"></a> `00abad1c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abad20"></a> `00abad20` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00abad24"></a> `00abad24` | `3a 05 a0 72` | movk w26,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00abad28"></a> `00abad28` | `e9 03 00 f9` | str x9,[sp] | `FALL_THROUGH`
<a id="insn-00abad2c"></a> `00abad2c` | `09 00 00 14` | b 0x00abad50 | `UNCONDITIONAL_JUMP`
<a id="insn-00abad30"></a> `00abad30` | `60 1b 40 f9` | ldr x0,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00abad34"></a> `00abad34` | `9c 03 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00abad38"></a> `00abad38` | `68 1f 40 f9` | ldr x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00abad3c"></a> `00abad3c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abad40"></a> `00abad40` | `68 1f 00 f9` | str x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00abad44"></a> `00abad44` | `e8 82 40 39` | ldrb w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00abad48"></a> `00abad48` | `39 07 00 91` | add x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00abad4c"></a> `00abad4c` | `a8 0f 00 36` | tbz w8,#0x0,0x00abaf40 | `CONDITIONAL_JUMP`
<a id="insn-00abad50"></a> `00abad50` | `ea 59 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abad54"></a> `00abad54` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abad58"></a> `00abad58` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abad5c"></a> `00abad5c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abad60"></a> `00abad60` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abad64"></a> `00abad64` | `15 f9 ff 97` | bl 0x00ab91b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abad68"></a> `00abad68` | `f6 0b 80 b9` | ldrsw x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abad6c"></a> `00abad6c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abad70"></a> `00abad70` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00abad74"></a> `00abad74` | `f5 b7 9f 1a` | cset w21,ge | `FALL_THROUGH`
<a id="insn-00abad78"></a> `00abad78` | `60 00 00 b4` | cbz x0,0x00abad84 | `CONDITIONAL_JUMP`
<a id="insn-00abad7c"></a> `00abad7c` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abad80"></a> `00abad80` | `4c 74 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abad84"></a> `00abad84` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00abad88"></a> `00abad88` | `aa 0d 00 54` | b.ge 0x00abaf3c | `CONDITIONAL_JUMP`
<a id="insn-00abad8c"></a> `00abad8c` | `db 59 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abad90"></a> `00abad90` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abad94"></a> `00abad94` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abad98"></a> `00abad98` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abad9c"></a> `00abad9c` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abada0"></a> `00abada0` | `06 f9 ff 97` | bl 0x00ab91b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abada4"></a> `00abada4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abada8"></a> `00abada8` | `16 78 79 b8` | ldr w22,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abadac"></a> `00abadac` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abadb0"></a> `00abadb0` | `40 74 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abadb4"></a> `00abadb4` | `df b6 00 71` | cmp w22,#0x2d | `FALL_THROUGH`
<a id="insn-00abadb8"></a> `00abadb8` | `ac 01 00 54` | b.gt 0x00abadec | `CONDITIONAL_JUMP`
<a id="insn-00abadbc"></a> `00abadbc` | `cf 59 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abadc0"></a> `00abadc0` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abadc4"></a> `00abadc4` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abadc8"></a> `00abadc8` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abadcc"></a> `00abadcc` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abadd0"></a> `00abadd0` | `fa f8 ff 97` | bl 0x00ab91b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abadd4"></a> `00abadd4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abadd8"></a> `00abadd8` | `a9 05 80 52` | mov w9,#0x2d | `FALL_THROUGH`
<a id="insn-00abaddc"></a> `00abaddc` | `08 78 79 b8` | ldr w8,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abade0"></a> `00abade0` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abade4"></a> `00abade4` | `3c 01 08 4b` | sub w28,w9,w8 | `FALL_THROUGH`
<a id="insn-00abade8"></a> `00abade8` | `0a 00 00 14` | b 0x00abae10 | `UNCONDITIONAL_JUMP`
<a id="insn-00abadec"></a> `00abadec` | `c3 59 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abadf0"></a> `00abadf0` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abadf4"></a> `00abadf4` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abadf8"></a> `00abadf8` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abadfc"></a> `00abadfc` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abae00"></a> `00abae00` | `ee f8 ff 97` | bl 0x00ab91b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abae04"></a> `00abae04` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abae08"></a> `00abae08` | `1c 78 79 b8` | ldr w28,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abae0c"></a> `00abae0c` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abae10"></a> `00abae10` | `28 74 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abae14"></a> `00abae14` | `b9 59 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abae18"></a> `00abae18` | `17 e0 4c 91` | add x23,x0,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00abae1c"></a> `00abae1c` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00abae20"></a> `00abae20` | `c8 8e 4d f8` | ldr x8,[x22, #0xd8]! | `FALL_THROUGH`
<a id="insn-00abae24"></a> `00abae24` | `c8 00 00 b5` | cbnz x8,0x00abae3c | `CONDITIONAL_JUMP`
<a id="insn-00abae28"></a> `00abae28` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00abae2c"></a> `00abae2c` | `0c 00 00 14` | b 0x00abae5c | `UNCONDITIONAL_JUMP`
<a id="insn-00abae30"></a> `00abae30` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00abae34"></a> `00abae34` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00abae38"></a> `00abae38` | `28 01 00 b4` | cbz x8,0x00abae5c | `CONDITIONAL_JUMP`
<a id="insn-00abae3c"></a> `00abae3c` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00abae40"></a> `00abae40` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abae44"></a> `00abae44` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00abae48"></a> `00abae48` | `4c ff ff 54` | b.gt 0x00abae30 | `CONDITIONAL_JUMP`
<a id="insn-00abae4c"></a> `00abae4c` | `6a 03 00 54` | b.ge 0x00abaeb8 | `CONDITIONAL_JUMP`
<a id="insn-00abae50"></a> `00abae50` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00abae54"></a> `00abae54` | `48 ff ff b5` | cbnz x8,0x00abae3c | `CONDITIONAL_JUMP`
<a id="insn-00abae58"></a> `00abae58` | `76 23 00 91` | add x22,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00abae5c"></a> `00abae5c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00abae60"></a> `00abae60` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00abae64"></a> `00abae64` | `0b 74 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abae68"></a> `00abae68` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abae6c"></a> `00abae6c` | `14 20 00 b9` | str w20,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abae70"></a> `00abae70` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00abae74"></a> `00abae74` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abae78"></a> `00abae78` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abae7c"></a> `00abae7c` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00abae80"></a> `00abae80` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00abae84"></a> `00abae84` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abae88"></a> `00abae88` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abae8c"></a> `00abae8c` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00abae90"></a> `00abae90` | `e8 6a 40 f9` | ldr x8,[x23, #0xd0] | `FALL_THROUGH`
<a id="insn-00abae94"></a> `00abae94` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abae98"></a> `00abae98` | `68 00 00 b4` | cbz x8,0x00abaea4 | `CONDITIONAL_JUMP`
<a id="insn-00abae9c"></a> `00abae9c` | `e8 6a 00 f9` | str x8,[x23, #0xd0] | `FALL_THROUGH`
<a id="insn-00abaea0"></a> `00abaea0` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00abaea4"></a> `00abaea4` | `e0 6e 40 f9` | ldr x0,[x23, #0xd8] | `FALL_THROUGH`
<a id="insn-00abaea8"></a> `00abaea8` | `3f 03 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00abaeac"></a> `00abaeac` | `e8 72 40 f9` | ldr x8,[x23, #0xe0] | `FALL_THROUGH`
<a id="insn-00abaeb0"></a> `00abaeb0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abaeb4"></a> `00abaeb4` | `e8 72 00 f9` | str x8,[x23, #0xe0] | `FALL_THROUGH`
<a id="insn-00abaeb8"></a> `00abaeb8` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00abaebc"></a> `00abaebc` | `c8 0e 43 f8` | ldr x8,[x22, #0x30]! | `FALL_THROUGH`
<a id="insn-00abaec0"></a> `00abaec0` | `c8 00 00 b5` | cbnz x8,0x00abaed8 | `CONDITIONAL_JUMP`
<a id="insn-00abaec4"></a> `00abaec4` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00abaec8"></a> `00abaec8` | `0d 00 00 14` | b 0x00abaefc | `UNCONDITIONAL_JUMP`
<a id="insn-00abaecc"></a> `00abaecc` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abaed0"></a> `00abaed0` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00abaed4"></a> `00abaed4` | `48 01 00 b4` | cbz x8,0x00abaefc | `CONDITIONAL_JUMP`
<a id="insn-00abaed8"></a> `00abaed8` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00abaedc"></a> `00abaedc` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abaee0"></a> `00abaee0` | `9f 03 08 6b` | cmp w28,w8 | `FALL_THROUGH`
<a id="insn-00abaee4"></a> `00abaee4` | `4b ff ff 54` | b.lt 0x00abaecc | `CONDITIONAL_JUMP`
<a id="insn-00abaee8"></a> `00abaee8` | `1f 01 1c 6b` | cmp w8,w28 | `FALL_THROUGH`
<a id="insn-00abaeec"></a> `00abaeec` | `ca f2 ff 54` | b.ge 0x00abad44 | `CONDITIONAL_JUMP`
<a id="insn-00abaef0"></a> `00abaef0` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00abaef4"></a> `00abaef4` | `28 ff ff b5` | cbnz x8,0x00abaed8 | `CONDITIONAL_JUMP`
<a id="insn-00abaef8"></a> `00abaef8` | `f6 22 00 91` | add x22,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abaefc"></a> `00abaefc` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abaf00"></a> `00abaf00` | `f8 03 17 aa` | mov x24,x23 | `FALL_THROUGH`
<a id="insn-00abaf04"></a> `00abaf04` | `e3 73 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf08"></a> `00abaf08` | `1c 1c 00 b9` | str w28,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abaf0c"></a> `00abaf0c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abaf10"></a> `00abaf10` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abaf14"></a> `00abaf14` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abaf18"></a> `00abaf18` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abaf1c"></a> `00abaf1c` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abaf20"></a> `00abaf20` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00abaf24"></a> `00abaf24` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00abaf28"></a> `00abaf28` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abaf2c"></a> `00abaf2c` | `28 f0 ff b4` | cbz x8,0x00abad30 | `CONDITIONAL_JUMP`
<a id="insn-00abaf30"></a> `00abaf30` | `68 17 00 f9` | str x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00abaf34"></a> `00abaf34` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00abaf38"></a> `00abaf38` | `7e ff ff 17` | b 0x00abad30 | `UNCONDITIONAL_JUMP`
<a id="insn-00abaf3c"></a> `00abaf3c` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00abaf40"></a> `00abaf40` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00abaf44"></a> `00abaf44` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abaf48"></a> `00abaf48` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abaf4c"></a> `00abaf4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abaf50"></a> `00abaf50` | `41 01 00 54` | b.ne 0x00abaf78 | `CONDITIONAL_JUMP`
<a id="insn-00abaf54"></a> `00abaf54` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abaf58"></a> `00abaf58` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abaf5c"></a> `00abaf5c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abaf60"></a> `00abaf60` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abaf64"></a> `00abaf64` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abaf68"></a> `00abaf68` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abaf6c"></a> `00abaf6c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abaf70"></a> `00abaf70` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abaf74"></a> `00abaf74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abaf78"></a> `00abaf78` | `da 73 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abacd8`](#insn-00abacd8) 範囲 `[['00abacd8', '00abacff']]`
  - `FALL_THROUGH` [`00abacfc`](#insn-00abacfc) → [`00abad00`](#insn-00abad00)
- ブロック [`00abad00`](#insn-00abad00) 範囲 `[['00abad00', '00abad0b']]`
  - `CONDITIONAL_JUMP` [`00abad08`](#insn-00abad08) → [`00abad14`](#insn-00abad14)
  - `FALL_THROUGH` [`00abad08`](#insn-00abad08) → [`00abad0c`](#insn-00abad0c)
- ブロック [`00abad0c`](#insn-00abad0c) 範囲 `[['00abad0c', '00abad13']]`
  - `UNCONDITIONAL_JUMP` [`00abad10`](#insn-00abad10) → [`00abaf44`](#insn-00abaf44)
- ブロック [`00abad14`](#insn-00abad14) 範囲 `[['00abad14', '00abad2f']]`
  - `UNCONDITIONAL_JUMP` [`00abad2c`](#insn-00abad2c) → [`00abad50`](#insn-00abad50)
- ブロック [`00abad30`](#insn-00abad30) 範囲 `[['00abad30', '00abad43']]`
  - `FALL_THROUGH` [`00abad40`](#insn-00abad40) → [`00abad44`](#insn-00abad44)
- ブロック [`00abad44`](#insn-00abad44) 範囲 `[['00abad44', '00abad4f']]`
  - `CONDITIONAL_JUMP` [`00abad4c`](#insn-00abad4c) → [`00abaf40`](#insn-00abaf40)
  - `FALL_THROUGH` [`00abad4c`](#insn-00abad4c) → [`00abad50`](#insn-00abad50)
- ブロック [`00abad50`](#insn-00abad50) 範囲 `[['00abad50', '00abad7b']]`
  - `CONDITIONAL_JUMP` [`00abad78`](#insn-00abad78) → [`00abad84`](#insn-00abad84)
  - `FALL_THROUGH` [`00abad78`](#insn-00abad78) → [`00abad7c`](#insn-00abad7c)
- ブロック [`00abad7c`](#insn-00abad7c) 範囲 `[['00abad7c', '00abad83']]`
  - `FALL_THROUGH` [`00abad80`](#insn-00abad80) → [`00abad84`](#insn-00abad84)
- ブロック [`00abad84`](#insn-00abad84) 範囲 `[['00abad84', '00abad8b']]`
  - `CONDITIONAL_JUMP` [`00abad88`](#insn-00abad88) → [`00abaf3c`](#insn-00abaf3c)
  - `FALL_THROUGH` [`00abad88`](#insn-00abad88) → [`00abad8c`](#insn-00abad8c)
- ブロック [`00abad8c`](#insn-00abad8c) 範囲 `[['00abad8c', '00abad9b']]`
  - `FALL_THROUGH` [`00abad98`](#insn-00abad98) → [`00abad9c`](#insn-00abad9c)
- ブロック [`00abad9c`](#insn-00abad9c) 範囲 `[['00abad9c', '00abadbb']]`
  - `CONDITIONAL_JUMP` [`00abadb8`](#insn-00abadb8) → [`00abadec`](#insn-00abadec)
  - `FALL_THROUGH` [`00abadb8`](#insn-00abadb8) → [`00abadbc`](#insn-00abadbc)
- ブロック [`00abadbc`](#insn-00abadbc) 範囲 `[['00abadbc', '00abadbf']]`
  - `FALL_THROUGH` [`00abadbc`](#insn-00abadbc) → [`00abadc0`](#insn-00abadc0)
- ブロック [`00abadc0`](#insn-00abadc0) 範囲 `[['00abadc0', '00abadcb']]`
  - `FALL_THROUGH` [`00abadc8`](#insn-00abadc8) → [`00abadcc`](#insn-00abadcc)
- ブロック [`00abadcc`](#insn-00abadcc) 範囲 `[['00abadcc', '00abadeb']]`
  - `UNCONDITIONAL_JUMP` [`00abade8`](#insn-00abade8) → [`00abae10`](#insn-00abae10)
- ブロック [`00abadec`](#insn-00abadec) 範囲 `[['00abadec', '00abae0f']]`
  - `FALL_THROUGH` [`00abae0c`](#insn-00abae0c) → [`00abae10`](#insn-00abae10)
- ブロック [`00abae10`](#insn-00abae10) 範囲 `[['00abae10', '00abae17']]`
  - `FALL_THROUGH` [`00abae14`](#insn-00abae14) → [`00abae18`](#insn-00abae18)
- ブロック [`00abae18`](#insn-00abae18) 範囲 `[['00abae18', '00abae23']]`
  - `FALL_THROUGH` [`00abae20`](#insn-00abae20) → [`00abae24`](#insn-00abae24)
- ブロック [`00abae24`](#insn-00abae24) 範囲 `[['00abae24', '00abae27']]`
  - `CONDITIONAL_JUMP` [`00abae24`](#insn-00abae24) → [`00abae3c`](#insn-00abae3c)
  - `FALL_THROUGH` [`00abae24`](#insn-00abae24) → [`00abae28`](#insn-00abae28)
- ブロック [`00abae28`](#insn-00abae28) 範囲 `[['00abae28', '00abae2f']]`
  - `UNCONDITIONAL_JUMP` [`00abae2c`](#insn-00abae2c) → [`00abae5c`](#insn-00abae5c)
- ブロック [`00abae30`](#insn-00abae30) 範囲 `[['00abae30', '00abae33']]`
  - `FALL_THROUGH` [`00abae30`](#insn-00abae30) → [`00abae34`](#insn-00abae34)
- ブロック [`00abae34`](#insn-00abae34) 範囲 `[['00abae34', '00abae3b']]`
  - `CONDITIONAL_JUMP` [`00abae38`](#insn-00abae38) → [`00abae5c`](#insn-00abae5c)
  - `FALL_THROUGH` [`00abae38`](#insn-00abae38) → [`00abae3c`](#insn-00abae3c)
- ブロック [`00abae3c`](#insn-00abae3c) 範囲 `[['00abae3c', '00abae4b']]`
  - `CONDITIONAL_JUMP` [`00abae48`](#insn-00abae48) → [`00abae30`](#insn-00abae30)
  - `FALL_THROUGH` [`00abae48`](#insn-00abae48) → [`00abae4c`](#insn-00abae4c)
- ブロック [`00abae4c`](#insn-00abae4c) 範囲 `[['00abae4c', '00abae4f']]`
  - `CONDITIONAL_JUMP` [`00abae4c`](#insn-00abae4c) → [`00abaeb8`](#insn-00abaeb8)
  - `FALL_THROUGH` [`00abae4c`](#insn-00abae4c) → [`00abae50`](#insn-00abae50)
- ブロック [`00abae50`](#insn-00abae50) 範囲 `[['00abae50', '00abae57']]`
  - `CONDITIONAL_JUMP` [`00abae54`](#insn-00abae54) → [`00abae3c`](#insn-00abae3c)
  - `FALL_THROUGH` [`00abae54`](#insn-00abae54) → [`00abae58`](#insn-00abae58)
- ブロック [`00abae58`](#insn-00abae58) 範囲 `[['00abae58', '00abae5b']]`
  - `FALL_THROUGH` [`00abae58`](#insn-00abae58) → [`00abae5c`](#insn-00abae5c)
- ブロック [`00abae5c`](#insn-00abae5c) 範囲 `[['00abae5c', '00abae9b']]`
  - `CONDITIONAL_JUMP` [`00abae98`](#insn-00abae98) → [`00abaea4`](#insn-00abaea4)
  - `FALL_THROUGH` [`00abae98`](#insn-00abae98) → [`00abae9c`](#insn-00abae9c)
- ブロック [`00abae9c`](#insn-00abae9c) 範囲 `[['00abae9c', '00abaea3']]`
  - `FALL_THROUGH` [`00abaea0`](#insn-00abaea0) → [`00abaea4`](#insn-00abaea4)
- ブロック [`00abaea4`](#insn-00abaea4) 範囲 `[['00abaea4', '00abaeb7']]`
  - `FALL_THROUGH` [`00abaeb4`](#insn-00abaeb4) → [`00abaeb8`](#insn-00abaeb8)
- ブロック [`00abaeb8`](#insn-00abaeb8) 範囲 `[['00abaeb8', '00abaec3']]`
  - `CONDITIONAL_JUMP` [`00abaec0`](#insn-00abaec0) → [`00abaed8`](#insn-00abaed8)
  - `FALL_THROUGH` [`00abaec0`](#insn-00abaec0) → [`00abaec4`](#insn-00abaec4)
- ブロック [`00abaec4`](#insn-00abaec4) 範囲 `[['00abaec4', '00abaecb']]`
  - `UNCONDITIONAL_JUMP` [`00abaec8`](#insn-00abaec8) → [`00abaefc`](#insn-00abaefc)
- ブロック [`00abaecc`](#insn-00abaecc) 範囲 `[['00abaecc', '00abaed7']]`
  - `CONDITIONAL_JUMP` [`00abaed4`](#insn-00abaed4) → [`00abaefc`](#insn-00abaefc)
  - `FALL_THROUGH` [`00abaed4`](#insn-00abaed4) → [`00abaed8`](#insn-00abaed8)
- ブロック [`00abaed8`](#insn-00abaed8) 範囲 `[['00abaed8', '00abaee7']]`
  - `CONDITIONAL_JUMP` [`00abaee4`](#insn-00abaee4) → [`00abaecc`](#insn-00abaecc)
  - `FALL_THROUGH` [`00abaee4`](#insn-00abaee4) → [`00abaee8`](#insn-00abaee8)
- ブロック [`00abaee8`](#insn-00abaee8) 範囲 `[['00abaee8', '00abaeef']]`
  - `CONDITIONAL_JUMP` [`00abaeec`](#insn-00abaeec) → [`00abad44`](#insn-00abad44)
  - `FALL_THROUGH` [`00abaeec`](#insn-00abaeec) → [`00abaef0`](#insn-00abaef0)
- ブロック [`00abaef0`](#insn-00abaef0) 範囲 `[['00abaef0', '00abaef7']]`
  - `CONDITIONAL_JUMP` [`00abaef4`](#insn-00abaef4) → [`00abaed8`](#insn-00abaed8)
  - `FALL_THROUGH` [`00abaef4`](#insn-00abaef4) → [`00abaef8`](#insn-00abaef8)
- ブロック [`00abaef8`](#insn-00abaef8) 範囲 `[['00abaef8', '00abaefb']]`
  - `FALL_THROUGH` [`00abaef8`](#insn-00abaef8) → [`00abaefc`](#insn-00abaefc)
- ブロック [`00abaefc`](#insn-00abaefc) 範囲 `[['00abaefc', '00abaf2f']]`
  - `CONDITIONAL_JUMP` [`00abaf2c`](#insn-00abaf2c) → [`00abad30`](#insn-00abad30)
  - `FALL_THROUGH` [`00abaf2c`](#insn-00abaf2c) → [`00abaf30`](#insn-00abaf30)
- ブロック [`00abaf30`](#insn-00abaf30) 範囲 `[['00abaf30', '00abaf3b']]`
  - `UNCONDITIONAL_JUMP` [`00abaf38`](#insn-00abaf38) → [`00abad30`](#insn-00abad30)
- ブロック [`00abaf3c`](#insn-00abaf3c) 範囲 `[['00abaf3c', '00abaf3f']]`
  - `FALL_THROUGH` [`00abaf3c`](#insn-00abaf3c) → [`00abaf40`](#insn-00abaf40)
- ブロック [`00abaf40`](#insn-00abaf40) 範囲 `[['00abaf40', '00abaf43']]`
  - `FALL_THROUGH` [`00abaf40`](#insn-00abaf40) → [`00abaf44`](#insn-00abaf44)
- ブロック [`00abaf44`](#insn-00abaf44) 範囲 `[['00abaf44', '00abaf53']]`
  - `CONDITIONAL_JUMP` [`00abaf50`](#insn-00abaf50) → [`00abaf78`](#insn-00abaf78)
  - `FALL_THROUGH` [`00abaf50`](#insn-00abaf50) → [`00abaf54`](#insn-00abaf54)
- ブロック [`00abaf54`](#insn-00abaf54) 範囲 `[['00abaf54', '00abaf77']]`
- ブロック [`00abaf78`](#insn-00abaf78) 範囲 `[['00abaf78', '00abaf7b']]`

## 命令位置別の参照

- [`00abacdc`](#insn-00abacdc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abace0`](#insn-00abace0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abace4`](#insn-00abace4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abace8`](#insn-00abace8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacec`](#insn-00abacec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacf0`](#insn-00abacf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad04`](#insn-00abad04) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad08`](#insn-00abad08) → [`00abad14`](#insn-00abad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad10`](#insn-00abad10) → [`00abaf44`](#insn-00abaf44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad28`](#insn-00abad28) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad2c`](#insn-00abad2c) → [`00abad50`](#insn-00abad50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad34`](#insn-00abad34) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00abad4c`](#insn-00abad4c) → [`00abaf40`](#insn-00abaf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad50`](#insn-00abad50) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abad64`](#insn-00abad64) → [`00ab91b8`](../00ab9/00ab91b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab91b8` · 推定シンボル `None` · 推定型 `None`
- [`00abad68`](#insn-00abad68) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad6c`](#insn-00abad6c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad78`](#insn-00abad78) → [`00abad84`](#insn-00abad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad7c`](#insn-00abad7c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad80`](#insn-00abad80) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abad88`](#insn-00abad88) → [`00abaf3c`](#insn-00abaf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad8c`](#insn-00abad8c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abada0`](#insn-00abada0) → [`00ab91b8`](../00ab9/00ab91b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab91b8` · 推定シンボル `None` · 推定型 `None`
- [`00abada4`](#insn-00abada4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadac`](#insn-00abadac) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadb0`](#insn-00abadb0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abadb8`](#insn-00abadb8) → [`00abadec`](#insn-00abadec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadbc`](#insn-00abadbc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abadd0`](#insn-00abadd0) → [`00ab91b8`](../00ab9/00ab91b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab91b8` · 推定シンボル `None` · 推定型 `None`
- [`00abadd4`](#insn-00abadd4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abade0`](#insn-00abade0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abade8`](#insn-00abade8) → [`00abae10`](#insn-00abae10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadec`](#insn-00abadec) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abae00`](#insn-00abae00) → [`00ab91b8`](../00ab9/00ab91b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab91b8` · 推定シンボル `None` · 推定型 `None`
- [`00abae04`](#insn-00abae04) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae0c`](#insn-00abae0c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae10`](#insn-00abae10) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abae14`](#insn-00abae14) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abae20`](#insn-00abae20) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abae24`](#insn-00abae24) → [`00abae3c`](#insn-00abae3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae2c`](#insn-00abae2c) → [`00abae5c`](#insn-00abae5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae38`](#insn-00abae38) → [`00abae5c`](#insn-00abae5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae48`](#insn-00abae48) → [`00abae30`](#insn-00abae30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae4c`](#insn-00abae4c) → [`00abaeb8`](#insn-00abaeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae54`](#insn-00abae54) → [`00abae3c`](#insn-00abae3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae64`](#insn-00abae64) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abae8c`](#insn-00abae8c) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abae90`](#insn-00abae90) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abae98`](#insn-00abae98) → [`00abaea4`](#insn-00abaea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae9c`](#insn-00abae9c) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abaea0`](#insn-00abaea0) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abaea4`](#insn-00abaea4) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abaea8`](#insn-00abaea8) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00abaeac`](#insn-00abaeac) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abaeb4`](#insn-00abaeb4) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abaec0`](#insn-00abaec0) → [`00abaed8`](#insn-00abaed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaec8`](#insn-00abaec8) → [`00abaefc`](#insn-00abaefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaed4`](#insn-00abaed4) → [`00abaefc`](#insn-00abaefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaee4`](#insn-00abaee4) → [`00abaecc`](#insn-00abaecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaeec`](#insn-00abaeec) → [`00abad44`](#insn-00abad44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaef4`](#insn-00abaef4) → [`00abaed8`](#insn-00abaed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf04`](#insn-00abaf04) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abaf2c`](#insn-00abaf2c) → [`00abad30`](#insn-00abad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf38`](#insn-00abaf38) → [`00abad30`](#insn-00abad30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf40`](#insn-00abaf40) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf48`](#insn-00abaf48) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf50`](#insn-00abaf50) → [`00abaf78`](#insn-00abaf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf58`](#insn-00abaf58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf5c`](#insn-00abaf5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf60`](#insn-00abaf60) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf64`](#insn-00abaf64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf68`](#insn-00abaf68) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf6c`](#insn-00abaf6c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf78`](#insn-00abaf78) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abacdc`](#insn-00abacdc)

~~~json
{
  "source": "00abacdc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abace0`](#insn-00abace0)

~~~json
{
  "source": "00abace0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abace4`](#insn-00abace4)

~~~json
{
  "source": "00abace4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abace8`](#insn-00abace8)

~~~json
{
  "source": "00abace8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacec`](#insn-00abacec)

~~~json
{
  "source": "00abacec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacf0`](#insn-00abacf0)

~~~json
{
  "source": "00abacf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad04`](#insn-00abad04)

~~~json
{
  "source": "00abad04",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad08`](#insn-00abad08)

~~~json
{
  "source": "00abad08",
  "target": "00abad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad10`](#insn-00abad10)

~~~json
{
  "source": "00abad10",
  "target": "00abaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad28`](#insn-00abad28)

~~~json
{
  "source": "00abad28",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad2c`](#insn-00abad2c)

~~~json
{
  "source": "00abad2c",
  "target": "00abad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad34`](#insn-00abad34)

~~~json
{
  "source": "00abad34",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad4c`](#insn-00abad4c)

~~~json
{
  "source": "00abad4c",
  "target": "00abaf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad50`](#insn-00abad50)

~~~json
{
  "source": "00abad50",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad64`](#insn-00abad64)

~~~json
{
  "source": "00abad64",
  "target": "00ab91b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad68`](#insn-00abad68)

~~~json
{
  "source": "00abad68",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad6c`](#insn-00abad6c)

~~~json
{
  "source": "00abad6c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad78`](#insn-00abad78)

~~~json
{
  "source": "00abad78",
  "target": "00abad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad7c`](#insn-00abad7c)

~~~json
{
  "source": "00abad7c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad80`](#insn-00abad80)

~~~json
{
  "source": "00abad80",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad88`](#insn-00abad88)

~~~json
{
  "source": "00abad88",
  "target": "00abaf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad8c`](#insn-00abad8c)

~~~json
{
  "source": "00abad8c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abada0`](#insn-00abada0)

~~~json
{
  "source": "00abada0",
  "target": "00ab91b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abada4`](#insn-00abada4)

~~~json
{
  "source": "00abada4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadac`](#insn-00abadac)

~~~json
{
  "source": "00abadac",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadb0`](#insn-00abadb0)

~~~json
{
  "source": "00abadb0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abadb8`](#insn-00abadb8)

~~~json
{
  "source": "00abadb8",
  "target": "00abadec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadbc`](#insn-00abadbc)

~~~json
{
  "source": "00abadbc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abadd0`](#insn-00abadd0)

~~~json
{
  "source": "00abadd0",
  "target": "00ab91b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abadd4`](#insn-00abadd4)

~~~json
{
  "source": "00abadd4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abade0`](#insn-00abade0)

~~~json
{
  "source": "00abade0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abade8`](#insn-00abade8)

~~~json
{
  "source": "00abade8",
  "target": "00abae10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadec`](#insn-00abadec)

~~~json
{
  "source": "00abadec",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae00`](#insn-00abae00)

~~~json
{
  "source": "00abae00",
  "target": "00ab91b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae04`](#insn-00abae04)

~~~json
{
  "source": "00abae04",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae0c`](#insn-00abae0c)

~~~json
{
  "source": "00abae0c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae10`](#insn-00abae10)

~~~json
{
  "source": "00abae10",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae14`](#insn-00abae14)

~~~json
{
  "source": "00abae14",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae20`](#insn-00abae20)

~~~json
{
  "source": "00abae20",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ecbf7d00709c1100",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abae24`](#insn-00abae24)

~~~json
{
  "source": "00abae24",
  "target": "00abae3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae2c`](#insn-00abae2c)

~~~json
{
  "source": "00abae2c",
  "target": "00abae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae38`](#insn-00abae38)

~~~json
{
  "source": "00abae38",
  "target": "00abae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae48`](#insn-00abae48)

~~~json
{
  "source": "00abae48",
  "target": "00abae30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae4c`](#insn-00abae4c)

~~~json
{
  "source": "00abae4c",
  "target": "00abaeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae54`](#insn-00abae54)

~~~json
{
  "source": "00abae54",
  "target": "00abae3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae64`](#insn-00abae64)

~~~json
{
  "source": "00abae64",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae8c`](#insn-00abae8c)

~~~json
{
  "source": "00abae8c",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ecbf7d00709c1100",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abae90`](#insn-00abae90)

~~~json
{
  "source": "00abae90",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8bf7d0064700a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abae98`](#insn-00abae98)

~~~json
{
  "source": "00abae98",
  "target": "00abaea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae9c`](#insn-00abae9c)

~~~json
{
  "source": "00abae9c",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8bf7d0064700a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaea0`](#insn-00abaea0)

~~~json
{
  "source": "00abaea0",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ecbf7d00709c1100",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaea4`](#insn-00abaea4)

~~~json
{
  "source": "00abaea4",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ecbf7d00709c1100",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaea8`](#insn-00abaea8)

~~~json
{
  "source": "00abaea8",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaeac`](#insn-00abaeac)

~~~json
{
  "source": "00abaeac",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c47d0078700a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaeb4`](#insn-00abaeb4)

~~~json
{
  "source": "00abaeb4",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c47d0078700a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaec0`](#insn-00abaec0)

~~~json
{
  "source": "00abaec0",
  "target": "00abaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaec8`](#insn-00abaec8)

~~~json
{
  "source": "00abaec8",
  "target": "00abaefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaed4`](#insn-00abaed4)

~~~json
{
  "source": "00abaed4",
  "target": "00abaefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaee4`](#insn-00abaee4)

~~~json
{
  "source": "00abaee4",
  "target": "00abaecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaeec`](#insn-00abaeec)

~~~json
{
  "source": "00abaeec",
  "target": "00abad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaef4`](#insn-00abaef4)

~~~json
{
  "source": "00abaef4",
  "target": "00abaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf04`](#insn-00abaf04)

~~~json
{
  "source": "00abaf04",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf2c`](#insn-00abaf2c)

~~~json
{
  "source": "00abaf2c",
  "target": "00abad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf38`](#insn-00abaf38)

~~~json
{
  "source": "00abaf38",
  "target": "00abad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf40`](#insn-00abaf40)

~~~json
{
  "source": "00abaf40",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf48`](#insn-00abaf48)

~~~json
{
  "source": "00abaf48",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf50`](#insn-00abaf50)

~~~json
{
  "source": "00abaf50",
  "target": "00abaf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf58`](#insn-00abaf58)

~~~json
{
  "source": "00abaf58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf5c`](#insn-00abaf5c)

~~~json
{
  "source": "00abaf5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf60`](#insn-00abaf60)

~~~json
{
  "source": "00abaf60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf64`](#insn-00abaf64)

~~~json
{
  "source": "00abaf64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf68`](#insn-00abaf68)

~~~json
{
  "source": "00abaf68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf6c`](#insn-00abaf6c)

~~~json
{
  "source": "00abaf6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf78`](#insn-00abaf78)

~~~json
{
  "source": "00abaf78",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
