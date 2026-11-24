# 00bcecec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bceca8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-18bcaf574d2a033c0351fd5ef31e0ffc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4b734`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-ca124e7530871503da5e19d49b4e112b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcecec",
  "name": "FUN_00bcecec",
  "size": 884,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ae0b729de4a58a7f5f191206cab98233d4a29434281ea9ffcc1e956e642c6b6",
  "source_text_sha256": "7ae0b729de4a58a7f5f191206cab98233d4a29434281ea9ffcc1e956e642c6b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcecec",
        "00bcf05f"
      ]
    ],
    "bytes_sha256": "247b6e65c8e4c50645a9b45fa3f830b1542d093090f4c6526ef0430b755b4145",
    "instruction_count": 221,
    "instruction_bytes": 884,
    "body_bytes": 884,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc24a0](../00bc2/00bc24a0.md)
- [00bce93c](../00bce/00bce93c.md)

## 呼び出し先

- [00bbde5c](../00bbd/00bbde5c.md)
- [00bc1140](../00bc1/00bc1140.md)
- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

## 関連文字列（未確認候補）

~~~text
"operator-="
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7460 bytes

~~~c

undefined8 * FUN_00bcecec(long *param_1,undefined1 *param_2)

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
      if ((byte)(&UNK_00c179d8)[uVar16 * 0x10] < bVar4) {
        uVar14 = uVar16 + 1;
        uVar16 = uVar15;
      }
      else {
                    /* try { // try from 00bced60 to 00cced6b has its CatchHandler @ 00bcf37c */
        if (((&UNK_00c179d8)[uVar16 * 0x10] == bVar4) &&
           ((byte)(&UNK_00c179d9)[uVar16 * 0x10] < pbVar2[1])) {
          uVar14 = uVar16 + 1;
          uVar16 = uVar15;
        }
      }
      uVar15 = uVar16;
    } while (uVar16 != uVar14);
    lVar11 = uVar14 * 0x10;
                    /* try { // try from 00bced88 to 00cced97 has its CatchHandler @ 00bcf378 */
                    /* try { // try from 00bced98 to 00cceda3 has its CatchHandler @ 00bcf364 */
    if (((&UNK_00c179d8)[lVar11] == bVar4) && ((&UNK_00c179d9)[lVar11] == pbVar2[1])) {
      bVar4 = (&UNK_00c179da)[lVar11];
                    /* try { // try from 00bceda4 to 00ccedb7 has its CatchHandler @ 00bcf354 */
      *param_1 = (long)(pbVar2 + 2);
      if (bVar4 == 8) {
        uVar5 = *(undefined1 *)((long)param_1 + 0x309);
                    /* try { // try from 00bcedb8 to 00ccedc3 has its CatchHandler @ 00bcf324 */
        lVar11 = param_1[0x61];
        *(undefined1 *)(param_1 + 0x61) = 0;
        uVar12 = uVar5;
                    /* try { // try from 00bcedc4 to 00ccedd3 has its CatchHandler @ 00bcf304 */
        if (param_2 != (undefined1 *)0x0) {
          uVar12 = 1;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar12;
        lVar6 = FUN_00bbde5c();
                    /* try { // try from 00bcedd4 to 00ccedeb has its CatchHandler @ 00bcf2c0 */
        if (lVar6 == 0) {
          puVar8 = (undefined8 *)0x0;
        }
        else {
          if (param_2 != (undefined1 *)0x0) {
            *param_2 = 1;
          }
                    /* try { // try from 00bcedec to 00ccee53 has its CatchHandler @ 00bce5d8 */
          pvVar17 = (void *)param_1[0x266];
          lVar13 = *(long *)((long)pvVar17 + 8);
          puVar7 = pvVar17;
          if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
            puVar7 = malloc(0x1000);
            if (puVar7 == (void *)0x0) goto LAB_00bcf05c;
            lVar13 = 0;
            *puVar7 = pvVar17;
            puVar7[1] = 0;
            param_1[0x266] = (long)puVar7;
          }
          *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
          puVar8 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
          *puVar8 = &PTR_FUN_00c19178;
          *(long *)((long)puVar7 + lVar13 + 0x20) = lVar6;
          *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 4;
                    /* try { // try from 00bcee54 to 00ccee93 has its CatchHandler @ 00bcf408 */
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
      if ((bVar4 == 4) && (((&UNK_00c179db)[lVar11] & 1) == 0)) {
        return (undefined8 *)0x0;
      }
      __s = *(char **)(&UNK_00c179e0 + lVar11);
                    /* try { // try from 00bcefc8 to 00ccefff has its CatchHandler @ 00bcf254 */
      sVar9 = strlen(__s);
      pvVar17 = (void *)param_1[0x266];
      lVar11 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (0xfffffffffffff00f < lVar11 - 0xfd0U) {
LAB_00bcf00c:
                    /* try { // try from 00bcf00c to 00ccf01b has its CatchHandler @ 00bcf24c */
                    /* try { // try from 00bcf01c to 00ccf033 has its CatchHandler @ 00bcf248 */
        *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
        puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
        *puVar7 = &PTR_FUN_00c17898;
        *(char **)((long)puVar8 + lVar11 + 0x20) = __s;
        *(size_t *)((long)puVar8 + lVar11 + 0x28) = sVar9;
                    /* try { // try from 00bcf034 to 00ccf46b has its CatchHandler @ 00bce5d8 */
        *(undefined1 *)((long)puVar8 + lVar11 + 0x18) = 8;
        *(ushort *)((long)puVar8 + lVar11 + 0x19) =
             *(ushort *)((long)puVar8 + lVar11 + 0x19) & 0xf000 | 0x540;
        return puVar7;
      }
      puVar8 = malloc(0x1000);
      if (puVar8 != (void *)0x0) {
        lVar11 = 0;
                    /* try { // try from 00bcf000 to 00ccf00b has its CatchHandler @ 00bcf250 */
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
        goto LAB_00bcf00c;
      }
      goto LAB_00bcf05c;
    }
    if (*(short *)pbVar2 == 0x696c) {
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1140();
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00bcf05c;
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c191e8;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 0x14;
      goto LAB_00bcef6c;
    }
  }
  if ((pbVar2 != pbVar3) && (*pbVar2 == 0x76)) {
    pbVar1 = pbVar2 + 1;
    *param_1 = (long)pbVar1;
                    /* try { // try from 00bcee94 to 00ccee9f has its CatchHandler @ 00bcf2ac */
    if ((pbVar3 != pbVar1) && (*pbVar1 - 0x30 < 10)) {
                    /* try { // try from 00bceea0 to 00cceeaf has its CatchHandler @ 00bcf28c */
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1140();
                    /* try { // try from 00bceeb0 to 00cceec7 has its CatchHandler @ 00bcf258 */
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
                    /* try { // try from 00bceec8 to 00ccefc7 has its CatchHandler @ 00bce5d8 */
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00bcf05c:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c19178;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 4;
LAB_00bcef6c:
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
<a id="insn-00bcecec"></a> `00bcecec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcecf0"></a> `00bcecf0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bcecf4"></a> `00bcecf4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcecf8"></a> `00bcecf8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcecfc"></a> `00bcecfc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bced00"></a> `00bced00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bced04"></a> `00bced04` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bced08"></a> `00bced08` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00bced0c"></a> `00bced0c` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bced10"></a> `00bced10` | `e3 0a 00 54` | b.cc 0x00bcee6c | `CONDITIONAL_JUMP`
<a id="insn-00bced14"></a> `00bced14` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bced18"></a> `00bced18` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00bced1c"></a> `00bced1c` | `ad 07 80 52` | mov w13,#0x3d | `FALL_THROUGH`
<a id="insn-00bced20"></a> `00bced20` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bced24"></a> `00bced24` | `ac 65 24 10` | adr x12,0xc179d8 | `FALL_THROUGH`
<a id="insn-00bced28"></a> `00bced28` | `04 00 00 14` | b 0x00bced38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bced2c"></a> `00bced2c` | `cb 05 00 91` | add x11,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bced30"></a> `00bced30` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bced34"></a> `00bced34` | `40 02 00 54` | b.eq 0x00bced7c | `CONDITIONAL_JUMP`
<a id="insn-00bced38"></a> `00bced38` | `6e 01 0d 8b` | add x14,x11,x13 | `FALL_THROUGH`
<a id="insn-00bced3c"></a> `00bced3c` | `ce fd 41 d3` | lsr x14,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bced40"></a> `00bced40` | `8f 11 0e 8b` | add x15,x12,x14, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bced44"></a> `00bced44` | `f0 01 40 39` | ldrb w16,[x15] | `FALL_THROUGH`
<a id="insn-00bced48"></a> `00bced48` | `1f 02 0a 6b` | cmp w16,w10 | `FALL_THROUGH`
<a id="insn-00bced4c"></a> `00bced4c` | `03 ff ff 54` | b.cc 0x00bced2c | `CONDITIONAL_JUMP`
<a id="insn-00bced50"></a> `00bced50` | `21 01 00 54` | b.ne 0x00bced74 | `CONDITIONAL_JUMP`
<a id="insn-00bced54"></a> `00bced54` | `ef 05 40 39` | ldrb w15,[x15, #0x1] | `FALL_THROUGH`
<a id="insn-00bced58"></a> `00bced58` | `10 05 40 39` | ldrb w16,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bced5c"></a> `00bced5c` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00bced60"></a> `00bced60` | `ef 27 9f 1a` | cset w15,cc | `FALL_THROUGH`
<a id="insn-00bced64"></a> `00bced64` | `ff 01 00 72` | tst w15,#0x1 | `FALL_THROUGH`
<a id="insn-00bced68"></a> `00bced68` | `6b 05 8e 9a` | csinc x11,x11,x14,eq | `FALL_THROUGH`
<a id="insn-00bced6c"></a> `00bced6c` | `ad 11 8e 9a` | csel x13,x13,x14,ne | `FALL_THROUGH`
<a id="insn-00bced70"></a> `00bced70` | `f0 ff ff 17` | b 0x00bced30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bced74"></a> `00bced74` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bced78"></a> `00bced78` | `ee ff ff 17` | b 0x00bced30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bced7c"></a> `00bced7c` | `8b 11 0b 8b` | add x11,x12,x11, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bced80"></a> `00bced80` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-00bced84"></a> `00bced84` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00bced88"></a> `00bced88` | `a1 06 00 54` | b.ne 0x00bcee5c | `CONDITIONAL_JUMP`
<a id="insn-00bced8c"></a> `00bced8c` | `6a 05 40 39` | ldrb w10,[x11, #0x1] | `FALL_THROUGH`
<a id="insn-00bced90"></a> `00bced90` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bced94"></a> `00bced94` | `5f 01 0c 6b` | cmp w10,w12 | `FALL_THROUGH`
<a id="insn-00bced98"></a> `00bced98` | `21 06 00 54` | b.ne 0x00bcee5c | `CONDITIONAL_JUMP`
<a id="insn-00bced9c"></a> `00bced9c` | `69 09 40 39` | ldrb w9,[x11, #0x2] | `FALL_THROUGH`
<a id="insn-00bceda0"></a> `00bceda0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bceda4"></a> `00bceda4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bceda8"></a> `00bceda8` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcedac"></a> `00bcedac` | `21 0f 00 54` | b.ne 0x00bcef90 | `CONDITIONAL_JUMP`
<a id="insn-00bcedb0"></a> `00bcedb0` | `14 24 4c 39` | ldrb w20,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00bcedb4"></a> `00bcedb4` | `3f 00 00 f1` | cmp x1,#0x0 | `FALL_THROUGH`
<a id="insn-00bcedb8"></a> `00bcedb8` | `15 20 4c 39` | ldrb w21,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00bcedbc"></a> `00bcedbc` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcedc0"></a> `00bcedc0` | `1f 20 0c 39` | strb wzr,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00bcedc4"></a> `00bcedc4` | `88 06 9f 1a` | csinc w8,w20,wzr,eq | `FALL_THROUGH`
<a id="insn-00bcedc8"></a> `00bcedc8` | `08 24 0c 39` | strb w8,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00bcedcc"></a> `00bcedcc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcedd0"></a> `00bcedd0` | `23 bc ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bcedd4"></a> `00bcedd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcedd8"></a> `00bcedd8` | `80 13 00 b4` | cbz x0,0x00bcf048 | `CONDITIONAL_JUMP`
<a id="insn-00bceddc"></a> `00bceddc` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcede0"></a> `00bcede0` | `77 00 00 b4` | cbz x23,0x00bcedec | `CONDITIONAL_JUMP`
<a id="insn-00bcede4"></a> `00bcede4` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcede8"></a> `00bcede8` | `e9 02 00 39` | strb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bcedec"></a> `00bcedec` | `17 99 49 f9` | ldr x23,[x8, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcedf0"></a> `00bcedf0` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bcedf4"></a> `00bcedf4` | `2a 41 3f d1` | sub x10,x9,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcedf8"></a> `00bcedf8` | `5f c5 3f b1` | cmn x10,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcedfc"></a> `00bcedfc` | `28 01 00 54` | b.hi 0x00bcee20 | `CONDITIONAL_JUMP`
<a id="insn-00bcee00"></a> `00bcee00` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcee04"></a> `00bcee04` | `f3 38 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee08"></a> `00bcee08` | `a0 12 00 b4` | cbz x0,0x00bcf05c | `CONDITIONAL_JUMP`
<a id="insn-00bcee0c"></a> `00bcee0c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bcee10"></a> `00bcee10` | `17 7c 00 a9` | stp x23,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcee14"></a> `00bcee14` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcee18"></a> `00bcee18` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcee1c"></a> `00bcee1c` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcee20"></a> `00bcee20` | `2a 81 00 91` | add x10,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcee24"></a> `00bcee24` | `e0 02 09 8b` | add x0,x23,x9 | `FALL_THROUGH`
<a id="insn-00bcee28"></a> `00bcee28` | `49 02 00 f0` | adrp x9,0xc19000 | `FALL_THROUGH`
<a id="insn-00bcee2c"></a> `00bcee2c` | `29 e1 05 91` | add x9,x9,#0x178 | `FALL_THROUGH`
<a id="insn-00bcee30"></a> `00bcee30` | `ea 06 00 f9` | str x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee34"></a> `00bcee34` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00bcee38"></a> `00bcee38` | `09 0c 01 f8` | str x9,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcee3c"></a> `00bcee3c` | `09 90 40 78` | ldurh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcee40"></a> `00bcee40` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00bcee44"></a> `00bcee44` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcee48"></a> `00bcee48` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcee4c"></a> `00bcee4c` | `0a 20 00 39` | strb w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee50"></a> `00bcee50` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00bcee54"></a> `00bcee54` | `09 90 00 78` | sturh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcee58"></a> `00bcee58` | `7e 00 00 14` | b 0x00bcf050 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcee5c"></a> `00bcee5c` | `0a 01 40 79` | ldrh w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcee60"></a> `00bcee60` | `8b 2d 8d 52` | mov w11,#0x696c | `FALL_THROUGH`
<a id="insn-00bcee64"></a> `00bcee64` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00bcee68"></a> `00bcee68` | `00 05 00 54` | b.eq 0x00bcef08 | `CONDITIONAL_JUMP`
<a id="insn-00bcee6c"></a> `00bcee6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcee70"></a> `00bcee70` | `40 09 00 54` | b.eq 0x00bcef98 | `CONDITIONAL_JUMP`
<a id="insn-00bcee74"></a> `00bcee74` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcee78"></a> `00bcee78` | `5f d9 01 71` | cmp w10,#0x76 | `FALL_THROUGH`
<a id="insn-00bcee7c"></a> `00bcee7c` | `e1 08 00 54` | b.ne 0x00bcef98 | `CONDITIONAL_JUMP`
<a id="insn-00bcee80"></a> `00bcee80` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcee84"></a> `00bcee84` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcee88"></a> `00bcee88` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bcee8c"></a> `00bcee8c` | `60 08 00 54` | b.eq 0x00bcef98 | `CONDITIONAL_JUMP`
<a id="insn-00bcee90"></a> `00bcee90` | `49 01 40 39` | ldrb w9,[x10] | `FALL_THROUGH`
<a id="insn-00bcee94"></a> `00bcee94` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bcee98"></a> `00bcee98` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bcee9c"></a> `00bcee9c` | `e8 07 00 54` | b.hi 0x00bcef98 | `CONDITIONAL_JUMP`
<a id="insn-00bceea0"></a> `00bceea0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bceea4"></a> `00bceea4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bceea8"></a> `00bceea8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bceeac"></a> `00bceeac` | `a5 c8 ff 97` | bl 0x00bc1140 | `UNCONDITIONAL_CALL`
<a id="insn-00bceeb0"></a> `00bceeb0` | `60 07 00 b4` | cbz x0,0x00bcef9c | `CONDITIONAL_JUMP`
<a id="insn-00bceeb4"></a> `00bceeb4` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bceeb8"></a> `00bceeb8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bceebc"></a> `00bceebc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bceec0"></a> `00bceec0` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bceec4"></a> `00bceec4` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bceec8"></a> `00bceec8` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bceecc"></a> `00bceecc` | `08 01 00 54` | b.hi 0x00bceeec | `CONDITIONAL_JUMP`
<a id="insn-00bceed0"></a> `00bceed0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bceed4"></a> `00bceed4` | `bf 38 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bceed8"></a> `00bceed8` | `20 0c 00 b4` | cbz x0,0x00bcf05c | `CONDITIONAL_JUMP`
<a id="insn-00bceedc"></a> `00bceedc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bceee0"></a> `00bceee0` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bceee4"></a> `00bceee4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bceee8"></a> `00bceee8` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bceeec"></a> `00bceeec` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bceef0"></a> `00bceef0` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bceef4"></a> `00bceef4` | `48 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bceef8"></a> `00bceef8` | `08 e1 05 91` | add x8,x8,#0x178 | `FALL_THROUGH`
<a id="insn-00bceefc"></a> `00bceefc` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef00"></a> `00bcef00` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bcef04"></a> `00bcef04` | `1a 00 00 14` | b 0x00bcef6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcef08"></a> `00bcef08` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcef0c"></a> `00bcef0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcef10"></a> `00bcef10` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcef14"></a> `00bcef14` | `8b c8 ff 97` | bl 0x00bc1140 | `UNCONDITIONAL_CALL`
<a id="insn-00bcef18"></a> `00bcef18` | `20 04 00 b4` | cbz x0,0x00bcef9c | `CONDITIONAL_JUMP`
<a id="insn-00bcef1c"></a> `00bcef1c` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcef20"></a> `00bcef20` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bcef24"></a> `00bcef24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcef28"></a> `00bcef28` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef2c"></a> `00bcef2c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcef30"></a> `00bcef30` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcef34"></a> `00bcef34` | `08 01 00 54` | b.hi 0x00bcef54 | `CONDITIONAL_JUMP`
<a id="insn-00bcef38"></a> `00bcef38` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcef3c"></a> `00bcef3c` | `a5 38 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcef40"></a> `00bcef40` | `e0 08 00 b4` | cbz x0,0x00bcf05c | `CONDITIONAL_JUMP`
<a id="insn-00bcef44"></a> `00bcef44` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcef48"></a> `00bcef48` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcef4c"></a> `00bcef4c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcef50"></a> `00bcef50` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcef54"></a> `00bcef54` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcef58"></a> `00bcef58` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bcef5c"></a> `00bcef5c` | `48 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bcef60"></a> `00bcef60` | `08 a1 07 91` | add x8,x8,#0x1e8 | `FALL_THROUGH`
<a id="insn-00bcef64"></a> `00bcef64` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef68"></a> `00bcef68` | `89 02 80 52` | mov w9,#0x14 | `FALL_THROUGH`
<a id="insn-00bcef6c"></a> `00bcef6c` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcef70"></a> `00bcef70` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcef74"></a> `00bcef74` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bcef78"></a> `00bcef78` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcef7c"></a> `00bcef7c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcef80"></a> `00bcef80` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bcef84"></a> `00bcef84` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcef88"></a> `00bcef88` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcef8c"></a> `00bcef8c` | `04 00 00 14` | b 0x00bcef9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcef90"></a> `00bcef90` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00bcef94"></a> `00bcef94` | `09 01 00 54` | b.ls 0x00bcefb4 | `CONDITIONAL_JUMP`
<a id="insn-00bcef98"></a> `00bcef98` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bcef9c"></a> `00bcef9c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcefa0"></a> `00bcefa0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcefa4"></a> `00bcefa4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcefa8"></a> `00bcefa8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcefac"></a> `00bcefac` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcefb0"></a> `00bcefb0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcefb4"></a> `00bcefb4` | `3f 11 00 71` | cmp w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bcefb8"></a> `00bcefb8` | `61 00 00 54` | b.ne 0x00bcefc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcefbc"></a> `00bcefbc` | `68 0d 40 39` | ldrb w8,[x11, #0x3] | `FALL_THROUGH`
<a id="insn-00bcefc0"></a> `00bcefc0` | `c8 fe 07 36` | tbz w8,#0x0,0x00bcef98 | `CONDITIONAL_JUMP`
<a id="insn-00bcefc4"></a> `00bcefc4` | `73 05 40 f9` | ldr x19,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcefc8"></a> `00bcefc8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcefcc"></a> `00bcefcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcefd0"></a> `00bcefd0` | `70 30 00 94` | bl 0x00bdb190 | `UNCONDITIONAL_CALL`
<a id="insn-00bcefd4"></a> `00bcefd4` | `95 9a 49 f9` | ldr x21,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcefd8"></a> `00bcefd8` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00bcefdc"></a> `00bcefdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcefe0"></a> `00bcefe0` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcefe4"></a> `00bcefe4` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcefe8"></a> `00bcefe8` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcefec"></a> `00bcefec` | `08 01 00 54` | b.hi 0x00bcf00c | `CONDITIONAL_JUMP`
<a id="insn-00bceff0"></a> `00bceff0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bceff4"></a> `00bceff4` | `77 38 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bceff8"></a> `00bceff8` | `20 03 00 b4` | cbz x0,0x00bcf05c | `CONDITIONAL_JUMP`
<a id="insn-00bceffc"></a> `00bceffc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcf000"></a> `00bcf000` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcf004"></a> `00bcf004` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcf008"></a> `00bcf008` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcf00c"></a> `00bcf00c` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf010"></a> `00bcf010` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bcf014"></a> `00bcf014` | `48 02 00 90` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bcf018"></a> `00bcf018` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bcf01c"></a> `00bcf01c` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf020"></a> `00bcf020` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bcf024"></a> `00bcf024` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcf028"></a> `00bcf028` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf02c"></a> `00bcf02c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcf030"></a> `00bcf030` | `13 50 01 a9` | stp x19,x20,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf034"></a> `00bcf034` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcf038"></a> `00bcf038` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf03c"></a> `00bcf03c` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bcf040"></a> `00bcf040` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf044"></a> `00bcf044` | `d6 ff ff 17` | b 0x00bcef9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf048"></a> `00bcf048` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bcf04c"></a> `00bcf04c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcf050"></a> `00bcf050` | `14 25 0c 39` | strb w20,[x8, #0x309] | `FALL_THROUGH`
<a id="insn-00bcf054"></a> `00bcf054` | `15 21 0c 39` | strb w21,[x8, #0x308] | `FALL_THROUGH`
<a id="insn-00bcf058"></a> `00bcf058` | `d1 ff ff 17` | b 0x00bcef9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf05c"></a> `00bcf05c` | `5d 30 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcecec`](#insn-00bcecec) 範囲 `[['00bcecec', '00bced13']]`
  - `CONDITIONAL_JUMP` [`00bced10`](#insn-00bced10) → [`00bcee6c`](#insn-00bcee6c)
  - `FALL_THROUGH` [`00bced10`](#insn-00bced10) → [`00bced14`](#insn-00bced14)
- ブロック [`00bced14`](#insn-00bced14) 範囲 `[['00bced14', '00bced2b']]`
  - `UNCONDITIONAL_JUMP` [`00bced28`](#insn-00bced28) → [`00bced38`](#insn-00bced38)
- ブロック [`00bced2c`](#insn-00bced2c) 範囲 `[['00bced2c', '00bced2f']]`
  - `FALL_THROUGH` [`00bced2c`](#insn-00bced2c) → [`00bced30`](#insn-00bced30)
- ブロック [`00bced30`](#insn-00bced30) 範囲 `[['00bced30', '00bced37']]`
  - `CONDITIONAL_JUMP` [`00bced34`](#insn-00bced34) → [`00bced7c`](#insn-00bced7c)
  - `FALL_THROUGH` [`00bced34`](#insn-00bced34) → [`00bced38`](#insn-00bced38)
- ブロック [`00bced38`](#insn-00bced38) 範囲 `[['00bced38', '00bced4f']]`
  - `CONDITIONAL_JUMP` [`00bced4c`](#insn-00bced4c) → [`00bced2c`](#insn-00bced2c)
  - `FALL_THROUGH` [`00bced4c`](#insn-00bced4c) → [`00bced50`](#insn-00bced50)
- ブロック [`00bced50`](#insn-00bced50) 範囲 `[['00bced50', '00bced53']]`
  - `CONDITIONAL_JUMP` [`00bced50`](#insn-00bced50) → [`00bced74`](#insn-00bced74)
  - `FALL_THROUGH` [`00bced50`](#insn-00bced50) → [`00bced54`](#insn-00bced54)
- ブロック [`00bced54`](#insn-00bced54) 範囲 `[['00bced54', '00bced5f']]`
  - `FALL_THROUGH` [`00bced5c`](#insn-00bced5c) → [`00bced60`](#insn-00bced60)
- ブロック [`00bced60`](#insn-00bced60) 範囲 `[['00bced60', '00bced73']]`
  - `UNCONDITIONAL_JUMP` [`00bced70`](#insn-00bced70) → [`00bced30`](#insn-00bced30)
- ブロック [`00bced74`](#insn-00bced74) 範囲 `[['00bced74', '00bced7b']]`
  - `UNCONDITIONAL_JUMP` [`00bced78`](#insn-00bced78) → [`00bced30`](#insn-00bced30)
- ブロック [`00bced7c`](#insn-00bced7c) 範囲 `[['00bced7c', '00bced87']]`
  - `FALL_THROUGH` [`00bced84`](#insn-00bced84) → [`00bced88`](#insn-00bced88)
- ブロック [`00bced88`](#insn-00bced88) 範囲 `[['00bced88', '00bced8b']]`
  - `CONDITIONAL_JUMP` [`00bced88`](#insn-00bced88) → [`00bcee5c`](#insn-00bcee5c)
  - `FALL_THROUGH` [`00bced88`](#insn-00bced88) → [`00bced8c`](#insn-00bced8c)
- ブロック [`00bced8c`](#insn-00bced8c) 範囲 `[['00bced8c', '00bced97']]`
  - `FALL_THROUGH` [`00bced94`](#insn-00bced94) → [`00bced98`](#insn-00bced98)
- ブロック [`00bced98`](#insn-00bced98) 範囲 `[['00bced98', '00bced9b']]`
  - `CONDITIONAL_JUMP` [`00bced98`](#insn-00bced98) → [`00bcee5c`](#insn-00bcee5c)
  - `FALL_THROUGH` [`00bced98`](#insn-00bced98) → [`00bced9c`](#insn-00bced9c)
- ブロック [`00bced9c`](#insn-00bced9c) 範囲 `[['00bced9c', '00bceda3']]`
  - `FALL_THROUGH` [`00bceda0`](#insn-00bceda0) → [`00bceda4`](#insn-00bceda4)
- ブロック [`00bceda4`](#insn-00bceda4) 範囲 `[['00bceda4', '00bcedaf']]`
  - `CONDITIONAL_JUMP` [`00bcedac`](#insn-00bcedac) → [`00bcef90`](#insn-00bcef90)
  - `FALL_THROUGH` [`00bcedac`](#insn-00bcedac) → [`00bcedb0`](#insn-00bcedb0)
- ブロック [`00bcedb0`](#insn-00bcedb0) 範囲 `[['00bcedb0', '00bcedb7']]`
  - `FALL_THROUGH` [`00bcedb4`](#insn-00bcedb4) → [`00bcedb8`](#insn-00bcedb8)
- ブロック [`00bcedb8`](#insn-00bcedb8) 範囲 `[['00bcedb8', '00bcedc3']]`
  - `FALL_THROUGH` [`00bcedc0`](#insn-00bcedc0) → [`00bcedc4`](#insn-00bcedc4)
- ブロック [`00bcedc4`](#insn-00bcedc4) 範囲 `[['00bcedc4', '00bcedd3']]`
  - `FALL_THROUGH` [`00bcedd0`](#insn-00bcedd0) → [`00bcedd4`](#insn-00bcedd4)
- ブロック [`00bcedd4`](#insn-00bcedd4) 範囲 `[['00bcedd4', '00bceddb']]`
  - `CONDITIONAL_JUMP` [`00bcedd8`](#insn-00bcedd8) → [`00bcf048`](#insn-00bcf048)
  - `FALL_THROUGH` [`00bcedd8`](#insn-00bcedd8) → [`00bceddc`](#insn-00bceddc)
- ブロック [`00bceddc`](#insn-00bceddc) 範囲 `[['00bceddc', '00bcede3']]`
  - `CONDITIONAL_JUMP` [`00bcede0`](#insn-00bcede0) → [`00bcedec`](#insn-00bcedec)
  - `FALL_THROUGH` [`00bcede0`](#insn-00bcede0) → [`00bcede4`](#insn-00bcede4)
- ブロック [`00bcede4`](#insn-00bcede4) 範囲 `[['00bcede4', '00bcedeb']]`
  - `FALL_THROUGH` [`00bcede8`](#insn-00bcede8) → [`00bcedec`](#insn-00bcedec)
- ブロック [`00bcedec`](#insn-00bcedec) 範囲 `[['00bcedec', '00bcedff']]`
  - `CONDITIONAL_JUMP` [`00bcedfc`](#insn-00bcedfc) → [`00bcee20`](#insn-00bcee20)
  - `FALL_THROUGH` [`00bcedfc`](#insn-00bcedfc) → [`00bcee00`](#insn-00bcee00)
- ブロック [`00bcee00`](#insn-00bcee00) 範囲 `[['00bcee00', '00bcee0b']]`
  - `CONDITIONAL_JUMP` [`00bcee08`](#insn-00bcee08) → [`00bcf05c`](#insn-00bcf05c)
  - `FALL_THROUGH` [`00bcee08`](#insn-00bcee08) → [`00bcee0c`](#insn-00bcee0c)
- ブロック [`00bcee0c`](#insn-00bcee0c) 範囲 `[['00bcee0c', '00bcee1f']]`
  - `FALL_THROUGH` [`00bcee1c`](#insn-00bcee1c) → [`00bcee20`](#insn-00bcee20)
- ブロック [`00bcee20`](#insn-00bcee20) 範囲 `[['00bcee20', '00bcee53']]`
  - `FALL_THROUGH` [`00bcee50`](#insn-00bcee50) → [`00bcee54`](#insn-00bcee54)
- ブロック [`00bcee54`](#insn-00bcee54) 範囲 `[['00bcee54', '00bcee5b']]`
  - `UNCONDITIONAL_JUMP` [`00bcee58`](#insn-00bcee58) → [`00bcf050`](#insn-00bcf050)
- ブロック [`00bcee5c`](#insn-00bcee5c) 範囲 `[['00bcee5c', '00bcee6b']]`
  - `CONDITIONAL_JUMP` [`00bcee68`](#insn-00bcee68) → [`00bcef08`](#insn-00bcef08)
  - `FALL_THROUGH` [`00bcee68`](#insn-00bcee68) → [`00bcee6c`](#insn-00bcee6c)
- ブロック [`00bcee6c`](#insn-00bcee6c) 範囲 `[['00bcee6c', '00bcee73']]`
  - `CONDITIONAL_JUMP` [`00bcee70`](#insn-00bcee70) → [`00bcef98`](#insn-00bcef98)
  - `FALL_THROUGH` [`00bcee70`](#insn-00bcee70) → [`00bcee74`](#insn-00bcee74)
- ブロック [`00bcee74`](#insn-00bcee74) 範囲 `[['00bcee74', '00bcee7f']]`
  - `CONDITIONAL_JUMP` [`00bcee7c`](#insn-00bcee7c) → [`00bcef98`](#insn-00bcef98)
  - `FALL_THROUGH` [`00bcee7c`](#insn-00bcee7c) → [`00bcee80`](#insn-00bcee80)
- ブロック [`00bcee80`](#insn-00bcee80) 範囲 `[['00bcee80', '00bcee8f']]`
  - `CONDITIONAL_JUMP` [`00bcee8c`](#insn-00bcee8c) → [`00bcef98`](#insn-00bcef98)
  - `FALL_THROUGH` [`00bcee8c`](#insn-00bcee8c) → [`00bcee90`](#insn-00bcee90)
- ブロック [`00bcee90`](#insn-00bcee90) 範囲 `[['00bcee90', '00bcee93']]`
  - `FALL_THROUGH` [`00bcee90`](#insn-00bcee90) → [`00bcee94`](#insn-00bcee94)
- ブロック [`00bcee94`](#insn-00bcee94) 範囲 `[['00bcee94', '00bcee9f']]`
  - `CONDITIONAL_JUMP` [`00bcee9c`](#insn-00bcee9c) → [`00bcef98`](#insn-00bcef98)
  - `FALL_THROUGH` [`00bcee9c`](#insn-00bcee9c) → [`00bceea0`](#insn-00bceea0)
- ブロック [`00bceea0`](#insn-00bceea0) 範囲 `[['00bceea0', '00bceeaf']]`
  - `FALL_THROUGH` [`00bceeac`](#insn-00bceeac) → [`00bceeb0`](#insn-00bceeb0)
- ブロック [`00bceeb0`](#insn-00bceeb0) 範囲 `[['00bceeb0', '00bceeb3']]`
  - `CONDITIONAL_JUMP` [`00bceeb0`](#insn-00bceeb0) → [`00bcef9c`](#insn-00bcef9c)
  - `FALL_THROUGH` [`00bceeb0`](#insn-00bceeb0) → [`00bceeb4`](#insn-00bceeb4)
- ブロック [`00bceeb4`](#insn-00bceeb4) 範囲 `[['00bceeb4', '00bceec7']]`
  - `FALL_THROUGH` [`00bceec4`](#insn-00bceec4) → [`00bceec8`](#insn-00bceec8)
- ブロック [`00bceec8`](#insn-00bceec8) 範囲 `[['00bceec8', '00bceecf']]`
  - `CONDITIONAL_JUMP` [`00bceecc`](#insn-00bceecc) → [`00bceeec`](#insn-00bceeec)
  - `FALL_THROUGH` [`00bceecc`](#insn-00bceecc) → [`00bceed0`](#insn-00bceed0)
- ブロック [`00bceed0`](#insn-00bceed0) 範囲 `[['00bceed0', '00bceedb']]`
  - `CONDITIONAL_JUMP` [`00bceed8`](#insn-00bceed8) → [`00bcf05c`](#insn-00bcf05c)
  - `FALL_THROUGH` [`00bceed8`](#insn-00bceed8) → [`00bceedc`](#insn-00bceedc)
- ブロック [`00bceedc`](#insn-00bceedc) 範囲 `[['00bceedc', '00bceeeb']]`
  - `FALL_THROUGH` [`00bceee8`](#insn-00bceee8) → [`00bceeec`](#insn-00bceeec)
- ブロック [`00bceeec`](#insn-00bceeec) 範囲 `[['00bceeec', '00bcef07']]`
  - `UNCONDITIONAL_JUMP` [`00bcef04`](#insn-00bcef04) → [`00bcef6c`](#insn-00bcef6c)
- ブロック [`00bcef08`](#insn-00bcef08) 範囲 `[['00bcef08', '00bcef1b']]`
  - `CONDITIONAL_JUMP` [`00bcef18`](#insn-00bcef18) → [`00bcef9c`](#insn-00bcef9c)
  - `FALL_THROUGH` [`00bcef18`](#insn-00bcef18) → [`00bcef1c`](#insn-00bcef1c)
- ブロック [`00bcef1c`](#insn-00bcef1c) 範囲 `[['00bcef1c', '00bcef37']]`
  - `CONDITIONAL_JUMP` [`00bcef34`](#insn-00bcef34) → [`00bcef54`](#insn-00bcef54)
  - `FALL_THROUGH` [`00bcef34`](#insn-00bcef34) → [`00bcef38`](#insn-00bcef38)
- ブロック [`00bcef38`](#insn-00bcef38) 範囲 `[['00bcef38', '00bcef43']]`
  - `CONDITIONAL_JUMP` [`00bcef40`](#insn-00bcef40) → [`00bcf05c`](#insn-00bcf05c)
  - `FALL_THROUGH` [`00bcef40`](#insn-00bcef40) → [`00bcef44`](#insn-00bcef44)
- ブロック [`00bcef44`](#insn-00bcef44) 範囲 `[['00bcef44', '00bcef53']]`
  - `FALL_THROUGH` [`00bcef50`](#insn-00bcef50) → [`00bcef54`](#insn-00bcef54)
- ブロック [`00bcef54`](#insn-00bcef54) 範囲 `[['00bcef54', '00bcef6b']]`
  - `FALL_THROUGH` [`00bcef68`](#insn-00bcef68) → [`00bcef6c`](#insn-00bcef6c)
- ブロック [`00bcef6c`](#insn-00bcef6c) 範囲 `[['00bcef6c', '00bcef8f']]`
  - `UNCONDITIONAL_JUMP` [`00bcef8c`](#insn-00bcef8c) → [`00bcef9c`](#insn-00bcef9c)
- ブロック [`00bcef90`](#insn-00bcef90) 範囲 `[['00bcef90', '00bcef97']]`
  - `CONDITIONAL_JUMP` [`00bcef94`](#insn-00bcef94) → [`00bcefb4`](#insn-00bcefb4)
  - `FALL_THROUGH` [`00bcef94`](#insn-00bcef94) → [`00bcef98`](#insn-00bcef98)
- ブロック [`00bcef98`](#insn-00bcef98) 範囲 `[['00bcef98', '00bcef9b']]`
  - `FALL_THROUGH` [`00bcef98`](#insn-00bcef98) → [`00bcef9c`](#insn-00bcef9c)
- ブロック [`00bcef9c`](#insn-00bcef9c) 範囲 `[['00bcef9c', '00bcefb3']]`
- ブロック [`00bcefb4`](#insn-00bcefb4) 範囲 `[['00bcefb4', '00bcefbb']]`
  - `CONDITIONAL_JUMP` [`00bcefb8`](#insn-00bcefb8) → [`00bcefc4`](#insn-00bcefc4)
  - `FALL_THROUGH` [`00bcefb8`](#insn-00bcefb8) → [`00bcefbc`](#insn-00bcefbc)
- ブロック [`00bcefbc`](#insn-00bcefbc) 範囲 `[['00bcefbc', '00bcefc3']]`
  - `CONDITIONAL_JUMP` [`00bcefc0`](#insn-00bcefc0) → [`00bcef98`](#insn-00bcef98)
  - `FALL_THROUGH` [`00bcefc0`](#insn-00bcefc0) → [`00bcefc4`](#insn-00bcefc4)
- ブロック [`00bcefc4`](#insn-00bcefc4) 範囲 `[['00bcefc4', '00bcefc7']]`
  - `FALL_THROUGH` [`00bcefc4`](#insn-00bcefc4) → [`00bcefc8`](#insn-00bcefc8)
- ブロック [`00bcefc8`](#insn-00bcefc8) 範囲 `[['00bcefc8', '00bcefef']]`
  - `CONDITIONAL_JUMP` [`00bcefec`](#insn-00bcefec) → [`00bcf00c`](#insn-00bcf00c)
  - `FALL_THROUGH` [`00bcefec`](#insn-00bcefec) → [`00bceff0`](#insn-00bceff0)
- ブロック [`00bceff0`](#insn-00bceff0) 範囲 `[['00bceff0', '00bceffb']]`
  - `CONDITIONAL_JUMP` [`00bceff8`](#insn-00bceff8) → [`00bcf05c`](#insn-00bcf05c)
  - `FALL_THROUGH` [`00bceff8`](#insn-00bceff8) → [`00bceffc`](#insn-00bceffc)
- ブロック [`00bceffc`](#insn-00bceffc) 範囲 `[['00bceffc', '00bcefff']]`
  - `FALL_THROUGH` [`00bceffc`](#insn-00bceffc) → [`00bcf000`](#insn-00bcf000)
- ブロック [`00bcf000`](#insn-00bcf000) 範囲 `[['00bcf000', '00bcf00b']]`
  - `FALL_THROUGH` [`00bcf008`](#insn-00bcf008) → [`00bcf00c`](#insn-00bcf00c)
- ブロック [`00bcf00c`](#insn-00bcf00c) 範囲 `[['00bcf00c', '00bcf01b']]`
  - `FALL_THROUGH` [`00bcf018`](#insn-00bcf018) → [`00bcf01c`](#insn-00bcf01c)
- ブロック [`00bcf01c`](#insn-00bcf01c) 範囲 `[['00bcf01c', '00bcf033']]`
  - `FALL_THROUGH` [`00bcf030`](#insn-00bcf030) → [`00bcf034`](#insn-00bcf034)
- ブロック [`00bcf034`](#insn-00bcf034) 範囲 `[['00bcf034', '00bcf047']]`
  - `UNCONDITIONAL_JUMP` [`00bcf044`](#insn-00bcf044) → [`00bcef9c`](#insn-00bcef9c)
- ブロック [`00bcf048`](#insn-00bcf048) 範囲 `[['00bcf048', '00bcf04f']]`
  - `FALL_THROUGH` [`00bcf04c`](#insn-00bcf04c) → [`00bcf050`](#insn-00bcf050)
- ブロック [`00bcf050`](#insn-00bcf050) 範囲 `[['00bcf050', '00bcf05b']]`
  - `UNCONDITIONAL_JUMP` [`00bcf058`](#insn-00bcf058) → [`00bcef9c`](#insn-00bcef9c)
- ブロック [`00bcf05c`](#insn-00bcf05c) 範囲 `[['00bcf05c', '00bcf05f']]`

## 命令位置別の参照

- [`00bcecf0`](#insn-00bcecf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf4`](#insn-00bcecf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf8`](#insn-00bcecf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecfc`](#insn-00bcecfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced10`](#insn-00bced10) → [`00bcee6c`](#insn-00bcee6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced28`](#insn-00bced28) → [`00bced38`](#insn-00bced38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced34`](#insn-00bced34) → [`00bced7c`](#insn-00bced7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced44`](#insn-00bced44) → `00c17bb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced4c`](#insn-00bced4c) → [`00bced2c`](#insn-00bced2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced50`](#insn-00bced50) → [`00bced74`](#insn-00bced74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced54`](#insn-00bced54) → `00c17bb9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced70`](#insn-00bced70) → [`00bced30`](#insn-00bced30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced78`](#insn-00bced78) → [`00bced30`](#insn-00bced30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced80`](#insn-00bced80) → `00c17bc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced88`](#insn-00bced88) → [`00bcee5c`](#insn-00bcee5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced8c`](#insn-00bced8c) → `00c17bc9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bced98`](#insn-00bced98) → [`00bcee5c`](#insn-00bcee5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced9c`](#insn-00bced9c) → `00c17bca`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcedac`](#insn-00bcedac) → [`00bcef90`](#insn-00bcef90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedd0`](#insn-00bcedd0) → [`00bbde5c`](../00bbd/00bbde5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bcedd8`](#insn-00bcedd8) → [`00bcf048`](#insn-00bcf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcede0`](#insn-00bcede0) → [`00bcedec`](#insn-00bcedec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedfc`](#insn-00bcedfc) → [`00bcee20`](#insn-00bcee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee04`](#insn-00bcee04) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcee08`](#insn-00bcee08) → [`00bcf05c`](#insn-00bcf05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee38`](#insn-00bcee38) → `00c19178`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcee58`](#insn-00bcee58) → [`00bcf050`](#insn-00bcf050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee68`](#insn-00bcee68) → [`00bcef08`](#insn-00bcef08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee70`](#insn-00bcee70) → [`00bcef98`](#insn-00bcef98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee7c`](#insn-00bcee7c) → [`00bcef98`](#insn-00bcef98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee8c`](#insn-00bcee8c) → [`00bcef98`](#insn-00bcef98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee9c`](#insn-00bcee9c) → [`00bcef98`](#insn-00bcef98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceeac`](#insn-00bceeac) → [`00bc1140`](../00bc1/00bc1140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1140` · 推定シンボル `None` · 推定型 `None`
- [`00bceeb0`](#insn-00bceeb0) → [`00bcef9c`](#insn-00bcef9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceecc`](#insn-00bceecc) → [`00bceeec`](#insn-00bceeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceed4`](#insn-00bceed4) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bceed8`](#insn-00bceed8) → [`00bcf05c`](#insn-00bcf05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef04`](#insn-00bcef04) → [`00bcef6c`](#insn-00bcef6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef14`](#insn-00bcef14) → [`00bc1140`](../00bc1/00bc1140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1140` · 推定シンボル `None` · 推定型 `None`
- [`00bcef18`](#insn-00bcef18) → [`00bcef9c`](#insn-00bcef9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef34`](#insn-00bcef34) → [`00bcef54`](#insn-00bcef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef3c`](#insn-00bcef3c) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcef40`](#insn-00bcef40) → [`00bcf05c`](#insn-00bcf05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef6c`](#insn-00bcef6c) → `00c19178`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcef6c`](#insn-00bcef6c) → `00c191e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcef8c`](#insn-00bcef8c) → [`00bcef9c`](#insn-00bcef9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef94`](#insn-00bcef94) → [`00bcefb4`](#insn-00bcefb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef9c`](#insn-00bcef9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefa0`](#insn-00bcefa0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefa4`](#insn-00bcefa4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefa8`](#insn-00bcefa8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefb8`](#insn-00bcefb8) → [`00bcefc4`](#insn-00bcefc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefbc`](#insn-00bcefbc) → `00c17bcb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcefc0`](#insn-00bcefc0) → [`00bcef98`](#insn-00bcef98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefc4`](#insn-00bcefc4) → `00c17bd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcefcc`](#insn-00bcefcc) → `002b09e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcefd0`](#insn-00bcefd0) → [`00bdb190`](../00bdb/00bdb190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb190` · 推定シンボル `None` · 推定型 `None`
- [`00bcefec`](#insn-00bcefec) → [`00bcf00c`](#insn-00bcf00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceff4`](#insn-00bceff4) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bceff8`](#insn-00bceff8) → [`00bcf05c`](#insn-00bcf05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf024`](#insn-00bcf024) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcf030`](#insn-00bcf030) → `002b09e1`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf044`](#insn-00bcf044) → [`00bcef9c`](#insn-00bcef9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf058`](#insn-00bcf058) → [`00bcef9c`](#insn-00bcef9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf05c`](#insn-00bcf05c) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcecf0`](#insn-00bcecf0)

~~~json
{
  "source": "00bcecf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecf4`](#insn-00bcecf4)

~~~json
{
  "source": "00bcecf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecf8`](#insn-00bcecf8)

~~~json
{
  "source": "00bcecf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecfc`](#insn-00bcecfc)

~~~json
{
  "source": "00bcecfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced10`](#insn-00bced10)

~~~json
{
  "source": "00bced10",
  "target": "00bcee6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced28`](#insn-00bced28)

~~~json
{
  "source": "00bced28",
  "target": "00bced38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced34`](#insn-00bced34)

~~~json
{
  "source": "00bced34",
  "target": "00bced7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced44`](#insn-00bced44)

~~~json
{
  "source": "00bced44",
  "target": "00c17bb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17bb8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6c",
  "capture_start": "00c17bb8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced4c`](#insn-00bced4c)

~~~json
{
  "source": "00bced4c",
  "target": "00bced2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced50`](#insn-00bced50)

~~~json
{
  "source": "00bced50",
  "target": "00bced74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced54`](#insn-00bced54)

~~~json
{
  "source": "00bced54",
  "target": "00c17bb9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17bb9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "74",
  "capture_start": "00c17bb9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced70`](#insn-00bced70)

~~~json
{
  "source": "00bced70",
  "target": "00bced30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced78`](#insn-00bced78)

~~~json
{
  "source": "00bced78",
  "target": "00bced30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced80`](#insn-00bced80)

~~~json
{
  "source": "00bced80",
  "target": "00c17bc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17bc8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6d",
  "capture_start": "00c17bc8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced88`](#insn-00bced88)

~~~json
{
  "source": "00bced88",
  "target": "00bcee5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced8c`](#insn-00bced8c)

~~~json
{
  "source": "00bced8c",
  "target": "00c17bc9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17bc9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "49",
  "capture_start": "00c17bc9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bced98`](#insn-00bced98)

~~~json
{
  "source": "00bced98",
  "target": "00bcee5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced9c`](#insn-00bced9c)

~~~json
{
  "source": "00bced9c",
  "target": "00c17bca",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17bca",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "02",
  "capture_start": "00c17bca",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcedac`](#insn-00bcedac)

~~~json
{
  "source": "00bcedac",
  "target": "00bcef90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedd0`](#insn-00bcedd0)

~~~json
{
  "source": "00bcedd0",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedd8`](#insn-00bcedd8)

~~~json
{
  "source": "00bcedd8",
  "target": "00bcf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcede0`](#insn-00bcede0)

~~~json
{
  "source": "00bcede0",
  "target": "00bcedec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedfc`](#insn-00bcedfc)

~~~json
{
  "source": "00bcedfc",
  "target": "00bcee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee04`](#insn-00bcee04)

~~~json
{
  "source": "00bcee04",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee08`](#insn-00bcee08)

~~~json
{
  "source": "00bcee08",
  "target": "00bcf05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee38`](#insn-00bcee38)

~~~json
{
  "source": "00bcee38",
  "target": "00c19178",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19178",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcee58`](#insn-00bcee58)

~~~json
{
  "source": "00bcee58",
  "target": "00bcf050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee68`](#insn-00bcee68)

~~~json
{
  "source": "00bcee68",
  "target": "00bcef08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee70`](#insn-00bcee70)

~~~json
{
  "source": "00bcee70",
  "target": "00bcef98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee7c`](#insn-00bcee7c)

~~~json
{
  "source": "00bcee7c",
  "target": "00bcef98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee8c`](#insn-00bcee8c)

~~~json
{
  "source": "00bcee8c",
  "target": "00bcef98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee9c`](#insn-00bcee9c)

~~~json
{
  "source": "00bcee9c",
  "target": "00bcef98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceeac`](#insn-00bceeac)

~~~json
{
  "source": "00bceeac",
  "target": "00bc1140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceeb0`](#insn-00bceeb0)

~~~json
{
  "source": "00bceeb0",
  "target": "00bcef9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceecc`](#insn-00bceecc)

~~~json
{
  "source": "00bceecc",
  "target": "00bceeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceed4`](#insn-00bceed4)

~~~json
{
  "source": "00bceed4",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceed8`](#insn-00bceed8)

~~~json
{
  "source": "00bceed8",
  "target": "00bcf05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef04`](#insn-00bcef04)

~~~json
{
  "source": "00bcef04",
  "target": "00bcef6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef14`](#insn-00bcef14)

~~~json
{
  "source": "00bcef14",
  "target": "00bc1140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcef18`](#insn-00bcef18)

~~~json
{
  "source": "00bcef18",
  "target": "00bcef9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef34`](#insn-00bcef34)

~~~json
{
  "source": "00bcef34",
  "target": "00bcef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef3c`](#insn-00bcef3c)

~~~json
{
  "source": "00bcef3c",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcef40`](#insn-00bcef40)

~~~json
{
  "source": "00bcef40",
  "target": "00bcf05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef6c`](#insn-00bcef6c)

~~~json
{
  "source": "00bcef6c",
  "target": "00c19178",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19178",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcef6c`](#insn-00bcef6c)

~~~json
{
  "source": "00bcef6c",
  "target": "00c191e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c191e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcef8c`](#insn-00bcef8c)

~~~json
{
  "source": "00bcef8c",
  "target": "00bcef9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef94`](#insn-00bcef94)

~~~json
{
  "source": "00bcef94",
  "target": "00bcefb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef9c`](#insn-00bcef9c)

~~~json
{
  "source": "00bcef9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefa0`](#insn-00bcefa0)

~~~json
{
  "source": "00bcefa0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefa4`](#insn-00bcefa4)

~~~json
{
  "source": "00bcefa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefa8`](#insn-00bcefa8)

~~~json
{
  "source": "00bcefa8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefb8`](#insn-00bcefb8)

~~~json
{
  "source": "00bcefb8",
  "target": "00bcefc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefbc`](#insn-00bcefbc)

~~~json
{
  "source": "00bcefbc",
  "target": "00c17bcb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17bcb",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "22",
  "capture_start": "00c17bcb",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcefc0`](#insn-00bcefc0)

~~~json
{
  "source": "00bcefc0",
  "target": "00bcef98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefc4`](#insn-00bcefc4)

~~~json
{
  "source": "00bcefc4",
  "target": "00c17bd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17bd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcefcc`](#insn-00bcefcc)

~~~json
{
  "source": "00bcefcc",
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
- 参照命令 [`00bcefd0`](#insn-00bcefd0)

~~~json
{
  "source": "00bcefd0",
  "target": "00bdb190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcefec`](#insn-00bcefec)

~~~json
{
  "source": "00bcefec",
  "target": "00bcf00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceff4`](#insn-00bceff4)

~~~json
{
  "source": "00bceff4",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceff8`](#insn-00bceff8)

~~~json
{
  "source": "00bceff8",
  "target": "00bcf05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf024`](#insn-00bcf024)

~~~json
{
  "source": "00bcf024",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcf030`](#insn-00bcf030)

~~~json
{
  "source": "00bcf030",
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
- 参照命令 [`00bcf044`](#insn-00bcf044)

~~~json
{
  "source": "00bcf044",
  "target": "00bcef9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf058`](#insn-00bcf058)

~~~json
{
  "source": "00bcf058",
  "target": "00bcef9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf05c`](#insn-00bcf05c)

~~~json
{
  "source": "00bcf05c",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
