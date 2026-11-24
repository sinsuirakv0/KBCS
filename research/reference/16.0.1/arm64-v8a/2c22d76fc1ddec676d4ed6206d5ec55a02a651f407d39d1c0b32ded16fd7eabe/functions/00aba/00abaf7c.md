# 00abaf7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abad80`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abad80.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-ad61e09f663c5f744ebf3ff243d59006)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abafec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aba/00abafec.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-562909f98e3f9544068b4e7c6f9d7e62)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abaf7c",
  "name": "FUN_00abaf7c",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "de5a7817fca7de86d24bc2642b06a1fd48120dfee6b8de531e1b695a73a05916",
  "source_text_sha256": "de5a7817fca7de86d24bc2642b06a1fd48120dfee6b8de531e1b695a73a05916",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abaf7c",
        "00abb123"
      ]
    ],
    "bytes_sha256": "c0e955cbcae041b16d9cfaf75209456e3dbe92df83333bd5ec4259417cb1f7a2",
    "instruction_count": 106,
    "instruction_bytes": 424,
    "body_bytes": 424,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a84d88](../00a84/00a84d88.md)
- [00a85294](../00a85/00a85294.md)
- [00a8670c](../00a86/00a8670c.md)
- [00a86810](../00a86/00a86810.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [008514f8](../00851/008514f8.md)
- [00c57e90](../00c57/00c57e90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3739 bytes

~~~c

int FUN_00abaf7c(void)

{
  long lVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  long *plVar5;
  long lVar6;
  int iVar7;
  undefined8 *puVar8;
  int iVar9;
  undefined8 *puVar10;
  
  iVar7 = 0;
  iVar9 = 0;
  do {
    if (iVar9 != 3) {
      lVar1 = FUN_008514f8();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1);
                    /* try { // try from 00abafe0 to 00bbafeb has its CatchHandler @ 00abca54 */
                    /* try { // try from 00abafec to 00bbafff has its CatchHandler @ 00abca40 */
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar2 = puVar4, puVar8 = puVar2, iVar9 < *(int *)(puVar2 + 4)) {
            puVar4 = (undefined8 *)*puVar2;
            puVar10 = puVar2;
            if ((undefined8 *)*puVar2 == (undefined8 *)0x0) goto LAB_00abb028;
          }
          if (iVar9 <= *(int *)(puVar2 + 4)) goto LAB_00abb084;
          puVar4 = (undefined8 *)puVar2[1];
        } while ((undefined8 *)puVar2[1] != (undefined8 *)0x0);
        puVar10 = puVar2 + 1;
      }
LAB_00abb028:
      puVar2 = (undefined8 *)_Znwm(0x40);
                    /* try { // try from 00abb038 to 00bbb043 has its CatchHandler @ 00abca00 */
      puVar2[7] = 0;
      puVar2[6] = 0;
                    /* try { // try from 00abb044 to 00bbb053 has its CatchHandler @ 00abc9e0 */
      puVar2[5] = puVar2 + 6;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar8;
                    /* try { // try from 00abb054 to 00bbb06f has its CatchHandler @ 00abc994 */
      *puVar10 = puVar2;
      plVar5 = *(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar1);
      *(int *)(puVar2 + 4) = iVar9;
      lVar6 = *plVar5;
      puVar4 = puVar2;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar1) = lVar6;
        puVar4 = (undefined8 *)*puVar10;
      }
                    /* try { // try from 00abb070 to 00bbb13b has its CatchHandler @ 00abad00 */
      FUN_0043bba4(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1),puVar4);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) + 1;
LAB_00abb084:
      puVar8 = puVar2 + 6;
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar4, puVar8 = puVar3, 0x2f < *(int *)((long)puVar3 + 0x1c)) {
            puVar4 = (undefined8 *)*puVar3;
            puVar10 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abb0c8;
          }
          if (*(int *)((long)puVar3 + 0x1c) == 0x2f) goto LAB_00abafb8;
          puVar4 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar10 = puVar3 + 1;
      }
