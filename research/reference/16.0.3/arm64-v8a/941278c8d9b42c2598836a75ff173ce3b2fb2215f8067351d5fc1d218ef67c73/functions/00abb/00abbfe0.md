# 00abbfe0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abafec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aba/00abafec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-ab93fb14e88558ead76a93b31c2b9a61)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abbfe0",
  "name": "FUN_00abbfe0",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1cda622f2e57fc18f1c2301670f4bccaa4e3e8604fcc2e9586e58400f3c01fc3",
  "source_text_sha256": "1cda622f2e57fc18f1c2301670f4bccaa4e3e8604fcc2e9586e58400f3c01fc3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abbfe0",
        "00abc187"
      ]
    ],
    "bytes_sha256": "6344f82598a9eb510631baf404097f87511f7ea2412f7c11f7ea414f06fbcb78",
    "instruction_count": 106,
    "instruction_bytes": 424,
    "body_bytes": 424,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a85dec](../00a85/00a85dec.md)
- [00a862f8](../00a86/00a862f8.md)
- [00a87770](../00a87/00a87770.md)
- [00a87874](../00a87/00a87874.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [008524fc](../00852/008524fc.md)
- [00c58f30](../00c58/00c58f30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3836 bytes

~~~c

int FUN_00abbfe0(void)

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
  
                    /* try { // try from 00abbfe0 to 00bbbfeb has its CatchHandler @ 00abda54 */
                    /* try { // try from 00abbfec to 00bbbfff has its CatchHandler @ 00abda40 */
  iVar7 = 0;
  iVar9 = 0;
  do {
                    /* try { // try from 00abc038 to 00bbc043 has its CatchHandler @ 00abda00 */
    if (iVar9 != 3) {
      lVar1 = FUN_008524fc();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1);
                    /* try { // try from 00abc044 to 00bbc053 has its CatchHandler @ 00abd9e0 */
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
                    /* try { // try from 00abc070 to 00bbc13b has its CatchHandler @ 00abbd00 */
          while (puVar2 = puVar4, puVar8 = puVar2, iVar9 < *(int *)(puVar2 + 4)) {
            puVar4 = (undefined8 *)*puVar2;
            puVar10 = puVar2;
            if ((undefined8 *)*puVar2 == (undefined8 *)0x0) goto LAB_00abc08c;
          }
          if (iVar9 <= *(int *)(puVar2 + 4)) goto LAB_00abc0e8;
          puVar4 = (undefined8 *)puVar2[1];
        } while ((undefined8 *)puVar2[1] != (undefined8 *)0x0);
        puVar10 = puVar2 + 1;
      }
LAB_00abc08c:
      puVar2 = (undefined8 *)_Znwm(0x40);
      puVar2[7] = 0;
      puVar2[6] = 0;
      puVar2[5] = puVar2 + 6;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar8;
      *puVar10 = puVar2;
      plVar5 = *(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar1);
      *(int *)(puVar2 + 4) = iVar9;
      lVar6 = *plVar5;
      puVar4 = puVar2;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar1) = lVar6;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bf04(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1),puVar4);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) + 1;
LAB_00abc0e8:
      puVar8 = puVar2 + 6;
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar4, puVar8 = puVar3, 0x2f < *(int *)((long)puVar3 + 0x1c)) {
            puVar4 = (undefined8 *)*puVar3;
            puVar10 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abc12c;
          }
          if (*(int *)((long)puVar3 + 0x1c) == 0x2f) goto LAB_00abc01c;
          puVar4 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar10 = puVar3 + 1;
      }
