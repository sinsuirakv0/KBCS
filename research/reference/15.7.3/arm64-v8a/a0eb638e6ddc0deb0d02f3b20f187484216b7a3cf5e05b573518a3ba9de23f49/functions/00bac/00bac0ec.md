# 00bac0ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bac024`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac024.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0026.md#compare-a11701e6049ba7c4de7d79a9d4ef3316)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bac130`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac130.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0019.md#compare-de000db82e52826cca827a44197e2d35)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bac0ec",
  "name": "FUN_00bac0ec",
  "size": 660,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "494c2b9c764a29c5eb6621ead771a3eb51fa301563260ed8b786ede6857d3afd",
  "source_text_sha256": "494c2b9c764a29c5eb6621ead771a3eb51fa301563260ed8b786ede6857d3afd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bac0ec",
        "00bac37f"
      ]
    ],
    "bytes_sha256": "dfe944a6df67142a55c96f11daf9ca74566ec70c47183c6d56bc21e4ece03f6e",
    "instruction_count": 165,
    "instruction_bytes": 660,
    "body_bytes": 660,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bac084](../00bac/00bac084.md)
- [00bac664](../00bac/00bac664.md)
- [00baecf0](../00bae/00baecf0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5203 bytes

~~~c

bool FUN_00bac0ec(long param_1,byte *param_2,long *param_3,long param_4,ushort *param_5,
                 long *param_6,ulong param_7,uint param_8)

{
  uint uVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  ushort *puVar5;
  byte *pbVar6;
  long lVar7;
  uint uVar8;
  ushort *puVar9;
  uint uVar10;
  
  *param_3 = param_1;
  *param_6 = param_4;
  pbVar6 = (byte *)*param_3;
  if (((((param_8 >> 2 & 1) != 0) && (2 < (long)param_2 - (long)pbVar6)) && (*pbVar6 == 0xef)) &&
     ((pbVar6[1] == 0xbb && (pbVar6[2] == 0xbf)))) {
    pbVar6 = pbVar6 + 3;
    *param_3 = (long)pbVar6;
  }
  if (param_2 <= pbVar6) {
    return false;
  }
  puVar5 = (ushort *)*param_6;
  do {
    puVar9 = puVar5;
    if (param_5 <= puVar9) break;
    bVar2 = *pbVar6;
    if (param_7 < bVar2) {
      return (bool)2;
    }
    if ((char)bVar2 < '\0') {
      if (bVar2 < 0xc2) {
        return (bool)2;
      }
                    /* try { // try from 00bac19c to 00cac1a7 has its CatchHandler @ 00bac2e0 */
      uVar8 = (uint)bVar2;
      if (bVar2 < 0xe0) {
                    /* try { // try from 00bac1ac to 00cac1bf has its CatchHandler @ 00bac2c0 */
        if ((long)param_2 - (long)pbVar6 < 2) {
          return true;
        }
        if ((pbVar6[1] & 0xc0) != 0x80) {
          return (bool)2;
        }
                    /* try { // try from 00bac1c0 to 00cac1db has its CatchHandler @ 00bac28c */
        uVar8 = pbVar6[1] & 0x3f | (bVar2 & 0x1f) << 6;
        if (param_7 < uVar8) {
          return (bool)2;
        }
        *puVar9 = (ushort)uVar8;
        pbVar6 = pbVar6 + 2;
      }
      else if (uVar8 < 0xf0) {
        if ((long)param_2 - (long)pbVar6 < 2) {
          return true;
        }
        uVar10 = (uint)pbVar6[1];
        if (uVar8 == 0xed) {
          uVar8 = uVar10 & 0xe0;
joined_r0x00bac254:
          if (uVar8 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar8 != 0xe0) {
            uVar8 = uVar10 & 0xc0;
                    /* try { // try from 00bac260 to 00cac26b has its CatchHandler @ 00bac32c */
            goto joined_r0x00bac254;
          }
          if ((uVar10 & 0xe0) != 0xa0) {
            return (bool)2;
          }
        }
        if ((long)param_2 - (long)pbVar6 == 2) {
          return true;
        }
                    /* try { // try from 00bac280 to 00cac28b has its CatchHandler @ 00bac2f4 */
                    /* catch() { ... } // from try @ 00bac1c0 with catch @ 00bac28c
                       try { // try from 00bac28c to 00cac357 has its CatchHandler @ 00babe04 */
        if (((pbVar6[2] & 0xc0) != 0x80) ||
           (uVar8 = (uVar10 & 0x3f) << 6, uVar10 = pbVar6[2] & 0x3f,
           param_7 < ((uint)bVar2 << 0xc & 0xffc0 | uVar8 | uVar10))) {
          return (bool)2;
        }
        *puVar9 = (ushort)((uint)bVar2 << 0xc) | (ushort)uVar8 | (ushort)uVar10;
        pbVar6 = pbVar6 + 3;
      }
      else {
        if (0xf4 < uVar8) {
          return (bool)2;
        }
        lVar7 = (long)param_2 - (long)pbVar6;
        if (lVar7 < 2) {
          return true;
        }
        bVar3 = pbVar6[1];
        uVar10 = (uint)bVar3;
        if (bVar2 == 0xf4) {
          uVar1 = uVar10 & 0xf0;
joined_r0x00bac2ac:
          if (uVar1 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar8 != 0xf0) {
            uVar1 = uVar10 & 0xc0;
            goto joined_r0x00bac2ac;
          }
          if (0x2f < uVar10 - 0x90) {
            return (bool)2;
          }
        }
                    /* catch() { ... } // from try @ 00bac1ac with catch @ 00bac2c0 */
        if (lVar7 == 2) {
          return true;
        }
        bVar2 = pbVar6[2];
        if ((bVar2 & 0xc0) != 0x80) {
          return (bool)2;
        }
        if (lVar7 == 3) {
          return true;
        }
                    /* catch() { ... } // from try @ 00bac19c with catch @ 00bac2e0 */
        bVar4 = pbVar6[3];
        if ((bVar4 & 0xc0) != 0x80) {
          return (bool)2;
        }
                    /* catch() { ... } // from try @ 00bac280 with catch @ 00bac2f4 */
        if ((long)param_5 - (long)puVar9 < 4) {
          return true;
        }
                    /* catch() { ... } // from try @ 00babfd4 with catch @ 00bac304 */
        if (param_7 < (((ulong)uVar8 & 7) << 0x12 | ((ulong)bVar3 & 0x3f) << 0xc |
                       ((ulong)bVar2 & 0x3f) << 6 | (ulong)bVar4 & 0x3f)) {
          return (bool)2;
        }
                    /* catch() { ... } // from try @ 00bac260 with catch @ 00bac32c */
        puVar9[1] = bVar4 & 0x3f | (bVar2 & 0xf) << 6 | 0xdc00;
        *param_6 = (long)(puVar9 + 1);
        lVar7 = *param_3;
        *puVar9 = ((ushort)((uVar10 & 0xf) << 2) |
                   (ushort)(((uVar8 & 7) << 2 | bVar3 >> 4 & 3) << 6) | bVar2 >> 4 & 3) + 0x3fc0 |
                  0xd800;
        pbVar6 = (byte *)(lVar7 + 4);
      }
    }
    else {
      *puVar9 = (ushort)bVar2;
      pbVar6 = pbVar6 + 1;
    }
    *param_3 = (long)pbVar6;
    lVar7 = *param_6;
    *param_6 = lVar7 + 2;
    pbVar6 = (byte *)*param_3;
    puVar5 = (ushort *)(lVar7 + 2);
  } while (pbVar6 < param_2);
  return param_5 <= puVar9;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bac0ec"></a> `00bac0ec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bac0f0"></a> `00bac0f0` | `40 00 00 f9` | str x0,[x2] | `FALL_THROUGH`
<a id="insn-00bac0f4"></a> `00bac0f4` | `a3 00 00 f9` | str x3,[x5] | `FALL_THROUGH`
<a id="insn-00bac0f8"></a> `00bac0f8` | `4c 00 40 f9` | ldr x12,[x2] | `FALL_THROUGH`
<a id="insn-00bac0fc"></a> `00bac0fc` | `e7 01 10 36` | tbz w7,#0x2,0x00bac138 | `CONDITIONAL_JUMP`
<a id="insn-00bac100"></a> `00bac100` | `28 00 0c cb` | sub x8,x1,x12 | `FALL_THROUGH`
<a id="insn-00bac104"></a> `00bac104` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bac108"></a> `00bac108` | `8b 01 00 54` | b.lt 0x00bac138 | `CONDITIONAL_JUMP`
<a id="insn-00bac10c"></a> `00bac10c` | `88 01 40 39` | ldrb w8,[x12] | `FALL_THROUGH`
<a id="insn-00bac110"></a> `00bac110` | `1f bd 03 71` | cmp w8,#0xef | `FALL_THROUGH`
<a id="insn-00bac114"></a> `00bac114` | `21 01 00 54` | b.ne 0x00bac138 | `CONDITIONAL_JUMP`
<a id="insn-00bac118"></a> `00bac118` | `88 05 40 39` | ldrb w8,[x12, #0x1] | `FALL_THROUGH`
<a id="insn-00bac11c"></a> `00bac11c` | `1f ed 02 71` | cmp w8,#0xbb | `FALL_THROUGH`
<a id="insn-00bac120"></a> `00bac120` | `c1 00 00 54` | b.ne 0x00bac138 | `CONDITIONAL_JUMP`
<a id="insn-00bac124"></a> `00bac124` | `88 09 40 39` | ldrb w8,[x12, #0x2] | `FALL_THROUGH`
<a id="insn-00bac128"></a> `00bac128` | `1f fd 02 71` | cmp w8,#0xbf | `FALL_THROUGH`
<a id="insn-00bac12c"></a> `00bac12c` | `61 00 00 54` | b.ne 0x00bac138 | `CONDITIONAL_JUMP`
<a id="insn-00bac130"></a> `00bac130` | `8c 0d 00 91` | add x12,x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bac134"></a> `00bac134` | `4c 00 00 f9` | str x12,[x2] | `FALL_THROUGH`
<a id="insn-00bac138"></a> `00bac138` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00bac13c"></a> `00bac13c` | `02 11 00 54` | b.cs 0x00bac35c | `CONDITIONAL_JUMP`
<a id="insn-00bac140"></a> `00bac140` | `ad 00 40 f9` | ldr x13,[x5] | `FALL_THROUGH`
<a id="insn-00bac144"></a> `00bac144` | `08 f8 87 52` | mov w8,#0x3fc0 | `FALL_THROUGH`
<a id="insn-00bac148"></a> `00bac148` | `09 00 9b 52` | mov w9,#0xd800 | `FALL_THROUGH`
<a id="insn-00bac14c"></a> `00bac14c` | `0a 80 9b 52` | mov w10,#0xdc00 | `FALL_THROUGH`
<a id="insn-00bac150"></a> `00bac150` | `0a 00 00 14` | b 0x00bac178 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac154"></a> `00bac154` | `6d 01 00 79` | strh w13,[x11] | `FALL_THROUGH`
<a id="insn-00bac158"></a> `00bac158` | `8c 05 00 91` | add x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bac15c"></a> `00bac15c` | `4c 00 00 f9` | str x12,[x2] | `FALL_THROUGH`
<a id="insn-00bac160"></a> `00bac160` | `ac 00 40 f9` | ldr x12,[x5] | `FALL_THROUGH`
<a id="insn-00bac164"></a> `00bac164` | `8d 09 00 91` | add x13,x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bac168"></a> `00bac168` | `ad 00 00 f9` | str x13,[x5] | `FALL_THROUGH`
<a id="insn-00bac16c"></a> `00bac16c` | `4c 00 40 f9` | ldr x12,[x2] | `FALL_THROUGH`
<a id="insn-00bac170"></a> `00bac170` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00bac174"></a> `00bac174` | `c2 0f 00 54` | b.cs 0x00bac36c | `CONDITIONAL_JUMP`
<a id="insn-00bac178"></a> `00bac178` | `eb 03 0d aa` | mov x11,x13 | `FALL_THROUGH`
<a id="insn-00bac17c"></a> `00bac17c` | `bf 01 04 eb` | cmp x13,x4 | `FALL_THROUGH`
<a id="insn-00bac180"></a> `00bac180` | `62 0f 00 54` | b.cs 0x00bac36c | `CONDITIONAL_JUMP`
<a id="insn-00bac184"></a> `00bac184` | `8d 01 40 39` | ldrb w13,[x12] | `FALL_THROUGH`
<a id="insn-00bac188"></a> `00bac188` | `bf 01 06 eb` | cmp x13,x6 | `FALL_THROUGH`
<a id="insn-00bac18c"></a> `00bac18c` | `c8 0e 00 54` | b.hi 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac190"></a> `00bac190` | `2d fe 3f 36` | tbz w13,#0x7,0x00bac154 | `CONDITIONAL_JUMP`
<a id="insn-00bac194"></a> `00bac194` | `bf 09 03 71` | cmp w13,#0xc2 | `FALL_THROUGH`
<a id="insn-00bac198"></a> `00bac198` | `63 0e 00 54` | b.cc 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac19c"></a> `00bac19c` | `bf 7d 03 71` | cmp w13,#0xdf | `FALL_THROUGH`
<a id="insn-00bac1a0"></a> `00bac1a0` | `e8 01 00 54` | b.hi 0x00bac1dc | `CONDITIONAL_JUMP`
<a id="insn-00bac1a4"></a> `00bac1a4` | `2e 00 0c cb` | sub x14,x1,x12 | `FALL_THROUGH`
<a id="insn-00bac1a8"></a> `00bac1a8` | `df 09 00 f1` | cmp x14,#0x2 | `FALL_THROUGH`
<a id="insn-00bac1ac"></a> `00bac1ac` | `6b 0e 00 54` | b.lt 0x00bac378 | `CONDITIONAL_JUMP`
<a id="insn-00bac1b0"></a> `00bac1b0` | `8e 05 40 39` | ldrb w14,[x12, #0x1] | `FALL_THROUGH`
<a id="insn-00bac1b4"></a> `00bac1b4` | `cf 05 1a 12` | and w15,w14,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac1b8"></a> `00bac1b8` | `ff 01 02 71` | cmp w15,#0x80 | `FALL_THROUGH`
<a id="insn-00bac1bc"></a> `00bac1bc` | `41 0d 00 54` | b.ne 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac1c0"></a> `00bac1c0` | `ce 15 00 12` | and w14,w14,#0x3f | `FALL_THROUGH`
<a id="insn-00bac1c4"></a> `00bac1c4` | `ae 11 1a 33` | bfm w14,w13,#0x1a,#0x4 | `FALL_THROUGH`
<a id="insn-00bac1c8"></a> `00bac1c8` | `df 01 06 eb` | cmp x14,x6 | `FALL_THROUGH`
<a id="insn-00bac1cc"></a> `00bac1cc` | `c8 0c 00 54` | b.hi 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac1d0"></a> `00bac1d0` | `6e 01 00 79` | strh w14,[x11] | `FALL_THROUGH`
<a id="insn-00bac1d4"></a> `00bac1d4` | `8c 09 00 91` | add x12,x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bac1d8"></a> `00bac1d8` | `e1 ff ff 17` | b 0x00bac15c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac1dc"></a> `00bac1dc` | `bf bd 03 71` | cmp w13,#0xef | `FALL_THROUGH`
<a id="insn-00bac1e0"></a> `00bac1e0` | `a8 01 00 54` | b.hi 0x00bac214 | `CONDITIONAL_JUMP`
<a id="insn-00bac1e4"></a> `00bac1e4` | `2f 00 0c cb` | sub x15,x1,x12 | `FALL_THROUGH`
<a id="insn-00bac1e8"></a> `00bac1e8` | `ff 09 00 f1` | cmp x15,#0x2 | `FALL_THROUGH`
<a id="insn-00bac1ec"></a> `00bac1ec` | `6b 0c 00 54` | b.lt 0x00bac378 | `CONDITIONAL_JUMP`
<a id="insn-00bac1f0"></a> `00bac1f0` | `8e 05 40 39` | ldrb w14,[x12, #0x1] | `FALL_THROUGH`
<a id="insn-00bac1f4"></a> `00bac1f4` | `bf b5 03 71` | cmp w13,#0xed | `FALL_THROUGH`
<a id="insn-00bac1f8"></a> `00bac1f8` | `a0 02 00 54` | b.eq 0x00bac24c | `CONDITIONAL_JUMP`
<a id="insn-00bac1fc"></a> `00bac1fc` | `bf 81 03 71` | cmp w13,#0xe0 | `FALL_THROUGH`
<a id="insn-00bac200"></a> `00bac200` | `e1 02 00 54` | b.ne 0x00bac25c | `CONDITIONAL_JUMP`
<a id="insn-00bac204"></a> `00bac204` | `d0 09 1b 12` | and w16,w14,#0xe0 | `FALL_THROUGH`
<a id="insn-00bac208"></a> `00bac208` | `1f 82 02 71` | cmp w16,#0xa0 | `FALL_THROUGH`
<a id="insn-00bac20c"></a> `00bac20c` | `e0 02 00 54` | b.eq 0x00bac268 | `CONDITIONAL_JUMP`
<a id="insn-00bac210"></a> `00bac210` | `55 00 00 14` | b 0x00bac364 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac214"></a> `00bac214` | `bf d1 03 71` | cmp w13,#0xf4 | `FALL_THROUGH`
<a id="insn-00bac218"></a> `00bac218` | `68 0a 00 54` | b.hi 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac21c"></a> `00bac21c` | `30 00 0c cb` | sub x16,x1,x12 | `FALL_THROUGH`
<a id="insn-00bac220"></a> `00bac220` | `1f 0a 00 f1` | cmp x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bac224"></a> `00bac224` | `ab 0a 00 54` | b.lt 0x00bac378 | `CONDITIONAL_JUMP`
<a id="insn-00bac228"></a> `00bac228` | `8e 05 40 39` | ldrb w14,[x12, #0x1] | `FALL_THROUGH`
<a id="insn-00bac22c"></a> `00bac22c` | `bf d1 03 71` | cmp w13,#0xf4 | `FALL_THROUGH`
<a id="insn-00bac230"></a> `00bac230` | `a0 03 00 54` | b.eq 0x00bac2a4 | `CONDITIONAL_JUMP`
<a id="insn-00bac234"></a> `00bac234` | `bf c1 03 71` | cmp w13,#0xf0 | `FALL_THROUGH`
<a id="insn-00bac238"></a> `00bac238` | `e1 03 00 54` | b.ne 0x00bac2b4 | `CONDITIONAL_JUMP`
<a id="insn-00bac23c"></a> `00bac23c` | `cf 41 02 51` | sub w15,w14,#0x90 | `FALL_THROUGH`
<a id="insn-00bac240"></a> `00bac240` | `ff c1 00 71` | cmp w15,#0x30 | `FALL_THROUGH`
<a id="insn-00bac244"></a> `00bac244` | `e3 03 00 54` | b.cc 0x00bac2c0 | `CONDITIONAL_JUMP`
<a id="insn-00bac248"></a> `00bac248` | `47 00 00 14` | b 0x00bac364 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac24c"></a> `00bac24c` | `d0 09 1b 12` | and w16,w14,#0xe0 | `FALL_THROUGH`
<a id="insn-00bac250"></a> `00bac250` | `1f 02 02 71` | cmp w16,#0x80 | `FALL_THROUGH`
<a id="insn-00bac254"></a> `00bac254` | `a0 00 00 54` | b.eq 0x00bac268 | `CONDITIONAL_JUMP`
<a id="insn-00bac258"></a> `00bac258` | `43 00 00 14` | b 0x00bac364 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac25c"></a> `00bac25c` | `d0 05 1a 12` | and w16,w14,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac260"></a> `00bac260` | `1f 02 02 71` | cmp w16,#0x80 | `FALL_THROUGH`
<a id="insn-00bac264"></a> `00bac264` | `01 08 00 54` | b.ne 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac268"></a> `00bac268` | `ff 09 00 f1` | cmp x15,#0x2 | `FALL_THROUGH`
<a id="insn-00bac26c"></a> `00bac26c` | `60 08 00 54` | b.eq 0x00bac378 | `CONDITIONAL_JUMP`
<a id="insn-00bac270"></a> `00bac270` | `8f 09 40 39` | ldrb w15,[x12, #0x2] | `FALL_THROUGH`
<a id="insn-00bac274"></a> `00bac274` | `f0 05 1a 12` | and w16,w15,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac278"></a> `00bac278` | `1f 02 02 71` | cmp w16,#0x80 | `FALL_THROUGH`
<a id="insn-00bac27c"></a> `00bac27c` | `41 07 00 54` | b.ne 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac280"></a> `00bac280` | `ad 4d 14 53` | lsl w13,w13,#0xc | `FALL_THROUGH`
<a id="insn-00bac284"></a> `00bac284` | `cd 15 1a 33` | bfm w13,w14,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bac288"></a> `00bac288` | `ed 15 00 33` | bfxil w13,w15,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bac28c"></a> `00bac28c` | `ae 3d 00 12` | and w14,w13,#0xffff | `FALL_THROUGH`
<a id="insn-00bac290"></a> `00bac290` | `df 01 06 eb` | cmp x14,x6 | `FALL_THROUGH`
<a id="insn-00bac294"></a> `00bac294` | `88 06 00 54` | b.hi 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac298"></a> `00bac298` | `6d 01 00 79` | strh w13,[x11] | `FALL_THROUGH`
<a id="insn-00bac29c"></a> `00bac29c` | `8c 0d 00 91` | add x12,x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bac2a0"></a> `00bac2a0` | `af ff ff 17` | b 0x00bac15c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac2a4"></a> `00bac2a4` | `cf 0d 1c 12` | and w15,w14,#0xf0 | `FALL_THROUGH`
<a id="insn-00bac2a8"></a> `00bac2a8` | `ff 01 02 71` | cmp w15,#0x80 | `FALL_THROUGH`
<a id="insn-00bac2ac"></a> `00bac2ac` | `a0 00 00 54` | b.eq 0x00bac2c0 | `CONDITIONAL_JUMP`
<a id="insn-00bac2b0"></a> `00bac2b0` | `2d 00 00 14` | b 0x00bac364 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac2b4"></a> `00bac2b4` | `cf 05 1a 12` | and w15,w14,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac2b8"></a> `00bac2b8` | `ff 01 02 71` | cmp w15,#0x80 | `FALL_THROUGH`
<a id="insn-00bac2bc"></a> `00bac2bc` | `41 05 00 54` | b.ne 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac2c0"></a> `00bac2c0` | `1f 0a 00 f1` | cmp x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bac2c4"></a> `00bac2c4` | `a0 05 00 54` | b.eq 0x00bac378 | `CONDITIONAL_JUMP`
<a id="insn-00bac2c8"></a> `00bac2c8` | `8f 09 40 39` | ldrb w15,[x12, #0x2] | `FALL_THROUGH`
<a id="insn-00bac2cc"></a> `00bac2cc` | `f1 05 1a 12` | and w17,w15,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac2d0"></a> `00bac2d0` | `3f 02 02 71` | cmp w17,#0x80 | `FALL_THROUGH`
<a id="insn-00bac2d4"></a> `00bac2d4` | `81 04 00 54` | b.ne 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac2d8"></a> `00bac2d8` | `1f 0e 00 f1` | cmp x16,#0x3 | `FALL_THROUGH`
<a id="insn-00bac2dc"></a> `00bac2dc` | `e0 04 00 54` | b.eq 0x00bac378 | `CONDITIONAL_JUMP`
<a id="insn-00bac2e0"></a> `00bac2e0` | `8c 0d 40 39` | ldrb w12,[x12, #0x3] | `FALL_THROUGH`
<a id="insn-00bac2e4"></a> `00bac2e4` | `90 05 1a 12` | and w16,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac2e8"></a> `00bac2e8` | `1f 02 02 71` | cmp w16,#0x80 | `FALL_THROUGH`
<a id="insn-00bac2ec"></a> `00bac2ec` | `c1 03 00 54` | b.ne 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac2f0"></a> `00bac2f0` | `90 00 0b cb` | sub x16,x4,x11 | `FALL_THROUGH`
<a id="insn-00bac2f4"></a> `00bac2f4` | `1f 12 00 f1` | cmp x16,#0x4 | `FALL_THROUGH`
<a id="insn-00bac2f8"></a> `00bac2f8` | `0b 04 00 54` | b.lt 0x00bac378 | `CONDITIONAL_JUMP`
<a id="insn-00bac2fc"></a> `00bac2fc` | `f0 03 0d 2a` | mov w16,w13 | `FALL_THROUGH`
<a id="insn-00bac300"></a> `00bac300` | `10 0a 6e d3` | ubfiz x16,x16,#0x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bac304"></a> `00bac304` | `d0 15 74 b3` | bfm x16,x14,#0x34,#0x5 | `FALL_THROUGH`
<a id="insn-00bac308"></a> `00bac308` | `f0 15 7a b3` | bfm x16,x15,#0x3a,#0x5 | `FALL_THROUGH`
<a id="insn-00bac30c"></a> `00bac30c` | `90 15 40 b3` | bfxil x16,x12,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bac310"></a> `00bac310` | `1f 02 06 eb` | cmp x16,x6 | `FALL_THROUGH`
<a id="insn-00bac314"></a> `00bac314` | `88 02 00 54` | b.hi 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac318"></a> `00bac318` | `ad 09 1e 53` | ubfiz w13,w13,#0x2,#0x3 | `FALL_THROUGH`
<a id="insn-00bac31c"></a> `00bac31c` | `8c 15 40 92` | and x12,x12,#0x3f | `FALL_THROUGH`
<a id="insn-00bac320"></a> `00bac320` | `ec 0d 1a 33` | bfm w12,w15,#0x1a,#0x3 | `FALL_THROUGH`
<a id="insn-00bac324"></a> `00bac324` | `cd 15 04 33` | bfxil w13,w14,#0x4,#0x2 | `FALL_THROUGH`
<a id="insn-00bac328"></a> `00bac328` | `ce 0d 1e 53` | ubfiz w14,w14,#0x2,#0x4 | `FALL_THROUGH`
<a id="insn-00bac32c"></a> `00bac32c` | `8c 01 0a 2a` | orr w12,w12,w10 | `FALL_THROUGH`
<a id="insn-00bac330"></a> `00bac330` | `cd 19 0d 2a` | orr w13,w14,w13, LSL #0x6 | `FALL_THROUGH`
<a id="insn-00bac334"></a> `00bac334` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bac338"></a> `00bac338` | `cc 2d 00 78` | strh w12,[x14, #0x2]! | `FALL_THROUGH`
<a id="insn-00bac33c"></a> `00bac33c` | `ed 15 04 33` | bfxil w13,w15,#0x4,#0x2 | `FALL_THROUGH`
<a id="insn-00bac340"></a> `00bac340` | `ae 00 00 f9` | str x14,[x5] | `FALL_THROUGH`
<a id="insn-00bac344"></a> `00bac344` | `ac 01 08 0b` | add w12,w13,w8 | `FALL_THROUGH`
<a id="insn-00bac348"></a> `00bac348` | `4d 00 40 f9` | ldr x13,[x2] | `FALL_THROUGH`
<a id="insn-00bac34c"></a> `00bac34c` | `8c 01 09 2a` | orr w12,w12,w9 | `FALL_THROUGH`
<a id="insn-00bac350"></a> `00bac350` | `6c 01 00 79` | strh w12,[x11] | `FALL_THROUGH`
<a id="insn-00bac354"></a> `00bac354` | `ac 11 00 91` | add x12,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bac358"></a> `00bac358` | `81 ff ff 17` | b 0x00bac15c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac35c"></a> `00bac35c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bac360"></a> `00bac360` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bac364"></a> `00bac364` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bac368"></a> `00bac368` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bac36c"></a> `00bac36c` | `7f 01 04 eb` | cmp x11,x4 | `FALL_THROUGH`
<a id="insn-00bac370"></a> `00bac370` | `e0 37 9f 1a` | cset w0,cs | `FALL_THROUGH`
<a id="insn-00bac374"></a> `00bac374` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bac378"></a> `00bac378` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bac37c"></a> `00bac37c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bac0ec`](#insn-00bac0ec) 範囲 `[['00bac0ec', '00bac0ff']]`
  - `CONDITIONAL_JUMP` [`00bac0fc`](#insn-00bac0fc) → [`00bac138`](#insn-00bac138)
  - `FALL_THROUGH` [`00bac0fc`](#insn-00bac0fc) → [`00bac100`](#insn-00bac100)
- ブロック [`00bac100`](#insn-00bac100) 範囲 `[['00bac100', '00bac10b']]`
  - `CONDITIONAL_JUMP` [`00bac108`](#insn-00bac108) → [`00bac138`](#insn-00bac138)
  - `FALL_THROUGH` [`00bac108`](#insn-00bac108) → [`00bac10c`](#insn-00bac10c)
- ブロック [`00bac10c`](#insn-00bac10c) 範囲 `[['00bac10c', '00bac117']]`
  - `CONDITIONAL_JUMP` [`00bac114`](#insn-00bac114) → [`00bac138`](#insn-00bac138)
  - `FALL_THROUGH` [`00bac114`](#insn-00bac114) → [`00bac118`](#insn-00bac118)
- ブロック [`00bac118`](#insn-00bac118) 範囲 `[['00bac118', '00bac123']]`
  - `CONDITIONAL_JUMP` [`00bac120`](#insn-00bac120) → [`00bac138`](#insn-00bac138)
  - `FALL_THROUGH` [`00bac120`](#insn-00bac120) → [`00bac124`](#insn-00bac124)
- ブロック [`00bac124`](#insn-00bac124) 範囲 `[['00bac124', '00bac12f']]`
  - `CONDITIONAL_JUMP` [`00bac12c`](#insn-00bac12c) → [`00bac138`](#insn-00bac138)
  - `FALL_THROUGH` [`00bac12c`](#insn-00bac12c) → [`00bac130`](#insn-00bac130)
- ブロック [`00bac130`](#insn-00bac130) 範囲 `[['00bac130', '00bac137']]`
  - `FALL_THROUGH` [`00bac134`](#insn-00bac134) → [`00bac138`](#insn-00bac138)
- ブロック [`00bac138`](#insn-00bac138) 範囲 `[['00bac138', '00bac13f']]`
  - `CONDITIONAL_JUMP` [`00bac13c`](#insn-00bac13c) → [`00bac35c`](#insn-00bac35c)
  - `FALL_THROUGH` [`00bac13c`](#insn-00bac13c) → [`00bac140`](#insn-00bac140)
- ブロック [`00bac140`](#insn-00bac140) 範囲 `[['00bac140', '00bac153']]`
  - `UNCONDITIONAL_JUMP` [`00bac150`](#insn-00bac150) → [`00bac178`](#insn-00bac178)
- ブロック [`00bac154`](#insn-00bac154) 範囲 `[['00bac154', '00bac15b']]`
  - `FALL_THROUGH` [`00bac158`](#insn-00bac158) → [`00bac15c`](#insn-00bac15c)
- ブロック [`00bac15c`](#insn-00bac15c) 範囲 `[['00bac15c', '00bac177']]`
  - `CONDITIONAL_JUMP` [`00bac174`](#insn-00bac174) → [`00bac36c`](#insn-00bac36c)
  - `FALL_THROUGH` [`00bac174`](#insn-00bac174) → [`00bac178`](#insn-00bac178)
- ブロック [`00bac178`](#insn-00bac178) 範囲 `[['00bac178', '00bac183']]`
  - `CONDITIONAL_JUMP` [`00bac180`](#insn-00bac180) → [`00bac36c`](#insn-00bac36c)
  - `FALL_THROUGH` [`00bac180`](#insn-00bac180) → [`00bac184`](#insn-00bac184)
- ブロック [`00bac184`](#insn-00bac184) 範囲 `[['00bac184', '00bac18f']]`
  - `CONDITIONAL_JUMP` [`00bac18c`](#insn-00bac18c) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac18c`](#insn-00bac18c) → [`00bac190`](#insn-00bac190)
- ブロック [`00bac190`](#insn-00bac190) 範囲 `[['00bac190', '00bac193']]`
  - `CONDITIONAL_JUMP` [`00bac190`](#insn-00bac190) → [`00bac154`](#insn-00bac154)
  - `FALL_THROUGH` [`00bac190`](#insn-00bac190) → [`00bac194`](#insn-00bac194)
- ブロック [`00bac194`](#insn-00bac194) 範囲 `[['00bac194', '00bac19b']]`
  - `CONDITIONAL_JUMP` [`00bac198`](#insn-00bac198) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac198`](#insn-00bac198) → [`00bac19c`](#insn-00bac19c)
- ブロック [`00bac19c`](#insn-00bac19c) 範囲 `[['00bac19c', '00bac1a3']]`
  - `CONDITIONAL_JUMP` [`00bac1a0`](#insn-00bac1a0) → [`00bac1dc`](#insn-00bac1dc)
  - `FALL_THROUGH` [`00bac1a0`](#insn-00bac1a0) → [`00bac1a4`](#insn-00bac1a4)
- ブロック [`00bac1a4`](#insn-00bac1a4) 範囲 `[['00bac1a4', '00bac1ab']]`
  - `FALL_THROUGH` [`00bac1a8`](#insn-00bac1a8) → [`00bac1ac`](#insn-00bac1ac)
- ブロック [`00bac1ac`](#insn-00bac1ac) 範囲 `[['00bac1ac', '00bac1af']]`
  - `CONDITIONAL_JUMP` [`00bac1ac`](#insn-00bac1ac) → [`00bac378`](#insn-00bac378)
  - `FALL_THROUGH` [`00bac1ac`](#insn-00bac1ac) → [`00bac1b0`](#insn-00bac1b0)
- ブロック [`00bac1b0`](#insn-00bac1b0) 範囲 `[['00bac1b0', '00bac1bf']]`
  - `CONDITIONAL_JUMP` [`00bac1bc`](#insn-00bac1bc) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac1bc`](#insn-00bac1bc) → [`00bac1c0`](#insn-00bac1c0)
- ブロック [`00bac1c0`](#insn-00bac1c0) 範囲 `[['00bac1c0', '00bac1cf']]`
  - `CONDITIONAL_JUMP` [`00bac1cc`](#insn-00bac1cc) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac1cc`](#insn-00bac1cc) → [`00bac1d0`](#insn-00bac1d0)
- ブロック [`00bac1d0`](#insn-00bac1d0) 範囲 `[['00bac1d0', '00bac1db']]`
  - `UNCONDITIONAL_JUMP` [`00bac1d8`](#insn-00bac1d8) → [`00bac15c`](#insn-00bac15c)
- ブロック [`00bac1dc`](#insn-00bac1dc) 範囲 `[['00bac1dc', '00bac1e3']]`
  - `CONDITIONAL_JUMP` [`00bac1e0`](#insn-00bac1e0) → [`00bac214`](#insn-00bac214)
  - `FALL_THROUGH` [`00bac1e0`](#insn-00bac1e0) → [`00bac1e4`](#insn-00bac1e4)
- ブロック [`00bac1e4`](#insn-00bac1e4) 範囲 `[['00bac1e4', '00bac1ef']]`
  - `CONDITIONAL_JUMP` [`00bac1ec`](#insn-00bac1ec) → [`00bac378`](#insn-00bac378)
  - `FALL_THROUGH` [`00bac1ec`](#insn-00bac1ec) → [`00bac1f0`](#insn-00bac1f0)
- ブロック [`00bac1f0`](#insn-00bac1f0) 範囲 `[['00bac1f0', '00bac1fb']]`
  - `CONDITIONAL_JUMP` [`00bac1f8`](#insn-00bac1f8) → [`00bac24c`](#insn-00bac24c)
  - `FALL_THROUGH` [`00bac1f8`](#insn-00bac1f8) → [`00bac1fc`](#insn-00bac1fc)
- ブロック [`00bac1fc`](#insn-00bac1fc) 範囲 `[['00bac1fc', '00bac203']]`
  - `CONDITIONAL_JUMP` [`00bac200`](#insn-00bac200) → [`00bac25c`](#insn-00bac25c)
  - `FALL_THROUGH` [`00bac200`](#insn-00bac200) → [`00bac204`](#insn-00bac204)
- ブロック [`00bac204`](#insn-00bac204) 範囲 `[['00bac204', '00bac20f']]`
  - `CONDITIONAL_JUMP` [`00bac20c`](#insn-00bac20c) → [`00bac268`](#insn-00bac268)
  - `FALL_THROUGH` [`00bac20c`](#insn-00bac20c) → [`00bac210`](#insn-00bac210)
- ブロック [`00bac210`](#insn-00bac210) 範囲 `[['00bac210', '00bac213']]`
  - `UNCONDITIONAL_JUMP` [`00bac210`](#insn-00bac210) → [`00bac364`](#insn-00bac364)
- ブロック [`00bac214`](#insn-00bac214) 範囲 `[['00bac214', '00bac21b']]`
  - `CONDITIONAL_JUMP` [`00bac218`](#insn-00bac218) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac218`](#insn-00bac218) → [`00bac21c`](#insn-00bac21c)
- ブロック [`00bac21c`](#insn-00bac21c) 範囲 `[['00bac21c', '00bac227']]`
  - `CONDITIONAL_JUMP` [`00bac224`](#insn-00bac224) → [`00bac378`](#insn-00bac378)
  - `FALL_THROUGH` [`00bac224`](#insn-00bac224) → [`00bac228`](#insn-00bac228)
- ブロック [`00bac228`](#insn-00bac228) 範囲 `[['00bac228', '00bac233']]`
  - `CONDITIONAL_JUMP` [`00bac230`](#insn-00bac230) → [`00bac2a4`](#insn-00bac2a4)
  - `FALL_THROUGH` [`00bac230`](#insn-00bac230) → [`00bac234`](#insn-00bac234)
- ブロック [`00bac234`](#insn-00bac234) 範囲 `[['00bac234', '00bac23b']]`
  - `CONDITIONAL_JUMP` [`00bac238`](#insn-00bac238) → [`00bac2b4`](#insn-00bac2b4)
  - `FALL_THROUGH` [`00bac238`](#insn-00bac238) → [`00bac23c`](#insn-00bac23c)
- ブロック [`00bac23c`](#insn-00bac23c) 範囲 `[['00bac23c', '00bac247']]`
  - `CONDITIONAL_JUMP` [`00bac244`](#insn-00bac244) → [`00bac2c0`](#insn-00bac2c0)
  - `FALL_THROUGH` [`00bac244`](#insn-00bac244) → [`00bac248`](#insn-00bac248)
- ブロック [`00bac248`](#insn-00bac248) 範囲 `[['00bac248', '00bac24b']]`
  - `UNCONDITIONAL_JUMP` [`00bac248`](#insn-00bac248) → [`00bac364`](#insn-00bac364)
- ブロック [`00bac24c`](#insn-00bac24c) 範囲 `[['00bac24c', '00bac257']]`
  - `CONDITIONAL_JUMP` [`00bac254`](#insn-00bac254) → [`00bac268`](#insn-00bac268)
  - `FALL_THROUGH` [`00bac254`](#insn-00bac254) → [`00bac258`](#insn-00bac258)
- ブロック [`00bac258`](#insn-00bac258) 範囲 `[['00bac258', '00bac25b']]`
  - `UNCONDITIONAL_JUMP` [`00bac258`](#insn-00bac258) → [`00bac364`](#insn-00bac364)
- ブロック [`00bac25c`](#insn-00bac25c) 範囲 `[['00bac25c', '00bac25f']]`
  - `FALL_THROUGH` [`00bac25c`](#insn-00bac25c) → [`00bac260`](#insn-00bac260)
- ブロック [`00bac260`](#insn-00bac260) 範囲 `[['00bac260', '00bac267']]`
  - `CONDITIONAL_JUMP` [`00bac264`](#insn-00bac264) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac264`](#insn-00bac264) → [`00bac268`](#insn-00bac268)
- ブロック [`00bac268`](#insn-00bac268) 範囲 `[['00bac268', '00bac26f']]`
  - `CONDITIONAL_JUMP` [`00bac26c`](#insn-00bac26c) → [`00bac378`](#insn-00bac378)
  - `FALL_THROUGH` [`00bac26c`](#insn-00bac26c) → [`00bac270`](#insn-00bac270)
- ブロック [`00bac270`](#insn-00bac270) 範囲 `[['00bac270', '00bac27f']]`
  - `CONDITIONAL_JUMP` [`00bac27c`](#insn-00bac27c) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac27c`](#insn-00bac27c) → [`00bac280`](#insn-00bac280)
- ブロック [`00bac280`](#insn-00bac280) 範囲 `[['00bac280', '00bac28b']]`
  - `FALL_THROUGH` [`00bac288`](#insn-00bac288) → [`00bac28c`](#insn-00bac28c)
- ブロック [`00bac28c`](#insn-00bac28c) 範囲 `[['00bac28c', '00bac297']]`
  - `CONDITIONAL_JUMP` [`00bac294`](#insn-00bac294) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac294`](#insn-00bac294) → [`00bac298`](#insn-00bac298)
- ブロック [`00bac298`](#insn-00bac298) 範囲 `[['00bac298', '00bac2a3']]`
  - `UNCONDITIONAL_JUMP` [`00bac2a0`](#insn-00bac2a0) → [`00bac15c`](#insn-00bac15c)
- ブロック [`00bac2a4`](#insn-00bac2a4) 範囲 `[['00bac2a4', '00bac2af']]`
  - `CONDITIONAL_JUMP` [`00bac2ac`](#insn-00bac2ac) → [`00bac2c0`](#insn-00bac2c0)
  - `FALL_THROUGH` [`00bac2ac`](#insn-00bac2ac) → [`00bac2b0`](#insn-00bac2b0)
- ブロック [`00bac2b0`](#insn-00bac2b0) 範囲 `[['00bac2b0', '00bac2b3']]`
  - `UNCONDITIONAL_JUMP` [`00bac2b0`](#insn-00bac2b0) → [`00bac364`](#insn-00bac364)
- ブロック [`00bac2b4`](#insn-00bac2b4) 範囲 `[['00bac2b4', '00bac2bf']]`
  - `CONDITIONAL_JUMP` [`00bac2bc`](#insn-00bac2bc) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac2bc`](#insn-00bac2bc) → [`00bac2c0`](#insn-00bac2c0)
- ブロック [`00bac2c0`](#insn-00bac2c0) 範囲 `[['00bac2c0', '00bac2c7']]`
  - `CONDITIONAL_JUMP` [`00bac2c4`](#insn-00bac2c4) → [`00bac378`](#insn-00bac378)
  - `FALL_THROUGH` [`00bac2c4`](#insn-00bac2c4) → [`00bac2c8`](#insn-00bac2c8)
- ブロック [`00bac2c8`](#insn-00bac2c8) 範囲 `[['00bac2c8', '00bac2d7']]`
  - `CONDITIONAL_JUMP` [`00bac2d4`](#insn-00bac2d4) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac2d4`](#insn-00bac2d4) → [`00bac2d8`](#insn-00bac2d8)
- ブロック [`00bac2d8`](#insn-00bac2d8) 範囲 `[['00bac2d8', '00bac2df']]`
  - `CONDITIONAL_JUMP` [`00bac2dc`](#insn-00bac2dc) → [`00bac378`](#insn-00bac378)
  - `FALL_THROUGH` [`00bac2dc`](#insn-00bac2dc) → [`00bac2e0`](#insn-00bac2e0)
- ブロック [`00bac2e0`](#insn-00bac2e0) 範囲 `[['00bac2e0', '00bac2ef']]`
  - `CONDITIONAL_JUMP` [`00bac2ec`](#insn-00bac2ec) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac2ec`](#insn-00bac2ec) → [`00bac2f0`](#insn-00bac2f0)
- ブロック [`00bac2f0`](#insn-00bac2f0) 範囲 `[['00bac2f0', '00bac2f3']]`
  - `FALL_THROUGH` [`00bac2f0`](#insn-00bac2f0) → [`00bac2f4`](#insn-00bac2f4)
- ブロック [`00bac2f4`](#insn-00bac2f4) 範囲 `[['00bac2f4', '00bac2fb']]`
  - `CONDITIONAL_JUMP` [`00bac2f8`](#insn-00bac2f8) → [`00bac378`](#insn-00bac378)
  - `FALL_THROUGH` [`00bac2f8`](#insn-00bac2f8) → [`00bac2fc`](#insn-00bac2fc)
- ブロック [`00bac2fc`](#insn-00bac2fc) 範囲 `[['00bac2fc', '00bac303']]`
  - `FALL_THROUGH` [`00bac300`](#insn-00bac300) → [`00bac304`](#insn-00bac304)
- ブロック [`00bac304`](#insn-00bac304) 範囲 `[['00bac304', '00bac317']]`
  - `CONDITIONAL_JUMP` [`00bac314`](#insn-00bac314) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac314`](#insn-00bac314) → [`00bac318`](#insn-00bac318)
- ブロック [`00bac318`](#insn-00bac318) 範囲 `[['00bac318', '00bac32b']]`
  - `FALL_THROUGH` [`00bac328`](#insn-00bac328) → [`00bac32c`](#insn-00bac32c)
- ブロック [`00bac32c`](#insn-00bac32c) 範囲 `[['00bac32c', '00bac35b']]`
  - `UNCONDITIONAL_JUMP` [`00bac358`](#insn-00bac358) → [`00bac15c`](#insn-00bac15c)
- ブロック [`00bac35c`](#insn-00bac35c) 範囲 `[['00bac35c', '00bac363']]`
- ブロック [`00bac364`](#insn-00bac364) 範囲 `[['00bac364', '00bac36b']]`
- ブロック [`00bac36c`](#insn-00bac36c) 範囲 `[['00bac36c', '00bac377']]`
- ブロック [`00bac378`](#insn-00bac378) 範囲 `[['00bac378', '00bac37f']]`

## 命令位置別の参照

- [`00bac0fc`](#insn-00bac0fc) → [`00bac138`](#insn-00bac138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac108`](#insn-00bac108) → [`00bac138`](#insn-00bac138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac114`](#insn-00bac114) → [`00bac138`](#insn-00bac138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac120`](#insn-00bac120) → [`00bac138`](#insn-00bac138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac12c`](#insn-00bac12c) → [`00bac138`](#insn-00bac138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac13c`](#insn-00bac13c) → [`00bac35c`](#insn-00bac35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac150`](#insn-00bac150) → [`00bac178`](#insn-00bac178) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac174`](#insn-00bac174) → [`00bac36c`](#insn-00bac36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac180`](#insn-00bac180) → [`00bac36c`](#insn-00bac36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac18c`](#insn-00bac18c) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac190`](#insn-00bac190) → [`00bac154`](#insn-00bac154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac198`](#insn-00bac198) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1a0`](#insn-00bac1a0) → [`00bac1dc`](#insn-00bac1dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1ac`](#insn-00bac1ac) → [`00bac378`](#insn-00bac378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1bc`](#insn-00bac1bc) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1cc`](#insn-00bac1cc) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1d8`](#insn-00bac1d8) → [`00bac15c`](#insn-00bac15c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1e0`](#insn-00bac1e0) → [`00bac214`](#insn-00bac214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1ec`](#insn-00bac1ec) → [`00bac378`](#insn-00bac378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1f8`](#insn-00bac1f8) → [`00bac24c`](#insn-00bac24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac200`](#insn-00bac200) → [`00bac25c`](#insn-00bac25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac20c`](#insn-00bac20c) → [`00bac268`](#insn-00bac268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac210`](#insn-00bac210) → [`00bac364`](#insn-00bac364) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac218`](#insn-00bac218) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac224`](#insn-00bac224) → [`00bac378`](#insn-00bac378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac230`](#insn-00bac230) → [`00bac2a4`](#insn-00bac2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac238`](#insn-00bac238) → [`00bac2b4`](#insn-00bac2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac244`](#insn-00bac244) → [`00bac2c0`](#insn-00bac2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac248`](#insn-00bac248) → [`00bac364`](#insn-00bac364) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac254`](#insn-00bac254) → [`00bac268`](#insn-00bac268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac258`](#insn-00bac258) → [`00bac364`](#insn-00bac364) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac264`](#insn-00bac264) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac26c`](#insn-00bac26c) → [`00bac378`](#insn-00bac378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac27c`](#insn-00bac27c) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac294`](#insn-00bac294) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2a0`](#insn-00bac2a0) → [`00bac15c`](#insn-00bac15c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2ac`](#insn-00bac2ac) → [`00bac2c0`](#insn-00bac2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2b0`](#insn-00bac2b0) → [`00bac364`](#insn-00bac364) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2bc`](#insn-00bac2bc) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2c4`](#insn-00bac2c4) → [`00bac378`](#insn-00bac378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2d4`](#insn-00bac2d4) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2dc`](#insn-00bac2dc) → [`00bac378`](#insn-00bac378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2ec`](#insn-00bac2ec) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2f8`](#insn-00bac2f8) → [`00bac378`](#insn-00bac378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac314`](#insn-00bac314) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac358`](#insn-00bac358) → [`00bac15c`](#insn-00bac15c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bac0fc`](#insn-00bac0fc)

~~~json
{
  "source": "00bac0fc",
  "target": "00bac138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac108`](#insn-00bac108)

~~~json
{
  "source": "00bac108",
  "target": "00bac138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac114`](#insn-00bac114)

~~~json
{
  "source": "00bac114",
  "target": "00bac138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac120`](#insn-00bac120)

~~~json
{
  "source": "00bac120",
  "target": "00bac138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac12c`](#insn-00bac12c)

~~~json
{
  "source": "00bac12c",
  "target": "00bac138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac13c`](#insn-00bac13c)

~~~json
{
  "source": "00bac13c",
  "target": "00bac35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac150`](#insn-00bac150)

~~~json
{
  "source": "00bac150",
  "target": "00bac178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac174`](#insn-00bac174)

~~~json
{
  "source": "00bac174",
  "target": "00bac36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac180`](#insn-00bac180)

~~~json
{
  "source": "00bac180",
  "target": "00bac36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac18c`](#insn-00bac18c)

~~~json
{
  "source": "00bac18c",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac190`](#insn-00bac190)

~~~json
{
  "source": "00bac190",
  "target": "00bac154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac198`](#insn-00bac198)

~~~json
{
  "source": "00bac198",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1a0`](#insn-00bac1a0)

~~~json
{
  "source": "00bac1a0",
  "target": "00bac1dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1ac`](#insn-00bac1ac)

~~~json
{
  "source": "00bac1ac",
  "target": "00bac378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1bc`](#insn-00bac1bc)

~~~json
{
  "source": "00bac1bc",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1cc`](#insn-00bac1cc)

~~~json
{
  "source": "00bac1cc",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1d8`](#insn-00bac1d8)

~~~json
{
  "source": "00bac1d8",
  "target": "00bac15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1e0`](#insn-00bac1e0)

~~~json
{
  "source": "00bac1e0",
  "target": "00bac214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1ec`](#insn-00bac1ec)

~~~json
{
  "source": "00bac1ec",
  "target": "00bac378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1f8`](#insn-00bac1f8)

~~~json
{
  "source": "00bac1f8",
  "target": "00bac24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac200`](#insn-00bac200)

~~~json
{
  "source": "00bac200",
  "target": "00bac25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac20c`](#insn-00bac20c)

~~~json
{
  "source": "00bac20c",
  "target": "00bac268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac210`](#insn-00bac210)

~~~json
{
  "source": "00bac210",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac218`](#insn-00bac218)

~~~json
{
  "source": "00bac218",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac224`](#insn-00bac224)

~~~json
{
  "source": "00bac224",
  "target": "00bac378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac230`](#insn-00bac230)

~~~json
{
  "source": "00bac230",
  "target": "00bac2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac238`](#insn-00bac238)

~~~json
{
  "source": "00bac238",
  "target": "00bac2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac244`](#insn-00bac244)

~~~json
{
  "source": "00bac244",
  "target": "00bac2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac248`](#insn-00bac248)

~~~json
{
  "source": "00bac248",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac254`](#insn-00bac254)

~~~json
{
  "source": "00bac254",
  "target": "00bac268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac258`](#insn-00bac258)

~~~json
{
  "source": "00bac258",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac264`](#insn-00bac264)

~~~json
{
  "source": "00bac264",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac26c`](#insn-00bac26c)

~~~json
{
  "source": "00bac26c",
  "target": "00bac378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac27c`](#insn-00bac27c)

~~~json
{
  "source": "00bac27c",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac294`](#insn-00bac294)

~~~json
{
  "source": "00bac294",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2a0`](#insn-00bac2a0)

~~~json
{
  "source": "00bac2a0",
  "target": "00bac15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2ac`](#insn-00bac2ac)

~~~json
{
  "source": "00bac2ac",
  "target": "00bac2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2b0`](#insn-00bac2b0)

~~~json
{
  "source": "00bac2b0",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2bc`](#insn-00bac2bc)

~~~json
{
  "source": "00bac2bc",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2c4`](#insn-00bac2c4)

~~~json
{
  "source": "00bac2c4",
  "target": "00bac378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2d4`](#insn-00bac2d4)

~~~json
{
  "source": "00bac2d4",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2dc`](#insn-00bac2dc)

~~~json
{
  "source": "00bac2dc",
  "target": "00bac378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2ec`](#insn-00bac2ec)

~~~json
{
  "source": "00bac2ec",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2f8`](#insn-00bac2f8)

~~~json
{
  "source": "00bac2f8",
  "target": "00bac378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac314`](#insn-00bac314)

~~~json
{
  "source": "00bac314",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac358`](#insn-00bac358)

~~~json
{
  "source": "00bac358",
  "target": "00bac15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
