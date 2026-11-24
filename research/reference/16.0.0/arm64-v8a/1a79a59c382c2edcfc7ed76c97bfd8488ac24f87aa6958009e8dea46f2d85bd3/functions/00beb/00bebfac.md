# 00bebfac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0003.md#review-5501265d02ab7a3233eeb3c56eddf079)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bebfac",
  "name": "FUN_00bebfac",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c77fe0b7051ec24d55f5db37f2abf8fc7350bf1e20ba681202c7d319054e29be",
  "source_text_sha256": "c77fe0b7051ec24d55f5db37f2abf8fc7350bf1e20ba681202c7d319054e29be",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bebfac",
        "00bec2a7"
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

- [00be5088](../00be5/00be5088.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6283 bytes

~~~c

uint * FUN_00bebfac(uint *param_1,uint *param_2,uint *param_3)

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
                if ((long)uVar10 < (long)uVar14) goto LAB_00bebfd4;
                uVar2 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                puVar6 = param_1 + uVar2;
                puVar12 = puVar9;
                if ((long)uVar14 < lVar8) break;
                uVar16 = *puVar6;
                puVar13 = puVar6;
                uVar14 = uVar2;
                if (uVar16 < uVar17) goto LAB_00bebfd4;
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
LAB_00bebfd4:
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
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00bec0c8;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  puVar1 = param_1 + uVar10;
                  puVar6 = puVar15;
                  if ((long)uVar7 < lVar8) break;
                  uVar17 = *puVar1;
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                  if (uVar17 < uVar16) goto LAB_00bec0c8;
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
              } while (uVar16 <= uVar17);
