# 00adcadc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adca98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-4cadd9d85cad6c81d3751fc68ba060d6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3c4b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-ed43c51b69b3258644ad9ff47d0ee28f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adcadc",
  "name": "FUN_00adcadc",
  "size": 488,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "532cd19c8823ce97fdb34764dc68c96694b2ae14075d80ef78ee46a9686a8623",
  "source_text_sha256": "532cd19c8823ce97fdb34764dc68c96694b2ae14075d80ef78ee46a9686a8623",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adcadc",
        "00adccc3"
      ]
    ],
    "bytes_sha256": "f61239b6191cc6d8a5cce38ba20638158a86311d15e1db115b904254a48a37ec",
    "instruction_count": 122,
    "instruction_bytes": 488,
    "body_bytes": 488,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004222e0](../00422/004222e0.md)
- [00453c78](../00453/00453c78.md)
- [0046aa44](../0046a/0046aa44.md)
- [0046c588](../0046c/0046c588.md)
- [0073496c](../00734/0073496c.md)
- [0073a038](../0073a/0073a038.md)
- [0073ab94](../0073a/0073ab94.md)
- [0073addc](../0073a/0073addc.md)
- [0073b3dc](../0073b/0073b3dc.md)
- [0073de68](../0073d/0073de68.md)
- [0073e258](../0073e/0073e258.md)
- [0073e4a4](../0073e/0073e4a4.md)
- [0073e6dc](../0073e/0073e6dc.md)
- [0073e890](../0073e/0073e890.md)
- [0073eb44](../0073e/0073eb44.md)
- [0073ed78](../0073e/0073ed78.md)
- [0084642c](../00846/0084642c.md)
- [00846bdc](../00846/00846bdc.md)
- [009ce214](../009ce/009ce214.md)
- [00acc348](../00acc/00acc348.md)

## 呼び出し先

