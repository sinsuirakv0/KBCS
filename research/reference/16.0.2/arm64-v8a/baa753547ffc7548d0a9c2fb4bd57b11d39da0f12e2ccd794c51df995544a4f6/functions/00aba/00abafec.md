# 00abafec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abaf7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aba/00abaf7c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-562909f98e3f9544068b4e7c6f9d7e62)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00abbfe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00abb/00abbfe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-ab93fb14e88558ead76a93b31c2b9a61)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abafec",
  "name": "FUN_00abafec",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe3ac32cd5f508273222196571c2422b2b6c804ce2e1360b37b3a4f6596d77a8",
  "source_text_sha256": "fe3ac32cd5f508273222196571c2422b2b6c804ce2e1360b37b3a4f6596d77a8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abafec",
        "00abb193"
      ]
    ],
    "bytes_sha256": "a3a847d82dd28cd6ec6caccd3e17950801a0030fdd6fc32459198564ab39dc5a",
    "instruction_count": 106,
    "instruction_bytes": 424,
    "body_bytes": 424,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a84df8](../00a84/00a84df8.md)
- [00a85304](../00a85/00a85304.md)
- [00a8677c](../00a86/00a8677c.md)
- [00a86880](../00a86/00a86880.md)

## 呼び出し先

- [0043bbe4](../0043b/0043bbe4.md)
- [00851550](../00851/00851550.md)
- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3836 bytes

~~~c

int FUN_00abafec(void)

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
                    /* try { // try from 00abb008 to 00bbb017 has its CatchHandler @ 00abcaac */
  iVar9 = 0;
  do {
    if (iVar9 != 3) {
      lVar1 = FUN_00851550();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1);
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar2 = puVar4, puVar8 = puVar2, iVar9 < *(int *)(puVar2 + 4)) {
            puVar4 = (undefined8 *)*puVar2;
            puVar10 = puVar2;
            if ((undefined8 *)*puVar2 == (undefined8 *)0x0) goto LAB_00abb098;
          }
          if (iVar9 <= *(int *)(puVar2 + 4)) goto LAB_00abb0f4;
                    /* try { // try from 00abb08c to 00bbb097 has its CatchHandler @ 00abca54 */
          puVar4 = (undefined8 *)puVar2[1];
        } while ((undefined8 *)puVar2[1] != (undefined8 *)0x0);
        puVar10 = puVar2 + 1;
      }
LAB_00abb098:
                    /* try { // try from 00abb098 to 00bbb0a7 has its CatchHandler @ 00abca34 */
      puVar2 = (undefined8 *)_Znwm(0x40);
                    /* try { // try from 00abb0a8 to 00bbb0c3 has its CatchHandler @ 00abc9e8 */
      puVar2[7] = 0;
      puVar2[6] = 0;
      puVar2[5] = puVar2 + 6;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar8;
                    /* try { // try from 00abb0c4 to 00bbb18f has its CatchHandler @ 00abad54 */
      *puVar10 = puVar2;
      plVar5 = *(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar1);
      *(int *)(puVar2 + 4) = iVar9;
      lVar6 = *plVar5;
      puVar4 = puVar2;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar1) = lVar6;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bbe4(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1),puVar4);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) + 1;
LAB_00abb0f4:
      puVar8 = puVar2 + 6;
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar4, puVar8 = puVar3, 0x2f < *(int *)((long)puVar3 + 0x1c)) {
            puVar4 = (undefined8 *)*puVar3;
            puVar10 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abb138;
          }
          if (*(int *)((long)puVar3 + 0x1c) == 0x2f) goto LAB_00abb028;
          puVar4 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar10 = puVar3 + 1;
      }
LAB_00abb138:
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
      FUN_0043bbe4(puVar2[6],puVar4);
      puVar2[7] = puVar2[7] + 1;