LAB_00abc12c:
      puVar3 = (undefined8 *)_Znwm(0x28);
      *puVar3 = 0;
      puVar3[1] = 0;
                    /* try { // try from 00abc13c to 00bbc143 has its CatchHandler @ 00abdcf0 */
      puVar3[2] = puVar8;
      *puVar10 = puVar3;
      plVar5 = (long *)puVar2[5];
      *(undefined4 *)((long)puVar3 + 0x1c) = 0x2f;
      *(undefined1 *)(puVar3 + 4) = 0;
      puVar4 = puVar3;
      if (*plVar5 != 0) {
                    /* try { // try from 00abc160 to 00bbc16b has its CatchHandler @ 00abdcd4 */
        puVar2[5] = *plVar5;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bf04(puVar2[6],puVar4);
      puVar2[7] = puVar2[7] + 1;
LAB_00abc01c:
      if (*(char *)(puVar3 + 4) != '\0') {
        iVar7 = iVar7 + 0x32;
      }
    }
    iVar9 = iVar9 + 1;
    if (iVar9 == 10) {
                    /* try { // try from 00abc16c to 00bbc17f has its CatchHandler @ 00abdc9c */
      return iVar7;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abbfe0"></a> `00abbfe0` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00abbfe4"></a> `00abbfe4` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abbfe8"></a> `00abbfe8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abbfec"></a> `00abbfec` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abbff0"></a> `00abbff0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abbff4"></a> `00abbff4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abbff8"></a> `00abbff8` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00abbffc"></a> `00abbffc` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00abc000"></a> `00abc000` | `f7 05 80 52` | mov w23,#0x2f | `FALL_THROUGH`
<a id="insn-00abc004"></a> `00abc004` | `0d 00 00 14` | b 0x00abc038 | `UNCONDITIONAL_JUMP`
<a id="insn-00abc008"></a> `00abc008` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00abc00c"></a> `00abc00c` | `be ff e5 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00abc010"></a> `00abc010` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00abc014"></a> `00abc014` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc018"></a> `00abc018` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00abc01c"></a> `00abc01c` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00abc020"></a> `00abc020` | `69 ca 00 11` | add w9,w19,#0x32 | `FALL_THROUGH`
<a id="insn-00abc024"></a> `00abc024` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00abc028"></a> `00abc028` | `73 02 89 1a` | csel w19,w19,w9,eq | `FALL_THROUGH`
<a id="insn-00abc02c"></a> `00abc02c` | `d6 06 00 11` | add w22,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00abc030"></a> `00abc030` | `df 2a 00 71` | cmp w22,#0xa | `FALL_THROUGH`
<a id="insn-00abc034"></a> `00abc034` | `c0 09 00 54` | b.eq 0x00abc16c | `CONDITIONAL_JUMP`
<a id="insn-00abc038"></a> `00abc038` | `df 0e 00 71` | cmp w22,#0x3 | `FALL_THROUGH`
<a id="insn-00abc03c"></a> `00abc03c` | `80 ff ff 54` | b.eq 0x00abc02c | `CONDITIONAL_JUMP`
<a id="insn-00abc040"></a> `00abc040` | `2f 59 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abc044"></a> `00abc044` | `15 e0 4c 91` | add x21,x0,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00abc048"></a> `00abc048` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00abc04c"></a> `00abc04c` | `08 8f 4d f8` | ldr x8,[x24, #0xd8]! | `FALL_THROUGH`
<a id="insn-00abc050"></a> `00abc050` | `c8 00 00 b5` | cbnz x8,0x00abc068 | `CONDITIONAL_JUMP`
<a id="insn-00abc054"></a> `00abc054` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00abc058"></a> `00abc058` | `0d 00 00 14` | b 0x00abc08c | `UNCONDITIONAL_JUMP`
<a id="insn-00abc05c"></a> `00abc05c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abc060"></a> `00abc060` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abc064"></a> `00abc064` | `48 01 00 b4` | cbz x8,0x00abc08c | `CONDITIONAL_JUMP`
<a id="insn-00abc068"></a> `00abc068` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00abc06c"></a> `00abc06c` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abc070"></a> `00abc070` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00abc074"></a> `00abc074` | `4b ff ff 54` | b.lt 0x00abc05c | `CONDITIONAL_JUMP`
<a id="insn-00abc078"></a> `00abc078` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00abc07c"></a> `00abc07c` | `6a 03 00 54` | b.ge 0x00abc0e8 | `CONDITIONAL_JUMP`
<a id="insn-00abc080"></a> `00abc080` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00abc084"></a> `00abc084` | `28 ff ff b5` | cbnz x8,0x00abc068 | `CONDITIONAL_JUMP`
<a id="insn-00abc088"></a> `00abc088` | `98 22 00 91` | add x24,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abc08c"></a> `00abc08c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00abc090"></a> `00abc090` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00abc094"></a> `00abc094` | `a7 73 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00abc098"></a> `00abc098` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abc09c"></a> `00abc09c` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abc0a0"></a> `00abc0a0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abc0a4"></a> `00abc0a4` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00abc0a8"></a> `00abc0a8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abc0ac"></a> `00abc0ac` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00abc0b0"></a> `00abc0b0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abc0b4"></a> `00abc0b4` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abc0b8"></a> `00abc0b8` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00abc0bc"></a> `00abc0bc` | `a8 6a 40 f9` | ldr x8,[x21, #0xd0] | `FALL_THROUGH`
<a id="insn-00abc0c0"></a> `00abc0c0` | `16 20 00 b9` | str w22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abc0c4"></a> `00abc0c4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abc0c8"></a> `00abc0c8` | `68 00 00 b4` | cbz x8,0x00abc0d4 | `CONDITIONAL_JUMP`
<a id="insn-00abc0cc"></a> `00abc0cc` | `a8 6a 00 f9` | str x8,[x21, #0xd0] | `FALL_THROUGH`
<a id="insn-00abc0d0"></a> `00abc0d0` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00abc0d4"></a> `00abc0d4` | `a0 6e 40 f9` | ldr x0,[x21, #0xd8] | `FALL_THROUGH`
<a id="insn-00abc0d8"></a> `00abc0d8` | `8b ff e5 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00abc0dc"></a> `00abc0dc` | `a8 72 40 f9` | ldr x8,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00abc0e0"></a> `00abc0e0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc0e4"></a> `00abc0e4` | `a8 72 00 f9` | str x8,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00abc0e8"></a> `00abc0e8` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abc0ec"></a> `00abc0ec` | `08 0f 43 f8` | ldr x8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00abc0f0"></a> `00abc0f0` | `c8 00 00 b5` | cbnz x8,0x00abc108 | `CONDITIONAL_JUMP`
<a id="insn-00abc0f4"></a> `00abc0f4` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00abc0f8"></a> `00abc0f8` | `0d 00 00 14` | b 0x00abc12c | `UNCONDITIONAL_JUMP`
<a id="insn-00abc0fc"></a> `00abc0fc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abc100"></a> `00abc100` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00abc104"></a> `00abc104` | `48 01 00 b4` | cbz x8,0x00abc12c | `CONDITIONAL_JUMP`
<a id="insn-00abc108"></a> `00abc108` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00abc10c"></a> `00abc10c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abc110"></a> `00abc110` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00abc114"></a> `00abc114` | `4a ff ff 54` | b.ge 0x00abc0fc | `CONDITIONAL_JUMP`
<a id="insn-00abc118"></a> `00abc118` | `1f bd 00 71` | cmp w8,#0x2f | `FALL_THROUGH`
<a id="insn-00abc11c"></a> `00abc11c` | `00 f8 ff 54` | b.eq 0x00abc01c | `CONDITIONAL_JUMP`
<a id="insn-00abc120"></a> `00abc120` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00abc124"></a> `00abc124` | `28 ff ff b5` | cbnz x8,0x00abc108 | `CONDITIONAL_JUMP`
<a id="insn-00abc128"></a> `00abc128` | `b8 22 00 91` | add x24,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abc12c"></a> `00abc12c` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abc130"></a> `00abc130` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00abc134"></a> `00abc134` | `7f 73 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00abc138"></a> `00abc138` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abc13c"></a> `00abc13c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abc140"></a> `00abc140` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abc144"></a> `00abc144` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abc148"></a> `00abc148` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00abc14c"></a> `00abc14c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00abc150"></a> `00abc150` | `17 1c 00 b9` | str w23,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abc154"></a> `00abc154` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abc158"></a> `00abc158` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abc15c"></a> `00abc15c` | `68 f5 ff b4` | cbz x8,0x00abc008 | `CONDITIONAL_JUMP`
<a id="insn-00abc160"></a> `00abc160` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00abc164"></a> `00abc164` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00abc168"></a> `00abc168` | `a8 ff ff 17` | b 0x00abc008 | `UNCONDITIONAL_JUMP`
<a id="insn-00abc16c"></a> `00abc16c` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00abc170"></a> `00abc170` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abc174"></a> `00abc174` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abc178"></a> `00abc178` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abc17c"></a> `00abc17c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abc180"></a> `00abc180` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00abc184"></a> `00abc184` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abbfe0`](#insn-00abbfe0) 範囲 `[['00abbfe0', '00abbfeb']]`
  - `FALL_THROUGH` [`00abbfe8`](#insn-00abbfe8) → [`00abbfec`](#insn-00abbfec)
- ブロック [`00abbfec`](#insn-00abbfec) 範囲 `[['00abbfec', '00abc007']]`
  - `UNCONDITIONAL_JUMP` [`00abc004`](#insn-00abc004) → [`00abc038`](#insn-00abc038)
- ブロック [`00abc008`](#insn-00abc008) 範囲 `[['00abc008', '00abc01b']]`
  - `FALL_THROUGH` [`00abc018`](#insn-00abc018) → [`00abc01c`](#insn-00abc01c)
- ブロック [`00abc01c`](#insn-00abc01c) 範囲 `[['00abc01c', '00abc02b']]`
  - `FALL_THROUGH` [`00abc028`](#insn-00abc028) → [`00abc02c`](#insn-00abc02c)
- ブロック [`00abc02c`](#insn-00abc02c) 範囲 `[['00abc02c', '00abc037']]`
  - `CONDITIONAL_JUMP` [`00abc034`](#insn-00abc034) → [`00abc16c`](#insn-00abc16c)
  - `FALL_THROUGH` [`00abc034`](#insn-00abc034) → [`00abc038`](#insn-00abc038)
- ブロック [`00abc038`](#insn-00abc038) 範囲 `[['00abc038', '00abc03f']]`
  - `CONDITIONAL_JUMP` [`00abc03c`](#insn-00abc03c) → [`00abc02c`](#insn-00abc02c)
  - `FALL_THROUGH` [`00abc03c`](#insn-00abc03c) → [`00abc040`](#insn-00abc040)
- ブロック [`00abc040`](#insn-00abc040) 範囲 `[['00abc040', '00abc043']]`
  - `FALL_THROUGH` [`00abc040`](#insn-00abc040) → [`00abc044`](#insn-00abc044)
- ブロック [`00abc044`](#insn-00abc044) 範囲 `[['00abc044', '00abc053']]`
  - `CONDITIONAL_JUMP` [`00abc050`](#insn-00abc050) → [`00abc068`](#insn-00abc068)
  - `FALL_THROUGH` [`00abc050`](#insn-00abc050) → [`00abc054`](#insn-00abc054)
- ブロック [`00abc054`](#insn-00abc054) 範囲 `[['00abc054', '00abc05b']]`
  - `UNCONDITIONAL_JUMP` [`00abc058`](#insn-00abc058) → [`00abc08c`](#insn-00abc08c)
- ブロック [`00abc05c`](#insn-00abc05c) 範囲 `[['00abc05c', '00abc067']]`
  - `CONDITIONAL_JUMP` [`00abc064`](#insn-00abc064) → [`00abc08c`](#insn-00abc08c)
  - `FALL_THROUGH` [`00abc064`](#insn-00abc064) → [`00abc068`](#insn-00abc068)
- ブロック [`00abc068`](#insn-00abc068) 範囲 `[['00abc068', '00abc06f']]`
  - `FALL_THROUGH` [`00abc06c`](#insn-00abc06c) → [`00abc070`](#insn-00abc070)
- ブロック [`00abc070`](#insn-00abc070) 範囲 `[['00abc070', '00abc077']]`
  - `CONDITIONAL_JUMP` [`00abc074`](#insn-00abc074) → [`00abc05c`](#insn-00abc05c)
  - `FALL_THROUGH` [`00abc074`](#insn-00abc074) → [`00abc078`](#insn-00abc078)
- ブロック [`00abc078`](#insn-00abc078) 範囲 `[['00abc078', '00abc07f']]`
  - `CONDITIONAL_JUMP` [`00abc07c`](#insn-00abc07c) → [`00abc0e8`](#insn-00abc0e8)
  - `FALL_THROUGH` [`00abc07c`](#insn-00abc07c) → [`00abc080`](#insn-00abc080)
- ブロック [`00abc080`](#insn-00abc080) 範囲 `[['00abc080', '00abc087']]`
  - `CONDITIONAL_JUMP` [`00abc084`](#insn-00abc084) → [`00abc068`](#insn-00abc068)
  - `FALL_THROUGH` [`00abc084`](#insn-00abc084) → [`00abc088`](#insn-00abc088)
- ブロック [`00abc088`](#insn-00abc088) 範囲 `[['00abc088', '00abc08b']]`
  - `FALL_THROUGH` [`00abc088`](#insn-00abc088) → [`00abc08c`](#insn-00abc08c)
- ブロック [`00abc08c`](#insn-00abc08c) 範囲 `[['00abc08c', '00abc0cb']]`
  - `CONDITIONAL_JUMP` [`00abc0c8`](#insn-00abc0c8) → [`00abc0d4`](#insn-00abc0d4)
  - `FALL_THROUGH` [`00abc0c8`](#insn-00abc0c8) → [`00abc0cc`](#insn-00abc0cc)
- ブロック [`00abc0cc`](#insn-00abc0cc) 範囲 `[['00abc0cc', '00abc0d3']]`
  - `FALL_THROUGH` [`00abc0d0`](#insn-00abc0d0) → [`00abc0d4`](#insn-00abc0d4)
- ブロック [`00abc0d4`](#insn-00abc0d4) 範囲 `[['00abc0d4', '00abc0e7']]`
  - `FALL_THROUGH` [`00abc0e4`](#insn-00abc0e4) → [`00abc0e8`](#insn-00abc0e8)
- ブロック [`00abc0e8`](#insn-00abc0e8) 範囲 `[['00abc0e8', '00abc0f3']]`
  - `CONDITIONAL_JUMP` [`00abc0f0`](#insn-00abc0f0) → [`00abc108`](#insn-00abc108)
  - `FALL_THROUGH` [`00abc0f0`](#insn-00abc0f0) → [`00abc0f4`](#insn-00abc0f4)
- ブロック [`00abc0f4`](#insn-00abc0f4) 範囲 `[['00abc0f4', '00abc0fb']]`
  - `UNCONDITIONAL_JUMP` [`00abc0f8`](#insn-00abc0f8) → [`00abc12c`](#insn-00abc12c)
- ブロック [`00abc0fc`](#insn-00abc0fc) 範囲 `[['00abc0fc', '00abc107']]`
  - `CONDITIONAL_JUMP` [`00abc104`](#insn-00abc104) → [`00abc12c`](#insn-00abc12c)
  - `FALL_THROUGH` [`00abc104`](#insn-00abc104) → [`00abc108`](#insn-00abc108)
- ブロック [`00abc108`](#insn-00abc108) 範囲 `[['00abc108', '00abc117']]`
  - `CONDITIONAL_JUMP` [`00abc114`](#insn-00abc114) → [`00abc0fc`](#insn-00abc0fc)
  - `FALL_THROUGH` [`00abc114`](#insn-00abc114) → [`00abc118`](#insn-00abc118)
- ブロック [`00abc118`](#insn-00abc118) 範囲 `[['00abc118', '00abc11f']]`
  - `CONDITIONAL_JUMP` [`00abc11c`](#insn-00abc11c) → [`00abc01c`](#insn-00abc01c)
  - `FALL_THROUGH` [`00abc11c`](#insn-00abc11c) → [`00abc120`](#insn-00abc120)
- ブロック [`00abc120`](#insn-00abc120) 範囲 `[['00abc120', '00abc127']]`
  - `CONDITIONAL_JUMP` [`00abc124`](#insn-00abc124) → [`00abc108`](#insn-00abc108)
  - `FALL_THROUGH` [`00abc124`](#insn-00abc124) → [`00abc128`](#insn-00abc128)
- ブロック [`00abc128`](#insn-00abc128) 範囲 `[['00abc128', '00abc12b']]`
  - `FALL_THROUGH` [`00abc128`](#insn-00abc128) → [`00abc12c`](#insn-00abc12c)
- ブロック [`00abc12c`](#insn-00abc12c) 範囲 `[['00abc12c', '00abc13b']]`
  - `FALL_THROUGH` [`00abc138`](#insn-00abc138) → [`00abc13c`](#insn-00abc13c)
- ブロック [`00abc13c`](#insn-00abc13c) 範囲 `[['00abc13c', '00abc15f']]`
  - `CONDITIONAL_JUMP` [`00abc15c`](#insn-00abc15c) → [`00abc008`](#insn-00abc008)
  - `FALL_THROUGH` [`00abc15c`](#insn-00abc15c) → [`00abc160`](#insn-00abc160)
- ブロック [`00abc160`](#insn-00abc160) 範囲 `[['00abc160', '00abc16b']]`
  - `UNCONDITIONAL_JUMP` [`00abc168`](#insn-00abc168) → [`00abc008`](#insn-00abc008)
- ブロック [`00abc16c`](#insn-00abc16c) 範囲 `[['00abc16c', '00abc187']]`

## 命令位置別の参照

- [`00abbfe0`](#insn-00abbfe0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfe4`](#insn-00abbfe4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfe8`](#insn-00abbfe8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfec`](#insn-00abbfec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbff0`](#insn-00abbff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc004`](#insn-00abc004) → [`00abc038`](#insn-00abc038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc00c`](#insn-00abc00c) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00abc034`](#insn-00abc034) → [`00abc16c`](#insn-00abc16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc03c`](#insn-00abc03c) → [`00abc02c`](#insn-00abc02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc040`](#insn-00abc040) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abc04c`](#insn-00abc04c) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc050`](#insn-00abc050) → [`00abc068`](#insn-00abc068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc058`](#insn-00abc058) → [`00abc08c`](#insn-00abc08c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc064`](#insn-00abc064) → [`00abc08c`](#insn-00abc08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc074`](#insn-00abc074) → [`00abc05c`](#insn-00abc05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc07c`](#insn-00abc07c) → [`00abc0e8`](#insn-00abc0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc084`](#insn-00abc084) → [`00abc068`](#insn-00abc068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc094`](#insn-00abc094) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00abc0b8`](#insn-00abc0b8) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc0bc`](#insn-00abc0bc) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc0c8`](#insn-00abc0c8) → [`00abc0d4`](#insn-00abc0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc0cc`](#insn-00abc0cc) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc0d0`](#insn-00abc0d0) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc0d4`](#insn-00abc0d4) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc0d8`](#insn-00abc0d8) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00abc0dc`](#insn-00abc0dc) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc0e4`](#insn-00abc0e4) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abc0f0`](#insn-00abc0f0) → [`00abc108`](#insn-00abc108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc0f8`](#insn-00abc0f8) → [`00abc12c`](#insn-00abc12c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc104`](#insn-00abc104) → [`00abc12c`](#insn-00abc12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc114`](#insn-00abc114) → [`00abc0fc`](#insn-00abc0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc11c`](#insn-00abc11c) → [`00abc01c`](#insn-00abc01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc124`](#insn-00abc124) → [`00abc108`](#insn-00abc108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc134`](#insn-00abc134) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00abc15c`](#insn-00abc15c) → [`00abc008`](#insn-00abc008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc168`](#insn-00abc168) → [`00abc008`](#insn-00abc008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc170`](#insn-00abc170) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc174`](#insn-00abc174) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc178`](#insn-00abc178) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc17c`](#insn-00abc17c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc180`](#insn-00abc180) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abbfe0`](#insn-00abbfe0)

~~~json
{
  "source": "00abbfe0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfe4`](#insn-00abbfe4)

~~~json
{
  "source": "00abbfe4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfe8`](#insn-00abbfe8)

~~~json
{
  "source": "00abbfe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfec`](#insn-00abbfec)

~~~json
{
  "source": "00abbfec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbff0`](#insn-00abbff0)

~~~json
{
  "source": "00abbff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc004`](#insn-00abc004)

~~~json
{
  "source": "00abc004",
  "target": "00abc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc00c`](#insn-00abc00c)

~~~json
{
  "source": "00abc00c",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc034`](#insn-00abc034)

~~~json
{
  "source": "00abc034",
  "target": "00abc16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc03c`](#insn-00abc03c)

~~~json
{
  "source": "00abc03c",
  "target": "00abc02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc040`](#insn-00abc040)

~~~json
{
  "source": "00abc040",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc04c`](#insn-00abc04c)

~~~json
{
  "source": "00abc04c",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc050`](#insn-00abc050)

~~~json
{
  "source": "00abc050",
  "target": "00abc068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc058`](#insn-00abc058)

~~~json
{
  "source": "00abc058",
  "target": "00abc08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc064`](#insn-00abc064)

~~~json
{
  "source": "00abc064",
  "target": "00abc08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc074`](#insn-00abc074)

~~~json
{
  "source": "00abc074",
  "target": "00abc05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc07c`](#insn-00abc07c)

~~~json
{
  "source": "00abc07c",
  "target": "00abc0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc084`](#insn-00abc084)

~~~json
{
  "source": "00abc084",
  "target": "00abc068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc094`](#insn-00abc094)

~~~json
{
  "source": "00abc094",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc0b8`](#insn-00abc0b8)

~~~json
{
  "source": "00abc0b8",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc0bc`](#insn-00abc0bc)

~~~json
{
  "source": "00abc0bc",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6cc97d004c6f0a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc0c8`](#insn-00abc0c8)

~~~json
{
  "source": "00abc0c8",
  "target": "00abc0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc0cc`](#insn-00abc0cc)

~~~json
{
  "source": "00abc0cc",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6cc97d004c6f0a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc0d0`](#insn-00abc0d0)

~~~json
{
  "source": "00abc0d0",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc0d4`](#insn-00abc0d4)

~~~json
{
  "source": "00abc0d4",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc0d8`](#insn-00abc0d8)

~~~json
{
  "source": "00abc0d8",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc0dc`](#insn-00abc0dc)

~~~json
{
  "source": "00abc0dc",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cc97d00746f0a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc0e4`](#insn-00abc0e4)

~~~json
{
  "source": "00abc0e4",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cc97d00746f0a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abc0f0`](#insn-00abc0f0)

~~~json
{
  "source": "00abc0f0",
  "target": "00abc108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc0f8`](#insn-00abc0f8)

~~~json
{
  "source": "00abc0f8",
  "target": "00abc12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc104`](#insn-00abc104)

~~~json
{
  "source": "00abc104",
  "target": "00abc12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc114`](#insn-00abc114)

~~~json
{
  "source": "00abc114",
  "target": "00abc0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc11c`](#insn-00abc11c)

~~~json
{
  "source": "00abc11c",
  "target": "00abc01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc124`](#insn-00abc124)

~~~json
{
  "source": "00abc124",
  "target": "00abc108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc134`](#insn-00abc134)

~~~json
{
  "source": "00abc134",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc15c`](#insn-00abc15c)

~~~json
{
  "source": "00abc15c",
  "target": "00abc008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc168`](#insn-00abc168)

~~~json
{
  "source": "00abc168",
  "target": "00abc008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc170`](#insn-00abc170)

~~~json
{
  "source": "00abc170",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc174`](#insn-00abc174)

~~~json
{
  "source": "00abc174",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc178`](#insn-00abc178)

~~~json
{
  "source": "00abc178",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc17c`](#insn-00abc17c)

~~~json
{
  "source": "00abc17c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc180`](#insn-00abc180)

~~~json
{
  "source": "00abc180",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