- [00418c24](../00418/00418c24.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb240](../00bdb/00bdb240.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7303 bytes

~~~c

void FUN_00adcadc(ulong *param_1,long *param_2)

{
  undefined1 (*pauVar1) [16];
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *pbVar6;
  byte *pbVar7;
  ulong uVar8;
  long lVar9;
  undefined1 (*pauVar10) [16];
  ulong uVar11;
  byte *pbVar12;
  ulong uVar13;
  byte *pbVar14;
  undefined8 uVar15;
  undefined1 auVar16 [16];
  undefined8 uVar17;
  undefined1 auVar18 [16];
  undefined8 uVar19;
  undefined8 uVar20;
  
  lVar9 = *param_2;
  lVar2 = param_2[1];
  uVar13 = lVar2 - lVar9;
  if (0xfffffffffffffff7 < uVar13) {
                    /* WARNING: Subroutine does not return */
    FUN_00418c24(param_1);
  }
  if (uVar13 < 0x17) {
    pbVar14 = (byte *)((long)param_1 + 1);
    *(byte *)param_1 = (byte)((int)uVar13 << 1);
    if (lVar2 != lVar9) goto LAB_00adcb58;
  }
  else {
    uVar11 = (uVar13 & 0xfffffffffffffff8) + 8;
    if ((uVar13 | 7) != 0x17) {
      uVar11 = uVar13 | 7;
    }
    pbVar14 = (byte *)_Znwm(uVar11 + 1);
    param_1[1] = uVar13;
    param_1[2] = (ulong)pbVar14;
    *param_1 = uVar11 + 1 | 1;
LAB_00adcb58:
    memset(pbVar14,0x58,uVar13);
  }
                    /* try { // try from 00adcb68 to 00bdcb73 has its CatchHandler @ 00adcb7c */
  pbVar14[uVar13] = 0;
  pbVar14 = (byte *)*param_2;
  pbVar3 = (byte *)param_2[1];
  if ((long)pbVar14 - (long)pbVar3 == 0) {
    return;
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00adcb68 with catch @ 00adcb7c
                        */
  pbVar6 = (byte *)param_1[2];
  uVar13 = (long)pbVar3 - (long)pbVar14;
  if ((*param_1 & 1) == 0) {
    pbVar6 = (byte *)((long)param_1 + 1);
  }
  pbVar7 = (byte *)param_2[4];
  pbVar4 = pbVar14;
  pbVar5 = pbVar6;
  if (7 < uVar13) {
    if ((pbVar6 + uVar13 <= pbVar14 || pbVar3 <= pbVar6) &&
       (pbVar7 <= pbVar6 || pbVar6 + uVar13 <= pbVar7 + ((long)pbVar14 - (long)pbVar3))) {
      if (uVar13 < 0x20) {
        uVar8 = 0;
      }
      else {
        uVar8 = uVar13 & 0xffffffffffffffe0;
        pauVar10 = (undefined1 (*) [16])(pbVar7 + -0x10);
        pbVar5 = pbVar14 + 0x10;
        pbVar4 = pbVar6 + 0x10;
        uVar11 = uVar8;
        do {
          pauVar1 = pauVar10 + -1;
          auVar16 = *pauVar10;
          uVar11 = uVar11 - 0x20;
          uVar17 = *(undefined8 *)(pbVar5 + -8);
          uVar15 = *(undefined8 *)(pbVar5 + -0x10);
          uVar20 = *(undefined8 *)(pbVar5 + 8);
          uVar19 = *(undefined8 *)pbVar5;
          pauVar10 = pauVar10 + -2;
          pbVar5 = pbVar5 + 0x20;
          auVar16 = NEON_rev64(auVar16,1);
          auVar18 = NEON_rev64(*pauVar1,1);
          auVar16 = NEON_ext(auVar16,auVar16,8,1);
          auVar18 = NEON_ext(auVar18,auVar18,8,1);
          pbVar4[-8] = auVar16[8] ^ (byte)uVar17;
          pbVar4[-7] = auVar16[9] ^ (byte)((ulong)uVar17 >> 8);
          pbVar4[-6] = auVar16[10] ^ (byte)((ulong)uVar17 >> 0x10);
          pbVar4[-5] = auVar16[0xb] ^ (byte)((ulong)uVar17 >> 0x18);
          pbVar4[-4] = auVar16[0xc] ^ (byte)((ulong)uVar17 >> 0x20);
          pbVar4[-3] = auVar16[0xd] ^ (byte)((ulong)uVar17 >> 0x28);
          pbVar4[-2] = auVar16[0xe] ^ (byte)((ulong)uVar17 >> 0x30);
          pbVar4[-1] = auVar16[0xf] ^ (byte)((ulong)uVar17 >> 0x38);
          pbVar4[-0x10] = auVar16[0] ^ (byte)uVar15;
          pbVar4[-0xf] = auVar16[1] ^ (byte)((ulong)uVar15 >> 8);
          pbVar4[-0xe] = auVar16[2] ^ (byte)((ulong)uVar15 >> 0x10);
          pbVar4[-0xd] = auVar16[3] ^ (byte)((ulong)uVar15 >> 0x18);
          pbVar4[-0xc] = auVar16[4] ^ (byte)((ulong)uVar15 >> 0x20);
          pbVar4[-0xb] = auVar16[5] ^ (byte)((ulong)uVar15 >> 0x28);
          pbVar4[-10] = auVar16[6] ^ (byte)((ulong)uVar15 >> 0x30);
          pbVar4[-9] = auVar16[7] ^ (byte)((ulong)uVar15 >> 0x38);
          pbVar4[8] = auVar18[8] ^ (byte)uVar20;
          pbVar4[9] = auVar18[9] ^ (byte)((ulong)uVar20 >> 8);
          pbVar4[10] = auVar18[10] ^ (byte)((ulong)uVar20 >> 0x10);
          pbVar4[0xb] = auVar18[0xb] ^ (byte)((ulong)uVar20 >> 0x18);
          pbVar4[0xc] = auVar18[0xc] ^ (byte)((ulong)uVar20 >> 0x20);
          pbVar4[0xd] = auVar18[0xd] ^ (byte)((ulong)uVar20 >> 0x28);
          pbVar4[0xe] = auVar18[0xe] ^ (byte)((ulong)uVar20 >> 0x30);
          pbVar4[0xf] = auVar18[0xf] ^ (byte)((ulong)uVar20 >> 0x38);
          *pbVar4 = auVar18[0] ^ (byte)uVar19;
          pbVar4[1] = auVar18[1] ^ (byte)((ulong)uVar19 >> 8);
          pbVar4[2] = auVar18[2] ^ (byte)((ulong)uVar19 >> 0x10);
          pbVar4[3] = auVar18[3] ^ (byte)((ulong)uVar19 >> 0x18);
          pbVar4[4] = auVar18[4] ^ (byte)((ulong)uVar19 >> 0x20);
          pbVar4[5] = auVar18[5] ^ (byte)((ulong)uVar19 >> 0x28);
          pbVar4[6] = auVar18[6] ^ (byte)((ulong)uVar19 >> 0x30);
          pbVar4[7] = auVar18[7] ^ (byte)((ulong)uVar19 >> 0x38);
          pbVar4 = pbVar4 + 0x20;
        } while (uVar11 != 0);
        if (uVar13 == uVar8) {
          return;
        }
        if ((uVar13 & 0x18) == 0) {
          pbVar7 = pbVar7 + -uVar8;
          pbVar4 = pbVar14 + uVar8;
          pbVar5 = pbVar6 + uVar8;
          goto LAB_00adcb9c;
        }
      }
      uVar11 = uVar13 & 0xfffffffffffffff8;
      pbVar12 = pbVar7 + -uVar8;
      pbVar5 = pbVar6 + uVar11;
      pbVar4 = pbVar14 + uVar11;
      pbVar7 = pbVar7 + -uVar11;
      lVar9 = uVar8 - uVar11;
      pbVar14 = pbVar14 + uVar8;
      pbVar6 = pbVar6 + uVar8;
      do {
        pbVar12 = pbVar12 + -8;
        lVar9 = lVar9 + 8;
        uVar17 = *(undefined8 *)pbVar14;
        uVar15 = NEON_rev64(*(undefined8 *)pbVar12,1);
        *(ulong *)pbVar6 =
             CONCAT17((byte)((ulong)uVar15 >> 0x38) ^ (byte)((ulong)uVar17 >> 0x38),
                      CONCAT16((byte)((ulong)uVar15 >> 0x30) ^ (byte)((ulong)uVar17 >> 0x30),
                               CONCAT15((byte)((ulong)uVar15 >> 0x28) ^
                                        (byte)((ulong)uVar17 >> 0x28),
                                        CONCAT14((byte)((ulong)uVar15 >> 0x20) ^
                                                 (byte)((ulong)uVar17 >> 0x20),
                                                 CONCAT13((byte)((ulong)uVar15 >> 0x18) ^
                                                          (byte)((ulong)uVar17 >> 0x18),
                                                          CONCAT12((byte)((ulong)uVar15 >> 0x10) ^
                                                                   (byte)((ulong)uVar17 >> 0x10),
                                                                   CONCAT11((byte)((ulong)uVar15 >>
                                                                                  8) ^
                                                                            (byte)((ulong)uVar17 >>
                                                                                  8),(byte)uVar15 ^
                                                                                     (byte)uVar17)))
                                                ))));
        pbVar14 = pbVar14 + 8;
        pbVar6 = pbVar6 + 8;
      } while (lVar9 != 0);
      if (uVar13 == uVar11) {
        return;
      }
    }
  }
LAB_00adcb9c:
  do {
    pbVar7 = pbVar7 + -1;
    pbVar14 = pbVar4 + 1;
    *pbVar5 = *pbVar7 ^ *pbVar4;
    pbVar4 = pbVar14;
    pbVar5 = pbVar5 + 1;
  } while (pbVar14 != pbVar3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adcadc"></a> `00adcadc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00adcae0"></a> `00adcae0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adcae4"></a> `00adcae4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcae8"></a> `00adcae8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adcaec"></a> `00adcaec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adcaf0"></a> `00adcaf0` | `0a 24 40 a9` | ldp x10,x9,[x0] | `FALL_THROUGH`
<a id="insn-00adcaf4"></a> `00adcaf4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00adcaf8"></a> `00adcaf8` | `35 01 0a cb` | sub x21,x9,x10 | `FALL_THROUGH`
<a id="insn-00adcafc"></a> `00adcafc` | `bf 22 00 b1` | cmn x21,#0x8 | `FALL_THROUGH`
<a id="insn-00adcb00"></a> `00adcb00` | `e2 0d 00 54` | b.cs 0x00adccbc | `CONDITIONAL_JUMP`
<a id="insn-00adcb04"></a> `00adcb04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adcb08"></a> `00adcb08` | `bf 5e 00 f1` | cmp x21,#0x17 | `FALL_THROUGH`
<a id="insn-00adcb0c"></a> `00adcb0c` | `e2 00 00 54` | b.cs 0x00adcb28 | `CONDITIONAL_JUMP`
<a id="insn-00adcb10"></a> `00adcb10` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00adcb14"></a> `00adcb14` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00adcb18"></a> `00adcb18` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00adcb1c"></a> `00adcb1c` | `c8 16 00 38` | strb w8,[x22], #0x1 | `FALL_THROUGH`
<a id="insn-00adcb20"></a> `00adcb20` | `c1 01 00 54` | b.ne 0x00adcb58 | `CONDITIONAL_JUMP`
<a id="insn-00adcb24"></a> `00adcb24` | `11 00 00 14` | b 0x00adcb68 | `UNCONDITIONAL_JUMP`
<a id="insn-00adcb28"></a> `00adcb28` | `a8 f2 7d 92` | and x8,x21,#-0x8 | `FALL_THROUGH`
<a id="insn-00adcb2c"></a> `00adcb2c` | `a9 0a 40 b2` | orr x9,x21,#0x7 | `FALL_THROUGH`
<a id="insn-00adcb30"></a> `00adcb30` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00adcb34"></a> `00adcb34` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-00adcb38"></a> `00adcb38` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00adcb3c"></a> `00adcb3c` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adcb40"></a> `00adcb40` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00adcb44"></a> `00adcb44` | `3f f9 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00adcb48"></a> `00adcb48` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00adcb4c"></a> `00adcb4c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00adcb50"></a> `00adcb50` | `95 82 00 a9` | stp x21,x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00adcb54"></a> `00adcb54` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00adcb58"></a> `00adcb58` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00adcb5c"></a> `00adcb5c` | `01 0b 80 52` | mov w1,#0x58 | `FALL_THROUGH`
<a id="insn-00adcb60"></a> `00adcb60` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00adcb64"></a> `00adcb64` | `b7 f9 03 94` | bl 0x00bdb240 | `UNCONDITIONAL_CALL`
<a id="insn-00adcb68"></a> `00adcb68` | `df 6a 35 38` | strb wzr,[x22, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00adcb6c"></a> `00adcb6c` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00adcb70"></a> `00adcb70` | `2d 01 08 eb` | subs x13,x9,x8 | `FALL_THROUGH`
<a id="insn-00adcb74"></a> `00adcb74` | `00 02 00 54` | b.eq 0x00adcbb4 | `CONDITIONAL_JUMP`
<a id="insn-00adcb78"></a> `00adcb78` | `8a 02 40 39` | ldrb w10,[x20] | `FALL_THROUGH`
<a id="insn-00adcb7c"></a> `00adcb7c` | `8c 0a 40 f9` | ldr x12,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00adcb80"></a> `00adcb80` | `0b 01 09 cb` | sub x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00adcb84"></a> `00adcb84` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00adcb88"></a> `00adcb88` | `8a 15 94 9a` | csinc x10,x12,x20,ne | `FALL_THROUGH`
<a id="insn-00adcb8c"></a> `00adcb8c` | `6c 12 40 f9` | ldr x12,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adcb90"></a> `00adcb90` | `7f 21 00 f1` | cmp x11,#0x8 | `FALL_THROUGH`
<a id="insn-00adcb94"></a> `00adcb94` | `a2 01 00 54` | b.cs 0x00adcbc8 | `CONDITIONAL_JUMP`
<a id="insn-00adcb98"></a> `00adcb98` | `8b 05 00 d1` | sub x11,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00adcb9c"></a> `00adcb9c` | `2c 15 40 38` | ldrb w12,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00adcba0"></a> `00adcba0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00adcba4"></a> `00adcba4` | `6d f5 5f 38` | ldrb w13,[x11], #-0x1 | `FALL_THROUGH`
<a id="insn-00adcba8"></a> `00adcba8` | `ac 01 0c 4a` | eor w12,w13,w12 | `FALL_THROUGH`
<a id="insn-00adcbac"></a> `00adcbac` | `4c 15 00 38` | strb w12,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00adcbb0"></a> `00adcbb0` | `61 ff ff 54` | b.ne 0x00adcb9c | `CONDITIONAL_JUMP`
<a id="insn-00adcbb4"></a> `00adcbb4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adcbb8"></a> `00adcbb8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adcbbc"></a> `00adcbbc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcbc0"></a> `00adcbc0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00adcbc4"></a> `00adcbc4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adcbc8"></a> `00adcbc8` | `4e 01 0b 8b` | add x14,x10,x11 | `FALL_THROUGH`
<a id="insn-00adcbcc"></a> `00adcbcc` | `8d 01 0d 8b` | add x13,x12,x13 | `FALL_THROUGH`
<a id="insn-00adcbd0"></a> `00adcbd0` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00adcbd4"></a> `00adcbd4` | `a2 31 4e fa` | ccmp x13,x14,#0x2,cc | `FALL_THROUGH`
<a id="insn-00adcbd8"></a> `00adcbd8` | `ed 27 9f 1a` | cset w13,cc | `FALL_THROUGH`
<a id="insn-00adcbdc"></a> `00adcbdc` | `3f 01 0e eb` | cmp x9,x14 | `FALL_THROUGH`
<a id="insn-00adcbe0"></a> `00adcbe0` | `42 31 48 fa` | ccmp x10,x8,#0x2,cc | `FALL_THROUGH`
<a id="insn-00adcbe4"></a> `00adcbe4` | `a3 fd ff 54` | b.cc 0x00adcb98 | `CONDITIONAL_JUMP`
<a id="insn-00adcbe8"></a> `00adcbe8` | `8d fd 07 37` | tbnz w13,#0x0,0x00adcb98 | `CONDITIONAL_JUMP`
<a id="insn-00adcbec"></a> `00adcbec` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00adcbf0"></a> `00adcbf0` | `62 00 00 54` | b.cs 0x00adcbfc | `CONDITIONAL_JUMP`
<a id="insn-00adcbf4"></a> `00adcbf4` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00adcbf8"></a> `00adcbf8` | `18 00 00 14` | b 0x00adcc58 | `UNCONDITIONAL_JUMP`
<a id="insn-00adcbfc"></a> `00adcbfc` | `6d e9 7b 92` | and x13,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00adcc00"></a> `00adcc00` | `8e 41 00 d1` | sub x14,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00adcc04"></a> `00adcc04` | `2f 41 00 91` | add x15,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00adcc08"></a> `00adcc08` | `50 41 00 91` | add x16,x10,#0x10 | `FALL_THROUGH`
<a id="insn-00adcc0c"></a> `00adcc0c` | `f1 03 0d aa` | mov x17,x13 | `FALL_THROUGH`
<a id="insn-00adcc10"></a> `00adcc10` | `c1 81 7f ad` | ldp q1,q0,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00adcc14"></a> `00adcc14` | `31 82 00 f1` | subs x17,x17,#0x20 | `FALL_THROUGH`
<a id="insn-00adcc18"></a> `00adcc18` | `e2 8d 7f ad` | ldp q2,q3,[x15, #-0x10] | `FALL_THROUGH`
<a id="insn-00adcc1c"></a> `00adcc1c` | `ce 81 00 d1` | sub x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00adcc20"></a> `00adcc20` | `ef 81 00 91` | add x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00adcc24"></a> `00adcc24` | `00 08 20 4e` | rev64 v0.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00adcc28"></a> `00adcc28` | `21 08 20 4e` | rev64 v1.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00adcc2c"></a> `00adcc2c` | `00 40 00 6e` | ext v0.16B,v0.16B,v0.16B,0x8 | `FALL_THROUGH`
<a id="insn-00adcc30"></a> `00adcc30` | `21 40 01 6e` | ext v1.16B,v1.16B,v1.16B,0x8 | `FALL_THROUGH`
<a id="insn-00adcc34"></a> `00adcc34` | `00 1c 22 6e` | eor v0.16B,v0.16B,v2.16B | `FALL_THROUGH`
<a id="insn-00adcc38"></a> `00adcc38` | `21 1c 23 6e` | eor v1.16B,v1.16B,v3.16B | `FALL_THROUGH`
<a id="insn-00adcc3c"></a> `00adcc3c` | `00 86 3f ad` | stp q0,q1,[x16, #-0x10] | `FALL_THROUGH`
<a id="insn-00adcc40"></a> `00adcc40` | `10 82 00 91` | add x16,x16,#0x20 | `FALL_THROUGH`
<a id="insn-00adcc44"></a> `00adcc44` | `61 fe ff 54` | b.ne 0x00adcc10 | `CONDITIONAL_JUMP`
<a id="insn-00adcc48"></a> `00adcc48` | `7f 01 0d eb` | cmp x11,x13 | `FALL_THROUGH`
<a id="insn-00adcc4c"></a> `00adcc4c` | `40 fb ff 54` | b.eq 0x00adcbb4 | `CONDITIONAL_JUMP`
<a id="insn-00adcc50"></a> `00adcc50` | `7f 05 7d f2` | tst x11,#0x18 | `FALL_THROUGH`
<a id="insn-00adcc54"></a> `00adcc54` | `c0 02 00 54` | b.eq 0x00adccac | `CONDITIONAL_JUMP`
<a id="insn-00adcc58"></a> `00adcc58` | `6e f1 7d 92` | and x14,x11,#-0x8 | `FALL_THROUGH`
<a id="insn-00adcc5c"></a> `00adcc5c` | `91 01 0d cb` | sub x17,x12,x13 | `FALL_THROUGH`
<a id="insn-00adcc60"></a> `00adcc60` | `4f 01 0e 8b` | add x15,x10,x14 | `FALL_THROUGH`
<a id="insn-00adcc64"></a> `00adcc64` | `30 01 0e 8b` | add x16,x9,x14 | `FALL_THROUGH`
<a id="insn-00adcc68"></a> `00adcc68` | `8c 01 0e cb` | sub x12,x12,x14 | `FALL_THROUGH`
<a id="insn-00adcc6c"></a> `00adcc6c` | `31 22 00 d1` | sub x17,x17,#0x8 | `FALL_THROUGH`
<a id="insn-00adcc70"></a> `00adcc70` | `29 01 0d 8b` | add x9,x9,x13 | `FALL_THROUGH`
<a id="insn-00adcc74"></a> `00adcc74` | `4a 01 0d 8b` | add x10,x10,x13 | `FALL_THROUGH`
<a id="insn-00adcc78"></a> `00adcc78` | `ad 01 0e cb` | sub x13,x13,x14 | `FALL_THROUGH`
<a id="insn-00adcc7c"></a> `00adcc7c` | `20 86 5f fc` | ldr d0,[x17], #-0x8 | `FALL_THROUGH`
<a id="insn-00adcc80"></a> `00adcc80` | `ad 21 00 b1` | adds x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00adcc84"></a> `00adcc84` | `21 85 40 fc` | ldr d1,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-00adcc88"></a> `00adcc88` | `00 08 20 0e` | rev64 v0.8B,v0.8B | `FALL_THROUGH`
<a id="insn-00adcc8c"></a> `00adcc8c` | `00 1c 21 2e` | eor v0.8B,v0.8B,v1.8B | `FALL_THROUGH`
<a id="insn-00adcc90"></a> `00adcc90` | `40 85 00 fc` | str d0,[x10], #0x8 | `FALL_THROUGH`
<a id="insn-00adcc94"></a> `00adcc94` | `41 ff ff 54` | b.ne 0x00adcc7c | `CONDITIONAL_JUMP`
<a id="insn-00adcc98"></a> `00adcc98` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00adcc9c"></a> `00adcc9c` | `ea 03 0f aa` | mov x10,x15 | `FALL_THROUGH`
<a id="insn-00adcca0"></a> `00adcca0` | `e9 03 10 aa` | mov x9,x16 | `FALL_THROUGH`
<a id="insn-00adcca4"></a> `00adcca4` | `a1 f7 ff 54` | b.ne 0x00adcb98 | `CONDITIONAL_JUMP`
<a id="insn-00adcca8"></a> `00adcca8` | `c3 ff ff 17` | b 0x00adcbb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00adccac"></a> `00adccac` | `8c 01 0d cb` | sub x12,x12,x13 | `FALL_THROUGH`
<a id="insn-00adccb0"></a> `00adccb0` | `29 01 0d 8b` | add x9,x9,x13 | `FALL_THROUGH`
<a id="insn-00adccb4"></a> `00adccb4` | `4a 01 0d 8b` | add x10,x10,x13 | `FALL_THROUGH`
<a id="insn-00adccb8"></a> `00adccb8` | `b8 ff ff 17` | b 0x00adcb98 | `UNCONDITIONAL_JUMP`
<a id="insn-00adccbc"></a> `00adccbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adccc0"></a> `00adccc0` | `d9 ef e4 97` | bl 0x00418c24 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adcadc`](#insn-00adcadc) 範囲 `[['00adcadc', '00adcb03']]`
  - `CONDITIONAL_JUMP` [`00adcb00`](#insn-00adcb00) → [`00adccbc`](#insn-00adccbc)
  - `FALL_THROUGH` [`00adcb00`](#insn-00adcb00) → [`00adcb04`](#insn-00adcb04)
- ブロック [`00adcb04`](#insn-00adcb04) 範囲 `[['00adcb04', '00adcb0f']]`
  - `CONDITIONAL_JUMP` [`00adcb0c`](#insn-00adcb0c) → [`00adcb28`](#insn-00adcb28)
  - `FALL_THROUGH` [`00adcb0c`](#insn-00adcb0c) → [`00adcb10`](#insn-00adcb10)
- ブロック [`00adcb10`](#insn-00adcb10) 範囲 `[['00adcb10', '00adcb23']]`
  - `CONDITIONAL_JUMP` [`00adcb20`](#insn-00adcb20) → [`00adcb58`](#insn-00adcb58)
  - `FALL_THROUGH` [`00adcb20`](#insn-00adcb20) → [`00adcb24`](#insn-00adcb24)
- ブロック [`00adcb24`](#insn-00adcb24) 範囲 `[['00adcb24', '00adcb27']]`
  - `UNCONDITIONAL_JUMP` [`00adcb24`](#insn-00adcb24) → [`00adcb68`](#insn-00adcb68)
- ブロック [`00adcb28`](#insn-00adcb28) 範囲 `[['00adcb28', '00adcb57']]`
  - `FALL_THROUGH` [`00adcb54`](#insn-00adcb54) → [`00adcb58`](#insn-00adcb58)
- ブロック [`00adcb58`](#insn-00adcb58) 範囲 `[['00adcb58', '00adcb67']]`
  - `FALL_THROUGH` [`00adcb64`](#insn-00adcb64) → [`00adcb68`](#insn-00adcb68)
- ブロック [`00adcb68`](#insn-00adcb68) 範囲 `[['00adcb68', '00adcb77']]`
  - `CONDITIONAL_JUMP` [`00adcb74`](#insn-00adcb74) → [`00adcbb4`](#insn-00adcbb4)
  - `FALL_THROUGH` [`00adcb74`](#insn-00adcb74) → [`00adcb78`](#insn-00adcb78)
- ブロック [`00adcb78`](#insn-00adcb78) 範囲 `[['00adcb78', '00adcb7b']]`
  - `FALL_THROUGH` [`00adcb78`](#insn-00adcb78) → [`00adcb7c`](#insn-00adcb7c)
- ブロック [`00adcb7c`](#insn-00adcb7c) 範囲 `[['00adcb7c', '00adcb97']]`
  - `CONDITIONAL_JUMP` [`00adcb94`](#insn-00adcb94) → [`00adcbc8`](#insn-00adcbc8)
  - `FALL_THROUGH` [`00adcb94`](#insn-00adcb94) → [`00adcb98`](#insn-00adcb98)
- ブロック [`00adcb98`](#insn-00adcb98) 範囲 `[['00adcb98', '00adcb9b']]`
  - `FALL_THROUGH` [`00adcb98`](#insn-00adcb98) → [`00adcb9c`](#insn-00adcb9c)
- ブロック [`00adcb9c`](#insn-00adcb9c) 範囲 `[['00adcb9c', '00adcbb3']]`
  - `CONDITIONAL_JUMP` [`00adcbb0`](#insn-00adcbb0) → [`00adcb9c`](#insn-00adcb9c)
  - `FALL_THROUGH` [`00adcbb0`](#insn-00adcbb0) → [`00adcbb4`](#insn-00adcbb4)
- ブロック [`00adcbb4`](#insn-00adcbb4) 範囲 `[['00adcbb4', '00adcbc7']]`
- ブロック [`00adcbc8`](#insn-00adcbc8) 範囲 `[['00adcbc8', '00adcbe7']]`
  - `CONDITIONAL_JUMP` [`00adcbe4`](#insn-00adcbe4) → [`00adcb98`](#insn-00adcb98)
  - `FALL_THROUGH` [`00adcbe4`](#insn-00adcbe4) → [`00adcbe8`](#insn-00adcbe8)
- ブロック [`00adcbe8`](#insn-00adcbe8) 範囲 `[['00adcbe8', '00adcbeb']]`
  - `CONDITIONAL_JUMP` [`00adcbe8`](#insn-00adcbe8) → [`00adcb98`](#insn-00adcb98)
  - `FALL_THROUGH` [`00adcbe8`](#insn-00adcbe8) → [`00adcbec`](#insn-00adcbec)
- ブロック [`00adcbec`](#insn-00adcbec) 範囲 `[['00adcbec', '00adcbf3']]`
  - `CONDITIONAL_JUMP` [`00adcbf0`](#insn-00adcbf0) → [`00adcbfc`](#insn-00adcbfc)
  - `FALL_THROUGH` [`00adcbf0`](#insn-00adcbf0) → [`00adcbf4`](#insn-00adcbf4)
- ブロック [`00adcbf4`](#insn-00adcbf4) 範囲 `[['00adcbf4', '00adcbfb']]`
  - `UNCONDITIONAL_JUMP` [`00adcbf8`](#insn-00adcbf8) → [`00adcc58`](#insn-00adcc58)
- ブロック [`00adcbfc`](#insn-00adcbfc) 範囲 `[['00adcbfc', '00adcc0f']]`
  - `FALL_THROUGH` [`00adcc0c`](#insn-00adcc0c) → [`00adcc10`](#insn-00adcc10)
- ブロック [`00adcc10`](#insn-00adcc10) 範囲 `[['00adcc10', '00adcc47']]`
  - `CONDITIONAL_JUMP` [`00adcc44`](#insn-00adcc44) → [`00adcc10`](#insn-00adcc10)
  - `FALL_THROUGH` [`00adcc44`](#insn-00adcc44) → [`00adcc48`](#insn-00adcc48)
- ブロック [`00adcc48`](#insn-00adcc48) 範囲 `[['00adcc48', '00adcc4f']]`
  - `CONDITIONAL_JUMP` [`00adcc4c`](#insn-00adcc4c) → [`00adcbb4`](#insn-00adcbb4)
  - `FALL_THROUGH` [`00adcc4c`](#insn-00adcc4c) → [`00adcc50`](#insn-00adcc50)
- ブロック [`00adcc50`](#insn-00adcc50) 範囲 `[['00adcc50', '00adcc57']]`
  - `CONDITIONAL_JUMP` [`00adcc54`](#insn-00adcc54) → [`00adccac`](#insn-00adccac)
  - `FALL_THROUGH` [`00adcc54`](#insn-00adcc54) → [`00adcc58`](#insn-00adcc58)
- ブロック [`00adcc58`](#insn-00adcc58) 範囲 `[['00adcc58', '00adcc7b']]`
  - `FALL_THROUGH` [`00adcc78`](#insn-00adcc78) → [`00adcc7c`](#insn-00adcc7c)
- ブロック [`00adcc7c`](#insn-00adcc7c) 範囲 `[['00adcc7c', '00adcc97']]`
  - `CONDITIONAL_JUMP` [`00adcc94`](#insn-00adcc94) → [`00adcc7c`](#insn-00adcc7c)
  - `FALL_THROUGH` [`00adcc94`](#insn-00adcc94) → [`00adcc98`](#insn-00adcc98)
- ブロック [`00adcc98`](#insn-00adcc98) 範囲 `[['00adcc98', '00adcca7']]`
  - `CONDITIONAL_JUMP` [`00adcca4`](#insn-00adcca4) → [`00adcb98`](#insn-00adcb98)
  - `FALL_THROUGH` [`00adcca4`](#insn-00adcca4) → [`00adcca8`](#insn-00adcca8)
- ブロック [`00adcca8`](#insn-00adcca8) 範囲 `[['00adcca8', '00adccab']]`
  - `UNCONDITIONAL_JUMP` [`00adcca8`](#insn-00adcca8) → [`00adcbb4`](#insn-00adcbb4)
- ブロック [`00adccac`](#insn-00adccac) 範囲 `[['00adccac', '00adccbb']]`
  - `UNCONDITIONAL_JUMP` [`00adccb8`](#insn-00adccb8) → [`00adcb98`](#insn-00adcb98)
- ブロック [`00adccbc`](#insn-00adccbc) 範囲 `[['00adccbc', '00adccc3']]`

## 命令位置別の参照

- [`00adcadc`](#insn-00adcadc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcae0`](#insn-00adcae0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcae4`](#insn-00adcae4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcae8`](#insn-00adcae8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcb00`](#insn-00adcb00) → [`00adccbc`](#insn-00adccbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcb0c`](#insn-00adcb0c) → [`00adcb28`](#insn-00adcb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcb20`](#insn-00adcb20) → [`00adcb58`](#insn-00adcb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcb24`](#insn-00adcb24) → [`00adcb68`](#insn-00adcb68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcb44`](#insn-00adcb44) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00adcb64`](#insn-00adcb64) → [`00bdb240`](../00bdb/00bdb240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb240` · 推定シンボル `None` · 推定型 `None`
- [`00adcb74`](#insn-00adcb74) → [`00adcbb4`](#insn-00adcbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcb94`](#insn-00adcb94) → [`00adcbc8`](#insn-00adcbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbb0`](#insn-00adcbb0) → [`00adcb9c`](#insn-00adcb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbb4`](#insn-00adcbb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbb8`](#insn-00adcbb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbbc`](#insn-00adcbbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbc0`](#insn-00adcbc0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbe4`](#insn-00adcbe4) → [`00adcb98`](#insn-00adcb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbe8`](#insn-00adcbe8) → [`00adcb98`](#insn-00adcb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbf0`](#insn-00adcbf0) → [`00adcbfc`](#insn-00adcbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbf8`](#insn-00adcbf8) → [`00adcc58`](#insn-00adcc58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc44`](#insn-00adcc44) → [`00adcc10`](#insn-00adcc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc4c`](#insn-00adcc4c) → [`00adcbb4`](#insn-00adcbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc54`](#insn-00adcc54) → [`00adccac`](#insn-00adccac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc94`](#insn-00adcc94) → [`00adcc7c`](#insn-00adcc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcca4`](#insn-00adcca4) → [`00adcb98`](#insn-00adcb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcca8`](#insn-00adcca8) → [`00adcbb4`](#insn-00adcbb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccb8`](#insn-00adccb8) → [`00adcb98`](#insn-00adcb98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccc0`](#insn-00adccc0) → [`00418c24`](../00418/00418c24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c24` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adcadc`](#insn-00adcadc)

~~~json
{
  "source": "00adcadc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcae0`](#insn-00adcae0)

~~~json
{
  "source": "00adcae0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcae4`](#insn-00adcae4)

~~~json
{
  "source": "00adcae4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcae8`](#insn-00adcae8)

~~~json
{
  "source": "00adcae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcb00`](#insn-00adcb00)

~~~json
{
  "source": "00adcb00",
  "target": "00adccbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcb0c`](#insn-00adcb0c)

~~~json
{
  "source": "00adcb0c",
  "target": "00adcb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcb20`](#insn-00adcb20)

~~~json
{
  "source": "00adcb20",
  "target": "00adcb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcb24`](#insn-00adcb24)

~~~json
{
  "source": "00adcb24",
  "target": "00adcb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcb44`](#insn-00adcb44)

~~~json
{
  "source": "00adcb44",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcb64`](#insn-00adcb64)

~~~json
{
  "source": "00adcb64",
  "target": "00bdb240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcb74`](#insn-00adcb74)

~~~json
{
  "source": "00adcb74",
  "target": "00adcbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcb94`](#insn-00adcb94)

~~~json
{
  "source": "00adcb94",
  "target": "00adcbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbb0`](#insn-00adcbb0)

~~~json
{
  "source": "00adcbb0",
  "target": "00adcb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbb4`](#insn-00adcbb4)

~~~json
{
  "source": "00adcbb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbb8`](#insn-00adcbb8)

~~~json
{
  "source": "00adcbb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbbc`](#insn-00adcbbc)

~~~json
{
  "source": "00adcbbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbc0`](#insn-00adcbc0)

~~~json
{
  "source": "00adcbc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbe4`](#insn-00adcbe4)

~~~json
{
  "source": "00adcbe4",
  "target": "00adcb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbe8`](#insn-00adcbe8)

~~~json
{
  "source": "00adcbe8",
  "target": "00adcb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbf0`](#insn-00adcbf0)

~~~json
{
  "source": "00adcbf0",
  "target": "00adcbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbf8`](#insn-00adcbf8)

~~~json
{
  "source": "00adcbf8",
  "target": "00adcc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc44`](#insn-00adcc44)

~~~json
{
  "source": "00adcc44",
  "target": "00adcc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc4c`](#insn-00adcc4c)

~~~json
{
  "source": "00adcc4c",
  "target": "00adcbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc54`](#insn-00adcc54)

~~~json
{
  "source": "00adcc54",
  "target": "00adccac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc94`](#insn-00adcc94)

~~~json
{
  "source": "00adcc94",
  "target": "00adcc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcca4`](#insn-00adcca4)

~~~json
{
  "source": "00adcca4",
  "target": "00adcb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcca8`](#insn-00adcca8)

~~~json
{
  "source": "00adcca8",
  "target": "00adcbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccb8`](#insn-00adccb8)

~~~json
{
  "source": "00adccb8",
  "target": "00adcb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccc0`](#insn-00adccc0)

~~~json
{
  "source": "00adccc0",
  "target": "00418c24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
