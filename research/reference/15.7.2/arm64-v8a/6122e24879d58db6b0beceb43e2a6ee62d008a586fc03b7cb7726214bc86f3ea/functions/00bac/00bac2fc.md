# 00bac2fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bac3c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac3c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-c1f6692e30bcfc230ba91ab1cd73cceb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bac2fc",
  "name": "FUN_00bac2fc",
  "size": 512,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4cb0e4eef59756b53a5f5cb00f7c9816d7882d34f8e42476ce767f24d2d98b84",
  "source_text_sha256": "4cb0e4eef59756b53a5f5cb00f7c9816d7882d34f8e42476ce767f24d2d98b84",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bac2fc",
        "00bac4fb"
      ]
    ],
    "bytes_sha256": "c9c9dd00818d5a8a0224e36f01918194dc22835534597c5c30afc837bd9491bb",
    "instruction_count": 128,
    "instruction_bytes": 512,
    "body_bytes": 512,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bac2e0](../00bac/00bac2e0.md)
- [00bac62c](../00bac/00bac62c.md)
- [00baeb7c](../00bae/00baeb7c.md)
- [00baecc0](../00bae/00baecc0.md)
- [00baee04](../00bae/00baee04.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2551 bytes

~~~c

int FUN_00bac2fc(byte *param_1,byte *param_2,ulong param_3,ulong param_4,uint param_5)

{
  long lVar1;
  byte bVar2;
  byte bVar3;
  byte *pbVar4;
  ulong uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  byte bVar9;
  
  pbVar4 = param_1;
  if ((((2 < (long)param_2 - (long)param_1) && ((param_5 >> 2 & 1) != 0)) && (*param_1 == 0xef)) &&
     (param_1[1] == 0xbb)) {
    lVar1 = 3;
    if (param_1[2] != 0xbf) {
      lVar1 = 0;
    }
    pbVar4 = param_1 + lVar1;
  }
  if ((pbVar4 < param_2) && (param_3 != 0)) {
    uVar5 = 0;
    while( true ) {
      bVar2 = *pbVar4;
      if (param_4 < bVar2) break;
      if ((char)bVar2 < '\0') {
        if (bVar2 < 0xc2) break;
        uVar6 = (uint)bVar2;
        if (bVar2 < 0xe0) {
          if ((((long)param_2 - (long)pbVar4 < 2) || ((pbVar4[1] & 0xc0) != 0x80)) ||
             (param_4 < (pbVar4[1] & 0x3f | (uVar6 & 0x1f) << 6))) break;
          pbVar4 = pbVar4 + 2;
        }
        else if (bVar2 < 0xf0) {
          if ((long)param_2 - (long)pbVar4 < 3) break;
          uVar7 = (uint)pbVar4[1];
          if (uVar6 == 0xed) {
            uVar8 = uVar7 & 0xe0;
LAB_00bac45c:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar6 != 0xe0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bac45c;
            }
            if ((uVar7 & 0xe0) != 0xa0) break;
          }
          if (((pbVar4[2] & 0xc0) != 0x80) ||
             (param_4 < ((uVar6 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar4[2] & 0x3f))) break;
          pbVar4 = pbVar4 + 3;
        }
        else {
          if (((0xf4 < uVar6) || ((long)param_2 - (long)pbVar4 < 4)) || (param_3 - uVar5 < 2))
          break;
          bVar3 = pbVar4[1];
          if (uVar6 == 0xf4) {
            bVar9 = bVar3 & 0xf0;
LAB_00bac4a0:
            if (bVar9 != 0x80) break;
          }
          else {
            if (uVar6 != 0xf0) {
              bVar9 = bVar3 & 0xc0;
              goto LAB_00bac4a0;
            }
            if (0x2f < bVar3 - 0x90) break;
          }
          if ((((pbVar4[2] & 0xc0) != 0x80) || ((pbVar4[3] & 0xc0) != 0x80)) ||
             (param_4 < (((ulong)bVar2 & 7) << 0x12 | ((ulong)bVar3 & 0x3f) << 0xc |
                         ((ulong)pbVar4[2] & 0x3f) << 6 | (ulong)pbVar4[3] & 0x3f))) break;
          uVar5 = uVar5 + 1;
          pbVar4 = pbVar4 + 4;
        }
      }
      else {
        pbVar4 = pbVar4 + 1;
      }
      if ((param_2 <= pbVar4) || (uVar5 = uVar5 + 1, param_3 <= uVar5)) break;
    }
  }
  return (int)pbVar4 - (int)param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bac2fc"></a> `00bac2fc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bac300"></a> `00bac300` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00bac304"></a> `00bac304` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bac308"></a> `00bac308` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bac30c"></a> `00bac30c` | `0b 02 00 54` | b.lt 0x00bac34c | `CONDITIONAL_JUMP`
<a id="insn-00bac310"></a> `00bac310` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bac314"></a> `00bac314` | `c4 01 10 36` | tbz w4,#0x2,0x00bac34c | `CONDITIONAL_JUMP`
<a id="insn-00bac318"></a> `00bac318` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bac31c"></a> `00bac31c` | `1f bd 03 71` | cmp w8,#0xef | `FALL_THROUGH`
<a id="insn-00bac320"></a> `00bac320` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bac324"></a> `00bac324` | `41 01 00 54` | b.ne 0x00bac34c | `CONDITIONAL_JUMP`
<a id="insn-00bac328"></a> `00bac328` | `08 04 40 39` | ldrb w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bac32c"></a> `00bac32c` | `1f ed 02 71` | cmp w8,#0xbb | `FALL_THROUGH`
<a id="insn-00bac330"></a> `00bac330` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bac334"></a> `00bac334` | `c1 00 00 54` | b.ne 0x00bac34c | `CONDITIONAL_JUMP`
<a id="insn-00bac338"></a> `00bac338` | `08 08 40 39` | ldrb w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00bac33c"></a> `00bac33c` | `1f fd 02 71` | cmp w8,#0xbf | `FALL_THROUGH`
<a id="insn-00bac340"></a> `00bac340` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bac344"></a> `00bac344` | `08 01 9f 9a` | csel x8,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00bac348"></a> `00bac348` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bac34c"></a> `00bac34c` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bac350"></a> `00bac350` | `22 0d 00 54` | b.cs 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac354"></a> `00bac354` | `02 0d 00 b4` | cbz x2,0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac358"></a> `00bac358` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bac35c"></a> `00bac35c` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bac360"></a> `00bac360` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bac364"></a> `00bac364` | `88 0c 00 54` | b.hi 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac368"></a> `00bac368` | `aa 00 38 37` | tbnz w10,#0x7,0x00bac37c | `CONDITIONAL_JUMP`
<a id="insn-00bac36c"></a> `00bac36c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac370"></a> `00bac370` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bac374"></a> `00bac374` | `a3 0b 00 54` | b.cc 0x00bac4e8 | `CONDITIONAL_JUMP`
<a id="insn-00bac378"></a> `00bac378` | `5f 00 00 14` | b 0x00bac4f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac37c"></a> `00bac37c` | `5f 09 03 71` | cmp w10,#0xc2 | `FALL_THROUGH`
<a id="insn-00bac380"></a> `00bac380` | `a3 0b 00 54` | b.cc 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac384"></a> `00bac384` | `5f 7d 03 71` | cmp w10,#0xdf | `FALL_THROUGH`
<a id="insn-00bac388"></a> `00bac388` | `08 02 00 54` | b.hi 0x00bac3c8 | `CONDITIONAL_JUMP`
<a id="insn-00bac38c"></a> `00bac38c` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bac390"></a> `00bac390` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bac394"></a> `00bac394` | `0b 0b 00 54` | b.lt 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac398"></a> `00bac398` | `0b 05 40 39` | ldrb w11,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bac39c"></a> `00bac39c` | `6c 05 1a 12` | and w12,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac3a0"></a> `00bac3a0` | `9f 01 02 71` | cmp w12,#0x80 | `FALL_THROUGH`
<a id="insn-00bac3a4"></a> `00bac3a4` | `81 0a 00 54` | b.ne 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac3a8"></a> `00bac3a8` | `6b 15 00 12` | and w11,w11,#0x3f | `FALL_THROUGH`
<a id="insn-00bac3ac"></a> `00bac3ac` | `4b 11 1a 33` | bfm w11,w10,#0x1a,#0x4 | `FALL_THROUGH`
<a id="insn-00bac3b0"></a> `00bac3b0` | `7f 01 03 eb` | cmp x11,x3 | `FALL_THROUGH`
<a id="insn-00bac3b4"></a> `00bac3b4` | `08 0a 00 54` | b.hi 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac3b8"></a> `00bac3b8` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bac3bc"></a> `00bac3bc` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bac3c0"></a> `00bac3c0` | `43 09 00 54` | b.cc 0x00bac4e8 | `CONDITIONAL_JUMP`
<a id="insn-00bac3c4"></a> `00bac3c4` | `4c 00 00 14` | b 0x00bac4f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac3c8"></a> `00bac3c8` | `5f bd 03 71` | cmp w10,#0xef | `FALL_THROUGH`
<a id="insn-00bac3cc"></a> `00bac3cc` | `c8 01 00 54` | b.hi 0x00bac404 | `CONDITIONAL_JUMP`
<a id="insn-00bac3d0"></a> `00bac3d0` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bac3d4"></a> `00bac3d4` | `7f 0d 00 f1` | cmp x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bac3d8"></a> `00bac3d8` | `eb 08 00 54` | b.lt 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac3dc"></a> `00bac3dc` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bac3e0"></a> `00bac3e0` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bac3e4"></a> `00bac3e4` | `5f b5 03 71` | cmp w10,#0xed | `FALL_THROUGH`
<a id="insn-00bac3e8"></a> `00bac3e8` | `40 03 00 54` | b.eq 0x00bac450 | `CONDITIONAL_JUMP`
<a id="insn-00bac3ec"></a> `00bac3ec` | `5f 81 03 71` | cmp w10,#0xe0 | `FALL_THROUGH`
<a id="insn-00bac3f0"></a> `00bac3f0` | `41 03 00 54` | b.ne 0x00bac458 | `CONDITIONAL_JUMP`
<a id="insn-00bac3f4"></a> `00bac3f4` | `8d 09 1b 12` | and w13,w12,#0xe0 | `FALL_THROUGH`
<a id="insn-00bac3f8"></a> `00bac3f8` | `bf 81 02 71` | cmp w13,#0xa0 | `FALL_THROUGH`
<a id="insn-00bac3fc"></a> `00bac3fc` | `40 03 00 54` | b.eq 0x00bac464 | `CONDITIONAL_JUMP`
<a id="insn-00bac400"></a> `00bac400` | `3d 00 00 14` | b 0x00bac4f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac404"></a> `00bac404` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bac408"></a> `00bac408` | `68 07 00 54` | b.hi 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac40c"></a> `00bac40c` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bac410"></a> `00bac410` | `7f 11 00 f1` | cmp x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bac414"></a> `00bac414` | `0b 07 00 54` | b.lt 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac418"></a> `00bac418` | `4b 00 09 cb` | sub x11,x2,x9 | `FALL_THROUGH`
<a id="insn-00bac41c"></a> `00bac41c` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bac420"></a> `00bac420` | `a3 06 00 54` | b.cc 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac424"></a> `00bac424` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bac428"></a> `00bac428` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bac42c"></a> `00bac42c` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bac430"></a> `00bac430` | `0d 0d 40 39` | ldrb w13,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bac434"></a> `00bac434` | `00 03 00 54` | b.eq 0x00bac494 | `CONDITIONAL_JUMP`
<a id="insn-00bac438"></a> `00bac438` | `5f c1 03 71` | cmp w10,#0xf0 | `FALL_THROUGH`
<a id="insn-00bac43c"></a> `00bac43c` | `01 03 00 54` | b.ne 0x00bac49c | `CONDITIONAL_JUMP`
<a id="insn-00bac440"></a> `00bac440` | `8e 41 02 51` | sub w14,w12,#0x90 | `FALL_THROUGH`
<a id="insn-00bac444"></a> `00bac444` | `df c1 00 71` | cmp w14,#0x30 | `FALL_THROUGH`
<a id="insn-00bac448"></a> `00bac448` | `03 03 00 54` | b.cc 0x00bac4a8 | `CONDITIONAL_JUMP`
<a id="insn-00bac44c"></a> `00bac44c` | `2a 00 00 14` | b 0x00bac4f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac450"></a> `00bac450` | `8d 09 1b 12` | and w13,w12,#0xe0 | `FALL_THROUGH`
<a id="insn-00bac454"></a> `00bac454` | `02 00 00 14` | b 0x00bac45c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac458"></a> `00bac458` | `8d 05 1a 12` | and w13,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac45c"></a> `00bac45c` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bac460"></a> `00bac460` | `a1 04 00 54` | b.ne 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac464"></a> `00bac464` | `6d 05 1a 12` | and w13,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac468"></a> `00bac468` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bac46c"></a> `00bac46c` | `41 04 00 54` | b.ne 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac470"></a> `00bac470` | `4a 0d 14 53` | ubfiz w10,w10,#0xc,#0x4 | `FALL_THROUGH`
<a id="insn-00bac474"></a> `00bac474` | `8a 15 1a 33` | bfm w10,w12,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bac478"></a> `00bac478` | `6a 15 00 33` | bfxil w10,w11,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bac47c"></a> `00bac47c` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bac480"></a> `00bac480` | `a8 03 00 54` | b.hi 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac484"></a> `00bac484` | `08 0d 00 91` | add x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bac488"></a> `00bac488` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bac48c"></a> `00bac48c` | `e3 02 00 54` | b.cc 0x00bac4e8 | `CONDITIONAL_JUMP`
<a id="insn-00bac490"></a> `00bac490` | `19 00 00 14` | b 0x00bac4f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac494"></a> `00bac494` | `8e 0d 1c 12` | and w14,w12,#0xf0 | `FALL_THROUGH`
<a id="insn-00bac498"></a> `00bac498` | `02 00 00 14` | b 0x00bac4a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac49c"></a> `00bac49c` | `8e 05 1a 12` | and w14,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac4a0"></a> `00bac4a0` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bac4a4"></a> `00bac4a4` | `81 02 00 54` | b.ne 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac4a8"></a> `00bac4a8` | `6e 05 1a 12` | and w14,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac4ac"></a> `00bac4ac` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bac4b0"></a> `00bac4b0` | `21 02 00 54` | b.ne 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac4b4"></a> `00bac4b4` | `ae 05 1a 12` | and w14,w13,#0xc0 | `FALL_THROUGH`
<a id="insn-00bac4b8"></a> `00bac4b8` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bac4bc"></a> `00bac4bc` | `c1 01 00 54` | b.ne 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac4c0"></a> `00bac4c0` | `4a 09 6e d3` | ubfiz x10,x10,#0x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bac4c4"></a> `00bac4c4` | `8a 15 74 b3` | bfm x10,x12,#0x34,#0x5 | `FALL_THROUGH`
<a id="insn-00bac4c8"></a> `00bac4c8` | `6a 15 7a b3` | bfm x10,x11,#0x3a,#0x5 | `FALL_THROUGH`
<a id="insn-00bac4cc"></a> `00bac4cc` | `aa 15 40 b3` | bfxil x10,x13,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bac4d0"></a> `00bac4d0` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bac4d4"></a> `00bac4d4` | `08 01 00 54` | b.hi 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac4d8"></a> `00bac4d8` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4dc"></a> `00bac4dc` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bac4e0"></a> `00bac4e0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bac4e4"></a> `00bac4e4` | `82 00 00 54` | b.cs 0x00bac4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac4e8"></a> `00bac4e8` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4ec"></a> `00bac4ec` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bac4f0"></a> `00bac4f0` | `63 f3 ff 54` | b.cc 0x00bac35c | `CONDITIONAL_JUMP`
<a id="insn-00bac4f4"></a> `00bac4f4` | `00 01 00 4b` | sub w0,w8,w0 | `FALL_THROUGH`
<a id="insn-00bac4f8"></a> `00bac4f8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bac2fc`](#insn-00bac2fc) 範囲 `[['00bac2fc', '00bac30f']]`
  - `CONDITIONAL_JUMP` [`00bac30c`](#insn-00bac30c) → [`00bac34c`](#insn-00bac34c)
  - `FALL_THROUGH` [`00bac30c`](#insn-00bac30c) → [`00bac310`](#insn-00bac310)
- ブロック [`00bac310`](#insn-00bac310) 範囲 `[['00bac310', '00bac317']]`
  - `CONDITIONAL_JUMP` [`00bac314`](#insn-00bac314) → [`00bac34c`](#insn-00bac34c)
  - `FALL_THROUGH` [`00bac314`](#insn-00bac314) → [`00bac318`](#insn-00bac318)
- ブロック [`00bac318`](#insn-00bac318) 範囲 `[['00bac318', '00bac327']]`
  - `CONDITIONAL_JUMP` [`00bac324`](#insn-00bac324) → [`00bac34c`](#insn-00bac34c)
  - `FALL_THROUGH` [`00bac324`](#insn-00bac324) → [`00bac328`](#insn-00bac328)
- ブロック [`00bac328`](#insn-00bac328) 範囲 `[['00bac328', '00bac337']]`
  - `CONDITIONAL_JUMP` [`00bac334`](#insn-00bac334) → [`00bac34c`](#insn-00bac34c)
  - `FALL_THROUGH` [`00bac334`](#insn-00bac334) → [`00bac338`](#insn-00bac338)
- ブロック [`00bac338`](#insn-00bac338) 範囲 `[['00bac338', '00bac34b']]`
  - `FALL_THROUGH` [`00bac348`](#insn-00bac348) → [`00bac34c`](#insn-00bac34c)
- ブロック [`00bac34c`](#insn-00bac34c) 範囲 `[['00bac34c', '00bac353']]`
  - `CONDITIONAL_JUMP` [`00bac350`](#insn-00bac350) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac350`](#insn-00bac350) → [`00bac354`](#insn-00bac354)
- ブロック [`00bac354`](#insn-00bac354) 範囲 `[['00bac354', '00bac357']]`
  - `CONDITIONAL_JUMP` [`00bac354`](#insn-00bac354) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac354`](#insn-00bac354) → [`00bac358`](#insn-00bac358)
- ブロック [`00bac358`](#insn-00bac358) 範囲 `[['00bac358', '00bac35b']]`
  - `FALL_THROUGH` [`00bac358`](#insn-00bac358) → [`00bac35c`](#insn-00bac35c)
- ブロック [`00bac35c`](#insn-00bac35c) 範囲 `[['00bac35c', '00bac367']]`
  - `CONDITIONAL_JUMP` [`00bac364`](#insn-00bac364) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac364`](#insn-00bac364) → [`00bac368`](#insn-00bac368)
- ブロック [`00bac368`](#insn-00bac368) 範囲 `[['00bac368', '00bac36b']]`
  - `CONDITIONAL_JUMP` [`00bac368`](#insn-00bac368) → [`00bac37c`](#insn-00bac37c)
  - `FALL_THROUGH` [`00bac368`](#insn-00bac368) → [`00bac36c`](#insn-00bac36c)
- ブロック [`00bac36c`](#insn-00bac36c) 範囲 `[['00bac36c', '00bac377']]`
  - `CONDITIONAL_JUMP` [`00bac374`](#insn-00bac374) → [`00bac4e8`](#insn-00bac4e8)
  - `FALL_THROUGH` [`00bac374`](#insn-00bac374) → [`00bac378`](#insn-00bac378)
- ブロック [`00bac378`](#insn-00bac378) 範囲 `[['00bac378', '00bac37b']]`
  - `UNCONDITIONAL_JUMP` [`00bac378`](#insn-00bac378) → [`00bac4f4`](#insn-00bac4f4)
- ブロック [`00bac37c`](#insn-00bac37c) 範囲 `[['00bac37c', '00bac383']]`
  - `CONDITIONAL_JUMP` [`00bac380`](#insn-00bac380) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac380`](#insn-00bac380) → [`00bac384`](#insn-00bac384)
- ブロック [`00bac384`](#insn-00bac384) 範囲 `[['00bac384', '00bac38b']]`
  - `CONDITIONAL_JUMP` [`00bac388`](#insn-00bac388) → [`00bac3c8`](#insn-00bac3c8)
  - `FALL_THROUGH` [`00bac388`](#insn-00bac388) → [`00bac38c`](#insn-00bac38c)
- ブロック [`00bac38c`](#insn-00bac38c) 範囲 `[['00bac38c', '00bac397']]`
  - `CONDITIONAL_JUMP` [`00bac394`](#insn-00bac394) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac394`](#insn-00bac394) → [`00bac398`](#insn-00bac398)
- ブロック [`00bac398`](#insn-00bac398) 範囲 `[['00bac398', '00bac3a7']]`
  - `CONDITIONAL_JUMP` [`00bac3a4`](#insn-00bac3a4) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac3a4`](#insn-00bac3a4) → [`00bac3a8`](#insn-00bac3a8)
- ブロック [`00bac3a8`](#insn-00bac3a8) 範囲 `[['00bac3a8', '00bac3b7']]`
  - `CONDITIONAL_JUMP` [`00bac3b4`](#insn-00bac3b4) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac3b4`](#insn-00bac3b4) → [`00bac3b8`](#insn-00bac3b8)
- ブロック [`00bac3b8`](#insn-00bac3b8) 範囲 `[['00bac3b8', '00bac3c3']]`
  - `CONDITIONAL_JUMP` [`00bac3c0`](#insn-00bac3c0) → [`00bac4e8`](#insn-00bac4e8)
  - `FALL_THROUGH` [`00bac3c0`](#insn-00bac3c0) → [`00bac3c4`](#insn-00bac3c4)
- ブロック [`00bac3c4`](#insn-00bac3c4) 範囲 `[['00bac3c4', '00bac3c7']]`
  - `UNCONDITIONAL_JUMP` [`00bac3c4`](#insn-00bac3c4) → [`00bac4f4`](#insn-00bac4f4)
- ブロック [`00bac3c8`](#insn-00bac3c8) 範囲 `[['00bac3c8', '00bac3cf']]`
  - `CONDITIONAL_JUMP` [`00bac3cc`](#insn-00bac3cc) → [`00bac404`](#insn-00bac404)
  - `FALL_THROUGH` [`00bac3cc`](#insn-00bac3cc) → [`00bac3d0`](#insn-00bac3d0)
- ブロック [`00bac3d0`](#insn-00bac3d0) 範囲 `[['00bac3d0', '00bac3db']]`
  - `CONDITIONAL_JUMP` [`00bac3d8`](#insn-00bac3d8) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac3d8`](#insn-00bac3d8) → [`00bac3dc`](#insn-00bac3dc)
- ブロック [`00bac3dc`](#insn-00bac3dc) 範囲 `[['00bac3dc', '00bac3eb']]`
  - `CONDITIONAL_JUMP` [`00bac3e8`](#insn-00bac3e8) → [`00bac450`](#insn-00bac450)
  - `FALL_THROUGH` [`00bac3e8`](#insn-00bac3e8) → [`00bac3ec`](#insn-00bac3ec)
- ブロック [`00bac3ec`](#insn-00bac3ec) 範囲 `[['00bac3ec', '00bac3f3']]`
  - `CONDITIONAL_JUMP` [`00bac3f0`](#insn-00bac3f0) → [`00bac458`](#insn-00bac458)
  - `FALL_THROUGH` [`00bac3f0`](#insn-00bac3f0) → [`00bac3f4`](#insn-00bac3f4)
- ブロック [`00bac3f4`](#insn-00bac3f4) 範囲 `[['00bac3f4', '00bac3ff']]`
  - `CONDITIONAL_JUMP` [`00bac3fc`](#insn-00bac3fc) → [`00bac464`](#insn-00bac464)
  - `FALL_THROUGH` [`00bac3fc`](#insn-00bac3fc) → [`00bac400`](#insn-00bac400)
- ブロック [`00bac400`](#insn-00bac400) 範囲 `[['00bac400', '00bac403']]`
  - `UNCONDITIONAL_JUMP` [`00bac400`](#insn-00bac400) → [`00bac4f4`](#insn-00bac4f4)
- ブロック [`00bac404`](#insn-00bac404) 範囲 `[['00bac404', '00bac40b']]`
  - `CONDITIONAL_JUMP` [`00bac408`](#insn-00bac408) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac408`](#insn-00bac408) → [`00bac40c`](#insn-00bac40c)
- ブロック [`00bac40c`](#insn-00bac40c) 範囲 `[['00bac40c', '00bac417']]`
  - `CONDITIONAL_JUMP` [`00bac414`](#insn-00bac414) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac414`](#insn-00bac414) → [`00bac418`](#insn-00bac418)
- ブロック [`00bac418`](#insn-00bac418) 範囲 `[['00bac418', '00bac423']]`
  - `CONDITIONAL_JUMP` [`00bac420`](#insn-00bac420) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac420`](#insn-00bac420) → [`00bac424`](#insn-00bac424)
- ブロック [`00bac424`](#insn-00bac424) 範囲 `[['00bac424', '00bac437']]`
  - `CONDITIONAL_JUMP` [`00bac434`](#insn-00bac434) → [`00bac494`](#insn-00bac494)
  - `FALL_THROUGH` [`00bac434`](#insn-00bac434) → [`00bac438`](#insn-00bac438)
- ブロック [`00bac438`](#insn-00bac438) 範囲 `[['00bac438', '00bac43f']]`
  - `CONDITIONAL_JUMP` [`00bac43c`](#insn-00bac43c) → [`00bac49c`](#insn-00bac49c)
  - `FALL_THROUGH` [`00bac43c`](#insn-00bac43c) → [`00bac440`](#insn-00bac440)
- ブロック [`00bac440`](#insn-00bac440) 範囲 `[['00bac440', '00bac44b']]`
  - `CONDITIONAL_JUMP` [`00bac448`](#insn-00bac448) → [`00bac4a8`](#insn-00bac4a8)
  - `FALL_THROUGH` [`00bac448`](#insn-00bac448) → [`00bac44c`](#insn-00bac44c)
- ブロック [`00bac44c`](#insn-00bac44c) 範囲 `[['00bac44c', '00bac44f']]`
  - `UNCONDITIONAL_JUMP` [`00bac44c`](#insn-00bac44c) → [`00bac4f4`](#insn-00bac4f4)
- ブロック [`00bac450`](#insn-00bac450) 範囲 `[['00bac450', '00bac457']]`
  - `UNCONDITIONAL_JUMP` [`00bac454`](#insn-00bac454) → [`00bac45c`](#insn-00bac45c)
- ブロック [`00bac458`](#insn-00bac458) 範囲 `[['00bac458', '00bac45b']]`
  - `FALL_THROUGH` [`00bac458`](#insn-00bac458) → [`00bac45c`](#insn-00bac45c)
- ブロック [`00bac45c`](#insn-00bac45c) 範囲 `[['00bac45c', '00bac463']]`
  - `CONDITIONAL_JUMP` [`00bac460`](#insn-00bac460) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac460`](#insn-00bac460) → [`00bac464`](#insn-00bac464)
- ブロック [`00bac464`](#insn-00bac464) 範囲 `[['00bac464', '00bac46f']]`
  - `CONDITIONAL_JUMP` [`00bac46c`](#insn-00bac46c) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac46c`](#insn-00bac46c) → [`00bac470`](#insn-00bac470)
- ブロック [`00bac470`](#insn-00bac470) 範囲 `[['00bac470', '00bac483']]`
  - `CONDITIONAL_JUMP` [`00bac480`](#insn-00bac480) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac480`](#insn-00bac480) → [`00bac484`](#insn-00bac484)
- ブロック [`00bac484`](#insn-00bac484) 範囲 `[['00bac484', '00bac48f']]`
  - `CONDITIONAL_JUMP` [`00bac48c`](#insn-00bac48c) → [`00bac4e8`](#insn-00bac4e8)
  - `FALL_THROUGH` [`00bac48c`](#insn-00bac48c) → [`00bac490`](#insn-00bac490)
- ブロック [`00bac490`](#insn-00bac490) 範囲 `[['00bac490', '00bac493']]`
  - `UNCONDITIONAL_JUMP` [`00bac490`](#insn-00bac490) → [`00bac4f4`](#insn-00bac4f4)
- ブロック [`00bac494`](#insn-00bac494) 範囲 `[['00bac494', '00bac49b']]`
  - `UNCONDITIONAL_JUMP` [`00bac498`](#insn-00bac498) → [`00bac4a0`](#insn-00bac4a0)
- ブロック [`00bac49c`](#insn-00bac49c) 範囲 `[['00bac49c', '00bac49f']]`
  - `FALL_THROUGH` [`00bac49c`](#insn-00bac49c) → [`00bac4a0`](#insn-00bac4a0)
- ブロック [`00bac4a0`](#insn-00bac4a0) 範囲 `[['00bac4a0', '00bac4a7']]`
  - `CONDITIONAL_JUMP` [`00bac4a4`](#insn-00bac4a4) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac4a4`](#insn-00bac4a4) → [`00bac4a8`](#insn-00bac4a8)
- ブロック [`00bac4a8`](#insn-00bac4a8) 範囲 `[['00bac4a8', '00bac4b3']]`
  - `CONDITIONAL_JUMP` [`00bac4b0`](#insn-00bac4b0) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac4b0`](#insn-00bac4b0) → [`00bac4b4`](#insn-00bac4b4)
- ブロック [`00bac4b4`](#insn-00bac4b4) 範囲 `[['00bac4b4', '00bac4bf']]`
  - `CONDITIONAL_JUMP` [`00bac4bc`](#insn-00bac4bc) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac4bc`](#insn-00bac4bc) → [`00bac4c0`](#insn-00bac4c0)
- ブロック [`00bac4c0`](#insn-00bac4c0) 範囲 `[['00bac4c0', '00bac4d7']]`
  - `CONDITIONAL_JUMP` [`00bac4d4`](#insn-00bac4d4) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac4d4`](#insn-00bac4d4) → [`00bac4d8`](#insn-00bac4d8)
- ブロック [`00bac4d8`](#insn-00bac4d8) 範囲 `[['00bac4d8', '00bac4e7']]`
  - `CONDITIONAL_JUMP` [`00bac4e4`](#insn-00bac4e4) → [`00bac4f4`](#insn-00bac4f4)
  - `FALL_THROUGH` [`00bac4e4`](#insn-00bac4e4) → [`00bac4e8`](#insn-00bac4e8)
- ブロック [`00bac4e8`](#insn-00bac4e8) 範囲 `[['00bac4e8', '00bac4f3']]`
  - `CONDITIONAL_JUMP` [`00bac4f0`](#insn-00bac4f0) → [`00bac35c`](#insn-00bac35c)
  - `FALL_THROUGH` [`00bac4f0`](#insn-00bac4f0) → [`00bac4f4`](#insn-00bac4f4)
- ブロック [`00bac4f4`](#insn-00bac4f4) 範囲 `[['00bac4f4', '00bac4fb']]`

## 命令位置別の参照

- [`00bac30c`](#insn-00bac30c) → [`00bac34c`](#insn-00bac34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac314`](#insn-00bac314) → [`00bac34c`](#insn-00bac34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac324`](#insn-00bac324) → [`00bac34c`](#insn-00bac34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac334`](#insn-00bac334) → [`00bac34c`](#insn-00bac34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac350`](#insn-00bac350) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac354`](#insn-00bac354) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac364`](#insn-00bac364) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac368`](#insn-00bac368) → [`00bac37c`](#insn-00bac37c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac374`](#insn-00bac374) → [`00bac4e8`](#insn-00bac4e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac378`](#insn-00bac378) → [`00bac4f4`](#insn-00bac4f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac380`](#insn-00bac380) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac388`](#insn-00bac388) → [`00bac3c8`](#insn-00bac3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac394`](#insn-00bac394) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3a4`](#insn-00bac3a4) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3b4`](#insn-00bac3b4) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3c0`](#insn-00bac3c0) → [`00bac4e8`](#insn-00bac4e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3c4`](#insn-00bac3c4) → [`00bac4f4`](#insn-00bac4f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3cc`](#insn-00bac3cc) → [`00bac404`](#insn-00bac404) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3d8`](#insn-00bac3d8) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3e8`](#insn-00bac3e8) → [`00bac450`](#insn-00bac450) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3f0`](#insn-00bac3f0) → [`00bac458`](#insn-00bac458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3fc`](#insn-00bac3fc) → [`00bac464`](#insn-00bac464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac400`](#insn-00bac400) → [`00bac4f4`](#insn-00bac4f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac408`](#insn-00bac408) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac414`](#insn-00bac414) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac420`](#insn-00bac420) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac434`](#insn-00bac434) → [`00bac494`](#insn-00bac494) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac43c`](#insn-00bac43c) → [`00bac49c`](#insn-00bac49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac448`](#insn-00bac448) → [`00bac4a8`](#insn-00bac4a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac44c`](#insn-00bac44c) → [`00bac4f4`](#insn-00bac4f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac454`](#insn-00bac454) → [`00bac45c`](#insn-00bac45c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac460`](#insn-00bac460) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac46c`](#insn-00bac46c) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac480`](#insn-00bac480) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac48c`](#insn-00bac48c) → [`00bac4e8`](#insn-00bac4e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac490`](#insn-00bac490) → [`00bac4f4`](#insn-00bac4f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac498`](#insn-00bac498) → [`00bac4a0`](#insn-00bac4a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4a4`](#insn-00bac4a4) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4b0`](#insn-00bac4b0) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4bc`](#insn-00bac4bc) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4d4`](#insn-00bac4d4) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4e4`](#insn-00bac4e4) → [`00bac4f4`](#insn-00bac4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4f0`](#insn-00bac4f0) → [`00bac35c`](#insn-00bac35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bac30c`](#insn-00bac30c)

~~~json
{
  "source": "00bac30c",
  "target": "00bac34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac314`](#insn-00bac314)

~~~json
{
  "source": "00bac314",
  "target": "00bac34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac324`](#insn-00bac324)

~~~json
{
  "source": "00bac324",
  "target": "00bac34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac334`](#insn-00bac334)

~~~json
{
  "source": "00bac334",
  "target": "00bac34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac350`](#insn-00bac350)

~~~json
{
  "source": "00bac350",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac354`](#insn-00bac354)

~~~json
{
  "source": "00bac354",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac364`](#insn-00bac364)

~~~json
{
  "source": "00bac364",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac368`](#insn-00bac368)

~~~json
{
  "source": "00bac368",
  "target": "00bac37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac374`](#insn-00bac374)

~~~json
{
  "source": "00bac374",
  "target": "00bac4e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac378`](#insn-00bac378)

~~~json
{
  "source": "00bac378",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac380`](#insn-00bac380)

~~~json
{
  "source": "00bac380",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac388`](#insn-00bac388)

~~~json
{
  "source": "00bac388",
  "target": "00bac3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac394`](#insn-00bac394)

~~~json
{
  "source": "00bac394",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3a4`](#insn-00bac3a4)

~~~json
{
  "source": "00bac3a4",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3b4`](#insn-00bac3b4)

~~~json
{
  "source": "00bac3b4",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3c0`](#insn-00bac3c0)

~~~json
{
  "source": "00bac3c0",
  "target": "00bac4e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3c4`](#insn-00bac3c4)

~~~json
{
  "source": "00bac3c4",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3cc`](#insn-00bac3cc)

~~~json
{
  "source": "00bac3cc",
  "target": "00bac404",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3d8`](#insn-00bac3d8)

~~~json
{
  "source": "00bac3d8",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3e8`](#insn-00bac3e8)

~~~json
{
  "source": "00bac3e8",
  "target": "00bac450",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3f0`](#insn-00bac3f0)

~~~json
{
  "source": "00bac3f0",
  "target": "00bac458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3fc`](#insn-00bac3fc)

~~~json
{
  "source": "00bac3fc",
  "target": "00bac464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac400`](#insn-00bac400)

~~~json
{
  "source": "00bac400",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac408`](#insn-00bac408)

~~~json
{
  "source": "00bac408",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac414`](#insn-00bac414)

~~~json
{
  "source": "00bac414",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac420`](#insn-00bac420)

~~~json
{
  "source": "00bac420",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac434`](#insn-00bac434)

~~~json
{
  "source": "00bac434",
  "target": "00bac494",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac43c`](#insn-00bac43c)

~~~json
{
  "source": "00bac43c",
  "target": "00bac49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac448`](#insn-00bac448)

~~~json
{
  "source": "00bac448",
  "target": "00bac4a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac44c`](#insn-00bac44c)

~~~json
{
  "source": "00bac44c",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac454`](#insn-00bac454)

~~~json
{
  "source": "00bac454",
  "target": "00bac45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac460`](#insn-00bac460)

~~~json
{
  "source": "00bac460",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac46c`](#insn-00bac46c)

~~~json
{
  "source": "00bac46c",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac480`](#insn-00bac480)

~~~json
{
  "source": "00bac480",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac48c`](#insn-00bac48c)

~~~json
{
  "source": "00bac48c",
  "target": "00bac4e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac490`](#insn-00bac490)

~~~json
{
  "source": "00bac490",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac498`](#insn-00bac498)

~~~json
{
  "source": "00bac498",
  "target": "00bac4a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4a4`](#insn-00bac4a4)

~~~json
{
  "source": "00bac4a4",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4b0`](#insn-00bac4b0)

~~~json
{
  "source": "00bac4b0",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4bc`](#insn-00bac4bc)

~~~json
{
  "source": "00bac4bc",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4d4`](#insn-00bac4d4)

~~~json
{
  "source": "00bac4d4",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4e4`](#insn-00bac4e4)

~~~json
{
  "source": "00bac4e4",
  "target": "00bac4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4f0`](#insn-00bac4f0)

~~~json
{
  "source": "00bac4f0",
  "target": "00bac35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