LAB_00abb0c8:
      puVar3 = (undefined8 *)_Znwm(0x28);
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = puVar8;
      *puVar10 = puVar3;
      plVar5 = (long *)puVar2[5];
      *(undefined4 *)((long)puVar3 + 0x1c) = 0x2f;
      *(undefined1 *)(puVar3 + 4) = 0;
      puVar4 = puVar3;
      if (*plVar5 != 0) {
        puVar2[5] = *plVar5;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bba4(puVar2[6],puVar4);
                    /* try { // try from 00abafb4 to 00bbafc3 has its CatchHandler @ 00abca58 */
      puVar2[7] = puVar2[7] + 1;
LAB_00abafb8:
      if (*(char *)(puVar3 + 4) != '\0') {
        iVar7 = iVar7 + 0x32;
      }
    }
    iVar9 = iVar9 + 1;
    if (iVar9 == 10) {
      return iVar7;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abaf7c"></a> `00abaf7c` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00abaf80"></a> `00abaf80` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abaf84"></a> `00abaf84` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abaf88"></a> `00abaf88` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abaf8c"></a> `00abaf8c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abaf90"></a> `00abaf90` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abaf94"></a> `00abaf94` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00abaf98"></a> `00abaf98` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00abaf9c"></a> `00abaf9c` | `f7 05 80 52` | mov w23,#0x2f | `FALL_THROUGH`
<a id="insn-00abafa0"></a> `00abafa0` | `0d 00 00 14` | b 0x00abafd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abafa4"></a> `00abafa4` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00abafa8"></a> `00abafa8` | `ff 02 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00abafac"></a> `00abafac` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00abafb0"></a> `00abafb0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abafb4"></a> `00abafb4` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00abafb8"></a> `00abafb8` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00abafbc"></a> `00abafbc` | `69 ca 00 11` | add w9,w19,#0x32 | `FALL_THROUGH`
<a id="insn-00abafc0"></a> `00abafc0` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00abafc4"></a> `00abafc4` | `73 02 89 1a` | csel w19,w19,w9,eq | `FALL_THROUGH`
<a id="insn-00abafc8"></a> `00abafc8` | `d6 06 00 11` | add w22,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00abafcc"></a> `00abafcc` | `df 2a 00 71` | cmp w22,#0xa | `FALL_THROUGH`
<a id="insn-00abafd0"></a> `00abafd0` | `c0 09 00 54` | b.eq 0x00abb108 | `CONDITIONAL_JUMP`
<a id="insn-00abafd4"></a> `00abafd4` | `df 0e 00 71` | cmp w22,#0x3 | `FALL_THROUGH`
<a id="insn-00abafd8"></a> `00abafd8` | `80 ff ff 54` | b.eq 0x00abafc8 | `CONDITIONAL_JUMP`
<a id="insn-00abafdc"></a> `00abafdc` | `47 59 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abafe0"></a> `00abafe0` | `15 e0 4c 91` | add x21,x0,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00abafe4"></a> `00abafe4` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00abafe8"></a> `00abafe8` | `08 8f 4d f8` | ldr x8,[x24, #0xd8]! | `FALL_THROUGH`
<a id="insn-00abafec"></a> `00abafec` | `c8 00 00 b5` | cbnz x8,0x00abb004 | `CONDITIONAL_JUMP`
<a id="insn-00abaff0"></a> `00abaff0` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00abaff4"></a> `00abaff4` | `0d 00 00 14` | b 0x00abb028 | `UNCONDITIONAL_JUMP`
<a id="insn-00abaff8"></a> `00abaff8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abaffc"></a> `00abaffc` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb000"></a> `00abb000` | `48 01 00 b4` | cbz x8,0x00abb028 | `CONDITIONAL_JUMP`
<a id="insn-00abb004"></a> `00abb004` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00abb008"></a> `00abb008` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abb00c"></a> `00abb00c` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00abb010"></a> `00abb010` | `4b ff ff 54` | b.lt 0x00abaff8 | `CONDITIONAL_JUMP`
<a id="insn-00abb014"></a> `00abb014` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00abb018"></a> `00abb018` | `6a 03 00 54` | b.ge 0x00abb084 | `CONDITIONAL_JUMP`
<a id="insn-00abb01c"></a> `00abb01c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00abb020"></a> `00abb020` | `28 ff ff b5` | cbnz x8,0x00abb004 | `CONDITIONAL_JUMP`
<a id="insn-00abb024"></a> `00abb024` | `98 22 00 91` | add x24,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abb028"></a> `00abb028` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00abb02c"></a> `00abb02c` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00abb030"></a> `00abb030` | `98 73 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abb034"></a> `00abb034` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abb038"></a> `00abb038` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abb03c"></a> `00abb03c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abb040"></a> `00abb040` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00abb044"></a> `00abb044` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abb048"></a> `00abb048` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00abb04c"></a> `00abb04c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abb050"></a> `00abb050` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abb054"></a> `00abb054` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00abb058"></a> `00abb058` | `a8 6a 40 f9` | ldr x8,[x21, #0xd0] | `FALL_THROUGH`
<a id="insn-00abb05c"></a> `00abb05c` | `16 20 00 b9` | str w22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abb060"></a> `00abb060` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abb064"></a> `00abb064` | `68 00 00 b4` | cbz x8,0x00abb070 | `CONDITIONAL_JUMP`
<a id="insn-00abb068"></a> `00abb068` | `a8 6a 00 f9` | str x8,[x21, #0xd0] | `FALL_THROUGH`
<a id="insn-00abb06c"></a> `00abb06c` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00abb070"></a> `00abb070` | `a0 6e 40 f9` | ldr x0,[x21, #0xd8] | `FALL_THROUGH`
<a id="insn-00abb074"></a> `00abb074` | `cc 02 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00abb078"></a> `00abb078` | `a8 72 40 f9` | ldr x8,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00abb07c"></a> `00abb07c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abb080"></a> `00abb080` | `a8 72 00 f9` | str x8,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00abb084"></a> `00abb084` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb088"></a> `00abb088` | `08 0f 43 f8` | ldr x8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00abb08c"></a> `00abb08c` | `c8 00 00 b5` | cbnz x8,0x00abb0a4 | `CONDITIONAL_JUMP`
<a id="insn-00abb090"></a> `00abb090` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00abb094"></a> `00abb094` | `0d 00 00 14` | b 0x00abb0c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb098"></a> `00abb098` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abb09c"></a> `00abb09c` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00abb0a0"></a> `00abb0a0` | `48 01 00 b4` | cbz x8,0x00abb0c8 | `CONDITIONAL_JUMP`
<a id="insn-00abb0a4"></a> `00abb0a4` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00abb0a8"></a> `00abb0a8` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abb0ac"></a> `00abb0ac` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00abb0b0"></a> `00abb0b0` | `4a ff ff 54` | b.ge 0x00abb098 | `CONDITIONAL_JUMP`
<a id="insn-00abb0b4"></a> `00abb0b4` | `1f bd 00 71` | cmp w8,#0x2f | `FALL_THROUGH`
<a id="insn-00abb0b8"></a> `00abb0b8` | `00 f8 ff 54` | b.eq 0x00abafb8 | `CONDITIONAL_JUMP`
<a id="insn-00abb0bc"></a> `00abb0bc` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00abb0c0"></a> `00abb0c0` | `28 ff ff b5` | cbnz x8,0x00abb0a4 | `CONDITIONAL_JUMP`
<a id="insn-00abb0c4"></a> `00abb0c4` | `b8 22 00 91` | add x24,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abb0c8"></a> `00abb0c8` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abb0cc"></a> `00abb0cc` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00abb0d0"></a> `00abb0d0` | `70 73 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abb0d4"></a> `00abb0d4` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abb0d8"></a> `00abb0d8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abb0dc"></a> `00abb0dc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abb0e0"></a> `00abb0e0` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abb0e4"></a> `00abb0e4` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00abb0e8"></a> `00abb0e8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00abb0ec"></a> `00abb0ec` | `17 1c 00 b9` | str w23,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abb0f0"></a> `00abb0f0` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abb0f4"></a> `00abb0f4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abb0f8"></a> `00abb0f8` | `68 f5 ff b4` | cbz x8,0x00abafa4 | `CONDITIONAL_JUMP`
<a id="insn-00abb0fc"></a> `00abb0fc` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00abb100"></a> `00abb100` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00abb104"></a> `00abb104` | `a8 ff ff 17` | b 0x00abafa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb108"></a> `00abb108` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00abb10c"></a> `00abb10c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abb110"></a> `00abb110` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abb114"></a> `00abb114` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abb118"></a> `00abb118` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abb11c"></a> `00abb11c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00abb120"></a> `00abb120` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abaf7c`](#insn-00abaf7c) 範囲 `[['00abaf7c', '00abafa3']]`
  - `UNCONDITIONAL_JUMP` [`00abafa0`](#insn-00abafa0) → [`00abafd4`](#insn-00abafd4)
- ブロック [`00abafa4`](#insn-00abafa4) 範囲 `[['00abafa4', '00abafb3']]`
  - `FALL_THROUGH` [`00abafb0`](#insn-00abafb0) → [`00abafb4`](#insn-00abafb4)
- ブロック [`00abafb4`](#insn-00abafb4) 範囲 `[['00abafb4', '00abafb7']]`
  - `FALL_THROUGH` [`00abafb4`](#insn-00abafb4) → [`00abafb8`](#insn-00abafb8)
- ブロック [`00abafb8`](#insn-00abafb8) 範囲 `[['00abafb8', '00abafc7']]`
  - `FALL_THROUGH` [`00abafc4`](#insn-00abafc4) → [`00abafc8`](#insn-00abafc8)
- ブロック [`00abafc8`](#insn-00abafc8) 範囲 `[['00abafc8', '00abafd3']]`
  - `CONDITIONAL_JUMP` [`00abafd0`](#insn-00abafd0) → [`00abb108`](#insn-00abb108)
  - `FALL_THROUGH` [`00abafd0`](#insn-00abafd0) → [`00abafd4`](#insn-00abafd4)
- ブロック [`00abafd4`](#insn-00abafd4) 範囲 `[['00abafd4', '00abafdb']]`
  - `CONDITIONAL_JUMP` [`00abafd8`](#insn-00abafd8) → [`00abafc8`](#insn-00abafc8)
  - `FALL_THROUGH` [`00abafd8`](#insn-00abafd8) → [`00abafdc`](#insn-00abafdc)
- ブロック [`00abafdc`](#insn-00abafdc) 範囲 `[['00abafdc', '00abafdf']]`
  - `FALL_THROUGH` [`00abafdc`](#insn-00abafdc) → [`00abafe0`](#insn-00abafe0)
- ブロック [`00abafe0`](#insn-00abafe0) 範囲 `[['00abafe0', '00abafeb']]`
  - `FALL_THROUGH` [`00abafe8`](#insn-00abafe8) → [`00abafec`](#insn-00abafec)
- ブロック [`00abafec`](#insn-00abafec) 範囲 `[['00abafec', '00abafef']]`
  - `CONDITIONAL_JUMP` [`00abafec`](#insn-00abafec) → [`00abb004`](#insn-00abb004)
  - `FALL_THROUGH` [`00abafec`](#insn-00abafec) → [`00abaff0`](#insn-00abaff0)
- ブロック [`00abaff0`](#insn-00abaff0) 範囲 `[['00abaff0', '00abaff7']]`
  - `UNCONDITIONAL_JUMP` [`00abaff4`](#insn-00abaff4) → [`00abb028`](#insn-00abb028)
- ブロック [`00abaff8`](#insn-00abaff8) 範囲 `[['00abaff8', '00abb003']]`
  - `CONDITIONAL_JUMP` [`00abb000`](#insn-00abb000) → [`00abb028`](#insn-00abb028)
  - `FALL_THROUGH` [`00abb000`](#insn-00abb000) → [`00abb004`](#insn-00abb004)
- ブロック [`00abb004`](#insn-00abb004) 範囲 `[['00abb004', '00abb013']]`
  - `CONDITIONAL_JUMP` [`00abb010`](#insn-00abb010) → [`00abaff8`](#insn-00abaff8)
  - `FALL_THROUGH` [`00abb010`](#insn-00abb010) → [`00abb014`](#insn-00abb014)
- ブロック [`00abb014`](#insn-00abb014) 範囲 `[['00abb014', '00abb01b']]`
  - `CONDITIONAL_JUMP` [`00abb018`](#insn-00abb018) → [`00abb084`](#insn-00abb084)
  - `FALL_THROUGH` [`00abb018`](#insn-00abb018) → [`00abb01c`](#insn-00abb01c)
- ブロック [`00abb01c`](#insn-00abb01c) 範囲 `[['00abb01c', '00abb023']]`
  - `CONDITIONAL_JUMP` [`00abb020`](#insn-00abb020) → [`00abb004`](#insn-00abb004)
  - `FALL_THROUGH` [`00abb020`](#insn-00abb020) → [`00abb024`](#insn-00abb024)
- ブロック [`00abb024`](#insn-00abb024) 範囲 `[['00abb024', '00abb027']]`
  - `FALL_THROUGH` [`00abb024`](#insn-00abb024) → [`00abb028`](#insn-00abb028)
- ブロック [`00abb028`](#insn-00abb028) 範囲 `[['00abb028', '00abb037']]`
  - `FALL_THROUGH` [`00abb034`](#insn-00abb034) → [`00abb038`](#insn-00abb038)
- ブロック [`00abb038`](#insn-00abb038) 範囲 `[['00abb038', '00abb043']]`
  - `FALL_THROUGH` [`00abb040`](#insn-00abb040) → [`00abb044`](#insn-00abb044)
- ブロック [`00abb044`](#insn-00abb044) 範囲 `[['00abb044', '00abb053']]`
  - `FALL_THROUGH` [`00abb050`](#insn-00abb050) → [`00abb054`](#insn-00abb054)
- ブロック [`00abb054`](#insn-00abb054) 範囲 `[['00abb054', '00abb067']]`
  - `CONDITIONAL_JUMP` [`00abb064`](#insn-00abb064) → [`00abb070`](#insn-00abb070)
  - `FALL_THROUGH` [`00abb064`](#insn-00abb064) → [`00abb068`](#insn-00abb068)
- ブロック [`00abb068`](#insn-00abb068) 範囲 `[['00abb068', '00abb06f']]`
  - `FALL_THROUGH` [`00abb06c`](#insn-00abb06c) → [`00abb070`](#insn-00abb070)
- ブロック [`00abb070`](#insn-00abb070) 範囲 `[['00abb070', '00abb083']]`
  - `FALL_THROUGH` [`00abb080`](#insn-00abb080) → [`00abb084`](#insn-00abb084)
- ブロック [`00abb084`](#insn-00abb084) 範囲 `[['00abb084', '00abb08f']]`
  - `CONDITIONAL_JUMP` [`00abb08c`](#insn-00abb08c) → [`00abb0a4`](#insn-00abb0a4)
  - `FALL_THROUGH` [`00abb08c`](#insn-00abb08c) → [`00abb090`](#insn-00abb090)
- ブロック [`00abb090`](#insn-00abb090) 範囲 `[['00abb090', '00abb097']]`
  - `UNCONDITIONAL_JUMP` [`00abb094`](#insn-00abb094) → [`00abb0c8`](#insn-00abb0c8)
- ブロック [`00abb098`](#insn-00abb098) 範囲 `[['00abb098', '00abb0a3']]`
  - `CONDITIONAL_JUMP` [`00abb0a0`](#insn-00abb0a0) → [`00abb0c8`](#insn-00abb0c8)
  - `FALL_THROUGH` [`00abb0a0`](#insn-00abb0a0) → [`00abb0a4`](#insn-00abb0a4)
- ブロック [`00abb0a4`](#insn-00abb0a4) 範囲 `[['00abb0a4', '00abb0b3']]`
  - `CONDITIONAL_JUMP` [`00abb0b0`](#insn-00abb0b0) → [`00abb098`](#insn-00abb098)
  - `FALL_THROUGH` [`00abb0b0`](#insn-00abb0b0) → [`00abb0b4`](#insn-00abb0b4)
- ブロック [`00abb0b4`](#insn-00abb0b4) 範囲 `[['00abb0b4', '00abb0bb']]`
  - `CONDITIONAL_JUMP` [`00abb0b8`](#insn-00abb0b8) → [`00abafb8`](#insn-00abafb8)
  - `FALL_THROUGH` [`00abb0b8`](#insn-00abb0b8) → [`00abb0bc`](#insn-00abb0bc)
- ブロック [`00abb0bc`](#insn-00abb0bc) 範囲 `[['00abb0bc', '00abb0c3']]`
  - `CONDITIONAL_JUMP` [`00abb0c0`](#insn-00abb0c0) → [`00abb0a4`](#insn-00abb0a4)
  - `FALL_THROUGH` [`00abb0c0`](#insn-00abb0c0) → [`00abb0c4`](#insn-00abb0c4)
- ブロック [`00abb0c4`](#insn-00abb0c4) 範囲 `[['00abb0c4', '00abb0c7']]`
  - `FALL_THROUGH` [`00abb0c4`](#insn-00abb0c4) → [`00abb0c8`](#insn-00abb0c8)
- ブロック [`00abb0c8`](#insn-00abb0c8) 範囲 `[['00abb0c8', '00abb0fb']]`
  - `CONDITIONAL_JUMP` [`00abb0f8`](#insn-00abb0f8) → [`00abafa4`](#insn-00abafa4)
  - `FALL_THROUGH` [`00abb0f8`](#insn-00abb0f8) → [`00abb0fc`](#insn-00abb0fc)
- ブロック [`00abb0fc`](#insn-00abb0fc) 範囲 `[['00abb0fc', '00abb107']]`
  - `UNCONDITIONAL_JUMP` [`00abb104`](#insn-00abb104) → [`00abafa4`](#insn-00abafa4)
- ブロック [`00abb108`](#insn-00abb108) 範囲 `[['00abb108', '00abb123']]`

## 命令位置別の参照

- [`00abaf7c`](#insn-00abaf7c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf80`](#insn-00abaf80) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf84`](#insn-00abaf84) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf88`](#insn-00abaf88) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf8c`](#insn-00abaf8c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafa0`](#insn-00abafa0) → [`00abafd4`](#insn-00abafd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafa8`](#insn-00abafa8) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00abafd0`](#insn-00abafd0) → [`00abb108`](#insn-00abb108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafd8`](#insn-00abafd8) → [`00abafc8`](#insn-00abafc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafdc`](#insn-00abafdc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abafe8`](#insn-00abafe8) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abafec`](#insn-00abafec) → [`00abb004`](#insn-00abb004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaff4`](#insn-00abaff4) → [`00abb028`](#insn-00abb028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb000`](#insn-00abb000) → [`00abb028`](#insn-00abb028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb010`](#insn-00abb010) → [`00abaff8`](#insn-00abaff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb018`](#insn-00abb018) → [`00abb084`](#insn-00abb084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb020`](#insn-00abb020) → [`00abb004`](#insn-00abb004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb030`](#insn-00abb030) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abb054`](#insn-00abb054) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb058`](#insn-00abb058) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb064`](#insn-00abb064) → [`00abb070`](#insn-00abb070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb068`](#insn-00abb068) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb06c`](#insn-00abb06c) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb070`](#insn-00abb070) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb074`](#insn-00abb074) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00abb078`](#insn-00abb078) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb080`](#insn-00abb080) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb08c`](#insn-00abb08c) → [`00abb0a4`](#insn-00abb0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb094`](#insn-00abb094) → [`00abb0c8`](#insn-00abb0c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0a0`](#insn-00abb0a0) → [`00abb0c8`](#insn-00abb0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0b0`](#insn-00abb0b0) → [`00abb098`](#insn-00abb098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0b8`](#insn-00abb0b8) → [`00abafb8`](#insn-00abafb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0c0`](#insn-00abb0c0) → [`00abb0a4`](#insn-00abb0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0d0`](#insn-00abb0d0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abb0f8`](#insn-00abb0f8) → [`00abafa4`](#insn-00abafa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb104`](#insn-00abb104) → [`00abafa4`](#insn-00abafa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb10c`](#insn-00abb10c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb110`](#insn-00abb110) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb114`](#insn-00abb114) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb118`](#insn-00abb118) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb11c`](#insn-00abb11c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abaf7c`](#insn-00abaf7c)

~~~json
{
  "source": "00abaf7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf80`](#insn-00abaf80)

~~~json
{
  "source": "00abaf80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf84`](#insn-00abaf84)

~~~json
{
  "source": "00abaf84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf88`](#insn-00abaf88)

~~~json
{
  "source": "00abaf88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf8c`](#insn-00abaf8c)

~~~json
{
  "source": "00abaf8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafa0`](#insn-00abafa0)

~~~json
{
  "source": "00abafa0",
  "target": "00abafd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafa8`](#insn-00abafa8)

~~~json
{
  "source": "00abafa8",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abafd0`](#insn-00abafd0)

~~~json
{
  "source": "00abafd0",
  "target": "00abb108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafd8`](#insn-00abafd8)

~~~json
{
  "source": "00abafd8",
  "target": "00abafc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafdc`](#insn-00abafdc)

~~~json
{
  "source": "00abafdc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abafe8`](#insn-00abafe8)

~~~json
{
  "source": "00abafe8",
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
- 参照命令 [`00abafec`](#insn-00abafec)

~~~json
{
  "source": "00abafec",
  "target": "00abb004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaff4`](#insn-00abaff4)

~~~json
{
  "source": "00abaff4",
  "target": "00abb028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb000`](#insn-00abb000)

~~~json
{
  "source": "00abb000",
  "target": "00abb028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb010`](#insn-00abb010)

~~~json
{
  "source": "00abb010",
  "target": "00abaff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb018`](#insn-00abb018)

~~~json
{
  "source": "00abb018",
  "target": "00abb084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb020`](#insn-00abb020)

~~~json
{
  "source": "00abb020",
  "target": "00abb004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb030`](#insn-00abb030)

~~~json
{
  "source": "00abb030",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb054`](#insn-00abb054)

~~~json
{
  "source": "00abb054",
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
- 参照命令 [`00abb058`](#insn-00abb058)

~~~json
{
  "source": "00abb058",
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
- 参照命令 [`00abb064`](#insn-00abb064)

~~~json
{
  "source": "00abb064",
  "target": "00abb070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb068`](#insn-00abb068)

~~~json
{
  "source": "00abb068",
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
- 参照命令 [`00abb06c`](#insn-00abb06c)

~~~json
{
  "source": "00abb06c",
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
- 参照命令 [`00abb070`](#insn-00abb070)

~~~json
{
  "source": "00abb070",
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
- 参照命令 [`00abb074`](#insn-00abb074)

~~~json
{
  "source": "00abb074",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb078`](#insn-00abb078)

~~~json
{
  "source": "00abb078",
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
- 参照命令 [`00abb080`](#insn-00abb080)

~~~json
{
  "source": "00abb080",
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
- 参照命令 [`00abb08c`](#insn-00abb08c)

~~~json
{
  "source": "00abb08c",
  "target": "00abb0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb094`](#insn-00abb094)

~~~json
{
  "source": "00abb094",
  "target": "00abb0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0a0`](#insn-00abb0a0)

~~~json
{
  "source": "00abb0a0",
  "target": "00abb0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0b0`](#insn-00abb0b0)

~~~json
{
  "source": "00abb0b0",
  "target": "00abb098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0b8`](#insn-00abb0b8)

~~~json
{
  "source": "00abb0b8",
  "target": "00abafb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0c0`](#insn-00abb0c0)

~~~json
{
  "source": "00abb0c0",
  "target": "00abb0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0d0`](#insn-00abb0d0)

~~~json
{
  "source": "00abb0d0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb0f8`](#insn-00abb0f8)

~~~json
{
  "source": "00abb0f8",
  "target": "00abafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb104`](#insn-00abb104)

~~~json
{
  "source": "00abb104",
  "target": "00abafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb10c`](#insn-00abb10c)

~~~json
{
  "source": "00abb10c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb110`](#insn-00abb110)

~~~json
{
  "source": "00abb110",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb114`](#insn-00abb114)

~~~json
{
  "source": "00abb114",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb118`](#insn-00abb118)

~~~json
{
  "source": "00abb118",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb11c`](#insn-00abb11c)

~~~json
{
  "source": "00abb11c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
