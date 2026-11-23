# 00afced4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afce0c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afce0c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-2592ffbc7dc471e9e17e020d90b15684)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afcf18`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcf18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-e0953b11da6b3117f946f93a44a00c82)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afced4",
  "name": "_ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2f4fac85ef9e39a3868625f68d002a13d13fdd1d7f10b55db8260c3e0ec16cb",
  "source_text_sha256": "d2f4fac85ef9e39a3868625f68d002a13d13fdd1d7f10b55db8260c3e0ec16cb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afced4",
        "00afd0c3"
      ]
    ],
    "bytes_sha256": "81032f137501c64fc52416167a767e402304f93d9748a85c26322ae1766b2307",
    "instruction_count": 124,
    "instruction_bytes": 496,
    "body_bytes": 496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdece0](../00bde/00bdece0.md)

## 呼び出し先

- [00bdb0e0](../00bdb/00bdb0e0.md)
- [00bded00](../00bde/00bded00.md)
- [00bded20](../00bde/00bded20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4246 bytes

~~~c

void _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (byte *param_1,byte *param_2)

{
  byte *pbVar1;
  ulong uVar2;
  byte bVar3;
  byte *pbVar4;
  bool bVar5;
  long lVar6;
  byte *pbVar7;
  ulong uVar8;
  byte *pbVar9;
  byte *pbVar10;
  bool bVar11;
  
  param_1[0] = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[6] = 0;
  param_1[7] = 0;
  param_1[8] = 0;
  param_1[9] = 0;
  param_1[10] = 0;
  param_1[0xb] = 0;
  param_1[0xc] = 0;
  param_1[0xd] = 0;
  param_1[0xe] = 0;
  param_1[0xf] = 0;
  param_1[0x10] = 0;
  param_1[0x11] = 0;
  param_1[0x12] = 0;
  param_1[0x13] = 0;
  param_1[0x14] = 0;
  param_1[0x15] = 0;
  param_1[0x16] = 0;
  param_1[0x17] = 0;
  bVar3 = *param_2;
  uVar8 = *(ulong *)(param_2 + 8);
  pbVar9 = *(byte **)(param_2 + 0x10);
  bVar5 = (bVar3 & 1) == 0;
  pbVar10 = pbVar9;
  uVar2 = uVar8;
  if (bVar5) {
    pbVar10 = param_2 + 1;
    uVar2 = (ulong)(bVar3 >> 1);
  }
  if (uVar2 != 0) {
                    /* try { // try from 00afcf28 to 00bfcf2f has its CatchHandler @ 00aff3a8 */
    pbVar1 = param_2 + 1;
    bVar11 = true;
    do {
      uVar2 = (ulong)(bVar3 >> 1);
      pbVar4 = pbVar1;
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
                    /* try { // try from 00afcf80 to 00bfcf87 has its CatchHandler @ 00aff3a0 */
      pbVar9 = pbVar10;
      if ((pbVar4 + uVar2 != pbVar10) &&
         (lVar6 = __strchr_chk(&DAT_002958ca,*pbVar10,2), lVar6 != 0)) {
        do {
          pbVar9 = pbVar4 + uVar2;
          if (pbVar4 + (uVar2 - 1) == pbVar10) break;
                    /* try { // try from 00afcfb0 to 00bfcfc7 has its CatchHandler @ 00aff39c */
          pbVar9 = pbVar10 + 1;
          lVar6 = __strchr_chk(&DAT_002958ca,pbVar10[1],2);
                    /* try { // try from 00afcfc8 to 00bfcff7 has its CatchHandler @ 00af560c */
          pbVar10 = pbVar9;
        } while (lVar6 != 0);
      }
      uVar8 = (ulong)(*param_2 >> 1);
      pbVar4 = pbVar1;
      if ((*param_2 & 1) != 0) {
        uVar8 = *(ulong *)(param_2 + 8);
        pbVar4 = *(byte **)(param_2 + 0x10);
      }
      pbVar10 = pbVar9;
                    /* try { // try from 00afcff8 to 00bfd00f has its CatchHandler @ 00aff38c */
      if ((pbVar4 + uVar8 != pbVar9) && (lVar6 = __strchr_chk(&DAT_002958ca,*pbVar9,2), lVar6 == 0))
      {
                    /* try { // try from 00afd010 to 00bfd03f has its CatchHandler @ 00af560c */
        pbVar7 = pbVar9;
        do {
          pbVar10 = pbVar4 + uVar8;
          if (pbVar4 + (uVar8 - 1) == pbVar7) break;
          pbVar10 = pbVar7 + 1;
          pbVar7 = pbVar7 + 1;
          lVar6 = __strchr_chk(&DAT_002958ca,*pbVar10,2);
          pbVar10 = pbVar7;
        } while (lVar6 == 0);
        if (pbVar10 != pbVar9) {
          if (!bVar11) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                      (param_1,&DAT_002958ca,1);
          }
          uVar8 = (ulong)(*param_1 >> 1);
          pbVar4 = param_1 + 1;
                    /* try { // try from 00afd070 to 00bfd087 has its CatchHandler @ 00aff384 */
          if ((*param_1 & 1) != 0) {
            uVar8 = *(ulong *)(param_1 + 8);
            pbVar4 = *(byte **)(param_1 + 0x10);
          }
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__libcpp_string_gets_noexcept_iteratorISC_EE5valueENS7_IPcEEE4typeESA_SC_SC_
                    (param_1,pbVar4 + uVar8,pbVar9,pbVar10);
          bVar11 = false;
        }
      }
      bVar3 = *param_2;
      uVar8 = *(ulong *)(param_2 + 8);
      pbVar9 = *(byte **)(param_2 + 0x10);
      bVar5 = (bVar3 & 1) == 0;
      uVar2 = (ulong)(bVar3 >> 1);
      pbVar4 = pbVar1;
                    /* try { // try from 00afcf58 to 00bfcf6f has its CatchHandler @ 00aff3a4 */
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
    } while (pbVar4 + uVar2 != pbVar10);
  }
                    /* try { // try from 00afd0c0 to 00bfd0d7 has its CatchHandler @ 00aff380 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afced4"></a> `00afced4` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afced8"></a> `00afced8` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcedc"></a> `00afcedc` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcee0"></a> `00afcee0` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afcee4"></a> `00afcee4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afcee8"></a> `00afcee8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afceec"></a> `00afceec` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afcef0"></a> `00afcef0` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00afcef4"></a> `00afcef4` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00afcef8"></a> `00afcef8` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afcefc"></a> `00afcefc` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00afcf00"></a> `00afcf00` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00afcf04"></a> `00afcf04` | `09 a8 40 a9` | ldp x9,x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afcf08"></a> `00afcf08` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf0c"></a> `00afcf0c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf10"></a> `00afcf10` | `eb 17 9f 1a` | cset w11,eq | `FALL_THROUGH`
<a id="insn-00afcf14"></a> `00afcf14` | `8c 01 89 9a` | csel x12,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00afcf18"></a> `00afcf18` | `57 15 80 9a` | csinc x23,x10,x0,ne | `FALL_THROUGH`
<a id="insn-00afcf1c"></a> `00afcf1c` | `4c 0c 00 b4` | cbz x12,0x00afd0a4 | `CONDITIONAL_JUMP`
<a id="insn-00afcf20"></a> `00afcf20` | `d5 bc ff b0` | adrp x21,0x295000 | `FALL_THROUGH`
<a id="insn-00afcf24"></a> `00afcf24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afcf28"></a> `00afcf28` | `18 04 00 91` | add x24,x0,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf2c"></a> `00afcf2c` | `8c 06 00 91` | add x12,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf30"></a> `00afcf30` | `3a 00 80 52` | mov w26,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf34"></a> `00afcf34` | `b5 2a 23 91` | add x21,x21,#0x8ca | `FALL_THROUGH`
<a id="insn-00afcf38"></a> `00afcf38` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00afcf3c"></a> `00afcf3c` | `ec 07 00 f9` | str x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afcf40"></a> `00afcf40` | `0c 00 00 14` | b 0x00afcf70 | `UNCONDITIONAL_JUMP`
<a id="insn-00afcf44"></a> `00afcf44` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00afcf48"></a> `00afcf48` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00afcf4c"></a> `00afcf4c` | `69 aa 40 a9` | ldp x9,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afcf50"></a> `00afcf50` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf54"></a> `00afcf54` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf58"></a> `00afcf58` | `0d 03 8a 9a` | csel x13,x24,x10,eq | `FALL_THROUGH`
<a id="insn-00afcf5c"></a> `00afcf5c` | `8c 01 89 9a` | csel x12,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00afcf60"></a> `00afcf60` | `ac 01 0c 8b` | add x12,x13,x12 | `FALL_THROUGH`
<a id="insn-00afcf64"></a> `00afcf64` | `eb 17 9f 1a` | cset w11,eq | `FALL_THROUGH`
<a id="insn-00afcf68"></a> `00afcf68` | `9f 01 17 eb` | cmp x12,x23 | `FALL_THROUGH`
<a id="insn-00afcf6c"></a> `00afcf6c` | `c0 09 00 54` | b.eq 0x00afd0a4 | `CONDITIONAL_JUMP`
<a id="insn-00afcf70"></a> `00afcf70` | `08 1d 01 53` | ubfx w8,w8,#0x1,#0x7 | `FALL_THROUGH`
<a id="insn-00afcf74"></a> `00afcf74` | `7f 01 00 72` | tst w11,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf78"></a> `00afcf78` | `1c 13 8a 9a` | csel x28,x24,x10,ne | `FALL_THROUGH`
<a id="insn-00afcf7c"></a> `00afcf7c` | `19 11 89 9a` | csel x25,x8,x9,ne | `FALL_THROUGH`
<a id="insn-00afcf80"></a> `00afcf80` | `9b 03 19 8b` | add x27,x28,x25 | `FALL_THROUGH`
<a id="insn-00afcf84"></a> `00afcf84` | `7f 03 17 eb` | cmp x27,x23 | `FALL_THROUGH`
<a id="insn-00afcf88"></a> `00afcf88` | `60 02 00 54` | b.eq 0x00afcfd4 | `CONDITIONAL_JUMP`
<a id="insn-00afcf8c"></a> `00afcf8c` | `e1 02 40 39` | ldrb w1,[x23] | `FALL_THROUGH`
<a id="insn-00afcf90"></a> `00afcf90` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afcf94"></a> `00afcf94` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afcf98"></a> `00afcf98` | `62 87 03 94` | bl 0x00bded20 | `UNCONDITIONAL_CALL`
<a id="insn-00afcf9c"></a> `00afcf9c` | `c0 01 00 b4` | cbz x0,0x00afcfd4 | `CONDITIONAL_JUMP`
<a id="insn-00afcfa0"></a> `00afcfa0` | `88 03 19 8b` | add x8,x28,x25 | `FALL_THROUGH`
<a id="insn-00afcfa4"></a> `00afcfa4` | `1c 05 00 d1` | sub x28,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcfa8"></a> `00afcfa8` | `9f 03 17 eb` | cmp x28,x23 | `FALL_THROUGH`
<a id="insn-00afcfac"></a> `00afcfac` | `20 01 00 54` | b.eq 0x00afcfd0 | `CONDITIONAL_JUMP`
<a id="insn-00afcfb0"></a> `00afcfb0` | `e1 06 40 39` | ldrb w1,[x23, #0x1] | `FALL_THROUGH`
<a id="insn-00afcfb4"></a> `00afcfb4` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afcfb8"></a> `00afcfb8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afcfbc"></a> `00afcfbc` | `f6 06 00 91` | add x22,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00afcfc0"></a> `00afcfc0` | `58 87 03 94` | bl 0x00bded20 | `UNCONDITIONAL_CALL`
<a id="insn-00afcfc4"></a> `00afcfc4` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00afcfc8"></a> `00afcfc8` | `00 ff ff b5` | cbnz x0,0x00afcfa8 | `CONDITIONAL_JUMP`
<a id="insn-00afcfcc"></a> `00afcfcc` | `02 00 00 14` | b 0x00afcfd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afcfd0"></a> `00afcfd0` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00afcfd4"></a> `00afcfd4` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00afcfd8"></a> `00afcfd8` | `6a a6 40 a9` | ldp x10,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afcfdc"></a> `00afcfdc` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcfe0"></a> `00afcfe0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcfe4"></a> `00afcfe4` | `17 03 89 9a` | csel x23,x24,x9,eq | `FALL_THROUGH`
<a id="insn-00afcfe8"></a> `00afcfe8` | `79 01 8a 9a` | csel x25,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afcfec"></a> `00afcfec` | `fb 02 19 8b` | add x27,x23,x25 | `FALL_THROUGH`
<a id="insn-00afcff0"></a> `00afcff0` | `7f 03 16 eb` | cmp x27,x22 | `FALL_THROUGH`
<a id="insn-00afcff4"></a> `00afcff4` | `80 fa ff 54` | b.eq 0x00afcf44 | `CONDITIONAL_JUMP`
<a id="insn-00afcff8"></a> `00afcff8` | `c1 02 40 39` | ldrb w1,[x22] | `FALL_THROUGH`
<a id="insn-00afcffc"></a> `00afcffc` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afd000"></a> `00afd000` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afd004"></a> `00afd004` | `47 87 03 94` | bl 0x00bded20 | `UNCONDITIONAL_CALL`
<a id="insn-00afd008"></a> `00afd008` | `e0 f9 ff b5` | cbnz x0,0x00afcf44 | `CONDITIONAL_JUMP`
<a id="insn-00afd00c"></a> `00afd00c` | `e8 02 19 8b` | add x8,x23,x25 | `FALL_THROUGH`
<a id="insn-00afd010"></a> `00afd010` | `1c 05 00 d1` | sub x28,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd014"></a> `00afd014` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00afd018"></a> `00afd018` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-00afd01c"></a> `00afd01c` | `a0 03 00 54` | b.eq 0x00afd090 | `CONDITIONAL_JUMP`
<a id="insn-00afd020"></a> `00afd020` | `01 05 40 39` | ldrb w1,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00afd024"></a> `00afd024` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afd028"></a> `00afd028` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afd02c"></a> `00afd02c` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd030"></a> `00afd030` | `3c 87 03 94` | bl 0x00bded20 | `UNCONDITIONAL_CALL`
<a id="insn-00afd034"></a> `00afd034` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00afd038"></a> `00afd038` | `00 ff ff b4` | cbz x0,0x00afd018 | `CONDITIONAL_JUMP`
<a id="insn-00afd03c"></a> `00afd03c` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00afd040"></a> `00afd040` | `e0 02 00 54` | b.eq 0x00afd09c | `CONDITIONAL_JUMP`
<a id="insn-00afd044"></a> `00afd044` | `ba 00 00 37` | tbnz w26,#0x0,0x00afd058 | `CONDITIONAL_JUMP`
<a id="insn-00afd048"></a> `00afd048` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afd04c"></a> `00afd04c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afd050"></a> `00afd050` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afd054"></a> `00afd054` | `23 78 03 94` | bl 0x00bdb0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afd058"></a> `00afd058` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00afd05c"></a> `00afd05c` | `8a a6 40 a9` | ldp x10,x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00afd060"></a> `00afd060` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afd064"></a> `00afd064` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afd068"></a> `00afd068` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd06c"></a> `00afd06c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd070"></a> `00afd070` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afd074"></a> `00afd074` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00afd078"></a> `00afd078` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00afd07c"></a> `00afd07c` | `69 01 8a 9a` | csel x9,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afd080"></a> `00afd080` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00afd084"></a> `00afd084` | `1f 87 03 94` | bl 0x00bded00 | `UNCONDITIONAL_CALL`
<a id="insn-00afd088"></a> `00afd088` | `fa 03 1f 2a` | mov w26,wzr | `FALL_THROUGH`
<a id="insn-00afd08c"></a> `00afd08c` | `04 00 00 14` | b 0x00afd09c | `UNCONDITIONAL_JUMP`
<a id="insn-00afd090"></a> `00afd090` | `f7 03 1b aa` | mov x23,x27 | `FALL_THROUGH`
<a id="insn-00afd094"></a> `00afd094` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00afd098"></a> `00afd098` | `61 fd ff 54` | b.ne 0x00afd044 | `CONDITIONAL_JUMP`
<a id="insn-00afd09c"></a> `00afd09c` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00afd0a0"></a> `00afd0a0` | `aa ff ff 17` | b 0x00afcf48 | `UNCONDITIONAL_JUMP`
<a id="insn-00afd0a4"></a> `00afd0a4` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afd0a8"></a> `00afd0a8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afd0ac"></a> `00afd0ac` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afd0b0"></a> `00afd0b0` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afd0b4"></a> `00afd0b4` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afd0b8"></a> `00afd0b8` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd0bc"></a> `00afd0bc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afd0c0"></a> `00afd0c0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afced4`](#insn-00afced4) 範囲 `[['00afced4', '00afcf1f']]`
  - `CONDITIONAL_JUMP` [`00afcf1c`](#insn-00afcf1c) → [`00afd0a4`](#insn-00afd0a4)
  - `FALL_THROUGH` [`00afcf1c`](#insn-00afcf1c) → [`00afcf20`](#insn-00afcf20)
- ブロック [`00afcf20`](#insn-00afcf20) 範囲 `[['00afcf20', '00afcf27']]`
  - `FALL_THROUGH` [`00afcf24`](#insn-00afcf24) → [`00afcf28`](#insn-00afcf28)
- ブロック [`00afcf28`](#insn-00afcf28) 範囲 `[['00afcf28', '00afcf43']]`
  - `UNCONDITIONAL_JUMP` [`00afcf40`](#insn-00afcf40) → [`00afcf70`](#insn-00afcf70)
- ブロック [`00afcf44`](#insn-00afcf44) 範囲 `[['00afcf44', '00afcf47']]`
  - `FALL_THROUGH` [`00afcf44`](#insn-00afcf44) → [`00afcf48`](#insn-00afcf48)
- ブロック [`00afcf48`](#insn-00afcf48) 範囲 `[['00afcf48', '00afcf57']]`
  - `FALL_THROUGH` [`00afcf54`](#insn-00afcf54) → [`00afcf58`](#insn-00afcf58)
- ブロック [`00afcf58`](#insn-00afcf58) 範囲 `[['00afcf58', '00afcf6f']]`
  - `CONDITIONAL_JUMP` [`00afcf6c`](#insn-00afcf6c) → [`00afd0a4`](#insn-00afd0a4)
  - `FALL_THROUGH` [`00afcf6c`](#insn-00afcf6c) → [`00afcf70`](#insn-00afcf70)
- ブロック [`00afcf70`](#insn-00afcf70) 範囲 `[['00afcf70', '00afcf7f']]`
  - `FALL_THROUGH` [`00afcf7c`](#insn-00afcf7c) → [`00afcf80`](#insn-00afcf80)
- ブロック [`00afcf80`](#insn-00afcf80) 範囲 `[['00afcf80', '00afcf8b']]`
  - `CONDITIONAL_JUMP` [`00afcf88`](#insn-00afcf88) → [`00afcfd4`](#insn-00afcfd4)
  - `FALL_THROUGH` [`00afcf88`](#insn-00afcf88) → [`00afcf8c`](#insn-00afcf8c)
- ブロック [`00afcf8c`](#insn-00afcf8c) 範囲 `[['00afcf8c', '00afcf9f']]`
  - `CONDITIONAL_JUMP` [`00afcf9c`](#insn-00afcf9c) → [`00afcfd4`](#insn-00afcfd4)
  - `FALL_THROUGH` [`00afcf9c`](#insn-00afcf9c) → [`00afcfa0`](#insn-00afcfa0)
- ブロック [`00afcfa0`](#insn-00afcfa0) 範囲 `[['00afcfa0', '00afcfa7']]`
  - `FALL_THROUGH` [`00afcfa4`](#insn-00afcfa4) → [`00afcfa8`](#insn-00afcfa8)
- ブロック [`00afcfa8`](#insn-00afcfa8) 範囲 `[['00afcfa8', '00afcfaf']]`
  - `CONDITIONAL_JUMP` [`00afcfac`](#insn-00afcfac) → [`00afcfd0`](#insn-00afcfd0)
  - `FALL_THROUGH` [`00afcfac`](#insn-00afcfac) → [`00afcfb0`](#insn-00afcfb0)
- ブロック [`00afcfb0`](#insn-00afcfb0) 範囲 `[['00afcfb0', '00afcfc7']]`
  - `FALL_THROUGH` [`00afcfc4`](#insn-00afcfc4) → [`00afcfc8`](#insn-00afcfc8)
- ブロック [`00afcfc8`](#insn-00afcfc8) 範囲 `[['00afcfc8', '00afcfcb']]`
  - `CONDITIONAL_JUMP` [`00afcfc8`](#insn-00afcfc8) → [`00afcfa8`](#insn-00afcfa8)
  - `FALL_THROUGH` [`00afcfc8`](#insn-00afcfc8) → [`00afcfcc`](#insn-00afcfcc)
- ブロック [`00afcfcc`](#insn-00afcfcc) 範囲 `[['00afcfcc', '00afcfcf']]`
  - `UNCONDITIONAL_JUMP` [`00afcfcc`](#insn-00afcfcc) → [`00afcfd4`](#insn-00afcfd4)
- ブロック [`00afcfd0`](#insn-00afcfd0) 範囲 `[['00afcfd0', '00afcfd3']]`
  - `FALL_THROUGH` [`00afcfd0`](#insn-00afcfd0) → [`00afcfd4`](#insn-00afcfd4)
- ブロック [`00afcfd4`](#insn-00afcfd4) 範囲 `[['00afcfd4', '00afcff7']]`
  - `CONDITIONAL_JUMP` [`00afcff4`](#insn-00afcff4) → [`00afcf44`](#insn-00afcf44)
  - `FALL_THROUGH` [`00afcff4`](#insn-00afcff4) → [`00afcff8`](#insn-00afcff8)
- ブロック [`00afcff8`](#insn-00afcff8) 範囲 `[['00afcff8', '00afd00b']]`
  - `CONDITIONAL_JUMP` [`00afd008`](#insn-00afd008) → [`00afcf44`](#insn-00afcf44)
  - `FALL_THROUGH` [`00afd008`](#insn-00afd008) → [`00afd00c`](#insn-00afd00c)
- ブロック [`00afd00c`](#insn-00afd00c) 範囲 `[['00afd00c', '00afd00f']]`
  - `FALL_THROUGH` [`00afd00c`](#insn-00afd00c) → [`00afd010`](#insn-00afd010)
- ブロック [`00afd010`](#insn-00afd010) 範囲 `[['00afd010', '00afd017']]`
  - `FALL_THROUGH` [`00afd014`](#insn-00afd014) → [`00afd018`](#insn-00afd018)
- ブロック [`00afd018`](#insn-00afd018) 範囲 `[['00afd018', '00afd01f']]`
  - `CONDITIONAL_JUMP` [`00afd01c`](#insn-00afd01c) → [`00afd090`](#insn-00afd090)
  - `FALL_THROUGH` [`00afd01c`](#insn-00afd01c) → [`00afd020`](#insn-00afd020)
- ブロック [`00afd020`](#insn-00afd020) 範囲 `[['00afd020', '00afd03b']]`
  - `CONDITIONAL_JUMP` [`00afd038`](#insn-00afd038) → [`00afd018`](#insn-00afd018)
  - `FALL_THROUGH` [`00afd038`](#insn-00afd038) → [`00afd03c`](#insn-00afd03c)
- ブロック [`00afd03c`](#insn-00afd03c) 範囲 `[['00afd03c', '00afd03f']]`
  - `FALL_THROUGH` [`00afd03c`](#insn-00afd03c) → [`00afd040`](#insn-00afd040)
- ブロック [`00afd040`](#insn-00afd040) 範囲 `[['00afd040', '00afd043']]`
  - `CONDITIONAL_JUMP` [`00afd040`](#insn-00afd040) → [`00afd09c`](#insn-00afd09c)
  - `FALL_THROUGH` [`00afd040`](#insn-00afd040) → [`00afd044`](#insn-00afd044)
- ブロック [`00afd044`](#insn-00afd044) 範囲 `[['00afd044', '00afd047']]`
  - `CONDITIONAL_JUMP` [`00afd044`](#insn-00afd044) → [`00afd058`](#insn-00afd058)
  - `FALL_THROUGH` [`00afd044`](#insn-00afd044) → [`00afd048`](#insn-00afd048)
- ブロック [`00afd048`](#insn-00afd048) 範囲 `[['00afd048', '00afd057']]`
  - `FALL_THROUGH` [`00afd054`](#insn-00afd054) → [`00afd058`](#insn-00afd058)
- ブロック [`00afd058`](#insn-00afd058) 範囲 `[['00afd058', '00afd06f']]`
  - `FALL_THROUGH` [`00afd06c`](#insn-00afd06c) → [`00afd070`](#insn-00afd070)
- ブロック [`00afd070`](#insn-00afd070) 範囲 `[['00afd070', '00afd08f']]`
  - `UNCONDITIONAL_JUMP` [`00afd08c`](#insn-00afd08c) → [`00afd09c`](#insn-00afd09c)
- ブロック [`00afd090`](#insn-00afd090) 範囲 `[['00afd090', '00afd09b']]`
  - `CONDITIONAL_JUMP` [`00afd098`](#insn-00afd098) → [`00afd044`](#insn-00afd044)
  - `FALL_THROUGH` [`00afd098`](#insn-00afd098) → [`00afd09c`](#insn-00afd09c)
- ブロック [`00afd09c`](#insn-00afd09c) 範囲 `[['00afd09c', '00afd0a3']]`
  - `UNCONDITIONAL_JUMP` [`00afd0a0`](#insn-00afd0a0) → [`00afcf48`](#insn-00afcf48)
- ブロック [`00afd0a4`](#insn-00afd0a4) 範囲 `[['00afd0a4', '00afd0bf']]`
  - `FALL_THROUGH` [`00afd0bc`](#insn-00afd0bc) → [`00afd0c0`](#insn-00afd0c0)
- ブロック [`00afd0c0`](#insn-00afd0c0) 範囲 `[['00afd0c0', '00afd0c3']]`

## 命令位置別の参照

- [`00afced8`](#insn-00afced8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcedc`](#insn-00afcedc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcee0`](#insn-00afcee0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcee4`](#insn-00afcee4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcee8`](#insn-00afcee8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afceec`](#insn-00afceec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf1c`](#insn-00afcf1c) → [`00afd0a4`](#insn-00afd0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf3c`](#insn-00afcf3c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf40`](#insn-00afcf40) → [`00afcf70`](#insn-00afcf70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf6c`](#insn-00afcf6c) → [`00afd0a4`](#insn-00afd0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf88`](#insn-00afcf88) → [`00afcfd4`](#insn-00afcfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf94`](#insn-00afcf94) → `002958ca`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf98`](#insn-00afcf98) → [`00bded20`](../00bde/00bded20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded20` · 推定シンボル `None` · 推定型 `None`
- [`00afcf9c`](#insn-00afcf9c) → [`00afcfd4`](#insn-00afcfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfac`](#insn-00afcfac) → [`00afcfd0`](#insn-00afcfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfb8`](#insn-00afcfb8) → `002958ca`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfc0`](#insn-00afcfc0) → [`00bded20`](../00bde/00bded20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded20` · 推定シンボル `None` · 推定型 `None`
- [`00afcfc8`](#insn-00afcfc8) → [`00afcfa8`](#insn-00afcfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfcc`](#insn-00afcfcc) → [`00afcfd4`](#insn-00afcfd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcff4`](#insn-00afcff4) → [`00afcf44`](#insn-00afcf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd000`](#insn-00afd000) → `002958ca`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd004`](#insn-00afd004) → [`00bded20`](../00bde/00bded20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded20` · 推定シンボル `None` · 推定型 `None`
- [`00afd008`](#insn-00afd008) → [`00afcf44`](#insn-00afcf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd01c`](#insn-00afd01c) → [`00afd090`](#insn-00afd090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd028`](#insn-00afd028) → `002958ca`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd030`](#insn-00afd030) → [`00bded20`](../00bde/00bded20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded20` · 推定シンボル `None` · 推定型 `None`
- [`00afd038`](#insn-00afd038) → [`00afd018`](#insn-00afd018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd040`](#insn-00afd040) → [`00afd09c`](#insn-00afd09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd044`](#insn-00afd044) → [`00afd058`](#insn-00afd058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd050`](#insn-00afd050) → `002958ca`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd054`](#insn-00afd054) → [`00bdb0e0`](../00bdb/00bdb0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0e0` · 推定シンボル `None` · 推定型 `None`
- [`00afd070`](#insn-00afd070) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd084`](#insn-00afd084) → [`00bded00`](../00bde/00bded00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded00` · 推定シンボル `None` · 推定型 `None`
- [`00afd08c`](#insn-00afd08c) → [`00afd09c`](#insn-00afd09c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd098`](#insn-00afd098) → [`00afd044`](#insn-00afd044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0a0`](#insn-00afd0a0) → [`00afcf48`](#insn-00afcf48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0a4`](#insn-00afd0a4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0a8`](#insn-00afd0a8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0ac`](#insn-00afd0ac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0b0`](#insn-00afd0b0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0b4`](#insn-00afd0b4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0b8`](#insn-00afd0b8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afced8`](#insn-00afced8)

~~~json
{
  "source": "00afced8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcedc`](#insn-00afcedc)

~~~json
{
  "source": "00afcedc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcee0`](#insn-00afcee0)

~~~json
{
  "source": "00afcee0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcee4`](#insn-00afcee4)

~~~json
{
  "source": "00afcee4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcee8`](#insn-00afcee8)

~~~json
{
  "source": "00afcee8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afceec`](#insn-00afceec)

~~~json
{
  "source": "00afceec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf1c`](#insn-00afcf1c)

~~~json
{
  "source": "00afcf1c",
  "target": "00afd0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf3c`](#insn-00afcf3c)

~~~json
{
  "source": "00afcf3c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf40`](#insn-00afcf40)

~~~json
{
  "source": "00afcf40",
  "target": "00afcf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf6c`](#insn-00afcf6c)

~~~json
{
  "source": "00afcf6c",
  "target": "00afd0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf88`](#insn-00afcf88)

~~~json
{
  "source": "00afcf88",
  "target": "00afcfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf94`](#insn-00afcf94)

~~~json
{
  "source": "00afcf94",
  "target": "002958ca",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf98`](#insn-00afcf98)

~~~json
{
  "source": "00afcf98",
  "target": "00bded20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcf9c`](#insn-00afcf9c)

~~~json
{
  "source": "00afcf9c",
  "target": "00afcfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfac`](#insn-00afcfac)

~~~json
{
  "source": "00afcfac",
  "target": "00afcfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfb8`](#insn-00afcfb8)

~~~json
{
  "source": "00afcfb8",
  "target": "002958ca",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfc0`](#insn-00afcfc0)

~~~json
{
  "source": "00afcfc0",
  "target": "00bded20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcfc8`](#insn-00afcfc8)

~~~json
{
  "source": "00afcfc8",
  "target": "00afcfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfcc`](#insn-00afcfcc)

~~~json
{
  "source": "00afcfcc",
  "target": "00afcfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcff4`](#insn-00afcff4)

~~~json
{
  "source": "00afcff4",
  "target": "00afcf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd000`](#insn-00afd000)

~~~json
{
  "source": "00afd000",
  "target": "002958ca",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd004`](#insn-00afd004)

~~~json
{
  "source": "00afd004",
  "target": "00bded20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd008`](#insn-00afd008)

~~~json
{
  "source": "00afd008",
  "target": "00afcf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd01c`](#insn-00afd01c)

~~~json
{
  "source": "00afd01c",
  "target": "00afd090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd028`](#insn-00afd028)

~~~json
{
  "source": "00afd028",
  "target": "002958ca",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd030`](#insn-00afd030)

~~~json
{
  "source": "00afd030",
  "target": "00bded20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd038`](#insn-00afd038)

~~~json
{
  "source": "00afd038",
  "target": "00afd018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd040`](#insn-00afd040)

~~~json
{
  "source": "00afd040",
  "target": "00afd09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd044`](#insn-00afd044)

~~~json
{
  "source": "00afd044",
  "target": "00afd058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd050`](#insn-00afd050)

~~~json
{
  "source": "00afd050",
  "target": "002958ca",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd054`](#insn-00afd054)

~~~json
{
  "source": "00afd054",
  "target": "00bdb0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd070`](#insn-00afd070)

~~~json
{
  "source": "00afd070",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd084`](#insn-00afd084)

~~~json
{
  "source": "00afd084",
  "target": "00bded00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd08c`](#insn-00afd08c)

~~~json
{
  "source": "00afd08c",
  "target": "00afd09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd098`](#insn-00afd098)

~~~json
{
  "source": "00afd098",
  "target": "00afd044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0a0`](#insn-00afd0a0)

~~~json
{
  "source": "00afd0a0",
  "target": "00afcf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0a4`](#insn-00afd0a4)

~~~json
{
  "source": "00afd0a4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0a8`](#insn-00afd0a8)

~~~json
{
  "source": "00afd0a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0ac`](#insn-00afd0ac)

~~~json
{
  "source": "00afd0ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0b0`](#insn-00afd0b0)

~~~json
{
  "source": "00afd0b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0b4`](#insn-00afd0b4)

~~~json
{
  "source": "00afd0b4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0b8`](#insn-00afd0b8)

~~~json
{
  "source": "00afd0b8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
