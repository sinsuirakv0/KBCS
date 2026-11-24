# 00bbeec8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbee2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbee2c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-ee9fa37bf3cacad8c41851d63aadfbc3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbfebc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfebc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-a726f899b1779e46eddadf8d2434c1b2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbeec8",
  "name": "_ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 3496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a304915e7765e133441ae9e15e99f388671a7bae4f58c114aa4888bf9bfd93a",
  "source_text_sha256": "4a304915e7765e133441ae9e15e99f388671a7bae4f58c114aa4888bf9bfd93a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbeec8",
        "00bbfc6f"
      ]
    ],
    "bytes_sha256": "b368f1600c7afb0b96097a45cd7f699a2155447ac0c113b2f4f5d9e8124b2704",
    "instruction_count": 874,
    "instruction_bytes": 3496,
    "body_bytes": 3496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d5b0](../00c5d/00c5d5b0.md)

## 呼び出し先

- [00c5d5c0](../00c5d/00c5d5c0.md)
- [00c5d600](../00c5d/00c5d600.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 30766 bytes

~~~c

undefined8
_ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  ulong uVar3;
  uint *puVar4;
  uint *puVar5;
  ushort uVar6;
  int iVar7;
  ulong uVar8;
  long lVar9;
  ulong uVar10;
  long lVar11;
  ulong uVar12;
  ulong uVar13;
  ushort *puVar14;
  
  lVar11 = *param_2;
  uVar13 = (long)param_1 - lVar11;
  if (((uVar13 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar10 = param_2[1];
    if (uVar10 < 5) {
      return 0;
    }
    uVar12 = uVar10 - 4;
    if (uVar12 < uVar13) {
      return 0;
    }
    iVar7 = *param_1;
    uVar1 = (int)param_2[7] + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar8 = uVar13 - (long)iVar7, (uVar8 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar8 <= uVar10 - 2)) {
      uVar6 = *(ushort *)(lVar11 + uVar8);
      if ((((uVar6 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar6 & 1) == 0)) {
        if (uVar10 <= uVar6) {
          return 0;
        }
        if (uVar10 - uVar6 < uVar8) {
          return 0;
        }
        puVar14 = (ushort *)((long)param_1 - (long)*param_1);
        uVar6 = *puVar14;
        lVar9 = -(long)*param_1;
        if (4 < uVar6) {
          if ((ulong)puVar14[2] != 0) {
            uVar8 = uVar13 + puVar14[2];
            if ((uVar8 & 3) == 0) {
              if (uVar12 < uVar8) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar12 < uVar8) {
                return 0;
              }
            }
            if ((int)*(uint *)(lVar11 + uVar8) < 1) {
              return 0;
            }
            if (uVar10 - 1 < uVar8 + *(uint *)(lVar11 + uVar8)) {
              return 0;
            }
          }
          if (((ulong)puVar14[2] != 0) &&
             (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[2]),
             puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
            uVar8 = (long)puVar4 - lVar11;
            if ((uVar8 & 3) == 0) {
              if (uVar12 < uVar8) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar12 < uVar8) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar4) {
              return 0;
            }
            uVar3 = (ulong)*puVar4 + 4;
            if (uVar10 - 1 < uVar3 + uVar8) {
              return 0;
            }
            if (uVar10 <= uVar3) {
              return 0;
            }
            if (uVar10 - uVar3 < uVar8) {
              return 0;
            }
            if (*(char *)(lVar11 + uVar3 + uVar8) != '\0') {
              return 0;
            }
          }
          if (6 < uVar6) {
            if ((ulong)puVar14[3] != 0) {
              uVar8 = uVar13 + puVar14[3];
              if ((uVar8 & 3) == 0) {
                if (uVar12 < uVar8) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar12 < uVar8) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar11 + uVar8) < 1) {
                return 0;
              }
              if (uVar10 - 1 < uVar8 + *(uint *)(lVar11 + uVar8)) {
                return 0;
              }
            }
            if (((ulong)puVar14[3] != 0) &&
               (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[3]),
               puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
              uVar8 = (long)puVar4 - lVar11;
              if ((uVar8 & 3) == 0) {
                if (uVar12 < uVar8) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar12 < uVar8) {
                  return 0;
                }
              }
              if ((ulong)param_2[4] <= (ulong)*puVar4) {
                return 0;
              }
              uVar3 = (ulong)*puVar4 + 4;
              if (uVar10 - 1 < uVar3 + uVar8) {
                return 0;
              }
              if (uVar10 <= uVar3) {
                return 0;
              }
              if (uVar10 - uVar3 < uVar8) {
                return 0;
              }
              if (*(char *)(lVar11 + uVar3 + uVar8) != '\0') {
                return 0;
              }
            }
            if (8 < uVar6) {
                    /* try { // try from 00bbf164 to 00cbf16f has its CatchHandler @ 00bbf4f4 */
              if ((ulong)puVar14[4] != 0) {
                uVar8 = uVar13 + puVar14[4];
                if ((uVar8 & 3) == 0) {
                  if (uVar12 < uVar8) {
                    return 0;
                  }
                }
                else {
                  if ((char)param_2[3] != '\0') {
                    return 0;
                  }
                  if (uVar12 < uVar8) {
                    return 0;
                  }
                }
                    /* try { // try from 00bbf194 to 00cbf1bb has its CatchHandler @ 00bbf4b0 */
                if ((int)*(uint *)(lVar11 + uVar8) < 1) {
                  return 0;
                }
                if (uVar10 - 1 < uVar8 + *(uint *)(lVar11 + uVar8)) {
                  return 0;
                }
              }
                    /* try { // try from 00bbf1bc to 00cbf407 has its CatchHandler @ 00bbe868 */
              if (((ulong)puVar14[4] != 0) &&
                 (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[4]),
                 puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
                uVar8 = (long)puVar4 - lVar11;
                if ((uVar8 & 3) == 0) {
                  if (uVar12 < uVar8) {
                    return 0;
                  }
                }
                else {
                  if ((char)param_2[3] != '\0') {
                    return 0;
                  }
                  if (uVar12 < uVar8) {
                    return 0;
                  }
                }
                if ((ulong)param_2[4] <= (ulong)*puVar4) {
                  return 0;
                }
                uVar3 = (ulong)*puVar4 + 4;
                if (uVar10 - 1 < uVar3 + uVar8) {
                  return 0;
                }
                if (uVar10 <= uVar3) {
                  return 0;
                }
                if (uVar10 - uVar3 < uVar8) {
                  return 0;
                }
                if (*(char *)(lVar11 + uVar3 + uVar8) != '\0') {
                  return 0;
                }
              }
              if (10 < uVar6) {
                if ((ulong)puVar14[5] != 0) {
                  uVar13 = uVar13 + puVar14[5];
                  if ((uVar13 & 3) == 0) {
                    if (uVar12 < uVar13) {
                      return 0;
                    }
                  }
                  else {
                    if ((char)param_2[3] != '\0') {
                      return 0;
                    }
                    if (uVar12 < uVar13) {
                      return 0;
                    }
                  }
                  if ((int)*(uint *)(lVar11 + uVar13) < 1) {
                    return 0;
                  }
                  if (uVar10 - 1 < uVar13 + *(uint *)(lVar11 + uVar13)) {
                    return 0;
                  }
                }
                if ((ulong)puVar14[5] != 0) {
                  puVar5 = (uint *)((long)param_1 + (ulong)puVar14[5]);
                  puVar4 = (uint *)((long)puVar5 + (ulong)*puVar5);
                  if (puVar4 != (uint *)0x0) {
                    uVar13 = (long)puVar4 - lVar11;
                    if ((uVar13 & 3) == 0) {
                      if (uVar12 < uVar13) {
                        return 0;
                      }
                    }
                    else {
                      if ((char)param_2[3] != '\0') {
                        return 0;
                      }
                      if (uVar12 < uVar13) {
                        return 0;
                      }
                    }
                    if ((ulong)param_2[4] >> 2 <= (ulong)*puVar4) {
                      return 0;
                    }
                    uVar12 = (ulong)*puVar4 * 4 + 4;
                    if (uVar10 <= uVar12) {
                      return 0;
                    }
                    if (uVar10 - uVar12 < uVar13) {
                      return 0;
                    }
                  }
                  puVar5 = (uint *)((long)puVar5 + (ulong)*puVar5);
                  if ((puVar5 != (uint *)0x0) && (*puVar5 != 0)) {
                    uVar10 = 0;
                    uVar13 = 0;
                    do {
                      puVar4 = (uint *)((long)puVar5 + (uVar10 & 0xfffffffc) + 4);
                      uVar12 = _ZNK3com6google8firebase9messaging3cpp8DataPair6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                         ((long)puVar4 + (ulong)*puVar4,param_2);
                      if ((uVar12 & 1) == 0) {
                        return 0;
                      }
                      uVar13 = uVar13 + 1;
                      uVar10 = uVar10 + 4;
                    } while (uVar13 < *puVar5);
                    lVar9 = -(long)*param_1;
                  }
                }
              }
            }
          }
        }
        puVar14 = (ushort *)((long)param_1 + lVar9);
        uVar6 = *puVar14;
        if (0xc < uVar6) {
          if ((ulong)puVar14[6] != 0) {
            uVar13 = (long)param_1 + ((ulong)puVar14[6] - *param_2);
            if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
              return 0;
            }
            uVar10 = param_2[1];
            if (uVar10 < 5) {
              return 0;
            }
            if (uVar10 - 4 < uVar13) {
              return 0;
            }
            uVar1 = *(uint *)(*param_2 + uVar13);
            if ((int)uVar1 < 1) {
              return 0;
            }
            if (uVar10 - 1 < uVar13 + uVar1) {
              return 0;
            }
          }
          if (((ulong)puVar14[6] != 0) &&
             (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[6]),
             puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
            uVar13 = (long)puVar4 - *param_2;
            if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
              return 0;
            }
            uVar10 = param_2[1];
            if (uVar10 < 5) {
              return 0;
            }
                    /* try { // try from 00bbf408 to 00cbf40f has its CatchHandler @ 00bbf424 */
            if (uVar10 - 4 < uVar13) {
              return 0;
            }
                    /* catch() { ... } // from try @ 00bbecac with catch @ 00bbf410
                       try { // try from 00bbf410 to 00cbf51f has its CatchHandler @ 00bbe868 */
            if ((ulong)param_2[4] <= (ulong)*puVar4) {
              return 0;
            }
                    /* catch() { ... } // from try @ 00bbecdc with catch @ 00bbf420 */
            uVar12 = (ulong)*puVar4 + 4;
                    /* catch() { ... } // from try @ 00bbf408 with catch @ 00bbf424 */
                    /* catch() { ... } // from try @ 00bbeda4 with catch @ 00bbf428 */
            if (uVar10 <= uVar12) {
              return 0;
            }
            if (uVar10 - uVar12 < uVar13) {
              return 0;
            }
          }
          if (0xe < uVar6) {
            if ((ulong)puVar14[7] != 0) {
                    /* catch() { ... } // from try @ 00bbec9c with catch @ 00bbf450 */
              uVar13 = (long)param_1 + ((ulong)puVar14[7] - *param_2);
                    /* catch() { ... } // from try @ 00bbebbc with catch @ 00bbf454 */
              if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                return 0;
              }
              uVar10 = param_2[1];
              if (uVar10 < 5) {
                return 0;
              }
              if (uVar10 - 4 < uVar13) {
                return 0;
              }
              uVar1 = *(uint *)(*param_2 + uVar13);
              if ((int)uVar1 < 1) {
                return 0;
              }
                    /* catch() { ... } // from try @ 00bbeb88 with catch @ 00bbf498 */
              if (uVar10 - 1 < uVar13 + uVar1) {
                return 0;
              }
            }
                    /* catch() { ... } // from try @ 00bbf194 with catch @ 00bbf4b0 */
            if (((ulong)puVar14[7] != 0) &&
               (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[7]),
               puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
              uVar13 = (long)puVar4 - *param_2;
              if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                return 0;
              }
              uVar10 = param_2[1];
              if (uVar10 < 5) {
                return 0;
              }
              if (uVar10 - 4 < uVar13) {
                return 0;
              }
                    /* catch() { ... } // from try @ 00bbf164 with catch @ 00bbf4f4 */
              if ((ulong)param_2[4] <= (ulong)*puVar4) {
                return 0;
              }
              uVar12 = (ulong)*puVar4 + 4;
              if (uVar10 - 1 < uVar12 + uVar13) {
                return 0;
              }
              if (uVar10 <= uVar12) {
                return 0;
              }
              if (uVar10 - uVar12 < uVar13) {
                return 0;
              }
              if (*(char *)(*param_2 + uVar12 + uVar13) != '\0') {
                return 0;
              }
            }
            if (0x10 < uVar6) {
              if ((ulong)puVar14[8] != 0) {
                uVar13 = (long)param_1 + ((ulong)puVar14[8] - *param_2);
                if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                  return 0;
                }
                uVar10 = param_2[1];
                if (uVar10 < 5) {
                  return 0;
                }
                if (uVar10 - 4 < uVar13) {
                  return 0;
                }
                uVar1 = *(uint *)(*param_2 + uVar13);
                if ((int)uVar1 < 1) {
                  return 0;
                }
                if (uVar10 - 1 < uVar13 + uVar1) {
                  return 0;
                }
              }
              if (((ulong)puVar14[8] != 0) &&
                 (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[8]),
                 puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
                uVar13 = (long)puVar4 - *param_2;
                if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                  return 0;
                }
                uVar10 = param_2[1];
                if (uVar10 < 5) {
                  return 0;
                }
                if (uVar10 - 4 < uVar13) {
                  return 0;
                }
                if ((ulong)param_2[4] <= (ulong)*puVar4) {
                  return 0;
                }
                uVar12 = (ulong)*puVar4 + 4;
                if (uVar10 - 1 < uVar12 + uVar13) {
                  return 0;
                }
                if (uVar10 <= uVar12) {
                  return 0;
                }
                if (uVar10 - uVar12 < uVar13) {
                  return 0;
                }
                if (*(char *)(*param_2 + uVar12 + uVar13) != '\0') {
                  return 0;
                }
              }
              if (0x12 < uVar6) {
                if ((ulong)puVar14[9] != 0) {
                  uVar13 = (long)param_1 + ((ulong)puVar14[9] - *param_2);
                  if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                    return 0;
                  }
                  uVar10 = param_2[1];
                  if (uVar10 < 5) {
                    return 0;
                  }
                  if (uVar10 - 4 < uVar13) {
                    return 0;
                  }
                  uVar1 = *(uint *)(*param_2 + uVar13);
                  if ((int)uVar1 < 1) {
                    return 0;
                  }
                  if (uVar10 - 1 < uVar13 + uVar1) {
                    return 0;
                  }
                }
                if (((ulong)puVar14[9] != 0) &&
                   (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[9]),
                   puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
                  uVar13 = (long)puVar4 - *param_2;
                  if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                    return 0;
                  }
                  uVar10 = param_2[1];
                  if (uVar10 < 5) {
                    return 0;
                  }
                  if (uVar10 - 4 < uVar13) {
                    return 0;
                  }
                  if ((ulong)param_2[4] <= (ulong)*puVar4) {
                    return 0;
                  }
                  uVar12 = (ulong)*puVar4 + 4;
                  if (uVar10 - 1 < uVar12 + uVar13) {
                    return 0;
                  }
                  if (uVar10 <= uVar12) {
                    return 0;
                  }
                  if (uVar10 - uVar12 < uVar13) {
                    return 0;
                  }
                  if (*(char *)(*param_2 + uVar12 + uVar13) != '\0') {
                    return 0;
                  }
                }
                if (0x14 < uVar6) {
                  if ((ulong)puVar14[10] != 0) {
                    uVar13 = (long)param_1 + ((ulong)puVar14[10] - *param_2);
                    if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                      return 0;
                    }
                    if ((ulong)param_2[1] < 5) {
                      return 0;
                    }
                    if (param_2[1] - 4U < uVar13) {
                      return 0;
                    }
                  }
                  if (0x16 < uVar6) {
                    if ((ulong)puVar14[0xb] != 0) {
                      uVar13 = (long)param_1 + ((ulong)puVar14[0xb] - *param_2);
                      if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                        return 0;
                      }
                      uVar10 = param_2[1];
                      if (uVar10 < 5) {
                        return 0;
                      }
                      if (uVar10 - 4 < uVar13) {
                        return 0;
                      }
                      uVar1 = *(uint *)(*param_2 + uVar13);
                      if ((int)uVar1 < 1) {
                        return 0;
                      }
                      if (uVar10 - 1 < uVar13 + uVar1) {
                        return 0;
                      }
                    }
                    if (((ulong)puVar14[0xb] != 0) &&
                       (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[0xb]),
                       puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
                      uVar13 = (long)puVar4 - *param_2;
                      if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                        return 0;
                      }
                      uVar10 = param_2[1];
                    /* try { // try from 00bbf7f4 to 00cbf9bf has its CatchHandler @ 00bbf7f4
                       catch() { ... } // from try @ 00bbf7f4 with catch @ 00bbf7f4
                       catch() { ... } // from try @ 00bbf9cc with catch @ 00bbf7f4 */
                      if (uVar10 < 5) {
                        return 0;
                      }
                      if (uVar10 - 4 < uVar13) {
                        return 0;
                      }
                      if ((ulong)param_2[4] <= (ulong)*puVar4) {
                        return 0;
                      }
                      uVar12 = (ulong)*puVar4 + 4;
                      if (uVar10 - 1 < uVar12 + uVar13) {
                        return 0;
                      }
                      if (uVar10 <= uVar12) {
                        return 0;
                      }
                      if (uVar10 - uVar12 < uVar13) {
                        return 0;
                      }
                      if (*(char *)(*param_2 + uVar12 + uVar13) != '\0') {
                        return 0;
                      }
                    }
                    if (0x18 < uVar6) {
                      if ((ulong)puVar14[0xc] != 0) {
                        uVar13 = (long)param_1 + ((ulong)puVar14[0xc] - *param_2);
                        if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                          return 0;
                        }
                        uVar10 = param_2[1];
                        if (uVar10 < 5) {
                          return 0;
                        }
                        if (uVar10 - 4 < uVar13) {
                          return 0;
                        }
                        uVar1 = *(uint *)(*param_2 + uVar13);
                        if ((int)uVar1 < 1) {
                          return 0;
                        }
                        if (uVar10 - 1 < uVar13 + uVar1) {
                          return 0;
                        }
                      }
                      if (((ulong)puVar14[0xc] != 0) &&
                         (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[0xc]),
                         puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
                        uVar13 = (long)puVar4 - *param_2;
                        if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                          return 0;
                        }
                        uVar10 = param_2[1];
                        if (uVar10 < 5) {
                          return 0;
                        }
                        if (uVar10 - 4 < uVar13) {
                          return 0;
                        }
                        if ((ulong)param_2[4] <= (ulong)*puVar4) {
                          return 0;
                        }
                        uVar12 = (ulong)*puVar4 + 4;
                        if (uVar10 - 1 < uVar12 + uVar13) {
                          return 0;
                        }
                        if (uVar10 <= uVar12) {
                          return 0;
                        }
                        if (uVar10 - uVar12 < uVar13) {
                          return 0;
                        }
                        if (*(char *)(*param_2 + uVar12 + uVar13) != '\0') {
                          return 0;
                        }
                      }
                      if (0x1a < uVar6) {
                        if ((ulong)puVar14[0xd] != 0) {
                          uVar13 = (long)param_1 + ((ulong)puVar14[0xd] - *param_2);
                          if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                            return 0;
                          }
                          uVar10 = param_2[1];
                          if (uVar10 < 5) {
                            return 0;
                          }
                          if (uVar10 - 4 < uVar13) {
                            return 0;
                          }
                          uVar1 = *(uint *)(*param_2 + uVar13);
                          if ((int)uVar1 < 1) {
                            return 0;
                          }
                          if (uVar10 - 1 < uVar13 + uVar1) {
                            return 0;
                          }
                        }
                        if (((ulong)puVar14[0xd] != 0) &&
                           (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[0xd]),
                           lVar11 = (long)puVar4 + (ulong)*puVar4, lVar11 != 0)) {
                    /* try { // try from 00bbf9c0 to 00cbf9cb has its CatchHandler @ 00bbfae8 */
                          uVar13 = _ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                             (lVar11,param_2);
                          if ((uVar13 & 1) == 0) {
                            return 0;
                          }
                    /* try { // try from 00bbf9cc to 00cbfb17 has its CatchHandler @ 00bbf7f4 */
                          lVar9 = -(long)*param_1;
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        puVar14 = (ushort *)((long)param_1 + lVar9);
        uVar6 = *puVar14;
        if (0x1c < uVar6) {
          if ((ulong)puVar14[0xe] != 0) {
            if ((ulong)param_2[1] < 2) {
              return 0;
            }
            if (param_2[1] - 1U < (long)param_1 + ((ulong)puVar14[0xe] - *param_2)) {
              return 0;
            }
          }
          if (0x1e < uVar6) {
            if ((ulong)puVar14[0xf] != 0) {
              uVar13 = (long)param_1 + ((ulong)puVar14[0xf] - *param_2);
              if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                return 0;
              }
              uVar10 = param_2[1];
              if (uVar10 < 5) {
                return 0;
              }
              if (uVar10 - 4 < uVar13) {
                return 0;
              }
              uVar1 = *(uint *)(*param_2 + uVar13);
              if ((int)uVar1 < 1) {
                return 0;
              }
              if (uVar10 - 1 < uVar13 + uVar1) {
                return 0;
              }
            }
            if (((ulong)puVar14[0xf] != 0) &&
               (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[0xf]),
               puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
              uVar13 = (long)puVar4 - *param_2;
              if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                return 0;
              }
              uVar10 = param_2[1];
              if (uVar10 < 5) {
                return 0;
              }
              if (uVar10 - 4 < uVar13) {
                return 0;
              }
              if ((ulong)param_2[4] <= (ulong)*puVar4) {
                return 0;
              }
              uVar12 = (ulong)*puVar4 + 4;
                    /* catch() { ... } // from try @ 00bbf9c0 with catch @ 00bbfae8 */
              if (uVar10 - 1 < uVar12 + uVar13) {
                return 0;
              }
              if (uVar10 <= uVar12) {
                return 0;
              }
              if (uVar10 - uVar12 < uVar13) {
                return 0;
              }
              if (*(char *)(*param_2 + uVar12 + uVar13) != '\0') {
                return 0;
              }
            }
            if (0x20 < uVar6) {
              if ((ulong)puVar14[0x10] != 0) {
                    /* catch() { ... } // from try @ 00bbfbc8 with catch @ 00bbfb18
                       catch() { ... } // from try @ 00bbfd08 with catch @ 00bbfb18
                       catch() { ... } // from try @ 00bbfdf4 with catch @ 00bbfb18
                       catch() { ... } // from try @ 00bbff64 with catch @ 00bbfb18
                       catch() { ... } // from try @ 00bc0014 with catch @ 00bbfb18
                       catch() { ... } // from try @ 00bc02ec with catch @ 00bbfb18 */
                uVar13 = (long)param_1 + ((ulong)puVar14[0x10] - *param_2);
                if (((uVar13 & 7) != 0) && ((char)param_2[3] != '\0')) {
                  return 0;
                }
                if ((ulong)param_2[1] < 9) {
                  return 0;
                }
                if (param_2[1] - 8U < uVar13) {
                  return 0;
                }
              }
              if (0x22 < uVar6) {
                if ((ulong)puVar14[0x11] != 0) {
                  uVar13 = (long)param_1 + ((ulong)puVar14[0x11] - *param_2);
                  if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                    return 0;
                  }
                  uVar10 = param_2[1];
                  if (uVar10 < 5) {
                    return 0;
                  }
                  if (uVar10 - 4 < uVar13) {
                    return 0;
                  }
                  uVar1 = *(uint *)(*param_2 + uVar13);
                  if ((int)uVar1 < 1) {
                    return 0;
                  }
                    /* try { // try from 00bbfba8 to 00cbfbc7 has its CatchHandler @ 00bc039c */
                  if (uVar10 - 1 < uVar13 + uVar1) {
                    return 0;
                  }
                }
                    /* try { // try from 00bbfbc8 to 00cbfcbb has its CatchHandler @ 00bbfb18 */
                if (((ulong)puVar14[0x11] != 0) &&
                   (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[0x11]),
                   puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
                  uVar13 = (long)puVar4 - *param_2;
                  if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                    return 0;
                  }
                  uVar10 = param_2[1];
                  if (uVar10 < 5) {
                    return 0;
                  }
                  if (uVar10 - 4 < uVar13) {
                    return 0;
                  }
                  if ((ulong)param_2[4] <= (ulong)*puVar4) {
                    return 0;
                  }
                  uVar12 = (ulong)*puVar4 + 4;
                  if (uVar10 - 1 < uVar12 + uVar13) {
                    return 0;
                  }
                  if (uVar10 <= uVar12) {
                    return 0;
                  }
                  if (uVar10 - uVar12 < uVar13) {
                    return 0;
                  }
                  if (*(char *)(*param_2 + uVar12 + uVar13) != '\0') {
                    return 0;
                  }
                }
              }
            }
          }
        }
        *(int *)(param_2 + 7) = (int)param_2[7] + -1;
        return 1;
      }
    }
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbeec8"></a> `00bbeec8` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbeecc"></a> `00bbeecc` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbeed0"></a> `00bbeed0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbeed4"></a> `00bbeed4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbeed8"></a> `00bbeed8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbeedc"></a> `00bbeedc` | `2a 00 40 f9` | ldr x10,[x1] | `FALL_THROUGH`
<a id="insn-00bbeee0"></a> `00bbeee0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbeee4"></a> `00bbeee4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbeee8"></a> `00bbeee8` | `0c 00 0a cb` | sub x12,x0,x10 | `FALL_THROUGH`
<a id="insn-00bbeeec"></a> `00bbeeec` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bbeef0"></a> `00bbeef0` | `60 00 00 54` | b.eq 0x00bbeefc | `CONDITIONAL_JUMP`
<a id="insn-00bbeef4"></a> `00bbeef4` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbeef8"></a> `00bbeef8` | `68 6a 00 35` | cbnz w8,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbeefc"></a> `00bbeefc` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbef00"></a> `00bbef00` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbef04"></a> `00bbef04` | `3f 15 00 f1` | cmp x9,#0x5 | `FALL_THROUGH`
<a id="insn-00bbef08"></a> `00bbef08` | `03 6a 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbef0c"></a> `00bbef0c` | `2b 11 00 d1` | sub x11,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00bbef10"></a> `00bbef10` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bbef14"></a> `00bbef14` | `a3 69 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbef18"></a> `00bbef18` | `6d 3a 47 29` | ldp w13,w14,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbef1c"></a> `00bbef1c` | `6f 12 40 b9` | ldr w15,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbef20"></a> `00bbef20` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbef24"></a> `00bbef24` | `b0 05 00 11` | add w16,w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbef28"></a> `00bbef28` | `cd 05 00 11` | add w13,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbef2c"></a> `00bbef2c` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bbef30"></a> `00bbef30` | `70 36 07 29` | stp w16,w13,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbef34"></a> `00bbef34` | `88 68 00 54` | b.hi 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbef38"></a> `00bbef38` | `6e 16 40 b9` | ldr w14,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00bbef3c"></a> `00bbef3c` | `bf 01 0e 6b` | cmp w13,w14 | `FALL_THROUGH`
<a id="insn-00bbef40"></a> `00bbef40` | `28 68 00 54` | b.hi 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbef44"></a> `00bbef44` | `88 01 08 cb` | sub x8,x12,x8 | `FALL_THROUGH`
<a id="insn-00bbef48"></a> `00bbef48` | `68 00 00 36` | tbz w8,#0x0,0x00bbef54 | `CONDITIONAL_JUMP`
<a id="insn-00bbef4c"></a> `00bbef4c` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbef50"></a> `00bbef50` | `ad 67 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbef54"></a> `00bbef54` | `2d 09 00 d1` | sub x13,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbef58"></a> `00bbef58` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00bbef5c"></a> `00bbef5c` | `43 67 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbef60"></a> `00bbef60` | `4d 69 68 78` | ldrh w13,[x10, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbef64"></a> `00bbef64` | `6d 00 00 36` | tbz w13,#0x0,0x00bbef70 | `CONDITIONAL_JUMP`
<a id="insn-00bbef68"></a> `00bbef68` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbef6c"></a> `00bbef6c` | `ce 66 00 35` | cbnz w14,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbef70"></a> `00bbef70` | `ad 66 00 37` | tbnz w13,#0x0,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbef74"></a> `00bbef74` | `2d 01 0d eb` | subs x13,x9,x13 | `FALL_THROUGH`
<a id="insn-00bbef78"></a> `00bbef78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbef7c"></a> `00bbef7c` | `69 66 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbef80"></a> `00bbef80` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00bbef84"></a> `00bbef84` | `23 66 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbef88"></a> `00bbef88` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbef8c"></a> `00bbef8c` | `8d 02 08 cb` | sub x13,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbef90"></a> `00bbef90` | `ae 01 40 79` | ldrh w14,[x13] | `FALL_THROUGH`
<a id="insn-00bbef94"></a> `00bbef94` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbef98"></a> `00bbef98` | `df 15 00 71` | cmp w14,#0x5 | `FALL_THROUGH`
<a id="insn-00bbef9c"></a> `00bbef9c` | `e3 1d 00 54` | b.cc 0x00bbf358 | `CONDITIONAL_JUMP`
<a id="insn-00bbefa0"></a> `00bbefa0` | `af 09 40 79` | ldrh w15,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbefa4"></a> `00bbefa4` | `6f 02 00 b4` | cbz x15,0x00bbeff0 | `CONDITIONAL_JUMP`
<a id="insn-00bbefa8"></a> `00bbefa8` | `8f 01 0f 8b` | add x15,x12,x15 | `FALL_THROUGH`
<a id="insn-00bbefac"></a> `00bbefac` | `ff 05 40 f2` | tst x15,#0x3 | `FALL_THROUGH`
<a id="insn-00bbefb0"></a> `00bbefb0` | `e0 00 00 54` | b.eq 0x00bbefcc | `CONDITIONAL_JUMP`
<a id="insn-00bbefb4"></a> `00bbefb4` | `70 62 40 39` | ldrb w16,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbefb8"></a> `00bbefb8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbefbc"></a> `00bbefbc` | `70 64 00 35` | cbnz w16,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbefc0"></a> `00bbefc0` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbefc4"></a> `00bbefc4` | `82 00 00 54` | b.cs 0x00bbefd4 | `CONDITIONAL_JUMP`
<a id="insn-00bbefc8"></a> `00bbefc8` | `20 03 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbefcc"></a> `00bbefcc` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbefd0"></a> `00bbefd0` | `a3 63 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbefd4"></a> `00bbefd4` | `50 69 6f b8` | ldr w16,[x10, x15, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbefd8"></a> `00bbefd8` | `1f 06 00 71` | cmp w16,#0x1 | `FALL_THROUGH`
<a id="insn-00bbefdc"></a> `00bbefdc` | `4b 63 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbefe0"></a> `00bbefe0` | `ef 01 10 8b` | add x15,x15,x16 | `FALL_THROUGH`
<a id="insn-00bbefe4"></a> `00bbefe4` | `30 05 00 d1` | sub x16,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbefe8"></a> `00bbefe8` | `1f 02 0f eb` | cmp x16,x15 | `FALL_THROUGH`
<a id="insn-00bbefec"></a> `00bbefec` | `c3 62 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbeff0"></a> `00bbeff0` | `af 09 40 79` | ldrh w15,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbeff4"></a> `00bbeff4` | `2f 04 00 b4` | cbz x15,0x00bbf078 | `CONDITIONAL_JUMP`
<a id="insn-00bbeff8"></a> `00bbeff8` | `8f 02 0f 8b` | add x15,x20,x15 | `FALL_THROUGH`
<a id="insn-00bbeffc"></a> `00bbeffc` | `f0 01 40 b9` | ldr w16,[x15] | `FALL_THROUGH`
<a id="insn-00bbf000"></a> `00bbf000` | `f0 01 10 ab` | adds x16,x15,x16 | `FALL_THROUGH`
<a id="insn-00bbf004"></a> `00bbf004` | `a0 03 00 54` | b.eq 0x00bbf078 | `CONDITIONAL_JUMP`
<a id="insn-00bbf008"></a> `00bbf008` | `0f 02 0a cb` | sub x15,x16,x10 | `FALL_THROUGH`
<a id="insn-00bbf00c"></a> `00bbf00c` | `ff 05 40 f2` | tst x15,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf010"></a> `00bbf010` | `e0 00 00 54` | b.eq 0x00bbf02c | `CONDITIONAL_JUMP`
<a id="insn-00bbf014"></a> `00bbf014` | `71 62 40 39` | ldrb w17,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf018"></a> `00bbf018` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf01c"></a> `00bbf01c` | `71 61 00 35` | cbnz w17,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf020"></a> `00bbf020` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf024"></a> `00bbf024` | `82 00 00 54` | b.cs 0x00bbf034 | `CONDITIONAL_JUMP`
<a id="insn-00bbf028"></a> `00bbf028` | `08 03 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf02c"></a> `00bbf02c` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf030"></a> `00bbf030` | `a3 60 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf034"></a> `00bbf034` | `10 02 40 b9` | ldr w16,[x16] | `FALL_THROUGH`
<a id="insn-00bbf038"></a> `00bbf038` | `71 12 40 f9` | ldr x17,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf03c"></a> `00bbf03c` | `3f 02 10 eb` | cmp x17,x16 | `FALL_THROUGH`
<a id="insn-00bbf040"></a> `00bbf040` | `29 60 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf044"></a> `00bbf044` | `11 12 00 91` | add x17,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf048"></a> `00bbf048` | `30 02 0f 8b` | add x16,x17,x15 | `FALL_THROUGH`
<a id="insn-00bbf04c"></a> `00bbf04c` | `20 05 00 d1` | sub x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf050"></a> `00bbf050` | `1f 00 10 eb` | cmp x0,x16 | `FALL_THROUGH`
<a id="insn-00bbf054"></a> `00bbf054` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf058"></a> `00bbf058` | `83 5f 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf05c"></a> `00bbf05c` | `3f 01 11 eb` | cmp x9,x17 | `FALL_THROUGH`
<a id="insn-00bbf060"></a> `00bbf060` | `49 5f 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf064"></a> `00bbf064` | `31 01 11 cb` | sub x17,x9,x17 | `FALL_THROUGH`
<a id="insn-00bbf068"></a> `00bbf068` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bbf06c"></a> `00bbf06c` | `e3 5e 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf070"></a> `00bbf070` | `4f 69 70 38` | ldrb w15,[x10, x16, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf074"></a> `00bbf074` | `8f 5e 00 35` | cbnz w15,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf078"></a> `00bbf078` | `df 1d 00 71` | cmp w14,#0x7 | `FALL_THROUGH`
<a id="insn-00bbf07c"></a> `00bbf07c` | `e3 16 00 54` | b.cc 0x00bbf358 | `CONDITIONAL_JUMP`
<a id="insn-00bbf080"></a> `00bbf080` | `af 0d 40 79` | ldrh w15,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbf084"></a> `00bbf084` | `6f 02 00 b4` | cbz x15,0x00bbf0d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf088"></a> `00bbf088` | `8f 01 0f 8b` | add x15,x12,x15 | `FALL_THROUGH`
<a id="insn-00bbf08c"></a> `00bbf08c` | `ff 05 40 f2` | tst x15,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf090"></a> `00bbf090` | `e0 00 00 54` | b.eq 0x00bbf0ac | `CONDITIONAL_JUMP`
<a id="insn-00bbf094"></a> `00bbf094` | `70 62 40 39` | ldrb w16,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf098"></a> `00bbf098` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf09c"></a> `00bbf09c` | `70 5d 00 35` | cbnz w16,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0a0"></a> `00bbf0a0` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf0a4"></a> `00bbf0a4` | `82 00 00 54` | b.cs 0x00bbf0b4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0a8"></a> `00bbf0a8` | `e8 02 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf0ac"></a> `00bbf0ac` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf0b0"></a> `00bbf0b0` | `a3 5c 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0b4"></a> `00bbf0b4` | `50 69 6f b8` | ldr w16,[x10, x15, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf0b8"></a> `00bbf0b8` | `1f 06 00 71` | cmp w16,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf0bc"></a> `00bbf0bc` | `4b 5c 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0c0"></a> `00bbf0c0` | `ef 01 10 8b` | add x15,x15,x16 | `FALL_THROUGH`
<a id="insn-00bbf0c4"></a> `00bbf0c4` | `30 05 00 d1` | sub x16,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf0c8"></a> `00bbf0c8` | `1f 02 0f eb` | cmp x16,x15 | `FALL_THROUGH`
<a id="insn-00bbf0cc"></a> `00bbf0cc` | `c3 5b 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0d0"></a> `00bbf0d0` | `af 0d 40 79` | ldrh w15,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbf0d4"></a> `00bbf0d4` | `2f 04 00 b4` | cbz x15,0x00bbf158 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0d8"></a> `00bbf0d8` | `8f 02 0f 8b` | add x15,x20,x15 | `FALL_THROUGH`
<a id="insn-00bbf0dc"></a> `00bbf0dc` | `f0 01 40 b9` | ldr w16,[x15] | `FALL_THROUGH`
<a id="insn-00bbf0e0"></a> `00bbf0e0` | `f0 01 10 ab` | adds x16,x15,x16 | `FALL_THROUGH`
<a id="insn-00bbf0e4"></a> `00bbf0e4` | `a0 03 00 54` | b.eq 0x00bbf158 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0e8"></a> `00bbf0e8` | `0f 02 0a cb` | sub x15,x16,x10 | `FALL_THROUGH`
<a id="insn-00bbf0ec"></a> `00bbf0ec` | `ff 05 40 f2` | tst x15,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf0f0"></a> `00bbf0f0` | `e0 00 00 54` | b.eq 0x00bbf10c | `CONDITIONAL_JUMP`
<a id="insn-00bbf0f4"></a> `00bbf0f4` | `71 62 40 39` | ldrb w17,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf0f8"></a> `00bbf0f8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf0fc"></a> `00bbf0fc` | `71 5a 00 35` | cbnz w17,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf100"></a> `00bbf100` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf104"></a> `00bbf104` | `82 00 00 54` | b.cs 0x00bbf114 | `CONDITIONAL_JUMP`
<a id="insn-00bbf108"></a> `00bbf108` | `d0 02 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf10c"></a> `00bbf10c` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf110"></a> `00bbf110` | `a3 59 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf114"></a> `00bbf114` | `10 02 40 b9` | ldr w16,[x16] | `FALL_THROUGH`
<a id="insn-00bbf118"></a> `00bbf118` | `71 12 40 f9` | ldr x17,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf11c"></a> `00bbf11c` | `3f 02 10 eb` | cmp x17,x16 | `FALL_THROUGH`
<a id="insn-00bbf120"></a> `00bbf120` | `29 59 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf124"></a> `00bbf124` | `11 12 00 91` | add x17,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf128"></a> `00bbf128` | `30 02 0f 8b` | add x16,x17,x15 | `FALL_THROUGH`
<a id="insn-00bbf12c"></a> `00bbf12c` | `20 05 00 d1` | sub x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf130"></a> `00bbf130` | `1f 00 10 eb` | cmp x0,x16 | `FALL_THROUGH`
<a id="insn-00bbf134"></a> `00bbf134` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf138"></a> `00bbf138` | `83 58 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf13c"></a> `00bbf13c` | `3f 01 11 eb` | cmp x9,x17 | `FALL_THROUGH`
<a id="insn-00bbf140"></a> `00bbf140` | `49 58 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf144"></a> `00bbf144` | `31 01 11 cb` | sub x17,x9,x17 | `FALL_THROUGH`
<a id="insn-00bbf148"></a> `00bbf148` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bbf14c"></a> `00bbf14c` | `e3 57 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf150"></a> `00bbf150` | `4f 69 70 38` | ldrb w15,[x10, x16, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf154"></a> `00bbf154` | `8f 57 00 35` | cbnz w15,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf158"></a> `00bbf158` | `df 25 00 71` | cmp w14,#0x9 | `FALL_THROUGH`
<a id="insn-00bbf15c"></a> `00bbf15c` | `e3 0f 00 54` | b.cc 0x00bbf358 | `CONDITIONAL_JUMP`
<a id="insn-00bbf160"></a> `00bbf160` | `af 11 40 79` | ldrh w15,[x13, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf164"></a> `00bbf164` | `6f 02 00 b4` | cbz x15,0x00bbf1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf168"></a> `00bbf168` | `8f 01 0f 8b` | add x15,x12,x15 | `FALL_THROUGH`
<a id="insn-00bbf16c"></a> `00bbf16c` | `ff 05 40 f2` | tst x15,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf170"></a> `00bbf170` | `e0 00 00 54` | b.eq 0x00bbf18c | `CONDITIONAL_JUMP`
<a id="insn-00bbf174"></a> `00bbf174` | `70 62 40 39` | ldrb w16,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf178"></a> `00bbf178` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf17c"></a> `00bbf17c` | `70 56 00 35` | cbnz w16,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf180"></a> `00bbf180` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf184"></a> `00bbf184` | `82 00 00 54` | b.cs 0x00bbf194 | `CONDITIONAL_JUMP`
<a id="insn-00bbf188"></a> `00bbf188` | `b0 02 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf18c"></a> `00bbf18c` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf190"></a> `00bbf190` | `a3 55 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf194"></a> `00bbf194` | `50 69 6f b8` | ldr w16,[x10, x15, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf198"></a> `00bbf198` | `1f 06 00 71` | cmp w16,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf19c"></a> `00bbf19c` | `4b 55 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1a0"></a> `00bbf1a0` | `ef 01 10 8b` | add x15,x15,x16 | `FALL_THROUGH`
<a id="insn-00bbf1a4"></a> `00bbf1a4` | `30 05 00 d1` | sub x16,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf1a8"></a> `00bbf1a8` | `1f 02 0f eb` | cmp x16,x15 | `FALL_THROUGH`
<a id="insn-00bbf1ac"></a> `00bbf1ac` | `c3 54 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1b0"></a> `00bbf1b0` | `af 11 40 79` | ldrh w15,[x13, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf1b4"></a> `00bbf1b4` | `2f 04 00 b4` | cbz x15,0x00bbf238 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1b8"></a> `00bbf1b8` | `8f 02 0f 8b` | add x15,x20,x15 | `FALL_THROUGH`
<a id="insn-00bbf1bc"></a> `00bbf1bc` | `f0 01 40 b9` | ldr w16,[x15] | `FALL_THROUGH`
<a id="insn-00bbf1c0"></a> `00bbf1c0` | `f0 01 10 ab` | adds x16,x15,x16 | `FALL_THROUGH`
<a id="insn-00bbf1c4"></a> `00bbf1c4` | `a0 03 00 54` | b.eq 0x00bbf238 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1c8"></a> `00bbf1c8` | `0f 02 0a cb` | sub x15,x16,x10 | `FALL_THROUGH`
<a id="insn-00bbf1cc"></a> `00bbf1cc` | `ff 05 40 f2` | tst x15,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf1d0"></a> `00bbf1d0` | `e0 00 00 54` | b.eq 0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbf1d4"></a> `00bbf1d4` | `71 62 40 39` | ldrb w17,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf1d8"></a> `00bbf1d8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf1dc"></a> `00bbf1dc` | `71 53 00 35` | cbnz w17,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1e0"></a> `00bbf1e0` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf1e4"></a> `00bbf1e4` | `82 00 00 54` | b.cs 0x00bbf1f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1e8"></a> `00bbf1e8` | `98 02 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf1ec"></a> `00bbf1ec` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00bbf1f0"></a> `00bbf1f0` | `a3 52 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1f4"></a> `00bbf1f4` | `10 02 40 b9` | ldr w16,[x16] | `FALL_THROUGH`
<a id="insn-00bbf1f8"></a> `00bbf1f8` | `71 12 40 f9` | ldr x17,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf1fc"></a> `00bbf1fc` | `3f 02 10 eb` | cmp x17,x16 | `FALL_THROUGH`
<a id="insn-00bbf200"></a> `00bbf200` | `29 52 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf204"></a> `00bbf204` | `11 12 00 91` | add x17,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf208"></a> `00bbf208` | `30 02 0f 8b` | add x16,x17,x15 | `FALL_THROUGH`
<a id="insn-00bbf20c"></a> `00bbf20c` | `20 05 00 d1` | sub x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf210"></a> `00bbf210` | `1f 00 10 eb` | cmp x0,x16 | `FALL_THROUGH`
<a id="insn-00bbf214"></a> `00bbf214` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf218"></a> `00bbf218` | `83 51 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf21c"></a> `00bbf21c` | `3f 01 11 eb` | cmp x9,x17 | `FALL_THROUGH`
<a id="insn-00bbf220"></a> `00bbf220` | `49 51 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf224"></a> `00bbf224` | `31 01 11 cb` | sub x17,x9,x17 | `FALL_THROUGH`
<a id="insn-00bbf228"></a> `00bbf228` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bbf22c"></a> `00bbf22c` | `e3 50 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf230"></a> `00bbf230` | `4f 69 70 38` | ldrb w15,[x10, x16, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf234"></a> `00bbf234` | `8f 50 00 35` | cbnz w15,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf238"></a> `00bbf238` | `df 2d 00 71` | cmp w14,#0xb | `FALL_THROUGH`
<a id="insn-00bbf23c"></a> `00bbf23c` | `e3 08 00 54` | b.cc 0x00bbf358 | `CONDITIONAL_JUMP`
<a id="insn-00bbf240"></a> `00bbf240` | `ae 15 40 79` | ldrh w14,[x13, #0xa] | `FALL_THROUGH`
<a id="insn-00bbf244"></a> `00bbf244` | `6e 02 00 b4` | cbz x14,0x00bbf290 | `CONDITIONAL_JUMP`
<a id="insn-00bbf248"></a> `00bbf248` | `8c 01 0e 8b` | add x12,x12,x14 | `FALL_THROUGH`
<a id="insn-00bbf24c"></a> `00bbf24c` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf250"></a> `00bbf250` | `e0 00 00 54` | b.eq 0x00bbf26c | `CONDITIONAL_JUMP`
<a id="insn-00bbf254"></a> `00bbf254` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf258"></a> `00bbf258` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf25c"></a> `00bbf25c` | `6e 4f 00 35` | cbnz w14,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf260"></a> `00bbf260` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf264"></a> `00bbf264` | `82 00 00 54` | b.cs 0x00bbf274 | `CONDITIONAL_JUMP`
<a id="insn-00bbf268"></a> `00bbf268` | `78 02 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf26c"></a> `00bbf26c` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf270"></a> `00bbf270` | `a3 4e 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf274"></a> `00bbf274` | `4e 69 6c b8` | ldr w14,[x10, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf278"></a> `00bbf278` | `df 05 00 71` | cmp w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf27c"></a> `00bbf27c` | `4b 4e 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf280"></a> `00bbf280` | `8c 01 0e 8b` | add x12,x12,x14 | `FALL_THROUGH`
<a id="insn-00bbf284"></a> `00bbf284` | `2e 05 00 d1` | sub x14,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf288"></a> `00bbf288` | `df 01 0c eb` | cmp x14,x12 | `FALL_THROUGH`
<a id="insn-00bbf28c"></a> `00bbf28c` | `c3 4d 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf290"></a> `00bbf290` | `ac 15 40 79` | ldrh w12,[x13, #0xa] | `FALL_THROUGH`
<a id="insn-00bbf294"></a> `00bbf294` | `2c 06 00 b4` | cbz x12,0x00bbf358 | `CONDITIONAL_JUMP`
<a id="insn-00bbf298"></a> `00bbf298` | `8c 02 0c 8b` | add x12,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf29c"></a> `00bbf29c` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00bbf2a0"></a> `00bbf2a0` | `8d 01 0d ab` | adds x13,x12,x13 | `FALL_THROUGH`
<a id="insn-00bbf2a4"></a> `00bbf2a4` | `e0 02 00 54` | b.eq 0x00bbf300 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2a8"></a> `00bbf2a8` | `aa 01 0a cb` | sub x10,x13,x10 | `FALL_THROUGH`
<a id="insn-00bbf2ac"></a> `00bbf2ac` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf2b0"></a> `00bbf2b0` | `e0 00 00 54` | b.eq 0x00bbf2cc | `CONDITIONAL_JUMP`
<a id="insn-00bbf2b4"></a> `00bbf2b4` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf2b8"></a> `00bbf2b8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf2bc"></a> `00bbf2bc` | `6e 4c 00 35` | cbnz w14,0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2c0"></a> `00bbf2c0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bbf2c4"></a> `00bbf2c4` | `82 00 00 54` | b.cs 0x00bbf2d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2c8"></a> `00bbf2c8` | `60 02 00 14` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf2cc"></a> `00bbf2cc` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bbf2d0"></a> `00bbf2d0` | `a3 4b 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2d4"></a> `00bbf2d4` | `ab 01 40 b9` | ldr w11,[x13] | `FALL_THROUGH`
<a id="insn-00bbf2d8"></a> `00bbf2d8` | `6d 12 40 f9` | ldr x13,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf2dc"></a> `00bbf2dc` | `7f 09 4d eb` | cmp x11,x13, LSR #0x2 | `FALL_THROUGH`
<a id="insn-00bbf2e0"></a> `00bbf2e0` | `22 4b 00 54` | b.cs 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2e4"></a> `00bbf2e4` | `6b f5 7e d3` | lsl x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf2e8"></a> `00bbf2e8` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf2ec"></a> `00bbf2ec` | `29 01 0b eb` | subs x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00bbf2f0"></a> `00bbf2f0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf2f4"></a> `00bbf2f4` | `a9 4a 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2f8"></a> `00bbf2f8` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbf2fc"></a> `00bbf2fc` | `63 4a 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf300"></a> `00bbf300` | `89 01 40 b9` | ldr w9,[x12] | `FALL_THROUGH`
<a id="insn-00bbf304"></a> `00bbf304` | `95 01 09 ab` | adds x21,x12,x9 | `FALL_THROUGH`
<a id="insn-00bbf308"></a> `00bbf308` | `80 02 00 54` | b.eq 0x00bbf358 | `CONDITIONAL_JUMP`
<a id="insn-00bbf30c"></a> `00bbf30c` | `a9 02 40 b9` | ldr w9,[x21] | `FALL_THROUGH`
<a id="insn-00bbf310"></a> `00bbf310` | `49 02 00 34` | cbz w9,0x00bbf358 | `CONDITIONAL_JUMP`
<a id="insn-00bbf314"></a> `00bbf314` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bbf318"></a> `00bbf318` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bbf31c"></a> `00bbf31c` | `b8 12 00 91` | add x24,x21,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf320"></a> `00bbf320` | `c8 76 7e 92` | and x8,x22,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00bbf324"></a> `00bbf324` | `08 03 08 8b` | add x8,x24,x8 | `FALL_THROUGH`
<a id="insn-00bbf328"></a> `00bbf328` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf32c"></a> `00bbf32c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbf330"></a> `00bbf330` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf334"></a> `00bbf334` | `b3 78 02 94` | bl 0x00c5d600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf338"></a> `00bbf338` | `60 48 00 36` | tbz w0,#0x0,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf33c"></a> `00bbf33c` | `a8 02 40 b9` | ldr w8,[x21] | `FALL_THROUGH`
<a id="insn-00bbf340"></a> `00bbf340` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf344"></a> `00bbf344` | `d6 12 00 91` | add x22,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf348"></a> `00bbf348` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00bbf34c"></a> `00bbf34c` | `a3 fe ff 54` | b.cc 0x00bbf320 | `CONDITIONAL_JUMP`
<a id="insn-00bbf350"></a> `00bbf350` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbf354"></a> `00bbf354` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbf358"></a> `00bbf358` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf35c"></a> `00bbf35c` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbf360"></a> `00bbf360` | `5f 35 00 71` | cmp w10,#0xd | `FALL_THROUGH`
<a id="insn-00bbf364"></a> `00bbf364` | `83 33 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf368"></a> `00bbf368` | `2b 19 40 79` | ldrh w11,[x9, #0xc] | `FALL_THROUGH`
<a id="insn-00bbf36c"></a> `00bbf36c` | `cb 02 00 b4` | cbz x11,0x00bbf3c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf370"></a> `00bbf370` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbf374"></a> `00bbf374` | `8d 02 0c cb` | sub x13,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf378"></a> `00bbf378` | `ab 01 0b 8b` | add x11,x13,x11 | `FALL_THROUGH`
<a id="insn-00bbf37c"></a> `00bbf37c` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf380"></a> `00bbf380` | `60 00 00 54` | b.eq 0x00bbf38c | `CONDITIONAL_JUMP`
<a id="insn-00bbf384"></a> `00bbf384` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf388"></a> `00bbf388` | `ed 45 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf38c"></a> `00bbf38c` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf390"></a> `00bbf390` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf394"></a> `00bbf394` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf398"></a> `00bbf398` | `83 45 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf39c"></a> `00bbf39c` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf3a0"></a> `00bbf3a0` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf3a4"></a> `00bbf3a4` | `23 45 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3a8"></a> `00bbf3a8` | `8c 69 6b b8` | ldr w12,[x12, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf3ac"></a> `00bbf3ac` | `9f 05 00 71` | cmp w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf3b0"></a> `00bbf3b0` | `ab 44 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3b4"></a> `00bbf3b4` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf3b8"></a> `00bbf3b8` | `ac 05 00 d1` | sub x12,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf3bc"></a> `00bbf3bc` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf3c0"></a> `00bbf3c0` | `23 44 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3c4"></a> `00bbf3c4` | `2b 19 40 79` | ldrh w11,[x9, #0xc] | `FALL_THROUGH`
<a id="insn-00bbf3c8"></a> `00bbf3c8` | `8b 03 00 b4` | cbz x11,0x00bbf438 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3cc"></a> `00bbf3cc` | `8b 02 0b 8b` | add x11,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbf3d0"></a> `00bbf3d0` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbf3d4"></a> `00bbf3d4` | `6c 01 0c ab` | adds x12,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf3d8"></a> `00bbf3d8` | `00 03 00 54` | b.eq 0x00bbf438 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3dc"></a> `00bbf3dc` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbf3e0"></a> `00bbf3e0` | `8b 01 0b cb` | sub x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf3e4"></a> `00bbf3e4` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf3e8"></a> `00bbf3e8` | `60 00 00 54` | b.eq 0x00bbf3f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3ec"></a> `00bbf3ec` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf3f0"></a> `00bbf3f0` | `ad 42 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3f4"></a> `00bbf3f4` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf3f8"></a> `00bbf3f8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf3fc"></a> `00bbf3fc` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf400"></a> `00bbf400` | `43 42 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf404"></a> `00bbf404` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf408"></a> `00bbf408` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf40c"></a> `00bbf40c` | `e3 41 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf410"></a> `00bbf410` | `8c 01 40 b9` | ldr w12,[x12] | `FALL_THROUGH`
<a id="insn-00bbf414"></a> `00bbf414` | `6e 12 40 f9` | ldr x14,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf418"></a> `00bbf418` | `df 01 0c eb` | cmp x14,x12 | `FALL_THROUGH`
<a id="insn-00bbf41c"></a> `00bbf41c` | `49 41 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf420"></a> `00bbf420` | `8c 11 00 91` | add x12,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf424"></a> `00bbf424` | `ac 01 0c eb` | subs x12,x13,x12 | `FALL_THROUGH`
<a id="insn-00bbf428"></a> `00bbf428` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf42c"></a> `00bbf42c` | `e9 40 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf430"></a> `00bbf430` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf434"></a> `00bbf434` | `a3 40 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf438"></a> `00bbf438` | `5f 3d 00 71` | cmp w10,#0xf | `FALL_THROUGH`
<a id="insn-00bbf43c"></a> `00bbf43c` | `c3 2c 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf440"></a> `00bbf440` | `2b 1d 40 79` | ldrh w11,[x9, #0xe] | `FALL_THROUGH`
<a id="insn-00bbf444"></a> `00bbf444` | `cb 02 00 b4` | cbz x11,0x00bbf49c | `CONDITIONAL_JUMP`
<a id="insn-00bbf448"></a> `00bbf448` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbf44c"></a> `00bbf44c` | `8d 02 0c cb` | sub x13,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf450"></a> `00bbf450` | `ab 01 0b 8b` | add x11,x13,x11 | `FALL_THROUGH`
<a id="insn-00bbf454"></a> `00bbf454` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf458"></a> `00bbf458` | `60 00 00 54` | b.eq 0x00bbf464 | `CONDITIONAL_JUMP`
<a id="insn-00bbf45c"></a> `00bbf45c` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf460"></a> `00bbf460` | `2d 3f 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf464"></a> `00bbf464` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf468"></a> `00bbf468` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf46c"></a> `00bbf46c` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf470"></a> `00bbf470` | `c3 3e 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf474"></a> `00bbf474` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf478"></a> `00bbf478` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf47c"></a> `00bbf47c` | `63 3e 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf480"></a> `00bbf480` | `8c 69 6b b8` | ldr w12,[x12, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf484"></a> `00bbf484` | `9f 05 00 71` | cmp w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf488"></a> `00bbf488` | `eb 3d 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf48c"></a> `00bbf48c` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf490"></a> `00bbf490` | `ac 05 00 d1` | sub x12,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf494"></a> `00bbf494` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf498"></a> `00bbf498` | `63 3d 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf49c"></a> `00bbf49c` | `2b 1d 40 79` | ldrh w11,[x9, #0xe] | `FALL_THROUGH`
<a id="insn-00bbf4a0"></a> `00bbf4a0` | `6b 04 00 b4` | cbz x11,0x00bbf52c | `CONDITIONAL_JUMP`
<a id="insn-00bbf4a4"></a> `00bbf4a4` | `8b 02 0b 8b` | add x11,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbf4a8"></a> `00bbf4a8` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbf4ac"></a> `00bbf4ac` | `6e 01 0c ab` | adds x14,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf4b0"></a> `00bbf4b0` | `e0 03 00 54` | b.eq 0x00bbf52c | `CONDITIONAL_JUMP`
<a id="insn-00bbf4b4"></a> `00bbf4b4` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbf4b8"></a> `00bbf4b8` | `cc 01 0b cb` | sub x12,x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf4bc"></a> `00bbf4bc` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf4c0"></a> `00bbf4c0` | `60 00 00 54` | b.eq 0x00bbf4cc | `CONDITIONAL_JUMP`
<a id="insn-00bbf4c4"></a> `00bbf4c4` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf4c8"></a> `00bbf4c8` | `ed 3b 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf4cc"></a> `00bbf4cc` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf4d0"></a> `00bbf4d0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf4d4"></a> `00bbf4d4` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf4d8"></a> `00bbf4d8` | `83 3b 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf4dc"></a> `00bbf4dc` | `af 11 00 d1` | sub x15,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf4e0"></a> `00bbf4e0` | `ff 01 0c eb` | cmp x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf4e4"></a> `00bbf4e4` | `23 3b 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf4e8"></a> `00bbf4e8` | `ce 01 40 b9` | ldr w14,[x14] | `FALL_THROUGH`
<a id="insn-00bbf4ec"></a> `00bbf4ec` | `6f 12 40 f9` | ldr x15,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf4f0"></a> `00bbf4f0` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbf4f4"></a> `00bbf4f4` | `89 3a 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf4f8"></a> `00bbf4f8` | `cf 11 00 91` | add x15,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf4fc"></a> `00bbf4fc` | `ee 01 0c 8b` | add x14,x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf500"></a> `00bbf500` | `b0 05 00 d1` | sub x16,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf504"></a> `00bbf504` | `1f 02 0e eb` | cmp x16,x14 | `FALL_THROUGH`
<a id="insn-00bbf508"></a> `00bbf508` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf50c"></a> `00bbf50c` | `e3 39 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf510"></a> `00bbf510` | `bf 01 0f eb` | cmp x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf514"></a> `00bbf514` | `a9 39 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf518"></a> `00bbf518` | `ad 01 0f cb` | sub x13,x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf51c"></a> `00bbf51c` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00bbf520"></a> `00bbf520` | `43 39 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf524"></a> `00bbf524` | `6b 69 6e 38` | ldrb w11,[x11, x14, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf528"></a> `00bbf528` | `eb 38 00 35` | cbnz w11,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf52c"></a> `00bbf52c` | `5f 45 00 71` | cmp w10,#0x11 | `FALL_THROUGH`
<a id="insn-00bbf530"></a> `00bbf530` | `23 25 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf534"></a> `00bbf534` | `2b 21 40 79` | ldrh w11,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf538"></a> `00bbf538` | `cb 02 00 b4` | cbz x11,0x00bbf590 | `CONDITIONAL_JUMP`
<a id="insn-00bbf53c"></a> `00bbf53c` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbf540"></a> `00bbf540` | `8d 02 0c cb` | sub x13,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf544"></a> `00bbf544` | `ab 01 0b 8b` | add x11,x13,x11 | `FALL_THROUGH`
<a id="insn-00bbf548"></a> `00bbf548` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf54c"></a> `00bbf54c` | `60 00 00 54` | b.eq 0x00bbf558 | `CONDITIONAL_JUMP`
<a id="insn-00bbf550"></a> `00bbf550` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf554"></a> `00bbf554` | `8d 37 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf558"></a> `00bbf558` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf55c"></a> `00bbf55c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf560"></a> `00bbf560` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf564"></a> `00bbf564` | `23 37 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf568"></a> `00bbf568` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf56c"></a> `00bbf56c` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf570"></a> `00bbf570` | `c3 36 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf574"></a> `00bbf574` | `8c 69 6b b8` | ldr w12,[x12, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf578"></a> `00bbf578` | `9f 05 00 71` | cmp w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf57c"></a> `00bbf57c` | `4b 36 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf580"></a> `00bbf580` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf584"></a> `00bbf584` | `ac 05 00 d1` | sub x12,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf588"></a> `00bbf588` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf58c"></a> `00bbf58c` | `c3 35 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf590"></a> `00bbf590` | `2b 21 40 79` | ldrh w11,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf594"></a> `00bbf594` | `6b 04 00 b4` | cbz x11,0x00bbf620 | `CONDITIONAL_JUMP`
<a id="insn-00bbf598"></a> `00bbf598` | `8b 02 0b 8b` | add x11,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbf59c"></a> `00bbf59c` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbf5a0"></a> `00bbf5a0` | `6e 01 0c ab` | adds x14,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf5a4"></a> `00bbf5a4` | `e0 03 00 54` | b.eq 0x00bbf620 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5a8"></a> `00bbf5a8` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbf5ac"></a> `00bbf5ac` | `cc 01 0b cb` | sub x12,x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf5b0"></a> `00bbf5b0` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf5b4"></a> `00bbf5b4` | `60 00 00 54` | b.eq 0x00bbf5c0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5b8"></a> `00bbf5b8` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf5bc"></a> `00bbf5bc` | `4d 34 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5c0"></a> `00bbf5c0` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf5c4"></a> `00bbf5c4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf5c8"></a> `00bbf5c8` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf5cc"></a> `00bbf5cc` | `e3 33 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5d0"></a> `00bbf5d0` | `af 11 00 d1` | sub x15,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf5d4"></a> `00bbf5d4` | `ff 01 0c eb` | cmp x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf5d8"></a> `00bbf5d8` | `83 33 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5dc"></a> `00bbf5dc` | `ce 01 40 b9` | ldr w14,[x14] | `FALL_THROUGH`
<a id="insn-00bbf5e0"></a> `00bbf5e0` | `6f 12 40 f9` | ldr x15,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf5e4"></a> `00bbf5e4` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbf5e8"></a> `00bbf5e8` | `e9 32 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5ec"></a> `00bbf5ec` | `cf 11 00 91` | add x15,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf5f0"></a> `00bbf5f0` | `ee 01 0c 8b` | add x14,x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf5f4"></a> `00bbf5f4` | `b0 05 00 d1` | sub x16,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf5f8"></a> `00bbf5f8` | `1f 02 0e eb` | cmp x16,x14 | `FALL_THROUGH`
<a id="insn-00bbf5fc"></a> `00bbf5fc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf600"></a> `00bbf600` | `43 32 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf604"></a> `00bbf604` | `bf 01 0f eb` | cmp x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf608"></a> `00bbf608` | `09 32 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf60c"></a> `00bbf60c` | `ad 01 0f cb` | sub x13,x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf610"></a> `00bbf610` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00bbf614"></a> `00bbf614` | `a3 31 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf618"></a> `00bbf618` | `6b 69 6e 38` | ldrb w11,[x11, x14, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf61c"></a> `00bbf61c` | `4b 31 00 35` | cbnz w11,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf620"></a> `00bbf620` | `5f 4d 00 71` | cmp w10,#0x13 | `FALL_THROUGH`
<a id="insn-00bbf624"></a> `00bbf624` | `83 1d 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf628"></a> `00bbf628` | `2b 25 40 79` | ldrh w11,[x9, #0x12] | `FALL_THROUGH`
<a id="insn-00bbf62c"></a> `00bbf62c` | `cb 02 00 b4` | cbz x11,0x00bbf684 | `CONDITIONAL_JUMP`
<a id="insn-00bbf630"></a> `00bbf630` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbf634"></a> `00bbf634` | `8d 02 0c cb` | sub x13,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf638"></a> `00bbf638` | `ab 01 0b 8b` | add x11,x13,x11 | `FALL_THROUGH`
<a id="insn-00bbf63c"></a> `00bbf63c` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf640"></a> `00bbf640` | `60 00 00 54` | b.eq 0x00bbf64c | `CONDITIONAL_JUMP`
<a id="insn-00bbf644"></a> `00bbf644` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf648"></a> `00bbf648` | `ed 2f 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf64c"></a> `00bbf64c` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf650"></a> `00bbf650` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf654"></a> `00bbf654` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf658"></a> `00bbf658` | `83 2f 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf65c"></a> `00bbf65c` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf660"></a> `00bbf660` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf664"></a> `00bbf664` | `23 2f 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf668"></a> `00bbf668` | `8c 69 6b b8` | ldr w12,[x12, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf66c"></a> `00bbf66c` | `9f 05 00 71` | cmp w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf670"></a> `00bbf670` | `ab 2e 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf674"></a> `00bbf674` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf678"></a> `00bbf678` | `ac 05 00 d1` | sub x12,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf67c"></a> `00bbf67c` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf680"></a> `00bbf680` | `23 2e 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf684"></a> `00bbf684` | `2b 25 40 79` | ldrh w11,[x9, #0x12] | `FALL_THROUGH`
<a id="insn-00bbf688"></a> `00bbf688` | `6b 04 00 b4` | cbz x11,0x00bbf714 | `CONDITIONAL_JUMP`
<a id="insn-00bbf68c"></a> `00bbf68c` | `8b 02 0b 8b` | add x11,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbf690"></a> `00bbf690` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbf694"></a> `00bbf694` | `6e 01 0c ab` | adds x14,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf698"></a> `00bbf698` | `e0 03 00 54` | b.eq 0x00bbf714 | `CONDITIONAL_JUMP`
<a id="insn-00bbf69c"></a> `00bbf69c` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbf6a0"></a> `00bbf6a0` | `cc 01 0b cb` | sub x12,x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf6a4"></a> `00bbf6a4` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf6a8"></a> `00bbf6a8` | `60 00 00 54` | b.eq 0x00bbf6b4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf6ac"></a> `00bbf6ac` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf6b0"></a> `00bbf6b0` | `ad 2c 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf6b4"></a> `00bbf6b4` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf6b8"></a> `00bbf6b8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf6bc"></a> `00bbf6bc` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf6c0"></a> `00bbf6c0` | `43 2c 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf6c4"></a> `00bbf6c4` | `af 11 00 d1` | sub x15,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf6c8"></a> `00bbf6c8` | `ff 01 0c eb` | cmp x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf6cc"></a> `00bbf6cc` | `e3 2b 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf6d0"></a> `00bbf6d0` | `ce 01 40 b9` | ldr w14,[x14] | `FALL_THROUGH`
<a id="insn-00bbf6d4"></a> `00bbf6d4` | `6f 12 40 f9` | ldr x15,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf6d8"></a> `00bbf6d8` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbf6dc"></a> `00bbf6dc` | `49 2b 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf6e0"></a> `00bbf6e0` | `cf 11 00 91` | add x15,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf6e4"></a> `00bbf6e4` | `ee 01 0c 8b` | add x14,x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf6e8"></a> `00bbf6e8` | `b0 05 00 d1` | sub x16,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf6ec"></a> `00bbf6ec` | `1f 02 0e eb` | cmp x16,x14 | `FALL_THROUGH`
<a id="insn-00bbf6f0"></a> `00bbf6f0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf6f4"></a> `00bbf6f4` | `a3 2a 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf6f8"></a> `00bbf6f8` | `bf 01 0f eb` | cmp x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf6fc"></a> `00bbf6fc` | `69 2a 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf700"></a> `00bbf700` | `ad 01 0f cb` | sub x13,x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf704"></a> `00bbf704` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00bbf708"></a> `00bbf708` | `03 2a 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf70c"></a> `00bbf70c` | `6b 69 6e 38` | ldrb w11,[x11, x14, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf710"></a> `00bbf710` | `ab 29 00 35` | cbnz w11,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf714"></a> `00bbf714` | `5f 55 00 71` | cmp w10,#0x15 | `FALL_THROUGH`
<a id="insn-00bbf718"></a> `00bbf718` | `e3 15 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf71c"></a> `00bbf71c` | `2b 29 40 79` | ldrh w11,[x9, #0x14] | `FALL_THROUGH`
<a id="insn-00bbf720"></a> `00bbf720` | `eb 01 00 b4` | cbz x11,0x00bbf75c | `CONDITIONAL_JUMP`
<a id="insn-00bbf724"></a> `00bbf724` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbf728"></a> `00bbf728` | `8c 02 0c cb` | sub x12,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf72c"></a> `00bbf72c` | `8b 01 0b 8b` | add x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf730"></a> `00bbf730` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf734"></a> `00bbf734` | `60 00 00 54` | b.eq 0x00bbf740 | `CONDITIONAL_JUMP`
<a id="insn-00bbf738"></a> `00bbf738` | `6c 62 40 39` | ldrb w12,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf73c"></a> `00bbf73c` | `4c 28 00 35` | cbnz w12,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf740"></a> `00bbf740` | `6c 06 40 f9` | ldr x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf744"></a> `00bbf744` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf748"></a> `00bbf748` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf74c"></a> `00bbf74c` | `e3 27 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf750"></a> `00bbf750` | `8c 11 00 d1` | sub x12,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf754"></a> `00bbf754` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf758"></a> `00bbf758` | `83 27 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf75c"></a> `00bbf75c` | `5f 5d 00 71` | cmp w10,#0x17 | `FALL_THROUGH`
<a id="insn-00bbf760"></a> `00bbf760` | `a3 13 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf764"></a> `00bbf764` | `2b 2d 40 79` | ldrh w11,[x9, #0x16] | `FALL_THROUGH`
<a id="insn-00bbf768"></a> `00bbf768` | `cb 02 00 b4` | cbz x11,0x00bbf7c0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf76c"></a> `00bbf76c` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbf770"></a> `00bbf770` | `8d 02 0c cb` | sub x13,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf774"></a> `00bbf774` | `ab 01 0b 8b` | add x11,x13,x11 | `FALL_THROUGH`
<a id="insn-00bbf778"></a> `00bbf778` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf77c"></a> `00bbf77c` | `60 00 00 54` | b.eq 0x00bbf788 | `CONDITIONAL_JUMP`
<a id="insn-00bbf780"></a> `00bbf780` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf784"></a> `00bbf784` | `0d 26 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf788"></a> `00bbf788` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf78c"></a> `00bbf78c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf790"></a> `00bbf790` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf794"></a> `00bbf794` | `a3 25 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf798"></a> `00bbf798` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf79c"></a> `00bbf79c` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf7a0"></a> `00bbf7a0` | `43 25 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7a4"></a> `00bbf7a4` | `8c 69 6b b8` | ldr w12,[x12, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf7a8"></a> `00bbf7a8` | `9f 05 00 71` | cmp w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf7ac"></a> `00bbf7ac` | `cb 24 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7b0"></a> `00bbf7b0` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf7b4"></a> `00bbf7b4` | `ac 05 00 d1` | sub x12,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf7b8"></a> `00bbf7b8` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf7bc"></a> `00bbf7bc` | `43 24 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7c0"></a> `00bbf7c0` | `2b 2d 40 79` | ldrh w11,[x9, #0x16] | `FALL_THROUGH`
<a id="insn-00bbf7c4"></a> `00bbf7c4` | `6b 04 00 b4` | cbz x11,0x00bbf850 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7c8"></a> `00bbf7c8` | `8b 02 0b 8b` | add x11,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbf7cc"></a> `00bbf7cc` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbf7d0"></a> `00bbf7d0` | `6e 01 0c ab` | adds x14,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf7d4"></a> `00bbf7d4` | `e0 03 00 54` | b.eq 0x00bbf850 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7d8"></a> `00bbf7d8` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbf7dc"></a> `00bbf7dc` | `cc 01 0b cb` | sub x12,x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf7e0"></a> `00bbf7e0` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf7e4"></a> `00bbf7e4` | `60 00 00 54` | b.eq 0x00bbf7f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7e8"></a> `00bbf7e8` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf7ec"></a> `00bbf7ec` | `cd 22 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7f0"></a> `00bbf7f0` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf7f4"></a> `00bbf7f4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf7f8"></a> `00bbf7f8` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf7fc"></a> `00bbf7fc` | `63 22 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf800"></a> `00bbf800` | `af 11 00 d1` | sub x15,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf804"></a> `00bbf804` | `ff 01 0c eb` | cmp x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf808"></a> `00bbf808` | `03 22 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf80c"></a> `00bbf80c` | `ce 01 40 b9` | ldr w14,[x14] | `FALL_THROUGH`
<a id="insn-00bbf810"></a> `00bbf810` | `6f 12 40 f9` | ldr x15,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf814"></a> `00bbf814` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbf818"></a> `00bbf818` | `69 21 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf81c"></a> `00bbf81c` | `cf 11 00 91` | add x15,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf820"></a> `00bbf820` | `ee 01 0c 8b` | add x14,x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf824"></a> `00bbf824` | `b0 05 00 d1` | sub x16,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf828"></a> `00bbf828` | `1f 02 0e eb` | cmp x16,x14 | `FALL_THROUGH`
<a id="insn-00bbf82c"></a> `00bbf82c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf830"></a> `00bbf830` | `c3 20 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf834"></a> `00bbf834` | `bf 01 0f eb` | cmp x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf838"></a> `00bbf838` | `89 20 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf83c"></a> `00bbf83c` | `ad 01 0f cb` | sub x13,x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf840"></a> `00bbf840` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00bbf844"></a> `00bbf844` | `23 20 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf848"></a> `00bbf848` | `6b 69 6e 38` | ldrb w11,[x11, x14, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf84c"></a> `00bbf84c` | `cb 1f 00 35` | cbnz w11,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf850"></a> `00bbf850` | `5f 65 00 71` | cmp w10,#0x19 | `FALL_THROUGH`
<a id="insn-00bbf854"></a> `00bbf854` | `03 0c 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf858"></a> `00bbf858` | `2b 31 40 79` | ldrh w11,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf85c"></a> `00bbf85c` | `cb 02 00 b4` | cbz x11,0x00bbf8b4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf860"></a> `00bbf860` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbf864"></a> `00bbf864` | `8d 02 0c cb` | sub x13,x20,x12 | `FALL_THROUGH`
<a id="insn-00bbf868"></a> `00bbf868` | `ab 01 0b 8b` | add x11,x13,x11 | `FALL_THROUGH`
<a id="insn-00bbf86c"></a> `00bbf86c` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf870"></a> `00bbf870` | `60 00 00 54` | b.eq 0x00bbf87c | `CONDITIONAL_JUMP`
<a id="insn-00bbf874"></a> `00bbf874` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf878"></a> `00bbf878` | `6d 1e 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf87c"></a> `00bbf87c` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf880"></a> `00bbf880` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf884"></a> `00bbf884` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf888"></a> `00bbf888` | `03 1e 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf88c"></a> `00bbf88c` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf890"></a> `00bbf890` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf894"></a> `00bbf894` | `a3 1d 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf898"></a> `00bbf898` | `8c 69 6b b8` | ldr w12,[x12, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf89c"></a> `00bbf89c` | `9f 05 00 71` | cmp w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf8a0"></a> `00bbf8a0` | `2b 1d 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8a4"></a> `00bbf8a4` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf8a8"></a> `00bbf8a8` | `ac 05 00 d1` | sub x12,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf8ac"></a> `00bbf8ac` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbf8b0"></a> `00bbf8b0` | `a3 1c 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8b4"></a> `00bbf8b4` | `2b 31 40 79` | ldrh w11,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf8b8"></a> `00bbf8b8` | `6b 04 00 b4` | cbz x11,0x00bbf944 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8bc"></a> `00bbf8bc` | `8b 02 0b 8b` | add x11,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbf8c0"></a> `00bbf8c0` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbf8c4"></a> `00bbf8c4` | `6e 01 0c ab` | adds x14,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbf8c8"></a> `00bbf8c8` | `e0 03 00 54` | b.eq 0x00bbf944 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8cc"></a> `00bbf8cc` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbf8d0"></a> `00bbf8d0` | `cc 01 0b cb` | sub x12,x14,x11 | `FALL_THROUGH`
<a id="insn-00bbf8d4"></a> `00bbf8d4` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf8d8"></a> `00bbf8d8` | `60 00 00 54` | b.eq 0x00bbf8e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8dc"></a> `00bbf8dc` | `6d 62 40 39` | ldrb w13,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf8e0"></a> `00bbf8e0` | `2d 1b 00 35` | cbnz w13,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8e4"></a> `00bbf8e4` | `6d 06 40 f9` | ldr x13,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf8e8"></a> `00bbf8e8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf8ec"></a> `00bbf8ec` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf8f0"></a> `00bbf8f0` | `c3 1a 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8f4"></a> `00bbf8f4` | `af 11 00 d1` | sub x15,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf8f8"></a> `00bbf8f8` | `ff 01 0c eb` | cmp x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf8fc"></a> `00bbf8fc` | `63 1a 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf900"></a> `00bbf900` | `ce 01 40 b9` | ldr w14,[x14] | `FALL_THROUGH`
<a id="insn-00bbf904"></a> `00bbf904` | `6f 12 40 f9` | ldr x15,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf908"></a> `00bbf908` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbf90c"></a> `00bbf90c` | `c9 19 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf910"></a> `00bbf910` | `cf 11 00 91` | add x15,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf914"></a> `00bbf914` | `ee 01 0c 8b` | add x14,x15,x12 | `FALL_THROUGH`
<a id="insn-00bbf918"></a> `00bbf918` | `b0 05 00 d1` | sub x16,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf91c"></a> `00bbf91c` | `1f 02 0e eb` | cmp x16,x14 | `FALL_THROUGH`
<a id="insn-00bbf920"></a> `00bbf920` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf924"></a> `00bbf924` | `23 19 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf928"></a> `00bbf928` | `bf 01 0f eb` | cmp x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf92c"></a> `00bbf92c` | `e9 18 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf930"></a> `00bbf930` | `ad 01 0f cb` | sub x13,x13,x15 | `FALL_THROUGH`
<a id="insn-00bbf934"></a> `00bbf934` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00bbf938"></a> `00bbf938` | `83 18 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf93c"></a> `00bbf93c` | `6b 69 6e 38` | ldrb w11,[x11, x14, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf940"></a> `00bbf940` | `2b 18 00 35` | cbnz w11,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf944"></a> `00bbf944` | `5f 6d 00 71` | cmp w10,#0x1b | `FALL_THROUGH`
<a id="insn-00bbf948"></a> `00bbf948` | `63 04 00 54` | b.cc 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf94c"></a> `00bbf94c` | `2a 35 40 79` | ldrh w10,[x9, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbf950"></a> `00bbf950` | `ca 02 00 b4` | cbz x10,0x00bbf9a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf954"></a> `00bbf954` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbf958"></a> `00bbf958` | `8c 02 0b cb` | sub x12,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbf95c"></a> `00bbf95c` | `8a 01 0a 8b` | add x10,x12,x10 | `FALL_THROUGH`
<a id="insn-00bbf960"></a> `00bbf960` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf964"></a> `00bbf964` | `60 00 00 54` | b.eq 0x00bbf970 | `CONDITIONAL_JUMP`
<a id="insn-00bbf968"></a> `00bbf968` | `6c 62 40 39` | ldrb w12,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf96c"></a> `00bbf96c` | `cc 16 00 35` | cbnz w12,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf970"></a> `00bbf970` | `6c 06 40 f9` | ldr x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf974"></a> `00bbf974` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf978"></a> `00bbf978` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf97c"></a> `00bbf97c` | `63 16 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf980"></a> `00bbf980` | `8d 11 00 d1` | sub x13,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf984"></a> `00bbf984` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00bbf988"></a> `00bbf988` | `03 16 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf98c"></a> `00bbf98c` | `6b 69 6a b8` | ldr w11,[x11, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf990"></a> `00bbf990` | `7f 05 00 71` | cmp w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf994"></a> `00bbf994` | `8b 15 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf998"></a> `00bbf998` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbf99c"></a> `00bbf99c` | `8b 05 00 d1` | sub x11,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf9a0"></a> `00bbf9a0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bbf9a4"></a> `00bbf9a4` | `03 15 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9a8"></a> `00bbf9a8` | `29 35 40 79` | ldrh w9,[x9, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbf9ac"></a> `00bbf9ac` | `49 01 00 b4` | cbz x9,0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9b0"></a> `00bbf9b0` | `89 02 09 8b` | add x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00bbf9b4"></a> `00bbf9b4` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbf9b8"></a> `00bbf9b8` | `20 01 0a ab` | adds x0,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbf9bc"></a> `00bbf9bc` | `c0 00 00 54` | b.eq 0x00bbf9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9c0"></a> `00bbf9c0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbf9c4"></a> `00bbf9c4` | `ff 76 02 94` | bl 0x00c5d5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf9c8"></a> `00bbf9c8` | `e0 13 00 36` | tbz w0,#0x0,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9cc"></a> `00bbf9cc` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbf9d0"></a> `00bbf9d0` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbf9d4"></a> `00bbf9d4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf9d8"></a> `00bbf9d8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf9dc"></a> `00bbf9dc` | `3f 75 00 71` | cmp w9,#0x1d | `FALL_THROUGH`
<a id="insn-00bbf9e0"></a> `00bbf9e0` | `e3 13 00 54` | b.cc 0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbf9e4"></a> `00bbf9e4` | `0a 39 40 79` | ldrh w10,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00bbf9e8"></a> `00bbf9e8` | `6a 01 00 b4` | cbz x10,0x00bbfa14 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9ec"></a> `00bbf9ec` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf9f0"></a> `00bbf9f0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbf9f4"></a> `00bbf9f4` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf9f8"></a> `00bbf9f8` | `83 12 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9fc"></a> `00bbf9fc` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bbfa00"></a> `00bbfa00` | `4a 01 14 8b` | add x10,x10,x20 | `FALL_THROUGH`
<a id="insn-00bbfa04"></a> `00bbfa04` | `6b 05 00 d1` | sub x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfa08"></a> `00bbfa08` | `4a 01 0c cb` | sub x10,x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfa0c"></a> `00bbfa0c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bbfa10"></a> `00bbfa10` | `c3 11 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa14"></a> `00bbfa14` | `3f 7d 00 71` | cmp w9,#0x1f | `FALL_THROUGH`
<a id="insn-00bbfa18"></a> `00bbfa18` | `23 12 00 54` | b.cc 0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbfa1c"></a> `00bbfa1c` | `0a 3d 40 79` | ldrh w10,[x8, #0x1e] | `FALL_THROUGH`
<a id="insn-00bbfa20"></a> `00bbfa20` | `ca 02 00 b4` | cbz x10,0x00bbfa78 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa24"></a> `00bbfa24` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbfa28"></a> `00bbfa28` | `8c 02 0b cb` | sub x12,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbfa2c"></a> `00bbfa2c` | `8a 01 0a 8b` | add x10,x12,x10 | `FALL_THROUGH`
<a id="insn-00bbfa30"></a> `00bbfa30` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfa34"></a> `00bbfa34` | `60 00 00 54` | b.eq 0x00bbfa40 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa38"></a> `00bbfa38` | `6c 62 40 39` | ldrb w12,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfa3c"></a> `00bbfa3c` | `4c 10 00 35` | cbnz w12,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa40"></a> `00bbfa40` | `6c 06 40 f9` | ldr x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfa44"></a> `00bbfa44` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfa48"></a> `00bbfa48` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfa4c"></a> `00bbfa4c` | `e3 0f 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa50"></a> `00bbfa50` | `8d 11 00 d1` | sub x13,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfa54"></a> `00bbfa54` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00bbfa58"></a> `00bbfa58` | `83 0f 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa5c"></a> `00bbfa5c` | `6b 69 6a b8` | ldr w11,[x11, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbfa60"></a> `00bbfa60` | `7f 05 00 71` | cmp w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfa64"></a> `00bbfa64` | `0b 0f 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa68"></a> `00bbfa68` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbfa6c"></a> `00bbfa6c` | `8b 05 00 d1` | sub x11,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfa70"></a> `00bbfa70` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bbfa74"></a> `00bbfa74` | `83 0e 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa78"></a> `00bbfa78` | `0a 3d 40 79` | ldrh w10,[x8, #0x1e] | `FALL_THROUGH`
<a id="insn-00bbfa7c"></a> `00bbfa7c` | `6a 04 00 b4` | cbz x10,0x00bbfb08 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa80"></a> `00bbfa80` | `8a 02 0a 8b` | add x10,x20,x10 | `FALL_THROUGH`
<a id="insn-00bbfa84"></a> `00bbfa84` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbfa88"></a> `00bbfa88` | `4d 01 0b ab` | adds x13,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbfa8c"></a> `00bbfa8c` | `e0 03 00 54` | b.eq 0x00bbfb08 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa90"></a> `00bbfa90` | `6a 02 40 f9` | ldr x10,[x19] | `FALL_THROUGH`
<a id="insn-00bbfa94"></a> `00bbfa94` | `ab 01 0a cb` | sub x11,x13,x10 | `FALL_THROUGH`
<a id="insn-00bbfa98"></a> `00bbfa98` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfa9c"></a> `00bbfa9c` | `60 00 00 54` | b.eq 0x00bbfaa8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfaa0"></a> `00bbfaa0` | `6c 62 40 39` | ldrb w12,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfaa4"></a> `00bbfaa4` | `0c 0d 00 35` | cbnz w12,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfaa8"></a> `00bbfaa8` | `6c 06 40 f9` | ldr x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfaac"></a> `00bbfaac` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfab0"></a> `00bbfab0` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfab4"></a> `00bbfab4` | `a3 0c 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfab8"></a> `00bbfab8` | `8e 11 00 d1` | sub x14,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfabc"></a> `00bbfabc` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00bbfac0"></a> `00bbfac0` | `43 0c 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfac4"></a> `00bbfac4` | `ad 01 40 b9` | ldr w13,[x13] | `FALL_THROUGH`
<a id="insn-00bbfac8"></a> `00bbfac8` | `6e 12 40 f9` | ldr x14,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfacc"></a> `00bbfacc` | `df 01 0d eb` | cmp x14,x13 | `FALL_THROUGH`
<a id="insn-00bbfad0"></a> `00bbfad0` | `a9 0b 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfad4"></a> `00bbfad4` | `ae 11 00 91` | add x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfad8"></a> `00bbfad8` | `cd 01 0b 8b` | add x13,x14,x11 | `FALL_THROUGH`
<a id="insn-00bbfadc"></a> `00bbfadc` | `8f 05 00 d1` | sub x15,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfae0"></a> `00bbfae0` | `ff 01 0d eb` | cmp x15,x13 | `FALL_THROUGH`
<a id="insn-00bbfae4"></a> `00bbfae4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfae8"></a> `00bbfae8` | `03 0b 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfaec"></a> `00bbfaec` | `9f 01 0e eb` | cmp x12,x14 | `FALL_THROUGH`
<a id="insn-00bbfaf0"></a> `00bbfaf0` | `c9 0a 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfaf4"></a> `00bbfaf4` | `8c 01 0e cb` | sub x12,x12,x14 | `FALL_THROUGH`
<a id="insn-00bbfaf8"></a> `00bbfaf8` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbfafc"></a> `00bbfafc` | `63 0a 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb00"></a> `00bbfb00` | `4a 69 6d 38` | ldrb w10,[x10, x13, LSL ] | `FALL_THROUGH`
<a id="insn-00bbfb04"></a> `00bbfb04` | `0a 0a 00 35` | cbnz w10,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb08"></a> `00bbfb08` | `3f 85 00 71` | cmp w9,#0x21 | `FALL_THROUGH`
<a id="insn-00bbfb0c"></a> `00bbfb0c` | `83 0a 00 54` | b.cc 0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb10"></a> `00bbfb10` | `0a 41 40 79` | ldrh w10,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfb14"></a> `00bbfb14` | `ea 01 00 b4` | cbz x10,0x00bbfb50 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb18"></a> `00bbfb18` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb1c"></a> `00bbfb1c` | `8b 02 0b cb` | sub x11,x20,x11 | `FALL_THROUGH`
<a id="insn-00bbfb20"></a> `00bbfb20` | `6a 01 0a 8b` | add x10,x11,x10 | `FALL_THROUGH`
<a id="insn-00bbfb24"></a> `00bbfb24` | `5f 09 40 f2` | tst x10,#0x7 | `FALL_THROUGH`
<a id="insn-00bbfb28"></a> `00bbfb28` | `60 00 00 54` | b.eq 0x00bbfb34 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb2c"></a> `00bbfb2c` | `6b 62 40 39` | ldrb w11,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfb30"></a> `00bbfb30` | `ab 08 00 35` | cbnz w11,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb34"></a> `00bbfb34` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfb38"></a> `00bbfb38` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfb3c"></a> `00bbfb3c` | `7f 25 00 f1` | cmp x11,#0x9 | `FALL_THROUGH`
<a id="insn-00bbfb40"></a> `00bbfb40` | `43 08 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb44"></a> `00bbfb44` | `6b 21 00 d1` | sub x11,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bbfb48"></a> `00bbfb48` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bbfb4c"></a> `00bbfb4c` | `e3 07 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb50"></a> `00bbfb50` | `3f 8d 00 71` | cmp w9,#0x23 | `FALL_THROUGH`
<a id="insn-00bbfb54"></a> `00bbfb54` | `43 08 00 54` | b.cc 0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb58"></a> `00bbfb58` | `09 45 40 79` | ldrh w9,[x8, #0x22] | `FALL_THROUGH`
<a id="insn-00bbfb5c"></a> `00bbfb5c` | `c9 02 00 b4` | cbz x9,0x00bbfbb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb60"></a> `00bbfb60` | `6a 02 40 f9` | ldr x10,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb64"></a> `00bbfb64` | `8b 02 0a cb` | sub x11,x20,x10 | `FALL_THROUGH`
<a id="insn-00bbfb68"></a> `00bbfb68` | `69 01 09 8b` | add x9,x11,x9 | `FALL_THROUGH`
<a id="insn-00bbfb6c"></a> `00bbfb6c` | `3f 05 40 f2` | tst x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfb70"></a> `00bbfb70` | `60 00 00 54` | b.eq 0x00bbfb7c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb74"></a> `00bbfb74` | `6b 62 40 39` | ldrb w11,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfb78"></a> `00bbfb78` | `6b 06 00 35` | cbnz w11,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb7c"></a> `00bbfb7c` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfb80"></a> `00bbfb80` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfb84"></a> `00bbfb84` | `7f 15 00 f1` | cmp x11,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfb88"></a> `00bbfb88` | `03 06 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb8c"></a> `00bbfb8c` | `6c 11 00 d1` | sub x12,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfb90"></a> `00bbfb90` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bbfb94"></a> `00bbfb94` | `a3 05 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb98"></a> `00bbfb98` | `4a 69 69 b8` | ldr w10,[x10, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbfb9c"></a> `00bbfb9c` | `5f 05 00 71` | cmp w10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfba0"></a> `00bbfba0` | `2b 05 00 54` | b.lt 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfba4"></a> `00bbfba4` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbfba8"></a> `00bbfba8` | `6a 05 00 d1` | sub x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfbac"></a> `00bbfbac` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bbfbb0"></a> `00bbfbb0` | `a3 04 00 54` | b.cc 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbb4"></a> `00bbfbb4` | `08 45 40 79` | ldrh w8,[x8, #0x22] | `FALL_THROUGH`
<a id="insn-00bbfbb8"></a> `00bbfbb8` | `28 05 00 b4` | cbz x8,0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbfbbc"></a> `00bbfbbc` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbfbc0"></a> `00bbfbc0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfbc4"></a> `00bbfbc4` | `0b 01 09 ab` | adds x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfbc8"></a> `00bbfbc8` | `a0 04 00 54` | b.eq 0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbfbcc"></a> `00bbfbcc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfbd0"></a> `00bbfbd0` | `69 01 08 cb` | sub x9,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbfbd4"></a> `00bbfbd4` | `3f 05 40 f2` | tst x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfbd8"></a> `00bbfbd8` | `60 00 00 54` | b.eq 0x00bbfbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbdc"></a> `00bbfbdc` | `6a 62 40 39` | ldrb w10,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfbe0"></a> `00bbfbe0` | `2a 03 00 35` | cbnz w10,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbe4"></a> `00bbfbe4` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfbe8"></a> `00bbfbe8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfbec"></a> `00bbfbec` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfbf0"></a> `00bbfbf0` | `c3 02 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbf4"></a> `00bbfbf4` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfbf8"></a> `00bbfbf8` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bbfbfc"></a> `00bbfbfc` | `63 02 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc00"></a> `00bbfc00` | `6b 01 40 b9` | ldr w11,[x11] | `FALL_THROUGH`
<a id="insn-00bbfc04"></a> `00bbfc04` | `6c 12 40 f9` | ldr x12,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfc08"></a> `00bbfc08` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbfc0c"></a> `00bbfc0c` | `c9 01 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc10"></a> `00bbfc10` | `6c 11 00 91` | add x12,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfc14"></a> `00bbfc14` | `8b 01 09 8b` | add x11,x12,x9 | `FALL_THROUGH`
<a id="insn-00bbfc18"></a> `00bbfc18` | `4d 05 00 d1` | sub x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfc1c"></a> `00bbfc1c` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bbfc20"></a> `00bbfc20` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfc24"></a> `00bbfc24` | `23 01 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc28"></a> `00bbfc28` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfc2c"></a> `00bbfc2c` | `e9 00 00 54` | b.ls 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc30"></a> `00bbfc30` | `4a 01 0c cb` | sub x10,x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfc34"></a> `00bbfc34` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bbfc38"></a> `00bbfc38` | `83 00 00 54` | b.cc 0x00bbfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc3c"></a> `00bbfc3c` | `08 69 6b 38` | ldrb w8,[x8, x11, LSL ] | `FALL_THROUGH`
<a id="insn-00bbfc40"></a> `00bbfc40` | `e8 00 00 34` | cbz w8,0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc44"></a> `00bbfc44` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfc48"></a> `00bbfc48` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfc4c"></a> `00bbfc4c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfc50"></a> `00bbfc50` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc54"></a> `00bbfc54` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfc58"></a> `00bbfc58` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfc5c"></a> `00bbfc5c` | `68 3a 40 b9` | ldr w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfc60"></a> `00bbfc60` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfc64"></a> `00bbfc64` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfc68"></a> `00bbfc68` | `68 3a 00 b9` | str w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfc6c"></a> `00bbfc6c` | `f7 ff ff 17` | b 0x00bbfc48 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbeec8`](#insn-00bbeec8) 範囲 `[['00bbeec8', '00bbeef3']]`
  - `CONDITIONAL_JUMP` [`00bbeef0`](#insn-00bbeef0) → [`00bbeefc`](#insn-00bbeefc)
  - `FALL_THROUGH` [`00bbeef0`](#insn-00bbeef0) → [`00bbeef4`](#insn-00bbeef4)
- ブロック [`00bbeef4`](#insn-00bbeef4) 範囲 `[['00bbeef4', '00bbeefb']]`
  - `CONDITIONAL_JUMP` [`00bbeef8`](#insn-00bbeef8) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbeef8`](#insn-00bbeef8) → [`00bbeefc`](#insn-00bbeefc)
- ブロック [`00bbeefc`](#insn-00bbeefc) 範囲 `[['00bbeefc', '00bbef0b']]`
  - `CONDITIONAL_JUMP` [`00bbef08`](#insn-00bbef08) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbef08`](#insn-00bbef08) → [`00bbef0c`](#insn-00bbef0c)
- ブロック [`00bbef0c`](#insn-00bbef0c) 範囲 `[['00bbef0c', '00bbef17']]`
  - `CONDITIONAL_JUMP` [`00bbef14`](#insn-00bbef14) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbef14`](#insn-00bbef14) → [`00bbef18`](#insn-00bbef18)
- ブロック [`00bbef18`](#insn-00bbef18) 範囲 `[['00bbef18', '00bbef37']]`
  - `CONDITIONAL_JUMP` [`00bbef34`](#insn-00bbef34) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbef34`](#insn-00bbef34) → [`00bbef38`](#insn-00bbef38)
- ブロック [`00bbef38`](#insn-00bbef38) 範囲 `[['00bbef38', '00bbef43']]`
  - `CONDITIONAL_JUMP` [`00bbef40`](#insn-00bbef40) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbef40`](#insn-00bbef40) → [`00bbef44`](#insn-00bbef44)
- ブロック [`00bbef44`](#insn-00bbef44) 範囲 `[['00bbef44', '00bbef4b']]`
  - `CONDITIONAL_JUMP` [`00bbef48`](#insn-00bbef48) → [`00bbef54`](#insn-00bbef54)
  - `FALL_THROUGH` [`00bbef48`](#insn-00bbef48) → [`00bbef4c`](#insn-00bbef4c)
- ブロック [`00bbef4c`](#insn-00bbef4c) 範囲 `[['00bbef4c', '00bbef53']]`
  - `CONDITIONAL_JUMP` [`00bbef50`](#insn-00bbef50) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbef50`](#insn-00bbef50) → [`00bbef54`](#insn-00bbef54)
- ブロック [`00bbef54`](#insn-00bbef54) 範囲 `[['00bbef54', '00bbef5f']]`
  - `CONDITIONAL_JUMP` [`00bbef5c`](#insn-00bbef5c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbef5c`](#insn-00bbef5c) → [`00bbef60`](#insn-00bbef60)
- ブロック [`00bbef60`](#insn-00bbef60) 範囲 `[['00bbef60', '00bbef67']]`
  - `CONDITIONAL_JUMP` [`00bbef64`](#insn-00bbef64) → [`00bbef70`](#insn-00bbef70)
  - `FALL_THROUGH` [`00bbef64`](#insn-00bbef64) → [`00bbef68`](#insn-00bbef68)
- ブロック [`00bbef68`](#insn-00bbef68) 範囲 `[['00bbef68', '00bbef6f']]`
  - `CONDITIONAL_JUMP` [`00bbef6c`](#insn-00bbef6c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbef6c`](#insn-00bbef6c) → [`00bbef70`](#insn-00bbef70)
- ブロック [`00bbef70`](#insn-00bbef70) 範囲 `[['00bbef70', '00bbef73']]`
  - `CONDITIONAL_JUMP` [`00bbef70`](#insn-00bbef70) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbef70`](#insn-00bbef70) → [`00bbef74`](#insn-00bbef74)
- ブロック [`00bbef74`](#insn-00bbef74) 範囲 `[['00bbef74', '00bbef7f']]`
  - `CONDITIONAL_JUMP` [`00bbef7c`](#insn-00bbef7c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbef7c`](#insn-00bbef7c) → [`00bbef80`](#insn-00bbef80)
- ブロック [`00bbef80`](#insn-00bbef80) 範囲 `[['00bbef80', '00bbef87']]`
  - `CONDITIONAL_JUMP` [`00bbef84`](#insn-00bbef84) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbef84`](#insn-00bbef84) → [`00bbef88`](#insn-00bbef88)
- ブロック [`00bbef88`](#insn-00bbef88) 範囲 `[['00bbef88', '00bbef9f']]`
  - `CONDITIONAL_JUMP` [`00bbef9c`](#insn-00bbef9c) → [`00bbf358`](#insn-00bbf358)
  - `FALL_THROUGH` [`00bbef9c`](#insn-00bbef9c) → [`00bbefa0`](#insn-00bbefa0)
- ブロック [`00bbefa0`](#insn-00bbefa0) 範囲 `[['00bbefa0', '00bbefa7']]`
  - `CONDITIONAL_JUMP` [`00bbefa4`](#insn-00bbefa4) → [`00bbeff0`](#insn-00bbeff0)
  - `FALL_THROUGH` [`00bbefa4`](#insn-00bbefa4) → [`00bbefa8`](#insn-00bbefa8)
- ブロック [`00bbefa8`](#insn-00bbefa8) 範囲 `[['00bbefa8', '00bbefb3']]`
  - `CONDITIONAL_JUMP` [`00bbefb0`](#insn-00bbefb0) → [`00bbefcc`](#insn-00bbefcc)
  - `FALL_THROUGH` [`00bbefb0`](#insn-00bbefb0) → [`00bbefb4`](#insn-00bbefb4)
- ブロック [`00bbefb4`](#insn-00bbefb4) 範囲 `[['00bbefb4', '00bbefbf']]`
  - `CONDITIONAL_JUMP` [`00bbefbc`](#insn-00bbefbc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbefbc`](#insn-00bbefbc) → [`00bbefc0`](#insn-00bbefc0)
- ブロック [`00bbefc0`](#insn-00bbefc0) 範囲 `[['00bbefc0', '00bbefc7']]`
  - `CONDITIONAL_JUMP` [`00bbefc4`](#insn-00bbefc4) → [`00bbefd4`](#insn-00bbefd4)
  - `FALL_THROUGH` [`00bbefc4`](#insn-00bbefc4) → [`00bbefc8`](#insn-00bbefc8)
- ブロック [`00bbefc8`](#insn-00bbefc8) 範囲 `[['00bbefc8', '00bbefcb']]`
  - `UNCONDITIONAL_JUMP` [`00bbefc8`](#insn-00bbefc8) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbefcc`](#insn-00bbefcc) 範囲 `[['00bbefcc', '00bbefd3']]`
  - `CONDITIONAL_JUMP` [`00bbefd0`](#insn-00bbefd0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbefd0`](#insn-00bbefd0) → [`00bbefd4`](#insn-00bbefd4)
- ブロック [`00bbefd4`](#insn-00bbefd4) 範囲 `[['00bbefd4', '00bbefdf']]`
  - `CONDITIONAL_JUMP` [`00bbefdc`](#insn-00bbefdc) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbefdc`](#insn-00bbefdc) → [`00bbefe0`](#insn-00bbefe0)
- ブロック [`00bbefe0`](#insn-00bbefe0) 範囲 `[['00bbefe0', '00bbefef']]`
  - `CONDITIONAL_JUMP` [`00bbefec`](#insn-00bbefec) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbefec`](#insn-00bbefec) → [`00bbeff0`](#insn-00bbeff0)
- ブロック [`00bbeff0`](#insn-00bbeff0) 範囲 `[['00bbeff0', '00bbeff7']]`
  - `CONDITIONAL_JUMP` [`00bbeff4`](#insn-00bbeff4) → [`00bbf078`](#insn-00bbf078)
  - `FALL_THROUGH` [`00bbeff4`](#insn-00bbeff4) → [`00bbeff8`](#insn-00bbeff8)
- ブロック [`00bbeff8`](#insn-00bbeff8) 範囲 `[['00bbeff8', '00bbf007']]`
  - `CONDITIONAL_JUMP` [`00bbf004`](#insn-00bbf004) → [`00bbf078`](#insn-00bbf078)
  - `FALL_THROUGH` [`00bbf004`](#insn-00bbf004) → [`00bbf008`](#insn-00bbf008)
- ブロック [`00bbf008`](#insn-00bbf008) 範囲 `[['00bbf008', '00bbf013']]`
  - `CONDITIONAL_JUMP` [`00bbf010`](#insn-00bbf010) → [`00bbf02c`](#insn-00bbf02c)
  - `FALL_THROUGH` [`00bbf010`](#insn-00bbf010) → [`00bbf014`](#insn-00bbf014)
- ブロック [`00bbf014`](#insn-00bbf014) 範囲 `[['00bbf014', '00bbf01f']]`
  - `CONDITIONAL_JUMP` [`00bbf01c`](#insn-00bbf01c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf01c`](#insn-00bbf01c) → [`00bbf020`](#insn-00bbf020)
- ブロック [`00bbf020`](#insn-00bbf020) 範囲 `[['00bbf020', '00bbf027']]`
  - `CONDITIONAL_JUMP` [`00bbf024`](#insn-00bbf024) → [`00bbf034`](#insn-00bbf034)
  - `FALL_THROUGH` [`00bbf024`](#insn-00bbf024) → [`00bbf028`](#insn-00bbf028)
- ブロック [`00bbf028`](#insn-00bbf028) 範囲 `[['00bbf028', '00bbf02b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf028`](#insn-00bbf028) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbf02c`](#insn-00bbf02c) 範囲 `[['00bbf02c', '00bbf033']]`
  - `CONDITIONAL_JUMP` [`00bbf030`](#insn-00bbf030) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf030`](#insn-00bbf030) → [`00bbf034`](#insn-00bbf034)
- ブロック [`00bbf034`](#insn-00bbf034) 範囲 `[['00bbf034', '00bbf043']]`
  - `CONDITIONAL_JUMP` [`00bbf040`](#insn-00bbf040) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf040`](#insn-00bbf040) → [`00bbf044`](#insn-00bbf044)
- ブロック [`00bbf044`](#insn-00bbf044) 範囲 `[['00bbf044', '00bbf05b']]`
  - `CONDITIONAL_JUMP` [`00bbf058`](#insn-00bbf058) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf058`](#insn-00bbf058) → [`00bbf05c`](#insn-00bbf05c)
- ブロック [`00bbf05c`](#insn-00bbf05c) 範囲 `[['00bbf05c', '00bbf063']]`
  - `CONDITIONAL_JUMP` [`00bbf060`](#insn-00bbf060) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf060`](#insn-00bbf060) → [`00bbf064`](#insn-00bbf064)
- ブロック [`00bbf064`](#insn-00bbf064) 範囲 `[['00bbf064', '00bbf06f']]`
  - `CONDITIONAL_JUMP` [`00bbf06c`](#insn-00bbf06c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf06c`](#insn-00bbf06c) → [`00bbf070`](#insn-00bbf070)
- ブロック [`00bbf070`](#insn-00bbf070) 範囲 `[['00bbf070', '00bbf077']]`
  - `CONDITIONAL_JUMP` [`00bbf074`](#insn-00bbf074) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf074`](#insn-00bbf074) → [`00bbf078`](#insn-00bbf078)
- ブロック [`00bbf078`](#insn-00bbf078) 範囲 `[['00bbf078', '00bbf07f']]`
  - `CONDITIONAL_JUMP` [`00bbf07c`](#insn-00bbf07c) → [`00bbf358`](#insn-00bbf358)
  - `FALL_THROUGH` [`00bbf07c`](#insn-00bbf07c) → [`00bbf080`](#insn-00bbf080)
- ブロック [`00bbf080`](#insn-00bbf080) 範囲 `[['00bbf080', '00bbf087']]`
  - `CONDITIONAL_JUMP` [`00bbf084`](#insn-00bbf084) → [`00bbf0d0`](#insn-00bbf0d0)
  - `FALL_THROUGH` [`00bbf084`](#insn-00bbf084) → [`00bbf088`](#insn-00bbf088)
- ブロック [`00bbf088`](#insn-00bbf088) 範囲 `[['00bbf088', '00bbf093']]`
  - `CONDITIONAL_JUMP` [`00bbf090`](#insn-00bbf090) → [`00bbf0ac`](#insn-00bbf0ac)
  - `FALL_THROUGH` [`00bbf090`](#insn-00bbf090) → [`00bbf094`](#insn-00bbf094)
- ブロック [`00bbf094`](#insn-00bbf094) 範囲 `[['00bbf094', '00bbf09f']]`
  - `CONDITIONAL_JUMP` [`00bbf09c`](#insn-00bbf09c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf09c`](#insn-00bbf09c) → [`00bbf0a0`](#insn-00bbf0a0)
- ブロック [`00bbf0a0`](#insn-00bbf0a0) 範囲 `[['00bbf0a0', '00bbf0a7']]`
  - `CONDITIONAL_JUMP` [`00bbf0a4`](#insn-00bbf0a4) → [`00bbf0b4`](#insn-00bbf0b4)
  - `FALL_THROUGH` [`00bbf0a4`](#insn-00bbf0a4) → [`00bbf0a8`](#insn-00bbf0a8)
- ブロック [`00bbf0a8`](#insn-00bbf0a8) 範囲 `[['00bbf0a8', '00bbf0ab']]`
  - `UNCONDITIONAL_JUMP` [`00bbf0a8`](#insn-00bbf0a8) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbf0ac`](#insn-00bbf0ac) 範囲 `[['00bbf0ac', '00bbf0b3']]`
  - `CONDITIONAL_JUMP` [`00bbf0b0`](#insn-00bbf0b0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf0b0`](#insn-00bbf0b0) → [`00bbf0b4`](#insn-00bbf0b4)
- ブロック [`00bbf0b4`](#insn-00bbf0b4) 範囲 `[['00bbf0b4', '00bbf0bf']]`
  - `CONDITIONAL_JUMP` [`00bbf0bc`](#insn-00bbf0bc) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf0bc`](#insn-00bbf0bc) → [`00bbf0c0`](#insn-00bbf0c0)
- ブロック [`00bbf0c0`](#insn-00bbf0c0) 範囲 `[['00bbf0c0', '00bbf0cf']]`
  - `CONDITIONAL_JUMP` [`00bbf0cc`](#insn-00bbf0cc) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf0cc`](#insn-00bbf0cc) → [`00bbf0d0`](#insn-00bbf0d0)
- ブロック [`00bbf0d0`](#insn-00bbf0d0) 範囲 `[['00bbf0d0', '00bbf0d7']]`
  - `CONDITIONAL_JUMP` [`00bbf0d4`](#insn-00bbf0d4) → [`00bbf158`](#insn-00bbf158)
  - `FALL_THROUGH` [`00bbf0d4`](#insn-00bbf0d4) → [`00bbf0d8`](#insn-00bbf0d8)
- ブロック [`00bbf0d8`](#insn-00bbf0d8) 範囲 `[['00bbf0d8', '00bbf0e7']]`
  - `CONDITIONAL_JUMP` [`00bbf0e4`](#insn-00bbf0e4) → [`00bbf158`](#insn-00bbf158)
  - `FALL_THROUGH` [`00bbf0e4`](#insn-00bbf0e4) → [`00bbf0e8`](#insn-00bbf0e8)
- ブロック [`00bbf0e8`](#insn-00bbf0e8) 範囲 `[['00bbf0e8', '00bbf0f3']]`
  - `CONDITIONAL_JUMP` [`00bbf0f0`](#insn-00bbf0f0) → [`00bbf10c`](#insn-00bbf10c)
  - `FALL_THROUGH` [`00bbf0f0`](#insn-00bbf0f0) → [`00bbf0f4`](#insn-00bbf0f4)
- ブロック [`00bbf0f4`](#insn-00bbf0f4) 範囲 `[['00bbf0f4', '00bbf0ff']]`
  - `CONDITIONAL_JUMP` [`00bbf0fc`](#insn-00bbf0fc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf0fc`](#insn-00bbf0fc) → [`00bbf100`](#insn-00bbf100)
- ブロック [`00bbf100`](#insn-00bbf100) 範囲 `[['00bbf100', '00bbf107']]`
  - `CONDITIONAL_JUMP` [`00bbf104`](#insn-00bbf104) → [`00bbf114`](#insn-00bbf114)
  - `FALL_THROUGH` [`00bbf104`](#insn-00bbf104) → [`00bbf108`](#insn-00bbf108)
- ブロック [`00bbf108`](#insn-00bbf108) 範囲 `[['00bbf108', '00bbf10b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf108`](#insn-00bbf108) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbf10c`](#insn-00bbf10c) 範囲 `[['00bbf10c', '00bbf113']]`
  - `CONDITIONAL_JUMP` [`00bbf110`](#insn-00bbf110) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf110`](#insn-00bbf110) → [`00bbf114`](#insn-00bbf114)
- ブロック [`00bbf114`](#insn-00bbf114) 範囲 `[['00bbf114', '00bbf123']]`
  - `CONDITIONAL_JUMP` [`00bbf120`](#insn-00bbf120) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf120`](#insn-00bbf120) → [`00bbf124`](#insn-00bbf124)
- ブロック [`00bbf124`](#insn-00bbf124) 範囲 `[['00bbf124', '00bbf13b']]`
  - `CONDITIONAL_JUMP` [`00bbf138`](#insn-00bbf138) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf138`](#insn-00bbf138) → [`00bbf13c`](#insn-00bbf13c)
- ブロック [`00bbf13c`](#insn-00bbf13c) 範囲 `[['00bbf13c', '00bbf143']]`
  - `CONDITIONAL_JUMP` [`00bbf140`](#insn-00bbf140) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf140`](#insn-00bbf140) → [`00bbf144`](#insn-00bbf144)
- ブロック [`00bbf144`](#insn-00bbf144) 範囲 `[['00bbf144', '00bbf14f']]`
  - `CONDITIONAL_JUMP` [`00bbf14c`](#insn-00bbf14c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf14c`](#insn-00bbf14c) → [`00bbf150`](#insn-00bbf150)
- ブロック [`00bbf150`](#insn-00bbf150) 範囲 `[['00bbf150', '00bbf157']]`
  - `CONDITIONAL_JUMP` [`00bbf154`](#insn-00bbf154) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf154`](#insn-00bbf154) → [`00bbf158`](#insn-00bbf158)
- ブロック [`00bbf158`](#insn-00bbf158) 範囲 `[['00bbf158', '00bbf15f']]`
  - `CONDITIONAL_JUMP` [`00bbf15c`](#insn-00bbf15c) → [`00bbf358`](#insn-00bbf358)
  - `FALL_THROUGH` [`00bbf15c`](#insn-00bbf15c) → [`00bbf160`](#insn-00bbf160)
- ブロック [`00bbf160`](#insn-00bbf160) 範囲 `[['00bbf160', '00bbf163']]`
  - `FALL_THROUGH` [`00bbf160`](#insn-00bbf160) → [`00bbf164`](#insn-00bbf164)
- ブロック [`00bbf164`](#insn-00bbf164) 範囲 `[['00bbf164', '00bbf167']]`
  - `CONDITIONAL_JUMP` [`00bbf164`](#insn-00bbf164) → [`00bbf1b0`](#insn-00bbf1b0)
  - `FALL_THROUGH` [`00bbf164`](#insn-00bbf164) → [`00bbf168`](#insn-00bbf168)
- ブロック [`00bbf168`](#insn-00bbf168) 範囲 `[['00bbf168', '00bbf173']]`
  - `CONDITIONAL_JUMP` [`00bbf170`](#insn-00bbf170) → [`00bbf18c`](#insn-00bbf18c)
  - `FALL_THROUGH` [`00bbf170`](#insn-00bbf170) → [`00bbf174`](#insn-00bbf174)
- ブロック [`00bbf174`](#insn-00bbf174) 範囲 `[['00bbf174', '00bbf17f']]`
  - `CONDITIONAL_JUMP` [`00bbf17c`](#insn-00bbf17c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf17c`](#insn-00bbf17c) → [`00bbf180`](#insn-00bbf180)
- ブロック [`00bbf180`](#insn-00bbf180) 範囲 `[['00bbf180', '00bbf187']]`
  - `CONDITIONAL_JUMP` [`00bbf184`](#insn-00bbf184) → [`00bbf194`](#insn-00bbf194)
  - `FALL_THROUGH` [`00bbf184`](#insn-00bbf184) → [`00bbf188`](#insn-00bbf188)
- ブロック [`00bbf188`](#insn-00bbf188) 範囲 `[['00bbf188', '00bbf18b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf188`](#insn-00bbf188) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbf18c`](#insn-00bbf18c) 範囲 `[['00bbf18c', '00bbf193']]`
  - `CONDITIONAL_JUMP` [`00bbf190`](#insn-00bbf190) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf190`](#insn-00bbf190) → [`00bbf194`](#insn-00bbf194)
- ブロック [`00bbf194`](#insn-00bbf194) 範囲 `[['00bbf194', '00bbf19f']]`
  - `CONDITIONAL_JUMP` [`00bbf19c`](#insn-00bbf19c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf19c`](#insn-00bbf19c) → [`00bbf1a0`](#insn-00bbf1a0)
- ブロック [`00bbf1a0`](#insn-00bbf1a0) 範囲 `[['00bbf1a0', '00bbf1af']]`
  - `CONDITIONAL_JUMP` [`00bbf1ac`](#insn-00bbf1ac) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf1ac`](#insn-00bbf1ac) → [`00bbf1b0`](#insn-00bbf1b0)
- ブロック [`00bbf1b0`](#insn-00bbf1b0) 範囲 `[['00bbf1b0', '00bbf1b7']]`
  - `CONDITIONAL_JUMP` [`00bbf1b4`](#insn-00bbf1b4) → [`00bbf238`](#insn-00bbf238)
  - `FALL_THROUGH` [`00bbf1b4`](#insn-00bbf1b4) → [`00bbf1b8`](#insn-00bbf1b8)
- ブロック [`00bbf1b8`](#insn-00bbf1b8) 範囲 `[['00bbf1b8', '00bbf1bb']]`
  - `FALL_THROUGH` [`00bbf1b8`](#insn-00bbf1b8) → [`00bbf1bc`](#insn-00bbf1bc)
- ブロック [`00bbf1bc`](#insn-00bbf1bc) 範囲 `[['00bbf1bc', '00bbf1c7']]`
  - `CONDITIONAL_JUMP` [`00bbf1c4`](#insn-00bbf1c4) → [`00bbf238`](#insn-00bbf238)
  - `FALL_THROUGH` [`00bbf1c4`](#insn-00bbf1c4) → [`00bbf1c8`](#insn-00bbf1c8)
- ブロック [`00bbf1c8`](#insn-00bbf1c8) 範囲 `[['00bbf1c8', '00bbf1d3']]`
  - `CONDITIONAL_JUMP` [`00bbf1d0`](#insn-00bbf1d0) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbf1d0`](#insn-00bbf1d0) → [`00bbf1d4`](#insn-00bbf1d4)
- ブロック [`00bbf1d4`](#insn-00bbf1d4) 範囲 `[['00bbf1d4', '00bbf1df']]`
  - `CONDITIONAL_JUMP` [`00bbf1dc`](#insn-00bbf1dc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf1dc`](#insn-00bbf1dc) → [`00bbf1e0`](#insn-00bbf1e0)
- ブロック [`00bbf1e0`](#insn-00bbf1e0) 範囲 `[['00bbf1e0', '00bbf1e7']]`
  - `CONDITIONAL_JUMP` [`00bbf1e4`](#insn-00bbf1e4) → [`00bbf1f4`](#insn-00bbf1f4)
  - `FALL_THROUGH` [`00bbf1e4`](#insn-00bbf1e4) → [`00bbf1e8`](#insn-00bbf1e8)
- ブロック [`00bbf1e8`](#insn-00bbf1e8) 範囲 `[['00bbf1e8', '00bbf1eb']]`
  - `UNCONDITIONAL_JUMP` [`00bbf1e8`](#insn-00bbf1e8) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbf1ec`](#insn-00bbf1ec) 範囲 `[['00bbf1ec', '00bbf1f3']]`
  - `CONDITIONAL_JUMP` [`00bbf1f0`](#insn-00bbf1f0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf1f0`](#insn-00bbf1f0) → [`00bbf1f4`](#insn-00bbf1f4)
- ブロック [`00bbf1f4`](#insn-00bbf1f4) 範囲 `[['00bbf1f4', '00bbf203']]`
  - `CONDITIONAL_JUMP` [`00bbf200`](#insn-00bbf200) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf200`](#insn-00bbf200) → [`00bbf204`](#insn-00bbf204)
- ブロック [`00bbf204`](#insn-00bbf204) 範囲 `[['00bbf204', '00bbf21b']]`
  - `CONDITIONAL_JUMP` [`00bbf218`](#insn-00bbf218) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf218`](#insn-00bbf218) → [`00bbf21c`](#insn-00bbf21c)
- ブロック [`00bbf21c`](#insn-00bbf21c) 範囲 `[['00bbf21c', '00bbf223']]`
  - `CONDITIONAL_JUMP` [`00bbf220`](#insn-00bbf220) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf220`](#insn-00bbf220) → [`00bbf224`](#insn-00bbf224)
- ブロック [`00bbf224`](#insn-00bbf224) 範囲 `[['00bbf224', '00bbf22f']]`
  - `CONDITIONAL_JUMP` [`00bbf22c`](#insn-00bbf22c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf22c`](#insn-00bbf22c) → [`00bbf230`](#insn-00bbf230)
- ブロック [`00bbf230`](#insn-00bbf230) 範囲 `[['00bbf230', '00bbf237']]`
  - `CONDITIONAL_JUMP` [`00bbf234`](#insn-00bbf234) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf234`](#insn-00bbf234) → [`00bbf238`](#insn-00bbf238)
- ブロック [`00bbf238`](#insn-00bbf238) 範囲 `[['00bbf238', '00bbf23f']]`
  - `CONDITIONAL_JUMP` [`00bbf23c`](#insn-00bbf23c) → [`00bbf358`](#insn-00bbf358)
  - `FALL_THROUGH` [`00bbf23c`](#insn-00bbf23c) → [`00bbf240`](#insn-00bbf240)
- ブロック [`00bbf240`](#insn-00bbf240) 範囲 `[['00bbf240', '00bbf247']]`
  - `CONDITIONAL_JUMP` [`00bbf244`](#insn-00bbf244) → [`00bbf290`](#insn-00bbf290)
  - `FALL_THROUGH` [`00bbf244`](#insn-00bbf244) → [`00bbf248`](#insn-00bbf248)
- ブロック [`00bbf248`](#insn-00bbf248) 範囲 `[['00bbf248', '00bbf253']]`
  - `CONDITIONAL_JUMP` [`00bbf250`](#insn-00bbf250) → [`00bbf26c`](#insn-00bbf26c)
  - `FALL_THROUGH` [`00bbf250`](#insn-00bbf250) → [`00bbf254`](#insn-00bbf254)
- ブロック [`00bbf254`](#insn-00bbf254) 範囲 `[['00bbf254', '00bbf25f']]`
  - `CONDITIONAL_JUMP` [`00bbf25c`](#insn-00bbf25c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf25c`](#insn-00bbf25c) → [`00bbf260`](#insn-00bbf260)
- ブロック [`00bbf260`](#insn-00bbf260) 範囲 `[['00bbf260', '00bbf267']]`
  - `CONDITIONAL_JUMP` [`00bbf264`](#insn-00bbf264) → [`00bbf274`](#insn-00bbf274)
  - `FALL_THROUGH` [`00bbf264`](#insn-00bbf264) → [`00bbf268`](#insn-00bbf268)
- ブロック [`00bbf268`](#insn-00bbf268) 範囲 `[['00bbf268', '00bbf26b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf268`](#insn-00bbf268) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbf26c`](#insn-00bbf26c) 範囲 `[['00bbf26c', '00bbf273']]`
  - `CONDITIONAL_JUMP` [`00bbf270`](#insn-00bbf270) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf270`](#insn-00bbf270) → [`00bbf274`](#insn-00bbf274)
- ブロック [`00bbf274`](#insn-00bbf274) 範囲 `[['00bbf274', '00bbf27f']]`
  - `CONDITIONAL_JUMP` [`00bbf27c`](#insn-00bbf27c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf27c`](#insn-00bbf27c) → [`00bbf280`](#insn-00bbf280)
- ブロック [`00bbf280`](#insn-00bbf280) 範囲 `[['00bbf280', '00bbf28f']]`
  - `CONDITIONAL_JUMP` [`00bbf28c`](#insn-00bbf28c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf28c`](#insn-00bbf28c) → [`00bbf290`](#insn-00bbf290)
- ブロック [`00bbf290`](#insn-00bbf290) 範囲 `[['00bbf290', '00bbf297']]`
  - `CONDITIONAL_JUMP` [`00bbf294`](#insn-00bbf294) → [`00bbf358`](#insn-00bbf358)
  - `FALL_THROUGH` [`00bbf294`](#insn-00bbf294) → [`00bbf298`](#insn-00bbf298)
- ブロック [`00bbf298`](#insn-00bbf298) 範囲 `[['00bbf298', '00bbf2a7']]`
  - `CONDITIONAL_JUMP` [`00bbf2a4`](#insn-00bbf2a4) → [`00bbf300`](#insn-00bbf300)
  - `FALL_THROUGH` [`00bbf2a4`](#insn-00bbf2a4) → [`00bbf2a8`](#insn-00bbf2a8)
- ブロック [`00bbf2a8`](#insn-00bbf2a8) 範囲 `[['00bbf2a8', '00bbf2b3']]`
  - `CONDITIONAL_JUMP` [`00bbf2b0`](#insn-00bbf2b0) → [`00bbf2cc`](#insn-00bbf2cc)
  - `FALL_THROUGH` [`00bbf2b0`](#insn-00bbf2b0) → [`00bbf2b4`](#insn-00bbf2b4)
- ブロック [`00bbf2b4`](#insn-00bbf2b4) 範囲 `[['00bbf2b4', '00bbf2bf']]`
  - `CONDITIONAL_JUMP` [`00bbf2bc`](#insn-00bbf2bc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf2bc`](#insn-00bbf2bc) → [`00bbf2c0`](#insn-00bbf2c0)
- ブロック [`00bbf2c0`](#insn-00bbf2c0) 範囲 `[['00bbf2c0', '00bbf2c7']]`
  - `CONDITIONAL_JUMP` [`00bbf2c4`](#insn-00bbf2c4) → [`00bbf2d4`](#insn-00bbf2d4)
  - `FALL_THROUGH` [`00bbf2c4`](#insn-00bbf2c4) → [`00bbf2c8`](#insn-00bbf2c8)
- ブロック [`00bbf2c8`](#insn-00bbf2c8) 範囲 `[['00bbf2c8', '00bbf2cb']]`
  - `UNCONDITIONAL_JUMP` [`00bbf2c8`](#insn-00bbf2c8) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbf2cc`](#insn-00bbf2cc) 範囲 `[['00bbf2cc', '00bbf2d3']]`
  - `CONDITIONAL_JUMP` [`00bbf2d0`](#insn-00bbf2d0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf2d0`](#insn-00bbf2d0) → [`00bbf2d4`](#insn-00bbf2d4)
- ブロック [`00bbf2d4`](#insn-00bbf2d4) 範囲 `[['00bbf2d4', '00bbf2e3']]`
  - `CONDITIONAL_JUMP` [`00bbf2e0`](#insn-00bbf2e0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf2e0`](#insn-00bbf2e0) → [`00bbf2e4`](#insn-00bbf2e4)
- ブロック [`00bbf2e4`](#insn-00bbf2e4) 範囲 `[['00bbf2e4', '00bbf2f7']]`
  - `CONDITIONAL_JUMP` [`00bbf2f4`](#insn-00bbf2f4) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf2f4`](#insn-00bbf2f4) → [`00bbf2f8`](#insn-00bbf2f8)
- ブロック [`00bbf2f8`](#insn-00bbf2f8) 範囲 `[['00bbf2f8', '00bbf2ff']]`
  - `CONDITIONAL_JUMP` [`00bbf2fc`](#insn-00bbf2fc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf2fc`](#insn-00bbf2fc) → [`00bbf300`](#insn-00bbf300)
- ブロック [`00bbf300`](#insn-00bbf300) 範囲 `[['00bbf300', '00bbf30b']]`
  - `CONDITIONAL_JUMP` [`00bbf308`](#insn-00bbf308) → [`00bbf358`](#insn-00bbf358)
  - `FALL_THROUGH` [`00bbf308`](#insn-00bbf308) → [`00bbf30c`](#insn-00bbf30c)
- ブロック [`00bbf30c`](#insn-00bbf30c) 範囲 `[['00bbf30c', '00bbf313']]`
  - `CONDITIONAL_JUMP` [`00bbf310`](#insn-00bbf310) → [`00bbf358`](#insn-00bbf358)
  - `FALL_THROUGH` [`00bbf310`](#insn-00bbf310) → [`00bbf314`](#insn-00bbf314)
- ブロック [`00bbf314`](#insn-00bbf314) 範囲 `[['00bbf314', '00bbf31f']]`
  - `FALL_THROUGH` [`00bbf31c`](#insn-00bbf31c) → [`00bbf320`](#insn-00bbf320)
- ブロック [`00bbf320`](#insn-00bbf320) 範囲 `[['00bbf320', '00bbf33b']]`
  - `CONDITIONAL_JUMP` [`00bbf338`](#insn-00bbf338) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf338`](#insn-00bbf338) → [`00bbf33c`](#insn-00bbf33c)
- ブロック [`00bbf33c`](#insn-00bbf33c) 範囲 `[['00bbf33c', '00bbf34f']]`
  - `CONDITIONAL_JUMP` [`00bbf34c`](#insn-00bbf34c) → [`00bbf320`](#insn-00bbf320)
  - `FALL_THROUGH` [`00bbf34c`](#insn-00bbf34c) → [`00bbf350`](#insn-00bbf350)
- ブロック [`00bbf350`](#insn-00bbf350) 範囲 `[['00bbf350', '00bbf357']]`
  - `FALL_THROUGH` [`00bbf354`](#insn-00bbf354) → [`00bbf358`](#insn-00bbf358)
- ブロック [`00bbf358`](#insn-00bbf358) 範囲 `[['00bbf358', '00bbf367']]`
  - `CONDITIONAL_JUMP` [`00bbf364`](#insn-00bbf364) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf364`](#insn-00bbf364) → [`00bbf368`](#insn-00bbf368)
- ブロック [`00bbf368`](#insn-00bbf368) 範囲 `[['00bbf368', '00bbf36f']]`
  - `CONDITIONAL_JUMP` [`00bbf36c`](#insn-00bbf36c) → [`00bbf3c4`](#insn-00bbf3c4)
  - `FALL_THROUGH` [`00bbf36c`](#insn-00bbf36c) → [`00bbf370`](#insn-00bbf370)
- ブロック [`00bbf370`](#insn-00bbf370) 範囲 `[['00bbf370', '00bbf383']]`
  - `CONDITIONAL_JUMP` [`00bbf380`](#insn-00bbf380) → [`00bbf38c`](#insn-00bbf38c)
  - `FALL_THROUGH` [`00bbf380`](#insn-00bbf380) → [`00bbf384`](#insn-00bbf384)
- ブロック [`00bbf384`](#insn-00bbf384) 範囲 `[['00bbf384', '00bbf38b']]`
  - `CONDITIONAL_JUMP` [`00bbf388`](#insn-00bbf388) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf388`](#insn-00bbf388) → [`00bbf38c`](#insn-00bbf38c)
- ブロック [`00bbf38c`](#insn-00bbf38c) 範囲 `[['00bbf38c', '00bbf39b']]`
  - `CONDITIONAL_JUMP` [`00bbf398`](#insn-00bbf398) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf398`](#insn-00bbf398) → [`00bbf39c`](#insn-00bbf39c)
- ブロック [`00bbf39c`](#insn-00bbf39c) 範囲 `[['00bbf39c', '00bbf3a7']]`
  - `CONDITIONAL_JUMP` [`00bbf3a4`](#insn-00bbf3a4) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf3a4`](#insn-00bbf3a4) → [`00bbf3a8`](#insn-00bbf3a8)
- ブロック [`00bbf3a8`](#insn-00bbf3a8) 範囲 `[['00bbf3a8', '00bbf3b3']]`
  - `CONDITIONAL_JUMP` [`00bbf3b0`](#insn-00bbf3b0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf3b0`](#insn-00bbf3b0) → [`00bbf3b4`](#insn-00bbf3b4)
- ブロック [`00bbf3b4`](#insn-00bbf3b4) 範囲 `[['00bbf3b4', '00bbf3c3']]`
  - `CONDITIONAL_JUMP` [`00bbf3c0`](#insn-00bbf3c0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf3c0`](#insn-00bbf3c0) → [`00bbf3c4`](#insn-00bbf3c4)
- ブロック [`00bbf3c4`](#insn-00bbf3c4) 範囲 `[['00bbf3c4', '00bbf3cb']]`
  - `CONDITIONAL_JUMP` [`00bbf3c8`](#insn-00bbf3c8) → [`00bbf438`](#insn-00bbf438)
  - `FALL_THROUGH` [`00bbf3c8`](#insn-00bbf3c8) → [`00bbf3cc`](#insn-00bbf3cc)
- ブロック [`00bbf3cc`](#insn-00bbf3cc) 範囲 `[['00bbf3cc', '00bbf3db']]`
  - `CONDITIONAL_JUMP` [`00bbf3d8`](#insn-00bbf3d8) → [`00bbf438`](#insn-00bbf438)
  - `FALL_THROUGH` [`00bbf3d8`](#insn-00bbf3d8) → [`00bbf3dc`](#insn-00bbf3dc)
- ブロック [`00bbf3dc`](#insn-00bbf3dc) 範囲 `[['00bbf3dc', '00bbf3eb']]`
  - `CONDITIONAL_JUMP` [`00bbf3e8`](#insn-00bbf3e8) → [`00bbf3f4`](#insn-00bbf3f4)
  - `FALL_THROUGH` [`00bbf3e8`](#insn-00bbf3e8) → [`00bbf3ec`](#insn-00bbf3ec)
- ブロック [`00bbf3ec`](#insn-00bbf3ec) 範囲 `[['00bbf3ec', '00bbf3f3']]`
  - `CONDITIONAL_JUMP` [`00bbf3f0`](#insn-00bbf3f0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf3f0`](#insn-00bbf3f0) → [`00bbf3f4`](#insn-00bbf3f4)
- ブロック [`00bbf3f4`](#insn-00bbf3f4) 範囲 `[['00bbf3f4', '00bbf403']]`
  - `CONDITIONAL_JUMP` [`00bbf400`](#insn-00bbf400) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf400`](#insn-00bbf400) → [`00bbf404`](#insn-00bbf404)
- ブロック [`00bbf404`](#insn-00bbf404) 範囲 `[['00bbf404', '00bbf407']]`
  - `FALL_THROUGH` [`00bbf404`](#insn-00bbf404) → [`00bbf408`](#insn-00bbf408)
- ブロック [`00bbf408`](#insn-00bbf408) 範囲 `[['00bbf408', '00bbf40f']]`
  - `CONDITIONAL_JUMP` [`00bbf40c`](#insn-00bbf40c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf40c`](#insn-00bbf40c) → [`00bbf410`](#insn-00bbf410)
- ブロック [`00bbf410`](#insn-00bbf410) 範囲 `[['00bbf410', '00bbf41f']]`
  - `CONDITIONAL_JUMP` [`00bbf41c`](#insn-00bbf41c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf41c`](#insn-00bbf41c) → [`00bbf420`](#insn-00bbf420)
- ブロック [`00bbf420`](#insn-00bbf420) 範囲 `[['00bbf420', '00bbf423']]`
  - `FALL_THROUGH` [`00bbf420`](#insn-00bbf420) → [`00bbf424`](#insn-00bbf424)
- ブロック [`00bbf424`](#insn-00bbf424) 範囲 `[['00bbf424', '00bbf427']]`
  - `FALL_THROUGH` [`00bbf424`](#insn-00bbf424) → [`00bbf428`](#insn-00bbf428)
- ブロック [`00bbf428`](#insn-00bbf428) 範囲 `[['00bbf428', '00bbf42f']]`
  - `CONDITIONAL_JUMP` [`00bbf42c`](#insn-00bbf42c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf42c`](#insn-00bbf42c) → [`00bbf430`](#insn-00bbf430)
- ブロック [`00bbf430`](#insn-00bbf430) 範囲 `[['00bbf430', '00bbf437']]`
  - `CONDITIONAL_JUMP` [`00bbf434`](#insn-00bbf434) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf434`](#insn-00bbf434) → [`00bbf438`](#insn-00bbf438)
- ブロック [`00bbf438`](#insn-00bbf438) 範囲 `[['00bbf438', '00bbf43f']]`
  - `CONDITIONAL_JUMP` [`00bbf43c`](#insn-00bbf43c) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf43c`](#insn-00bbf43c) → [`00bbf440`](#insn-00bbf440)
- ブロック [`00bbf440`](#insn-00bbf440) 範囲 `[['00bbf440', '00bbf447']]`
  - `CONDITIONAL_JUMP` [`00bbf444`](#insn-00bbf444) → [`00bbf49c`](#insn-00bbf49c)
  - `FALL_THROUGH` [`00bbf444`](#insn-00bbf444) → [`00bbf448`](#insn-00bbf448)
- ブロック [`00bbf448`](#insn-00bbf448) 範囲 `[['00bbf448', '00bbf44f']]`
  - `FALL_THROUGH` [`00bbf44c`](#insn-00bbf44c) → [`00bbf450`](#insn-00bbf450)
- ブロック [`00bbf450`](#insn-00bbf450) 範囲 `[['00bbf450', '00bbf453']]`
  - `FALL_THROUGH` [`00bbf450`](#insn-00bbf450) → [`00bbf454`](#insn-00bbf454)
- ブロック [`00bbf454`](#insn-00bbf454) 範囲 `[['00bbf454', '00bbf45b']]`
  - `CONDITIONAL_JUMP` [`00bbf458`](#insn-00bbf458) → [`00bbf464`](#insn-00bbf464)
  - `FALL_THROUGH` [`00bbf458`](#insn-00bbf458) → [`00bbf45c`](#insn-00bbf45c)
- ブロック [`00bbf45c`](#insn-00bbf45c) 範囲 `[['00bbf45c', '00bbf463']]`
  - `CONDITIONAL_JUMP` [`00bbf460`](#insn-00bbf460) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf460`](#insn-00bbf460) → [`00bbf464`](#insn-00bbf464)
- ブロック [`00bbf464`](#insn-00bbf464) 範囲 `[['00bbf464', '00bbf473']]`
  - `CONDITIONAL_JUMP` [`00bbf470`](#insn-00bbf470) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf470`](#insn-00bbf470) → [`00bbf474`](#insn-00bbf474)
- ブロック [`00bbf474`](#insn-00bbf474) 範囲 `[['00bbf474', '00bbf47f']]`
  - `CONDITIONAL_JUMP` [`00bbf47c`](#insn-00bbf47c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf47c`](#insn-00bbf47c) → [`00bbf480`](#insn-00bbf480)
- ブロック [`00bbf480`](#insn-00bbf480) 範囲 `[['00bbf480', '00bbf48b']]`
  - `CONDITIONAL_JUMP` [`00bbf488`](#insn-00bbf488) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf488`](#insn-00bbf488) → [`00bbf48c`](#insn-00bbf48c)
- ブロック [`00bbf48c`](#insn-00bbf48c) 範囲 `[['00bbf48c', '00bbf497']]`
  - `FALL_THROUGH` [`00bbf494`](#insn-00bbf494) → [`00bbf498`](#insn-00bbf498)
- ブロック [`00bbf498`](#insn-00bbf498) 範囲 `[['00bbf498', '00bbf49b']]`
  - `CONDITIONAL_JUMP` [`00bbf498`](#insn-00bbf498) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf498`](#insn-00bbf498) → [`00bbf49c`](#insn-00bbf49c)
- ブロック [`00bbf49c`](#insn-00bbf49c) 範囲 `[['00bbf49c', '00bbf4a3']]`
  - `CONDITIONAL_JUMP` [`00bbf4a0`](#insn-00bbf4a0) → [`00bbf52c`](#insn-00bbf52c)
  - `FALL_THROUGH` [`00bbf4a0`](#insn-00bbf4a0) → [`00bbf4a4`](#insn-00bbf4a4)
- ブロック [`00bbf4a4`](#insn-00bbf4a4) 範囲 `[['00bbf4a4', '00bbf4af']]`
  - `FALL_THROUGH` [`00bbf4ac`](#insn-00bbf4ac) → [`00bbf4b0`](#insn-00bbf4b0)
- ブロック [`00bbf4b0`](#insn-00bbf4b0) 範囲 `[['00bbf4b0', '00bbf4b3']]`
  - `CONDITIONAL_JUMP` [`00bbf4b0`](#insn-00bbf4b0) → [`00bbf52c`](#insn-00bbf52c)
  - `FALL_THROUGH` [`00bbf4b0`](#insn-00bbf4b0) → [`00bbf4b4`](#insn-00bbf4b4)
- ブロック [`00bbf4b4`](#insn-00bbf4b4) 範囲 `[['00bbf4b4', '00bbf4c3']]`
  - `CONDITIONAL_JUMP` [`00bbf4c0`](#insn-00bbf4c0) → [`00bbf4cc`](#insn-00bbf4cc)
  - `FALL_THROUGH` [`00bbf4c0`](#insn-00bbf4c0) → [`00bbf4c4`](#insn-00bbf4c4)
- ブロック [`00bbf4c4`](#insn-00bbf4c4) 範囲 `[['00bbf4c4', '00bbf4cb']]`
  - `CONDITIONAL_JUMP` [`00bbf4c8`](#insn-00bbf4c8) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf4c8`](#insn-00bbf4c8) → [`00bbf4cc`](#insn-00bbf4cc)
- ブロック [`00bbf4cc`](#insn-00bbf4cc) 範囲 `[['00bbf4cc', '00bbf4db']]`
  - `CONDITIONAL_JUMP` [`00bbf4d8`](#insn-00bbf4d8) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf4d8`](#insn-00bbf4d8) → [`00bbf4dc`](#insn-00bbf4dc)
- ブロック [`00bbf4dc`](#insn-00bbf4dc) 範囲 `[['00bbf4dc', '00bbf4e7']]`
  - `CONDITIONAL_JUMP` [`00bbf4e4`](#insn-00bbf4e4) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf4e4`](#insn-00bbf4e4) → [`00bbf4e8`](#insn-00bbf4e8)
- ブロック [`00bbf4e8`](#insn-00bbf4e8) 範囲 `[['00bbf4e8', '00bbf4f3']]`
  - `FALL_THROUGH` [`00bbf4f0`](#insn-00bbf4f0) → [`00bbf4f4`](#insn-00bbf4f4)
- ブロック [`00bbf4f4`](#insn-00bbf4f4) 範囲 `[['00bbf4f4', '00bbf4f7']]`
  - `CONDITIONAL_JUMP` [`00bbf4f4`](#insn-00bbf4f4) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf4f4`](#insn-00bbf4f4) → [`00bbf4f8`](#insn-00bbf4f8)
- ブロック [`00bbf4f8`](#insn-00bbf4f8) 範囲 `[['00bbf4f8', '00bbf50f']]`
  - `CONDITIONAL_JUMP` [`00bbf50c`](#insn-00bbf50c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf50c`](#insn-00bbf50c) → [`00bbf510`](#insn-00bbf510)
- ブロック [`00bbf510`](#insn-00bbf510) 範囲 `[['00bbf510', '00bbf517']]`
  - `CONDITIONAL_JUMP` [`00bbf514`](#insn-00bbf514) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf514`](#insn-00bbf514) → [`00bbf518`](#insn-00bbf518)
- ブロック [`00bbf518`](#insn-00bbf518) 範囲 `[['00bbf518', '00bbf523']]`
  - `CONDITIONAL_JUMP` [`00bbf520`](#insn-00bbf520) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf520`](#insn-00bbf520) → [`00bbf524`](#insn-00bbf524)
- ブロック [`00bbf524`](#insn-00bbf524) 範囲 `[['00bbf524', '00bbf52b']]`
  - `CONDITIONAL_JUMP` [`00bbf528`](#insn-00bbf528) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf528`](#insn-00bbf528) → [`00bbf52c`](#insn-00bbf52c)
- ブロック [`00bbf52c`](#insn-00bbf52c) 範囲 `[['00bbf52c', '00bbf533']]`
  - `CONDITIONAL_JUMP` [`00bbf530`](#insn-00bbf530) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf530`](#insn-00bbf530) → [`00bbf534`](#insn-00bbf534)
- ブロック [`00bbf534`](#insn-00bbf534) 範囲 `[['00bbf534', '00bbf53b']]`
  - `CONDITIONAL_JUMP` [`00bbf538`](#insn-00bbf538) → [`00bbf590`](#insn-00bbf590)
  - `FALL_THROUGH` [`00bbf538`](#insn-00bbf538) → [`00bbf53c`](#insn-00bbf53c)
- ブロック [`00bbf53c`](#insn-00bbf53c) 範囲 `[['00bbf53c', '00bbf54f']]`
  - `CONDITIONAL_JUMP` [`00bbf54c`](#insn-00bbf54c) → [`00bbf558`](#insn-00bbf558)
  - `FALL_THROUGH` [`00bbf54c`](#insn-00bbf54c) → [`00bbf550`](#insn-00bbf550)
- ブロック [`00bbf550`](#insn-00bbf550) 範囲 `[['00bbf550', '00bbf557']]`
  - `CONDITIONAL_JUMP` [`00bbf554`](#insn-00bbf554) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf554`](#insn-00bbf554) → [`00bbf558`](#insn-00bbf558)
- ブロック [`00bbf558`](#insn-00bbf558) 範囲 `[['00bbf558', '00bbf567']]`
  - `CONDITIONAL_JUMP` [`00bbf564`](#insn-00bbf564) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf564`](#insn-00bbf564) → [`00bbf568`](#insn-00bbf568)
- ブロック [`00bbf568`](#insn-00bbf568) 範囲 `[['00bbf568', '00bbf573']]`
  - `CONDITIONAL_JUMP` [`00bbf570`](#insn-00bbf570) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf570`](#insn-00bbf570) → [`00bbf574`](#insn-00bbf574)
- ブロック [`00bbf574`](#insn-00bbf574) 範囲 `[['00bbf574', '00bbf57f']]`
  - `CONDITIONAL_JUMP` [`00bbf57c`](#insn-00bbf57c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf57c`](#insn-00bbf57c) → [`00bbf580`](#insn-00bbf580)
- ブロック [`00bbf580`](#insn-00bbf580) 範囲 `[['00bbf580', '00bbf58f']]`
  - `CONDITIONAL_JUMP` [`00bbf58c`](#insn-00bbf58c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf58c`](#insn-00bbf58c) → [`00bbf590`](#insn-00bbf590)
- ブロック [`00bbf590`](#insn-00bbf590) 範囲 `[['00bbf590', '00bbf597']]`
  - `CONDITIONAL_JUMP` [`00bbf594`](#insn-00bbf594) → [`00bbf620`](#insn-00bbf620)
  - `FALL_THROUGH` [`00bbf594`](#insn-00bbf594) → [`00bbf598`](#insn-00bbf598)
- ブロック [`00bbf598`](#insn-00bbf598) 範囲 `[['00bbf598', '00bbf5a7']]`
  - `CONDITIONAL_JUMP` [`00bbf5a4`](#insn-00bbf5a4) → [`00bbf620`](#insn-00bbf620)
  - `FALL_THROUGH` [`00bbf5a4`](#insn-00bbf5a4) → [`00bbf5a8`](#insn-00bbf5a8)
- ブロック [`00bbf5a8`](#insn-00bbf5a8) 範囲 `[['00bbf5a8', '00bbf5b7']]`
  - `CONDITIONAL_JUMP` [`00bbf5b4`](#insn-00bbf5b4) → [`00bbf5c0`](#insn-00bbf5c0)
  - `FALL_THROUGH` [`00bbf5b4`](#insn-00bbf5b4) → [`00bbf5b8`](#insn-00bbf5b8)
- ブロック [`00bbf5b8`](#insn-00bbf5b8) 範囲 `[['00bbf5b8', '00bbf5bf']]`
  - `CONDITIONAL_JUMP` [`00bbf5bc`](#insn-00bbf5bc) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf5bc`](#insn-00bbf5bc) → [`00bbf5c0`](#insn-00bbf5c0)
- ブロック [`00bbf5c0`](#insn-00bbf5c0) 範囲 `[['00bbf5c0', '00bbf5cf']]`
  - `CONDITIONAL_JUMP` [`00bbf5cc`](#insn-00bbf5cc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf5cc`](#insn-00bbf5cc) → [`00bbf5d0`](#insn-00bbf5d0)
- ブロック [`00bbf5d0`](#insn-00bbf5d0) 範囲 `[['00bbf5d0', '00bbf5db']]`
  - `CONDITIONAL_JUMP` [`00bbf5d8`](#insn-00bbf5d8) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf5d8`](#insn-00bbf5d8) → [`00bbf5dc`](#insn-00bbf5dc)
- ブロック [`00bbf5dc`](#insn-00bbf5dc) 範囲 `[['00bbf5dc', '00bbf5eb']]`
  - `CONDITIONAL_JUMP` [`00bbf5e8`](#insn-00bbf5e8) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf5e8`](#insn-00bbf5e8) → [`00bbf5ec`](#insn-00bbf5ec)
- ブロック [`00bbf5ec`](#insn-00bbf5ec) 範囲 `[['00bbf5ec', '00bbf603']]`
  - `CONDITIONAL_JUMP` [`00bbf600`](#insn-00bbf600) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf600`](#insn-00bbf600) → [`00bbf604`](#insn-00bbf604)
- ブロック [`00bbf604`](#insn-00bbf604) 範囲 `[['00bbf604', '00bbf60b']]`
  - `CONDITIONAL_JUMP` [`00bbf608`](#insn-00bbf608) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf608`](#insn-00bbf608) → [`00bbf60c`](#insn-00bbf60c)
- ブロック [`00bbf60c`](#insn-00bbf60c) 範囲 `[['00bbf60c', '00bbf617']]`
  - `CONDITIONAL_JUMP` [`00bbf614`](#insn-00bbf614) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf614`](#insn-00bbf614) → [`00bbf618`](#insn-00bbf618)
- ブロック [`00bbf618`](#insn-00bbf618) 範囲 `[['00bbf618', '00bbf61f']]`
  - `CONDITIONAL_JUMP` [`00bbf61c`](#insn-00bbf61c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf61c`](#insn-00bbf61c) → [`00bbf620`](#insn-00bbf620)
- ブロック [`00bbf620`](#insn-00bbf620) 範囲 `[['00bbf620', '00bbf627']]`
  - `CONDITIONAL_JUMP` [`00bbf624`](#insn-00bbf624) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf624`](#insn-00bbf624) → [`00bbf628`](#insn-00bbf628)
- ブロック [`00bbf628`](#insn-00bbf628) 範囲 `[['00bbf628', '00bbf62f']]`
  - `CONDITIONAL_JUMP` [`00bbf62c`](#insn-00bbf62c) → [`00bbf684`](#insn-00bbf684)
  - `FALL_THROUGH` [`00bbf62c`](#insn-00bbf62c) → [`00bbf630`](#insn-00bbf630)
- ブロック [`00bbf630`](#insn-00bbf630) 範囲 `[['00bbf630', '00bbf643']]`
  - `CONDITIONAL_JUMP` [`00bbf640`](#insn-00bbf640) → [`00bbf64c`](#insn-00bbf64c)
  - `FALL_THROUGH` [`00bbf640`](#insn-00bbf640) → [`00bbf644`](#insn-00bbf644)
- ブロック [`00bbf644`](#insn-00bbf644) 範囲 `[['00bbf644', '00bbf64b']]`
  - `CONDITIONAL_JUMP` [`00bbf648`](#insn-00bbf648) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf648`](#insn-00bbf648) → [`00bbf64c`](#insn-00bbf64c)
- ブロック [`00bbf64c`](#insn-00bbf64c) 範囲 `[['00bbf64c', '00bbf65b']]`
  - `CONDITIONAL_JUMP` [`00bbf658`](#insn-00bbf658) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf658`](#insn-00bbf658) → [`00bbf65c`](#insn-00bbf65c)
- ブロック [`00bbf65c`](#insn-00bbf65c) 範囲 `[['00bbf65c', '00bbf667']]`
  - `CONDITIONAL_JUMP` [`00bbf664`](#insn-00bbf664) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf664`](#insn-00bbf664) → [`00bbf668`](#insn-00bbf668)
- ブロック [`00bbf668`](#insn-00bbf668) 範囲 `[['00bbf668', '00bbf673']]`
  - `CONDITIONAL_JUMP` [`00bbf670`](#insn-00bbf670) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf670`](#insn-00bbf670) → [`00bbf674`](#insn-00bbf674)
- ブロック [`00bbf674`](#insn-00bbf674) 範囲 `[['00bbf674', '00bbf683']]`
  - `CONDITIONAL_JUMP` [`00bbf680`](#insn-00bbf680) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf680`](#insn-00bbf680) → [`00bbf684`](#insn-00bbf684)
- ブロック [`00bbf684`](#insn-00bbf684) 範囲 `[['00bbf684', '00bbf68b']]`
  - `CONDITIONAL_JUMP` [`00bbf688`](#insn-00bbf688) → [`00bbf714`](#insn-00bbf714)
  - `FALL_THROUGH` [`00bbf688`](#insn-00bbf688) → [`00bbf68c`](#insn-00bbf68c)
- ブロック [`00bbf68c`](#insn-00bbf68c) 範囲 `[['00bbf68c', '00bbf69b']]`
  - `CONDITIONAL_JUMP` [`00bbf698`](#insn-00bbf698) → [`00bbf714`](#insn-00bbf714)
  - `FALL_THROUGH` [`00bbf698`](#insn-00bbf698) → [`00bbf69c`](#insn-00bbf69c)
- ブロック [`00bbf69c`](#insn-00bbf69c) 範囲 `[['00bbf69c', '00bbf6ab']]`
  - `CONDITIONAL_JUMP` [`00bbf6a8`](#insn-00bbf6a8) → [`00bbf6b4`](#insn-00bbf6b4)
  - `FALL_THROUGH` [`00bbf6a8`](#insn-00bbf6a8) → [`00bbf6ac`](#insn-00bbf6ac)
- ブロック [`00bbf6ac`](#insn-00bbf6ac) 範囲 `[['00bbf6ac', '00bbf6b3']]`
  - `CONDITIONAL_JUMP` [`00bbf6b0`](#insn-00bbf6b0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf6b0`](#insn-00bbf6b0) → [`00bbf6b4`](#insn-00bbf6b4)
- ブロック [`00bbf6b4`](#insn-00bbf6b4) 範囲 `[['00bbf6b4', '00bbf6c3']]`
  - `CONDITIONAL_JUMP` [`00bbf6c0`](#insn-00bbf6c0) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf6c0`](#insn-00bbf6c0) → [`00bbf6c4`](#insn-00bbf6c4)
- ブロック [`00bbf6c4`](#insn-00bbf6c4) 範囲 `[['00bbf6c4', '00bbf6cf']]`
  - `CONDITIONAL_JUMP` [`00bbf6cc`](#insn-00bbf6cc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf6cc`](#insn-00bbf6cc) → [`00bbf6d0`](#insn-00bbf6d0)
- ブロック [`00bbf6d0`](#insn-00bbf6d0) 範囲 `[['00bbf6d0', '00bbf6df']]`
  - `CONDITIONAL_JUMP` [`00bbf6dc`](#insn-00bbf6dc) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf6dc`](#insn-00bbf6dc) → [`00bbf6e0`](#insn-00bbf6e0)
- ブロック [`00bbf6e0`](#insn-00bbf6e0) 範囲 `[['00bbf6e0', '00bbf6f7']]`
  - `CONDITIONAL_JUMP` [`00bbf6f4`](#insn-00bbf6f4) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf6f4`](#insn-00bbf6f4) → [`00bbf6f8`](#insn-00bbf6f8)
- ブロック [`00bbf6f8`](#insn-00bbf6f8) 範囲 `[['00bbf6f8', '00bbf6ff']]`
  - `CONDITIONAL_JUMP` [`00bbf6fc`](#insn-00bbf6fc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf6fc`](#insn-00bbf6fc) → [`00bbf700`](#insn-00bbf700)
- ブロック [`00bbf700`](#insn-00bbf700) 範囲 `[['00bbf700', '00bbf70b']]`
  - `CONDITIONAL_JUMP` [`00bbf708`](#insn-00bbf708) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf708`](#insn-00bbf708) → [`00bbf70c`](#insn-00bbf70c)
- ブロック [`00bbf70c`](#insn-00bbf70c) 範囲 `[['00bbf70c', '00bbf713']]`
  - `CONDITIONAL_JUMP` [`00bbf710`](#insn-00bbf710) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf710`](#insn-00bbf710) → [`00bbf714`](#insn-00bbf714)
- ブロック [`00bbf714`](#insn-00bbf714) 範囲 `[['00bbf714', '00bbf71b']]`
  - `CONDITIONAL_JUMP` [`00bbf718`](#insn-00bbf718) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf718`](#insn-00bbf718) → [`00bbf71c`](#insn-00bbf71c)
- ブロック [`00bbf71c`](#insn-00bbf71c) 範囲 `[['00bbf71c', '00bbf723']]`
  - `CONDITIONAL_JUMP` [`00bbf720`](#insn-00bbf720) → [`00bbf75c`](#insn-00bbf75c)
  - `FALL_THROUGH` [`00bbf720`](#insn-00bbf720) → [`00bbf724`](#insn-00bbf724)
- ブロック [`00bbf724`](#insn-00bbf724) 範囲 `[['00bbf724', '00bbf737']]`
  - `CONDITIONAL_JUMP` [`00bbf734`](#insn-00bbf734) → [`00bbf740`](#insn-00bbf740)
  - `FALL_THROUGH` [`00bbf734`](#insn-00bbf734) → [`00bbf738`](#insn-00bbf738)
- ブロック [`00bbf738`](#insn-00bbf738) 範囲 `[['00bbf738', '00bbf73f']]`
  - `CONDITIONAL_JUMP` [`00bbf73c`](#insn-00bbf73c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf73c`](#insn-00bbf73c) → [`00bbf740`](#insn-00bbf740)
- ブロック [`00bbf740`](#insn-00bbf740) 範囲 `[['00bbf740', '00bbf74f']]`
  - `CONDITIONAL_JUMP` [`00bbf74c`](#insn-00bbf74c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf74c`](#insn-00bbf74c) → [`00bbf750`](#insn-00bbf750)
- ブロック [`00bbf750`](#insn-00bbf750) 範囲 `[['00bbf750', '00bbf75b']]`
  - `CONDITIONAL_JUMP` [`00bbf758`](#insn-00bbf758) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf758`](#insn-00bbf758) → [`00bbf75c`](#insn-00bbf75c)
- ブロック [`00bbf75c`](#insn-00bbf75c) 範囲 `[['00bbf75c', '00bbf763']]`
  - `CONDITIONAL_JUMP` [`00bbf760`](#insn-00bbf760) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf760`](#insn-00bbf760) → [`00bbf764`](#insn-00bbf764)
- ブロック [`00bbf764`](#insn-00bbf764) 範囲 `[['00bbf764', '00bbf76b']]`
  - `CONDITIONAL_JUMP` [`00bbf768`](#insn-00bbf768) → [`00bbf7c0`](#insn-00bbf7c0)
  - `FALL_THROUGH` [`00bbf768`](#insn-00bbf768) → [`00bbf76c`](#insn-00bbf76c)
- ブロック [`00bbf76c`](#insn-00bbf76c) 範囲 `[['00bbf76c', '00bbf77f']]`
  - `CONDITIONAL_JUMP` [`00bbf77c`](#insn-00bbf77c) → [`00bbf788`](#insn-00bbf788)
  - `FALL_THROUGH` [`00bbf77c`](#insn-00bbf77c) → [`00bbf780`](#insn-00bbf780)
- ブロック [`00bbf780`](#insn-00bbf780) 範囲 `[['00bbf780', '00bbf787']]`
  - `CONDITIONAL_JUMP` [`00bbf784`](#insn-00bbf784) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf784`](#insn-00bbf784) → [`00bbf788`](#insn-00bbf788)
- ブロック [`00bbf788`](#insn-00bbf788) 範囲 `[['00bbf788', '00bbf797']]`
  - `CONDITIONAL_JUMP` [`00bbf794`](#insn-00bbf794) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf794`](#insn-00bbf794) → [`00bbf798`](#insn-00bbf798)
- ブロック [`00bbf798`](#insn-00bbf798) 範囲 `[['00bbf798', '00bbf7a3']]`
  - `CONDITIONAL_JUMP` [`00bbf7a0`](#insn-00bbf7a0) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf7a0`](#insn-00bbf7a0) → [`00bbf7a4`](#insn-00bbf7a4)
- ブロック [`00bbf7a4`](#insn-00bbf7a4) 範囲 `[['00bbf7a4', '00bbf7af']]`
  - `CONDITIONAL_JUMP` [`00bbf7ac`](#insn-00bbf7ac) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf7ac`](#insn-00bbf7ac) → [`00bbf7b0`](#insn-00bbf7b0)
- ブロック [`00bbf7b0`](#insn-00bbf7b0) 範囲 `[['00bbf7b0', '00bbf7bf']]`
  - `CONDITIONAL_JUMP` [`00bbf7bc`](#insn-00bbf7bc) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf7bc`](#insn-00bbf7bc) → [`00bbf7c0`](#insn-00bbf7c0)
- ブロック [`00bbf7c0`](#insn-00bbf7c0) 範囲 `[['00bbf7c0', '00bbf7c7']]`
  - `CONDITIONAL_JUMP` [`00bbf7c4`](#insn-00bbf7c4) → [`00bbf850`](#insn-00bbf850)
  - `FALL_THROUGH` [`00bbf7c4`](#insn-00bbf7c4) → [`00bbf7c8`](#insn-00bbf7c8)
- ブロック [`00bbf7c8`](#insn-00bbf7c8) 範囲 `[['00bbf7c8', '00bbf7d7']]`
  - `CONDITIONAL_JUMP` [`00bbf7d4`](#insn-00bbf7d4) → [`00bbf850`](#insn-00bbf850)
  - `FALL_THROUGH` [`00bbf7d4`](#insn-00bbf7d4) → [`00bbf7d8`](#insn-00bbf7d8)
- ブロック [`00bbf7d8`](#insn-00bbf7d8) 範囲 `[['00bbf7d8', '00bbf7e7']]`
  - `CONDITIONAL_JUMP` [`00bbf7e4`](#insn-00bbf7e4) → [`00bbf7f0`](#insn-00bbf7f0)
  - `FALL_THROUGH` [`00bbf7e4`](#insn-00bbf7e4) → [`00bbf7e8`](#insn-00bbf7e8)
- ブロック [`00bbf7e8`](#insn-00bbf7e8) 範囲 `[['00bbf7e8', '00bbf7ef']]`
  - `CONDITIONAL_JUMP` [`00bbf7ec`](#insn-00bbf7ec) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf7ec`](#insn-00bbf7ec) → [`00bbf7f0`](#insn-00bbf7f0)
- ブロック [`00bbf7f0`](#insn-00bbf7f0) 範囲 `[['00bbf7f0', '00bbf7f3']]`
  - `FALL_THROUGH` [`00bbf7f0`](#insn-00bbf7f0) → [`00bbf7f4`](#insn-00bbf7f4)
- ブロック [`00bbf7f4`](#insn-00bbf7f4) 範囲 `[['00bbf7f4', '00bbf7ff']]`
  - `CONDITIONAL_JUMP` [`00bbf7fc`](#insn-00bbf7fc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf7fc`](#insn-00bbf7fc) → [`00bbf800`](#insn-00bbf800)
- ブロック [`00bbf800`](#insn-00bbf800) 範囲 `[['00bbf800', '00bbf80b']]`
  - `CONDITIONAL_JUMP` [`00bbf808`](#insn-00bbf808) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf808`](#insn-00bbf808) → [`00bbf80c`](#insn-00bbf80c)
- ブロック [`00bbf80c`](#insn-00bbf80c) 範囲 `[['00bbf80c', '00bbf81b']]`
  - `CONDITIONAL_JUMP` [`00bbf818`](#insn-00bbf818) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf818`](#insn-00bbf818) → [`00bbf81c`](#insn-00bbf81c)
- ブロック [`00bbf81c`](#insn-00bbf81c) 範囲 `[['00bbf81c', '00bbf833']]`
  - `CONDITIONAL_JUMP` [`00bbf830`](#insn-00bbf830) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf830`](#insn-00bbf830) → [`00bbf834`](#insn-00bbf834)
- ブロック [`00bbf834`](#insn-00bbf834) 範囲 `[['00bbf834', '00bbf83b']]`
  - `CONDITIONAL_JUMP` [`00bbf838`](#insn-00bbf838) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf838`](#insn-00bbf838) → [`00bbf83c`](#insn-00bbf83c)
- ブロック [`00bbf83c`](#insn-00bbf83c) 範囲 `[['00bbf83c', '00bbf847']]`
  - `CONDITIONAL_JUMP` [`00bbf844`](#insn-00bbf844) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf844`](#insn-00bbf844) → [`00bbf848`](#insn-00bbf848)
- ブロック [`00bbf848`](#insn-00bbf848) 範囲 `[['00bbf848', '00bbf84f']]`
  - `CONDITIONAL_JUMP` [`00bbf84c`](#insn-00bbf84c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf84c`](#insn-00bbf84c) → [`00bbf850`](#insn-00bbf850)
- ブロック [`00bbf850`](#insn-00bbf850) 範囲 `[['00bbf850', '00bbf857']]`
  - `CONDITIONAL_JUMP` [`00bbf854`](#insn-00bbf854) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf854`](#insn-00bbf854) → [`00bbf858`](#insn-00bbf858)
- ブロック [`00bbf858`](#insn-00bbf858) 範囲 `[['00bbf858', '00bbf85f']]`
  - `CONDITIONAL_JUMP` [`00bbf85c`](#insn-00bbf85c) → [`00bbf8b4`](#insn-00bbf8b4)
  - `FALL_THROUGH` [`00bbf85c`](#insn-00bbf85c) → [`00bbf860`](#insn-00bbf860)
- ブロック [`00bbf860`](#insn-00bbf860) 範囲 `[['00bbf860', '00bbf873']]`
  - `CONDITIONAL_JUMP` [`00bbf870`](#insn-00bbf870) → [`00bbf87c`](#insn-00bbf87c)
  - `FALL_THROUGH` [`00bbf870`](#insn-00bbf870) → [`00bbf874`](#insn-00bbf874)
- ブロック [`00bbf874`](#insn-00bbf874) 範囲 `[['00bbf874', '00bbf87b']]`
  - `CONDITIONAL_JUMP` [`00bbf878`](#insn-00bbf878) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf878`](#insn-00bbf878) → [`00bbf87c`](#insn-00bbf87c)
- ブロック [`00bbf87c`](#insn-00bbf87c) 範囲 `[['00bbf87c', '00bbf88b']]`
  - `CONDITIONAL_JUMP` [`00bbf888`](#insn-00bbf888) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf888`](#insn-00bbf888) → [`00bbf88c`](#insn-00bbf88c)
- ブロック [`00bbf88c`](#insn-00bbf88c) 範囲 `[['00bbf88c', '00bbf897']]`
  - `CONDITIONAL_JUMP` [`00bbf894`](#insn-00bbf894) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf894`](#insn-00bbf894) → [`00bbf898`](#insn-00bbf898)
- ブロック [`00bbf898`](#insn-00bbf898) 範囲 `[['00bbf898', '00bbf8a3']]`
  - `CONDITIONAL_JUMP` [`00bbf8a0`](#insn-00bbf8a0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf8a0`](#insn-00bbf8a0) → [`00bbf8a4`](#insn-00bbf8a4)
- ブロック [`00bbf8a4`](#insn-00bbf8a4) 範囲 `[['00bbf8a4', '00bbf8b3']]`
  - `CONDITIONAL_JUMP` [`00bbf8b0`](#insn-00bbf8b0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf8b0`](#insn-00bbf8b0) → [`00bbf8b4`](#insn-00bbf8b4)
- ブロック [`00bbf8b4`](#insn-00bbf8b4) 範囲 `[['00bbf8b4', '00bbf8bb']]`
  - `CONDITIONAL_JUMP` [`00bbf8b8`](#insn-00bbf8b8) → [`00bbf944`](#insn-00bbf944)
  - `FALL_THROUGH` [`00bbf8b8`](#insn-00bbf8b8) → [`00bbf8bc`](#insn-00bbf8bc)
- ブロック [`00bbf8bc`](#insn-00bbf8bc) 範囲 `[['00bbf8bc', '00bbf8cb']]`
  - `CONDITIONAL_JUMP` [`00bbf8c8`](#insn-00bbf8c8) → [`00bbf944`](#insn-00bbf944)
  - `FALL_THROUGH` [`00bbf8c8`](#insn-00bbf8c8) → [`00bbf8cc`](#insn-00bbf8cc)
- ブロック [`00bbf8cc`](#insn-00bbf8cc) 範囲 `[['00bbf8cc', '00bbf8db']]`
  - `CONDITIONAL_JUMP` [`00bbf8d8`](#insn-00bbf8d8) → [`00bbf8e4`](#insn-00bbf8e4)
  - `FALL_THROUGH` [`00bbf8d8`](#insn-00bbf8d8) → [`00bbf8dc`](#insn-00bbf8dc)
- ブロック [`00bbf8dc`](#insn-00bbf8dc) 範囲 `[['00bbf8dc', '00bbf8e3']]`
  - `CONDITIONAL_JUMP` [`00bbf8e0`](#insn-00bbf8e0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf8e0`](#insn-00bbf8e0) → [`00bbf8e4`](#insn-00bbf8e4)
- ブロック [`00bbf8e4`](#insn-00bbf8e4) 範囲 `[['00bbf8e4', '00bbf8f3']]`
  - `CONDITIONAL_JUMP` [`00bbf8f0`](#insn-00bbf8f0) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf8f0`](#insn-00bbf8f0) → [`00bbf8f4`](#insn-00bbf8f4)
- ブロック [`00bbf8f4`](#insn-00bbf8f4) 範囲 `[['00bbf8f4', '00bbf8ff']]`
  - `CONDITIONAL_JUMP` [`00bbf8fc`](#insn-00bbf8fc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf8fc`](#insn-00bbf8fc) → [`00bbf900`](#insn-00bbf900)
- ブロック [`00bbf900`](#insn-00bbf900) 範囲 `[['00bbf900', '00bbf90f']]`
  - `CONDITIONAL_JUMP` [`00bbf90c`](#insn-00bbf90c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf90c`](#insn-00bbf90c) → [`00bbf910`](#insn-00bbf910)
- ブロック [`00bbf910`](#insn-00bbf910) 範囲 `[['00bbf910', '00bbf927']]`
  - `CONDITIONAL_JUMP` [`00bbf924`](#insn-00bbf924) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf924`](#insn-00bbf924) → [`00bbf928`](#insn-00bbf928)
- ブロック [`00bbf928`](#insn-00bbf928) 範囲 `[['00bbf928', '00bbf92f']]`
  - `CONDITIONAL_JUMP` [`00bbf92c`](#insn-00bbf92c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf92c`](#insn-00bbf92c) → [`00bbf930`](#insn-00bbf930)
- ブロック [`00bbf930`](#insn-00bbf930) 範囲 `[['00bbf930', '00bbf93b']]`
  - `CONDITIONAL_JUMP` [`00bbf938`](#insn-00bbf938) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf938`](#insn-00bbf938) → [`00bbf93c`](#insn-00bbf93c)
- ブロック [`00bbf93c`](#insn-00bbf93c) 範囲 `[['00bbf93c', '00bbf943']]`
  - `CONDITIONAL_JUMP` [`00bbf940`](#insn-00bbf940) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf940`](#insn-00bbf940) → [`00bbf944`](#insn-00bbf944)
- ブロック [`00bbf944`](#insn-00bbf944) 範囲 `[['00bbf944', '00bbf94b']]`
  - `CONDITIONAL_JUMP` [`00bbf948`](#insn-00bbf948) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf948`](#insn-00bbf948) → [`00bbf94c`](#insn-00bbf94c)
- ブロック [`00bbf94c`](#insn-00bbf94c) 範囲 `[['00bbf94c', '00bbf953']]`
  - `CONDITIONAL_JUMP` [`00bbf950`](#insn-00bbf950) → [`00bbf9a8`](#insn-00bbf9a8)
  - `FALL_THROUGH` [`00bbf950`](#insn-00bbf950) → [`00bbf954`](#insn-00bbf954)
- ブロック [`00bbf954`](#insn-00bbf954) 範囲 `[['00bbf954', '00bbf967']]`
  - `CONDITIONAL_JUMP` [`00bbf964`](#insn-00bbf964) → [`00bbf970`](#insn-00bbf970)
  - `FALL_THROUGH` [`00bbf964`](#insn-00bbf964) → [`00bbf968`](#insn-00bbf968)
- ブロック [`00bbf968`](#insn-00bbf968) 範囲 `[['00bbf968', '00bbf96f']]`
  - `CONDITIONAL_JUMP` [`00bbf96c`](#insn-00bbf96c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf96c`](#insn-00bbf96c) → [`00bbf970`](#insn-00bbf970)
- ブロック [`00bbf970`](#insn-00bbf970) 範囲 `[['00bbf970', '00bbf97f']]`
  - `CONDITIONAL_JUMP` [`00bbf97c`](#insn-00bbf97c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf97c`](#insn-00bbf97c) → [`00bbf980`](#insn-00bbf980)
- ブロック [`00bbf980`](#insn-00bbf980) 範囲 `[['00bbf980', '00bbf98b']]`
  - `CONDITIONAL_JUMP` [`00bbf988`](#insn-00bbf988) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf988`](#insn-00bbf988) → [`00bbf98c`](#insn-00bbf98c)
- ブロック [`00bbf98c`](#insn-00bbf98c) 範囲 `[['00bbf98c', '00bbf997']]`
  - `CONDITIONAL_JUMP` [`00bbf994`](#insn-00bbf994) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf994`](#insn-00bbf994) → [`00bbf998`](#insn-00bbf998)
- ブロック [`00bbf998`](#insn-00bbf998) 範囲 `[['00bbf998', '00bbf9a7']]`
  - `CONDITIONAL_JUMP` [`00bbf9a4`](#insn-00bbf9a4) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf9a4`](#insn-00bbf9a4) → [`00bbf9a8`](#insn-00bbf9a8)
- ブロック [`00bbf9a8`](#insn-00bbf9a8) 範囲 `[['00bbf9a8', '00bbf9af']]`
  - `CONDITIONAL_JUMP` [`00bbf9ac`](#insn-00bbf9ac) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf9ac`](#insn-00bbf9ac) → [`00bbf9b0`](#insn-00bbf9b0)
- ブロック [`00bbf9b0`](#insn-00bbf9b0) 範囲 `[['00bbf9b0', '00bbf9bf']]`
  - `CONDITIONAL_JUMP` [`00bbf9bc`](#insn-00bbf9bc) → [`00bbf9d4`](#insn-00bbf9d4)
  - `FALL_THROUGH` [`00bbf9bc`](#insn-00bbf9bc) → [`00bbf9c0`](#insn-00bbf9c0)
- ブロック [`00bbf9c0`](#insn-00bbf9c0) 範囲 `[['00bbf9c0', '00bbf9cb']]`
  - `CONDITIONAL_JUMP` [`00bbf9c8`](#insn-00bbf9c8) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbf9c8`](#insn-00bbf9c8) → [`00bbf9cc`](#insn-00bbf9cc)
- ブロック [`00bbf9cc`](#insn-00bbf9cc) 範囲 `[['00bbf9cc', '00bbf9d3']]`
  - `FALL_THROUGH` [`00bbf9d0`](#insn-00bbf9d0) → [`00bbf9d4`](#insn-00bbf9d4)
- ブロック [`00bbf9d4`](#insn-00bbf9d4) 範囲 `[['00bbf9d4', '00bbf9e3']]`
  - `CONDITIONAL_JUMP` [`00bbf9e0`](#insn-00bbf9e0) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbf9e0`](#insn-00bbf9e0) → [`00bbf9e4`](#insn-00bbf9e4)
- ブロック [`00bbf9e4`](#insn-00bbf9e4) 範囲 `[['00bbf9e4', '00bbf9eb']]`
  - `CONDITIONAL_JUMP` [`00bbf9e8`](#insn-00bbf9e8) → [`00bbfa14`](#insn-00bbfa14)
  - `FALL_THROUGH` [`00bbf9e8`](#insn-00bbf9e8) → [`00bbf9ec`](#insn-00bbf9ec)
- ブロック [`00bbf9ec`](#insn-00bbf9ec) 範囲 `[['00bbf9ec', '00bbf9fb']]`
  - `CONDITIONAL_JUMP` [`00bbf9f8`](#insn-00bbf9f8) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbf9f8`](#insn-00bbf9f8) → [`00bbf9fc`](#insn-00bbf9fc)
- ブロック [`00bbf9fc`](#insn-00bbf9fc) 範囲 `[['00bbf9fc', '00bbfa13']]`
  - `CONDITIONAL_JUMP` [`00bbfa10`](#insn-00bbfa10) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfa10`](#insn-00bbfa10) → [`00bbfa14`](#insn-00bbfa14)
- ブロック [`00bbfa14`](#insn-00bbfa14) 範囲 `[['00bbfa14', '00bbfa1b']]`
  - `CONDITIONAL_JUMP` [`00bbfa18`](#insn-00bbfa18) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbfa18`](#insn-00bbfa18) → [`00bbfa1c`](#insn-00bbfa1c)
- ブロック [`00bbfa1c`](#insn-00bbfa1c) 範囲 `[['00bbfa1c', '00bbfa23']]`
  - `CONDITIONAL_JUMP` [`00bbfa20`](#insn-00bbfa20) → [`00bbfa78`](#insn-00bbfa78)
  - `FALL_THROUGH` [`00bbfa20`](#insn-00bbfa20) → [`00bbfa24`](#insn-00bbfa24)
- ブロック [`00bbfa24`](#insn-00bbfa24) 範囲 `[['00bbfa24', '00bbfa37']]`
  - `CONDITIONAL_JUMP` [`00bbfa34`](#insn-00bbfa34) → [`00bbfa40`](#insn-00bbfa40)
  - `FALL_THROUGH` [`00bbfa34`](#insn-00bbfa34) → [`00bbfa38`](#insn-00bbfa38)
- ブロック [`00bbfa38`](#insn-00bbfa38) 範囲 `[['00bbfa38', '00bbfa3f']]`
  - `CONDITIONAL_JUMP` [`00bbfa3c`](#insn-00bbfa3c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfa3c`](#insn-00bbfa3c) → [`00bbfa40`](#insn-00bbfa40)
- ブロック [`00bbfa40`](#insn-00bbfa40) 範囲 `[['00bbfa40', '00bbfa4f']]`
  - `CONDITIONAL_JUMP` [`00bbfa4c`](#insn-00bbfa4c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfa4c`](#insn-00bbfa4c) → [`00bbfa50`](#insn-00bbfa50)
- ブロック [`00bbfa50`](#insn-00bbfa50) 範囲 `[['00bbfa50', '00bbfa5b']]`
  - `CONDITIONAL_JUMP` [`00bbfa58`](#insn-00bbfa58) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfa58`](#insn-00bbfa58) → [`00bbfa5c`](#insn-00bbfa5c)
- ブロック [`00bbfa5c`](#insn-00bbfa5c) 範囲 `[['00bbfa5c', '00bbfa67']]`
  - `CONDITIONAL_JUMP` [`00bbfa64`](#insn-00bbfa64) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfa64`](#insn-00bbfa64) → [`00bbfa68`](#insn-00bbfa68)
- ブロック [`00bbfa68`](#insn-00bbfa68) 範囲 `[['00bbfa68', '00bbfa77']]`
  - `CONDITIONAL_JUMP` [`00bbfa74`](#insn-00bbfa74) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfa74`](#insn-00bbfa74) → [`00bbfa78`](#insn-00bbfa78)
- ブロック [`00bbfa78`](#insn-00bbfa78) 範囲 `[['00bbfa78', '00bbfa7f']]`
  - `CONDITIONAL_JUMP` [`00bbfa7c`](#insn-00bbfa7c) → [`00bbfb08`](#insn-00bbfb08)
  - `FALL_THROUGH` [`00bbfa7c`](#insn-00bbfa7c) → [`00bbfa80`](#insn-00bbfa80)
- ブロック [`00bbfa80`](#insn-00bbfa80) 範囲 `[['00bbfa80', '00bbfa8f']]`
  - `CONDITIONAL_JUMP` [`00bbfa8c`](#insn-00bbfa8c) → [`00bbfb08`](#insn-00bbfb08)
  - `FALL_THROUGH` [`00bbfa8c`](#insn-00bbfa8c) → [`00bbfa90`](#insn-00bbfa90)
- ブロック [`00bbfa90`](#insn-00bbfa90) 範囲 `[['00bbfa90', '00bbfa9f']]`
  - `CONDITIONAL_JUMP` [`00bbfa9c`](#insn-00bbfa9c) → [`00bbfaa8`](#insn-00bbfaa8)
  - `FALL_THROUGH` [`00bbfa9c`](#insn-00bbfa9c) → [`00bbfaa0`](#insn-00bbfaa0)
- ブロック [`00bbfaa0`](#insn-00bbfaa0) 範囲 `[['00bbfaa0', '00bbfaa7']]`
  - `CONDITIONAL_JUMP` [`00bbfaa4`](#insn-00bbfaa4) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfaa4`](#insn-00bbfaa4) → [`00bbfaa8`](#insn-00bbfaa8)
- ブロック [`00bbfaa8`](#insn-00bbfaa8) 範囲 `[['00bbfaa8', '00bbfab7']]`
  - `CONDITIONAL_JUMP` [`00bbfab4`](#insn-00bbfab4) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfab4`](#insn-00bbfab4) → [`00bbfab8`](#insn-00bbfab8)
- ブロック [`00bbfab8`](#insn-00bbfab8) 範囲 `[['00bbfab8', '00bbfac3']]`
  - `CONDITIONAL_JUMP` [`00bbfac0`](#insn-00bbfac0) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfac0`](#insn-00bbfac0) → [`00bbfac4`](#insn-00bbfac4)
- ブロック [`00bbfac4`](#insn-00bbfac4) 範囲 `[['00bbfac4', '00bbfad3']]`
  - `CONDITIONAL_JUMP` [`00bbfad0`](#insn-00bbfad0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfad0`](#insn-00bbfad0) → [`00bbfad4`](#insn-00bbfad4)
- ブロック [`00bbfad4`](#insn-00bbfad4) 範囲 `[['00bbfad4', '00bbfae7']]`
  - `FALL_THROUGH` [`00bbfae4`](#insn-00bbfae4) → [`00bbfae8`](#insn-00bbfae8)
- ブロック [`00bbfae8`](#insn-00bbfae8) 範囲 `[['00bbfae8', '00bbfaeb']]`
  - `CONDITIONAL_JUMP` [`00bbfae8`](#insn-00bbfae8) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfae8`](#insn-00bbfae8) → [`00bbfaec`](#insn-00bbfaec)
- ブロック [`00bbfaec`](#insn-00bbfaec) 範囲 `[['00bbfaec', '00bbfaf3']]`
  - `CONDITIONAL_JUMP` [`00bbfaf0`](#insn-00bbfaf0) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfaf0`](#insn-00bbfaf0) → [`00bbfaf4`](#insn-00bbfaf4)
- ブロック [`00bbfaf4`](#insn-00bbfaf4) 範囲 `[['00bbfaf4', '00bbfaff']]`
  - `CONDITIONAL_JUMP` [`00bbfafc`](#insn-00bbfafc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfafc`](#insn-00bbfafc) → [`00bbfb00`](#insn-00bbfb00)
- ブロック [`00bbfb00`](#insn-00bbfb00) 範囲 `[['00bbfb00', '00bbfb07']]`
  - `CONDITIONAL_JUMP` [`00bbfb04`](#insn-00bbfb04) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfb04`](#insn-00bbfb04) → [`00bbfb08`](#insn-00bbfb08)
- ブロック [`00bbfb08`](#insn-00bbfb08) 範囲 `[['00bbfb08', '00bbfb0f']]`
  - `CONDITIONAL_JUMP` [`00bbfb0c`](#insn-00bbfb0c) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbfb0c`](#insn-00bbfb0c) → [`00bbfb10`](#insn-00bbfb10)
- ブロック [`00bbfb10`](#insn-00bbfb10) 範囲 `[['00bbfb10', '00bbfb17']]`
  - `CONDITIONAL_JUMP` [`00bbfb14`](#insn-00bbfb14) → [`00bbfb50`](#insn-00bbfb50)
  - `FALL_THROUGH` [`00bbfb14`](#insn-00bbfb14) → [`00bbfb18`](#insn-00bbfb18)
- ブロック [`00bbfb18`](#insn-00bbfb18) 範囲 `[['00bbfb18', '00bbfb2b']]`
  - `CONDITIONAL_JUMP` [`00bbfb28`](#insn-00bbfb28) → [`00bbfb34`](#insn-00bbfb34)
  - `FALL_THROUGH` [`00bbfb28`](#insn-00bbfb28) → [`00bbfb2c`](#insn-00bbfb2c)
- ブロック [`00bbfb2c`](#insn-00bbfb2c) 範囲 `[['00bbfb2c', '00bbfb33']]`
  - `CONDITIONAL_JUMP` [`00bbfb30`](#insn-00bbfb30) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfb30`](#insn-00bbfb30) → [`00bbfb34`](#insn-00bbfb34)
- ブロック [`00bbfb34`](#insn-00bbfb34) 範囲 `[['00bbfb34', '00bbfb43']]`
  - `CONDITIONAL_JUMP` [`00bbfb40`](#insn-00bbfb40) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfb40`](#insn-00bbfb40) → [`00bbfb44`](#insn-00bbfb44)
- ブロック [`00bbfb44`](#insn-00bbfb44) 範囲 `[['00bbfb44', '00bbfb4f']]`
  - `CONDITIONAL_JUMP` [`00bbfb4c`](#insn-00bbfb4c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfb4c`](#insn-00bbfb4c) → [`00bbfb50`](#insn-00bbfb50)
- ブロック [`00bbfb50`](#insn-00bbfb50) 範囲 `[['00bbfb50', '00bbfb57']]`
  - `CONDITIONAL_JUMP` [`00bbfb54`](#insn-00bbfb54) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbfb54`](#insn-00bbfb54) → [`00bbfb58`](#insn-00bbfb58)
- ブロック [`00bbfb58`](#insn-00bbfb58) 範囲 `[['00bbfb58', '00bbfb5f']]`
  - `CONDITIONAL_JUMP` [`00bbfb5c`](#insn-00bbfb5c) → [`00bbfbb4`](#insn-00bbfbb4)
  - `FALL_THROUGH` [`00bbfb5c`](#insn-00bbfb5c) → [`00bbfb60`](#insn-00bbfb60)
- ブロック [`00bbfb60`](#insn-00bbfb60) 範囲 `[['00bbfb60', '00bbfb73']]`
  - `CONDITIONAL_JUMP` [`00bbfb70`](#insn-00bbfb70) → [`00bbfb7c`](#insn-00bbfb7c)
  - `FALL_THROUGH` [`00bbfb70`](#insn-00bbfb70) → [`00bbfb74`](#insn-00bbfb74)
- ブロック [`00bbfb74`](#insn-00bbfb74) 範囲 `[['00bbfb74', '00bbfb7b']]`
  - `CONDITIONAL_JUMP` [`00bbfb78`](#insn-00bbfb78) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfb78`](#insn-00bbfb78) → [`00bbfb7c`](#insn-00bbfb7c)
- ブロック [`00bbfb7c`](#insn-00bbfb7c) 範囲 `[['00bbfb7c', '00bbfb8b']]`
  - `CONDITIONAL_JUMP` [`00bbfb88`](#insn-00bbfb88) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfb88`](#insn-00bbfb88) → [`00bbfb8c`](#insn-00bbfb8c)
- ブロック [`00bbfb8c`](#insn-00bbfb8c) 範囲 `[['00bbfb8c', '00bbfb97']]`
  - `CONDITIONAL_JUMP` [`00bbfb94`](#insn-00bbfb94) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfb94`](#insn-00bbfb94) → [`00bbfb98`](#insn-00bbfb98)
- ブロック [`00bbfb98`](#insn-00bbfb98) 範囲 `[['00bbfb98', '00bbfba3']]`
  - `CONDITIONAL_JUMP` [`00bbfba0`](#insn-00bbfba0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfba0`](#insn-00bbfba0) → [`00bbfba4`](#insn-00bbfba4)
- ブロック [`00bbfba4`](#insn-00bbfba4) 範囲 `[['00bbfba4', '00bbfba7']]`
  - `FALL_THROUGH` [`00bbfba4`](#insn-00bbfba4) → [`00bbfba8`](#insn-00bbfba8)
- ブロック [`00bbfba8`](#insn-00bbfba8) 範囲 `[['00bbfba8', '00bbfbb3']]`
  - `CONDITIONAL_JUMP` [`00bbfbb0`](#insn-00bbfbb0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfbb0`](#insn-00bbfbb0) → [`00bbfbb4`](#insn-00bbfbb4)
- ブロック [`00bbfbb4`](#insn-00bbfbb4) 範囲 `[['00bbfbb4', '00bbfbbb']]`
  - `CONDITIONAL_JUMP` [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfbbc`](#insn-00bbfbbc)
- ブロック [`00bbfbbc`](#insn-00bbfbbc) 範囲 `[['00bbfbbc', '00bbfbc7']]`
  - `FALL_THROUGH` [`00bbfbc4`](#insn-00bbfbc4) → [`00bbfbc8`](#insn-00bbfbc8)
- ブロック [`00bbfbc8`](#insn-00bbfbc8) 範囲 `[['00bbfbc8', '00bbfbcb']]`
  - `CONDITIONAL_JUMP` [`00bbfbc8`](#insn-00bbfbc8) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbfbc8`](#insn-00bbfbc8) → [`00bbfbcc`](#insn-00bbfbcc)
- ブロック [`00bbfbcc`](#insn-00bbfbcc) 範囲 `[['00bbfbcc', '00bbfbdb']]`
  - `CONDITIONAL_JUMP` [`00bbfbd8`](#insn-00bbfbd8) → [`00bbfbe4`](#insn-00bbfbe4)
  - `FALL_THROUGH` [`00bbfbd8`](#insn-00bbfbd8) → [`00bbfbdc`](#insn-00bbfbdc)
- ブロック [`00bbfbdc`](#insn-00bbfbdc) 範囲 `[['00bbfbdc', '00bbfbe3']]`
  - `CONDITIONAL_JUMP` [`00bbfbe0`](#insn-00bbfbe0) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfbe0`](#insn-00bbfbe0) → [`00bbfbe4`](#insn-00bbfbe4)
- ブロック [`00bbfbe4`](#insn-00bbfbe4) 範囲 `[['00bbfbe4', '00bbfbf3']]`
  - `CONDITIONAL_JUMP` [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfbf4`](#insn-00bbfbf4)
- ブロック [`00bbfbf4`](#insn-00bbfbf4) 範囲 `[['00bbfbf4', '00bbfbff']]`
  - `CONDITIONAL_JUMP` [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfc00`](#insn-00bbfc00)
- ブロック [`00bbfc00`](#insn-00bbfc00) 範囲 `[['00bbfc00', '00bbfc0f']]`
  - `CONDITIONAL_JUMP` [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfc10`](#insn-00bbfc10)
- ブロック [`00bbfc10`](#insn-00bbfc10) 範囲 `[['00bbfc10', '00bbfc27']]`
  - `CONDITIONAL_JUMP` [`00bbfc24`](#insn-00bbfc24) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfc24`](#insn-00bbfc24) → [`00bbfc28`](#insn-00bbfc28)
- ブロック [`00bbfc28`](#insn-00bbfc28) 範囲 `[['00bbfc28', '00bbfc2f']]`
  - `CONDITIONAL_JUMP` [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfc30`](#insn-00bbfc30)
- ブロック [`00bbfc30`](#insn-00bbfc30) 範囲 `[['00bbfc30', '00bbfc3b']]`
  - `CONDITIONAL_JUMP` [`00bbfc38`](#insn-00bbfc38) → [`00bbfc48`](#insn-00bbfc48)
  - `FALL_THROUGH` [`00bbfc38`](#insn-00bbfc38) → [`00bbfc3c`](#insn-00bbfc3c)
- ブロック [`00bbfc3c`](#insn-00bbfc3c) 範囲 `[['00bbfc3c', '00bbfc43']]`
  - `CONDITIONAL_JUMP` [`00bbfc40`](#insn-00bbfc40) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbfc40`](#insn-00bbfc40) → [`00bbfc44`](#insn-00bbfc44)
- ブロック [`00bbfc44`](#insn-00bbfc44) 範囲 `[['00bbfc44', '00bbfc47']]`
  - `FALL_THROUGH` [`00bbfc44`](#insn-00bbfc44) → [`00bbfc48`](#insn-00bbfc48)
- ブロック [`00bbfc48`](#insn-00bbfc48) 範囲 `[['00bbfc48', '00bbfc5b']]`
- ブロック [`00bbfc5c`](#insn-00bbfc5c) 範囲 `[['00bbfc5c', '00bbfc6f']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfc48`](#insn-00bbfc48)

## 命令位置別の参照

- [`00bbeec8`](#insn-00bbeec8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeecc`](#insn-00bbeecc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeed0`](#insn-00bbeed0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeed4`](#insn-00bbeed4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeef0`](#insn-00bbeef0) → [`00bbeefc`](#insn-00bbeefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeef8`](#insn-00bbeef8) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef08`](#insn-00bbef08) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef14`](#insn-00bbef14) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef34`](#insn-00bbef34) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef40`](#insn-00bbef40) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef48`](#insn-00bbef48) → [`00bbef54`](#insn-00bbef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef50`](#insn-00bbef50) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef5c`](#insn-00bbef5c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef64`](#insn-00bbef64) → [`00bbef70`](#insn-00bbef70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef6c`](#insn-00bbef6c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef70`](#insn-00bbef70) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef7c`](#insn-00bbef7c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef84`](#insn-00bbef84) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef9c`](#insn-00bbef9c) → [`00bbf358`](#insn-00bbf358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefa4`](#insn-00bbefa4) → [`00bbeff0`](#insn-00bbeff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefb0`](#insn-00bbefb0) → [`00bbefcc`](#insn-00bbefcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefbc`](#insn-00bbefbc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefc4`](#insn-00bbefc4) → [`00bbefd4`](#insn-00bbefd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefc8`](#insn-00bbefc8) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefd0`](#insn-00bbefd0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefdc`](#insn-00bbefdc) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefec`](#insn-00bbefec) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeff4`](#insn-00bbeff4) → [`00bbf078`](#insn-00bbf078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf004`](#insn-00bbf004) → [`00bbf078`](#insn-00bbf078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf010`](#insn-00bbf010) → [`00bbf02c`](#insn-00bbf02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf01c`](#insn-00bbf01c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf024`](#insn-00bbf024) → [`00bbf034`](#insn-00bbf034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf028`](#insn-00bbf028) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf030`](#insn-00bbf030) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf040`](#insn-00bbf040) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf058`](#insn-00bbf058) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf060`](#insn-00bbf060) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf06c`](#insn-00bbf06c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf074`](#insn-00bbf074) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf07c`](#insn-00bbf07c) → [`00bbf358`](#insn-00bbf358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf084`](#insn-00bbf084) → [`00bbf0d0`](#insn-00bbf0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf090`](#insn-00bbf090) → [`00bbf0ac`](#insn-00bbf0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf09c`](#insn-00bbf09c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0a4`](#insn-00bbf0a4) → [`00bbf0b4`](#insn-00bbf0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0a8`](#insn-00bbf0a8) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0b0`](#insn-00bbf0b0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0bc`](#insn-00bbf0bc) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0cc`](#insn-00bbf0cc) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0d4`](#insn-00bbf0d4) → [`00bbf158`](#insn-00bbf158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0e4`](#insn-00bbf0e4) → [`00bbf158`](#insn-00bbf158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0f0`](#insn-00bbf0f0) → [`00bbf10c`](#insn-00bbf10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0fc`](#insn-00bbf0fc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf104`](#insn-00bbf104) → [`00bbf114`](#insn-00bbf114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf108`](#insn-00bbf108) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf110`](#insn-00bbf110) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf120`](#insn-00bbf120) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf138`](#insn-00bbf138) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf140`](#insn-00bbf140) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf14c`](#insn-00bbf14c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf154`](#insn-00bbf154) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf15c`](#insn-00bbf15c) → [`00bbf358`](#insn-00bbf358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf164`](#insn-00bbf164) → [`00bbf1b0`](#insn-00bbf1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf170`](#insn-00bbf170) → [`00bbf18c`](#insn-00bbf18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf17c`](#insn-00bbf17c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf184`](#insn-00bbf184) → [`00bbf194`](#insn-00bbf194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf188`](#insn-00bbf188) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf190`](#insn-00bbf190) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf19c`](#insn-00bbf19c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1ac`](#insn-00bbf1ac) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1b4`](#insn-00bbf1b4) → [`00bbf238`](#insn-00bbf238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1c4`](#insn-00bbf1c4) → [`00bbf238`](#insn-00bbf238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1d0`](#insn-00bbf1d0) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1dc`](#insn-00bbf1dc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1e4`](#insn-00bbf1e4) → [`00bbf1f4`](#insn-00bbf1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1e8`](#insn-00bbf1e8) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1f0`](#insn-00bbf1f0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf200`](#insn-00bbf200) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf218`](#insn-00bbf218) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf220`](#insn-00bbf220) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf22c`](#insn-00bbf22c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf234`](#insn-00bbf234) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf23c`](#insn-00bbf23c) → [`00bbf358`](#insn-00bbf358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf244`](#insn-00bbf244) → [`00bbf290`](#insn-00bbf290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf250`](#insn-00bbf250) → [`00bbf26c`](#insn-00bbf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf25c`](#insn-00bbf25c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf264`](#insn-00bbf264) → [`00bbf274`](#insn-00bbf274) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf268`](#insn-00bbf268) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf270`](#insn-00bbf270) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf27c`](#insn-00bbf27c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf28c`](#insn-00bbf28c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf294`](#insn-00bbf294) → [`00bbf358`](#insn-00bbf358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2a4`](#insn-00bbf2a4) → [`00bbf300`](#insn-00bbf300) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2b0`](#insn-00bbf2b0) → [`00bbf2cc`](#insn-00bbf2cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2bc`](#insn-00bbf2bc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2c4`](#insn-00bbf2c4) → [`00bbf2d4`](#insn-00bbf2d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2c8`](#insn-00bbf2c8) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2d0`](#insn-00bbf2d0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2e0`](#insn-00bbf2e0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2f4`](#insn-00bbf2f4) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2fc`](#insn-00bbf2fc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf308`](#insn-00bbf308) → [`00bbf358`](#insn-00bbf358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf310`](#insn-00bbf310) → [`00bbf358`](#insn-00bbf358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf334`](#insn-00bbf334) → [`00c5d600`](../00c5d/00c5d600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d600` · 推定シンボル `None` · 推定型 `None`
- [`00bbf338`](#insn-00bbf338) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf34c`](#insn-00bbf34c) → [`00bbf320`](#insn-00bbf320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf364`](#insn-00bbf364) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf36c`](#insn-00bbf36c) → [`00bbf3c4`](#insn-00bbf3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf380`](#insn-00bbf380) → [`00bbf38c`](#insn-00bbf38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf388`](#insn-00bbf388) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf398`](#insn-00bbf398) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3a4`](#insn-00bbf3a4) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3b0`](#insn-00bbf3b0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3c0`](#insn-00bbf3c0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3c8`](#insn-00bbf3c8) → [`00bbf438`](#insn-00bbf438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3d8`](#insn-00bbf3d8) → [`00bbf438`](#insn-00bbf438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3e8`](#insn-00bbf3e8) → [`00bbf3f4`](#insn-00bbf3f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3f0`](#insn-00bbf3f0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf400`](#insn-00bbf400) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf40c`](#insn-00bbf40c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf41c`](#insn-00bbf41c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf42c`](#insn-00bbf42c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf434`](#insn-00bbf434) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf43c`](#insn-00bbf43c) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf444`](#insn-00bbf444) → [`00bbf49c`](#insn-00bbf49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf458`](#insn-00bbf458) → [`00bbf464`](#insn-00bbf464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf460`](#insn-00bbf460) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf470`](#insn-00bbf470) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf47c`](#insn-00bbf47c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf488`](#insn-00bbf488) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf498`](#insn-00bbf498) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4a0`](#insn-00bbf4a0) → [`00bbf52c`](#insn-00bbf52c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4b0`](#insn-00bbf4b0) → [`00bbf52c`](#insn-00bbf52c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4c0`](#insn-00bbf4c0) → [`00bbf4cc`](#insn-00bbf4cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4c8`](#insn-00bbf4c8) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4d8`](#insn-00bbf4d8) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4e4`](#insn-00bbf4e4) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4f4`](#insn-00bbf4f4) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf50c`](#insn-00bbf50c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf514`](#insn-00bbf514) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf520`](#insn-00bbf520) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf528`](#insn-00bbf528) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf530`](#insn-00bbf530) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf538`](#insn-00bbf538) → [`00bbf590`](#insn-00bbf590) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf54c`](#insn-00bbf54c) → [`00bbf558`](#insn-00bbf558) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf554`](#insn-00bbf554) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf564`](#insn-00bbf564) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf570`](#insn-00bbf570) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf57c`](#insn-00bbf57c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf58c`](#insn-00bbf58c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf594`](#insn-00bbf594) → [`00bbf620`](#insn-00bbf620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5a4`](#insn-00bbf5a4) → [`00bbf620`](#insn-00bbf620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5b4`](#insn-00bbf5b4) → [`00bbf5c0`](#insn-00bbf5c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5bc`](#insn-00bbf5bc) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5cc`](#insn-00bbf5cc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5d8`](#insn-00bbf5d8) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5e8`](#insn-00bbf5e8) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf600`](#insn-00bbf600) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf608`](#insn-00bbf608) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf614`](#insn-00bbf614) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf61c`](#insn-00bbf61c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf624`](#insn-00bbf624) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf62c`](#insn-00bbf62c) → [`00bbf684`](#insn-00bbf684) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf640`](#insn-00bbf640) → [`00bbf64c`](#insn-00bbf64c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf648`](#insn-00bbf648) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf658`](#insn-00bbf658) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf664`](#insn-00bbf664) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf670`](#insn-00bbf670) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf680`](#insn-00bbf680) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf688`](#insn-00bbf688) → [`00bbf714`](#insn-00bbf714) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf698`](#insn-00bbf698) → [`00bbf714`](#insn-00bbf714) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6a8`](#insn-00bbf6a8) → [`00bbf6b4`](#insn-00bbf6b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6b0`](#insn-00bbf6b0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6c0`](#insn-00bbf6c0) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6cc`](#insn-00bbf6cc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6dc`](#insn-00bbf6dc) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6f4`](#insn-00bbf6f4) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6fc`](#insn-00bbf6fc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf708`](#insn-00bbf708) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf710`](#insn-00bbf710) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf718`](#insn-00bbf718) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf720`](#insn-00bbf720) → [`00bbf75c`](#insn-00bbf75c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf734`](#insn-00bbf734) → [`00bbf740`](#insn-00bbf740) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf73c`](#insn-00bbf73c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf74c`](#insn-00bbf74c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf758`](#insn-00bbf758) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf760`](#insn-00bbf760) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf768`](#insn-00bbf768) → [`00bbf7c0`](#insn-00bbf7c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf77c`](#insn-00bbf77c) → [`00bbf788`](#insn-00bbf788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf784`](#insn-00bbf784) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf794`](#insn-00bbf794) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7a0`](#insn-00bbf7a0) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7ac`](#insn-00bbf7ac) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7bc`](#insn-00bbf7bc) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7c4`](#insn-00bbf7c4) → [`00bbf850`](#insn-00bbf850) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7d4`](#insn-00bbf7d4) → [`00bbf850`](#insn-00bbf850) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7e4`](#insn-00bbf7e4) → [`00bbf7f0`](#insn-00bbf7f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7ec`](#insn-00bbf7ec) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7fc`](#insn-00bbf7fc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf808`](#insn-00bbf808) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf818`](#insn-00bbf818) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf830`](#insn-00bbf830) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf838`](#insn-00bbf838) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf844`](#insn-00bbf844) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf84c`](#insn-00bbf84c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf854`](#insn-00bbf854) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf85c`](#insn-00bbf85c) → [`00bbf8b4`](#insn-00bbf8b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf870`](#insn-00bbf870) → [`00bbf87c`](#insn-00bbf87c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf878`](#insn-00bbf878) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf888`](#insn-00bbf888) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf894`](#insn-00bbf894) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8a0`](#insn-00bbf8a0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8b0`](#insn-00bbf8b0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8b8`](#insn-00bbf8b8) → [`00bbf944`](#insn-00bbf944) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8c8`](#insn-00bbf8c8) → [`00bbf944`](#insn-00bbf944) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8d8`](#insn-00bbf8d8) → [`00bbf8e4`](#insn-00bbf8e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8e0`](#insn-00bbf8e0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8f0`](#insn-00bbf8f0) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8fc`](#insn-00bbf8fc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf90c`](#insn-00bbf90c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf924`](#insn-00bbf924) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf92c`](#insn-00bbf92c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf938`](#insn-00bbf938) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf940`](#insn-00bbf940) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf948`](#insn-00bbf948) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf950`](#insn-00bbf950) → [`00bbf9a8`](#insn-00bbf9a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf964`](#insn-00bbf964) → [`00bbf970`](#insn-00bbf970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf96c`](#insn-00bbf96c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf97c`](#insn-00bbf97c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf988`](#insn-00bbf988) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf994`](#insn-00bbf994) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9a4`](#insn-00bbf9a4) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9ac`](#insn-00bbf9ac) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9bc`](#insn-00bbf9bc) → [`00bbf9d4`](#insn-00bbf9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9c4`](#insn-00bbf9c4) → [`00c5d5c0`](../00c5d/00c5d5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9c8`](#insn-00bbf9c8) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9e0`](#insn-00bbf9e0) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9e8`](#insn-00bbf9e8) → [`00bbfa14`](#insn-00bbfa14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9f8`](#insn-00bbf9f8) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa10`](#insn-00bbfa10) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa18`](#insn-00bbfa18) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa20`](#insn-00bbfa20) → [`00bbfa78`](#insn-00bbfa78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa34`](#insn-00bbfa34) → [`00bbfa40`](#insn-00bbfa40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa3c`](#insn-00bbfa3c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa4c`](#insn-00bbfa4c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa58`](#insn-00bbfa58) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa64`](#insn-00bbfa64) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa74`](#insn-00bbfa74) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa7c`](#insn-00bbfa7c) → [`00bbfb08`](#insn-00bbfb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa8c`](#insn-00bbfa8c) → [`00bbfb08`](#insn-00bbfb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa9c`](#insn-00bbfa9c) → [`00bbfaa8`](#insn-00bbfaa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfaa4`](#insn-00bbfaa4) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfab4`](#insn-00bbfab4) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfac0`](#insn-00bbfac0) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfad0`](#insn-00bbfad0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfae8`](#insn-00bbfae8) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfaf0`](#insn-00bbfaf0) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfafc`](#insn-00bbfafc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb04`](#insn-00bbfb04) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb0c`](#insn-00bbfb0c) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb14`](#insn-00bbfb14) → [`00bbfb50`](#insn-00bbfb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb28`](#insn-00bbfb28) → [`00bbfb34`](#insn-00bbfb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb30`](#insn-00bbfb30) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb40`](#insn-00bbfb40) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb4c`](#insn-00bbfb4c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb54`](#insn-00bbfb54) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb5c`](#insn-00bbfb5c) → [`00bbfbb4`](#insn-00bbfbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb70`](#insn-00bbfb70) → [`00bbfb7c`](#insn-00bbfb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb78`](#insn-00bbfb78) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb88`](#insn-00bbfb88) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb94`](#insn-00bbfb94) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfba0`](#insn-00bbfba0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbb0`](#insn-00bbfbb0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbc8`](#insn-00bbfbc8) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbd8`](#insn-00bbfbd8) → [`00bbfbe4`](#insn-00bbfbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbe0`](#insn-00bbfbe0) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc24`](#insn-00bbfc24) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc38`](#insn-00bbfc38) → [`00bbfc48`](#insn-00bbfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc40`](#insn-00bbfc40) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc48`](#insn-00bbfc48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc4c`](#insn-00bbfc4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc50`](#insn-00bbfc50) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfc48`](#insn-00bbfc48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbeec8`](#insn-00bbeec8)

~~~json
{
  "source": "00bbeec8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeecc`](#insn-00bbeecc)

~~~json
{
  "source": "00bbeecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeed0`](#insn-00bbeed0)

~~~json
{
  "source": "00bbeed0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeed4`](#insn-00bbeed4)

~~~json
{
  "source": "00bbeed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeef0`](#insn-00bbeef0)

~~~json
{
  "source": "00bbeef0",
  "target": "00bbeefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeef8`](#insn-00bbeef8)

~~~json
{
  "source": "00bbeef8",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef08`](#insn-00bbef08)

~~~json
{
  "source": "00bbef08",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef14`](#insn-00bbef14)

~~~json
{
  "source": "00bbef14",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef34`](#insn-00bbef34)

~~~json
{
  "source": "00bbef34",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef40`](#insn-00bbef40)

~~~json
{
  "source": "00bbef40",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef48`](#insn-00bbef48)

~~~json
{
  "source": "00bbef48",
  "target": "00bbef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef50`](#insn-00bbef50)

~~~json
{
  "source": "00bbef50",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef5c`](#insn-00bbef5c)

~~~json
{
  "source": "00bbef5c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef64`](#insn-00bbef64)

~~~json
{
  "source": "00bbef64",
  "target": "00bbef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef6c`](#insn-00bbef6c)

~~~json
{
  "source": "00bbef6c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef70`](#insn-00bbef70)

~~~json
{
  "source": "00bbef70",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef7c`](#insn-00bbef7c)

~~~json
{
  "source": "00bbef7c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef84`](#insn-00bbef84)

~~~json
{
  "source": "00bbef84",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef9c`](#insn-00bbef9c)

~~~json
{
  "source": "00bbef9c",
  "target": "00bbf358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefa4`](#insn-00bbefa4)

~~~json
{
  "source": "00bbefa4",
  "target": "00bbeff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefb0`](#insn-00bbefb0)

~~~json
{
  "source": "00bbefb0",
  "target": "00bbefcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefbc`](#insn-00bbefbc)

~~~json
{
  "source": "00bbefbc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefc4`](#insn-00bbefc4)

~~~json
{
  "source": "00bbefc4",
  "target": "00bbefd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefc8`](#insn-00bbefc8)

~~~json
{
  "source": "00bbefc8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefd0`](#insn-00bbefd0)

~~~json
{
  "source": "00bbefd0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefdc`](#insn-00bbefdc)

~~~json
{
  "source": "00bbefdc",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefec`](#insn-00bbefec)

~~~json
{
  "source": "00bbefec",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeff4`](#insn-00bbeff4)

~~~json
{
  "source": "00bbeff4",
  "target": "00bbf078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf004`](#insn-00bbf004)

~~~json
{
  "source": "00bbf004",
  "target": "00bbf078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf010`](#insn-00bbf010)

~~~json
{
  "source": "00bbf010",
  "target": "00bbf02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf01c`](#insn-00bbf01c)

~~~json
{
  "source": "00bbf01c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf024`](#insn-00bbf024)

~~~json
{
  "source": "00bbf024",
  "target": "00bbf034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf028`](#insn-00bbf028)

~~~json
{
  "source": "00bbf028",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf030`](#insn-00bbf030)

~~~json
{
  "source": "00bbf030",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf040`](#insn-00bbf040)

~~~json
{
  "source": "00bbf040",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf058`](#insn-00bbf058)

~~~json
{
  "source": "00bbf058",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf060`](#insn-00bbf060)

~~~json
{
  "source": "00bbf060",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf06c`](#insn-00bbf06c)

~~~json
{
  "source": "00bbf06c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf074`](#insn-00bbf074)

~~~json
{
  "source": "00bbf074",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf07c`](#insn-00bbf07c)

~~~json
{
  "source": "00bbf07c",
  "target": "00bbf358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf084`](#insn-00bbf084)

~~~json
{
  "source": "00bbf084",
  "target": "00bbf0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf090`](#insn-00bbf090)

~~~json
{
  "source": "00bbf090",
  "target": "00bbf0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf09c`](#insn-00bbf09c)

~~~json
{
  "source": "00bbf09c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0a4`](#insn-00bbf0a4)

~~~json
{
  "source": "00bbf0a4",
  "target": "00bbf0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0a8`](#insn-00bbf0a8)

~~~json
{
  "source": "00bbf0a8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0b0`](#insn-00bbf0b0)

~~~json
{
  "source": "00bbf0b0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0bc`](#insn-00bbf0bc)

~~~json
{
  "source": "00bbf0bc",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0cc`](#insn-00bbf0cc)

~~~json
{
  "source": "00bbf0cc",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0d4`](#insn-00bbf0d4)

~~~json
{
  "source": "00bbf0d4",
  "target": "00bbf158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0e4`](#insn-00bbf0e4)

~~~json
{
  "source": "00bbf0e4",
  "target": "00bbf158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0f0`](#insn-00bbf0f0)

~~~json
{
  "source": "00bbf0f0",
  "target": "00bbf10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0fc`](#insn-00bbf0fc)

~~~json
{
  "source": "00bbf0fc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf104`](#insn-00bbf104)

~~~json
{
  "source": "00bbf104",
  "target": "00bbf114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf108`](#insn-00bbf108)

~~~json
{
  "source": "00bbf108",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf110`](#insn-00bbf110)

~~~json
{
  "source": "00bbf110",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf120`](#insn-00bbf120)

~~~json
{
  "source": "00bbf120",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf138`](#insn-00bbf138)

~~~json
{
  "source": "00bbf138",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf140`](#insn-00bbf140)

~~~json
{
  "source": "00bbf140",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf14c`](#insn-00bbf14c)

~~~json
{
  "source": "00bbf14c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf154`](#insn-00bbf154)

~~~json
{
  "source": "00bbf154",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf15c`](#insn-00bbf15c)

~~~json
{
  "source": "00bbf15c",
  "target": "00bbf358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf164`](#insn-00bbf164)

~~~json
{
  "source": "00bbf164",
  "target": "00bbf1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf170`](#insn-00bbf170)

~~~json
{
  "source": "00bbf170",
  "target": "00bbf18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf17c`](#insn-00bbf17c)

~~~json
{
  "source": "00bbf17c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf184`](#insn-00bbf184)

~~~json
{
  "source": "00bbf184",
  "target": "00bbf194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf188`](#insn-00bbf188)

~~~json
{
  "source": "00bbf188",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf190`](#insn-00bbf190)

~~~json
{
  "source": "00bbf190",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf19c`](#insn-00bbf19c)

~~~json
{
  "source": "00bbf19c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1ac`](#insn-00bbf1ac)

~~~json
{
  "source": "00bbf1ac",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1b4`](#insn-00bbf1b4)

~~~json
{
  "source": "00bbf1b4",
  "target": "00bbf238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1c4`](#insn-00bbf1c4)

~~~json
{
  "source": "00bbf1c4",
  "target": "00bbf238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1d0`](#insn-00bbf1d0)

~~~json
{
  "source": "00bbf1d0",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1dc`](#insn-00bbf1dc)

~~~json
{
  "source": "00bbf1dc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1e4`](#insn-00bbf1e4)

~~~json
{
  "source": "00bbf1e4",
  "target": "00bbf1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1e8`](#insn-00bbf1e8)

~~~json
{
  "source": "00bbf1e8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1f0`](#insn-00bbf1f0)

~~~json
{
  "source": "00bbf1f0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf200`](#insn-00bbf200)

~~~json
{
  "source": "00bbf200",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf218`](#insn-00bbf218)

~~~json
{
  "source": "00bbf218",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf220`](#insn-00bbf220)

~~~json
{
  "source": "00bbf220",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf22c`](#insn-00bbf22c)

~~~json
{
  "source": "00bbf22c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf234`](#insn-00bbf234)

~~~json
{
  "source": "00bbf234",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf23c`](#insn-00bbf23c)

~~~json
{
  "source": "00bbf23c",
  "target": "00bbf358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf244`](#insn-00bbf244)

~~~json
{
  "source": "00bbf244",
  "target": "00bbf290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf250`](#insn-00bbf250)

~~~json
{
  "source": "00bbf250",
  "target": "00bbf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf25c`](#insn-00bbf25c)

~~~json
{
  "source": "00bbf25c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf264`](#insn-00bbf264)

~~~json
{
  "source": "00bbf264",
  "target": "00bbf274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf268`](#insn-00bbf268)

~~~json
{
  "source": "00bbf268",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf270`](#insn-00bbf270)

~~~json
{
  "source": "00bbf270",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf27c`](#insn-00bbf27c)

~~~json
{
  "source": "00bbf27c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf28c`](#insn-00bbf28c)

~~~json
{
  "source": "00bbf28c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf294`](#insn-00bbf294)

~~~json
{
  "source": "00bbf294",
  "target": "00bbf358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2a4`](#insn-00bbf2a4)

~~~json
{
  "source": "00bbf2a4",
  "target": "00bbf300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2b0`](#insn-00bbf2b0)

~~~json
{
  "source": "00bbf2b0",
  "target": "00bbf2cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2bc`](#insn-00bbf2bc)

~~~json
{
  "source": "00bbf2bc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2c4`](#insn-00bbf2c4)

~~~json
{
  "source": "00bbf2c4",
  "target": "00bbf2d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2c8`](#insn-00bbf2c8)

~~~json
{
  "source": "00bbf2c8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2d0`](#insn-00bbf2d0)

~~~json
{
  "source": "00bbf2d0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2e0`](#insn-00bbf2e0)

~~~json
{
  "source": "00bbf2e0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2f4`](#insn-00bbf2f4)

~~~json
{
  "source": "00bbf2f4",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2fc`](#insn-00bbf2fc)

~~~json
{
  "source": "00bbf2fc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf308`](#insn-00bbf308)

~~~json
{
  "source": "00bbf308",
  "target": "00bbf358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf310`](#insn-00bbf310)

~~~json
{
  "source": "00bbf310",
  "target": "00bbf358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf334`](#insn-00bbf334)

~~~json
{
  "source": "00bbf334",
  "target": "00c5d600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf338`](#insn-00bbf338)

~~~json
{
  "source": "00bbf338",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf34c`](#insn-00bbf34c)

~~~json
{
  "source": "00bbf34c",
  "target": "00bbf320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf364`](#insn-00bbf364)

~~~json
{
  "source": "00bbf364",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf36c`](#insn-00bbf36c)

~~~json
{
  "source": "00bbf36c",
  "target": "00bbf3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf380`](#insn-00bbf380)

~~~json
{
  "source": "00bbf380",
  "target": "00bbf38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf388`](#insn-00bbf388)

~~~json
{
  "source": "00bbf388",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf398`](#insn-00bbf398)

~~~json
{
  "source": "00bbf398",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3a4`](#insn-00bbf3a4)

~~~json
{
  "source": "00bbf3a4",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3b0`](#insn-00bbf3b0)

~~~json
{
  "source": "00bbf3b0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3c0`](#insn-00bbf3c0)

~~~json
{
  "source": "00bbf3c0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3c8`](#insn-00bbf3c8)

~~~json
{
  "source": "00bbf3c8",
  "target": "00bbf438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3d8`](#insn-00bbf3d8)

~~~json
{
  "source": "00bbf3d8",
  "target": "00bbf438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3e8`](#insn-00bbf3e8)

~~~json
{
  "source": "00bbf3e8",
  "target": "00bbf3f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3f0`](#insn-00bbf3f0)

~~~json
{
  "source": "00bbf3f0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf400`](#insn-00bbf400)

~~~json
{
  "source": "00bbf400",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf40c`](#insn-00bbf40c)

~~~json
{
  "source": "00bbf40c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf41c`](#insn-00bbf41c)

~~~json
{
  "source": "00bbf41c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf42c`](#insn-00bbf42c)

~~~json
{
  "source": "00bbf42c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf434`](#insn-00bbf434)

~~~json
{
  "source": "00bbf434",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf43c`](#insn-00bbf43c)

~~~json
{
  "source": "00bbf43c",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf444`](#insn-00bbf444)

~~~json
{
  "source": "00bbf444",
  "target": "00bbf49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf458`](#insn-00bbf458)

~~~json
{
  "source": "00bbf458",
  "target": "00bbf464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf460`](#insn-00bbf460)

~~~json
{
  "source": "00bbf460",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf470`](#insn-00bbf470)

~~~json
{
  "source": "00bbf470",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf47c`](#insn-00bbf47c)

~~~json
{
  "source": "00bbf47c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf488`](#insn-00bbf488)

~~~json
{
  "source": "00bbf488",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf498`](#insn-00bbf498)

~~~json
{
  "source": "00bbf498",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4a0`](#insn-00bbf4a0)

~~~json
{
  "source": "00bbf4a0",
  "target": "00bbf52c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4b0`](#insn-00bbf4b0)

~~~json
{
  "source": "00bbf4b0",
  "target": "00bbf52c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4c0`](#insn-00bbf4c0)

~~~json
{
  "source": "00bbf4c0",
  "target": "00bbf4cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4c8`](#insn-00bbf4c8)

~~~json
{
  "source": "00bbf4c8",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4d8`](#insn-00bbf4d8)

~~~json
{
  "source": "00bbf4d8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4e4`](#insn-00bbf4e4)

~~~json
{
  "source": "00bbf4e4",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4f4`](#insn-00bbf4f4)

~~~json
{
  "source": "00bbf4f4",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf50c`](#insn-00bbf50c)

~~~json
{
  "source": "00bbf50c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf514`](#insn-00bbf514)

~~~json
{
  "source": "00bbf514",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf520`](#insn-00bbf520)

~~~json
{
  "source": "00bbf520",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf528`](#insn-00bbf528)

~~~json
{
  "source": "00bbf528",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf530`](#insn-00bbf530)

~~~json
{
  "source": "00bbf530",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf538`](#insn-00bbf538)

~~~json
{
  "source": "00bbf538",
  "target": "00bbf590",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf54c`](#insn-00bbf54c)

~~~json
{
  "source": "00bbf54c",
  "target": "00bbf558",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf554`](#insn-00bbf554)

~~~json
{
  "source": "00bbf554",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf564`](#insn-00bbf564)

~~~json
{
  "source": "00bbf564",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf570`](#insn-00bbf570)

~~~json
{
  "source": "00bbf570",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf57c`](#insn-00bbf57c)

~~~json
{
  "source": "00bbf57c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf58c`](#insn-00bbf58c)

~~~json
{
  "source": "00bbf58c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf594`](#insn-00bbf594)

~~~json
{
  "source": "00bbf594",
  "target": "00bbf620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5a4`](#insn-00bbf5a4)

~~~json
{
  "source": "00bbf5a4",
  "target": "00bbf620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5b4`](#insn-00bbf5b4)

~~~json
{
  "source": "00bbf5b4",
  "target": "00bbf5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5bc`](#insn-00bbf5bc)

~~~json
{
  "source": "00bbf5bc",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5cc`](#insn-00bbf5cc)

~~~json
{
  "source": "00bbf5cc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5d8`](#insn-00bbf5d8)

~~~json
{
  "source": "00bbf5d8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5e8`](#insn-00bbf5e8)

~~~json
{
  "source": "00bbf5e8",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf600`](#insn-00bbf600)

~~~json
{
  "source": "00bbf600",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf608`](#insn-00bbf608)

~~~json
{
  "source": "00bbf608",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf614`](#insn-00bbf614)

~~~json
{
  "source": "00bbf614",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf61c`](#insn-00bbf61c)

~~~json
{
  "source": "00bbf61c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf624`](#insn-00bbf624)

~~~json
{
  "source": "00bbf624",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf62c`](#insn-00bbf62c)

~~~json
{
  "source": "00bbf62c",
  "target": "00bbf684",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf640`](#insn-00bbf640)

~~~json
{
  "source": "00bbf640",
  "target": "00bbf64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf648`](#insn-00bbf648)

~~~json
{
  "source": "00bbf648",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf658`](#insn-00bbf658)

~~~json
{
  "source": "00bbf658",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf664`](#insn-00bbf664)

~~~json
{
  "source": "00bbf664",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf670`](#insn-00bbf670)

~~~json
{
  "source": "00bbf670",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf680`](#insn-00bbf680)

~~~json
{
  "source": "00bbf680",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf688`](#insn-00bbf688)

~~~json
{
  "source": "00bbf688",
  "target": "00bbf714",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf698`](#insn-00bbf698)

~~~json
{
  "source": "00bbf698",
  "target": "00bbf714",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6a8`](#insn-00bbf6a8)

~~~json
{
  "source": "00bbf6a8",
  "target": "00bbf6b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6b0`](#insn-00bbf6b0)

~~~json
{
  "source": "00bbf6b0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6c0`](#insn-00bbf6c0)

~~~json
{
  "source": "00bbf6c0",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6cc`](#insn-00bbf6cc)

~~~json
{
  "source": "00bbf6cc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6dc`](#insn-00bbf6dc)

~~~json
{
  "source": "00bbf6dc",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6f4`](#insn-00bbf6f4)

~~~json
{
  "source": "00bbf6f4",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6fc`](#insn-00bbf6fc)

~~~json
{
  "source": "00bbf6fc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf708`](#insn-00bbf708)

~~~json
{
  "source": "00bbf708",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf710`](#insn-00bbf710)

~~~json
{
  "source": "00bbf710",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf718`](#insn-00bbf718)

~~~json
{
  "source": "00bbf718",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf720`](#insn-00bbf720)

~~~json
{
  "source": "00bbf720",
  "target": "00bbf75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf734`](#insn-00bbf734)

~~~json
{
  "source": "00bbf734",
  "target": "00bbf740",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf73c`](#insn-00bbf73c)

~~~json
{
  "source": "00bbf73c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf74c`](#insn-00bbf74c)

~~~json
{
  "source": "00bbf74c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf758`](#insn-00bbf758)

~~~json
{
  "source": "00bbf758",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf760`](#insn-00bbf760)

~~~json
{
  "source": "00bbf760",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf768`](#insn-00bbf768)

~~~json
{
  "source": "00bbf768",
  "target": "00bbf7c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf77c`](#insn-00bbf77c)

~~~json
{
  "source": "00bbf77c",
  "target": "00bbf788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf784`](#insn-00bbf784)

~~~json
{
  "source": "00bbf784",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf794`](#insn-00bbf794)

~~~json
{
  "source": "00bbf794",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7a0`](#insn-00bbf7a0)

~~~json
{
  "source": "00bbf7a0",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7ac`](#insn-00bbf7ac)

~~~json
{
  "source": "00bbf7ac",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7bc`](#insn-00bbf7bc)

~~~json
{
  "source": "00bbf7bc",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7c4`](#insn-00bbf7c4)

~~~json
{
  "source": "00bbf7c4",
  "target": "00bbf850",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7d4`](#insn-00bbf7d4)

~~~json
{
  "source": "00bbf7d4",
  "target": "00bbf850",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7e4`](#insn-00bbf7e4)

~~~json
{
  "source": "00bbf7e4",
  "target": "00bbf7f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7ec`](#insn-00bbf7ec)

~~~json
{
  "source": "00bbf7ec",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7fc`](#insn-00bbf7fc)

~~~json
{
  "source": "00bbf7fc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf808`](#insn-00bbf808)

~~~json
{
  "source": "00bbf808",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf818`](#insn-00bbf818)

~~~json
{
  "source": "00bbf818",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf830`](#insn-00bbf830)

~~~json
{
  "source": "00bbf830",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf838`](#insn-00bbf838)

~~~json
{
  "source": "00bbf838",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf844`](#insn-00bbf844)

~~~json
{
  "source": "00bbf844",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf84c`](#insn-00bbf84c)

~~~json
{
  "source": "00bbf84c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf854`](#insn-00bbf854)

~~~json
{
  "source": "00bbf854",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf85c`](#insn-00bbf85c)

~~~json
{
  "source": "00bbf85c",
  "target": "00bbf8b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf870`](#insn-00bbf870)

~~~json
{
  "source": "00bbf870",
  "target": "00bbf87c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf878`](#insn-00bbf878)

~~~json
{
  "source": "00bbf878",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf888`](#insn-00bbf888)

~~~json
{
  "source": "00bbf888",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf894`](#insn-00bbf894)

~~~json
{
  "source": "00bbf894",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8a0`](#insn-00bbf8a0)

~~~json
{
  "source": "00bbf8a0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8b0`](#insn-00bbf8b0)

~~~json
{
  "source": "00bbf8b0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8b8`](#insn-00bbf8b8)

~~~json
{
  "source": "00bbf8b8",
  "target": "00bbf944",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8c8`](#insn-00bbf8c8)

~~~json
{
  "source": "00bbf8c8",
  "target": "00bbf944",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8d8`](#insn-00bbf8d8)

~~~json
{
  "source": "00bbf8d8",
  "target": "00bbf8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8e0`](#insn-00bbf8e0)

~~~json
{
  "source": "00bbf8e0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8f0`](#insn-00bbf8f0)

~~~json
{
  "source": "00bbf8f0",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8fc`](#insn-00bbf8fc)

~~~json
{
  "source": "00bbf8fc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf90c`](#insn-00bbf90c)

~~~json
{
  "source": "00bbf90c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf924`](#insn-00bbf924)

~~~json
{
  "source": "00bbf924",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf92c`](#insn-00bbf92c)

~~~json
{
  "source": "00bbf92c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf938`](#insn-00bbf938)

~~~json
{
  "source": "00bbf938",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf940`](#insn-00bbf940)

~~~json
{
  "source": "00bbf940",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf948`](#insn-00bbf948)

~~~json
{
  "source": "00bbf948",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf950`](#insn-00bbf950)

~~~json
{
  "source": "00bbf950",
  "target": "00bbf9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf964`](#insn-00bbf964)

~~~json
{
  "source": "00bbf964",
  "target": "00bbf970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf96c`](#insn-00bbf96c)

~~~json
{
  "source": "00bbf96c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf97c`](#insn-00bbf97c)

~~~json
{
  "source": "00bbf97c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf988`](#insn-00bbf988)

~~~json
{
  "source": "00bbf988",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf994`](#insn-00bbf994)

~~~json
{
  "source": "00bbf994",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9a4`](#insn-00bbf9a4)

~~~json
{
  "source": "00bbf9a4",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9ac`](#insn-00bbf9ac)

~~~json
{
  "source": "00bbf9ac",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9bc`](#insn-00bbf9bc)

~~~json
{
  "source": "00bbf9bc",
  "target": "00bbf9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9c4`](#insn-00bbf9c4)

~~~json
{
  "source": "00bbf9c4",
  "target": "00c5d5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf9c8`](#insn-00bbf9c8)

~~~json
{
  "source": "00bbf9c8",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9e0`](#insn-00bbf9e0)

~~~json
{
  "source": "00bbf9e0",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9e8`](#insn-00bbf9e8)

~~~json
{
  "source": "00bbf9e8",
  "target": "00bbfa14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9f8`](#insn-00bbf9f8)

~~~json
{
  "source": "00bbf9f8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa10`](#insn-00bbfa10)

~~~json
{
  "source": "00bbfa10",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa18`](#insn-00bbfa18)

~~~json
{
  "source": "00bbfa18",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa20`](#insn-00bbfa20)

~~~json
{
  "source": "00bbfa20",
  "target": "00bbfa78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa34`](#insn-00bbfa34)

~~~json
{
  "source": "00bbfa34",
  "target": "00bbfa40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa3c`](#insn-00bbfa3c)

~~~json
{
  "source": "00bbfa3c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa4c`](#insn-00bbfa4c)

~~~json
{
  "source": "00bbfa4c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa58`](#insn-00bbfa58)

~~~json
{
  "source": "00bbfa58",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa64`](#insn-00bbfa64)

~~~json
{
  "source": "00bbfa64",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa74`](#insn-00bbfa74)

~~~json
{
  "source": "00bbfa74",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa7c`](#insn-00bbfa7c)

~~~json
{
  "source": "00bbfa7c",
  "target": "00bbfb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa8c`](#insn-00bbfa8c)

~~~json
{
  "source": "00bbfa8c",
  "target": "00bbfb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa9c`](#insn-00bbfa9c)

~~~json
{
  "source": "00bbfa9c",
  "target": "00bbfaa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfaa4`](#insn-00bbfaa4)

~~~json
{
  "source": "00bbfaa4",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfab4`](#insn-00bbfab4)

~~~json
{
  "source": "00bbfab4",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfac0`](#insn-00bbfac0)

~~~json
{
  "source": "00bbfac0",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfad0`](#insn-00bbfad0)

~~~json
{
  "source": "00bbfad0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfae8`](#insn-00bbfae8)

~~~json
{
  "source": "00bbfae8",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfaf0`](#insn-00bbfaf0)

~~~json
{
  "source": "00bbfaf0",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfafc`](#insn-00bbfafc)

~~~json
{
  "source": "00bbfafc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb04`](#insn-00bbfb04)

~~~json
{
  "source": "00bbfb04",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb0c`](#insn-00bbfb0c)

~~~json
{
  "source": "00bbfb0c",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb14`](#insn-00bbfb14)

~~~json
{
  "source": "00bbfb14",
  "target": "00bbfb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb28`](#insn-00bbfb28)

~~~json
{
  "source": "00bbfb28",
  "target": "00bbfb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb30`](#insn-00bbfb30)

~~~json
{
  "source": "00bbfb30",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb40`](#insn-00bbfb40)

~~~json
{
  "source": "00bbfb40",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb4c`](#insn-00bbfb4c)

~~~json
{
  "source": "00bbfb4c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb54`](#insn-00bbfb54)

~~~json
{
  "source": "00bbfb54",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb5c`](#insn-00bbfb5c)

~~~json
{
  "source": "00bbfb5c",
  "target": "00bbfbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb70`](#insn-00bbfb70)

~~~json
{
  "source": "00bbfb70",
  "target": "00bbfb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb78`](#insn-00bbfb78)

~~~json
{
  "source": "00bbfb78",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb88`](#insn-00bbfb88)

~~~json
{
  "source": "00bbfb88",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb94`](#insn-00bbfb94)

~~~json
{
  "source": "00bbfb94",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfba0`](#insn-00bbfba0)

~~~json
{
  "source": "00bbfba0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbb0`](#insn-00bbfbb0)

~~~json
{
  "source": "00bbfbb0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbb8`](#insn-00bbfbb8)

~~~json
{
  "source": "00bbfbb8",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbc8`](#insn-00bbfbc8)

~~~json
{
  "source": "00bbfbc8",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbd8`](#insn-00bbfbd8)

~~~json
{
  "source": "00bbfbd8",
  "target": "00bbfbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbe0`](#insn-00bbfbe0)

~~~json
{
  "source": "00bbfbe0",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbf0`](#insn-00bbfbf0)

~~~json
{
  "source": "00bbfbf0",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbfc`](#insn-00bbfbfc)

~~~json
{
  "source": "00bbfbfc",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc0c`](#insn-00bbfc0c)

~~~json
{
  "source": "00bbfc0c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc24`](#insn-00bbfc24)

~~~json
{
  "source": "00bbfc24",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc2c`](#insn-00bbfc2c)

~~~json
{
  "source": "00bbfc2c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc38`](#insn-00bbfc38)

~~~json
{
  "source": "00bbfc38",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc40`](#insn-00bbfc40)

~~~json
{
  "source": "00bbfc40",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc48`](#insn-00bbfc48)

~~~json
{
  "source": "00bbfc48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc4c`](#insn-00bbfc4c)

~~~json
{
  "source": "00bbfc4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc50`](#insn-00bbfc50)

~~~json
{
  "source": "00bbfc50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc6c`](#insn-00bbfc6c)

~~~json
{
  "source": "00bbfc6c",
  "target": "00bbfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
