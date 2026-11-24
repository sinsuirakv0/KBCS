# 00be9acc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0005.md#review-9d1a22a0d97213a477b6bb3a3907ba05)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0003.md#review-9d1a22a0d97213a477b6bb3a3907ba05)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00be9acc",
  "name": "FUN_00be9acc",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78441f87a34f62306df212ce9b1b629ba1ec07214c6287d2a7a7f93d0e46f91e",
  "source_text_sha256": "78441f87a34f62306df212ce9b1b629ba1ec07214c6287d2a7a7f93d0e46f91e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00be9acc",
        "00be9dc7"
      ]
    ],
    "bytes_sha256": "50eb489d317f27a0c4cad66122c79fe08b0b20aa42e7d878a0085be0b497e192",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be29a0](../00be2/00be29a0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6477 bytes

~~~c

uint * FUN_00be9acc(uint *param_1,uint *param_2,uint *param_3)

{
  uint *puVar1;
  ulong uVar2;
  uint uVar3;
  uint uVar4;
  bool bVar5;
  uint *puVar6;
  ulong uVar7;
  long lVar8;
  uint *puVar9;
  ulong uVar10;
  long lVar11;
  uint *puVar12;
  uint *puVar13;
  ulong uVar14;
  uint *puVar15;
  uint uVar16;
  uint uVar17;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 2;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar2 = (uVar7 & 0x3fffffffffffffff) << 1 | 1;
          uVar14 = (uVar7 & 0x3fffffffffffffff) * 2 + 2;
          puVar12 = param_1 + uVar2;
          if ((long)uVar14 < lVar8) {
            uVar17 = *puVar12;
            uVar3 = puVar12[1];
            uVar16 = uVar17;
            if (uVar17 <= uVar3) {
              uVar16 = uVar3;
            }
            puVar13 = puVar12 + 1;
            if (uVar3 <= uVar17) {
              puVar13 = puVar12;
              uVar14 = uVar2;
            }
          }
          else {
            uVar16 = *puVar12;
            puVar13 = puVar12;
            uVar14 = uVar2;
          }
          uVar17 = param_1[uVar7];
          puVar12 = param_1 + uVar7;
          if (uVar17 <= uVar16) {
            do {
              while( true ) {
                puVar9 = puVar13;
                *puVar12 = uVar16;
                if ((long)uVar10 < (long)uVar14) goto LAB_00be9af4;
                uVar2 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                puVar6 = param_1 + uVar2;
                puVar12 = puVar9;
                if ((long)uVar14 < lVar8) break;
                uVar16 = *puVar6;
                puVar13 = puVar6;
                uVar14 = uVar2;
                if (uVar16 < uVar17) goto LAB_00be9af4;
              }
              uVar3 = *puVar6;
              uVar4 = puVar6[1];
              uVar16 = uVar3;
              if (uVar3 <= uVar4) {
                uVar16 = uVar4;
              }
              puVar13 = puVar6 + 1;
              if (uVar4 <= uVar3) {
                uVar14 = uVar2;
                puVar13 = puVar6;
              }
            } while (uVar17 <= uVar16);
LAB_00be9af4:
            *puVar9 = uVar17;
          }
        }
        bVar5 = 0 < (long)uVar7;
        uVar7 = uVar7 - 1;
      } while (bVar5);
    }
    puVar12 = param_2;
    if (param_2 != param_3) {
      puVar13 = param_1 + 1;
      puVar9 = param_2;
      do {
        uVar16 = *puVar9;
        if (uVar16 < *param_1) {
          *puVar9 = *param_1;
          *param_1 = uVar16;
          if (1 < lVar8) {
            uVar17 = *puVar13;
            if ((long)param_2 - (long)param_1 == 8) {
              uVar7 = 1;
              puVar12 = puVar13;
            }
            else {
              uVar3 = param_1[2];
              bVar5 = uVar3 <= uVar17;
              if (uVar17 <= uVar3) {
                uVar17 = uVar3;
              }
              puVar12 = param_1 + 2;
                    /* try { // try from 00be9c44 to 00ce9c77 has its CatchHandler @ 00bea280 */
              if (bVar5) {
                puVar12 = puVar13;
              }
              uVar7 = 1;
              if (!bVar5) {
                uVar7 = 2;
              }
            }
            puVar6 = param_1;
            if (uVar16 <= uVar17) {
              do {
                while( true ) {
                  puVar15 = puVar12;
                  *puVar6 = uVar17;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00be9be8;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  puVar1 = param_1 + uVar10;
                  puVar6 = puVar15;
                  if ((long)uVar7 < lVar8) break;
                  uVar17 = *puVar1;
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                  if (uVar17 < uVar16) goto LAB_00be9be8;
                }
                uVar3 = *puVar1;
                uVar4 = puVar1[1];
                uVar17 = uVar3;
                if (uVar3 <= uVar4) {
                  uVar17 = uVar4;
                }
                puVar12 = puVar1 + 1;
                if (uVar4 <= uVar3) {
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                }
                    /* try { // try from 00be9c78 to 00ce9e93 has its CatchHandler @ 00be128c */
              } while (uVar16 <= uVar17);
LAB_00be9be8:
              *puVar15 = uVar16;
            }
          }
        }
        puVar9 = puVar9 + 1;
        puVar12 = param_3;
      } while (puVar9 != param_3);
    }
    param_3 = puVar12;
    if (1 < lVar8) {
      do {
        uVar16 = *param_1;
        uVar7 = 0;
        puVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          puVar13 = puVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            uVar4 = puVar12[uVar7 + 2];
            uVar3 = puVar12[uVar7 + 1];
            uVar17 = uVar3;
            if (uVar3 <= uVar4) {
              uVar17 = uVar4;
            }
            puVar9 = puVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if (uVar4 <= uVar3) {
              puVar9 = puVar13;
              uVar7 = uVar14;
            }
          }
          else {
            uVar17 = *puVar13;
            puVar9 = puVar13;
            uVar7 = uVar14;
          }
          *puVar12 = uVar17;
          puVar12 = puVar9;
        } while ((long)uVar7 <= (long)(lVar8 - 2U >> 1));
        param_2 = param_2 + -1;
        if (puVar9 == param_2) {
          *puVar9 = uVar16;
        }
        else {
          lVar11 = (long)puVar9 + (4 - (long)param_1) >> 2;
          *puVar9 = *param_2;
          *param_2 = uVar16;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            uVar16 = *puVar9;
            uVar17 = param_1[uVar7];
            puVar12 = param_1 + uVar7;
            if (uVar17 < uVar16) {
              do {
                puVar13 = puVar12;
                *puVar9 = uVar17;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                uVar17 = param_1[uVar7];
                puVar9 = puVar13;
                puVar12 = param_1 + uVar7;
              } while (uVar17 < uVar16);
              *puVar13 = uVar16;
            }
          }
        }
        bVar5 = 2 < lVar8;
        lVar8 = lVar8 + -1;
      } while (bVar5);
    }
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00be9acc"></a> `00be9acc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00be9ad0"></a> `00be9ad0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00be9ad4"></a> `00be9ad4` | `e0 0f 00 54` | b.eq 0x00be9cd0 | `CONDITIONAL_JUMP`
<a id="insn-00be9ad8"></a> `00be9ad8` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00be9adc"></a> `00be9adc` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00be9ae0"></a> `00be9ae0` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00be9ae4"></a> `00be9ae4` | `0b 07 00 54` | b.lt 0x00be9bc4 | `CONDITIONAL_JUMP`
<a id="insn-00be9ae8"></a> `00be9ae8` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00be9aec"></a> `00be9aec` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00be9af0"></a> `00be9af0` | `05 00 00 14` | b 0x00be9b04 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9af4"></a> `00be9af4` | `0f 02 00 b9` | str w15,[x16] | `FALL_THROUGH`
<a id="insn-00be9af8"></a> `00be9af8` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00be9afc"></a> `00be9afc` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00be9b00"></a> `00be9b00` | `2d 06 00 54` | b.le 0x00be9bc4 | `CONDITIONAL_JUMP`
<a id="insn-00be9b04"></a> `00be9b04` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00be9b08"></a> `00be9b08` | `8b ff ff 54` | b.lt 0x00be9af8 | `CONDITIONAL_JUMP`
<a id="insn-00be9b0c"></a> `00be9b0c` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00be9b10"></a> `00be9b10` | `8d f5 7f d3` | ubfiz x13,x12,#0x1,#0x3e | `FALL_THROUGH`
<a id="insn-00be9b14"></a> `00be9b14` | `8e f5 7f b3` | bfm x14,x12,#0x3f,#0x3d | `FALL_THROUGH`
<a id="insn-00be9b18"></a> `00be9b18` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00be9b1c"></a> `00be9b1c` | `0d 08 0e 8b` | add x13,x0,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00be9b20"></a> `00be9b20` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00be9b24"></a> `00be9b24` | `2a 01 00 54` | b.ge 0x00be9b48 | `CONDITIONAL_JUMP`
<a id="insn-00be9b28"></a> `00be9b28` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00be9b2c"></a> `00be9b2c` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00be9b30"></a> `00be9b30` | `03 4e 40 b8` | ldr w3,[x16, #0x4]! | `FALL_THROUGH`
<a id="insn-00be9b34"></a> `00be9b34` | `3f 02 03 6b` | cmp w17,w3 | `FALL_THROUGH`
<a id="insn-00be9b38"></a> `00be9b38` | `31 82 83 1a` | csel w17,w17,w3,hi | `FALL_THROUGH`
<a id="insn-00be9b3c"></a> `00be9b3c` | `0d 32 8d 9a` | csel x13,x16,x13,cc | `FALL_THROUGH`
<a id="insn-00be9b40"></a> `00be9b40` | `ee 31 8e 9a` | csel x14,x15,x14,cc | `FALL_THROUGH`
<a id="insn-00be9b44"></a> `00be9b44` | `02 00 00 14` | b 0x00be9b4c | `UNCONDITIONAL_JUMP`
<a id="insn-00be9b48"></a> `00be9b48` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00be9b4c"></a> `00be9b4c` | `10 08 0c 8b` | add x16,x0,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00be9b50"></a> `00be9b50` | `0f 02 40 b9` | ldr w15,[x16] | `FALL_THROUGH`
<a id="insn-00be9b54"></a> `00be9b54` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00be9b58"></a> `00be9b58` | `62 01 00 54` | b.cs 0x00be9b84 | `CONDITIONAL_JUMP`
<a id="insn-00be9b5c"></a> `00be9b5c` | `e7 ff ff 17` | b 0x00be9af8 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9b60"></a> `00be9b60` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00be9b64"></a> `00be9b64` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00be9b68"></a> `00be9b68` | `85 4c 40 b8` | ldr w5,[x4, #0x4]! | `FALL_THROUGH`
<a id="insn-00be9b6c"></a> `00be9b6c` | `3f 02 05 6b` | cmp w17,w5 | `FALL_THROUGH`
<a id="insn-00be9b70"></a> `00be9b70` | `31 82 85 1a` | csel w17,w17,w5,hi | `FALL_THROUGH`
<a id="insn-00be9b74"></a> `00be9b74` | `8d 30 8d 9a` | csel x13,x4,x13,cc | `FALL_THROUGH`
<a id="insn-00be9b78"></a> `00be9b78` | `ce 31 83 9a` | csel x14,x14,x3,cc | `FALL_THROUGH`
<a id="insn-00be9b7c"></a> `00be9b7c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00be9b80"></a> `00be9b80` | `a3 fb ff 54` | b.cc 0x00be9af4 | `CONDITIONAL_JUMP`
<a id="insn-00be9b84"></a> `00be9b84` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00be9b88"></a> `00be9b88` | `11 02 00 b9` | str w17,[x16] | `FALL_THROUGH`
<a id="insn-00be9b8c"></a> `00be9b8c` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00be9b90"></a> `00be9b90` | `2b fb ff 54` | b.lt 0x00be9af4 | `CONDITIONAL_JUMP`
<a id="insn-00be9b94"></a> `00be9b94` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00be9b98"></a> `00be9b98` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00be9b9c"></a> `00be9b9c` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00be9ba0"></a> `00be9ba0` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00be9ba4"></a> `00be9ba4` | `0d 08 03 8b` | add x13,x0,x3, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00be9ba8"></a> `00be9ba8` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00be9bac"></a> `00be9bac` | `ab fd ff 54` | b.lt 0x00be9b60 | `CONDITIONAL_JUMP`
<a id="insn-00be9bb0"></a> `00be9bb0` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00be9bb4"></a> `00be9bb4` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00be9bb8"></a> `00be9bb8` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00be9bbc"></a> `00be9bbc` | `42 fe ff 54` | b.cs 0x00be9b84 | `CONDITIONAL_JUMP`
<a id="insn-00be9bc0"></a> `00be9bc0` | `cd ff ff 17` | b 0x00be9af4 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9bc4"></a> `00be9bc4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00be9bc8"></a> `00be9bc8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00be9bcc"></a> `00be9bcc` | `c0 07 00 54` | b.eq 0x00be9cc4 | `CONDITIONAL_JUMP`
<a id="insn-00be9bd0"></a> `00be9bd0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00be9bd4"></a> `00be9bd4` | `0b 10 00 91` | add x11,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00be9bd8"></a> `00be9bd8` | `0c 20 00 91` | add x12,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00be9bdc"></a> `00be9bdc` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00be9be0"></a> `00be9be0` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00be9be4"></a> `00be9be4` | `05 00 00 14` | b 0x00be9bf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9be8"></a> `00be9be8` | `6f 00 00 b9` | str w15,[x3] | `FALL_THROUGH`
<a id="insn-00be9bec"></a> `00be9bec` | `ce 11 00 91` | add x14,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00be9bf0"></a> `00be9bf0` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00be9bf4"></a> `00be9bf4` | `60 06 00 54` | b.eq 0x00be9cc0 | `CONDITIONAL_JUMP`
<a id="insn-00be9bf8"></a> `00be9bf8` | `cf 01 40 b9` | ldr w15,[x14] | `FALL_THROUGH`
<a id="insn-00be9bfc"></a> `00be9bfc` | `10 00 40 b9` | ldr w16,[x0] | `FALL_THROUGH`
<a id="insn-00be9c00"></a> `00be9c00` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00be9c04"></a> `00be9c04` | `42 ff ff 54` | b.cs 0x00be9bec | `CONDITIONAL_JUMP`
<a id="insn-00be9c08"></a> `00be9c08` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00be9c0c"></a> `00be9c0c` | `d0 01 00 b9` | str w16,[x14] | `FALL_THROUGH`
<a id="insn-00be9c10"></a> `00be9c10` | `0f 00 00 b9` | str w15,[x0] | `FALL_THROUGH`
<a id="insn-00be9c14"></a> `00be9c14` | `cb fe ff 54` | b.lt 0x00be9bec | `CONDITIONAL_JUMP`
<a id="insn-00be9c18"></a> `00be9c18` | `71 01 40 b9` | ldr w17,[x11] | `FALL_THROUGH`
<a id="insn-00be9c1c"></a> `00be9c1c` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-00be9c20"></a> `00be9c20` | `c1 00 00 54` | b.ne 0x00be9c38 | `CONDITIONAL_JUMP`
<a id="insn-00be9c24"></a> `00be9c24` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00be9c28"></a> `00be9c28` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00be9c2c"></a> `00be9c2c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00be9c30"></a> `00be9c30` | `e3 fd ff 54` | b.cc 0x00be9bec | `CONDITIONAL_JUMP`
<a id="insn-00be9c34"></a> `00be9c34` | `08 00 00 14` | b 0x00be9c54 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9c38"></a> `00be9c38` | `90 01 40 b9` | ldr w16,[x12] | `FALL_THROUGH`
<a id="insn-00be9c3c"></a> `00be9c3c` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00be9c40"></a> `00be9c40` | `31 82 90 1a` | csel w17,w17,w16,hi | `FALL_THROUGH`
<a id="insn-00be9c44"></a> `00be9c44` | `90 31 8b 9a` | csel x16,x12,x11,cc | `FALL_THROUGH`
<a id="insn-00be9c48"></a> `00be9c48` | `a4 25 8d 9a` | cinc x4,x13,cc | `FALL_THROUGH`
<a id="insn-00be9c4c"></a> `00be9c4c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00be9c50"></a> `00be9c50` | `e3 fc ff 54` | b.cc 0x00be9bec | `CONDITIONAL_JUMP`
<a id="insn-00be9c54"></a> `00be9c54` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00be9c58"></a> `00be9c58` | `0a 00 00 14` | b 0x00be9c80 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9c5c"></a> `00be9c5c` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00be9c60"></a> `00be9c60` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00be9c64"></a> `00be9c64` | `c7 4c 40 b8` | ldr w7,[x6, #0x4]! | `FALL_THROUGH`
<a id="insn-00be9c68"></a> `00be9c68` | `3f 02 07 6b` | cmp w17,w7 | `FALL_THROUGH`
<a id="insn-00be9c6c"></a> `00be9c6c` | `31 82 87 1a` | csel w17,w17,w7,hi | `FALL_THROUGH`
<a id="insn-00be9c70"></a> `00be9c70` | `d0 30 90 9a` | csel x16,x6,x16,cc | `FALL_THROUGH`
<a id="insn-00be9c74"></a> `00be9c74` | `84 30 85 9a` | csel x4,x4,x5,cc | `FALL_THROUGH`
<a id="insn-00be9c78"></a> `00be9c78` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00be9c7c"></a> `00be9c7c` | `63 fb ff 54` | b.cc 0x00be9be8 | `CONDITIONAL_JUMP`
<a id="insn-00be9c80"></a> `00be9c80` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00be9c84"></a> `00be9c84` | `71 00 00 b9` | str w17,[x3] | `FALL_THROUGH`
<a id="insn-00be9c88"></a> `00be9c88` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00be9c8c"></a> `00be9c8c` | `eb fa ff 54` | b.lt 0x00be9be8 | `CONDITIONAL_JUMP`
<a id="insn-00be9c90"></a> `00be9c90` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00be9c94"></a> `00be9c94` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00be9c98"></a> `00be9c98` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00be9c9c"></a> `00be9c9c` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00be9ca0"></a> `00be9ca0` | `10 08 05 8b` | add x16,x0,x5, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00be9ca4"></a> `00be9ca4` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00be9ca8"></a> `00be9ca8` | `ab fd ff 54` | b.lt 0x00be9c5c | `CONDITIONAL_JUMP`
<a id="insn-00be9cac"></a> `00be9cac` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00be9cb0"></a> `00be9cb0` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00be9cb4"></a> `00be9cb4` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00be9cb8"></a> `00be9cb8` | `42 fe ff 54` | b.cs 0x00be9c80 | `CONDITIONAL_JUMP`
<a id="insn-00be9cbc"></a> `00be9cbc` | `cb ff ff 17` | b 0x00be9be8 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9cc0"></a> `00be9cc0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00be9cc4"></a> `00be9cc4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00be9cc8"></a> `00be9cc8` | `0a 01 00 54` | b.ge 0x00be9ce8 | `CONDITIONAL_JUMP`
<a id="insn-00be9ccc"></a> `00be9ccc` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00be9cd0"></a> `00be9cd0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00be9cd4"></a> `00be9cd4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00be9cd8"></a> `00be9cd8` | `2a 01 00 b9` | str w10,[x9] | `FALL_THROUGH`
<a id="insn-00be9cdc"></a> `00be9cdc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00be9ce0"></a> `00be9ce0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00be9ce4"></a> `00be9ce4` | `4d ff ff 54` | b.le 0x00be9ccc | `CONDITIONAL_JUMP`
<a id="insn-00be9ce8"></a> `00be9ce8` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00be9cec"></a> `00be9cec` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00be9cf0"></a> `00be9cf0` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00be9cf4"></a> `00be9cf4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00be9cf8"></a> `00be9cf8` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00be9cfc"></a> `00be9cfc` | `0b 00 00 14` | b 0x00be9d28 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9d00"></a> `00be9d00` | `0d 8e 40 b8` | ldr w13,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00be9d04"></a> `00be9d04` | `0f c2 5f b8` | ldur w15,[x16, #-0x4] | `FALL_THROUGH`
<a id="insn-00be9d08"></a> `00be9d08` | `ff 01 0d 6b` | cmp w15,w13 | `FALL_THROUGH`
<a id="insn-00be9d0c"></a> `00be9d0c` | `ef 81 8d 1a` | csel w15,w15,w13,hi | `FALL_THROUGH`
<a id="insn-00be9d10"></a> `00be9d10` | `09 32 89 9a` | csel x9,x16,x9,cc | `FALL_THROUGH`
<a id="insn-00be9d14"></a> `00be9d14` | `2d 32 8e 9a` | csel x13,x17,x14,cc | `FALL_THROUGH`
<a id="insn-00be9d18"></a> `00be9d18` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00be9d1c"></a> `00be9d1c` | `8f 01 00 b9` | str w15,[x12] | `FALL_THROUGH`
<a id="insn-00be9d20"></a> `00be9d20` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00be9d24"></a> `00be9d24` | `8c 01 00 54` | b.gt 0x00be9d54 | `CONDITIONAL_JUMP`
<a id="insn-00be9d28"></a> `00be9d28` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00be9d2c"></a> `00be9d2c` | `90 09 0d 8b` | add x16,x12,x13, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00be9d30"></a> `00be9d30` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00be9d34"></a> `00be9d34` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00be9d38"></a> `00be9d38` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00be9d3c"></a> `00be9d3c` | `09 12 00 91` | add x9,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00be9d40"></a> `00be9d40` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00be9d44"></a> `00be9d44` | `eb fd ff 54` | b.lt 0x00be9d00 | `CONDITIONAL_JUMP`
<a id="insn-00be9d48"></a> `00be9d48` | `2f 01 40 b9` | ldr w15,[x9] | `FALL_THROUGH`
<a id="insn-00be9d4c"></a> `00be9d4c` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00be9d50"></a> `00be9d50` | `f2 ff ff 17` | b 0x00be9d18 | `UNCONDITIONAL_JUMP`
<a id="insn-00be9d54"></a> `00be9d54` | `21 10 00 d1` | sub x1,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00be9d58"></a> `00be9d58` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00be9d5c"></a> `00be9d5c` | `e0 fb ff 54` | b.eq 0x00be9cd8 | `CONDITIONAL_JUMP`
<a id="insn-00be9d60"></a> `00be9d60` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00be9d64"></a> `00be9d64` | `2c 00 40 b9` | ldr w12,[x1] | `FALL_THROUGH`
<a id="insn-00be9d68"></a> `00be9d68` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00be9d6c"></a> `00be9d6c` | `6b fd 42 93` | asr x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00be9d70"></a> `00be9d70` | `2c 01 00 b9` | str w12,[x9] | `FALL_THROUGH`
<a id="insn-00be9d74"></a> `00be9d74` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00be9d78"></a> `00be9d78` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00be9d7c"></a> `00be9d7c` | `0b fb ff 54` | b.lt 0x00be9cdc | `CONDITIONAL_JUMP`
<a id="insn-00be9d80"></a> `00be9d80` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00be9d84"></a> `00be9d84` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00be9d88"></a> `00be9d88` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00be9d8c"></a> `00be9d8c` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00be9d90"></a> `00be9d90` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00be9d94"></a> `00be9d94` | `42 fa ff 54` | b.cs 0x00be9cdc | `CONDITIONAL_JUMP`
<a id="insn-00be9d98"></a> `00be9d98` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00be9d9c"></a> `00be9d9c` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00be9da0"></a> `00be9da0` | `cd 01 00 b9` | str w13,[x14] | `FALL_THROUGH`
<a id="insn-00be9da4"></a> `00be9da4` | `ea 00 00 b4` | cbz x10,0x00be9dc0 | `CONDITIONAL_JUMP`
<a id="insn-00be9da8"></a> `00be9da8` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00be9dac"></a> `00be9dac` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00be9db0"></a> `00be9db0` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00be9db4"></a> `00be9db4` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00be9db8"></a> `00be9db8` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00be9dbc"></a> `00be9dbc` | `e3 fe ff 54` | b.cc 0x00be9d98 | `CONDITIONAL_JUMP`
<a id="insn-00be9dc0"></a> `00be9dc0` | `2b 01 00 b9` | str w11,[x9] | `FALL_THROUGH`
<a id="insn-00be9dc4"></a> `00be9dc4` | `c6 ff ff 17` | b 0x00be9cdc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00be9acc`](#insn-00be9acc) 範囲 `[['00be9acc', '00be9ad7']]`
  - `CONDITIONAL_JUMP` [`00be9ad4`](#insn-00be9ad4) → [`00be9cd0`](#insn-00be9cd0)
  - `FALL_THROUGH` [`00be9ad4`](#insn-00be9ad4) → [`00be9ad8`](#insn-00be9ad8)
- ブロック [`00be9ad8`](#insn-00be9ad8) 範囲 `[['00be9ad8', '00be9ae7']]`
  - `CONDITIONAL_JUMP` [`00be9ae4`](#insn-00be9ae4) → [`00be9bc4`](#insn-00be9bc4)
  - `FALL_THROUGH` [`00be9ae4`](#insn-00be9ae4) → [`00be9ae8`](#insn-00be9ae8)
- ブロック [`00be9ae8`](#insn-00be9ae8) 範囲 `[['00be9ae8', '00be9af3']]`
  - `UNCONDITIONAL_JUMP` [`00be9af0`](#insn-00be9af0) → [`00be9b04`](#insn-00be9b04)
- ブロック [`00be9af4`](#insn-00be9af4) 範囲 `[['00be9af4', '00be9af7']]`
  - `FALL_THROUGH` [`00be9af4`](#insn-00be9af4) → [`00be9af8`](#insn-00be9af8)
- ブロック [`00be9af8`](#insn-00be9af8) 範囲 `[['00be9af8', '00be9b03']]`
  - `CONDITIONAL_JUMP` [`00be9b00`](#insn-00be9b00) → [`00be9bc4`](#insn-00be9bc4)
  - `FALL_THROUGH` [`00be9b00`](#insn-00be9b00) → [`00be9b04`](#insn-00be9b04)
- ブロック [`00be9b04`](#insn-00be9b04) 範囲 `[['00be9b04', '00be9b0b']]`
  - `CONDITIONAL_JUMP` [`00be9b08`](#insn-00be9b08) → [`00be9af8`](#insn-00be9af8)
  - `FALL_THROUGH` [`00be9b08`](#insn-00be9b08) → [`00be9b0c`](#insn-00be9b0c)
- ブロック [`00be9b0c`](#insn-00be9b0c) 範囲 `[['00be9b0c', '00be9b27']]`
  - `CONDITIONAL_JUMP` [`00be9b24`](#insn-00be9b24) → [`00be9b48`](#insn-00be9b48)
  - `FALL_THROUGH` [`00be9b24`](#insn-00be9b24) → [`00be9b28`](#insn-00be9b28)
- ブロック [`00be9b28`](#insn-00be9b28) 範囲 `[['00be9b28', '00be9b47']]`
  - `UNCONDITIONAL_JUMP` [`00be9b44`](#insn-00be9b44) → [`00be9b4c`](#insn-00be9b4c)
- ブロック [`00be9b48`](#insn-00be9b48) 範囲 `[['00be9b48', '00be9b4b']]`
  - `FALL_THROUGH` [`00be9b48`](#insn-00be9b48) → [`00be9b4c`](#insn-00be9b4c)
- ブロック [`00be9b4c`](#insn-00be9b4c) 範囲 `[['00be9b4c', '00be9b5b']]`
  - `CONDITIONAL_JUMP` [`00be9b58`](#insn-00be9b58) → [`00be9b84`](#insn-00be9b84)
  - `FALL_THROUGH` [`00be9b58`](#insn-00be9b58) → [`00be9b5c`](#insn-00be9b5c)
- ブロック [`00be9b5c`](#insn-00be9b5c) 範囲 `[['00be9b5c', '00be9b5f']]`
  - `UNCONDITIONAL_JUMP` [`00be9b5c`](#insn-00be9b5c) → [`00be9af8`](#insn-00be9af8)
- ブロック [`00be9b60`](#insn-00be9b60) 範囲 `[['00be9b60', '00be9b83']]`
  - `CONDITIONAL_JUMP` [`00be9b80`](#insn-00be9b80) → [`00be9af4`](#insn-00be9af4)
  - `FALL_THROUGH` [`00be9b80`](#insn-00be9b80) → [`00be9b84`](#insn-00be9b84)
- ブロック [`00be9b84`](#insn-00be9b84) 範囲 `[['00be9b84', '00be9b93']]`
  - `CONDITIONAL_JUMP` [`00be9b90`](#insn-00be9b90) → [`00be9af4`](#insn-00be9af4)
  - `FALL_THROUGH` [`00be9b90`](#insn-00be9b90) → [`00be9b94`](#insn-00be9b94)
- ブロック [`00be9b94`](#insn-00be9b94) 範囲 `[['00be9b94', '00be9baf']]`
  - `CONDITIONAL_JUMP` [`00be9bac`](#insn-00be9bac) → [`00be9b60`](#insn-00be9b60)
  - `FALL_THROUGH` [`00be9bac`](#insn-00be9bac) → [`00be9bb0`](#insn-00be9bb0)
- ブロック [`00be9bb0`](#insn-00be9bb0) 範囲 `[['00be9bb0', '00be9bbf']]`
  - `CONDITIONAL_JUMP` [`00be9bbc`](#insn-00be9bbc) → [`00be9b84`](#insn-00be9b84)
  - `FALL_THROUGH` [`00be9bbc`](#insn-00be9bbc) → [`00be9bc0`](#insn-00be9bc0)
- ブロック [`00be9bc0`](#insn-00be9bc0) 範囲 `[['00be9bc0', '00be9bc3']]`
  - `UNCONDITIONAL_JUMP` [`00be9bc0`](#insn-00be9bc0) → [`00be9af4`](#insn-00be9af4)
- ブロック [`00be9bc4`](#insn-00be9bc4) 範囲 `[['00be9bc4', '00be9bcf']]`
  - `CONDITIONAL_JUMP` [`00be9bcc`](#insn-00be9bcc) → [`00be9cc4`](#insn-00be9cc4)
  - `FALL_THROUGH` [`00be9bcc`](#insn-00be9bcc) → [`00be9bd0`](#insn-00be9bd0)
- ブロック [`00be9bd0`](#insn-00be9bd0) 範囲 `[['00be9bd0', '00be9be7']]`
  - `UNCONDITIONAL_JUMP` [`00be9be4`](#insn-00be9be4) → [`00be9bf8`](#insn-00be9bf8)
- ブロック [`00be9be8`](#insn-00be9be8) 範囲 `[['00be9be8', '00be9beb']]`
  - `FALL_THROUGH` [`00be9be8`](#insn-00be9be8) → [`00be9bec`](#insn-00be9bec)
- ブロック [`00be9bec`](#insn-00be9bec) 範囲 `[['00be9bec', '00be9bf7']]`
  - `CONDITIONAL_JUMP` [`00be9bf4`](#insn-00be9bf4) → [`00be9cc0`](#insn-00be9cc0)
  - `FALL_THROUGH` [`00be9bf4`](#insn-00be9bf4) → [`00be9bf8`](#insn-00be9bf8)
- ブロック [`00be9bf8`](#insn-00be9bf8) 範囲 `[['00be9bf8', '00be9c07']]`
  - `CONDITIONAL_JUMP` [`00be9c04`](#insn-00be9c04) → [`00be9bec`](#insn-00be9bec)
  - `FALL_THROUGH` [`00be9c04`](#insn-00be9c04) → [`00be9c08`](#insn-00be9c08)
- ブロック [`00be9c08`](#insn-00be9c08) 範囲 `[['00be9c08', '00be9c17']]`
  - `CONDITIONAL_JUMP` [`00be9c14`](#insn-00be9c14) → [`00be9bec`](#insn-00be9bec)
  - `FALL_THROUGH` [`00be9c14`](#insn-00be9c14) → [`00be9c18`](#insn-00be9c18)
- ブロック [`00be9c18`](#insn-00be9c18) 範囲 `[['00be9c18', '00be9c23']]`
  - `CONDITIONAL_JUMP` [`00be9c20`](#insn-00be9c20) → [`00be9c38`](#insn-00be9c38)
  - `FALL_THROUGH` [`00be9c20`](#insn-00be9c20) → [`00be9c24`](#insn-00be9c24)
- ブロック [`00be9c24`](#insn-00be9c24) 範囲 `[['00be9c24', '00be9c33']]`
  - `CONDITIONAL_JUMP` [`00be9c30`](#insn-00be9c30) → [`00be9bec`](#insn-00be9bec)
  - `FALL_THROUGH` [`00be9c30`](#insn-00be9c30) → [`00be9c34`](#insn-00be9c34)
- ブロック [`00be9c34`](#insn-00be9c34) 範囲 `[['00be9c34', '00be9c37']]`
  - `UNCONDITIONAL_JUMP` [`00be9c34`](#insn-00be9c34) → [`00be9c54`](#insn-00be9c54)
- ブロック [`00be9c38`](#insn-00be9c38) 範囲 `[['00be9c38', '00be9c43']]`
  - `FALL_THROUGH` [`00be9c40`](#insn-00be9c40) → [`00be9c44`](#insn-00be9c44)
- ブロック [`00be9c44`](#insn-00be9c44) 範囲 `[['00be9c44', '00be9c53']]`
  - `CONDITIONAL_JUMP` [`00be9c50`](#insn-00be9c50) → [`00be9bec`](#insn-00be9bec)
  - `FALL_THROUGH` [`00be9c50`](#insn-00be9c50) → [`00be9c54`](#insn-00be9c54)
- ブロック [`00be9c54`](#insn-00be9c54) 範囲 `[['00be9c54', '00be9c5b']]`
  - `UNCONDITIONAL_JUMP` [`00be9c58`](#insn-00be9c58) → [`00be9c80`](#insn-00be9c80)
- ブロック [`00be9c5c`](#insn-00be9c5c) 範囲 `[['00be9c5c', '00be9c77']]`
  - `FALL_THROUGH` [`00be9c74`](#insn-00be9c74) → [`00be9c78`](#insn-00be9c78)
- ブロック [`00be9c78`](#insn-00be9c78) 範囲 `[['00be9c78', '00be9c7f']]`
  - `CONDITIONAL_JUMP` [`00be9c7c`](#insn-00be9c7c) → [`00be9be8`](#insn-00be9be8)
  - `FALL_THROUGH` [`00be9c7c`](#insn-00be9c7c) → [`00be9c80`](#insn-00be9c80)
- ブロック [`00be9c80`](#insn-00be9c80) 範囲 `[['00be9c80', '00be9c8f']]`
  - `CONDITIONAL_JUMP` [`00be9c8c`](#insn-00be9c8c) → [`00be9be8`](#insn-00be9be8)
  - `FALL_THROUGH` [`00be9c8c`](#insn-00be9c8c) → [`00be9c90`](#insn-00be9c90)
- ブロック [`00be9c90`](#insn-00be9c90) 範囲 `[['00be9c90', '00be9cab']]`
  - `CONDITIONAL_JUMP` [`00be9ca8`](#insn-00be9ca8) → [`00be9c5c`](#insn-00be9c5c)
  - `FALL_THROUGH` [`00be9ca8`](#insn-00be9ca8) → [`00be9cac`](#insn-00be9cac)
- ブロック [`00be9cac`](#insn-00be9cac) 範囲 `[['00be9cac', '00be9cbb']]`
  - `CONDITIONAL_JUMP` [`00be9cb8`](#insn-00be9cb8) → [`00be9c80`](#insn-00be9c80)
  - `FALL_THROUGH` [`00be9cb8`](#insn-00be9cb8) → [`00be9cbc`](#insn-00be9cbc)
- ブロック [`00be9cbc`](#insn-00be9cbc) 範囲 `[['00be9cbc', '00be9cbf']]`
  - `UNCONDITIONAL_JUMP` [`00be9cbc`](#insn-00be9cbc) → [`00be9be8`](#insn-00be9be8)
- ブロック [`00be9cc0`](#insn-00be9cc0) 範囲 `[['00be9cc0', '00be9cc3']]`
  - `FALL_THROUGH` [`00be9cc0`](#insn-00be9cc0) → [`00be9cc4`](#insn-00be9cc4)
- ブロック [`00be9cc4`](#insn-00be9cc4) 範囲 `[['00be9cc4', '00be9ccb']]`
  - `CONDITIONAL_JUMP` [`00be9cc8`](#insn-00be9cc8) → [`00be9ce8`](#insn-00be9ce8)
  - `FALL_THROUGH` [`00be9cc8`](#insn-00be9cc8) → [`00be9ccc`](#insn-00be9ccc)
- ブロック [`00be9ccc`](#insn-00be9ccc) 範囲 `[['00be9ccc', '00be9ccf']]`
  - `FALL_THROUGH` [`00be9ccc`](#insn-00be9ccc) → [`00be9cd0`](#insn-00be9cd0)
- ブロック [`00be9cd0`](#insn-00be9cd0) 範囲 `[['00be9cd0', '00be9cd7']]`
- ブロック [`00be9cd8`](#insn-00be9cd8) 範囲 `[['00be9cd8', '00be9cdb']]`
  - `FALL_THROUGH` [`00be9cd8`](#insn-00be9cd8) → [`00be9cdc`](#insn-00be9cdc)
- ブロック [`00be9cdc`](#insn-00be9cdc) 範囲 `[['00be9cdc', '00be9ce7']]`
  - `CONDITIONAL_JUMP` [`00be9ce4`](#insn-00be9ce4) → [`00be9ccc`](#insn-00be9ccc)
  - `FALL_THROUGH` [`00be9ce4`](#insn-00be9ce4) → [`00be9ce8`](#insn-00be9ce8)
- ブロック [`00be9ce8`](#insn-00be9ce8) 範囲 `[['00be9ce8', '00be9cff']]`
  - `UNCONDITIONAL_JUMP` [`00be9cfc`](#insn-00be9cfc) → [`00be9d28`](#insn-00be9d28)
- ブロック [`00be9d00`](#insn-00be9d00) 範囲 `[['00be9d00', '00be9d17']]`
  - `FALL_THROUGH` [`00be9d14`](#insn-00be9d14) → [`00be9d18`](#insn-00be9d18)
- ブロック [`00be9d18`](#insn-00be9d18) 範囲 `[['00be9d18', '00be9d27']]`
  - `CONDITIONAL_JUMP` [`00be9d24`](#insn-00be9d24) → [`00be9d54`](#insn-00be9d54)
  - `FALL_THROUGH` [`00be9d24`](#insn-00be9d24) → [`00be9d28`](#insn-00be9d28)
- ブロック [`00be9d28`](#insn-00be9d28) 範囲 `[['00be9d28', '00be9d47']]`
  - `CONDITIONAL_JUMP` [`00be9d44`](#insn-00be9d44) → [`00be9d00`](#insn-00be9d00)
  - `FALL_THROUGH` [`00be9d44`](#insn-00be9d44) → [`00be9d48`](#insn-00be9d48)
- ブロック [`00be9d48`](#insn-00be9d48) 範囲 `[['00be9d48', '00be9d53']]`
  - `UNCONDITIONAL_JUMP` [`00be9d50`](#insn-00be9d50) → [`00be9d18`](#insn-00be9d18)
- ブロック [`00be9d54`](#insn-00be9d54) 範囲 `[['00be9d54', '00be9d5f']]`
  - `CONDITIONAL_JUMP` [`00be9d5c`](#insn-00be9d5c) → [`00be9cd8`](#insn-00be9cd8)
  - `FALL_THROUGH` [`00be9d5c`](#insn-00be9d5c) → [`00be9d60`](#insn-00be9d60)
- ブロック [`00be9d60`](#insn-00be9d60) 範囲 `[['00be9d60', '00be9d7f']]`
  - `CONDITIONAL_JUMP` [`00be9d7c`](#insn-00be9d7c) → [`00be9cdc`](#insn-00be9cdc)
  - `FALL_THROUGH` [`00be9d7c`](#insn-00be9d7c) → [`00be9d80`](#insn-00be9d80)
- ブロック [`00be9d80`](#insn-00be9d80) 範囲 `[['00be9d80', '00be9d97']]`
  - `CONDITIONAL_JUMP` [`00be9d94`](#insn-00be9d94) → [`00be9cdc`](#insn-00be9cdc)
  - `FALL_THROUGH` [`00be9d94`](#insn-00be9d94) → [`00be9d98`](#insn-00be9d98)
- ブロック [`00be9d98`](#insn-00be9d98) 範囲 `[['00be9d98', '00be9da7']]`
  - `CONDITIONAL_JUMP` [`00be9da4`](#insn-00be9da4) → [`00be9dc0`](#insn-00be9dc0)
  - `FALL_THROUGH` [`00be9da4`](#insn-00be9da4) → [`00be9da8`](#insn-00be9da8)
- ブロック [`00be9da8`](#insn-00be9da8) 範囲 `[['00be9da8', '00be9dbf']]`
  - `CONDITIONAL_JUMP` [`00be9dbc`](#insn-00be9dbc) → [`00be9d98`](#insn-00be9d98)
  - `FALL_THROUGH` [`00be9dbc`](#insn-00be9dbc) → [`00be9dc0`](#insn-00be9dc0)
- ブロック [`00be9dc0`](#insn-00be9dc0) 範囲 `[['00be9dc0', '00be9dc7']]`
  - `UNCONDITIONAL_JUMP` [`00be9dc4`](#insn-00be9dc4) → [`00be9cdc`](#insn-00be9cdc)

## 命令位置別の参照

- [`00be9ad4`](#insn-00be9ad4) → [`00be9cd0`](#insn-00be9cd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9ae4`](#insn-00be9ae4) → [`00be9bc4`](#insn-00be9bc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9af0`](#insn-00be9af0) → [`00be9b04`](#insn-00be9b04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b00`](#insn-00be9b00) → [`00be9bc4`](#insn-00be9bc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b08`](#insn-00be9b08) → [`00be9af8`](#insn-00be9af8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b24`](#insn-00be9b24) → [`00be9b48`](#insn-00be9b48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b44`](#insn-00be9b44) → [`00be9b4c`](#insn-00be9b4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b58`](#insn-00be9b58) → [`00be9b84`](#insn-00be9b84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b5c`](#insn-00be9b5c) → [`00be9af8`](#insn-00be9af8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b80`](#insn-00be9b80) → [`00be9af4`](#insn-00be9af4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9b90`](#insn-00be9b90) → [`00be9af4`](#insn-00be9af4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9bac`](#insn-00be9bac) → [`00be9b60`](#insn-00be9b60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9bbc`](#insn-00be9bbc) → [`00be9b84`](#insn-00be9b84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9bc0`](#insn-00be9bc0) → [`00be9af4`](#insn-00be9af4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9bcc`](#insn-00be9bcc) → [`00be9cc4`](#insn-00be9cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9be4`](#insn-00be9be4) → [`00be9bf8`](#insn-00be9bf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9bf4`](#insn-00be9bf4) → [`00be9cc0`](#insn-00be9cc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c04`](#insn-00be9c04) → [`00be9bec`](#insn-00be9bec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c14`](#insn-00be9c14) → [`00be9bec`](#insn-00be9bec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c20`](#insn-00be9c20) → [`00be9c38`](#insn-00be9c38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c30`](#insn-00be9c30) → [`00be9bec`](#insn-00be9bec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c34`](#insn-00be9c34) → [`00be9c54`](#insn-00be9c54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c50`](#insn-00be9c50) → [`00be9bec`](#insn-00be9bec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c58`](#insn-00be9c58) → [`00be9c80`](#insn-00be9c80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c7c`](#insn-00be9c7c) → [`00be9be8`](#insn-00be9be8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9c8c`](#insn-00be9c8c) → [`00be9be8`](#insn-00be9be8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9ca8`](#insn-00be9ca8) → [`00be9c5c`](#insn-00be9c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9cb8`](#insn-00be9cb8) → [`00be9c80`](#insn-00be9c80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9cbc`](#insn-00be9cbc) → [`00be9be8`](#insn-00be9be8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9cc8`](#insn-00be9cc8) → [`00be9ce8`](#insn-00be9ce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9ce4`](#insn-00be9ce4) → [`00be9ccc`](#insn-00be9ccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9cfc`](#insn-00be9cfc) → [`00be9d28`](#insn-00be9d28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9d24`](#insn-00be9d24) → [`00be9d54`](#insn-00be9d54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9d44`](#insn-00be9d44) → [`00be9d00`](#insn-00be9d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9d50`](#insn-00be9d50) → [`00be9d18`](#insn-00be9d18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9d5c`](#insn-00be9d5c) → [`00be9cd8`](#insn-00be9cd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9d7c`](#insn-00be9d7c) → [`00be9cdc`](#insn-00be9cdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9d94`](#insn-00be9d94) → [`00be9cdc`](#insn-00be9cdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9da4`](#insn-00be9da4) → [`00be9dc0`](#insn-00be9dc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9dbc`](#insn-00be9dbc) → [`00be9d98`](#insn-00be9d98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be9dc4`](#insn-00be9dc4) → [`00be9cdc`](#insn-00be9cdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00be9ad4`](#insn-00be9ad4)

~~~json
{
  "source": "00be9ad4",
  "target": "00be9cd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9ae4`](#insn-00be9ae4)

~~~json
{
  "source": "00be9ae4",
  "target": "00be9bc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9af0`](#insn-00be9af0)

~~~json
{
  "source": "00be9af0",
  "target": "00be9b04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b00`](#insn-00be9b00)

~~~json
{
  "source": "00be9b00",
  "target": "00be9bc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b08`](#insn-00be9b08)

~~~json
{
  "source": "00be9b08",
  "target": "00be9af8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b24`](#insn-00be9b24)

~~~json
{
  "source": "00be9b24",
  "target": "00be9b48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b44`](#insn-00be9b44)

~~~json
{
  "source": "00be9b44",
  "target": "00be9b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b58`](#insn-00be9b58)

~~~json
{
  "source": "00be9b58",
  "target": "00be9b84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b5c`](#insn-00be9b5c)

~~~json
{
  "source": "00be9b5c",
  "target": "00be9af8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b80`](#insn-00be9b80)

~~~json
{
  "source": "00be9b80",
  "target": "00be9af4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9b90`](#insn-00be9b90)

~~~json
{
  "source": "00be9b90",
  "target": "00be9af4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9bac`](#insn-00be9bac)

~~~json
{
  "source": "00be9bac",
  "target": "00be9b60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9bbc`](#insn-00be9bbc)

~~~json
{
  "source": "00be9bbc",
  "target": "00be9b84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9bc0`](#insn-00be9bc0)

~~~json
{
  "source": "00be9bc0",
  "target": "00be9af4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9bcc`](#insn-00be9bcc)

~~~json
{
  "source": "00be9bcc",
  "target": "00be9cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9be4`](#insn-00be9be4)

~~~json
{
  "source": "00be9be4",
  "target": "00be9bf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9bf4`](#insn-00be9bf4)

~~~json
{
  "source": "00be9bf4",
  "target": "00be9cc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c04`](#insn-00be9c04)

~~~json
{
  "source": "00be9c04",
  "target": "00be9bec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c14`](#insn-00be9c14)

~~~json
{
  "source": "00be9c14",
  "target": "00be9bec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c20`](#insn-00be9c20)

~~~json
{
  "source": "00be9c20",
  "target": "00be9c38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c30`](#insn-00be9c30)

~~~json
{
  "source": "00be9c30",
  "target": "00be9bec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c34`](#insn-00be9c34)

~~~json
{
  "source": "00be9c34",
  "target": "00be9c54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c50`](#insn-00be9c50)

~~~json
{
  "source": "00be9c50",
  "target": "00be9bec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c58`](#insn-00be9c58)

~~~json
{
  "source": "00be9c58",
  "target": "00be9c80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c7c`](#insn-00be9c7c)

~~~json
{
  "source": "00be9c7c",
  "target": "00be9be8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9c8c`](#insn-00be9c8c)

~~~json
{
  "source": "00be9c8c",
  "target": "00be9be8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9ca8`](#insn-00be9ca8)

~~~json
{
  "source": "00be9ca8",
  "target": "00be9c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9cb8`](#insn-00be9cb8)

~~~json
{
  "source": "00be9cb8",
  "target": "00be9c80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9cbc`](#insn-00be9cbc)

~~~json
{
  "source": "00be9cbc",
  "target": "00be9be8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9cc8`](#insn-00be9cc8)

~~~json
{
  "source": "00be9cc8",
  "target": "00be9ce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9ce4`](#insn-00be9ce4)

~~~json
{
  "source": "00be9ce4",
  "target": "00be9ccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9cfc`](#insn-00be9cfc)

~~~json
{
  "source": "00be9cfc",
  "target": "00be9d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9d24`](#insn-00be9d24)

~~~json
{
  "source": "00be9d24",
  "target": "00be9d54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9d44`](#insn-00be9d44)

~~~json
{
  "source": "00be9d44",
  "target": "00be9d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9d50`](#insn-00be9d50)

~~~json
{
  "source": "00be9d50",
  "target": "00be9d18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9d5c`](#insn-00be9d5c)

~~~json
{
  "source": "00be9d5c",
  "target": "00be9cd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9d7c`](#insn-00be9d7c)

~~~json
{
  "source": "00be9d7c",
  "target": "00be9cdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9d94`](#insn-00be9d94)

~~~json
{
  "source": "00be9d94",
  "target": "00be9cdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9da4`](#insn-00be9da4)

~~~json
{
  "source": "00be9da4",
  "target": "00be9dc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9dbc`](#insn-00be9dbc)

~~~json
{
  "source": "00be9dbc",
  "target": "00be9d98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be9dc4`](#insn-00be9dc4)

~~~json
{
  "source": "00be9dc4",
  "target": "00be9cdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
