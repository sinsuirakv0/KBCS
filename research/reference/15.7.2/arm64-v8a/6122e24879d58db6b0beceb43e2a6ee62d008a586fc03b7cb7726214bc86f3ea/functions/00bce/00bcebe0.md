# 00bcebe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bceca8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-eb9deee7dd31c5e95ea23debebd46841)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcebe0",
  "name": "FUN_00bcebe0",
  "size": 884,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2072be5ac59a5e4e1007139d6bfb18453ccaf0f565976b22b154e40c0c807590",
  "source_text_sha256": "2072be5ac59a5e4e1007139d6bfb18453ccaf0f565976b22b154e40c0c807590",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcebe0",
        "00bcef53"
      ]
    ],
    "bytes_sha256": "3f3bd48795b7c918275e9f1d51dbbedd368447146b628a4425e40ec945c4d042",
    "instruction_count": 221,
    "instruction_bytes": 884,
    "body_bytes": 884,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc2394](../00bc2/00bc2394.md)
- [00bce830](../00bce/00bce830.md)

## 呼び出し先

- [00bbdd50](../00bbd/00bbdd50.md)
- [00bc1034](../00bc1/00bc1034.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

## 関連文字列（未確認候補）

~~~text
"operator-="
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7460 bytes

~~~c

undefined8 * FUN_00bcebe0(long *param_1,undefined1 *param_2)

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
      if ((byte)(&UNK_00c178d8)[uVar16 * 0x10] < bVar4) {
        uVar14 = uVar16 + 1;
        uVar16 = uVar15;
      }
      else {
                    /* try { // try from 00bcec54 to 00ccec5f has its CatchHandler @ 00bcf270 */
        if (((&UNK_00c178d8)[uVar16 * 0x10] == bVar4) &&
           ((byte)(&UNK_00c178d9)[uVar16 * 0x10] < pbVar2[1])) {
          uVar14 = uVar16 + 1;
          uVar16 = uVar15;
        }
      }
      uVar15 = uVar16;
    } while (uVar16 != uVar14);
    lVar11 = uVar14 * 0x10;
                    /* try { // try from 00bcec7c to 00ccec8b has its CatchHandler @ 00bcf26c */
                    /* try { // try from 00bcec8c to 00ccec97 has its CatchHandler @ 00bcf258 */
    if (((&UNK_00c178d8)[lVar11] == bVar4) && ((&UNK_00c178d9)[lVar11] == pbVar2[1])) {
      bVar4 = (&UNK_00c178da)[lVar11];
                    /* try { // try from 00bcec98 to 00ccecab has its CatchHandler @ 00bcf248 */
      *param_1 = (long)(pbVar2 + 2);
      if (bVar4 == 8) {
        uVar5 = *(undefined1 *)((long)param_1 + 0x309);
                    /* try { // try from 00bcecac to 00ccecb7 has its CatchHandler @ 00bcf218 */
        lVar11 = param_1[0x61];
        *(undefined1 *)(param_1 + 0x61) = 0;
        uVar12 = uVar5;
                    /* try { // try from 00bcecb8 to 00ccecc7 has its CatchHandler @ 00bcf1f8 */
        if (param_2 != (undefined1 *)0x0) {
          uVar12 = 1;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar12;
        lVar6 = FUN_00bbdd50();
                    /* try { // try from 00bcecc8 to 00ccecdf has its CatchHandler @ 00bcf1b4 */
        if (lVar6 == 0) {
          puVar8 = (undefined8 *)0x0;
        }
        else {
          if (param_2 != (undefined1 *)0x0) {
            *param_2 = 1;
          }
                    /* try { // try from 00bcece0 to 00cced47 has its CatchHandler @ 00bce4cc */
          pvVar17 = (void *)param_1[0x266];
          lVar13 = *(long *)((long)pvVar17 + 8);
          puVar7 = pvVar17;
          if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
            puVar7 = malloc(0x1000);
            if (puVar7 == (void *)0x0) goto LAB_00bcef50;
            lVar13 = 0;
            *puVar7 = pvVar17;
            puVar7[1] = 0;
            param_1[0x266] = (long)puVar7;
          }
          *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
          puVar8 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
          *puVar8 = &PTR_FUN_00c19078;
          *(long *)((long)puVar7 + lVar13 + 0x20) = lVar6;
          *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 4;
                    /* try { // try from 00bced48 to 00cced87 has its CatchHandler @ 00bcf2fc */
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
      if ((bVar4 == 4) && (((&UNK_00c178db)[lVar11] & 1) == 0)) {
        return (undefined8 *)0x0;
      }
      __s = *(char **)(&UNK_00c178e0 + lVar11);
                    /* try { // try from 00bceebc to 00cceef3 has its CatchHandler @ 00bcf148 */
      sVar9 = strlen(__s);
      pvVar17 = (void *)param_1[0x266];
      lVar11 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (0xfffffffffffff00f < lVar11 - 0xfd0U) {
LAB_00bcef00:
                    /* try { // try from 00bcef00 to 00ccef0f has its CatchHandler @ 00bcf140 */
                    /* try { // try from 00bcef10 to 00ccef27 has its CatchHandler @ 00bcf13c */
        *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
        puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
        *puVar7 = &PTR_FUN_00c17798;
        *(char **)((long)puVar8 + lVar11 + 0x20) = __s;
        *(size_t *)((long)puVar8 + lVar11 + 0x28) = sVar9;
                    /* try { // try from 00bcef28 to 00ccf35f has its CatchHandler @ 00bce4cc */
        *(undefined1 *)((long)puVar8 + lVar11 + 0x18) = 8;
        *(ushort *)((long)puVar8 + lVar11 + 0x19) =
             *(ushort *)((long)puVar8 + lVar11 + 0x19) & 0xf000 | 0x540;
        return puVar7;
      }
      puVar8 = malloc(0x1000);
      if (puVar8 != (void *)0x0) {
        lVar11 = 0;
                    /* try { // try from 00bceef4 to 00cceeff has its CatchHandler @ 00bcf144 */
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
        goto LAB_00bcef00;
      }
      goto LAB_00bcef50;
    }
    if (*(short *)pbVar2 == 0x696c) {
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1034();
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00bcef50;
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c190e8;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 0x14;
      goto LAB_00bcee60;
    }
  }
  if ((pbVar2 != pbVar3) && (*pbVar2 == 0x76)) {
    pbVar1 = pbVar2 + 1;
    *param_1 = (long)pbVar1;
                    /* try { // try from 00bced88 to 00cced93 has its CatchHandler @ 00bcf1a0 */
    if ((pbVar3 != pbVar1) && (*pbVar1 - 0x30 < 10)) {
                    /* try { // try from 00bced94 to 00cceda3 has its CatchHandler @ 00bcf180 */
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1034();
                    /* try { // try from 00bceda4 to 00ccedbb has its CatchHandler @ 00bcf14c */
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
                    /* try { // try from 00bcedbc to 00cceebb has its CatchHandler @ 00bce4cc */
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00bcef50:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c19078;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 4;
LAB_00bcee60:
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
<a id="insn-00bcebe0"></a> `00bcebe0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcebe4"></a> `00bcebe4` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bcebe8"></a> `00bcebe8` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcebec"></a> `00bcebec` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcebf0"></a> `00bcebf0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcebf4"></a> `00bcebf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcebf8"></a> `00bcebf8` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bcebfc"></a> `00bcebfc` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00bcec00"></a> `00bcec00` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bcec04"></a> `00bcec04` | `e3 0a 00 54` | b.cc 0x00bced60 | `CONDITIONAL_JUMP`
<a id="insn-00bcec08"></a> `00bcec08` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcec0c"></a> `00bcec0c` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00bcec10"></a> `00bcec10` | `ad 07 80 52` | mov w13,#0x3d | `FALL_THROUGH`
<a id="insn-00bcec14"></a> `00bcec14` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bcec18"></a> `00bcec18` | `0c 66 24 10` | adr x12,0xc178d8 | `FALL_THROUGH`
<a id="insn-00bcec1c"></a> `00bcec1c` | `04 00 00 14` | b 0x00bcec2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcec20"></a> `00bcec20` | `cb 05 00 91` | add x11,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bcec24"></a> `00bcec24` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bcec28"></a> `00bcec28` | `40 02 00 54` | b.eq 0x00bcec70 | `CONDITIONAL_JUMP`
<a id="insn-00bcec2c"></a> `00bcec2c` | `6e 01 0d 8b` | add x14,x11,x13 | `FALL_THROUGH`
<a id="insn-00bcec30"></a> `00bcec30` | `ce fd 41 d3` | lsr x14,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bcec34"></a> `00bcec34` | `8f 11 0e 8b` | add x15,x12,x14, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bcec38"></a> `00bcec38` | `f0 01 40 39` | ldrb w16,[x15] | `FALL_THROUGH`
<a id="insn-00bcec3c"></a> `00bcec3c` | `1f 02 0a 6b` | cmp w16,w10 | `FALL_THROUGH`
<a id="insn-00bcec40"></a> `00bcec40` | `03 ff ff 54` | b.cc 0x00bcec20 | `CONDITIONAL_JUMP`
<a id="insn-00bcec44"></a> `00bcec44` | `21 01 00 54` | b.ne 0x00bcec68 | `CONDITIONAL_JUMP`
<a id="insn-00bcec48"></a> `00bcec48` | `ef 05 40 39` | ldrb w15,[x15, #0x1] | `FALL_THROUGH`
<a id="insn-00bcec4c"></a> `00bcec4c` | `10 05 40 39` | ldrb w16,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bcec50"></a> `00bcec50` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00bcec54"></a> `00bcec54` | `ef 27 9f 1a` | cset w15,cc | `FALL_THROUGH`
<a id="insn-00bcec58"></a> `00bcec58` | `ff 01 00 72` | tst w15,#0x1 | `FALL_THROUGH`
<a id="insn-00bcec5c"></a> `00bcec5c` | `6b 05 8e 9a` | csinc x11,x11,x14,eq | `FALL_THROUGH`
<a id="insn-00bcec60"></a> `00bcec60` | `ad 11 8e 9a` | csel x13,x13,x14,ne | `FALL_THROUGH`
<a id="insn-00bcec64"></a> `00bcec64` | `f0 ff ff 17` | b 0x00bcec24 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcec68"></a> `00bcec68` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bcec6c"></a> `00bcec6c` | `ee ff ff 17` | b 0x00bcec24 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcec70"></a> `00bcec70` | `8b 11 0b 8b` | add x11,x12,x11, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bcec74"></a> `00bcec74` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-00bcec78"></a> `00bcec78` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00bcec7c"></a> `00bcec7c` | `a1 06 00 54` | b.ne 0x00bced50 | `CONDITIONAL_JUMP`
<a id="insn-00bcec80"></a> `00bcec80` | `6a 05 40 39` | ldrb w10,[x11, #0x1] | `FALL_THROUGH`
<a id="insn-00bcec84"></a> `00bcec84` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bcec88"></a> `00bcec88` | `5f 01 0c 6b` | cmp w10,w12 | `FALL_THROUGH`
<a id="insn-00bcec8c"></a> `00bcec8c` | `21 06 00 54` | b.ne 0x00bced50 | `CONDITIONAL_JUMP`
<a id="insn-00bcec90"></a> `00bcec90` | `69 09 40 39` | ldrb w9,[x11, #0x2] | `FALL_THROUGH`
<a id="insn-00bcec94"></a> `00bcec94` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcec98"></a> `00bcec98` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcec9c"></a> `00bcec9c` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bceca0"></a> `00bceca0` | `21 0f 00 54` | b.ne 0x00bcee84 | `CONDITIONAL_JUMP`
<a id="insn-00bceca4"></a> `00bceca4` | `14 24 4c 39` | ldrb w20,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00bceca8"></a> `00bceca8` | `3f 00 00 f1` | cmp x1,#0x0 | `FALL_THROUGH`
<a id="insn-00bcecac"></a> `00bcecac` | `15 20 4c 39` | ldrb w21,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00bcecb0"></a> `00bcecb0` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcecb4"></a> `00bcecb4` | `1f 20 0c 39` | strb wzr,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00bcecb8"></a> `00bcecb8` | `88 06 9f 1a` | csinc w8,w20,wzr,eq | `FALL_THROUGH`
<a id="insn-00bcecbc"></a> `00bcecbc` | `08 24 0c 39` | strb w8,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00bcecc0"></a> `00bcecc0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcecc4"></a> `00bcecc4` | `23 bc ff 97` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecc8"></a> `00bcecc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bceccc"></a> `00bceccc` | `80 13 00 b4` | cbz x0,0x00bcef3c | `CONDITIONAL_JUMP`
<a id="insn-00bcecd0"></a> `00bcecd0` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcecd4"></a> `00bcecd4` | `77 00 00 b4` | cbz x23,0x00bcece0 | `CONDITIONAL_JUMP`
<a id="insn-00bcecd8"></a> `00bcecd8` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcecdc"></a> `00bcecdc` | `e9 02 00 39` | strb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bcece0"></a> `00bcece0` | `17 99 49 f9` | ldr x23,[x8, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcece4"></a> `00bcece4` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bcece8"></a> `00bcece8` | `2a 41 3f d1` | sub x10,x9,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcecec"></a> `00bcecec` | `5f c5 3f b1` | cmn x10,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcecf0"></a> `00bcecf0` | `28 01 00 54` | b.hi 0x00bced14 | `CONDITIONAL_JUMP`
<a id="insn-00bcecf4"></a> `00bcecf4` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcecf8"></a> `00bcecf8` | `f6 38 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecfc"></a> `00bcecfc` | `a0 12 00 b4` | cbz x0,0x00bcef50 | `CONDITIONAL_JUMP`
<a id="insn-00bced00"></a> `00bced00` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bced04"></a> `00bced04` | `17 7c 00 a9` | stp x23,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bced08"></a> `00bced08` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bced0c"></a> `00bced0c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bced10"></a> `00bced10` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00bced14"></a> `00bced14` | `2a 81 00 91` | add x10,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00bced18"></a> `00bced18` | `e0 02 09 8b` | add x0,x23,x9 | `FALL_THROUGH`
<a id="insn-00bced1c"></a> `00bced1c` | `49 02 00 f0` | adrp x9,0xc19000 | `FALL_THROUGH`
<a id="insn-00bced20"></a> `00bced20` | `29 e1 01 91` | add x9,x9,#0x78 | `FALL_THROUGH`
<a id="insn-00bced24"></a> `00bced24` | `ea 06 00 f9` | str x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bced28"></a> `00bced28` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00bced2c"></a> `00bced2c` | `09 0c 01 f8` | str x9,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bced30"></a> `00bced30` | `09 90 40 78` | ldurh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bced34"></a> `00bced34` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00bced38"></a> `00bced38` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bced3c"></a> `00bced3c` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bced40"></a> `00bced40` | `0a 20 00 39` | strb w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bced44"></a> `00bced44` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00bced48"></a> `00bced48` | `09 90 00 78` | sturh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bced4c"></a> `00bced4c` | `7e 00 00 14` | b 0x00bcef44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bced50"></a> `00bced50` | `0a 01 40 79` | ldrh w10,[x8] | `FALL_THROUGH`
<a id="insn-00bced54"></a> `00bced54` | `8b 2d 8d 52` | mov w11,#0x696c | `FALL_THROUGH`
<a id="insn-00bced58"></a> `00bced58` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00bced5c"></a> `00bced5c` | `00 05 00 54` | b.eq 0x00bcedfc | `CONDITIONAL_JUMP`
<a id="insn-00bced60"></a> `00bced60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bced64"></a> `00bced64` | `40 09 00 54` | b.eq 0x00bcee8c | `CONDITIONAL_JUMP`
<a id="insn-00bced68"></a> `00bced68` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bced6c"></a> `00bced6c` | `5f d9 01 71` | cmp w10,#0x76 | `FALL_THROUGH`
<a id="insn-00bced70"></a> `00bced70` | `e1 08 00 54` | b.ne 0x00bcee8c | `CONDITIONAL_JUMP`
<a id="insn-00bced74"></a> `00bced74` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bced78"></a> `00bced78` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bced7c"></a> `00bced7c` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bced80"></a> `00bced80` | `60 08 00 54` | b.eq 0x00bcee8c | `CONDITIONAL_JUMP`
<a id="insn-00bced84"></a> `00bced84` | `49 01 40 39` | ldrb w9,[x10] | `FALL_THROUGH`
<a id="insn-00bced88"></a> `00bced88` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bced8c"></a> `00bced8c` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bced90"></a> `00bced90` | `e8 07 00 54` | b.hi 0x00bcee8c | `CONDITIONAL_JUMP`
<a id="insn-00bced94"></a> `00bced94` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bced98"></a> `00bced98` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bced9c"></a> `00bced9c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bceda0"></a> `00bceda0` | `a5 c8 ff 97` | bl 0x00bc1034 | `UNCONDITIONAL_CALL`
<a id="insn-00bceda4"></a> `00bceda4` | `60 07 00 b4` | cbz x0,0x00bcee90 | `CONDITIONAL_JUMP`
<a id="insn-00bceda8"></a> `00bceda8` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcedac"></a> `00bcedac` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bcedb0"></a> `00bcedb0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcedb4"></a> `00bcedb4` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcedb8"></a> `00bcedb8` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcedbc"></a> `00bcedbc` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcedc0"></a> `00bcedc0` | `08 01 00 54` | b.hi 0x00bcede0 | `CONDITIONAL_JUMP`
<a id="insn-00bcedc4"></a> `00bcedc4` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcedc8"></a> `00bcedc8` | `c2 38 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcedcc"></a> `00bcedcc` | `20 0c 00 b4` | cbz x0,0x00bcef50 | `CONDITIONAL_JUMP`
<a id="insn-00bcedd0"></a> `00bcedd0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcedd4"></a> `00bcedd4` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcedd8"></a> `00bcedd8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bceddc"></a> `00bceddc` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcede0"></a> `00bcede0` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcede4"></a> `00bcede4` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bcede8"></a> `00bcede8` | `48 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bcedec"></a> `00bcedec` | `08 e1 01 91` | add x8,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00bcedf0"></a> `00bcedf0` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcedf4"></a> `00bcedf4` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bcedf8"></a> `00bcedf8` | `1a 00 00 14` | b 0x00bcee60 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcedfc"></a> `00bcedfc` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcee00"></a> `00bcee00` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcee04"></a> `00bcee04` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcee08"></a> `00bcee08` | `8b c8 ff 97` | bl 0x00bc1034 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee0c"></a> `00bcee0c` | `20 04 00 b4` | cbz x0,0x00bcee90 | `CONDITIONAL_JUMP`
<a id="insn-00bcee10"></a> `00bcee10` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcee14"></a> `00bcee14` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bcee18"></a> `00bcee18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcee1c"></a> `00bcee1c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee20"></a> `00bcee20` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcee24"></a> `00bcee24` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcee28"></a> `00bcee28` | `08 01 00 54` | b.hi 0x00bcee48 | `CONDITIONAL_JUMP`
<a id="insn-00bcee2c"></a> `00bcee2c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcee30"></a> `00bcee30` | `a8 38 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee34"></a> `00bcee34` | `e0 08 00 b4` | cbz x0,0x00bcef50 | `CONDITIONAL_JUMP`
<a id="insn-00bcee38"></a> `00bcee38` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcee3c"></a> `00bcee3c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcee40"></a> `00bcee40` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcee44"></a> `00bcee44` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcee48"></a> `00bcee48` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcee4c"></a> `00bcee4c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bcee50"></a> `00bcee50` | `48 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bcee54"></a> `00bcee54` | `08 a1 03 91` | add x8,x8,#0xe8 | `FALL_THROUGH`
<a id="insn-00bcee58"></a> `00bcee58` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee5c"></a> `00bcee5c` | `89 02 80 52` | mov w9,#0x14 | `FALL_THROUGH`
<a id="insn-00bcee60"></a> `00bcee60` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcee64"></a> `00bcee64` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcee68"></a> `00bcee68` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bcee6c"></a> `00bcee6c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcee70"></a> `00bcee70` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee74"></a> `00bcee74` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bcee78"></a> `00bcee78` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcee7c"></a> `00bcee7c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcee80"></a> `00bcee80` | `04 00 00 14` | b 0x00bcee90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcee84"></a> `00bcee84` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00bcee88"></a> `00bcee88` | `09 01 00 54` | b.ls 0x00bceea8 | `CONDITIONAL_JUMP`
<a id="insn-00bcee8c"></a> `00bcee8c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bcee90"></a> `00bcee90` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcee94"></a> `00bcee94` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcee98"></a> `00bcee98` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcee9c"></a> `00bcee9c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bceea0"></a> `00bceea0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bceea4"></a> `00bceea4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bceea8"></a> `00bceea8` | `3f 11 00 71` | cmp w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bceeac"></a> `00bceeac` | `61 00 00 54` | b.ne 0x00bceeb8 | `CONDITIONAL_JUMP`
<a id="insn-00bceeb0"></a> `00bceeb0` | `68 0d 40 39` | ldrb w8,[x11, #0x3] | `FALL_THROUGH`
<a id="insn-00bceeb4"></a> `00bceeb4` | `c8 fe 07 36` | tbz w8,#0x0,0x00bcee8c | `CONDITIONAL_JUMP`
<a id="insn-00bceeb8"></a> `00bceeb8` | `73 05 40 f9` | ldr x19,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bceebc"></a> `00bceebc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bceec0"></a> `00bceec0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bceec4"></a> `00bceec4` | `73 30 00 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00bceec8"></a> `00bceec8` | `95 9a 49 f9` | ldr x21,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bceecc"></a> `00bceecc` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00bceed0"></a> `00bceed0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bceed4"></a> `00bceed4` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bceed8"></a> `00bceed8` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bceedc"></a> `00bceedc` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bceee0"></a> `00bceee0` | `08 01 00 54` | b.hi 0x00bcef00 | `CONDITIONAL_JUMP`
<a id="insn-00bceee4"></a> `00bceee4` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bceee8"></a> `00bceee8` | `7a 38 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bceeec"></a> `00bceeec` | `20 03 00 b4` | cbz x0,0x00bcef50 | `CONDITIONAL_JUMP`
<a id="insn-00bceef0"></a> `00bceef0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bceef4"></a> `00bceef4` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bceef8"></a> `00bceef8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bceefc"></a> `00bceefc` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcef00"></a> `00bcef00` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcef04"></a> `00bcef04` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bcef08"></a> `00bcef08` | `48 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bcef0c"></a> `00bcef0c` | `08 61 1e 91` | add x8,x8,#0x798 | `FALL_THROUGH`
<a id="insn-00bcef10"></a> `00bcef10` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef14"></a> `00bcef14` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bcef18"></a> `00bcef18` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcef1c"></a> `00bcef1c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcef20"></a> `00bcef20` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcef24"></a> `00bcef24` | `13 50 01 a9` | stp x19,x20,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcef28"></a> `00bcef28` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcef2c"></a> `00bcef2c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef30"></a> `00bcef30` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bcef34"></a> `00bcef34` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcef38"></a> `00bcef38` | `d6 ff ff 17` | b 0x00bcee90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcef3c"></a> `00bcef3c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bcef40"></a> `00bcef40` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcef44"></a> `00bcef44` | `14 25 0c 39` | strb w20,[x8, #0x309] | `FALL_THROUGH`
<a id="insn-00bcef48"></a> `00bcef48` | `15 21 0c 39` | strb w21,[x8, #0x308] | `FALL_THROUGH`
<a id="insn-00bcef4c"></a> `00bcef4c` | `d1 ff ff 17` | b 0x00bcee90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcef50"></a> `00bcef50` | `60 30 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcebe0`](#insn-00bcebe0) 範囲 `[['00bcebe0', '00bcec07']]`
  - `CONDITIONAL_JUMP` [`00bcec04`](#insn-00bcec04) → [`00bced60`](#insn-00bced60)
  - `FALL_THROUGH` [`00bcec04`](#insn-00bcec04) → [`00bcec08`](#insn-00bcec08)
- ブロック [`00bcec08`](#insn-00bcec08) 範囲 `[['00bcec08', '00bcec1f']]`
  - `UNCONDITIONAL_JUMP` [`00bcec1c`](#insn-00bcec1c) → [`00bcec2c`](#insn-00bcec2c)
- ブロック [`00bcec20`](#insn-00bcec20) 範囲 `[['00bcec20', '00bcec23']]`
  - `FALL_THROUGH` [`00bcec20`](#insn-00bcec20) → [`00bcec24`](#insn-00bcec24)
- ブロック [`00bcec24`](#insn-00bcec24) 範囲 `[['00bcec24', '00bcec2b']]`
  - `CONDITIONAL_JUMP` [`00bcec28`](#insn-00bcec28) → [`00bcec70`](#insn-00bcec70)
  - `FALL_THROUGH` [`00bcec28`](#insn-00bcec28) → [`00bcec2c`](#insn-00bcec2c)
- ブロック [`00bcec2c`](#insn-00bcec2c) 範囲 `[['00bcec2c', '00bcec43']]`
  - `CONDITIONAL_JUMP` [`00bcec40`](#insn-00bcec40) → [`00bcec20`](#insn-00bcec20)
  - `FALL_THROUGH` [`00bcec40`](#insn-00bcec40) → [`00bcec44`](#insn-00bcec44)
- ブロック [`00bcec44`](#insn-00bcec44) 範囲 `[['00bcec44', '00bcec47']]`
  - `CONDITIONAL_JUMP` [`00bcec44`](#insn-00bcec44) → [`00bcec68`](#insn-00bcec68)
  - `FALL_THROUGH` [`00bcec44`](#insn-00bcec44) → [`00bcec48`](#insn-00bcec48)
- ブロック [`00bcec48`](#insn-00bcec48) 範囲 `[['00bcec48', '00bcec53']]`
  - `FALL_THROUGH` [`00bcec50`](#insn-00bcec50) → [`00bcec54`](#insn-00bcec54)
- ブロック [`00bcec54`](#insn-00bcec54) 範囲 `[['00bcec54', '00bcec67']]`
  - `UNCONDITIONAL_JUMP` [`00bcec64`](#insn-00bcec64) → [`00bcec24`](#insn-00bcec24)
- ブロック [`00bcec68`](#insn-00bcec68) 範囲 `[['00bcec68', '00bcec6f']]`
  - `UNCONDITIONAL_JUMP` [`00bcec6c`](#insn-00bcec6c) → [`00bcec24`](#insn-00bcec24)
- ブロック [`00bcec70`](#insn-00bcec70) 範囲 `[['00bcec70', '00bcec7b']]`
  - `FALL_THROUGH` [`00bcec78`](#insn-00bcec78) → [`00bcec7c`](#insn-00bcec7c)
- ブロック [`00bcec7c`](#insn-00bcec7c) 範囲 `[['00bcec7c', '00bcec7f']]`
  - `CONDITIONAL_JUMP` [`00bcec7c`](#insn-00bcec7c) → [`00bced50`](#insn-00bced50)
  - `FALL_THROUGH` [`00bcec7c`](#insn-00bcec7c) → [`00bcec80`](#insn-00bcec80)
- ブロック [`00bcec80`](#insn-00bcec80) 範囲 `[['00bcec80', '00bcec8b']]`
  - `FALL_THROUGH` [`00bcec88`](#insn-00bcec88) → [`00bcec8c`](#insn-00bcec8c)
- ブロック [`00bcec8c`](#insn-00bcec8c) 範囲 `[['00bcec8c', '00bcec8f']]`
  - `CONDITIONAL_JUMP` [`00bcec8c`](#insn-00bcec8c) → [`00bced50`](#insn-00bced50)
  - `FALL_THROUGH` [`00bcec8c`](#insn-00bcec8c) → [`00bcec90`](#insn-00bcec90)
- ブロック [`00bcec90`](#insn-00bcec90) 範囲 `[['00bcec90', '00bcec97']]`
  - `FALL_THROUGH` [`00bcec94`](#insn-00bcec94) → [`00bcec98`](#insn-00bcec98)
- ブロック [`00bcec98`](#insn-00bcec98) 範囲 `[['00bcec98', '00bceca3']]`
  - `CONDITIONAL_JUMP` [`00bceca0`](#insn-00bceca0) → [`00bcee84`](#insn-00bcee84)
  - `FALL_THROUGH` [`00bceca0`](#insn-00bceca0) → [`00bceca4`](#insn-00bceca4)
- ブロック [`00bceca4`](#insn-00bceca4) 範囲 `[['00bceca4', '00bcecab']]`
  - `FALL_THROUGH` [`00bceca8`](#insn-00bceca8) → [`00bcecac`](#insn-00bcecac)
- ブロック [`00bcecac`](#insn-00bcecac) 範囲 `[['00bcecac', '00bcecb7']]`
  - `FALL_THROUGH` [`00bcecb4`](#insn-00bcecb4) → [`00bcecb8`](#insn-00bcecb8)
- ブロック [`00bcecb8`](#insn-00bcecb8) 範囲 `[['00bcecb8', '00bcecc7']]`
  - `FALL_THROUGH` [`00bcecc4`](#insn-00bcecc4) → [`00bcecc8`](#insn-00bcecc8)
- ブロック [`00bcecc8`](#insn-00bcecc8) 範囲 `[['00bcecc8', '00bceccf']]`
  - `CONDITIONAL_JUMP` [`00bceccc`](#insn-00bceccc) → [`00bcef3c`](#insn-00bcef3c)
  - `FALL_THROUGH` [`00bceccc`](#insn-00bceccc) → [`00bcecd0`](#insn-00bcecd0)
- ブロック [`00bcecd0`](#insn-00bcecd0) 範囲 `[['00bcecd0', '00bcecd7']]`
  - `CONDITIONAL_JUMP` [`00bcecd4`](#insn-00bcecd4) → [`00bcece0`](#insn-00bcece0)
  - `FALL_THROUGH` [`00bcecd4`](#insn-00bcecd4) → [`00bcecd8`](#insn-00bcecd8)
- ブロック [`00bcecd8`](#insn-00bcecd8) 範囲 `[['00bcecd8', '00bcecdf']]`
  - `FALL_THROUGH` [`00bcecdc`](#insn-00bcecdc) → [`00bcece0`](#insn-00bcece0)
- ブロック [`00bcece0`](#insn-00bcece0) 範囲 `[['00bcece0', '00bcecf3']]`
  - `CONDITIONAL_JUMP` [`00bcecf0`](#insn-00bcecf0) → [`00bced14`](#insn-00bced14)
  - `FALL_THROUGH` [`00bcecf0`](#insn-00bcecf0) → [`00bcecf4`](#insn-00bcecf4)
- ブロック [`00bcecf4`](#insn-00bcecf4) 範囲 `[['00bcecf4', '00bcecff']]`
  - `CONDITIONAL_JUMP` [`00bcecfc`](#insn-00bcecfc) → [`00bcef50`](#insn-00bcef50)
  - `FALL_THROUGH` [`00bcecfc`](#insn-00bcecfc) → [`00bced00`](#insn-00bced00)
- ブロック [`00bced00`](#insn-00bced00) 範囲 `[['00bced00', '00bced13']]`
  - `FALL_THROUGH` [`00bced10`](#insn-00bced10) → [`00bced14`](#insn-00bced14)
- ブロック [`00bced14`](#insn-00bced14) 範囲 `[['00bced14', '00bced47']]`
  - `FALL_THROUGH` [`00bced44`](#insn-00bced44) → [`00bced48`](#insn-00bced48)
- ブロック [`00bced48`](#insn-00bced48) 範囲 `[['00bced48', '00bced4f']]`
  - `UNCONDITIONAL_JUMP` [`00bced4c`](#insn-00bced4c) → [`00bcef44`](#insn-00bcef44)
- ブロック [`00bced50`](#insn-00bced50) 範囲 `[['00bced50', '00bced5f']]`
  - `CONDITIONAL_JUMP` [`00bced5c`](#insn-00bced5c) → [`00bcedfc`](#insn-00bcedfc)
  - `FALL_THROUGH` [`00bced5c`](#insn-00bced5c) → [`00bced60`](#insn-00bced60)
- ブロック [`00bced60`](#insn-00bced60) 範囲 `[['00bced60', '00bced67']]`
  - `CONDITIONAL_JUMP` [`00bced64`](#insn-00bced64) → [`00bcee8c`](#insn-00bcee8c)
  - `FALL_THROUGH` [`00bced64`](#insn-00bced64) → [`00bced68`](#insn-00bced68)
- ブロック [`00bced68`](#insn-00bced68) 範囲 `[['00bced68', '00bced73']]`
  - `CONDITIONAL_JUMP` [`00bced70`](#insn-00bced70) → [`00bcee8c`](#insn-00bcee8c)
  - `FALL_THROUGH` [`00bced70`](#insn-00bced70) → [`00bced74`](#insn-00bced74)
- ブロック [`00bced74`](#insn-00bced74) 範囲 `[['00bced74', '00bced83']]`
  - `CONDITIONAL_JUMP` [`00bced80`](#insn-00bced80) → [`00bcee8c`](#insn-00bcee8c)
  - `FALL_THROUGH` [`00bced80`](#insn-00bced80) → [`00bced84`](#insn-00bced84)
- ブロック [`00bced84`](#insn-00bced84) 範囲 `[['00bced84', '00bced87']]`
  - `FALL_THROUGH` [`00bced84`](#insn-00bced84) → [`00bced88`](#insn-00bced88)
- ブロック [`00bced88`](#insn-00bced88) 範囲 `[['00bced88', '00bced93']]`
  - `CONDITIONAL_JUMP` [`00bced90`](#insn-00bced90) → [`00bcee8c`](#insn-00bcee8c)
  - `FALL_THROUGH` [`00bced90`](#insn-00bced90) → [`00bced94`](#insn-00bced94)
- ブロック [`00bced94`](#insn-00bced94) 範囲 `[['00bced94', '00bceda3']]`
  - `FALL_THROUGH` [`00bceda0`](#insn-00bceda0) → [`00bceda4`](#insn-00bceda4)
- ブロック [`00bceda4`](#insn-00bceda4) 範囲 `[['00bceda4', '00bceda7']]`
  - `CONDITIONAL_JUMP` [`00bceda4`](#insn-00bceda4) → [`00bcee90`](#insn-00bcee90)
  - `FALL_THROUGH` [`00bceda4`](#insn-00bceda4) → [`00bceda8`](#insn-00bceda8)
- ブロック [`00bceda8`](#insn-00bceda8) 範囲 `[['00bceda8', '00bcedbb']]`
  - `FALL_THROUGH` [`00bcedb8`](#insn-00bcedb8) → [`00bcedbc`](#insn-00bcedbc)
- ブロック [`00bcedbc`](#insn-00bcedbc) 範囲 `[['00bcedbc', '00bcedc3']]`
  - `CONDITIONAL_JUMP` [`00bcedc0`](#insn-00bcedc0) → [`00bcede0`](#insn-00bcede0)
  - `FALL_THROUGH` [`00bcedc0`](#insn-00bcedc0) → [`00bcedc4`](#insn-00bcedc4)
- ブロック [`00bcedc4`](#insn-00bcedc4) 範囲 `[['00bcedc4', '00bcedcf']]`
  - `CONDITIONAL_JUMP` [`00bcedcc`](#insn-00bcedcc) → [`00bcef50`](#insn-00bcef50)
  - `FALL_THROUGH` [`00bcedcc`](#insn-00bcedcc) → [`00bcedd0`](#insn-00bcedd0)
- ブロック [`00bcedd0`](#insn-00bcedd0) 範囲 `[['00bcedd0', '00bceddf']]`
  - `FALL_THROUGH` [`00bceddc`](#insn-00bceddc) → [`00bcede0`](#insn-00bcede0)
- ブロック [`00bcede0`](#insn-00bcede0) 範囲 `[['00bcede0', '00bcedfb']]`
  - `UNCONDITIONAL_JUMP` [`00bcedf8`](#insn-00bcedf8) → [`00bcee60`](#insn-00bcee60)
- ブロック [`00bcedfc`](#insn-00bcedfc) 範囲 `[['00bcedfc', '00bcee0f']]`
  - `CONDITIONAL_JUMP` [`00bcee0c`](#insn-00bcee0c) → [`00bcee90`](#insn-00bcee90)
  - `FALL_THROUGH` [`00bcee0c`](#insn-00bcee0c) → [`00bcee10`](#insn-00bcee10)
- ブロック [`00bcee10`](#insn-00bcee10) 範囲 `[['00bcee10', '00bcee2b']]`
  - `CONDITIONAL_JUMP` [`00bcee28`](#insn-00bcee28) → [`00bcee48`](#insn-00bcee48)
  - `FALL_THROUGH` [`00bcee28`](#insn-00bcee28) → [`00bcee2c`](#insn-00bcee2c)
- ブロック [`00bcee2c`](#insn-00bcee2c) 範囲 `[['00bcee2c', '00bcee37']]`
  - `CONDITIONAL_JUMP` [`00bcee34`](#insn-00bcee34) → [`00bcef50`](#insn-00bcef50)
  - `FALL_THROUGH` [`00bcee34`](#insn-00bcee34) → [`00bcee38`](#insn-00bcee38)
- ブロック [`00bcee38`](#insn-00bcee38) 範囲 `[['00bcee38', '00bcee47']]`
  - `FALL_THROUGH` [`00bcee44`](#insn-00bcee44) → [`00bcee48`](#insn-00bcee48)
- ブロック [`00bcee48`](#insn-00bcee48) 範囲 `[['00bcee48', '00bcee5f']]`
  - `FALL_THROUGH` [`00bcee5c`](#insn-00bcee5c) → [`00bcee60`](#insn-00bcee60)
- ブロック [`00bcee60`](#insn-00bcee60) 範囲 `[['00bcee60', '00bcee83']]`
  - `UNCONDITIONAL_JUMP` [`00bcee80`](#insn-00bcee80) → [`00bcee90`](#insn-00bcee90)
- ブロック [`00bcee84`](#insn-00bcee84) 範囲 `[['00bcee84', '00bcee8b']]`
  - `CONDITIONAL_JUMP` [`00bcee88`](#insn-00bcee88) → [`00bceea8`](#insn-00bceea8)
  - `FALL_THROUGH` [`00bcee88`](#insn-00bcee88) → [`00bcee8c`](#insn-00bcee8c)
- ブロック [`00bcee8c`](#insn-00bcee8c) 範囲 `[['00bcee8c', '00bcee8f']]`
  - `FALL_THROUGH` [`00bcee8c`](#insn-00bcee8c) → [`00bcee90`](#insn-00bcee90)
- ブロック [`00bcee90`](#insn-00bcee90) 範囲 `[['00bcee90', '00bceea7']]`
- ブロック [`00bceea8`](#insn-00bceea8) 範囲 `[['00bceea8', '00bceeaf']]`
  - `CONDITIONAL_JUMP` [`00bceeac`](#insn-00bceeac) → [`00bceeb8`](#insn-00bceeb8)
  - `FALL_THROUGH` [`00bceeac`](#insn-00bceeac) → [`00bceeb0`](#insn-00bceeb0)
- ブロック [`00bceeb0`](#insn-00bceeb0) 範囲 `[['00bceeb0', '00bceeb7']]`
  - `CONDITIONAL_JUMP` [`00bceeb4`](#insn-00bceeb4) → [`00bcee8c`](#insn-00bcee8c)
  - `FALL_THROUGH` [`00bceeb4`](#insn-00bceeb4) → [`00bceeb8`](#insn-00bceeb8)
- ブロック [`00bceeb8`](#insn-00bceeb8) 範囲 `[['00bceeb8', '00bceebb']]`
  - `FALL_THROUGH` [`00bceeb8`](#insn-00bceeb8) → [`00bceebc`](#insn-00bceebc)
- ブロック [`00bceebc`](#insn-00bceebc) 範囲 `[['00bceebc', '00bceee3']]`
  - `CONDITIONAL_JUMP` [`00bceee0`](#insn-00bceee0) → [`00bcef00`](#insn-00bcef00)
  - `FALL_THROUGH` [`00bceee0`](#insn-00bceee0) → [`00bceee4`](#insn-00bceee4)
- ブロック [`00bceee4`](#insn-00bceee4) 範囲 `[['00bceee4', '00bceeef']]`
  - `CONDITIONAL_JUMP` [`00bceeec`](#insn-00bceeec) → [`00bcef50`](#insn-00bcef50)
  - `FALL_THROUGH` [`00bceeec`](#insn-00bceeec) → [`00bceef0`](#insn-00bceef0)
- ブロック [`00bceef0`](#insn-00bceef0) 範囲 `[['00bceef0', '00bceef3']]`
  - `FALL_THROUGH` [`00bceef0`](#insn-00bceef0) → [`00bceef4`](#insn-00bceef4)
- ブロック [`00bceef4`](#insn-00bceef4) 範囲 `[['00bceef4', '00bceeff']]`
  - `FALL_THROUGH` [`00bceefc`](#insn-00bceefc) → [`00bcef00`](#insn-00bcef00)
- ブロック [`00bcef00`](#insn-00bcef00) 範囲 `[['00bcef00', '00bcef0f']]`
  - `FALL_THROUGH` [`00bcef0c`](#insn-00bcef0c) → [`00bcef10`](#insn-00bcef10)
- ブロック [`00bcef10`](#insn-00bcef10) 範囲 `[['00bcef10', '00bcef27']]`
  - `FALL_THROUGH` [`00bcef24`](#insn-00bcef24) → [`00bcef28`](#insn-00bcef28)
- ブロック [`00bcef28`](#insn-00bcef28) 範囲 `[['00bcef28', '00bcef3b']]`
  - `UNCONDITIONAL_JUMP` [`00bcef38`](#insn-00bcef38) → [`00bcee90`](#insn-00bcee90)
- ブロック [`00bcef3c`](#insn-00bcef3c) 範囲 `[['00bcef3c', '00bcef43']]`
  - `FALL_THROUGH` [`00bcef40`](#insn-00bcef40) → [`00bcef44`](#insn-00bcef44)
- ブロック [`00bcef44`](#insn-00bcef44) 範囲 `[['00bcef44', '00bcef4f']]`
  - `UNCONDITIONAL_JUMP` [`00bcef4c`](#insn-00bcef4c) → [`00bcee90`](#insn-00bcee90)
- ブロック [`00bcef50`](#insn-00bcef50) 範囲 `[['00bcef50', '00bcef53']]`

## 命令位置別の参照

- [`00bcebe4`](#insn-00bcebe4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebe8`](#insn-00bcebe8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebec`](#insn-00bcebec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebf0`](#insn-00bcebf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec04`](#insn-00bcec04) → [`00bced60`](#insn-00bced60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec1c`](#insn-00bcec1c) → [`00bcec2c`](#insn-00bcec2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec28`](#insn-00bcec28) → [`00bcec70`](#insn-00bcec70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec38`](#insn-00bcec38) → `00c17ab8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcec40`](#insn-00bcec40) → [`00bcec20`](#insn-00bcec20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec44`](#insn-00bcec44) → [`00bcec68`](#insn-00bcec68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec48`](#insn-00bcec48) → `00c17ab9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcec64`](#insn-00bcec64) → [`00bcec24`](#insn-00bcec24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec6c`](#insn-00bcec6c) → [`00bcec24`](#insn-00bcec24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec74`](#insn-00bcec74) → `00c17ac8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcec7c`](#insn-00bcec7c) → [`00bced50`](#insn-00bced50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec80`](#insn-00bcec80) → `00c17ac9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcec8c`](#insn-00bcec8c) → [`00bced50`](#insn-00bced50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec90`](#insn-00bcec90) → `00c17aca`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bceca0`](#insn-00bceca0) → [`00bcee84`](#insn-00bcee84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecc4`](#insn-00bcecc4) → [`00bbdd50`](../00bbd/00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bceccc`](#insn-00bceccc) → [`00bcef3c`](#insn-00bcef3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecd4`](#insn-00bcecd4) → [`00bcece0`](#insn-00bcece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf0`](#insn-00bcecf0) → [`00bced14`](#insn-00bced14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf8`](#insn-00bcecf8) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcecfc`](#insn-00bcecfc) → [`00bcef50`](#insn-00bcef50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced2c`](#insn-00bced2c) → `00c19078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bced4c`](#insn-00bced4c) → [`00bcef44`](#insn-00bcef44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced5c`](#insn-00bced5c) → [`00bcedfc`](#insn-00bcedfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced64`](#insn-00bced64) → [`00bcee8c`](#insn-00bcee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced70`](#insn-00bced70) → [`00bcee8c`](#insn-00bcee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced80`](#insn-00bced80) → [`00bcee8c`](#insn-00bcee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced90`](#insn-00bced90) → [`00bcee8c`](#insn-00bcee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceda0`](#insn-00bceda0) → [`00bc1034`](../00bc1/00bc1034.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1034` · 推定シンボル `None` · 推定型 `None`
- [`00bceda4`](#insn-00bceda4) → [`00bcee90`](#insn-00bcee90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedc0`](#insn-00bcedc0) → [`00bcede0`](#insn-00bcede0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedc8`](#insn-00bcedc8) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcedcc`](#insn-00bcedcc) → [`00bcef50`](#insn-00bcef50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedf8`](#insn-00bcedf8) → [`00bcee60`](#insn-00bcee60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee08`](#insn-00bcee08) → [`00bc1034`](../00bc1/00bc1034.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1034` · 推定シンボル `None` · 推定型 `None`
- [`00bcee0c`](#insn-00bcee0c) → [`00bcee90`](#insn-00bcee90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee28`](#insn-00bcee28) → [`00bcee48`](#insn-00bcee48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee30`](#insn-00bcee30) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcee34`](#insn-00bcee34) → [`00bcef50`](#insn-00bcef50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee60`](#insn-00bcee60) → `00c19078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcee60`](#insn-00bcee60) → `00c190e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcee80`](#insn-00bcee80) → [`00bcee90`](#insn-00bcee90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee88`](#insn-00bcee88) → [`00bceea8`](#insn-00bceea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee90`](#insn-00bcee90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee94`](#insn-00bcee94) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee98`](#insn-00bcee98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee9c`](#insn-00bcee9c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceeac`](#insn-00bceeac) → [`00bceeb8`](#insn-00bceeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceeb0`](#insn-00bceeb0) → `00c17acb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bceeb4`](#insn-00bceeb4) → [`00bcee8c`](#insn-00bcee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceeb8`](#insn-00bceeb8) → `00c17ad0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bceec0`](#insn-00bceec0) → `002b09e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bceec4`](#insn-00bceec4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00bceee0`](#insn-00bceee0) → [`00bcef00`](#insn-00bcef00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceee8`](#insn-00bceee8) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bceeec`](#insn-00bceeec) → [`00bcef50`](#insn-00bcef50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef18`](#insn-00bcef18) → `00c17798`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcef24`](#insn-00bcef24) → `002b09e1`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcef38`](#insn-00bcef38) → [`00bcee90`](#insn-00bcee90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef4c`](#insn-00bcef4c) → [`00bcee90`](#insn-00bcee90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef50`](#insn-00bcef50) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcebe4`](#insn-00bcebe4)

~~~json
{
  "source": "00bcebe4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebe8`](#insn-00bcebe8)

~~~json
{
  "source": "00bcebe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebec`](#insn-00bcebec)

~~~json
{
  "source": "00bcebec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebf0`](#insn-00bcebf0)

~~~json
{
  "source": "00bcebf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec04`](#insn-00bcec04)

~~~json
{
  "source": "00bcec04",
  "target": "00bced60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec1c`](#insn-00bcec1c)

~~~json
{
  "source": "00bcec1c",
  "target": "00bcec2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec28`](#insn-00bcec28)

~~~json
{
  "source": "00bcec28",
  "target": "00bcec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec38`](#insn-00bcec38)

~~~json
{
  "source": "00bcec38",
  "target": "00c17ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17ab8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6c",
  "capture_start": "00c17ab8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcec40`](#insn-00bcec40)

~~~json
{
  "source": "00bcec40",
  "target": "00bcec20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec44`](#insn-00bcec44)

~~~json
{
  "source": "00bcec44",
  "target": "00bcec68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec48`](#insn-00bcec48)

~~~json
{
  "source": "00bcec48",
  "target": "00c17ab9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17ab9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "74",
  "capture_start": "00c17ab9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcec64`](#insn-00bcec64)

~~~json
{
  "source": "00bcec64",
  "target": "00bcec24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec6c`](#insn-00bcec6c)

~~~json
{
  "source": "00bcec6c",
  "target": "00bcec24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec74`](#insn-00bcec74)

~~~json
{
  "source": "00bcec74",
  "target": "00c17ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17ac8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6d",
  "capture_start": "00c17ac8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcec7c`](#insn-00bcec7c)

~~~json
{
  "source": "00bcec7c",
  "target": "00bced50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec80`](#insn-00bcec80)

~~~json
{
  "source": "00bcec80",
  "target": "00c17ac9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17ac9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "49",
  "capture_start": "00c17ac9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcec8c`](#insn-00bcec8c)

~~~json
{
  "source": "00bcec8c",
  "target": "00bced50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec90`](#insn-00bcec90)

~~~json
{
  "source": "00bcec90",
  "target": "00c17aca",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17aca",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "02",
  "capture_start": "00c17aca",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bceca0`](#insn-00bceca0)

~~~json
{
  "source": "00bceca0",
  "target": "00bcee84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecc4`](#insn-00bcecc4)

~~~json
{
  "source": "00bcecc4",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceccc`](#insn-00bceccc)

~~~json
{
  "source": "00bceccc",
  "target": "00bcef3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecd4`](#insn-00bcecd4)

~~~json
{
  "source": "00bcecd4",
  "target": "00bcece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecf0`](#insn-00bcecf0)

~~~json
{
  "source": "00bcecf0",
  "target": "00bced14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecf8`](#insn-00bcecf8)

~~~json
{
  "source": "00bcecf8",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecfc`](#insn-00bcecfc)

~~~json
{
  "source": "00bcecfc",
  "target": "00bcef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced2c`](#insn-00bced2c)

~~~json
{
  "source": "00bced2c",
  "target": "00c19078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19078",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bced4c`](#insn-00bced4c)

~~~json
{
  "source": "00bced4c",
  "target": "00bcef44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced5c`](#insn-00bced5c)

~~~json
{
  "source": "00bced5c",
  "target": "00bcedfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced64`](#insn-00bced64)

~~~json
{
  "source": "00bced64",
  "target": "00bcee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced70`](#insn-00bced70)

~~~json
{
  "source": "00bced70",
  "target": "00bcee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced80`](#insn-00bced80)

~~~json
{
  "source": "00bced80",
  "target": "00bcee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced90`](#insn-00bced90)

~~~json
{
  "source": "00bced90",
  "target": "00bcee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceda0`](#insn-00bceda0)

~~~json
{
  "source": "00bceda0",
  "target": "00bc1034",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceda4`](#insn-00bceda4)

~~~json
{
  "source": "00bceda4",
  "target": "00bcee90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedc0`](#insn-00bcedc0)

~~~json
{
  "source": "00bcedc0",
  "target": "00bcede0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedc8`](#insn-00bcedc8)

~~~json
{
  "source": "00bcedc8",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedcc`](#insn-00bcedcc)

~~~json
{
  "source": "00bcedcc",
  "target": "00bcef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedf8`](#insn-00bcedf8)

~~~json
{
  "source": "00bcedf8",
  "target": "00bcee60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee08`](#insn-00bcee08)

~~~json
{
  "source": "00bcee08",
  "target": "00bc1034",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee0c`](#insn-00bcee0c)

~~~json
{
  "source": "00bcee0c",
  "target": "00bcee90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee28`](#insn-00bcee28)

~~~json
{
  "source": "00bcee28",
  "target": "00bcee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee30`](#insn-00bcee30)

~~~json
{
  "source": "00bcee30",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee34`](#insn-00bcee34)

~~~json
{
  "source": "00bcee34",
  "target": "00bcef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee60`](#insn-00bcee60)

~~~json
{
  "source": "00bcee60",
  "target": "00c19078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19078",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcee60`](#insn-00bcee60)

~~~json
{
  "source": "00bcee60",
  "target": "00c190e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c190e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcee80`](#insn-00bcee80)

~~~json
{
  "source": "00bcee80",
  "target": "00bcee90",
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
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee94`](#insn-00bcee94)

~~~json
{
  "source": "00bcee94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee98`](#insn-00bcee98)

~~~json
{
  "source": "00bcee98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee9c`](#insn-00bcee9c)

~~~json
{
  "source": "00bcee9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceeac`](#insn-00bceeac)

~~~json
{
  "source": "00bceeac",
  "target": "00bceeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceeb0`](#insn-00bceeb0)

~~~json
{
  "source": "00bceeb0",
  "target": "00c17acb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17acb",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "22",
  "capture_start": "00c17acb",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bceeb4`](#insn-00bceeb4)

~~~json
{
  "source": "00bceeb4",
  "target": "00bcee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceeb8`](#insn-00bceeb8)

~~~json
{
  "source": "00bceeb8",
  "target": "00c17ad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17ad0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bceec0`](#insn-00bceec0)

~~~json
{
  "source": "00bceec0",
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
- 参照命令 [`00bceec4`](#insn-00bceec4)

~~~json
{
  "source": "00bceec4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceee0`](#insn-00bceee0)

~~~json
{
  "source": "00bceee0",
  "target": "00bcef00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceee8`](#insn-00bceee8)

~~~json
{
  "source": "00bceee8",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceeec`](#insn-00bceeec)

~~~json
{
  "source": "00bceeec",
  "target": "00bcef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef18`](#insn-00bcef18)

~~~json
{
  "source": "00bcef18",
  "target": "00c17798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17798",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcef24`](#insn-00bcef24)

~~~json
{
  "source": "00bcef24",
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
- 参照命令 [`00bcef38`](#insn-00bcef38)

~~~json
{
  "source": "00bcef38",
  "target": "00bcee90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef4c`](#insn-00bcef4c)

~~~json
{
  "source": "00bcef4c",
  "target": "00bcee90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef50`](#insn-00bcef50)

~~~json
{
  "source": "00bcef50",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
