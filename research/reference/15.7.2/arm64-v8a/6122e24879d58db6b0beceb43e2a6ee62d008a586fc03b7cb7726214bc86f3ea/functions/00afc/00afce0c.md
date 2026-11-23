# 00afce0c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afced4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afced4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-2592ffbc7dc471e9e17e020d90b15684)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afce0c",
  "name": "_ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f410c2961d0cc37920bcca1d75b34288fa05830a36c44a9421bc9d2b197a0f46",
  "source_text_sha256": "f410c2961d0cc37920bcca1d75b34288fa05830a36c44a9421bc9d2b197a0f46",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afce0c",
        "00afcffb"
      ]
    ],
    "bytes_sha256": "59658ac4efd4e74f80fdfd1ef9aa0094fbf4d986c401e0e7b9353786cbbc1d75",
    "instruction_count": 124,
    "instruction_bytes": 496,
    "body_bytes": 496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdec30](../00bde/00bdec30.md)

## 呼び出し先

- [00bdb030](../00bdb/00bdb030.md)
- [00bdec50](../00bde/00bdec50.md)
- [00bdec70](../00bde/00bdec70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4052 bytes

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
    pbVar1 = param_2 + 1;
    bVar11 = true;
    do {
      uVar2 = (ulong)(bVar3 >> 1);
      pbVar4 = pbVar1;
                    /* try { // try from 00afceac to 00bfcec3 has its CatchHandler @ 00aff3ac */
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
      pbVar9 = pbVar10;
                    /* try { // try from 00afcec4 to 00bfcf27 has its CatchHandler @ 00af560c */
      if ((pbVar4 + uVar2 != pbVar10) &&
         (lVar6 = __strchr_chk(&DAT_0029583d,*pbVar10,2), lVar6 != 0)) {
        do {
          pbVar9 = pbVar4 + uVar2;
          if (pbVar4 + (uVar2 - 1) == pbVar10) break;
          pbVar9 = pbVar10 + 1;
          lVar6 = __strchr_chk(&DAT_0029583d,pbVar10[1],2);
          pbVar10 = pbVar9;
        } while (lVar6 != 0);
      }
      uVar8 = (ulong)(*param_2 >> 1);
      pbVar4 = pbVar1;
      if ((*param_2 & 1) != 0) {
        uVar8 = *(ulong *)(param_2 + 8);
        pbVar4 = *(byte **)(param_2 + 0x10);
      }
                    /* try { // try from 00afcf28 to 00bfcf2f has its CatchHandler @ 00aff3a8 */
      pbVar10 = pbVar9;
      if ((pbVar4 + uVar8 != pbVar9) && (lVar6 = __strchr_chk(&DAT_0029583d,*pbVar9,2), lVar6 == 0))
      {
        pbVar7 = pbVar9;
        do {
          pbVar10 = pbVar4 + uVar8;
          if (pbVar4 + (uVar8 - 1) == pbVar7) break;
                    /* try { // try from 00afcf58 to 00bfcf6f has its CatchHandler @ 00aff3a4 */
          pbVar10 = pbVar7 + 1;
          pbVar7 = pbVar7 + 1;
          lVar6 = __strchr_chk(&DAT_0029583d,*pbVar10,2);
          pbVar10 = pbVar7;
        } while (lVar6 == 0);
        if (pbVar10 != pbVar9) {
          if (!bVar11) {
                    /* try { // try from 00afcf80 to 00bfcf87 has its CatchHandler @ 00aff3a0 */
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                      (param_1,&DAT_0029583d,1);
          }
          uVar8 = (ulong)(*param_1 >> 1);
          pbVar4 = param_1 + 1;
                    /* try { // try from 00afcfb0 to 00bfcfc7 has its CatchHandler @ 00aff39c */
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
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
    } while (pbVar4 + uVar2 != pbVar10);
  }
                    /* try { // try from 00afcff8 to 00bfd00f has its CatchHandler @ 00aff38c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afce0c"></a> `00afce0c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afce10"></a> `00afce10` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afce14"></a> `00afce14` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afce18"></a> `00afce18` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afce1c"></a> `00afce1c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afce20"></a> `00afce20` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afce24"></a> `00afce24` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afce28"></a> `00afce28` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00afce2c"></a> `00afce2c` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00afce30"></a> `00afce30` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afce34"></a> `00afce34` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00afce38"></a> `00afce38` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00afce3c"></a> `00afce3c` | `09 a8 40 a9` | ldp x9,x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afce40"></a> `00afce40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afce44"></a> `00afce44` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afce48"></a> `00afce48` | `eb 17 9f 1a` | cset w11,eq | `FALL_THROUGH`
<a id="insn-00afce4c"></a> `00afce4c` | `8c 01 89 9a` | csel x12,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00afce50"></a> `00afce50` | `57 15 80 9a` | csinc x23,x10,x0,ne | `FALL_THROUGH`
<a id="insn-00afce54"></a> `00afce54` | `4c 0c 00 b4` | cbz x12,0x00afcfdc | `CONDITIONAL_JUMP`
<a id="insn-00afce58"></a> `00afce58` | `d5 bc ff b0` | adrp x21,0x295000 | `FALL_THROUGH`
<a id="insn-00afce5c"></a> `00afce5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afce60"></a> `00afce60` | `18 04 00 91` | add x24,x0,#0x1 | `FALL_THROUGH`
<a id="insn-00afce64"></a> `00afce64` | `8c 06 00 91` | add x12,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00afce68"></a> `00afce68` | `3a 00 80 52` | mov w26,#0x1 | `FALL_THROUGH`
<a id="insn-00afce6c"></a> `00afce6c` | `b5 f6 20 91` | add x21,x21,#0x83d | `FALL_THROUGH`
<a id="insn-00afce70"></a> `00afce70` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00afce74"></a> `00afce74` | `ec 07 00 f9` | str x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afce78"></a> `00afce78` | `0c 00 00 14` | b 0x00afcea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afce7c"></a> `00afce7c` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00afce80"></a> `00afce80` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00afce84"></a> `00afce84` | `69 aa 40 a9` | ldp x9,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afce88"></a> `00afce88` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afce8c"></a> `00afce8c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afce90"></a> `00afce90` | `0d 03 8a 9a` | csel x13,x24,x10,eq | `FALL_THROUGH`
<a id="insn-00afce94"></a> `00afce94` | `8c 01 89 9a` | csel x12,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00afce98"></a> `00afce98` | `ac 01 0c 8b` | add x12,x13,x12 | `FALL_THROUGH`
<a id="insn-00afce9c"></a> `00afce9c` | `eb 17 9f 1a` | cset w11,eq | `FALL_THROUGH`
<a id="insn-00afcea0"></a> `00afcea0` | `9f 01 17 eb` | cmp x12,x23 | `FALL_THROUGH`
<a id="insn-00afcea4"></a> `00afcea4` | `c0 09 00 54` | b.eq 0x00afcfdc | `CONDITIONAL_JUMP`
<a id="insn-00afcea8"></a> `00afcea8` | `08 1d 01 53` | ubfx w8,w8,#0x1,#0x7 | `FALL_THROUGH`
<a id="insn-00afceac"></a> `00afceac` | `7f 01 00 72` | tst w11,#0x1 | `FALL_THROUGH`
<a id="insn-00afceb0"></a> `00afceb0` | `1c 13 8a 9a` | csel x28,x24,x10,ne | `FALL_THROUGH`
<a id="insn-00afceb4"></a> `00afceb4` | `19 11 89 9a` | csel x25,x8,x9,ne | `FALL_THROUGH`
<a id="insn-00afceb8"></a> `00afceb8` | `9b 03 19 8b` | add x27,x28,x25 | `FALL_THROUGH`
<a id="insn-00afcebc"></a> `00afcebc` | `7f 03 17 eb` | cmp x27,x23 | `FALL_THROUGH`
<a id="insn-00afcec0"></a> `00afcec0` | `60 02 00 54` | b.eq 0x00afcf0c | `CONDITIONAL_JUMP`
<a id="insn-00afcec4"></a> `00afcec4` | `e1 02 40 39` | ldrb w1,[x23] | `FALL_THROUGH`
<a id="insn-00afcec8"></a> `00afcec8` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afcecc"></a> `00afcecc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afced0"></a> `00afced0` | `68 87 03 94` | bl 0x00bdec70 | `UNCONDITIONAL_CALL`
<a id="insn-00afced4"></a> `00afced4` | `c0 01 00 b4` | cbz x0,0x00afcf0c | `CONDITIONAL_JUMP`
<a id="insn-00afced8"></a> `00afced8` | `88 03 19 8b` | add x8,x28,x25 | `FALL_THROUGH`
<a id="insn-00afcedc"></a> `00afcedc` | `1c 05 00 d1` | sub x28,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcee0"></a> `00afcee0` | `9f 03 17 eb` | cmp x28,x23 | `FALL_THROUGH`
<a id="insn-00afcee4"></a> `00afcee4` | `20 01 00 54` | b.eq 0x00afcf08 | `CONDITIONAL_JUMP`
<a id="insn-00afcee8"></a> `00afcee8` | `e1 06 40 39` | ldrb w1,[x23, #0x1] | `FALL_THROUGH`
<a id="insn-00afceec"></a> `00afceec` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afcef0"></a> `00afcef0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afcef4"></a> `00afcef4` | `f6 06 00 91` | add x22,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00afcef8"></a> `00afcef8` | `5e 87 03 94` | bl 0x00bdec70 | `UNCONDITIONAL_CALL`
<a id="insn-00afcefc"></a> `00afcefc` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00afcf00"></a> `00afcf00` | `00 ff ff b5` | cbnz x0,0x00afcee0 | `CONDITIONAL_JUMP`
<a id="insn-00afcf04"></a> `00afcf04` | `02 00 00 14` | b 0x00afcf0c | `UNCONDITIONAL_JUMP`
<a id="insn-00afcf08"></a> `00afcf08` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00afcf0c"></a> `00afcf0c` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00afcf10"></a> `00afcf10` | `6a a6 40 a9` | ldp x10,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afcf14"></a> `00afcf14` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf18"></a> `00afcf18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf1c"></a> `00afcf1c` | `17 03 89 9a` | csel x23,x24,x9,eq | `FALL_THROUGH`
<a id="insn-00afcf20"></a> `00afcf20` | `79 01 8a 9a` | csel x25,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afcf24"></a> `00afcf24` | `fb 02 19 8b` | add x27,x23,x25 | `FALL_THROUGH`
<a id="insn-00afcf28"></a> `00afcf28` | `7f 03 16 eb` | cmp x27,x22 | `FALL_THROUGH`
<a id="insn-00afcf2c"></a> `00afcf2c` | `80 fa ff 54` | b.eq 0x00afce7c | `CONDITIONAL_JUMP`
<a id="insn-00afcf30"></a> `00afcf30` | `c1 02 40 39` | ldrb w1,[x22] | `FALL_THROUGH`
<a id="insn-00afcf34"></a> `00afcf34` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afcf38"></a> `00afcf38` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afcf3c"></a> `00afcf3c` | `4d 87 03 94` | bl 0x00bdec70 | `UNCONDITIONAL_CALL`
<a id="insn-00afcf40"></a> `00afcf40` | `e0 f9 ff b5` | cbnz x0,0x00afce7c | `CONDITIONAL_JUMP`
<a id="insn-00afcf44"></a> `00afcf44` | `e8 02 19 8b` | add x8,x23,x25 | `FALL_THROUGH`
<a id="insn-00afcf48"></a> `00afcf48` | `1c 05 00 d1` | sub x28,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf4c"></a> `00afcf4c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00afcf50"></a> `00afcf50` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-00afcf54"></a> `00afcf54` | `a0 03 00 54` | b.eq 0x00afcfc8 | `CONDITIONAL_JUMP`
<a id="insn-00afcf58"></a> `00afcf58` | `01 05 40 39` | ldrb w1,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00afcf5c"></a> `00afcf5c` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00afcf60"></a> `00afcf60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afcf64"></a> `00afcf64` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf68"></a> `00afcf68` | `42 87 03 94` | bl 0x00bdec70 | `UNCONDITIONAL_CALL`
<a id="insn-00afcf6c"></a> `00afcf6c` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00afcf70"></a> `00afcf70` | `00 ff ff b4` | cbz x0,0x00afcf50 | `CONDITIONAL_JUMP`
<a id="insn-00afcf74"></a> `00afcf74` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00afcf78"></a> `00afcf78` | `e0 02 00 54` | b.eq 0x00afcfd4 | `CONDITIONAL_JUMP`
<a id="insn-00afcf7c"></a> `00afcf7c` | `ba 00 00 37` | tbnz w26,#0x0,0x00afcf90 | `CONDITIONAL_JUMP`
<a id="insn-00afcf80"></a> `00afcf80` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afcf84"></a> `00afcf84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afcf88"></a> `00afcf88` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afcf8c"></a> `00afcf8c` | `29 78 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00afcf90"></a> `00afcf90` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00afcf94"></a> `00afcf94` | `8a a6 40 a9` | ldp x10,x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00afcf98"></a> `00afcf98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afcf9c"></a> `00afcf9c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afcfa0"></a> `00afcfa0` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcfa4"></a> `00afcfa4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afcfa8"></a> `00afcfa8` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afcfac"></a> `00afcfac` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00afcfb0"></a> `00afcfb0` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00afcfb4"></a> `00afcfb4` | `69 01 8a 9a` | csel x9,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afcfb8"></a> `00afcfb8` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00afcfbc"></a> `00afcfbc` | `25 87 03 94` | bl 0x00bdec50 | `UNCONDITIONAL_CALL`
<a id="insn-00afcfc0"></a> `00afcfc0` | `fa 03 1f 2a` | mov w26,wzr | `FALL_THROUGH`
<a id="insn-00afcfc4"></a> `00afcfc4` | `04 00 00 14` | b 0x00afcfd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afcfc8"></a> `00afcfc8` | `f7 03 1b aa` | mov x23,x27 | `FALL_THROUGH`
<a id="insn-00afcfcc"></a> `00afcfcc` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00afcfd0"></a> `00afcfd0` | `61 fd ff 54` | b.ne 0x00afcf7c | `CONDITIONAL_JUMP`
<a id="insn-00afcfd4"></a> `00afcfd4` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00afcfd8"></a> `00afcfd8` | `aa ff ff 17` | b 0x00afce80 | `UNCONDITIONAL_JUMP`
<a id="insn-00afcfdc"></a> `00afcfdc` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afcfe0"></a> `00afcfe0` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afcfe4"></a> `00afcfe4` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afcfe8"></a> `00afcfe8` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afcfec"></a> `00afcfec` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcff0"></a> `00afcff0` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcff4"></a> `00afcff4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afcff8"></a> `00afcff8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afce0c`](#insn-00afce0c) 範囲 `[['00afce0c', '00afce57']]`
  - `CONDITIONAL_JUMP` [`00afce54`](#insn-00afce54) → [`00afcfdc`](#insn-00afcfdc)
  - `FALL_THROUGH` [`00afce54`](#insn-00afce54) → [`00afce58`](#insn-00afce58)
- ブロック [`00afce58`](#insn-00afce58) 範囲 `[['00afce58', '00afce7b']]`
  - `UNCONDITIONAL_JUMP` [`00afce78`](#insn-00afce78) → [`00afcea8`](#insn-00afcea8)
- ブロック [`00afce7c`](#insn-00afce7c) 範囲 `[['00afce7c', '00afce7f']]`
  - `FALL_THROUGH` [`00afce7c`](#insn-00afce7c) → [`00afce80`](#insn-00afce80)
- ブロック [`00afce80`](#insn-00afce80) 範囲 `[['00afce80', '00afcea7']]`
  - `CONDITIONAL_JUMP` [`00afcea4`](#insn-00afcea4) → [`00afcfdc`](#insn-00afcfdc)
  - `FALL_THROUGH` [`00afcea4`](#insn-00afcea4) → [`00afcea8`](#insn-00afcea8)
- ブロック [`00afcea8`](#insn-00afcea8) 範囲 `[['00afcea8', '00afceab']]`
  - `FALL_THROUGH` [`00afcea8`](#insn-00afcea8) → [`00afceac`](#insn-00afceac)
- ブロック [`00afceac`](#insn-00afceac) 範囲 `[['00afceac', '00afcec3']]`
  - `CONDITIONAL_JUMP` [`00afcec0`](#insn-00afcec0) → [`00afcf0c`](#insn-00afcf0c)
  - `FALL_THROUGH` [`00afcec0`](#insn-00afcec0) → [`00afcec4`](#insn-00afcec4)
- ブロック [`00afcec4`](#insn-00afcec4) 範囲 `[['00afcec4', '00afced7']]`
  - `CONDITIONAL_JUMP` [`00afced4`](#insn-00afced4) → [`00afcf0c`](#insn-00afcf0c)
  - `FALL_THROUGH` [`00afced4`](#insn-00afced4) → [`00afced8`](#insn-00afced8)
- ブロック [`00afced8`](#insn-00afced8) 範囲 `[['00afced8', '00afcedf']]`
  - `FALL_THROUGH` [`00afcedc`](#insn-00afcedc) → [`00afcee0`](#insn-00afcee0)
- ブロック [`00afcee0`](#insn-00afcee0) 範囲 `[['00afcee0', '00afcee7']]`
  - `CONDITIONAL_JUMP` [`00afcee4`](#insn-00afcee4) → [`00afcf08`](#insn-00afcf08)
  - `FALL_THROUGH` [`00afcee4`](#insn-00afcee4) → [`00afcee8`](#insn-00afcee8)
- ブロック [`00afcee8`](#insn-00afcee8) 範囲 `[['00afcee8', '00afcf03']]`
  - `CONDITIONAL_JUMP` [`00afcf00`](#insn-00afcf00) → [`00afcee0`](#insn-00afcee0)
  - `FALL_THROUGH` [`00afcf00`](#insn-00afcf00) → [`00afcf04`](#insn-00afcf04)
- ブロック [`00afcf04`](#insn-00afcf04) 範囲 `[['00afcf04', '00afcf07']]`
  - `UNCONDITIONAL_JUMP` [`00afcf04`](#insn-00afcf04) → [`00afcf0c`](#insn-00afcf0c)
- ブロック [`00afcf08`](#insn-00afcf08) 範囲 `[['00afcf08', '00afcf0b']]`
  - `FALL_THROUGH` [`00afcf08`](#insn-00afcf08) → [`00afcf0c`](#insn-00afcf0c)
- ブロック [`00afcf0c`](#insn-00afcf0c) 範囲 `[['00afcf0c', '00afcf27']]`
  - `FALL_THROUGH` [`00afcf24`](#insn-00afcf24) → [`00afcf28`](#insn-00afcf28)
- ブロック [`00afcf28`](#insn-00afcf28) 範囲 `[['00afcf28', '00afcf2f']]`
  - `CONDITIONAL_JUMP` [`00afcf2c`](#insn-00afcf2c) → [`00afce7c`](#insn-00afce7c)
  - `FALL_THROUGH` [`00afcf2c`](#insn-00afcf2c) → [`00afcf30`](#insn-00afcf30)
- ブロック [`00afcf30`](#insn-00afcf30) 範囲 `[['00afcf30', '00afcf43']]`
  - `CONDITIONAL_JUMP` [`00afcf40`](#insn-00afcf40) → [`00afce7c`](#insn-00afce7c)
  - `FALL_THROUGH` [`00afcf40`](#insn-00afcf40) → [`00afcf44`](#insn-00afcf44)
- ブロック [`00afcf44`](#insn-00afcf44) 範囲 `[['00afcf44', '00afcf4f']]`
  - `FALL_THROUGH` [`00afcf4c`](#insn-00afcf4c) → [`00afcf50`](#insn-00afcf50)
- ブロック [`00afcf50`](#insn-00afcf50) 範囲 `[['00afcf50', '00afcf57']]`
  - `CONDITIONAL_JUMP` [`00afcf54`](#insn-00afcf54) → [`00afcfc8`](#insn-00afcfc8)
  - `FALL_THROUGH` [`00afcf54`](#insn-00afcf54) → [`00afcf58`](#insn-00afcf58)
- ブロック [`00afcf58`](#insn-00afcf58) 範囲 `[['00afcf58', '00afcf73']]`
  - `CONDITIONAL_JUMP` [`00afcf70`](#insn-00afcf70) → [`00afcf50`](#insn-00afcf50)
  - `FALL_THROUGH` [`00afcf70`](#insn-00afcf70) → [`00afcf74`](#insn-00afcf74)
- ブロック [`00afcf74`](#insn-00afcf74) 範囲 `[['00afcf74', '00afcf7b']]`
  - `CONDITIONAL_JUMP` [`00afcf78`](#insn-00afcf78) → [`00afcfd4`](#insn-00afcfd4)
  - `FALL_THROUGH` [`00afcf78`](#insn-00afcf78) → [`00afcf7c`](#insn-00afcf7c)
- ブロック [`00afcf7c`](#insn-00afcf7c) 範囲 `[['00afcf7c', '00afcf7f']]`
  - `CONDITIONAL_JUMP` [`00afcf7c`](#insn-00afcf7c) → [`00afcf90`](#insn-00afcf90)
  - `FALL_THROUGH` [`00afcf7c`](#insn-00afcf7c) → [`00afcf80`](#insn-00afcf80)
- ブロック [`00afcf80`](#insn-00afcf80) 範囲 `[['00afcf80', '00afcf8f']]`
  - `FALL_THROUGH` [`00afcf8c`](#insn-00afcf8c) → [`00afcf90`](#insn-00afcf90)
- ブロック [`00afcf90`](#insn-00afcf90) 範囲 `[['00afcf90', '00afcfaf']]`
  - `FALL_THROUGH` [`00afcfac`](#insn-00afcfac) → [`00afcfb0`](#insn-00afcfb0)
- ブロック [`00afcfb0`](#insn-00afcfb0) 範囲 `[['00afcfb0', '00afcfc7']]`
  - `UNCONDITIONAL_JUMP` [`00afcfc4`](#insn-00afcfc4) → [`00afcfd4`](#insn-00afcfd4)
- ブロック [`00afcfc8`](#insn-00afcfc8) 範囲 `[['00afcfc8', '00afcfd3']]`
  - `CONDITIONAL_JUMP` [`00afcfd0`](#insn-00afcfd0) → [`00afcf7c`](#insn-00afcf7c)
  - `FALL_THROUGH` [`00afcfd0`](#insn-00afcfd0) → [`00afcfd4`](#insn-00afcfd4)
- ブロック [`00afcfd4`](#insn-00afcfd4) 範囲 `[['00afcfd4', '00afcfdb']]`
  - `UNCONDITIONAL_JUMP` [`00afcfd8`](#insn-00afcfd8) → [`00afce80`](#insn-00afce80)
- ブロック [`00afcfdc`](#insn-00afcfdc) 範囲 `[['00afcfdc', '00afcff7']]`
  - `FALL_THROUGH` [`00afcff4`](#insn-00afcff4) → [`00afcff8`](#insn-00afcff8)
- ブロック [`00afcff8`](#insn-00afcff8) 範囲 `[['00afcff8', '00afcffb']]`

## 命令位置別の参照

- [`00afce10`](#insn-00afce10) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce14`](#insn-00afce14) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce18`](#insn-00afce18) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce1c`](#insn-00afce1c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce20`](#insn-00afce20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce24`](#insn-00afce24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce54`](#insn-00afce54) → [`00afcfdc`](#insn-00afcfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce74`](#insn-00afce74) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce78`](#insn-00afce78) → [`00afcea8`](#insn-00afcea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcea4`](#insn-00afcea4) → [`00afcfdc`](#insn-00afcfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcec0`](#insn-00afcec0) → [`00afcf0c`](#insn-00afcf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcecc`](#insn-00afcecc) → `0029583d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afced0`](#insn-00afced0) → [`00bdec70`](../00bde/00bdec70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec70` · 推定シンボル `None` · 推定型 `None`
- [`00afced4`](#insn-00afced4) → [`00afcf0c`](#insn-00afcf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcee4`](#insn-00afcee4) → [`00afcf08`](#insn-00afcf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcef0`](#insn-00afcef0) → `0029583d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcef8`](#insn-00afcef8) → [`00bdec70`](../00bde/00bdec70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec70` · 推定シンボル `None` · 推定型 `None`
- [`00afcf00`](#insn-00afcf00) → [`00afcee0`](#insn-00afcee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf04`](#insn-00afcf04) → [`00afcf0c`](#insn-00afcf0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf2c`](#insn-00afcf2c) → [`00afce7c`](#insn-00afce7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf38`](#insn-00afcf38) → `0029583d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf3c`](#insn-00afcf3c) → [`00bdec70`](../00bde/00bdec70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec70` · 推定シンボル `None` · 推定型 `None`
- [`00afcf40`](#insn-00afcf40) → [`00afce7c`](#insn-00afce7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf54`](#insn-00afcf54) → [`00afcfc8`](#insn-00afcfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf60`](#insn-00afcf60) → `0029583d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf68`](#insn-00afcf68) → [`00bdec70`](../00bde/00bdec70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec70` · 推定シンボル `None` · 推定型 `None`
- [`00afcf70`](#insn-00afcf70) → [`00afcf50`](#insn-00afcf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf78`](#insn-00afcf78) → [`00afcfd4`](#insn-00afcfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf7c`](#insn-00afcf7c) → [`00afcf90`](#insn-00afcf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf88`](#insn-00afcf88) → `0029583d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf8c`](#insn-00afcf8c) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00afcfa8`](#insn-00afcfa8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfbc`](#insn-00afcfbc) → [`00bdec50`](../00bde/00bdec50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec50` · 推定シンボル `None` · 推定型 `None`
- [`00afcfc4`](#insn-00afcfc4) → [`00afcfd4`](#insn-00afcfd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfd0`](#insn-00afcfd0) → [`00afcf7c`](#insn-00afcf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfd8`](#insn-00afcfd8) → [`00afce80`](#insn-00afce80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfdc`](#insn-00afcfdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfe0`](#insn-00afcfe0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfe4`](#insn-00afcfe4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfe8`](#insn-00afcfe8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfec`](#insn-00afcfec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcff0`](#insn-00afcff0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afce10`](#insn-00afce10)

~~~json
{
  "source": "00afce10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce14`](#insn-00afce14)

~~~json
{
  "source": "00afce14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce18`](#insn-00afce18)

~~~json
{
  "source": "00afce18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce1c`](#insn-00afce1c)

~~~json
{
  "source": "00afce1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce20`](#insn-00afce20)

~~~json
{
  "source": "00afce20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce24`](#insn-00afce24)

~~~json
{
  "source": "00afce24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce54`](#insn-00afce54)

~~~json
{
  "source": "00afce54",
  "target": "00afcfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce74`](#insn-00afce74)

~~~json
{
  "source": "00afce74",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce78`](#insn-00afce78)

~~~json
{
  "source": "00afce78",
  "target": "00afcea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcea4`](#insn-00afcea4)

~~~json
{
  "source": "00afcea4",
  "target": "00afcfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcec0`](#insn-00afcec0)

~~~json
{
  "source": "00afcec0",
  "target": "00afcf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcecc`](#insn-00afcecc)

~~~json
{
  "source": "00afcecc",
  "target": "0029583d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afced0`](#insn-00afced0)

~~~json
{
  "source": "00afced0",
  "target": "00bdec70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afced4`](#insn-00afced4)

~~~json
{
  "source": "00afced4",
  "target": "00afcf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcee4`](#insn-00afcee4)

~~~json
{
  "source": "00afcee4",
  "target": "00afcf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcef0`](#insn-00afcef0)

~~~json
{
  "source": "00afcef0",
  "target": "0029583d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcef8`](#insn-00afcef8)

~~~json
{
  "source": "00afcef8",
  "target": "00bdec70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcf00`](#insn-00afcf00)

~~~json
{
  "source": "00afcf00",
  "target": "00afcee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf04`](#insn-00afcf04)

~~~json
{
  "source": "00afcf04",
  "target": "00afcf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf2c`](#insn-00afcf2c)

~~~json
{
  "source": "00afcf2c",
  "target": "00afce7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf38`](#insn-00afcf38)

~~~json
{
  "source": "00afcf38",
  "target": "0029583d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf3c`](#insn-00afcf3c)

~~~json
{
  "source": "00afcf3c",
  "target": "00bdec70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcf40`](#insn-00afcf40)

~~~json
{
  "source": "00afcf40",
  "target": "00afce7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf54`](#insn-00afcf54)

~~~json
{
  "source": "00afcf54",
  "target": "00afcfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf60`](#insn-00afcf60)

~~~json
{
  "source": "00afcf60",
  "target": "0029583d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf68`](#insn-00afcf68)

~~~json
{
  "source": "00afcf68",
  "target": "00bdec70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcf70`](#insn-00afcf70)

~~~json
{
  "source": "00afcf70",
  "target": "00afcf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf78`](#insn-00afcf78)

~~~json
{
  "source": "00afcf78",
  "target": "00afcfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf7c`](#insn-00afcf7c)

~~~json
{
  "source": "00afcf7c",
  "target": "00afcf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf88`](#insn-00afcf88)

~~~json
{
  "source": "00afcf88",
  "target": "0029583d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf8c`](#insn-00afcf8c)

~~~json
{
  "source": "00afcf8c",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcfa8`](#insn-00afcfa8)

~~~json
{
  "source": "00afcfa8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfbc`](#insn-00afcfbc)

~~~json
{
  "source": "00afcfbc",
  "target": "00bdec50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcfc4`](#insn-00afcfc4)

~~~json
{
  "source": "00afcfc4",
  "target": "00afcfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfd0`](#insn-00afcfd0)

~~~json
{
  "source": "00afcfd0",
  "target": "00afcf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfd8`](#insn-00afcfd8)

~~~json
{
  "source": "00afcfd8",
  "target": "00afce80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfdc`](#insn-00afcfdc)

~~~json
{
  "source": "00afcfdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfe0`](#insn-00afcfe0)

~~~json
{
  "source": "00afcfe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfe4`](#insn-00afcfe4)

~~~json
{
  "source": "00afcfe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfe8`](#insn-00afcfe8)

~~~json
{
  "source": "00afcfe8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfec`](#insn-00afcfec)

~~~json
{
  "source": "00afcfec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcff0`](#insn-00afcff0)

~~~json
{
  "source": "00afcff0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