LAB_00bec0c8:
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
<a id="insn-00bebfac"></a> `00bebfac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bebfb0"></a> `00bebfb0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bebfb4"></a> `00bebfb4` | `e0 0f 00 54` | b.eq 0x00bec1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bebfb8"></a> `00bebfb8` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bebfbc"></a> `00bebfbc` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bebfc0"></a> `00bebfc0` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebfc4"></a> `00bebfc4` | `0b 07 00 54` | b.lt 0x00bec0a4 | `CONDITIONAL_JUMP`
<a id="insn-00bebfc8"></a> `00bebfc8` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bebfcc"></a> `00bebfcc` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bebfd0"></a> `00bebfd0` | `05 00 00 14` | b 0x00bebfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebfd4"></a> `00bebfd4` | `0f 02 00 b9` | str w15,[x16] | `FALL_THROUGH`
<a id="insn-00bebfd8"></a> `00bebfd8` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bebfdc"></a> `00bebfdc` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bebfe0"></a> `00bebfe0` | `2d 06 00 54` | b.le 0x00bec0a4 | `CONDITIONAL_JUMP`
<a id="insn-00bebfe4"></a> `00bebfe4` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bebfe8"></a> `00bebfe8` | `8b ff ff 54` | b.lt 0x00bebfd8 | `CONDITIONAL_JUMP`
<a id="insn-00bebfec"></a> `00bebfec` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bebff0"></a> `00bebff0` | `8d f5 7f d3` | ubfiz x13,x12,#0x1,#0x3e | `FALL_THROUGH`
<a id="insn-00bebff4"></a> `00bebff4` | `8e f5 7f b3` | bfm x14,x12,#0x3f,#0x3d | `FALL_THROUGH`
<a id="insn-00bebff8"></a> `00bebff8` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bebffc"></a> `00bebffc` | `0d 08 0e 8b` | add x13,x0,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec000"></a> `00bec000` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bec004"></a> `00bec004` | `2a 01 00 54` | b.ge 0x00bec028 | `CONDITIONAL_JUMP`
<a id="insn-00bec008"></a> `00bec008` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bec00c"></a> `00bec00c` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec010"></a> `00bec010` | `03 4e 40 b8` | ldr w3,[x16, #0x4]! | `FALL_THROUGH`
<a id="insn-00bec014"></a> `00bec014` | `3f 02 03 6b` | cmp w17,w3 | `FALL_THROUGH`
<a id="insn-00bec018"></a> `00bec018` | `31 82 83 1a` | csel w17,w17,w3,hi | `FALL_THROUGH`
<a id="insn-00bec01c"></a> `00bec01c` | `0d 32 8d 9a` | csel x13,x16,x13,cc | `FALL_THROUGH`
<a id="insn-00bec020"></a> `00bec020` | `ee 31 8e 9a` | csel x14,x15,x14,cc | `FALL_THROUGH`
<a id="insn-00bec024"></a> `00bec024` | `02 00 00 14` | b 0x00bec02c | `UNCONDITIONAL_JUMP`
<a id="insn-00bec028"></a> `00bec028` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec02c"></a> `00bec02c` | `10 08 0c 8b` | add x16,x0,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec030"></a> `00bec030` | `0f 02 40 b9` | ldr w15,[x16] | `FALL_THROUGH`
<a id="insn-00bec034"></a> `00bec034` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec038"></a> `00bec038` | `62 01 00 54` | b.cs 0x00bec064 | `CONDITIONAL_JUMP`
<a id="insn-00bec03c"></a> `00bec03c` | `e7 ff ff 17` | b 0x00bebfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec040"></a> `00bec040` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bec044"></a> `00bec044` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec048"></a> `00bec048` | `85 4c 40 b8` | ldr w5,[x4, #0x4]! | `FALL_THROUGH`
<a id="insn-00bec04c"></a> `00bec04c` | `3f 02 05 6b` | cmp w17,w5 | `FALL_THROUGH`
<a id="insn-00bec050"></a> `00bec050` | `31 82 85 1a` | csel w17,w17,w5,hi | `FALL_THROUGH`
<a id="insn-00bec054"></a> `00bec054` | `8d 30 8d 9a` | csel x13,x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bec058"></a> `00bec058` | `ce 31 83 9a` | csel x14,x14,x3,cc | `FALL_THROUGH`
<a id="insn-00bec05c"></a> `00bec05c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec060"></a> `00bec060` | `a3 fb ff 54` | b.cc 0x00bebfd4 | `CONDITIONAL_JUMP`
<a id="insn-00bec064"></a> `00bec064` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bec068"></a> `00bec068` | `11 02 00 b9` | str w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec06c"></a> `00bec06c` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bec070"></a> `00bec070` | `2b fb ff 54` | b.lt 0x00bebfd4 | `CONDITIONAL_JUMP`
<a id="insn-00bec074"></a> `00bec074` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bec078"></a> `00bec078` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec07c"></a> `00bec07c` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec080"></a> `00bec080` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bec084"></a> `00bec084` | `0d 08 03 8b` | add x13,x0,x3, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec088"></a> `00bec088` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bec08c"></a> `00bec08c` | `ab fd ff 54` | b.lt 0x00bec040 | `CONDITIONAL_JUMP`
<a id="insn-00bec090"></a> `00bec090` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec094"></a> `00bec094` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bec098"></a> `00bec098` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec09c"></a> `00bec09c` | `42 fe ff 54` | b.cs 0x00bec064 | `CONDITIONAL_JUMP`
<a id="insn-00bec0a0"></a> `00bec0a0` | `cd ff ff 17` | b 0x00bebfd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec0a4"></a> `00bec0a4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bec0a8"></a> `00bec0a8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bec0ac"></a> `00bec0ac` | `c0 07 00 54` | b.eq 0x00bec1a4 | `CONDITIONAL_JUMP`
<a id="insn-00bec0b0"></a> `00bec0b0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec0b4"></a> `00bec0b4` | `0b 10 00 91` | add x11,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bec0b8"></a> `00bec0b8` | `0c 20 00 91` | add x12,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bec0bc"></a> `00bec0bc` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bec0c0"></a> `00bec0c0` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bec0c4"></a> `00bec0c4` | `05 00 00 14` | b 0x00bec0d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec0c8"></a> `00bec0c8` | `6f 00 00 b9` | str w15,[x3] | `FALL_THROUGH`
<a id="insn-00bec0cc"></a> `00bec0cc` | `ce 11 00 91` | add x14,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bec0d0"></a> `00bec0d0` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bec0d4"></a> `00bec0d4` | `60 06 00 54` | b.eq 0x00bec1a0 | `CONDITIONAL_JUMP`
<a id="insn-00bec0d8"></a> `00bec0d8` | `cf 01 40 b9` | ldr w15,[x14] | `FALL_THROUGH`
<a id="insn-00bec0dc"></a> `00bec0dc` | `10 00 40 b9` | ldr w16,[x0] | `FALL_THROUGH`
<a id="insn-00bec0e0"></a> `00bec0e0` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00bec0e4"></a> `00bec0e4` | `42 ff ff 54` | b.cs 0x00bec0cc | `CONDITIONAL_JUMP`
<a id="insn-00bec0e8"></a> `00bec0e8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec0ec"></a> `00bec0ec` | `d0 01 00 b9` | str w16,[x14] | `FALL_THROUGH`
<a id="insn-00bec0f0"></a> `00bec0f0` | `0f 00 00 b9` | str w15,[x0] | `FALL_THROUGH`
<a id="insn-00bec0f4"></a> `00bec0f4` | `cb fe ff 54` | b.lt 0x00bec0cc | `CONDITIONAL_JUMP`
<a id="insn-00bec0f8"></a> `00bec0f8` | `71 01 40 b9` | ldr w17,[x11] | `FALL_THROUGH`
<a id="insn-00bec0fc"></a> `00bec0fc` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bec100"></a> `00bec100` | `c1 00 00 54` | b.ne 0x00bec118 | `CONDITIONAL_JUMP`
<a id="insn-00bec104"></a> `00bec104` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00bec108"></a> `00bec108` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bec10c"></a> `00bec10c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec110"></a> `00bec110` | `e3 fd ff 54` | b.cc 0x00bec0cc | `CONDITIONAL_JUMP`
<a id="insn-00bec114"></a> `00bec114` | `08 00 00 14` | b 0x00bec134 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec118"></a> `00bec118` | `90 01 40 b9` | ldr w16,[x12] | `FALL_THROUGH`
<a id="insn-00bec11c"></a> `00bec11c` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00bec120"></a> `00bec120` | `31 82 90 1a` | csel w17,w17,w16,hi | `FALL_THROUGH`
<a id="insn-00bec124"></a> `00bec124` | `90 31 8b 9a` | csel x16,x12,x11,cc | `FALL_THROUGH`
<a id="insn-00bec128"></a> `00bec128` | `a4 25 8d 9a` | cinc x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bec12c"></a> `00bec12c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec130"></a> `00bec130` | `e3 fc ff 54` | b.cc 0x00bec0cc | `CONDITIONAL_JUMP`
<a id="insn-00bec134"></a> `00bec134` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bec138"></a> `00bec138` | `0a 00 00 14` | b 0x00bec160 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec13c"></a> `00bec13c` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00bec140"></a> `00bec140` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec144"></a> `00bec144` | `c7 4c 40 b8` | ldr w7,[x6, #0x4]! | `FALL_THROUGH`
<a id="insn-00bec148"></a> `00bec148` | `3f 02 07 6b` | cmp w17,w7 | `FALL_THROUGH`
<a id="insn-00bec14c"></a> `00bec14c` | `31 82 87 1a` | csel w17,w17,w7,hi | `FALL_THROUGH`
<a id="insn-00bec150"></a> `00bec150` | `d0 30 90 9a` | csel x16,x6,x16,cc | `FALL_THROUGH`
<a id="insn-00bec154"></a> `00bec154` | `84 30 85 9a` | csel x4,x4,x5,cc | `FALL_THROUGH`
<a id="insn-00bec158"></a> `00bec158` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec15c"></a> `00bec15c` | `63 fb ff 54` | b.cc 0x00bec0c8 | `CONDITIONAL_JUMP`
<a id="insn-00bec160"></a> `00bec160` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bec164"></a> `00bec164` | `71 00 00 b9` | str w17,[x3] | `FALL_THROUGH`
<a id="insn-00bec168"></a> `00bec168` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bec16c"></a> `00bec16c` | `eb fa ff 54` | b.lt 0x00bec0c8 | `CONDITIONAL_JUMP`
<a id="insn-00bec170"></a> `00bec170` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bec174"></a> `00bec174` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bec178"></a> `00bec178` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec17c"></a> `00bec17c` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bec180"></a> `00bec180` | `10 08 05 8b` | add x16,x0,x5, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec184"></a> `00bec184` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bec188"></a> `00bec188` | `ab fd ff 54` | b.lt 0x00bec13c | `CONDITIONAL_JUMP`
<a id="insn-00bec18c"></a> `00bec18c` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec190"></a> `00bec190` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bec194"></a> `00bec194` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec198"></a> `00bec198` | `42 fe ff 54` | b.cs 0x00bec160 | `CONDITIONAL_JUMP`
<a id="insn-00bec19c"></a> `00bec19c` | `cb ff ff 17` | b 0x00bec0c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec1a0"></a> `00bec1a0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bec1a4"></a> `00bec1a4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec1a8"></a> `00bec1a8` | `0a 01 00 54` | b.ge 0x00bec1c8 | `CONDITIONAL_JUMP`
<a id="insn-00bec1ac"></a> `00bec1ac` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bec1b0"></a> `00bec1b0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bec1b4"></a> `00bec1b4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bec1b8"></a> `00bec1b8` | `2a 01 00 b9` | str w10,[x9] | `FALL_THROUGH`
<a id="insn-00bec1bc"></a> `00bec1bc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec1c0"></a> `00bec1c0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bec1c4"></a> `00bec1c4` | `4d ff ff 54` | b.le 0x00bec1ac | `CONDITIONAL_JUMP`
<a id="insn-00bec1c8"></a> `00bec1c8` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec1cc"></a> `00bec1cc` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00bec1d0"></a> `00bec1d0` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bec1d4"></a> `00bec1d4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bec1d8"></a> `00bec1d8` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bec1dc"></a> `00bec1dc` | `0b 00 00 14` | b 0x00bec208 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec1e0"></a> `00bec1e0` | `0d 8e 40 b8` | ldr w13,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00bec1e4"></a> `00bec1e4` | `0f c2 5f b8` | ldur w15,[x16, #-0x4] | `FALL_THROUGH`
<a id="insn-00bec1e8"></a> `00bec1e8` | `ff 01 0d 6b` | cmp w15,w13 | `FALL_THROUGH`
<a id="insn-00bec1ec"></a> `00bec1ec` | `ef 81 8d 1a` | csel w15,w15,w13,hi | `FALL_THROUGH`
<a id="insn-00bec1f0"></a> `00bec1f0` | `09 32 89 9a` | csel x9,x16,x9,cc | `FALL_THROUGH`
<a id="insn-00bec1f4"></a> `00bec1f4` | `2d 32 8e 9a` | csel x13,x17,x14,cc | `FALL_THROUGH`
<a id="insn-00bec1f8"></a> `00bec1f8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bec1fc"></a> `00bec1fc` | `8f 01 00 b9` | str w15,[x12] | `FALL_THROUGH`
<a id="insn-00bec200"></a> `00bec200` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bec204"></a> `00bec204` | `8c 01 00 54` | b.gt 0x00bec234 | `CONDITIONAL_JUMP`
<a id="insn-00bec208"></a> `00bec208` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bec20c"></a> `00bec20c` | `90 09 0d 8b` | add x16,x12,x13, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec210"></a> `00bec210` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec214"></a> `00bec214` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec218"></a> `00bec218` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bec21c"></a> `00bec21c` | `09 12 00 91` | add x9,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00bec220"></a> `00bec220` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bec224"></a> `00bec224` | `eb fd ff 54` | b.lt 0x00bec1e0 | `CONDITIONAL_JUMP`
<a id="insn-00bec228"></a> `00bec228` | `2f 01 40 b9` | ldr w15,[x9] | `FALL_THROUGH`
<a id="insn-00bec22c"></a> `00bec22c` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bec230"></a> `00bec230` | `f2 ff ff 17` | b 0x00bec1f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec234"></a> `00bec234` | `21 10 00 d1` | sub x1,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00bec238"></a> `00bec238` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bec23c"></a> `00bec23c` | `e0 fb ff 54` | b.eq 0x00bec1b8 | `CONDITIONAL_JUMP`
<a id="insn-00bec240"></a> `00bec240` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bec244"></a> `00bec244` | `2c 00 40 b9` | ldr w12,[x1] | `FALL_THROUGH`
<a id="insn-00bec248"></a> `00bec248` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bec24c"></a> `00bec24c` | `6b fd 42 93` | asr x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec250"></a> `00bec250` | `2c 01 00 b9` | str w12,[x9] | `FALL_THROUGH`
<a id="insn-00bec254"></a> `00bec254` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00bec258"></a> `00bec258` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec25c"></a> `00bec25c` | `0b fb ff 54` | b.lt 0x00bec1bc | `CONDITIONAL_JUMP`
<a id="insn-00bec260"></a> `00bec260` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bec264"></a> `00bec264` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec268"></a> `00bec268` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec26c"></a> `00bec26c` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec270"></a> `00bec270` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec274"></a> `00bec274` | `42 fa ff 54` | b.cs 0x00bec1bc | `CONDITIONAL_JUMP`
<a id="insn-00bec278"></a> `00bec278` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bec27c"></a> `00bec27c` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bec280"></a> `00bec280` | `cd 01 00 b9` | str w13,[x14] | `FALL_THROUGH`
<a id="insn-00bec284"></a> `00bec284` | `ea 00 00 b4` | cbz x10,0x00bec2a0 | `CONDITIONAL_JUMP`
<a id="insn-00bec288"></a> `00bec288` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec28c"></a> `00bec28c` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec290"></a> `00bec290` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec294"></a> `00bec294` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec298"></a> `00bec298` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec29c"></a> `00bec29c` | `e3 fe ff 54` | b.cc 0x00bec278 | `CONDITIONAL_JUMP`
<a id="insn-00bec2a0"></a> `00bec2a0` | `2b 01 00 b9` | str w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec2a4"></a> `00bec2a4` | `c6 ff ff 17` | b 0x00bec1bc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bebfac`](#insn-00bebfac) 範囲 `[['00bebfac', '00bebfb7']]`
  - `CONDITIONAL_JUMP` [`00bebfb4`](#insn-00bebfb4) → [`00bec1b0`](#insn-00bec1b0)
  - `FALL_THROUGH` [`00bebfb4`](#insn-00bebfb4) → [`00bebfb8`](#insn-00bebfb8)
- ブロック [`00bebfb8`](#insn-00bebfb8) 範囲 `[['00bebfb8', '00bebfc7']]`
  - `CONDITIONAL_JUMP` [`00bebfc4`](#insn-00bebfc4) → [`00bec0a4`](#insn-00bec0a4)
  - `FALL_THROUGH` [`00bebfc4`](#insn-00bebfc4) → [`00bebfc8`](#insn-00bebfc8)
- ブロック [`00bebfc8`](#insn-00bebfc8) 範囲 `[['00bebfc8', '00bebfd3']]`
  - `UNCONDITIONAL_JUMP` [`00bebfd0`](#insn-00bebfd0) → [`00bebfe4`](#insn-00bebfe4)
- ブロック [`00bebfd4`](#insn-00bebfd4) 範囲 `[['00bebfd4', '00bebfd7']]`
  - `FALL_THROUGH` [`00bebfd4`](#insn-00bebfd4) → [`00bebfd8`](#insn-00bebfd8)
- ブロック [`00bebfd8`](#insn-00bebfd8) 範囲 `[['00bebfd8', '00bebfe3']]`
  - `CONDITIONAL_JUMP` [`00bebfe0`](#insn-00bebfe0) → [`00bec0a4`](#insn-00bec0a4)
  - `FALL_THROUGH` [`00bebfe0`](#insn-00bebfe0) → [`00bebfe4`](#insn-00bebfe4)
- ブロック [`00bebfe4`](#insn-00bebfe4) 範囲 `[['00bebfe4', '00bebfeb']]`
  - `CONDITIONAL_JUMP` [`00bebfe8`](#insn-00bebfe8) → [`00bebfd8`](#insn-00bebfd8)
  - `FALL_THROUGH` [`00bebfe8`](#insn-00bebfe8) → [`00bebfec`](#insn-00bebfec)
- ブロック [`00bebfec`](#insn-00bebfec) 範囲 `[['00bebfec', '00bec007']]`
  - `CONDITIONAL_JUMP` [`00bec004`](#insn-00bec004) → [`00bec028`](#insn-00bec028)
  - `FALL_THROUGH` [`00bec004`](#insn-00bec004) → [`00bec008`](#insn-00bec008)
- ブロック [`00bec008`](#insn-00bec008) 範囲 `[['00bec008', '00bec027']]`
  - `UNCONDITIONAL_JUMP` [`00bec024`](#insn-00bec024) → [`00bec02c`](#insn-00bec02c)
- ブロック [`00bec028`](#insn-00bec028) 範囲 `[['00bec028', '00bec02b']]`
  - `FALL_THROUGH` [`00bec028`](#insn-00bec028) → [`00bec02c`](#insn-00bec02c)
- ブロック [`00bec02c`](#insn-00bec02c) 範囲 `[['00bec02c', '00bec03b']]`
  - `CONDITIONAL_JUMP` [`00bec038`](#insn-00bec038) → [`00bec064`](#insn-00bec064)
  - `FALL_THROUGH` [`00bec038`](#insn-00bec038) → [`00bec03c`](#insn-00bec03c)
- ブロック [`00bec03c`](#insn-00bec03c) 範囲 `[['00bec03c', '00bec03f']]`
  - `UNCONDITIONAL_JUMP` [`00bec03c`](#insn-00bec03c) → [`00bebfd8`](#insn-00bebfd8)
- ブロック [`00bec040`](#insn-00bec040) 範囲 `[['00bec040', '00bec063']]`
  - `CONDITIONAL_JUMP` [`00bec060`](#insn-00bec060) → [`00bebfd4`](#insn-00bebfd4)
  - `FALL_THROUGH` [`00bec060`](#insn-00bec060) → [`00bec064`](#insn-00bec064)
- ブロック [`00bec064`](#insn-00bec064) 範囲 `[['00bec064', '00bec073']]`
  - `CONDITIONAL_JUMP` [`00bec070`](#insn-00bec070) → [`00bebfd4`](#insn-00bebfd4)
  - `FALL_THROUGH` [`00bec070`](#insn-00bec070) → [`00bec074`](#insn-00bec074)
- ブロック [`00bec074`](#insn-00bec074) 範囲 `[['00bec074', '00bec08f']]`
  - `CONDITIONAL_JUMP` [`00bec08c`](#insn-00bec08c) → [`00bec040`](#insn-00bec040)
  - `FALL_THROUGH` [`00bec08c`](#insn-00bec08c) → [`00bec090`](#insn-00bec090)
- ブロック [`00bec090`](#insn-00bec090) 範囲 `[['00bec090', '00bec09f']]`
  - `CONDITIONAL_JUMP` [`00bec09c`](#insn-00bec09c) → [`00bec064`](#insn-00bec064)
  - `FALL_THROUGH` [`00bec09c`](#insn-00bec09c) → [`00bec0a0`](#insn-00bec0a0)
- ブロック [`00bec0a0`](#insn-00bec0a0) 範囲 `[['00bec0a0', '00bec0a3']]`
  - `UNCONDITIONAL_JUMP` [`00bec0a0`](#insn-00bec0a0) → [`00bebfd4`](#insn-00bebfd4)
- ブロック [`00bec0a4`](#insn-00bec0a4) 範囲 `[['00bec0a4', '00bec0af']]`
  - `CONDITIONAL_JUMP` [`00bec0ac`](#insn-00bec0ac) → [`00bec1a4`](#insn-00bec1a4)
  - `FALL_THROUGH` [`00bec0ac`](#insn-00bec0ac) → [`00bec0b0`](#insn-00bec0b0)
- ブロック [`00bec0b0`](#insn-00bec0b0) 範囲 `[['00bec0b0', '00bec0c7']]`
  - `UNCONDITIONAL_JUMP` [`00bec0c4`](#insn-00bec0c4) → [`00bec0d8`](#insn-00bec0d8)
- ブロック [`00bec0c8`](#insn-00bec0c8) 範囲 `[['00bec0c8', '00bec0cb']]`
  - `FALL_THROUGH` [`00bec0c8`](#insn-00bec0c8) → [`00bec0cc`](#insn-00bec0cc)
- ブロック [`00bec0cc`](#insn-00bec0cc) 範囲 `[['00bec0cc', '00bec0d7']]`
  - `CONDITIONAL_JUMP` [`00bec0d4`](#insn-00bec0d4) → [`00bec1a0`](#insn-00bec1a0)
  - `FALL_THROUGH` [`00bec0d4`](#insn-00bec0d4) → [`00bec0d8`](#insn-00bec0d8)
- ブロック [`00bec0d8`](#insn-00bec0d8) 範囲 `[['00bec0d8', '00bec0e7']]`
  - `CONDITIONAL_JUMP` [`00bec0e4`](#insn-00bec0e4) → [`00bec0cc`](#insn-00bec0cc)
  - `FALL_THROUGH` [`00bec0e4`](#insn-00bec0e4) → [`00bec0e8`](#insn-00bec0e8)
- ブロック [`00bec0e8`](#insn-00bec0e8) 範囲 `[['00bec0e8', '00bec0f7']]`
  - `CONDITIONAL_JUMP` [`00bec0f4`](#insn-00bec0f4) → [`00bec0cc`](#insn-00bec0cc)
  - `FALL_THROUGH` [`00bec0f4`](#insn-00bec0f4) → [`00bec0f8`](#insn-00bec0f8)
- ブロック [`00bec0f8`](#insn-00bec0f8) 範囲 `[['00bec0f8', '00bec103']]`
  - `CONDITIONAL_JUMP` [`00bec100`](#insn-00bec100) → [`00bec118`](#insn-00bec118)
  - `FALL_THROUGH` [`00bec100`](#insn-00bec100) → [`00bec104`](#insn-00bec104)
- ブロック [`00bec104`](#insn-00bec104) 範囲 `[['00bec104', '00bec113']]`
  - `CONDITIONAL_JUMP` [`00bec110`](#insn-00bec110) → [`00bec0cc`](#insn-00bec0cc)
  - `FALL_THROUGH` [`00bec110`](#insn-00bec110) → [`00bec114`](#insn-00bec114)
- ブロック [`00bec114`](#insn-00bec114) 範囲 `[['00bec114', '00bec117']]`
  - `UNCONDITIONAL_JUMP` [`00bec114`](#insn-00bec114) → [`00bec134`](#insn-00bec134)
- ブロック [`00bec118`](#insn-00bec118) 範囲 `[['00bec118', '00bec133']]`
  - `CONDITIONAL_JUMP` [`00bec130`](#insn-00bec130) → [`00bec0cc`](#insn-00bec0cc)
  - `FALL_THROUGH` [`00bec130`](#insn-00bec130) → [`00bec134`](#insn-00bec134)
- ブロック [`00bec134`](#insn-00bec134) 範囲 `[['00bec134', '00bec13b']]`
  - `UNCONDITIONAL_JUMP` [`00bec138`](#insn-00bec138) → [`00bec160`](#insn-00bec160)
- ブロック [`00bec13c`](#insn-00bec13c) 範囲 `[['00bec13c', '00bec15f']]`
  - `CONDITIONAL_JUMP` [`00bec15c`](#insn-00bec15c) → [`00bec0c8`](#insn-00bec0c8)
  - `FALL_THROUGH` [`00bec15c`](#insn-00bec15c) → [`00bec160`](#insn-00bec160)
- ブロック [`00bec160`](#insn-00bec160) 範囲 `[['00bec160', '00bec16f']]`
  - `CONDITIONAL_JUMP` [`00bec16c`](#insn-00bec16c) → [`00bec0c8`](#insn-00bec0c8)
  - `FALL_THROUGH` [`00bec16c`](#insn-00bec16c) → [`00bec170`](#insn-00bec170)
- ブロック [`00bec170`](#insn-00bec170) 範囲 `[['00bec170', '00bec18b']]`
  - `CONDITIONAL_JUMP` [`00bec188`](#insn-00bec188) → [`00bec13c`](#insn-00bec13c)
  - `FALL_THROUGH` [`00bec188`](#insn-00bec188) → [`00bec18c`](#insn-00bec18c)
- ブロック [`00bec18c`](#insn-00bec18c) 範囲 `[['00bec18c', '00bec19b']]`
  - `CONDITIONAL_JUMP` [`00bec198`](#insn-00bec198) → [`00bec160`](#insn-00bec160)
  - `FALL_THROUGH` [`00bec198`](#insn-00bec198) → [`00bec19c`](#insn-00bec19c)
- ブロック [`00bec19c`](#insn-00bec19c) 範囲 `[['00bec19c', '00bec19f']]`
  - `UNCONDITIONAL_JUMP` [`00bec19c`](#insn-00bec19c) → [`00bec0c8`](#insn-00bec0c8)
- ブロック [`00bec1a0`](#insn-00bec1a0) 範囲 `[['00bec1a0', '00bec1a3']]`
  - `FALL_THROUGH` [`00bec1a0`](#insn-00bec1a0) → [`00bec1a4`](#insn-00bec1a4)
- ブロック [`00bec1a4`](#insn-00bec1a4) 範囲 `[['00bec1a4', '00bec1ab']]`
  - `CONDITIONAL_JUMP` [`00bec1a8`](#insn-00bec1a8) → [`00bec1c8`](#insn-00bec1c8)
  - `FALL_THROUGH` [`00bec1a8`](#insn-00bec1a8) → [`00bec1ac`](#insn-00bec1ac)
- ブロック [`00bec1ac`](#insn-00bec1ac) 範囲 `[['00bec1ac', '00bec1af']]`
  - `FALL_THROUGH` [`00bec1ac`](#insn-00bec1ac) → [`00bec1b0`](#insn-00bec1b0)
- ブロック [`00bec1b0`](#insn-00bec1b0) 範囲 `[['00bec1b0', '00bec1b7']]`
- ブロック [`00bec1b8`](#insn-00bec1b8) 範囲 `[['00bec1b8', '00bec1bb']]`
  - `FALL_THROUGH` [`00bec1b8`](#insn-00bec1b8) → [`00bec1bc`](#insn-00bec1bc)
- ブロック [`00bec1bc`](#insn-00bec1bc) 範囲 `[['00bec1bc', '00bec1c7']]`
  - `CONDITIONAL_JUMP` [`00bec1c4`](#insn-00bec1c4) → [`00bec1ac`](#insn-00bec1ac)
  - `FALL_THROUGH` [`00bec1c4`](#insn-00bec1c4) → [`00bec1c8`](#insn-00bec1c8)
- ブロック [`00bec1c8`](#insn-00bec1c8) 範囲 `[['00bec1c8', '00bec1df']]`
  - `UNCONDITIONAL_JUMP` [`00bec1dc`](#insn-00bec1dc) → [`00bec208`](#insn-00bec208)
- ブロック [`00bec1e0`](#insn-00bec1e0) 範囲 `[['00bec1e0', '00bec1f7']]`
  - `FALL_THROUGH` [`00bec1f4`](#insn-00bec1f4) → [`00bec1f8`](#insn-00bec1f8)
- ブロック [`00bec1f8`](#insn-00bec1f8) 範囲 `[['00bec1f8', '00bec207']]`
  - `CONDITIONAL_JUMP` [`00bec204`](#insn-00bec204) → [`00bec234`](#insn-00bec234)
  - `FALL_THROUGH` [`00bec204`](#insn-00bec204) → [`00bec208`](#insn-00bec208)
- ブロック [`00bec208`](#insn-00bec208) 範囲 `[['00bec208', '00bec227']]`
  - `CONDITIONAL_JUMP` [`00bec224`](#insn-00bec224) → [`00bec1e0`](#insn-00bec1e0)
  - `FALL_THROUGH` [`00bec224`](#insn-00bec224) → [`00bec228`](#insn-00bec228)
- ブロック [`00bec228`](#insn-00bec228) 範囲 `[['00bec228', '00bec233']]`
  - `UNCONDITIONAL_JUMP` [`00bec230`](#insn-00bec230) → [`00bec1f8`](#insn-00bec1f8)
- ブロック [`00bec234`](#insn-00bec234) 範囲 `[['00bec234', '00bec23f']]`
  - `CONDITIONAL_JUMP` [`00bec23c`](#insn-00bec23c) → [`00bec1b8`](#insn-00bec1b8)
  - `FALL_THROUGH` [`00bec23c`](#insn-00bec23c) → [`00bec240`](#insn-00bec240)
- ブロック [`00bec240`](#insn-00bec240) 範囲 `[['00bec240', '00bec25f']]`
  - `CONDITIONAL_JUMP` [`00bec25c`](#insn-00bec25c) → [`00bec1bc`](#insn-00bec1bc)
  - `FALL_THROUGH` [`00bec25c`](#insn-00bec25c) → [`00bec260`](#insn-00bec260)
- ブロック [`00bec260`](#insn-00bec260) 範囲 `[['00bec260', '00bec277']]`
  - `CONDITIONAL_JUMP` [`00bec274`](#insn-00bec274) → [`00bec1bc`](#insn-00bec1bc)
  - `FALL_THROUGH` [`00bec274`](#insn-00bec274) → [`00bec278`](#insn-00bec278)
- ブロック [`00bec278`](#insn-00bec278) 範囲 `[['00bec278', '00bec287']]`
  - `CONDITIONAL_JUMP` [`00bec284`](#insn-00bec284) → [`00bec2a0`](#insn-00bec2a0)
  - `FALL_THROUGH` [`00bec284`](#insn-00bec284) → [`00bec288`](#insn-00bec288)
- ブロック [`00bec288`](#insn-00bec288) 範囲 `[['00bec288', '00bec29f']]`
  - `CONDITIONAL_JUMP` [`00bec29c`](#insn-00bec29c) → [`00bec278`](#insn-00bec278)
  - `FALL_THROUGH` [`00bec29c`](#insn-00bec29c) → [`00bec2a0`](#insn-00bec2a0)
- ブロック [`00bec2a0`](#insn-00bec2a0) 範囲 `[['00bec2a0', '00bec2a7']]`
  - `UNCONDITIONAL_JUMP` [`00bec2a4`](#insn-00bec2a4) → [`00bec1bc`](#insn-00bec1bc)

## 命令位置別の参照

- [`00bebfb4`](#insn-00bebfb4) → [`00bec1b0`](#insn-00bec1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfc4`](#insn-00bebfc4) → [`00bec0a4`](#insn-00bec0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfd0`](#insn-00bebfd0) → [`00bebfe4`](#insn-00bebfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfe0`](#insn-00bebfe0) → [`00bec0a4`](#insn-00bec0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfe8`](#insn-00bebfe8) → [`00bebfd8`](#insn-00bebfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec004`](#insn-00bec004) → [`00bec028`](#insn-00bec028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec024`](#insn-00bec024) → [`00bec02c`](#insn-00bec02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec038`](#insn-00bec038) → [`00bec064`](#insn-00bec064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec03c`](#insn-00bec03c) → [`00bebfd8`](#insn-00bebfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec060`](#insn-00bec060) → [`00bebfd4`](#insn-00bebfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec070`](#insn-00bec070) → [`00bebfd4`](#insn-00bebfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec08c`](#insn-00bec08c) → [`00bec040`](#insn-00bec040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec09c`](#insn-00bec09c) → [`00bec064`](#insn-00bec064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0a0`](#insn-00bec0a0) → [`00bebfd4`](#insn-00bebfd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0ac`](#insn-00bec0ac) → [`00bec1a4`](#insn-00bec1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0c4`](#insn-00bec0c4) → [`00bec0d8`](#insn-00bec0d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0d4`](#insn-00bec0d4) → [`00bec1a0`](#insn-00bec1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0e4`](#insn-00bec0e4) → [`00bec0cc`](#insn-00bec0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0f4`](#insn-00bec0f4) → [`00bec0cc`](#insn-00bec0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec100`](#insn-00bec100) → [`00bec118`](#insn-00bec118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec110`](#insn-00bec110) → [`00bec0cc`](#insn-00bec0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec114`](#insn-00bec114) → [`00bec134`](#insn-00bec134) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec130`](#insn-00bec130) → [`00bec0cc`](#insn-00bec0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec138`](#insn-00bec138) → [`00bec160`](#insn-00bec160) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec15c`](#insn-00bec15c) → [`00bec0c8`](#insn-00bec0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec16c`](#insn-00bec16c) → [`00bec0c8`](#insn-00bec0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec188`](#insn-00bec188) → [`00bec13c`](#insn-00bec13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec198`](#insn-00bec198) → [`00bec160`](#insn-00bec160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec19c`](#insn-00bec19c) → [`00bec0c8`](#insn-00bec0c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1a8`](#insn-00bec1a8) → [`00bec1c8`](#insn-00bec1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1c4`](#insn-00bec1c4) → [`00bec1ac`](#insn-00bec1ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1dc`](#insn-00bec1dc) → [`00bec208`](#insn-00bec208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec204`](#insn-00bec204) → [`00bec234`](#insn-00bec234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec224`](#insn-00bec224) → [`00bec1e0`](#insn-00bec1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec230`](#insn-00bec230) → [`00bec1f8`](#insn-00bec1f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec23c`](#insn-00bec23c) → [`00bec1b8`](#insn-00bec1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec25c`](#insn-00bec25c) → [`00bec1bc`](#insn-00bec1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec274`](#insn-00bec274) → [`00bec1bc`](#insn-00bec1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec284`](#insn-00bec284) → [`00bec2a0`](#insn-00bec2a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec29c`](#insn-00bec29c) → [`00bec278`](#insn-00bec278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2a4`](#insn-00bec2a4) → [`00bec1bc`](#insn-00bec1bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bebfb4`](#insn-00bebfb4)

~~~json
{
  "source": "00bebfb4",
  "target": "00bec1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfc4`](#insn-00bebfc4)

~~~json
{
  "source": "00bebfc4",
  "target": "00bec0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfd0`](#insn-00bebfd0)

~~~json
{
  "source": "00bebfd0",
  "target": "00bebfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfe0`](#insn-00bebfe0)

~~~json
{
  "source": "00bebfe0",
  "target": "00bec0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfe8`](#insn-00bebfe8)

~~~json
{
  "source": "00bebfe8",
  "target": "00bebfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec004`](#insn-00bec004)

~~~json
{
  "source": "00bec004",
  "target": "00bec028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec024`](#insn-00bec024)

~~~json
{
  "source": "00bec024",
  "target": "00bec02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec038`](#insn-00bec038)

~~~json
{
  "source": "00bec038",
  "target": "00bec064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec03c`](#insn-00bec03c)

~~~json
{
  "source": "00bec03c",
  "target": "00bebfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec060`](#insn-00bec060)

~~~json
{
  "source": "00bec060",
  "target": "00bebfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec070`](#insn-00bec070)

~~~json
{
  "source": "00bec070",
  "target": "00bebfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec08c`](#insn-00bec08c)

~~~json
{
  "source": "00bec08c",
  "target": "00bec040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec09c`](#insn-00bec09c)

~~~json
{
  "source": "00bec09c",
  "target": "00bec064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0a0`](#insn-00bec0a0)

~~~json
{
  "source": "00bec0a0",
  "target": "00bebfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0ac`](#insn-00bec0ac)

~~~json
{
  "source": "00bec0ac",
  "target": "00bec1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0c4`](#insn-00bec0c4)

~~~json
{
  "source": "00bec0c4",
  "target": "00bec0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0d4`](#insn-00bec0d4)

~~~json
{
  "source": "00bec0d4",
  "target": "00bec1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0e4`](#insn-00bec0e4)

~~~json
{
  "source": "00bec0e4",
  "target": "00bec0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0f4`](#insn-00bec0f4)

~~~json
{
  "source": "00bec0f4",
  "target": "00bec0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec100`](#insn-00bec100)

~~~json
{
  "source": "00bec100",
  "target": "00bec118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec110`](#insn-00bec110)

~~~json
{
  "source": "00bec110",
  "target": "00bec0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec114`](#insn-00bec114)

~~~json
{
  "source": "00bec114",
  "target": "00bec134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec130`](#insn-00bec130)

~~~json
{
  "source": "00bec130",
  "target": "00bec0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec138`](#insn-00bec138)

~~~json
{
  "source": "00bec138",
  "target": "00bec160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec15c`](#insn-00bec15c)

~~~json
{
  "source": "00bec15c",
  "target": "00bec0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec16c`](#insn-00bec16c)

~~~json
{
  "source": "00bec16c",
  "target": "00bec0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec188`](#insn-00bec188)

~~~json
{
  "source": "00bec188",
  "target": "00bec13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec198`](#insn-00bec198)

~~~json
{
  "source": "00bec198",
  "target": "00bec160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec19c`](#insn-00bec19c)

~~~json
{
  "source": "00bec19c",
  "target": "00bec0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1a8`](#insn-00bec1a8)

~~~json
{
  "source": "00bec1a8",
  "target": "00bec1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1c4`](#insn-00bec1c4)

~~~json
{
  "source": "00bec1c4",
  "target": "00bec1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1dc`](#insn-00bec1dc)

~~~json
{
  "source": "00bec1dc",
  "target": "00bec208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec204`](#insn-00bec204)

~~~json
{
  "source": "00bec204",
  "target": "00bec234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec224`](#insn-00bec224)

~~~json
{
  "source": "00bec224",
  "target": "00bec1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec230`](#insn-00bec230)

~~~json
{
  "source": "00bec230",
  "target": "00bec1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec23c`](#insn-00bec23c)

~~~json
{
  "source": "00bec23c",
  "target": "00bec1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec25c`](#insn-00bec25c)

~~~json
{
  "source": "00bec25c",
  "target": "00bec1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec274`](#insn-00bec274)

~~~json
{
  "source": "00bec274",
  "target": "00bec1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec284`](#insn-00bec284)

~~~json
{
  "source": "00bec284",
  "target": "00bec2a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec29c`](#insn-00bec29c)

~~~json
{
  "source": "00bec29c",
  "target": "00bec278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2a4`](#insn-00bec2a4)

~~~json
{
  "source": "00bec2a4",
  "target": "00bec1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