LAB_00abb028:
                    /* try { // try from 00abb034 to 00bbb03f has its CatchHandler @ 00abcaa8 */
      if (*(char *)(puVar3 + 4) != '\0') {
        iVar7 = iVar7 + 0x32;
      }
    }
    iVar9 = iVar9 + 1;
                    /* try { // try from 00abb040 to 00bbb053 has its CatchHandler @ 00abca94 */
    if (iVar9 == 10) {
                    /* try { // try from 00abb190 to 00bbb197 has its CatchHandler @ 00abcd44 */
      return iVar7;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abafec"></a> `00abafec` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00abaff0"></a> `00abaff0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abaff4"></a> `00abaff4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abaff8"></a> `00abaff8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abaffc"></a> `00abaffc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abb000"></a> `00abb000` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abb004"></a> `00abb004` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00abb008"></a> `00abb008` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00abb00c"></a> `00abb00c` | `f7 05 80 52` | mov w23,#0x2f | `FALL_THROUGH`
<a id="insn-00abb010"></a> `00abb010` | `0d 00 00 14` | b 0x00abb044 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb014"></a> `00abb014` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00abb018"></a> `00abb018` | `f3 02 e6 97` | bl 0x0043bbe4 | `UNCONDITIONAL_CALL`
<a id="insn-00abb01c"></a> `00abb01c` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00abb020"></a> `00abb020` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abb024"></a> `00abb024` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00abb028"></a> `00abb028` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00abb02c"></a> `00abb02c` | `69 ca 00 11` | add w9,w19,#0x32 | `FALL_THROUGH`
<a id="insn-00abb030"></a> `00abb030` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00abb034"></a> `00abb034` | `73 02 89 1a` | csel w19,w19,w9,eq | `FALL_THROUGH`
<a id="insn-00abb038"></a> `00abb038` | `d6 06 00 11` | add w22,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00abb03c"></a> `00abb03c` | `df 2a 00 71` | cmp w22,#0xa | `FALL_THROUGH`
<a id="insn-00abb040"></a> `00abb040` | `c0 09 00 54` | b.eq 0x00abb178 | `CONDITIONAL_JUMP`
<a id="insn-00abb044"></a> `00abb044` | `df 0e 00 71` | cmp w22,#0x3 | `FALL_THROUGH`
<a id="insn-00abb048"></a> `00abb048` | `80 ff ff 54` | b.eq 0x00abb038 | `CONDITIONAL_JUMP`
<a id="insn-00abb04c"></a> `00abb04c` | `41 59 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00abb050"></a> `00abb050` | `15 e0 4c 91` | add x21,x0,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00abb054"></a> `00abb054` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00abb058"></a> `00abb058` | `08 8f 4d f8` | ldr x8,[x24, #0xd8]! | `FALL_THROUGH`
<a id="insn-00abb05c"></a> `00abb05c` | `c8 00 00 b5` | cbnz x8,0x00abb074 | `CONDITIONAL_JUMP`
<a id="insn-00abb060"></a> `00abb060` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00abb064"></a> `00abb064` | `0d 00 00 14` | b 0x00abb098 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb068"></a> `00abb068` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abb06c"></a> `00abb06c` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb070"></a> `00abb070` | `48 01 00 b4` | cbz x8,0x00abb098 | `CONDITIONAL_JUMP`
<a id="insn-00abb074"></a> `00abb074` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00abb078"></a> `00abb078` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abb07c"></a> `00abb07c` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00abb080"></a> `00abb080` | `4b ff ff 54` | b.lt 0x00abb068 | `CONDITIONAL_JUMP`
<a id="insn-00abb084"></a> `00abb084` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00abb088"></a> `00abb088` | `6a 03 00 54` | b.ge 0x00abb0f4 | `CONDITIONAL_JUMP`
<a id="insn-00abb08c"></a> `00abb08c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00abb090"></a> `00abb090` | `28 ff ff b5` | cbnz x8,0x00abb074 | `CONDITIONAL_JUMP`
<a id="insn-00abb094"></a> `00abb094` | `98 22 00 91` | add x24,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abb098"></a> `00abb098` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00abb09c"></a> `00abb09c` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00abb0a0"></a> `00abb0a0` | `b0 73 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb0a4"></a> `00abb0a4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abb0a8"></a> `00abb0a8` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abb0ac"></a> `00abb0ac` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abb0b0"></a> `00abb0b0` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00abb0b4"></a> `00abb0b4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abb0b8"></a> `00abb0b8` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00abb0bc"></a> `00abb0bc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abb0c0"></a> `00abb0c0` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abb0c4"></a> `00abb0c4` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00abb0c8"></a> `00abb0c8` | `a8 6a 40 f9` | ldr x8,[x21, #0xd0] | `FALL_THROUGH`
<a id="insn-00abb0cc"></a> `00abb0cc` | `16 20 00 b9` | str w22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abb0d0"></a> `00abb0d0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abb0d4"></a> `00abb0d4` | `68 00 00 b4` | cbz x8,0x00abb0e0 | `CONDITIONAL_JUMP`
<a id="insn-00abb0d8"></a> `00abb0d8` | `a8 6a 00 f9` | str x8,[x21, #0xd0] | `FALL_THROUGH`
<a id="insn-00abb0dc"></a> `00abb0dc` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00abb0e0"></a> `00abb0e0` | `a0 6e 40 f9` | ldr x0,[x21, #0xd8] | `FALL_THROUGH`
<a id="insn-00abb0e4"></a> `00abb0e4` | `c0 02 e6 97` | bl 0x0043bbe4 | `UNCONDITIONAL_CALL`
<a id="insn-00abb0e8"></a> `00abb0e8` | `a8 72 40 f9` | ldr x8,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00abb0ec"></a> `00abb0ec` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abb0f0"></a> `00abb0f0` | `a8 72 00 f9` | str x8,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00abb0f4"></a> `00abb0f4` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb0f8"></a> `00abb0f8` | `08 0f 43 f8` | ldr x8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00abb0fc"></a> `00abb0fc` | `c8 00 00 b5` | cbnz x8,0x00abb114 | `CONDITIONAL_JUMP`
<a id="insn-00abb100"></a> `00abb100` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00abb104"></a> `00abb104` | `0d 00 00 14` | b 0x00abb138 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb108"></a> `00abb108` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abb10c"></a> `00abb10c` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00abb110"></a> `00abb110` | `48 01 00 b4` | cbz x8,0x00abb138 | `CONDITIONAL_JUMP`
<a id="insn-00abb114"></a> `00abb114` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00abb118"></a> `00abb118` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abb11c"></a> `00abb11c` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00abb120"></a> `00abb120` | `4a ff ff 54` | b.ge 0x00abb108 | `CONDITIONAL_JUMP`
<a id="insn-00abb124"></a> `00abb124` | `1f bd 00 71` | cmp w8,#0x2f | `FALL_THROUGH`
<a id="insn-00abb128"></a> `00abb128` | `00 f8 ff 54` | b.eq 0x00abb028 | `CONDITIONAL_JUMP`
<a id="insn-00abb12c"></a> `00abb12c` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00abb130"></a> `00abb130` | `28 ff ff b5` | cbnz x8,0x00abb114 | `CONDITIONAL_JUMP`
<a id="insn-00abb134"></a> `00abb134` | `b8 22 00 91` | add x24,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abb138"></a> `00abb138` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abb13c"></a> `00abb13c` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00abb140"></a> `00abb140` | `88 73 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb144"></a> `00abb144` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abb148"></a> `00abb148` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abb14c"></a> `00abb14c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abb150"></a> `00abb150` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abb154"></a> `00abb154` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00abb158"></a> `00abb158` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00abb15c"></a> `00abb15c` | `17 1c 00 b9` | str w23,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abb160"></a> `00abb160` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abb164"></a> `00abb164` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abb168"></a> `00abb168` | `68 f5 ff b4` | cbz x8,0x00abb014 | `CONDITIONAL_JUMP`
<a id="insn-00abb16c"></a> `00abb16c` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00abb170"></a> `00abb170` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00abb174"></a> `00abb174` | `a8 ff ff 17` | b 0x00abb014 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb178"></a> `00abb178` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00abb17c"></a> `00abb17c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abb180"></a> `00abb180` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abb184"></a> `00abb184` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abb188"></a> `00abb188` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abb18c"></a> `00abb18c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00abb190"></a> `00abb190` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abafec`](#insn-00abafec) 範囲 `[['00abafec', '00abb007']]`
  - `FALL_THROUGH` [`00abb004`](#insn-00abb004) → [`00abb008`](#insn-00abb008)
- ブロック [`00abb008`](#insn-00abb008) 範囲 `[['00abb008', '00abb013']]`
  - `UNCONDITIONAL_JUMP` [`00abb010`](#insn-00abb010) → [`00abb044`](#insn-00abb044)
- ブロック [`00abb014`](#insn-00abb014) 範囲 `[['00abb014', '00abb027']]`
  - `FALL_THROUGH` [`00abb024`](#insn-00abb024) → [`00abb028`](#insn-00abb028)
- ブロック [`00abb028`](#insn-00abb028) 範囲 `[['00abb028', '00abb033']]`
  - `FALL_THROUGH` [`00abb030`](#insn-00abb030) → [`00abb034`](#insn-00abb034)
- ブロック [`00abb034`](#insn-00abb034) 範囲 `[['00abb034', '00abb037']]`
  - `FALL_THROUGH` [`00abb034`](#insn-00abb034) → [`00abb038`](#insn-00abb038)
- ブロック [`00abb038`](#insn-00abb038) 範囲 `[['00abb038', '00abb03f']]`
  - `FALL_THROUGH` [`00abb03c`](#insn-00abb03c) → [`00abb040`](#insn-00abb040)
- ブロック [`00abb040`](#insn-00abb040) 範囲 `[['00abb040', '00abb043']]`
  - `CONDITIONAL_JUMP` [`00abb040`](#insn-00abb040) → [`00abb178`](#insn-00abb178)
  - `FALL_THROUGH` [`00abb040`](#insn-00abb040) → [`00abb044`](#insn-00abb044)
- ブロック [`00abb044`](#insn-00abb044) 範囲 `[['00abb044', '00abb04b']]`
  - `CONDITIONAL_JUMP` [`00abb048`](#insn-00abb048) → [`00abb038`](#insn-00abb038)
  - `FALL_THROUGH` [`00abb048`](#insn-00abb048) → [`00abb04c`](#insn-00abb04c)
- ブロック [`00abb04c`](#insn-00abb04c) 範囲 `[['00abb04c', '00abb05f']]`
  - `CONDITIONAL_JUMP` [`00abb05c`](#insn-00abb05c) → [`00abb074`](#insn-00abb074)
  - `FALL_THROUGH` [`00abb05c`](#insn-00abb05c) → [`00abb060`](#insn-00abb060)
- ブロック [`00abb060`](#insn-00abb060) 範囲 `[['00abb060', '00abb067']]`
  - `UNCONDITIONAL_JUMP` [`00abb064`](#insn-00abb064) → [`00abb098`](#insn-00abb098)
- ブロック [`00abb068`](#insn-00abb068) 範囲 `[['00abb068', '00abb073']]`
  - `CONDITIONAL_JUMP` [`00abb070`](#insn-00abb070) → [`00abb098`](#insn-00abb098)
  - `FALL_THROUGH` [`00abb070`](#insn-00abb070) → [`00abb074`](#insn-00abb074)
- ブロック [`00abb074`](#insn-00abb074) 範囲 `[['00abb074', '00abb083']]`
  - `CONDITIONAL_JUMP` [`00abb080`](#insn-00abb080) → [`00abb068`](#insn-00abb068)
  - `FALL_THROUGH` [`00abb080`](#insn-00abb080) → [`00abb084`](#insn-00abb084)
- ブロック [`00abb084`](#insn-00abb084) 範囲 `[['00abb084', '00abb08b']]`
  - `CONDITIONAL_JUMP` [`00abb088`](#insn-00abb088) → [`00abb0f4`](#insn-00abb0f4)
  - `FALL_THROUGH` [`00abb088`](#insn-00abb088) → [`00abb08c`](#insn-00abb08c)
- ブロック [`00abb08c`](#insn-00abb08c) 範囲 `[['00abb08c', '00abb093']]`
  - `CONDITIONAL_JUMP` [`00abb090`](#insn-00abb090) → [`00abb074`](#insn-00abb074)
  - `FALL_THROUGH` [`00abb090`](#insn-00abb090) → [`00abb094`](#insn-00abb094)
- ブロック [`00abb094`](#insn-00abb094) 範囲 `[['00abb094', '00abb097']]`
  - `FALL_THROUGH` [`00abb094`](#insn-00abb094) → [`00abb098`](#insn-00abb098)
- ブロック [`00abb098`](#insn-00abb098) 範囲 `[['00abb098', '00abb0a7']]`
  - `FALL_THROUGH` [`00abb0a4`](#insn-00abb0a4) → [`00abb0a8`](#insn-00abb0a8)
- ブロック [`00abb0a8`](#insn-00abb0a8) 範囲 `[['00abb0a8', '00abb0c3']]`
  - `FALL_THROUGH` [`00abb0c0`](#insn-00abb0c0) → [`00abb0c4`](#insn-00abb0c4)
- ブロック [`00abb0c4`](#insn-00abb0c4) 範囲 `[['00abb0c4', '00abb0d7']]`
  - `CONDITIONAL_JUMP` [`00abb0d4`](#insn-00abb0d4) → [`00abb0e0`](#insn-00abb0e0)
  - `FALL_THROUGH` [`00abb0d4`](#insn-00abb0d4) → [`00abb0d8`](#insn-00abb0d8)
- ブロック [`00abb0d8`](#insn-00abb0d8) 範囲 `[['00abb0d8', '00abb0df']]`
  - `FALL_THROUGH` [`00abb0dc`](#insn-00abb0dc) → [`00abb0e0`](#insn-00abb0e0)
- ブロック [`00abb0e0`](#insn-00abb0e0) 範囲 `[['00abb0e0', '00abb0f3']]`
  - `FALL_THROUGH` [`00abb0f0`](#insn-00abb0f0) → [`00abb0f4`](#insn-00abb0f4)
- ブロック [`00abb0f4`](#insn-00abb0f4) 範囲 `[['00abb0f4', '00abb0ff']]`
  - `CONDITIONAL_JUMP` [`00abb0fc`](#insn-00abb0fc) → [`00abb114`](#insn-00abb114)
  - `FALL_THROUGH` [`00abb0fc`](#insn-00abb0fc) → [`00abb100`](#insn-00abb100)
- ブロック [`00abb100`](#insn-00abb100) 範囲 `[['00abb100', '00abb107']]`
  - `UNCONDITIONAL_JUMP` [`00abb104`](#insn-00abb104) → [`00abb138`](#insn-00abb138)
- ブロック [`00abb108`](#insn-00abb108) 範囲 `[['00abb108', '00abb113']]`
  - `CONDITIONAL_JUMP` [`00abb110`](#insn-00abb110) → [`00abb138`](#insn-00abb138)
  - `FALL_THROUGH` [`00abb110`](#insn-00abb110) → [`00abb114`](#insn-00abb114)
- ブロック [`00abb114`](#insn-00abb114) 範囲 `[['00abb114', '00abb123']]`
  - `CONDITIONAL_JUMP` [`00abb120`](#insn-00abb120) → [`00abb108`](#insn-00abb108)
  - `FALL_THROUGH` [`00abb120`](#insn-00abb120) → [`00abb124`](#insn-00abb124)
- ブロック [`00abb124`](#insn-00abb124) 範囲 `[['00abb124', '00abb12b']]`
  - `CONDITIONAL_JUMP` [`00abb128`](#insn-00abb128) → [`00abb028`](#insn-00abb028)
  - `FALL_THROUGH` [`00abb128`](#insn-00abb128) → [`00abb12c`](#insn-00abb12c)
- ブロック [`00abb12c`](#insn-00abb12c) 範囲 `[['00abb12c', '00abb133']]`
  - `CONDITIONAL_JUMP` [`00abb130`](#insn-00abb130) → [`00abb114`](#insn-00abb114)
  - `FALL_THROUGH` [`00abb130`](#insn-00abb130) → [`00abb134`](#insn-00abb134)
- ブロック [`00abb134`](#insn-00abb134) 範囲 `[['00abb134', '00abb137']]`
  - `FALL_THROUGH` [`00abb134`](#insn-00abb134) → [`00abb138`](#insn-00abb138)
- ブロック [`00abb138`](#insn-00abb138) 範囲 `[['00abb138', '00abb16b']]`
  - `CONDITIONAL_JUMP` [`00abb168`](#insn-00abb168) → [`00abb014`](#insn-00abb014)
  - `FALL_THROUGH` [`00abb168`](#insn-00abb168) → [`00abb16c`](#insn-00abb16c)
- ブロック [`00abb16c`](#insn-00abb16c) 範囲 `[['00abb16c', '00abb177']]`
  - `UNCONDITIONAL_JUMP` [`00abb174`](#insn-00abb174) → [`00abb014`](#insn-00abb014)
- ブロック [`00abb178`](#insn-00abb178) 範囲 `[['00abb178', '00abb18f']]`
  - `FALL_THROUGH` [`00abb18c`](#insn-00abb18c) → [`00abb190`](#insn-00abb190)
- ブロック [`00abb190`](#insn-00abb190) 範囲 `[['00abb190', '00abb193']]`

## 命令位置別の参照

- [`00abafec`](#insn-00abafec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaff0`](#insn-00abaff0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaff4`](#insn-00abaff4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaff8`](#insn-00abaff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaffc`](#insn-00abaffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb010`](#insn-00abb010) → [`00abb044`](#insn-00abb044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb018`](#insn-00abb018) → [`0043bbe4`](../0043b/0043bbe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bbe4` · 推定シンボル `None` · 推定型 `None`
- [`00abb040`](#insn-00abb040) → [`00abb178`](#insn-00abb178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb048`](#insn-00abb048) → [`00abb038`](#insn-00abb038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb04c`](#insn-00abb04c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00abb058`](#insn-00abb058) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb05c`](#insn-00abb05c) → [`00abb074`](#insn-00abb074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb064`](#insn-00abb064) → [`00abb098`](#insn-00abb098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb070`](#insn-00abb070) → [`00abb098`](#insn-00abb098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb080`](#insn-00abb080) → [`00abb068`](#insn-00abb068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb088`](#insn-00abb088) → [`00abb0f4`](#insn-00abb0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb090`](#insn-00abb090) → [`00abb074`](#insn-00abb074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0a0`](#insn-00abb0a0) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00abb0c4`](#insn-00abb0c4) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb0c8`](#insn-00abb0c8) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb0d4`](#insn-00abb0d4) → [`00abb0e0`](#insn-00abb0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0d8`](#insn-00abb0d8) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb0dc`](#insn-00abb0dc) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb0e0`](#insn-00abb0e0) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb0e4`](#insn-00abb0e4) → [`0043bbe4`](../0043b/0043bbe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bbe4` · 推定シンボル `None` · 推定型 `None`
- [`00abb0e8`](#insn-00abb0e8) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb0f0`](#insn-00abb0f0) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abb0fc`](#insn-00abb0fc) → [`00abb114`](#insn-00abb114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb104`](#insn-00abb104) → [`00abb138`](#insn-00abb138) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb110`](#insn-00abb110) → [`00abb138`](#insn-00abb138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb120`](#insn-00abb120) → [`00abb108`](#insn-00abb108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb128`](#insn-00abb128) → [`00abb028`](#insn-00abb028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb130`](#insn-00abb130) → [`00abb114`](#insn-00abb114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb140`](#insn-00abb140) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00abb168`](#insn-00abb168) → [`00abb014`](#insn-00abb014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb174`](#insn-00abb174) → [`00abb014`](#insn-00abb014) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb17c`](#insn-00abb17c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb180`](#insn-00abb180) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb184`](#insn-00abb184) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb188`](#insn-00abb188) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb18c`](#insn-00abb18c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abafec`](#insn-00abafec)

~~~json
{
  "source": "00abafec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaff0`](#insn-00abaff0)

~~~json
{
  "source": "00abaff0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaff4`](#insn-00abaff4)

~~~json
{
  "source": "00abaff4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaff8`](#insn-00abaff8)

~~~json
{
  "source": "00abaff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaffc`](#insn-00abaffc)

~~~json
{
  "source": "00abaffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb010`](#insn-00abb010)

~~~json
{
  "source": "00abb010",
  "target": "00abb044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb018`](#insn-00abb018)

~~~json
{
  "source": "00abb018",
  "target": "0043bbe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb040`](#insn-00abb040)

~~~json
{
  "source": "00abb040",
  "target": "00abb178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb048`](#insn-00abb048)

~~~json
{
  "source": "00abb048",
  "target": "00abb038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb04c`](#insn-00abb04c)

~~~json
{
  "source": "00abb04c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb058`](#insn-00abb058)

~~~json
{
  "source": "00abb058",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18bf7d008c6f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb05c`](#insn-00abb05c)

~~~json
{
  "source": "00abb05c",
  "target": "00abb074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb064`](#insn-00abb064)

~~~json
{
  "source": "00abb064",
  "target": "00abb098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb070`](#insn-00abb070)

~~~json
{
  "source": "00abb070",
  "target": "00abb098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb080`](#insn-00abb080)

~~~json
{
  "source": "00abb080",
  "target": "00abb068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb088`](#insn-00abb088)

~~~json
{
  "source": "00abb088",
  "target": "00abb0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb090`](#insn-00abb090)

~~~json
{
  "source": "00abb090",
  "target": "00abb074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0a0`](#insn-00abb0a0)

~~~json
{
  "source": "00abb0a0",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb0c4`](#insn-00abb0c4)

~~~json
{
  "source": "00abb0c4",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18bf7d008c6f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0c8`](#insn-00abb0c8)

~~~json
{
  "source": "00abb0c8",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "14bf7d00786f0a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0d4`](#insn-00abb0d4)

~~~json
{
  "source": "00abb0d4",
  "target": "00abb0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0d8`](#insn-00abb0d8)

~~~json
{
  "source": "00abb0d8",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "14bf7d00786f0a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0dc`](#insn-00abb0dc)

~~~json
{
  "source": "00abb0dc",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18bf7d008c6f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0e0`](#insn-00abb0e0)

~~~json
{
  "source": "00abb0e0",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18bf7d008c6f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0e4`](#insn-00abb0e4)

~~~json
{
  "source": "00abb0e4",
  "target": "0043bbe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb0e8`](#insn-00abb0e8)

~~~json
{
  "source": "00abb0e8",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ccbf7d00d86f0a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0f0`](#insn-00abb0f0)

~~~json
{
  "source": "00abb0f0",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ccbf7d00d86f0a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0fc`](#insn-00abb0fc)

~~~json
{
  "source": "00abb0fc",
  "target": "00abb114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb104`](#insn-00abb104)

~~~json
{
  "source": "00abb104",
  "target": "00abb138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb110`](#insn-00abb110)

~~~json
{
  "source": "00abb110",
  "target": "00abb138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb120`](#insn-00abb120)

~~~json
{
  "source": "00abb120",
  "target": "00abb108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb128`](#insn-00abb128)

~~~json
{
  "source": "00abb128",
  "target": "00abb028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb130`](#insn-00abb130)

~~~json
{
  "source": "00abb130",
  "target": "00abb114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb140`](#insn-00abb140)

~~~json
{
  "source": "00abb140",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb168`](#insn-00abb168)

~~~json
{
  "source": "00abb168",
  "target": "00abb014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb174`](#insn-00abb174)

~~~json
{
  "source": "00abb174",
  "target": "00abb014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb17c`](#insn-00abb17c)

~~~json
{
  "source": "00abb17c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb180`](#insn-00abb180)

~~~json
{
  "source": "00abb180",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb184`](#insn-00abb184)

~~~json
{
  "source": "00abb184",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb188`](#insn-00abb188)

~~~json
{
  "source": "00abb188",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb18c`](#insn-00abb18c)

~~~json
{
  "source": "00abb18c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
