# 00bceca8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcebe0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebe0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-eb9deee7dd31c5e95ea23debebd46841)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcecec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-18bcaf574d2a033c0351fd5ef31e0ffc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceca8",
  "name": "FUN_00bceca8",
  "size": 884,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2fc50efdfad960a58d734ad7260d55876caf9f54c7d3bf7b2a38b5d841767e50",
  "source_text_sha256": "2fc50efdfad960a58d734ad7260d55876caf9f54c7d3bf7b2a38b5d841767e50",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bceca8",
        "00bcf01b"
      ]
    ],
    "bytes_sha256": "866713c8bcbfbeaddb4d1a7b3dc346cf445a7464bfebf98e51101f5f20d348db",
    "instruction_count": 221,
    "instruction_bytes": 884,
    "body_bytes": 884,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc245c](../00bc2/00bc245c.md)
- [00bce8f8](../00bce/00bce8f8.md)

## 呼び出し先

- [00bbde18](../00bbd/00bbde18.md)
- [00bc10fc](../00bc1/00bc10fc.md)
- [00bdb140](../00bdb/00bdb140.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

## 関連文字列（未確認候補）

~~~text
"operator-="
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7460 bytes

~~~c

undefined8 * FUN_00bceca8(long *param_1,undefined1 *param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  byte bVar4;
  undefined1 uVar5;
  long lVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  size_t sVar9;
  undefined **ppuVar10;
  long lVar11;
  undefined1 uVar12;
  long lVar13;
  ulong uVar14;
  ulong uVar15;
  ulong uVar16;
  char *__s;
  void *pvVar17;
  
  pbVar2 = (byte *)*param_1;
  pbVar3 = (byte *)param_1[1];
  if (1 < (ulong)((long)pbVar3 - (long)pbVar2)) {
    bVar4 = *pbVar2;
    uVar14 = 0;
    uVar15 = 0x3d;
    do {
      uVar16 = uVar14 + uVar15 >> 1;
      if ((byte)(&UNK_00c17988)[uVar16 * 0x10] < bVar4) {
        uVar14 = uVar16 + 1;
        uVar16 = uVar15;
      }
      else {
                    /* try { // try from 00bced1c to 00cced27 has its CatchHandler @ 00bcf338 */
        if (((&UNK_00c17988)[uVar16 * 0x10] == bVar4) &&
           ((byte)(&UNK_00c17989)[uVar16 * 0x10] < pbVar2[1])) {
          uVar14 = uVar16 + 1;
          uVar16 = uVar15;
        }
      }
      uVar15 = uVar16;
    } while (uVar16 != uVar14);
    lVar11 = uVar14 * 0x10;
                    /* try { // try from 00bced44 to 00cced53 has its CatchHandler @ 00bcf334 */
                    /* try { // try from 00bced54 to 00cced5f has its CatchHandler @ 00bcf320 */
    if (((&UNK_00c17988)[lVar11] == bVar4) && ((&UNK_00c17989)[lVar11] == pbVar2[1])) {
      bVar4 = (&UNK_00c1798a)[lVar11];
                    /* try { // try from 00bced60 to 00cced73 has its CatchHandler @ 00bcf310 */
      *param_1 = (long)(pbVar2 + 2);
      if (bVar4 == 8) {
        uVar5 = *(undefined1 *)((long)param_1 + 0x309);
                    /* try { // try from 00bced74 to 00cced7f has its CatchHandler @ 00bcf2e0 */
        lVar11 = param_1[0x61];
        *(undefined1 *)(param_1 + 0x61) = 0;
        uVar12 = uVar5;
                    /* try { // try from 00bced80 to 00cced8f has its CatchHandler @ 00bcf2c0 */
        if (param_2 != (undefined1 *)0x0) {
          uVar12 = 1;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar12;
        lVar6 = FUN_00bbde18();
                    /* try { // try from 00bced90 to 00cceda7 has its CatchHandler @ 00bcf27c */
        if (lVar6 == 0) {
          puVar8 = (undefined8 *)0x0;
        }
        else {
          if (param_2 != (undefined1 *)0x0) {
            *param_2 = 1;
          }
                    /* try { // try from 00bceda8 to 00ccee0f has its CatchHandler @ 00bce594 */
          pvVar17 = (void *)param_1[0x266];
          lVar13 = *(long *)((long)pvVar17 + 8);
          puVar7 = pvVar17;
          if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
            puVar7 = malloc(0x1000);
            if (puVar7 == (void *)0x0) goto LAB_00bcf018;
            lVar13 = 0;
            *puVar7 = pvVar17;
            puVar7[1] = 0;
            param_1[0x266] = (long)puVar7;
          }
          *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
          puVar8 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
          *puVar8 = &PTR_FUN_00c19128;
          *(long *)((long)puVar7 + lVar13 + 0x20) = lVar6;
          *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 4;
                    /* try { // try from 00bcee10 to 00ccee4f has its CatchHandler @ 00bcf3c4 */
          *(ushort *)((long)puVar7 + lVar13 + 0x19) =
               *(ushort *)((long)puVar7 + lVar13 + 0x19) & 0xf000 | 0x540;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar5;
        *(char *)(param_1 + 0x61) = (char)lVar11;
        return puVar8;
      }
      if (10 < bVar4) {
        return (undefined8 *)0x0;
      }
      if ((bVar4 == 4) && (((&UNK_00c1798b)[lVar11] & 1) == 0)) {
        return (undefined8 *)0x0;
      }
      __s = *(char **)(&UNK_00c17990 + lVar11);
                    /* try { // try from 00bcef84 to 00ccefbb has its CatchHandler @ 00bcf210 */
      sVar9 = strlen(__s);
      pvVar17 = (void *)param_1[0x266];
      lVar11 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (0xfffffffffffff00f < lVar11 - 0xfd0U) {
LAB_00bcefc8:
                    /* try { // try from 00bcefc8 to 00ccefd7 has its CatchHandler @ 00bcf208 */
                    /* try { // try from 00bcefd8 to 00ccefef has its CatchHandler @ 00bcf204 */
        *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
        puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
        *puVar7 = &PTR_FUN_00c17848;
        *(char **)((long)puVar8 + lVar11 + 0x20) = __s;
        *(size_t *)((long)puVar8 + lVar11 + 0x28) = sVar9;
                    /* try { // try from 00bceff0 to 00ccf427 has its CatchHandler @ 00bce594 */
        *(undefined1 *)((long)puVar8 + lVar11 + 0x18) = 8;
        *(ushort *)((long)puVar8 + lVar11 + 0x19) =
             *(ushort *)((long)puVar8 + lVar11 + 0x19) & 0xf000 | 0x540;
        return puVar7;
      }
      puVar8 = malloc(0x1000);
      if (puVar8 != (void *)0x0) {
        lVar11 = 0;
                    /* try { // try from 00bcefbc to 00ccefc7 has its CatchHandler @ 00bcf20c */
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
        goto LAB_00bcefc8;
      }
      goto LAB_00bcf018;
    }
    if (*(short *)pbVar2 == 0x696c) {
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc10fc();
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00bcf018;
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c19198;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 0x14;
      goto LAB_00bcef28;
    }
  }
  if ((pbVar2 != pbVar3) && (*pbVar2 == 0x76)) {
    pbVar1 = pbVar2 + 1;
    *param_1 = (long)pbVar1;
                    /* try { // try from 00bcee50 to 00ccee5b has its CatchHandler @ 00bcf268 */
    if ((pbVar3 != pbVar1) && (*pbVar1 - 0x30 < 10)) {
                    /* try { // try from 00bcee5c to 00ccee6b has its CatchHandler @ 00bcf248 */
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc10fc();
                    /* try { // try from 00bcee6c to 00ccee83 has its CatchHandler @ 00bcf214 */
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
                    /* try { // try from 00bcee84 to 00ccef83 has its CatchHandler @ 00bce594 */
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00bcf018:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c19128;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 4;
LAB_00bcef28:
      *(undefined8 *)(lVar13 + 0x10) = ppuVar10;
      *(undefined1 *)(lVar13 + 0x18) = uVar12;
      *(long *)(lVar13 + 0x20) = lVar11;
      *(ushort *)(lVar13 + 0x19) = *(ushort *)(lVar13 + 0x19) & 0xf000 | 0x540;
      return (undefined8 *)(lVar13 + 0x10);
    }
  }
  return (undefined8 *)0x0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bceca8"></a> `00bceca8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcecac"></a> `00bcecac` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bcecb0"></a> `00bcecb0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcecb4"></a> `00bcecb4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcecb8"></a> `00bcecb8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcecbc"></a> `00bcecbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcecc0"></a> `00bcecc0` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bcecc4"></a> `00bcecc4` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00bcecc8"></a> `00bcecc8` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bceccc"></a> `00bceccc` | `e3 0a 00 54` | b.cc 0x00bcee28 | `CONDITIONAL_JUMP`
<a id="insn-00bcecd0"></a> `00bcecd0` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcecd4"></a> `00bcecd4` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00bcecd8"></a> `00bcecd8` | `ad 07 80 52` | mov w13,#0x3d | `FALL_THROUGH`
<a id="insn-00bcecdc"></a> `00bcecdc` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bcece0"></a> `00bcece0` | `4c 65 24 10` | adr x12,0xc17988 | `FALL_THROUGH`
<a id="insn-00bcece4"></a> `00bcece4` | `04 00 00 14` | b 0x00bcecf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcece8"></a> `00bcece8` | `cb 05 00 91` | add x11,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bcecec"></a> `00bcecec` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bcecf0"></a> `00bcecf0` | `40 02 00 54` | b.eq 0x00bced38 | `CONDITIONAL_JUMP`
<a id="insn-00bcecf4"></a> `00bcecf4` | `6e 01 0d 8b` | add x14,x11,x13 | `FALL_THROUGH`
<a id="insn-00bcecf8"></a> `00bcecf8` | `ce fd 41 d3` | lsr x14,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bcecfc"></a> `00bcecfc` | `8f 11 0e 8b` | add x15,x12,x14, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bced00"></a> `00bced00` | `f0 01 40 39` | ldrb w16,[x15] | `FALL_THROUGH`
<a id="insn-00bced04"></a> `00bced04` | `1f 02 0a 6b` | cmp w16,w10 | `FALL_THROUGH`
<a id="insn-00bced08"></a> `00bced08` | `03 ff ff 54` | b.cc 0x00bcece8 | `CONDITIONAL_JUMP`
<a id="insn-00bced0c"></a> `00bced0c` | `21 01 00 54` | b.ne 0x00bced30 | `CONDITIONAL_JUMP`
<a id="insn-00bced10"></a> `00bced10` | `ef 05 40 39` | ldrb w15,[x15, #0x1] | `FALL_THROUGH`
<a id="insn-00bced14"></a> `00bced14` | `10 05 40 39` | ldrb w16,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bced18"></a> `00bced18` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00bced1c"></a> `00bced1c` | `ef 27 9f 1a` | cset w15,cc | `FALL_THROUGH`
<a id="insn-00bced20"></a> `00bced20` | `ff 01 00 72` | tst w15,#0x1 | `FALL_THROUGH`
<a id="insn-00bced24"></a> `00bced24` | `6b 05 8e 9a` | csinc x11,x11,x14,eq | `FALL_THROUGH`
<a id="insn-00bced28"></a> `00bced28` | `ad 11 8e 9a` | csel x13,x13,x14,ne | `FALL_THROUGH`
<a id="insn-00bced2c"></a> `00bced2c` | `f0 ff ff 17` | b 0x00bcecec | `UNCONDITIONAL_JUMP`
<a id="insn-00bced30"></a> `00bced30` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bced34"></a> `00bced34` | `ee ff ff 17` | b 0x00bcecec | `UNCONDITIONAL_JUMP`
<a id="insn-00bced38"></a> `00bced38` | `8b 11 0b 8b` | add x11,x12,x11, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bced3c"></a> `00bced3c` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-00bced40"></a> `00bced40` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00bced44"></a> `00bced44` | `a1 06 00 54` | b.ne 0x00bcee18 | `CONDITIONAL_JUMP`
<a id="insn-00bced48"></a> `00bced48` | `6a 05 40 39` | ldrb w10,[x11, #0x1] | `FALL_THROUGH`
<a id="insn-00bced4c"></a> `00bced4c` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bced50"></a> `00bced50` | `5f 01 0c 6b` | cmp w10,w12 | `FALL_THROUGH`
<a id="insn-00bced54"></a> `00bced54` | `21 06 00 54` | b.ne 0x00bcee18 | `CONDITIONAL_JUMP`
<a id="insn-00bced58"></a> `00bced58` | `69 09 40 39` | ldrb w9,[x11, #0x2] | `FALL_THROUGH`
<a id="insn-00bced5c"></a> `00bced5c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bced60"></a> `00bced60` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bced64"></a> `00bced64` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bced68"></a> `00bced68` | `21 0f 00 54` | b.ne 0x00bcef4c | `CONDITIONAL_JUMP`
<a id="insn-00bced6c"></a> `00bced6c` | `14 24 4c 39` | ldrb w20,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00bced70"></a> `00bced70` | `3f 00 00 f1` | cmp x1,#0x0 | `FALL_THROUGH`
<a id="insn-00bced74"></a> `00bced74` | `15 20 4c 39` | ldrb w21,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00bced78"></a> `00bced78` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bced7c"></a> `00bced7c` | `1f 20 0c 39` | strb wzr,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00bced80"></a> `00bced80` | `88 06 9f 1a` | csinc w8,w20,wzr,eq | `FALL_THROUGH`
<a id="insn-00bced84"></a> `00bced84` | `08 24 0c 39` | strb w8,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00bced88"></a> `00bced88` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bced8c"></a> `00bced8c` | `23 bc ff 97` | bl 0x00bbde18 | `UNCONDITIONAL_CALL`
<a id="insn-00bced90"></a> `00bced90` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bced94"></a> `00bced94` | `80 13 00 b4` | cbz x0,0x00bcf004 | `CONDITIONAL_JUMP`
<a id="insn-00bced98"></a> `00bced98` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bced9c"></a> `00bced9c` | `77 00 00 b4` | cbz x23,0x00bceda8 | `CONDITIONAL_JUMP`
<a id="insn-00bceda0"></a> `00bceda0` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bceda4"></a> `00bceda4` | `e9 02 00 39` | strb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bceda8"></a> `00bceda8` | `17 99 49 f9` | ldr x23,[x8, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcedac"></a> `00bcedac` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bcedb0"></a> `00bcedb0` | `2a 41 3f d1` | sub x10,x9,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcedb4"></a> `00bcedb4` | `5f c5 3f b1` | cmn x10,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcedb8"></a> `00bcedb8` | `28 01 00 54` | b.hi 0x00bceddc | `CONDITIONAL_JUMP`
<a id="insn-00bcedbc"></a> `00bcedbc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcedc0"></a> `00bcedc0` | `f0 38 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bcedc4"></a> `00bcedc4` | `a0 12 00 b4` | cbz x0,0x00bcf018 | `CONDITIONAL_JUMP`
<a id="insn-00bcedc8"></a> `00bcedc8` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bcedcc"></a> `00bcedcc` | `17 7c 00 a9` | stp x23,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcedd0"></a> `00bcedd0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcedd4"></a> `00bcedd4` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcedd8"></a> `00bcedd8` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00bceddc"></a> `00bceddc` | `2a 81 00 91` | add x10,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcede0"></a> `00bcede0` | `e0 02 09 8b` | add x0,x23,x9 | `FALL_THROUGH`
<a id="insn-00bcede4"></a> `00bcede4` | `49 02 00 f0` | adrp x9,0xc19000 | `FALL_THROUGH`
<a id="insn-00bcede8"></a> `00bcede8` | `29 a1 04 91` | add x9,x9,#0x128 | `FALL_THROUGH`
<a id="insn-00bcedec"></a> `00bcedec` | `ea 06 00 f9` | str x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bcedf0"></a> `00bcedf0` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00bcedf4"></a> `00bcedf4` | `09 0c 01 f8` | str x9,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcedf8"></a> `00bcedf8` | `09 90 40 78` | ldurh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcedfc"></a> `00bcedfc` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00bcee00"></a> `00bcee00` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcee04"></a> `00bcee04` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcee08"></a> `00bcee08` | `0a 20 00 39` | strb w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee0c"></a> `00bcee0c` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00bcee10"></a> `00bcee10` | `09 90 00 78` | sturh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcee14"></a> `00bcee14` | `7e 00 00 14` | b 0x00bcf00c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcee18"></a> `00bcee18` | `0a 01 40 79` | ldrh w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcee1c"></a> `00bcee1c` | `8b 2d 8d 52` | mov w11,#0x696c | `FALL_THROUGH`
<a id="insn-00bcee20"></a> `00bcee20` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00bcee24"></a> `00bcee24` | `00 05 00 54` | b.eq 0x00bceec4 | `CONDITIONAL_JUMP`
<a id="insn-00bcee28"></a> `00bcee28` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcee2c"></a> `00bcee2c` | `40 09 00 54` | b.eq 0x00bcef54 | `CONDITIONAL_JUMP`
<a id="insn-00bcee30"></a> `00bcee30` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcee34"></a> `00bcee34` | `5f d9 01 71` | cmp w10,#0x76 | `FALL_THROUGH`
<a id="insn-00bcee38"></a> `00bcee38` | `e1 08 00 54` | b.ne 0x00bcef54 | `CONDITIONAL_JUMP`
<a id="insn-00bcee3c"></a> `00bcee3c` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcee40"></a> `00bcee40` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcee44"></a> `00bcee44` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bcee48"></a> `00bcee48` | `60 08 00 54` | b.eq 0x00bcef54 | `CONDITIONAL_JUMP`
<a id="insn-00bcee4c"></a> `00bcee4c` | `49 01 40 39` | ldrb w9,[x10] | `FALL_THROUGH`
<a id="insn-00bcee50"></a> `00bcee50` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bcee54"></a> `00bcee54` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bcee58"></a> `00bcee58` | `e8 07 00 54` | b.hi 0x00bcef54 | `CONDITIONAL_JUMP`
<a id="insn-00bcee5c"></a> `00bcee5c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcee60"></a> `00bcee60` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcee64"></a> `00bcee64` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcee68"></a> `00bcee68` | `a5 c8 ff 97` | bl 0x00bc10fc | `UNCONDITIONAL_CALL`
<a id="insn-00bcee6c"></a> `00bcee6c` | `60 07 00 b4` | cbz x0,0x00bcef58 | `CONDITIONAL_JUMP`
<a id="insn-00bcee70"></a> `00bcee70` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcee74"></a> `00bcee74` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bcee78"></a> `00bcee78` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcee7c"></a> `00bcee7c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee80"></a> `00bcee80` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcee84"></a> `00bcee84` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcee88"></a> `00bcee88` | `08 01 00 54` | b.hi 0x00bceea8 | `CONDITIONAL_JUMP`
<a id="insn-00bcee8c"></a> `00bcee8c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcee90"></a> `00bcee90` | `bc 38 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee94"></a> `00bcee94` | `20 0c 00 b4` | cbz x0,0x00bcf018 | `CONDITIONAL_JUMP`
<a id="insn-00bcee98"></a> `00bcee98` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcee9c"></a> `00bcee9c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bceea0"></a> `00bceea0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bceea4"></a> `00bceea4` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bceea8"></a> `00bceea8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bceeac"></a> `00bceeac` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bceeb0"></a> `00bceeb0` | `48 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bceeb4"></a> `00bceeb4` | `08 a1 04 91` | add x8,x8,#0x128 | `FALL_THROUGH`
<a id="insn-00bceeb8"></a> `00bceeb8` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bceebc"></a> `00bceebc` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bceec0"></a> `00bceec0` | `1a 00 00 14` | b 0x00bcef28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bceec4"></a> `00bceec4` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bceec8"></a> `00bceec8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bceecc"></a> `00bceecc` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bceed0"></a> `00bceed0` | `8b c8 ff 97` | bl 0x00bc10fc | `UNCONDITIONAL_CALL`
<a id="insn-00bceed4"></a> `00bceed4` | `20 04 00 b4` | cbz x0,0x00bcef58 | `CONDITIONAL_JUMP`
<a id="insn-00bceed8"></a> `00bceed8` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bceedc"></a> `00bceedc` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bceee0"></a> `00bceee0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bceee4"></a> `00bceee4` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bceee8"></a> `00bceee8` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bceeec"></a> `00bceeec` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bceef0"></a> `00bceef0` | `08 01 00 54` | b.hi 0x00bcef10 | `CONDITIONAL_JUMP`
<a id="insn-00bceef4"></a> `00bceef4` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bceef8"></a> `00bceef8` | `a2 38 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bceefc"></a> `00bceefc` | `e0 08 00 b4` | cbz x0,0x00bcf018 | `CONDITIONAL_JUMP`
<a id="insn-00bcef00"></a> `00bcef00` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcef04"></a> `00bcef04` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcef08"></a> `00bcef08` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcef0c"></a> `00bcef0c` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcef10"></a> `00bcef10` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcef14"></a> `00bcef14` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bcef18"></a> `00bcef18` | `48 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bcef1c"></a> `00bcef1c` | `08 61 06 91` | add x8,x8,#0x198 | `FALL_THROUGH`
<a id="insn-00bcef20"></a> `00bcef20` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef24"></a> `00bcef24` | `89 02 80 52` | mov w9,#0x14 | `FALL_THROUGH`
<a id="insn-00bcef28"></a> `00bcef28` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcef2c"></a> `00bcef2c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcef30"></a> `00bcef30` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bcef34"></a> `00bcef34` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcef38"></a> `00bcef38` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef3c"></a> `00bcef3c` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bcef40"></a> `00bcef40` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcef44"></a> `00bcef44` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcef48"></a> `00bcef48` | `04 00 00 14` | b 0x00bcef58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcef4c"></a> `00bcef4c` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00bcef50"></a> `00bcef50` | `09 01 00 54` | b.ls 0x00bcef70 | `CONDITIONAL_JUMP`
<a id="insn-00bcef54"></a> `00bcef54` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bcef58"></a> `00bcef58` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcef5c"></a> `00bcef5c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcef60"></a> `00bcef60` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcef64"></a> `00bcef64` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcef68"></a> `00bcef68` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcef6c"></a> `00bcef6c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcef70"></a> `00bcef70` | `3f 11 00 71` | cmp w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bcef74"></a> `00bcef74` | `61 00 00 54` | b.ne 0x00bcef80 | `CONDITIONAL_JUMP`
<a id="insn-00bcef78"></a> `00bcef78` | `68 0d 40 39` | ldrb w8,[x11, #0x3] | `FALL_THROUGH`
<a id="insn-00bcef7c"></a> `00bcef7c` | `c8 fe 07 36` | tbz w8,#0x0,0x00bcef54 | `CONDITIONAL_JUMP`
<a id="insn-00bcef80"></a> `00bcef80` | `73 05 40 f9` | ldr x19,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef84"></a> `00bcef84` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcef88"></a> `00bcef88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcef8c"></a> `00bcef8c` | `6d 30 00 94` | bl 0x00bdb140 | `UNCONDITIONAL_CALL`
<a id="insn-00bcef90"></a> `00bcef90` | `95 9a 49 f9` | ldr x21,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcef94"></a> `00bcef94` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00bcef98"></a> `00bcef98` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcef9c"></a> `00bcef9c` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcefa0"></a> `00bcefa0` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcefa4"></a> `00bcefa4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcefa8"></a> `00bcefa8` | `08 01 00 54` | b.hi 0x00bcefc8 | `CONDITIONAL_JUMP`
<a id="insn-00bcefac"></a> `00bcefac` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcefb0"></a> `00bcefb0` | `74 38 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bcefb4"></a> `00bcefb4` | `20 03 00 b4` | cbz x0,0x00bcf018 | `CONDITIONAL_JUMP`
<a id="insn-00bcefb8"></a> `00bcefb8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcefbc"></a> `00bcefbc` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcefc0"></a> `00bcefc0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcefc4"></a> `00bcefc4` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcefc8"></a> `00bcefc8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcefcc"></a> `00bcefcc` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bcefd0"></a> `00bcefd0` | `48 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bcefd4"></a> `00bcefd4` | `08 21 21 91` | add x8,x8,#0x848 | `FALL_THROUGH`
<a id="insn-00bcefd8"></a> `00bcefd8` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcefdc"></a> `00bcefdc` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bcefe0"></a> `00bcefe0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcefe4"></a> `00bcefe4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcefe8"></a> `00bcefe8` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcefec"></a> `00bcefec` | `13 50 01 a9` | stp x19,x20,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bceff0"></a> `00bceff0` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bceff4"></a> `00bceff4` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bceff8"></a> `00bceff8` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bceffc"></a> `00bceffc` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf000"></a> `00bcf000` | `d6 ff ff 17` | b 0x00bcef58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf004"></a> `00bcf004` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bcf008"></a> `00bcf008` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcf00c"></a> `00bcf00c` | `14 25 0c 39` | strb w20,[x8, #0x309] | `FALL_THROUGH`
<a id="insn-00bcf010"></a> `00bcf010` | `15 21 0c 39` | strb w21,[x8, #0x308] | `FALL_THROUGH`
<a id="insn-00bcf014"></a> `00bcf014` | `d1 ff ff 17` | b 0x00bcef58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf018"></a> `00bcf018` | `5a 30 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bceca8`](#insn-00bceca8) 範囲 `[['00bceca8', '00bceccf']]`
  - `CONDITIONAL_JUMP` [`00bceccc`](#insn-00bceccc) → [`00bcee28`](#insn-00bcee28)
  - `FALL_THROUGH` [`00bceccc`](#insn-00bceccc) → [`00bcecd0`](#insn-00bcecd0)
- ブロック [`00bcecd0`](#insn-00bcecd0) 範囲 `[['00bcecd0', '00bcece7']]`
  - `UNCONDITIONAL_JUMP` [`00bcece4`](#insn-00bcece4) → [`00bcecf4`](#insn-00bcecf4)
- ブロック [`00bcece8`](#insn-00bcece8) 範囲 `[['00bcece8', '00bceceb']]`
  - `FALL_THROUGH` [`00bcece8`](#insn-00bcece8) → [`00bcecec`](#insn-00bcecec)
- ブロック [`00bcecec`](#insn-00bcecec) 範囲 `[['00bcecec', '00bcecf3']]`
  - `CONDITIONAL_JUMP` [`00bcecf0`](#insn-00bcecf0) → [`00bced38`](#insn-00bced38)
  - `FALL_THROUGH` [`00bcecf0`](#insn-00bcecf0) → [`00bcecf4`](#insn-00bcecf4)
- ブロック [`00bcecf4`](#insn-00bcecf4) 範囲 `[['00bcecf4', '00bced0b']]`
  - `CONDITIONAL_JUMP` [`00bced08`](#insn-00bced08) → [`00bcece8`](#insn-00bcece8)
  - `FALL_THROUGH` [`00bced08`](#insn-00bced08) → [`00bced0c`](#insn-00bced0c)
- ブロック [`00bced0c`](#insn-00bced0c) 範囲 `[['00bced0c', '00bced0f']]`
  - `CONDITIONAL_JUMP` [`00bced0c`](#insn-00bced0c) → [`00bced30`](#insn-00bced30)
  - `FALL_THROUGH` [`00bced0c`](#insn-00bced0c) → [`00bced10`](#insn-00bced10)
- ブロック [`00bced10`](#insn-00bced10) 範囲 `[['00bced10', '00bced1b']]`
  - `FALL_THROUGH` [`00bced18`](#insn-00bced18) → [`00bced1c`](#insn-00bced1c)
- ブロック [`00bced1c`](#insn-00bced1c) 範囲 `[['00bced1c', '00bced2f']]`
  - `UNCONDITIONAL_JUMP` [`00bced2c`](#insn-00bced2c) → [`00bcecec`](#insn-00bcecec)
- ブロック [`00bced30`](#insn-00bced30) 範囲 `[['00bced30', '00bced37']]`
  - `UNCONDITIONAL_JUMP` [`00bced34`](#insn-00bced34) → [`00bcecec`](#insn-00bcecec)
- ブロック [`00bced38`](#insn-00bced38) 範囲 `[['00bced38', '00bced43']]`
  - `FALL_THROUGH` [`00bced40`](#insn-00bced40) → [`00bced44`](#insn-00bced44)
- ブロック [`00bced44`](#insn-00bced44) 範囲 `[['00bced44', '00bced47']]`
  - `CONDITIONAL_JUMP` [`00bced44`](#insn-00bced44) → [`00bcee18`](#insn-00bcee18)
  - `FALL_THROUGH` [`00bced44`](#insn-00bced44) → [`00bced48`](#insn-00bced48)
- ブロック [`00bced48`](#insn-00bced48) 範囲 `[['00bced48', '00bced53']]`
  - `FALL_THROUGH` [`00bced50`](#insn-00bced50) → [`00bced54`](#insn-00bced54)
- ブロック [`00bced54`](#insn-00bced54) 範囲 `[['00bced54', '00bced57']]`
  - `CONDITIONAL_JUMP` [`00bced54`](#insn-00bced54) → [`00bcee18`](#insn-00bcee18)
  - `FALL_THROUGH` [`00bced54`](#insn-00bced54) → [`00bced58`](#insn-00bced58)
- ブロック [`00bced58`](#insn-00bced58) 範囲 `[['00bced58', '00bced5f']]`
  - `FALL_THROUGH` [`00bced5c`](#insn-00bced5c) → [`00bced60`](#insn-00bced60)
- ブロック [`00bced60`](#insn-00bced60) 範囲 `[['00bced60', '00bced6b']]`
  - `CONDITIONAL_JUMP` [`00bced68`](#insn-00bced68) → [`00bcef4c`](#insn-00bcef4c)
  - `FALL_THROUGH` [`00bced68`](#insn-00bced68) → [`00bced6c`](#insn-00bced6c)
- ブロック [`00bced6c`](#insn-00bced6c) 範囲 `[['00bced6c', '00bced73']]`
  - `FALL_THROUGH` [`00bced70`](#insn-00bced70) → [`00bced74`](#insn-00bced74)
- ブロック [`00bced74`](#insn-00bced74) 範囲 `[['00bced74', '00bced7f']]`
  - `FALL_THROUGH` [`00bced7c`](#insn-00bced7c) → [`00bced80`](#insn-00bced80)
- ブロック [`00bced80`](#insn-00bced80) 範囲 `[['00bced80', '00bced8f']]`
  - `FALL_THROUGH` [`00bced8c`](#insn-00bced8c) → [`00bced90`](#insn-00bced90)
- ブロック [`00bced90`](#insn-00bced90) 範囲 `[['00bced90', '00bced97']]`
  - `CONDITIONAL_JUMP` [`00bced94`](#insn-00bced94) → [`00bcf004`](#insn-00bcf004)
  - `FALL_THROUGH` [`00bced94`](#insn-00bced94) → [`00bced98`](#insn-00bced98)
- ブロック [`00bced98`](#insn-00bced98) 範囲 `[['00bced98', '00bced9f']]`
  - `CONDITIONAL_JUMP` [`00bced9c`](#insn-00bced9c) → [`00bceda8`](#insn-00bceda8)
  - `FALL_THROUGH` [`00bced9c`](#insn-00bced9c) → [`00bceda0`](#insn-00bceda0)
- ブロック [`00bceda0`](#insn-00bceda0) 範囲 `[['00bceda0', '00bceda7']]`
  - `FALL_THROUGH` [`00bceda4`](#insn-00bceda4) → [`00bceda8`](#insn-00bceda8)
- ブロック [`00bceda8`](#insn-00bceda8) 範囲 `[['00bceda8', '00bcedbb']]`
  - `CONDITIONAL_JUMP` [`00bcedb8`](#insn-00bcedb8) → [`00bceddc`](#insn-00bceddc)
  - `FALL_THROUGH` [`00bcedb8`](#insn-00bcedb8) → [`00bcedbc`](#insn-00bcedbc)
- ブロック [`00bcedbc`](#insn-00bcedbc) 範囲 `[['00bcedbc', '00bcedc7']]`
  - `CONDITIONAL_JUMP` [`00bcedc4`](#insn-00bcedc4) → [`00bcf018`](#insn-00bcf018)
  - `FALL_THROUGH` [`00bcedc4`](#insn-00bcedc4) → [`00bcedc8`](#insn-00bcedc8)
- ブロック [`00bcedc8`](#insn-00bcedc8) 範囲 `[['00bcedc8', '00bceddb']]`
  - `FALL_THROUGH` [`00bcedd8`](#insn-00bcedd8) → [`00bceddc`](#insn-00bceddc)
- ブロック [`00bceddc`](#insn-00bceddc) 範囲 `[['00bceddc', '00bcee0f']]`
  - `FALL_THROUGH` [`00bcee0c`](#insn-00bcee0c) → [`00bcee10`](#insn-00bcee10)
- ブロック [`00bcee10`](#insn-00bcee10) 範囲 `[['00bcee10', '00bcee17']]`
  - `UNCONDITIONAL_JUMP` [`00bcee14`](#insn-00bcee14) → [`00bcf00c`](#insn-00bcf00c)
- ブロック [`00bcee18`](#insn-00bcee18) 範囲 `[['00bcee18', '00bcee27']]`
  - `CONDITIONAL_JUMP` [`00bcee24`](#insn-00bcee24) → [`00bceec4`](#insn-00bceec4)
  - `FALL_THROUGH` [`00bcee24`](#insn-00bcee24) → [`00bcee28`](#insn-00bcee28)
- ブロック [`00bcee28`](#insn-00bcee28) 範囲 `[['00bcee28', '00bcee2f']]`
  - `CONDITIONAL_JUMP` [`00bcee2c`](#insn-00bcee2c) → [`00bcef54`](#insn-00bcef54)
  - `FALL_THROUGH` [`00bcee2c`](#insn-00bcee2c) → [`00bcee30`](#insn-00bcee30)
- ブロック [`00bcee30`](#insn-00bcee30) 範囲 `[['00bcee30', '00bcee3b']]`
  - `CONDITIONAL_JUMP` [`00bcee38`](#insn-00bcee38) → [`00bcef54`](#insn-00bcef54)
  - `FALL_THROUGH` [`00bcee38`](#insn-00bcee38) → [`00bcee3c`](#insn-00bcee3c)
- ブロック [`00bcee3c`](#insn-00bcee3c) 範囲 `[['00bcee3c', '00bcee4b']]`
  - `CONDITIONAL_JUMP` [`00bcee48`](#insn-00bcee48) → [`00bcef54`](#insn-00bcef54)
  - `FALL_THROUGH` [`00bcee48`](#insn-00bcee48) → [`00bcee4c`](#insn-00bcee4c)
- ブロック [`00bcee4c`](#insn-00bcee4c) 範囲 `[['00bcee4c', '00bcee4f']]`
  - `FALL_THROUGH` [`00bcee4c`](#insn-00bcee4c) → [`00bcee50`](#insn-00bcee50)
- ブロック [`00bcee50`](#insn-00bcee50) 範囲 `[['00bcee50', '00bcee5b']]`
  - `CONDITIONAL_JUMP` [`00bcee58`](#insn-00bcee58) → [`00bcef54`](#insn-00bcef54)
  - `FALL_THROUGH` [`00bcee58`](#insn-00bcee58) → [`00bcee5c`](#insn-00bcee5c)
- ブロック [`00bcee5c`](#insn-00bcee5c) 範囲 `[['00bcee5c', '00bcee6b']]`
  - `FALL_THROUGH` [`00bcee68`](#insn-00bcee68) → [`00bcee6c`](#insn-00bcee6c)
- ブロック [`00bcee6c`](#insn-00bcee6c) 範囲 `[['00bcee6c', '00bcee6f']]`
  - `CONDITIONAL_JUMP` [`00bcee6c`](#insn-00bcee6c) → [`00bcef58`](#insn-00bcef58)
  - `FALL_THROUGH` [`00bcee6c`](#insn-00bcee6c) → [`00bcee70`](#insn-00bcee70)
- ブロック [`00bcee70`](#insn-00bcee70) 範囲 `[['00bcee70', '00bcee83']]`
  - `FALL_THROUGH` [`00bcee80`](#insn-00bcee80) → [`00bcee84`](#insn-00bcee84)
- ブロック [`00bcee84`](#insn-00bcee84) 範囲 `[['00bcee84', '00bcee8b']]`
  - `CONDITIONAL_JUMP` [`00bcee88`](#insn-00bcee88) → [`00bceea8`](#insn-00bceea8)
  - `FALL_THROUGH` [`00bcee88`](#insn-00bcee88) → [`00bcee8c`](#insn-00bcee8c)
- ブロック [`00bcee8c`](#insn-00bcee8c) 範囲 `[['00bcee8c', '00bcee97']]`
  - `CONDITIONAL_JUMP` [`00bcee94`](#insn-00bcee94) → [`00bcf018`](#insn-00bcf018)
  - `FALL_THROUGH` [`00bcee94`](#insn-00bcee94) → [`00bcee98`](#insn-00bcee98)
- ブロック [`00bcee98`](#insn-00bcee98) 範囲 `[['00bcee98', '00bceea7']]`
  - `FALL_THROUGH` [`00bceea4`](#insn-00bceea4) → [`00bceea8`](#insn-00bceea8)
- ブロック [`00bceea8`](#insn-00bceea8) 範囲 `[['00bceea8', '00bceec3']]`
  - `UNCONDITIONAL_JUMP` [`00bceec0`](#insn-00bceec0) → [`00bcef28`](#insn-00bcef28)
- ブロック [`00bceec4`](#insn-00bceec4) 範囲 `[['00bceec4', '00bceed7']]`
  - `CONDITIONAL_JUMP` [`00bceed4`](#insn-00bceed4) → [`00bcef58`](#insn-00bcef58)
  - `FALL_THROUGH` [`00bceed4`](#insn-00bceed4) → [`00bceed8`](#insn-00bceed8)
- ブロック [`00bceed8`](#insn-00bceed8) 範囲 `[['00bceed8', '00bceef3']]`
  - `CONDITIONAL_JUMP` [`00bceef0`](#insn-00bceef0) → [`00bcef10`](#insn-00bcef10)
  - `FALL_THROUGH` [`00bceef0`](#insn-00bceef0) → [`00bceef4`](#insn-00bceef4)
- ブロック [`00bceef4`](#insn-00bceef4) 範囲 `[['00bceef4', '00bceeff']]`
  - `CONDITIONAL_JUMP` [`00bceefc`](#insn-00bceefc) → [`00bcf018`](#insn-00bcf018)
  - `FALL_THROUGH` [`00bceefc`](#insn-00bceefc) → [`00bcef00`](#insn-00bcef00)
- ブロック [`00bcef00`](#insn-00bcef00) 範囲 `[['00bcef00', '00bcef0f']]`
  - `FALL_THROUGH` [`00bcef0c`](#insn-00bcef0c) → [`00bcef10`](#insn-00bcef10)
- ブロック [`00bcef10`](#insn-00bcef10) 範囲 `[['00bcef10', '00bcef27']]`
  - `FALL_THROUGH` [`00bcef24`](#insn-00bcef24) → [`00bcef28`](#insn-00bcef28)
- ブロック [`00bcef28`](#insn-00bcef28) 範囲 `[['00bcef28', '00bcef4b']]`
  - `UNCONDITIONAL_JUMP` [`00bcef48`](#insn-00bcef48) → [`00bcef58`](#insn-00bcef58)
- ブロック [`00bcef4c`](#insn-00bcef4c) 範囲 `[['00bcef4c', '00bcef53']]`
  - `CONDITIONAL_JUMP` [`00bcef50`](#insn-00bcef50) → [`00bcef70`](#insn-00bcef70)
  - `FALL_THROUGH` [`00bcef50`](#insn-00bcef50) → [`00bcef54`](#insn-00bcef54)
- ブロック [`00bcef54`](#insn-00bcef54) 範囲 `[['00bcef54', '00bcef57']]`
  - `FALL_THROUGH` [`00bcef54`](#insn-00bcef54) → [`00bcef58`](#insn-00bcef58)
- ブロック [`00bcef58`](#insn-00bcef58) 範囲 `[['00bcef58', '00bcef6f']]`
- ブロック [`00bcef70`](#insn-00bcef70) 範囲 `[['00bcef70', '00bcef77']]`
  - `CONDITIONAL_JUMP` [`00bcef74`](#insn-00bcef74) → [`00bcef80`](#insn-00bcef80)
  - `FALL_THROUGH` [`00bcef74`](#insn-00bcef74) → [`00bcef78`](#insn-00bcef78)
- ブロック [`00bcef78`](#insn-00bcef78) 範囲 `[['00bcef78', '00bcef7f']]`
  - `CONDITIONAL_JUMP` [`00bcef7c`](#insn-00bcef7c) → [`00bcef54`](#insn-00bcef54)
  - `FALL_THROUGH` [`00bcef7c`](#insn-00bcef7c) → [`00bcef80`](#insn-00bcef80)
- ブロック [`00bcef80`](#insn-00bcef80) 範囲 `[['00bcef80', '00bcef83']]`
  - `FALL_THROUGH` [`00bcef80`](#insn-00bcef80) → [`00bcef84`](#insn-00bcef84)
- ブロック [`00bcef84`](#insn-00bcef84) 範囲 `[['00bcef84', '00bcefab']]`
  - `CONDITIONAL_JUMP` [`00bcefa8`](#insn-00bcefa8) → [`00bcefc8`](#insn-00bcefc8)
  - `FALL_THROUGH` [`00bcefa8`](#insn-00bcefa8) → [`00bcefac`](#insn-00bcefac)
- ブロック [`00bcefac`](#insn-00bcefac) 範囲 `[['00bcefac', '00bcefb7']]`
  - `CONDITIONAL_JUMP` [`00bcefb4`](#insn-00bcefb4) → [`00bcf018`](#insn-00bcf018)
  - `FALL_THROUGH` [`00bcefb4`](#insn-00bcefb4) → [`00bcefb8`](#insn-00bcefb8)
- ブロック [`00bcefb8`](#insn-00bcefb8) 範囲 `[['00bcefb8', '00bcefbb']]`
  - `FALL_THROUGH` [`00bcefb8`](#insn-00bcefb8) → [`00bcefbc`](#insn-00bcefbc)
- ブロック [`00bcefbc`](#insn-00bcefbc) 範囲 `[['00bcefbc', '00bcefc7']]`
  - `FALL_THROUGH` [`00bcefc4`](#insn-00bcefc4) → [`00bcefc8`](#insn-00bcefc8)
- ブロック [`00bcefc8`](#insn-00bcefc8) 範囲 `[['00bcefc8', '00bcefd7']]`
  - `FALL_THROUGH` [`00bcefd4`](#insn-00bcefd4) → [`00bcefd8`](#insn-00bcefd8)
- ブロック [`00bcefd8`](#insn-00bcefd8) 範囲 `[['00bcefd8', '00bcefef']]`
  - `FALL_THROUGH` [`00bcefec`](#insn-00bcefec) → [`00bceff0`](#insn-00bceff0)
- ブロック [`00bceff0`](#insn-00bceff0) 範囲 `[['00bceff0', '00bcf003']]`
  - `UNCONDITIONAL_JUMP` [`00bcf000`](#insn-00bcf000) → [`00bcef58`](#insn-00bcef58)
- ブロック [`00bcf004`](#insn-00bcf004) 範囲 `[['00bcf004', '00bcf00b']]`
  - `FALL_THROUGH` [`00bcf008`](#insn-00bcf008) → [`00bcf00c`](#insn-00bcf00c)
- ブロック [`00bcf00c`](#insn-00bcf00c) 範囲 `[['00bcf00c', '00bcf017']]`
  - `UNCONDITIONAL_JUMP` [`00bcf014`](#insn-00bcf014) → [`00bcef58`](#insn-00bcef58)
- ブロック [`00bcf018`](#insn-00bcf018) 範囲 `[['00bcf018', '00bcf01b']]`

## 命令位置別の参照

- [`00bcecac`](#insn-00bcecac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecb0`](#insn-00bcecb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecb4`](#insn-00bcecb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecb8`](#insn-00bcecb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceccc`](#insn-00bceccc) → [`00bcee28`](#insn-00bcee28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcece4`](#insn-00bcece4) → [`00bcecf4`](#insn-00bcecf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf0`](#insn-00bcecf0) → [`00bced38`](#insn-00bced38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced00`](#insn-00bced00) → `00c17b68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced08`](#insn-00bced08) → [`00bcece8`](#insn-00bcece8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced0c`](#insn-00bced0c) → [`00bced30`](#insn-00bced30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced10`](#insn-00bced10) → `00c17b69`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced2c`](#insn-00bced2c) → [`00bcecec`](#insn-00bcecec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced34`](#insn-00bced34) → [`00bcecec`](#insn-00bcecec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced3c`](#insn-00bced3c) → `00c17b78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced44`](#insn-00bced44) → [`00bcee18`](#insn-00bcee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced48`](#insn-00bced48) → `00c17b79`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced54`](#insn-00bced54) → [`00bcee18`](#insn-00bcee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced58`](#insn-00bced58) → `00c17b7a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced68`](#insn-00bced68) → [`00bcef4c`](#insn-00bcef4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced8c`](#insn-00bced8c) → [`00bbde18`](../00bbd/00bbde18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde18` · 推定シンボル `None` · 推定型 `None`
- [`00bced94`](#insn-00bced94) → [`00bcf004`](#insn-00bcf004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced9c`](#insn-00bced9c) → [`00bceda8`](#insn-00bceda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedb8`](#insn-00bcedb8) → [`00bceddc`](#insn-00bceddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedc0`](#insn-00bcedc0) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bcedc4`](#insn-00bcedc4) → [`00bcf018`](#insn-00bcf018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedf4`](#insn-00bcedf4) → `00c19128`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcee14`](#insn-00bcee14) → [`00bcf00c`](#insn-00bcf00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee24`](#insn-00bcee24) → [`00bceec4`](#insn-00bceec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee2c`](#insn-00bcee2c) → [`00bcef54`](#insn-00bcef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee38`](#insn-00bcee38) → [`00bcef54`](#insn-00bcef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee48`](#insn-00bcee48) → [`00bcef54`](#insn-00bcef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee58`](#insn-00bcee58) → [`00bcef54`](#insn-00bcef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee68`](#insn-00bcee68) → [`00bc10fc`](../00bc1/00bc10fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc10fc` · 推定シンボル `None` · 推定型 `None`
- [`00bcee6c`](#insn-00bcee6c) → [`00bcef58`](#insn-00bcef58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee88`](#insn-00bcee88) → [`00bceea8`](#insn-00bceea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee90`](#insn-00bcee90) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bcee94`](#insn-00bcee94) → [`00bcf018`](#insn-00bcf018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceec0`](#insn-00bceec0) → [`00bcef28`](#insn-00bcef28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceed0`](#insn-00bceed0) → [`00bc10fc`](../00bc1/00bc10fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc10fc` · 推定シンボル `None` · 推定型 `None`
- [`00bceed4`](#insn-00bceed4) → [`00bcef58`](#insn-00bcef58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceef0`](#insn-00bceef0) → [`00bcef10`](#insn-00bcef10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceef8`](#insn-00bceef8) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bceefc`](#insn-00bceefc) → [`00bcf018`](#insn-00bcf018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef28`](#insn-00bcef28) → `00c19128`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcef28`](#insn-00bcef28) → `00c19198`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcef48`](#insn-00bcef48) → [`00bcef58`](#insn-00bcef58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef50`](#insn-00bcef50) → [`00bcef70`](#insn-00bcef70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef58`](#insn-00bcef58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef5c`](#insn-00bcef5c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef60`](#insn-00bcef60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef64`](#insn-00bcef64) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef74`](#insn-00bcef74) → [`00bcef80`](#insn-00bcef80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef78`](#insn-00bcef78) → `00c17b7b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcef7c`](#insn-00bcef7c) → [`00bcef54`](#insn-00bcef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef80`](#insn-00bcef80) → `00c17b80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcef88`](#insn-00bcef88) → `002b09e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcef8c`](#insn-00bcef8c) → [`00bdb140`](../00bdb/00bdb140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb140` · 推定シンボル `None` · 推定型 `None`
- [`00bcefa8`](#insn-00bcefa8) → [`00bcefc8`](#insn-00bcefc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefb0`](#insn-00bcefb0) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bcefb4`](#insn-00bcefb4) → [`00bcf018`](#insn-00bcf018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefe0`](#insn-00bcefe0) → `00c17848`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcefec`](#insn-00bcefec) → `002b09e1`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf000`](#insn-00bcf000) → [`00bcef58`](#insn-00bcef58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf014`](#insn-00bcf014) → [`00bcef58`](#insn-00bcef58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf018`](#insn-00bcf018) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcecac`](#insn-00bcecac)

~~~json
{
  "source": "00bcecac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecb0`](#insn-00bcecb0)

~~~json
{
  "source": "00bcecb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecb4`](#insn-00bcecb4)

~~~json
{
  "source": "00bcecb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecb8`](#insn-00bcecb8)

~~~json
{
  "source": "00bcecb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceccc`](#insn-00bceccc)

~~~json
{
  "source": "00bceccc",
  "target": "00bcee28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcece4`](#insn-00bcece4)

~~~json
{
  "source": "00bcece4",
  "target": "00bcecf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecf0`](#insn-00bcecf0)

~~~json
{
  "source": "00bcecf0",
  "target": "00bced38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced00`](#insn-00bced00)

~~~json
{
  "source": "00bced00",
  "target": "00c17b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17b68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6c",
  "capture_start": "00c17b68",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced08`](#insn-00bced08)

~~~json
{
  "source": "00bced08",
  "target": "00bcece8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced0c`](#insn-00bced0c)

~~~json
{
  "source": "00bced0c",
  "target": "00bced30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced10`](#insn-00bced10)

~~~json
{
  "source": "00bced10",
  "target": "00c17b69",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17b69",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "74",
  "capture_start": "00c17b69",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced2c`](#insn-00bced2c)

~~~json
{
  "source": "00bced2c",
  "target": "00bcecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced34`](#insn-00bced34)

~~~json
{
  "source": "00bced34",
  "target": "00bcecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced3c`](#insn-00bced3c)

~~~json
{
  "source": "00bced3c",
  "target": "00c17b78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17b78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6d",
  "capture_start": "00c17b78",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced44`](#insn-00bced44)

~~~json
{
  "source": "00bced44",
  "target": "00bcee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced48`](#insn-00bced48)

~~~json
{
  "source": "00bced48",
  "target": "00c17b79",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17b79",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "49",
  "capture_start": "00c17b79",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced54`](#insn-00bced54)

~~~json
{
  "source": "00bced54",
  "target": "00bcee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced58`](#insn-00bced58)

~~~json
{
  "source": "00bced58",
  "target": "00c17b7a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17b7a",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "02",
  "capture_start": "00c17b7a",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced68`](#insn-00bced68)

~~~json
{
  "source": "00bced68",
  "target": "00bcef4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced8c`](#insn-00bced8c)

~~~json
{
  "source": "00bced8c",
  "target": "00bbde18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bced94`](#insn-00bced94)

~~~json
{
  "source": "00bced94",
  "target": "00bcf004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced9c`](#insn-00bced9c)

~~~json
{
  "source": "00bced9c",
  "target": "00bceda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedb8`](#insn-00bcedb8)

~~~json
{
  "source": "00bcedb8",
  "target": "00bceddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedc0`](#insn-00bcedc0)

~~~json
{
  "source": "00bcedc0",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedc4`](#insn-00bcedc4)

~~~json
{
  "source": "00bcedc4",
  "target": "00bcf018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedf4`](#insn-00bcedf4)

~~~json
{
  "source": "00bcedf4",
  "target": "00c19128",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19128",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcee14`](#insn-00bcee14)

~~~json
{
  "source": "00bcee14",
  "target": "00bcf00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee24`](#insn-00bcee24)

~~~json
{
  "source": "00bcee24",
  "target": "00bceec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee2c`](#insn-00bcee2c)

~~~json
{
  "source": "00bcee2c",
  "target": "00bcef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee38`](#insn-00bcee38)

~~~json
{
  "source": "00bcee38",
  "target": "00bcef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee48`](#insn-00bcee48)

~~~json
{
  "source": "00bcee48",
  "target": "00bcef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee58`](#insn-00bcee58)

~~~json
{
  "source": "00bcee58",
  "target": "00bcef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee68`](#insn-00bcee68)

~~~json
{
  "source": "00bcee68",
  "target": "00bc10fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee6c`](#insn-00bcee6c)

~~~json
{
  "source": "00bcee6c",
  "target": "00bcef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee88`](#insn-00bcee88)

~~~json
{
  "source": "00bcee88",
  "target": "00bceea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee90`](#insn-00bcee90)

~~~json
{
  "source": "00bcee90",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee94`](#insn-00bcee94)

~~~json
{
  "source": "00bcee94",
  "target": "00bcf018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceec0`](#insn-00bceec0)

~~~json
{
  "source": "00bceec0",
  "target": "00bcef28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceed0`](#insn-00bceed0)

~~~json
{
  "source": "00bceed0",
  "target": "00bc10fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceed4`](#insn-00bceed4)

~~~json
{
  "source": "00bceed4",
  "target": "00bcef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceef0`](#insn-00bceef0)

~~~json
{
  "source": "00bceef0",
  "target": "00bcef10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceef8`](#insn-00bceef8)

~~~json
{
  "source": "00bceef8",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceefc`](#insn-00bceefc)

~~~json
{
  "source": "00bceefc",
  "target": "00bcf018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef28`](#insn-00bcef28)

~~~json
{
  "source": "00bcef28",
  "target": "00c19128",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19128",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcef28`](#insn-00bcef28)

~~~json
{
  "source": "00bcef28",
  "target": "00c19198",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19198",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcef48`](#insn-00bcef48)

~~~json
{
  "source": "00bcef48",
  "target": "00bcef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef50`](#insn-00bcef50)

~~~json
{
  "source": "00bcef50",
  "target": "00bcef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef58`](#insn-00bcef58)

~~~json
{
  "source": "00bcef58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef5c`](#insn-00bcef5c)

~~~json
{
  "source": "00bcef5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef60`](#insn-00bcef60)

~~~json
{
  "source": "00bcef60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef64`](#insn-00bcef64)

~~~json
{
  "source": "00bcef64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef74`](#insn-00bcef74)

~~~json
{
  "source": "00bcef74",
  "target": "00bcef80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef78`](#insn-00bcef78)

~~~json
{
  "source": "00bcef78",
  "target": "00c17b7b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17b7b",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "22",
  "capture_start": "00c17b7b",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcef7c`](#insn-00bcef7c)

~~~json
{
  "source": "00bcef7c",
  "target": "00bcef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef80`](#insn-00bcef80)

~~~json
{
  "source": "00bcef80",
  "target": "00c17b80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17b80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcef88`](#insn-00bcef88)

~~~json
{
  "source": "00bcef88",
  "target": "002b09e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b09e1",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6f70657261746f722d3d00",
  "capture_start": "002b09e1",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcef8c`](#insn-00bcef8c)

~~~json
{
  "source": "00bcef8c",
  "target": "00bdb140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcefa8`](#insn-00bcefa8)

~~~json
{
  "source": "00bcefa8",
  "target": "00bcefc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefb0`](#insn-00bcefb0)

~~~json
{
  "source": "00bcefb0",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcefb4`](#insn-00bcefb4)

~~~json
{
  "source": "00bcefb4",
  "target": "00bcf018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefe0`](#insn-00bcefe0)

~~~json
{
  "source": "00bcefe0",
  "target": "00c17848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17848",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcefec`](#insn-00bcefec)

~~~json
{
  "source": "00bcefec",
  "target": "002b09e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b09e1",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6f70657261746f722d3d00",
  "capture_start": "002b09e1",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf000`](#insn-00bcf000)

~~~json
{
  "source": "00bcf000",
  "target": "00bcef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf014`](#insn-00bcf014)

~~~json
{
  "source": "00bcf014",
  "target": "00bcef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf018`](#insn-00bcf018)

~~~json
{
  "source": "00bcf018",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
