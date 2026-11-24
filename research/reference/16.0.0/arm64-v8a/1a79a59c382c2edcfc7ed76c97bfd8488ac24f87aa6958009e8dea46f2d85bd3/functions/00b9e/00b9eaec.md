# 00b9eaec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0173.md#review-8a1d3a9cb3715f1a27ab11715e3ca427)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b9ef14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9e/00b9ef14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-f2213cd3a5c09dde97598a286318ebb1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b9eaec",
  "name": "_ZNK10reflection5Field6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 2168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1eb2cd145dd4472f86d9e1a35191549663587366ce992c4842ab7d7657060f62",
  "source_text_sha256": "1eb2cd145dd4472f86d9e1a35191549663587366ce992c4842ab7d7657060f62",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b9eaec",
        "00b9f363"
      ]
    ],
    "bytes_sha256": "4ff9c7fb91fab72f41e26bbc830c0e10cfd07947dc808ca9d67f06189a73a86e",
    "instruction_count": 542,
    "instruction_bytes": 2168,
    "body_bytes": 2168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c550](../00c5c/00c5c550.md)

## 呼び出し先

- [00c5c540](../00c5c/00c5c540.md)
- [00c5c5b0](../00c5c/00c5c5b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 22927 bytes

~~~c

undefined8
_ZNK10reflection5Field6VerifyERN11flatbuffers16VerifierTemplateILb0EEE(int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  ulong uVar3;
  uint *puVar4;
  uint *puVar5;
  ushort uVar6;
  int iVar7;
  long lVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  long lVar13;
  ushort *puVar14;
  ulong uVar15;
  
                    /* try { // try from 00b9eaec to 00c9eaf3 has its CatchHandler @ 00b9eafc */
                    /* catch() { ... } // from try @ 00b9e7b8 with catch @ 00b9eaf4
                       try { // try from 00b9eaf4 to 00c9ebef has its CatchHandler @ 00b9c4f4 */
                    /* catch() { ... } // from try @ 00b9e7c0 with catch @ 00b9eaf8 */
                    /* catch() { ... } // from try @ 00b9eaec with catch @ 00b9eafc */
  lVar8 = *param_2;
  uVar9 = (long)param_1 - lVar8;
                    /* catch() { ... } // from try @ 00b9e510 with catch @ 00b9eb14 */
  if (((uVar9 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar11 = param_2[1];
    if (uVar11 < 5) {
      return 0;
    }
                    /* catch() { ... } // from try @ 00b9ead0 with catch @ 00b9eb2c */
    uVar10 = uVar11 - 4;
    if (uVar10 < uVar9) {
      return 0;
    }
    iVar7 = *param_1;
                    /* catch() { ... } // from try @ 00b9e274 with catch @ 00b9eb44 */
    uVar1 = (int)param_2[7] + 1;
                    /* catch() { ... } // from try @ 00b9eab4 with catch @ 00b9eb48 */
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
                    /* catch() { ... } // from try @ 00b9e20c with catch @ 00b9eb60 */
                    /* catch() { ... } // from try @ 00b9e240 with catch @ 00b9eb68 */
                    /* catch() { ... } // from try @ 00b9d574 with catch @ 00b9eb70
                       catch() { ... } // from try @ 00b9d630 with catch @ 00b9eb70
                       catch() { ... } // from try @ 00b9d71c with catch @ 00b9eb70
                       catch() { ... } // from try @ 00b9e4e0 with catch @ 00b9eb70
                       catch() { ... } // from try @ 00b9e6e0 with catch @ 00b9eb70 */
                    /* catch() { ... } // from try @ 00b9e148 with catch @ 00b9eb74 */
                    /* catch() { ... } // from try @ 00b9d680 with catch @ 00b9eb7c */
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar12 = uVar9 - (long)iVar7, (uVar12 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar12 <= uVar11 - 2)) {
                    /* catch() { ... } // from try @ 00b9e2e4 with catch @ 00b9eb80 */
      uVar6 = *(ushort *)(lVar8 + uVar12);
                    /* catch() { ... } // from try @ 00b9cda8 with catch @ 00b9eb84
                       catch() { ... } // from try @ 00b9d598 with catch @ 00b9eb84
                       catch() { ... } // from try @ 00b9d670 with catch @ 00b9eb84 */
                    /* catch() { ... } // from try @ 00b9d200 with catch @ 00b9eb88 */
                    /* catch() { ... } // from try @ 00b9e2ec with catch @ 00b9eb8c */
      if ((((uVar6 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar6 & 1) == 0)) {
        if (uVar11 <= uVar6) {
          return 0;
        }
        if (uVar11 - uVar6 < uVar12) {
          return 0;
        }
        lVar13 = (long)*param_1;
        puVar14 = (ushort *)((long)param_1 - lVar13);
        uVar6 = *puVar14;
                    /* catch() { ... } // from try @ 00b9d1a4 with catch @ 00b9ebb4 */
                    /* catch() { ... } // from try @ 00b9d154 with catch @ 00b9ebb8 */
                    /* catch() { ... } // from try @ 00b9c7bc with catch @ 00b9ebbc */
                    /* catch() { ... } // from try @ 00b9d07c with catch @ 00b9ebc0 */
        if ((4 < uVar6) && (uVar12 = (ulong)puVar14[2], uVar12 != 0)) {
                    /* catch() { ... } // from try @ 00b9cfc0 with catch @ 00b9ebc4 */
          uVar3 = uVar9 + uVar12;
                    /* catch() { ... } // from try @ 00b9cf0c with catch @ 00b9ebc8 */
                    /* catch() { ... } // from try @ 00b9d4b4 with catch @ 00b9ebcc */
          if ((uVar3 & 3) == 0) {
            if (uVar10 < uVar3) {
              return 0;
            }
          }
          else {
                    /* catch() { ... } // from try @ 00b9d3e8 with catch @ 00b9ebd0 */
                    /* catch() { ... } // from try @ 00b9d324 with catch @ 00b9ebd4 */
            if ((char)param_2[3] != '\0') {
              return 0;
            }
            if (uVar10 < uVar3) {
              return 0;
            }
          }
                    /* try { // try from 00b9ebf0 to 00c9ec7b has its CatchHandler @ 00b9ebf0
                       catch() { ... } // from try @ 00b9ebf0 with catch @ 00b9ebf0
                       catch() { ... } // from try @ 00b9ed68 with catch @ 00b9ebf0
                       catch() { ... } // from try @ 00b9ef44 with catch @ 00b9ebf0 */
          if ((0 < (int)*(uint *)(lVar8 + uVar3)) &&
             (uVar15 = uVar11 - 1, uVar3 + *(uint *)(lVar8 + uVar3) <= uVar15)) {
            puVar4 = (uint *)((long)((long)param_1 + uVar12) +
                             (ulong)*(uint *)((long)param_1 + uVar12));
            if (puVar4 == (uint *)0x0) {
              if (uVar6 < 7) {
                return 0;
              }
            }
            else {
              uVar12 = (long)puVar4 - lVar8;
              if ((uVar12 & 3) == 0) {
                if (uVar10 < uVar12) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar10 < uVar12) {
                  return 0;
                }
              }
              if ((ulong)param_2[4] <= (ulong)*puVar4) {
                return 0;
              }
              uVar3 = (ulong)*puVar4 + 4;
              if (uVar15 < uVar3 + uVar12) {
                return 0;
              }
              if (uVar11 <= uVar3) {
                return 0;
              }
              if (uVar11 - uVar3 < uVar12) {
                return 0;
              }
              if (uVar6 < 7) {
                return 0;
              }
              if (*(char *)(lVar8 + uVar3 + uVar12) != '\0') {
                return 0;
              }
            }
            uVar11 = (ulong)puVar14[3];
            if (uVar11 != 0) {
              uVar9 = uVar9 + uVar11;
              if ((uVar9 & 3) == 0) {
                if (uVar10 < uVar9) {
                  return 0;
                }
              }
              else {
                    /* try { // try from 00b9ec7c to 00c9ec87 has its CatchHandler @ 00b9ef54 */
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                    /* try { // try from 00b9ec88 to 00c9ed67 has its CatchHandler @ 00b9ef58 */
                if (uVar10 < uVar9) {
                  return 0;
                }
              }
              if ((0 < (int)*(uint *)(lVar8 + uVar9)) &&
                 (uVar9 + *(uint *)(lVar8 + uVar9) <= uVar15)) {
                lVar8 = (long)((long)param_1 + uVar11) + (ulong)*(uint *)((long)param_1 + uVar11);
                if (lVar8 != 0) {
                  uVar9 = _ZNK10reflection4Type6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                    (lVar8,param_2);
                  if ((uVar9 & 1) == 0) {
                    return 0;
                  }
                  lVar13 = (long)*param_1;
                }
                lVar13 = -lVar13;
                puVar14 = (ushort *)((long)param_1 + lVar13);
                uVar6 = *puVar14;
                if (8 < uVar6) {
                  if ((ulong)puVar14[4] != 0) {
                    /* try { // try from 00b9ed68 to 00c9ede3 has its CatchHandler @ 00b9ebf0 */
                    uVar9 = (long)param_1 + ((ulong)puVar14[4] - *param_2);
                    if (((uVar9 & 1) != 0) && ((char)param_2[3] != '\0')) {
                      return 0;
                    }
                    if ((ulong)param_2[1] < 3) {
                      return 0;
                    }
                    if (param_2[1] - 2U < uVar9) {
                      return 0;
                    }
                  }
                  if (10 < uVar6) {
                    if ((ulong)puVar14[5] != 0) {
                      uVar9 = (long)param_1 + ((ulong)puVar14[5] - *param_2);
                      if (((uVar9 & 1) != 0) && ((char)param_2[3] != '\0')) {
                        return 0;
                      }
                    /* try { // try from 00b9ede4 to 00c9edeb has its CatchHandler @ 00b9ef48 */
                      if ((ulong)param_2[1] < 3) {
                        return 0;
                      }
                    /* try { // try from 00b9edec to 00c9ee37 has its CatchHandler @ 00b9ef4c */
                      if (param_2[1] - 2U < uVar9) {
                        return 0;
                      }
                    }
                    if (0xc < uVar6) {
                      if ((ulong)puVar14[6] != 0) {
                        uVar9 = (long)param_1 + ((ulong)puVar14[6] - *param_2);
                        if (((uVar9 & 7) != 0) && ((char)param_2[3] != '\0')) {
                          return 0;
                        }
                        if ((ulong)param_2[1] < 9) {
                          return 0;
                        }
                        if (param_2[1] - 8U < uVar9) {
                          return 0;
                        }
                      }
                      if (0xe < uVar6) {
                        if ((ulong)puVar14[7] != 0) {
                          uVar9 = (long)param_1 + ((ulong)puVar14[7] - *param_2);
                    /* try { // try from 00b9ee6c to 00c9ee6f has its CatchHandler @ 00b9ef44 */
                          if (((uVar9 & 7) != 0) && ((char)param_2[3] != '\0')) {
                            return 0;
                          }
                          if ((ulong)param_2[1] < 9) {
                            return 0;
                          }
                          if (param_2[1] - 8U < uVar9) {
                            return 0;
                          }
                        }
                        if (0x10 < uVar6) {
                          if ((ulong)puVar14[8] != 0) {
                            if ((ulong)param_2[1] < 2) {
                              return 0;
                            }
                            if (param_2[1] - 1U < (long)param_1 + ((ulong)puVar14[8] - *param_2)) {
                              return 0;
                            }
                          }
                          if (0x12 < uVar6) {
                            if ((ulong)puVar14[9] != 0) {
                              if ((ulong)param_2[1] < 2) {
                                return 0;
                              }
                              if (param_2[1] - 1U < (long)param_1 + ((ulong)puVar14[9] - *param_2))
                              {
                                return 0;
                              }
                            }
                    /* try { // try from 00b9ef24 to 00c9ef43 has its CatchHandler @ 00b9ef50 */
                            if (0x14 < uVar6) {
                              if ((ulong)puVar14[10] != 0) {
                    /* catch() { ... } // from try @ 00b9ee6c with catch @ 00b9ef44
                       try { // try from 00b9ef44 to 00c9ef9b has its CatchHandler @ 00b9ebf0 */
                                if ((ulong)param_2[1] < 2) {
                                  return 0;
                                }
                    /* catch() { ... } // from try @ 00b9ede4 with catch @ 00b9ef48 */
                    /* catch() { ... } // from try @ 00b9edec with catch @ 00b9ef4c */
                    /* catch() { ... } // from try @ 00b9ef24 with catch @ 00b9ef50 */
                    /* catch() { ... } // from try @ 00b9ec7c with catch @ 00b9ef54 */
                    /* catch() { ... } // from try @ 00b9ec88 with catch @ 00b9ef58 */
                                if (param_2[1] - 1U <
                                    (long)param_1 + ((ulong)puVar14[10] - *param_2)) {
                                  return 0;
                                }
                              }
                              if (0x16 < uVar6) {
                                if ((ulong)puVar14[0xb] != 0) {
                                  uVar9 = (long)param_1 + ((ulong)puVar14[0xb] - *param_2);
                                  if (((uVar9 & 3) != 0) && ((char)param_2[3] != '\0')) {
                                    return 0;
                                  }
                    /* catch() { ... } // from try @ 00b9f094 with catch @ 00b9ef9c
                       catch() { ... } // from try @ 00b9f19c with catch @ 00b9ef9c */
                                  uVar11 = param_2[1];
                                  if (uVar11 < 5) {
                                    return 0;
                                  }
                                  if (uVar11 - 4 < uVar9) {
                                    return 0;
                                  }
                                  uVar1 = *(uint *)(*param_2 + uVar9);
                                  if ((int)uVar1 < 1) {
                                    return 0;
                                  }
                                  if (uVar11 - 1 < uVar9 + uVar1) {
                                    return 0;
                                  }
                                }
                                if ((ulong)puVar14[0xb] != 0) {
                                  puVar5 = (uint *)((long)param_1 + (ulong)puVar14[0xb]);
                                  puVar4 = (uint *)((long)puVar5 + (ulong)*puVar5);
                                  if (puVar4 != (uint *)0x0) {
                                    uVar9 = (long)puVar4 - *param_2;
                                    if (((uVar9 & 3) != 0) && ((char)param_2[3] != '\0')) {
                                      return 0;
                                    }
                                    uVar11 = param_2[1];
                                    if (uVar11 < 5) {
                                      return 0;
                                    }
                                    if (uVar11 - 4 < uVar9) {
                                      return 0;
                                    }
                                    if ((ulong)param_2[4] >> 2 <= (ulong)*puVar4) {
                                      return 0;
                                    }
                                    uVar10 = (ulong)*puVar4 * 4 + 4;
                                    if (uVar11 <= uVar10) {
                                      return 0;
                                    }
                                    if (uVar11 - uVar10 < uVar9) {
                                      return 0;
                                    }
                                  }
                                  puVar5 = (uint *)((long)puVar5 + (ulong)*puVar5);
                                  if ((puVar5 != (uint *)0x0) && (*puVar5 != 0)) {
                                    uVar11 = 0;
                                    uVar9 = 0;
                                    do {
                                      puVar4 = (uint *)((long)puVar5 + (uVar11 & 0xfffffffc) + 4);
                    /* try { // try from 00b9f090 to 00c9f093 has its CatchHandler @ 00b9f1a0 */
                    /* try { // try from 00b9f094 to 00c9f0f7 has its CatchHandler @ 00b9ef9c */
                                      uVar10 = _ZNK10reflection8KeyValue6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                                         ((long)puVar4 + (ulong)*puVar4,param_2);
                                      if ((uVar10 & 1) == 0) {
                                        return 0;
                                      }
                                      uVar9 = uVar9 + 1;
                                      uVar11 = uVar11 + 4;
                                    } while (uVar9 < *puVar5);
                                    lVar13 = -(long)*param_1;
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
                puVar14 = (ushort *)((long)param_1 + lVar13);
                uVar6 = *puVar14;
                if (0x18 < uVar6) {
                  if ((ulong)puVar14[0xc] != 0) {
                    uVar9 = (long)param_1 + ((ulong)puVar14[0xc] - *param_2);
                    /* try { // try from 00b9f0f8 to 00c9f0ff has its CatchHandler @ 00b9f19c */
                    if (((uVar9 & 3) != 0) && ((char)param_2[3] != '\0')) {
                      return 0;
                    }
                    uVar11 = param_2[1];
                    if (uVar11 < 5) {
                      return 0;
                    }
                    if (uVar11 - 4 < uVar9) {
                      return 0;
                    }
                    uVar1 = *(uint *)(*param_2 + uVar9);
                    if ((int)uVar1 < 1) {
                      return 0;
                    }
                    if (uVar11 - 1 < uVar9 + uVar1) {
                      return 0;
                    }
                  }
                  if ((ulong)puVar14[0xc] != 0) {
                    puVar5 = (uint *)((long)param_1 + (ulong)puVar14[0xc]);
                    puVar4 = (uint *)((long)puVar5 + (ulong)*puVar5);
                    if (puVar4 != (uint *)0x0) {
                      uVar9 = (long)puVar4 - *param_2;
                    /* try { // try from 00b9f174 to 00c9f19b has its CatchHandler @ 00b9f1b0 */
                      if (((uVar9 & 3) != 0) && ((char)param_2[3] != '\0')) {
                        return 0;
                      }
                      uVar11 = param_2[1];
                      if (uVar11 < 5) {
                        return 0;
                      }
                      if (uVar11 - 4 < uVar9) {
                        return 0;
                      }
                    /* catch() { ... } // from try @ 00b9f0f8 with catch @ 00b9f19c
                       try { // try from 00b9f19c to 00c9f1e7 has its CatchHandler @ 00b9ef9c */
                    /* catch() { ... } // from try @ 00b9f090 with catch @ 00b9f1a0 */
                      if ((ulong)param_2[4] >> 2 <= (ulong)*puVar4) {
                        return 0;
                      }
                    /* catch() { ... } // from try @ 00b9f174 with catch @ 00b9f1b0 */
                      uVar10 = (ulong)*puVar4 * 4 + 4;
                      if (uVar11 <= uVar10) {
                        return 0;
                      }
                      if (uVar11 - uVar10 < uVar9) {
                        return 0;
                      }
                    }
                    puVar5 = (uint *)((long)puVar5 + (ulong)*puVar5);
                    if ((puVar5 != (uint *)0x0) && (*puVar5 != 0)) {
                      uVar9 = 0;
                      uVar11 = param_2[1];
                      do {
                        puVar4 = (uint *)((long)puVar5 + (uVar9 & 0xfffffffc) + 4);
                        puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4);
                        uVar10 = (long)puVar4 - *param_2;
                    /* try { // try from 00b9f220 to 00c9f307 has its CatchHandler @ 00b9f220
                       catch() { ... } // from try @ 00b9f220 with catch @ 00b9f220
                       catch() { ... } // from try @ 00b9f310 with catch @ 00b9f220 */
                        if ((char)param_2[3] != '\0' && (uVar10 & 3) != 0) {
                          return 0;
                        }
                        if (uVar11 < 5) {
                          return 0;
                        }
                        if (uVar11 - 4 < uVar10) {
                          return 0;
                        }
                        uVar12 = (ulong)*puVar4;
                        if ((ulong)param_2[4] <= uVar12) {
                          return 0;
                        }
                        uVar12 = uVar12 + 4;
                        if (uVar11 - 1 < uVar12 + uVar10) {
                          return 0;
                        }
                        if (uVar11 <= uVar12) {
                          return 0;
                        }
                        if (uVar11 - uVar12 < uVar10) {
                          return 0;
                        }
                        if (*(char *)(*param_2 + uVar12 + uVar10) != '\0') {
                          return 0;
                        }
                        uVar9 = uVar9 + 4;
                      } while ((ulong)*puVar5 * 4 - uVar9 != 0);
                    }
                  }
                  if (0x1a < uVar6) {
                    if ((ulong)puVar14[0xd] != 0) {
                      if ((ulong)param_2[1] < 2) {
                        return 0;
                      }
                      if (param_2[1] - 1U < (long)param_1 + ((ulong)puVar14[0xd] - *param_2)) {
                        return 0;
                      }
                    }
                    if (0x1c < uVar6) {
                      if ((ulong)puVar14[0xe] != 0) {
                        uVar9 = (long)param_1 + ((ulong)puVar14[0xe] - *param_2);
                        if (((uVar9 & 1) != 0) && ((char)param_2[3] != '\0')) {
                          return 0;
                        }
                        if ((ulong)param_2[1] < 3) {
                          return 0;
                        }
                    /* try { // try from 00b9f308 to 00c9f30f has its CatchHandler @ 00b9f438 */
                    /* try { // try from 00b9f310 to 00c9f45f has its CatchHandler @ 00b9f220 */
                        if (param_2[1] - 2U < uVar9) {
                          return 0;
                        }
                      }
                      if ((0x1e < uVar6) && ((ulong)puVar14[0xf] != 0)) {
                        if ((ulong)param_2[1] < 2) {
                          return 0;
                        }
                        if (param_2[1] - 1U < (long)param_1 + ((ulong)puVar14[0xf] - *param_2)) {
                          return 0;
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
        }
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
<a id="insn-00b9eaec"></a> `00b9eaec` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b9eaf0"></a> `00b9eaf0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b9eaf4"></a> `00b9eaf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b9eaf8"></a> `00b9eaf8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b9eafc"></a> `00b9eafc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b9eb00"></a> `00b9eb00` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00b9eb04"></a> `00b9eb04` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b9eb08"></a> `00b9eb08` | `0a 00 09 cb` | sub x10,x0,x9 | `FALL_THROUGH`
<a id="insn-00b9eb0c"></a> `00b9eb0c` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b9eb10"></a> `00b9eb10` | `60 00 00 54` | b.eq 0x00b9eb1c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb14"></a> `00b9eb14` | `2b 60 40 39` | ldrb w11,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b9eb18"></a> `00b9eb18` | `ab 07 00 35` | cbnz w11,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb1c"></a> `00b9eb1c` | `2c 04 40 f9` | ldr x12,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b9eb20"></a> `00b9eb20` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9eb24"></a> `00b9eb24` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00b9eb28"></a> `00b9eb28` | `43 07 00 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eb2c"></a> `00b9eb2c` | `8b 11 00 d1` | sub x11,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00b9eb30"></a> `00b9eb30` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00b9eb34"></a> `00b9eb34` | `e3 06 00 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eb38"></a> `00b9eb38` | `2e 3c 47 29` | ldp w14,w15,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00b9eb3c"></a> `00b9eb3c` | `30 10 40 b9` | ldr w16,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b9eb40"></a> `00b9eb40` | `0d 01 80 b9` | ldrsw x13,[x8] | `FALL_THROUGH`
<a id="insn-00b9eb44"></a> `00b9eb44` | `d1 05 00 11` | add w17,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00b9eb48"></a> `00b9eb48` | `ee 05 00 11` | add w14,w15,#0x1 | `FALL_THROUGH`
<a id="insn-00b9eb4c"></a> `00b9eb4c` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00b9eb50"></a> `00b9eb50` | `31 38 07 29` | stp w17,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00b9eb54"></a> `00b9eb54` | `c8 05 00 54` | b.hi 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb58"></a> `00b9eb58` | `2f 14 40 b9` | ldr w15,[x1, #0x14] | `FALL_THROUGH`
<a id="insn-00b9eb5c"></a> `00b9eb5c` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00b9eb60"></a> `00b9eb60` | `68 05 00 54` | b.hi 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb64"></a> `00b9eb64` | `4d 01 0d cb` | sub x13,x10,x13 | `FALL_THROUGH`
<a id="insn-00b9eb68"></a> `00b9eb68` | `6d 00 00 36` | tbz w13,#0x0,0x00b9eb74 | `CONDITIONAL_JUMP`
<a id="insn-00b9eb6c"></a> `00b9eb6c` | `2e 60 40 39` | ldrb w14,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b9eb70"></a> `00b9eb70` | `ee 04 00 35` | cbnz w14,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb74"></a> `00b9eb74` | `8e 09 00 d1` | sub x14,x12,#0x2 | `FALL_THROUGH`
<a id="insn-00b9eb78"></a> `00b9eb78` | `df 01 0d eb` | cmp x14,x13 | `FALL_THROUGH`
<a id="insn-00b9eb7c"></a> `00b9eb7c` | `83 04 00 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb80"></a> `00b9eb80` | `2e 69 6d 78` | ldrh w14,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b9eb84"></a> `00b9eb84` | `6e 00 00 36` | tbz w14,#0x0,0x00b9eb90 | `CONDITIONAL_JUMP`
<a id="insn-00b9eb88"></a> `00b9eb88` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b9eb8c"></a> `00b9eb8c` | `0f 04 00 35` | cbnz w15,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb90"></a> `00b9eb90` | `ee 03 00 37` | tbnz w14,#0x0,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9eb94"></a> `00b9eb94` | `8e 01 0e eb` | subs x14,x12,x14 | `FALL_THROUGH`
<a id="insn-00b9eb98"></a> `00b9eb98` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9eb9c"></a> `00b9eb9c` | `a9 03 00 54` | b.ls 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eba0"></a> `00b9eba0` | `df 01 0d eb` | cmp x14,x13 | `FALL_THROUGH`
<a id="insn-00b9eba4"></a> `00b9eba4` | `63 03 00 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eba8"></a> `00b9eba8` | `0d 01 80 b9` | ldrsw x13,[x8] | `FALL_THROUGH`
<a id="insn-00b9ebac"></a> `00b9ebac` | `0e 01 0d cb` | sub x14,x8,x13 | `FALL_THROUGH`
<a id="insn-00b9ebb0"></a> `00b9ebb0` | `d0 01 40 79` | ldrh w16,[x14] | `FALL_THROUGH`
<a id="insn-00b9ebb4"></a> `00b9ebb4` | `1f 16 00 71` | cmp w16,#0x5 | `FALL_THROUGH`
<a id="insn-00b9ebb8"></a> `00b9ebb8` | `a3 02 00 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ebbc"></a> `00b9ebbc` | `d1 09 40 79` | ldrh w17,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b9ebc0"></a> `00b9ebc0` | `71 02 00 b4` | cbz x17,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ebc4"></a> `00b9ebc4` | `4f 01 11 8b` | add x15,x10,x17 | `FALL_THROUGH`
<a id="insn-00b9ebc8"></a> `00b9ebc8` | `ff 05 40 f2` | tst x15,#0x3 | `FALL_THROUGH`
<a id="insn-00b9ebcc"></a> `00b9ebcc` | `e0 00 00 54` | b.eq 0x00b9ebe8 | `CONDITIONAL_JUMP`
<a id="insn-00b9ebd0"></a> `00b9ebd0` | `22 60 40 39` | ldrb w2,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b9ebd4"></a> `00b9ebd4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ebd8"></a> `00b9ebd8` | `c2 01 00 35` | cbnz w2,0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ebdc"></a> `00b9ebdc` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00b9ebe0"></a> `00b9ebe0` | `82 00 00 54` | b.cs 0x00b9ebf0 | `CONDITIONAL_JUMP`
<a id="insn-00b9ebe4"></a> `00b9ebe4` | `0b 00 00 14` | b 0x00b9ec10 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9ebe8"></a> `00b9ebe8` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-00b9ebec"></a> `00b9ebec` | `03 01 00 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ebf0"></a> `00b9ebf0` | `20 69 6f b8` | ldr w0,[x9, x15, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b9ebf4"></a> `00b9ebf4` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b9ebf8"></a> `00b9ebf8` | `ab 00 00 54` | b.lt 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ebfc"></a> `00b9ebfc` | `e0 01 00 8b` | add x0,x15,x0 | `FALL_THROUGH`
<a id="insn-00b9ec00"></a> `00b9ec00` | `8f 05 00 d1` | sub x15,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00b9ec04"></a> `00b9ec04` | `ff 01 00 eb` | cmp x15,x0 | `FALL_THROUGH`
<a id="insn-00b9ec08"></a> `00b9ec08` | `e2 00 00 54` | b.cs 0x00b9ec24 | `CONDITIONAL_JUMP`
<a id="insn-00b9ec0c"></a> `00b9ec0c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ec10"></a> `00b9ec10` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b9ec14"></a> `00b9ec14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b9ec18"></a> `00b9ec18` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b9ec1c"></a> `00b9ec1c` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b9ec20"></a> `00b9ec20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b9ec24"></a> `00b9ec24` | `11 01 11 8b` | add x17,x8,x17 | `FALL_THROUGH`
<a id="insn-00b9ec28"></a> `00b9ec28` | `20 02 40 b9` | ldr w0,[x17] | `FALL_THROUGH`
<a id="insn-00b9ec2c"></a> `00b9ec2c` | `22 02 00 ab` | adds x2,x17,x0 | `FALL_THROUGH`
<a id="insn-00b9ec30"></a> `00b9ec30` | `40 01 00 54` | b.eq 0x00b9ec58 | `CONDITIONAL_JUMP`
<a id="insn-00b9ec34"></a> `00b9ec34` | `51 00 09 cb` | sub x17,x2,x9 | `FALL_THROUGH`
<a id="insn-00b9ec38"></a> `00b9ec38` | `3f 06 40 f2` | tst x17,#0x3 | `FALL_THROUGH`
<a id="insn-00b9ec3c"></a> `00b9ec3c` | `c0 02 00 54` | b.eq 0x00b9ec94 | `CONDITIONAL_JUMP`
<a id="insn-00b9ec40"></a> `00b9ec40` | `23 60 40 39` | ldrb w3,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b9ec44"></a> `00b9ec44` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ec48"></a> `00b9ec48` | `43 fe ff 35` | cbnz w3,0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ec4c"></a> `00b9ec4c` | `7f 01 11 eb` | cmp x11,x17 | `FALL_THROUGH`
<a id="insn-00b9ec50"></a> `00b9ec50` | `62 02 00 54` | b.cs 0x00b9ec9c | `CONDITIONAL_JUMP`
<a id="insn-00b9ec54"></a> `00b9ec54` | `ef ff ff 17` | b 0x00b9ec10 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9ec58"></a> `00b9ec58` | `1f 1e 00 71` | cmp w16,#0x7 | `FALL_THROUGH`
<a id="insn-00b9ec5c"></a> `00b9ec5c` | `83 fd ff 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ec60"></a> `00b9ec60` | `e8 07 00 a9` | stp x8,x1,[sp] | `FALL_THROUGH`
<a id="insn-00b9ec64"></a> `00b9ec64` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00b9ec68"></a> `00b9ec68` | `28 fd ff b4` | cbz x8,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ec6c"></a> `00b9ec6c` | `4a 01 08 8b` | add x10,x10,x8 | `FALL_THROUGH`
<a id="insn-00b9ec70"></a> `00b9ec70` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b9ec74"></a> `00b9ec74` | `00 04 00 54` | b.eq 0x00b9ecf4 | `CONDITIONAL_JUMP`
<a id="insn-00b9ec78"></a> `00b9ec78` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ec7c"></a> `00b9ec7c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ec80"></a> `00b9ec80` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9ec84"></a> `00b9ec84` | `6c fc ff 35` | cbnz w12,0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ec88"></a> `00b9ec88` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00b9ec8c"></a> `00b9ec8c` | `82 03 00 54` | b.cs 0x00b9ecfc | `CONDITIONAL_JUMP`
<a id="insn-00b9ec90"></a> `00b9ec90` | `e0 ff ff 17` | b 0x00b9ec10 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9ec94"></a> `00b9ec94` | `7f 01 11 eb` | cmp x11,x17 | `FALL_THROUGH`
<a id="insn-00b9ec98"></a> `00b9ec98` | `a3 fb ff 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ec9c"></a> `00b9ec9c` | `40 00 40 b9` | ldr w0,[x2] | `FALL_THROUGH`
<a id="insn-00b9eca0"></a> `00b9eca0` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00b9eca4"></a> `00b9eca4` | `21 10 40 f9` | ldr x1,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00b9eca8"></a> `00b9eca8` | `3f 00 00 eb` | cmp x1,x0 | `FALL_THROUGH`
<a id="insn-00b9ecac"></a> `00b9ecac` | `09 fb ff 54` | b.ls 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ecb0"></a> `00b9ecb0` | `03 10 00 91` | add x3,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00b9ecb4"></a> `00b9ecb4` | `61 00 11 8b` | add x1,x3,x17 | `FALL_THROUGH`
<a id="insn-00b9ecb8"></a> `00b9ecb8` | `ff 01 01 eb` | cmp x15,x1 | `FALL_THROUGH`
<a id="insn-00b9ecbc"></a> `00b9ecbc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ecc0"></a> `00b9ecc0` | `83 fa ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ecc4"></a> `00b9ecc4` | `9f 01 03 eb` | cmp x12,x3 | `FALL_THROUGH`
<a id="insn-00b9ecc8"></a> `00b9ecc8` | `49 fa ff 54` | b.ls 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eccc"></a> `00b9eccc` | `8c 01 03 cb` | sub x12,x12,x3 | `FALL_THROUGH`
<a id="insn-00b9ecd0"></a> `00b9ecd0` | `9f 01 11 eb` | cmp x12,x17 | `FALL_THROUGH`
<a id="insn-00b9ecd4"></a> `00b9ecd4` | `e3 f9 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ecd8"></a> `00b9ecd8` | `1f 1e 00 71` | cmp w16,#0x7 | `FALL_THROUGH`
<a id="insn-00b9ecdc"></a> `00b9ecdc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ece0"></a> `00b9ece0` | `83 f9 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ece4"></a> `00b9ece4` | `2c 69 61 38` | ldrb w12,[x9, x1, LSL ] | `FALL_THROUGH`
<a id="insn-00b9ece8"></a> `00b9ece8` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00b9ecec"></a> `00b9ecec` | `ac fb ff 34` | cbz w12,0x00b9ec60 | `CONDITIONAL_JUMP`
<a id="insn-00b9ecf0"></a> `00b9ecf0` | `c8 ff ff 17` | b 0x00b9ec10 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9ecf4"></a> `00b9ecf4` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00b9ecf8"></a> `00b9ecf8` | `a3 f8 ff 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ecfc"></a> `00b9ecfc` | `29 69 6a b8` | ldr w9,[x9, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b9ed00"></a> `00b9ed00` | `3f 05 00 71` | cmp w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b9ed04"></a> `00b9ed04` | `4b f8 ff 54` | b.lt 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ed08"></a> `00b9ed08` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-00b9ed0c"></a> `00b9ed0c` | `ff 01 09 eb` | cmp x15,x9 | `FALL_THROUGH`
<a id="insn-00b9ed10"></a> `00b9ed10` | `e3 f7 ff 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ed14"></a> `00b9ed14` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00b9ed18"></a> `00b9ed18` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00b9ed1c"></a> `00b9ed1c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b9ed20"></a> `00b9ed20` | `00 01 09 ab` | adds x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00b9ed24"></a> `00b9ed24` | `00 01 00 54` | b.eq 0x00b9ed44 | `CONDITIONAL_JUMP`
<a id="insn-00b9ed28"></a> `00b9ed28` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ed2c"></a> `00b9ed2c` | `05 f6 02 94` | bl 0x00c5c540 | `UNCONDITIONAL_CALL`
<a id="insn-00b9ed30"></a> `00b9ed30` | `e0 f6 07 36` | tbz w0,#0x0,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ed34"></a> `00b9ed34` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00b9ed38"></a> `00b9ed38` | `08 01 80 b9` | ldrsw x8,[x8] | `FALL_THROUGH`
<a id="insn-00b9ed3c"></a> `00b9ed3c` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00b9ed40"></a> `00b9ed40` | `02 00 00 14` | b 0x00b9ed48 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9ed44"></a> `00b9ed44` | `e8 03 0d cb` | neg x8,x13 | `FALL_THROUGH`
<a id="insn-00b9ed48"></a> `00b9ed48` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00b9ed4c"></a> `00b9ed4c` | `29 01 08 8b` | add x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00b9ed50"></a> `00b9ed50` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00b9ed54"></a> `00b9ed54` | `5f 25 00 71` | cmp w10,#0x9 | `FALL_THROUGH`
<a id="insn-00b9ed58"></a> `00b9ed58` | `43 1b 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9ed5c"></a> `00b9ed5c` | `2b 11 40 79` | ldrh w11,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ed60"></a> `00b9ed60` | `ec 37 40 a9` | ldp x12,x13,[sp] | `FALL_THROUGH`
<a id="insn-00b9ed64"></a> `00b9ed64` | `0b 02 00 b4` | cbz x11,0x00b9eda4 | `CONDITIONAL_JUMP`
<a id="insn-00b9ed68"></a> `00b9ed68` | `ad 01 40 f9` | ldr x13,[x13] | `FALL_THROUGH`
<a id="insn-00b9ed6c"></a> `00b9ed6c` | `8c 01 0d cb` | sub x12,x12,x13 | `FALL_THROUGH`
<a id="insn-00b9ed70"></a> `00b9ed70` | `8b 01 0b 8b` | add x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ed74"></a> `00b9ed74` | `8b 00 00 36` | tbz w11,#0x0,0x00b9ed84 | `CONDITIONAL_JUMP`
<a id="insn-00b9ed78"></a> `00b9ed78` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ed7c"></a> `00b9ed7c` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9ed80"></a> `00b9ed80` | `6c f4 ff 35` | cbnz w12,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ed84"></a> `00b9ed84` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ed88"></a> `00b9ed88` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ed8c"></a> `00b9ed8c` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ed90"></a> `00b9ed90` | `9f 0d 00 f1` | cmp x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b9ed94"></a> `00b9ed94` | `e3 f3 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ed98"></a> `00b9ed98` | `8c 09 00 d1` | sub x12,x12,#0x2 | `FALL_THROUGH`
<a id="insn-00b9ed9c"></a> `00b9ed9c` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9eda0"></a> `00b9eda0` | `83 f3 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eda4"></a> `00b9eda4` | `5f 2d 00 71` | cmp w10,#0xb | `FALL_THROUGH`
<a id="insn-00b9eda8"></a> `00b9eda8` | `c3 18 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9edac"></a> `00b9edac` | `2b 15 40 79` | ldrh w11,[x9, #0xa] | `FALL_THROUGH`
<a id="insn-00b9edb0"></a> `00b9edb0` | `ec 37 40 a9` | ldp x12,x13,[sp] | `FALL_THROUGH`
<a id="insn-00b9edb4"></a> `00b9edb4` | `0b 02 00 b4` | cbz x11,0x00b9edf4 | `CONDITIONAL_JUMP`
<a id="insn-00b9edb8"></a> `00b9edb8` | `ad 01 40 f9` | ldr x13,[x13] | `FALL_THROUGH`
<a id="insn-00b9edbc"></a> `00b9edbc` | `8c 01 0d cb` | sub x12,x12,x13 | `FALL_THROUGH`
<a id="insn-00b9edc0"></a> `00b9edc0` | `8b 01 0b 8b` | add x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9edc4"></a> `00b9edc4` | `8b 00 00 36` | tbz w11,#0x0,0x00b9edd4 | `CONDITIONAL_JUMP`
<a id="insn-00b9edc8"></a> `00b9edc8` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9edcc"></a> `00b9edcc` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9edd0"></a> `00b9edd0` | `ec f1 ff 35` | cbnz w12,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9edd4"></a> `00b9edd4` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9edd8"></a> `00b9edd8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9eddc"></a> `00b9eddc` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ede0"></a> `00b9ede0` | `9f 0d 00 f1` | cmp x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b9ede4"></a> `00b9ede4` | `63 f1 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ede8"></a> `00b9ede8` | `8c 09 00 d1` | sub x12,x12,#0x2 | `FALL_THROUGH`
<a id="insn-00b9edec"></a> `00b9edec` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9edf0"></a> `00b9edf0` | `03 f1 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9edf4"></a> `00b9edf4` | `5f 35 00 71` | cmp w10,#0xd | `FALL_THROUGH`
<a id="insn-00b9edf8"></a> `00b9edf8` | `43 16 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9edfc"></a> `00b9edfc` | `2b 19 40 79` | ldrh w11,[x9, #0xc] | `FALL_THROUGH`
<a id="insn-00b9ee00"></a> `00b9ee00` | `ec 37 40 a9` | ldp x12,x13,[sp] | `FALL_THROUGH`
<a id="insn-00b9ee04"></a> `00b9ee04` | `2b 02 00 b4` | cbz x11,0x00b9ee48 | `CONDITIONAL_JUMP`
<a id="insn-00b9ee08"></a> `00b9ee08` | `ad 01 40 f9` | ldr x13,[x13] | `FALL_THROUGH`
<a id="insn-00b9ee0c"></a> `00b9ee0c` | `8c 01 0d cb` | sub x12,x12,x13 | `FALL_THROUGH`
<a id="insn-00b9ee10"></a> `00b9ee10` | `8b 01 0b 8b` | add x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ee14"></a> `00b9ee14` | `7f 09 40 f2` | tst x11,#0x7 | `FALL_THROUGH`
<a id="insn-00b9ee18"></a> `00b9ee18` | `80 00 00 54` | b.eq 0x00b9ee28 | `CONDITIONAL_JUMP`
<a id="insn-00b9ee1c"></a> `00b9ee1c` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ee20"></a> `00b9ee20` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9ee24"></a> `00b9ee24` | `4c ef ff 35` | cbnz w12,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ee28"></a> `00b9ee28` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ee2c"></a> `00b9ee2c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ee30"></a> `00b9ee30` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ee34"></a> `00b9ee34` | `9f 25 00 f1` | cmp x12,#0x9 | `FALL_THROUGH`
<a id="insn-00b9ee38"></a> `00b9ee38` | `c3 ee ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ee3c"></a> `00b9ee3c` | `8c 21 00 d1` | sub x12,x12,#0x8 | `FALL_THROUGH`
<a id="insn-00b9ee40"></a> `00b9ee40` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ee44"></a> `00b9ee44` | `63 ee ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ee48"></a> `00b9ee48` | `5f 3d 00 71` | cmp w10,#0xf | `FALL_THROUGH`
<a id="insn-00b9ee4c"></a> `00b9ee4c` | `a3 13 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9ee50"></a> `00b9ee50` | `2b 1d 40 79` | ldrh w11,[x9, #0xe] | `FALL_THROUGH`
<a id="insn-00b9ee54"></a> `00b9ee54` | `ec 37 40 a9` | ldp x12,x13,[sp] | `FALL_THROUGH`
<a id="insn-00b9ee58"></a> `00b9ee58` | `2b 02 00 b4` | cbz x11,0x00b9ee9c | `CONDITIONAL_JUMP`
<a id="insn-00b9ee5c"></a> `00b9ee5c` | `ad 01 40 f9` | ldr x13,[x13] | `FALL_THROUGH`
<a id="insn-00b9ee60"></a> `00b9ee60` | `8c 01 0d cb` | sub x12,x12,x13 | `FALL_THROUGH`
<a id="insn-00b9ee64"></a> `00b9ee64` | `8b 01 0b 8b` | add x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ee68"></a> `00b9ee68` | `7f 09 40 f2` | tst x11,#0x7 | `FALL_THROUGH`
<a id="insn-00b9ee6c"></a> `00b9ee6c` | `80 00 00 54` | b.eq 0x00b9ee7c | `CONDITIONAL_JUMP`
<a id="insn-00b9ee70"></a> `00b9ee70` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ee74"></a> `00b9ee74` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9ee78"></a> `00b9ee78` | `ac ec ff 35` | cbnz w12,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ee7c"></a> `00b9ee7c` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ee80"></a> `00b9ee80` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ee84"></a> `00b9ee84` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ee88"></a> `00b9ee88` | `9f 25 00 f1` | cmp x12,#0x9 | `FALL_THROUGH`
<a id="insn-00b9ee8c"></a> `00b9ee8c` | `23 ec ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ee90"></a> `00b9ee90` | `8c 21 00 d1` | sub x12,x12,#0x8 | `FALL_THROUGH`
<a id="insn-00b9ee94"></a> `00b9ee94` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ee98"></a> `00b9ee98` | `c3 eb ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ee9c"></a> `00b9ee9c` | `5f 45 00 71` | cmp w10,#0x11 | `FALL_THROUGH`
<a id="insn-00b9eea0"></a> `00b9eea0` | `03 11 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9eea4"></a> `00b9eea4` | `2b 21 40 79` | ldrh w11,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b9eea8"></a> `00b9eea8` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9eeac"></a> `00b9eeac` | `ab 01 00 b4` | cbz x11,0x00b9eee0 | `CONDITIONAL_JUMP`
<a id="insn-00b9eeb0"></a> `00b9eeb0` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9eeb4"></a> `00b9eeb4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9eeb8"></a> `00b9eeb8` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00b9eebc"></a> `00b9eebc` | `a3 ea ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eec0"></a> `00b9eec0` | `ed 07 40 f9` | ldr x13,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9eec4"></a> `00b9eec4` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00b9eec8"></a> `00b9eec8` | `ae 01 40 f9` | ldr x14,[x13] | `FALL_THROUGH`
<a id="insn-00b9eecc"></a> `00b9eecc` | `ed 03 40 f9` | ldr x13,[sp] | `FALL_THROUGH`
<a id="insn-00b9eed0"></a> `00b9eed0` | `6b 01 0d 8b` | add x11,x11,x13 | `FALL_THROUGH`
<a id="insn-00b9eed4"></a> `00b9eed4` | `6b 01 0e cb` | sub x11,x11,x14 | `FALL_THROUGH`
<a id="insn-00b9eed8"></a> `00b9eed8` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9eedc"></a> `00b9eedc` | `a3 e9 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9eee0"></a> `00b9eee0` | `5f 4d 00 71` | cmp w10,#0x13 | `FALL_THROUGH`
<a id="insn-00b9eee4"></a> `00b9eee4` | `e3 0e 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9eee8"></a> `00b9eee8` | `2b 25 40 79` | ldrh w11,[x9, #0x12] | `FALL_THROUGH`
<a id="insn-00b9eeec"></a> `00b9eeec` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9eef0"></a> `00b9eef0` | `ab 01 00 b4` | cbz x11,0x00b9ef24 | `CONDITIONAL_JUMP`
<a id="insn-00b9eef4"></a> `00b9eef4` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9eef8"></a> `00b9eef8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9eefc"></a> `00b9eefc` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00b9ef00"></a> `00b9ef00` | `83 e8 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef04"></a> `00b9ef04` | `ed 07 40 f9` | ldr x13,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ef08"></a> `00b9ef08` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00b9ef0c"></a> `00b9ef0c` | `ae 01 40 f9` | ldr x14,[x13] | `FALL_THROUGH`
<a id="insn-00b9ef10"></a> `00b9ef10` | `ed 03 40 f9` | ldr x13,[sp] | `FALL_THROUGH`
<a id="insn-00b9ef14"></a> `00b9ef14` | `6b 01 0d 8b` | add x11,x11,x13 | `FALL_THROUGH`
<a id="insn-00b9ef18"></a> `00b9ef18` | `6b 01 0e cb` | sub x11,x11,x14 | `FALL_THROUGH`
<a id="insn-00b9ef1c"></a> `00b9ef1c` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ef20"></a> `00b9ef20` | `83 e7 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef24"></a> `00b9ef24` | `5f 55 00 71` | cmp w10,#0x15 | `FALL_THROUGH`
<a id="insn-00b9ef28"></a> `00b9ef28` | `c3 0c 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef2c"></a> `00b9ef2c` | `2b 29 40 79` | ldrh w11,[x9, #0x14] | `FALL_THROUGH`
<a id="insn-00b9ef30"></a> `00b9ef30` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ef34"></a> `00b9ef34` | `ab 01 00 b4` | cbz x11,0x00b9ef68 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef38"></a> `00b9ef38` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ef3c"></a> `00b9ef3c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9ef40"></a> `00b9ef40` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00b9ef44"></a> `00b9ef44` | `63 e6 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef48"></a> `00b9ef48` | `ed 07 40 f9` | ldr x13,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ef4c"></a> `00b9ef4c` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00b9ef50"></a> `00b9ef50` | `ae 01 40 f9` | ldr x14,[x13] | `FALL_THROUGH`
<a id="insn-00b9ef54"></a> `00b9ef54` | `ed 03 40 f9` | ldr x13,[sp] | `FALL_THROUGH`
<a id="insn-00b9ef58"></a> `00b9ef58` | `6b 01 0d 8b` | add x11,x11,x13 | `FALL_THROUGH`
<a id="insn-00b9ef5c"></a> `00b9ef5c` | `6b 01 0e cb` | sub x11,x11,x14 | `FALL_THROUGH`
<a id="insn-00b9ef60"></a> `00b9ef60` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ef64"></a> `00b9ef64` | `63 e5 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef68"></a> `00b9ef68` | `5f 5d 00 71` | cmp w10,#0x17 | `FALL_THROUGH`
<a id="insn-00b9ef6c"></a> `00b9ef6c` | `a3 0a 00 54` | b.cc 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef70"></a> `00b9ef70` | `2a 2d 40 79` | ldrh w10,[x9, #0x16] | `FALL_THROUGH`
<a id="insn-00b9ef74"></a> `00b9ef74` | `2a 03 00 b4` | cbz x10,0x00b9efd8 | `CONDITIONAL_JUMP`
<a id="insn-00b9ef78"></a> `00b9ef78` | `ec 2f 40 a9` | ldp x12,x11,[sp] | `FALL_THROUGH`
<a id="insn-00b9ef7c"></a> `00b9ef7c` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-00b9ef80"></a> `00b9ef80` | `8c 01 0b cb` | sub x12,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9ef84"></a> `00b9ef84` | `8a 01 0a 8b` | add x10,x12,x10 | `FALL_THROUGH`
<a id="insn-00b9ef88"></a> `00b9ef88` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b9ef8c"></a> `00b9ef8c` | `80 00 00 54` | b.eq 0x00b9ef9c | `CONDITIONAL_JUMP`
<a id="insn-00b9ef90"></a> `00b9ef90` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9ef94"></a> `00b9ef94` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9ef98"></a> `00b9ef98` | `ac e3 ff 35` | cbnz w12,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9ef9c"></a> `00b9ef9c` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9efa0"></a> `00b9efa0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9efa4"></a> `00b9efa4` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9efa8"></a> `00b9efa8` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00b9efac"></a> `00b9efac` | `23 e3 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9efb0"></a> `00b9efb0` | `8d 11 00 d1` | sub x13,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00b9efb4"></a> `00b9efb4` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00b9efb8"></a> `00b9efb8` | `c3 e2 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9efbc"></a> `00b9efbc` | `6b 69 6a b8` | ldr w11,[x11, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b9efc0"></a> `00b9efc0` | `7f 05 00 71` | cmp w11,#0x1 | `FALL_THROUGH`
<a id="insn-00b9efc4"></a> `00b9efc4` | `4b e2 ff 54` | b.lt 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9efc8"></a> `00b9efc8` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b9efcc"></a> `00b9efcc` | `8b 05 00 d1` | sub x11,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00b9efd0"></a> `00b9efd0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00b9efd4"></a> `00b9efd4` | `c3 e1 ff 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9efd8"></a> `00b9efd8` | `29 2d 40 79` | ldrh w9,[x9, #0x16] | `FALL_THROUGH`
<a id="insn-00b9efdc"></a> `00b9efdc` | `29 07 00 b4` | cbz x9,0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9efe0"></a> `00b9efe0` | `ea 03 40 f9` | ldr x10,[sp] | `FALL_THROUGH`
<a id="insn-00b9efe4"></a> `00b9efe4` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-00b9efe8"></a> `00b9efe8` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00b9efec"></a> `00b9efec` | `2b 01 0a ab` | adds x11,x9,x10 | `FALL_THROUGH`
<a id="insn-00b9eff0"></a> `00b9eff0` | `ea 07 40 f9` | ldr x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9eff4"></a> `00b9eff4` | `80 03 00 54` | b.eq 0x00b9f064 | `CONDITIONAL_JUMP`
<a id="insn-00b9eff8"></a> `00b9eff8` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00b9effc"></a> `00b9effc` | `6a 01 0a cb` | sub x10,x11,x10 | `FALL_THROUGH`
<a id="insn-00b9f000"></a> `00b9f000` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b9f004"></a> `00b9f004` | `80 00 00 54` | b.eq 0x00b9f014 | `CONDITIONAL_JUMP`
<a id="insn-00b9f008"></a> `00b9f008` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f00c"></a> `00b9f00c` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9f010"></a> `00b9f010` | `ec df ff 35` | cbnz w12,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f014"></a> `00b9f014` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f018"></a> `00b9f018` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f01c"></a> `00b9f01c` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f020"></a> `00b9f020` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00b9f024"></a> `00b9f024` | `63 df ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f028"></a> `00b9f028` | `8d 11 00 d1` | sub x13,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f02c"></a> `00b9f02c` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00b9f030"></a> `00b9f030` | `ed 07 40 f9` | ldr x13,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f034"></a> `00b9f034` | `e3 de ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f038"></a> `00b9f038` | `6b 01 40 b9` | ldr w11,[x11] | `FALL_THROUGH`
<a id="insn-00b9f03c"></a> `00b9f03c` | `ad 11 40 f9` | ldr x13,[x13, #0x20] | `FALL_THROUGH`
<a id="insn-00b9f040"></a> `00b9f040` | `7f 09 4d eb` | cmp x11,x13, LSR #0x2 | `FALL_THROUGH`
<a id="insn-00b9f044"></a> `00b9f044` | `42 de ff 54` | b.cs 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f048"></a> `00b9f048` | `6b f5 7e d3` | lsl x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b9f04c"></a> `00b9f04c` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f050"></a> `00b9f050` | `8b 01 0b eb` | subs x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9f054"></a> `00b9f054` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f058"></a> `00b9f058` | `c9 dd ff 54` | b.ls 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f05c"></a> `00b9f05c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00b9f060"></a> `00b9f060` | `83 dd ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f064"></a> `00b9f064` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00b9f068"></a> `00b9f068` | `33 01 0a ab` | adds x19,x9,x10 | `FALL_THROUGH`
<a id="insn-00b9f06c"></a> `00b9f06c` | `a0 02 00 54` | b.eq 0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9f070"></a> `00b9f070` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-00b9f074"></a> `00b9f074` | `69 02 00 34` | cbz w9,0x00b9f0c0 | `CONDITIONAL_JUMP`
<a id="insn-00b9f078"></a> `00b9f078` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00b9f07c"></a> `00b9f07c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00b9f080"></a> `00b9f080` | `76 12 00 91` | add x22,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f084"></a> `00b9f084` | `88 76 7e 92` | and x8,x20,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00b9f088"></a> `00b9f088` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00b9f08c"></a> `00b9f08c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b9f090"></a> `00b9f090` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f094"></a> `00b9f094` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00b9f098"></a> `00b9f098` | `46 f5 02 94` | bl 0x00c5c5b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b9f09c"></a> `00b9f09c` | `80 db 07 36` | tbz w0,#0x0,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f0a0"></a> `00b9f0a0` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00b9f0a4"></a> `00b9f0a4` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f0a8"></a> `00b9f0a8` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f0ac"></a> `00b9f0ac` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00b9f0b0"></a> `00b9f0b0` | `a3 fe ff 54` | b.cc 0x00b9f084 | `CONDITIONAL_JUMP`
<a id="insn-00b9f0b4"></a> `00b9f0b4` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00b9f0b8"></a> `00b9f0b8` | `08 01 80 b9` | ldrsw x8,[x8] | `FALL_THROUGH`
<a id="insn-00b9f0bc"></a> `00b9f0bc` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00b9f0c0"></a> `00b9f0c0` | `e9 2b 40 a9` | ldp x9,x10,[sp] | `FALL_THROUGH`
<a id="insn-00b9f0c4"></a> `00b9f0c4` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00b9f0c8"></a> `00b9f0c8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b9f0cc"></a> `00b9f0cc` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00b9f0d0"></a> `00b9f0d0` | `03 14 00 54` | b.cc 0x00b9f350 | `CONDITIONAL_JUMP`
<a id="insn-00b9f0d4"></a> `00b9f0d4` | `0a 31 40 79` | ldrh w10,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b9f0d8"></a> `00b9f0d8` | `2a 03 00 b4` | cbz x10,0x00b9f13c | `CONDITIONAL_JUMP`
<a id="insn-00b9f0dc"></a> `00b9f0dc` | `ec 2f 40 a9` | ldp x12,x11,[sp] | `FALL_THROUGH`
<a id="insn-00b9f0e0"></a> `00b9f0e0` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-00b9f0e4"></a> `00b9f0e4` | `8c 01 0b cb` | sub x12,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9f0e8"></a> `00b9f0e8` | `8a 01 0a 8b` | add x10,x12,x10 | `FALL_THROUGH`
<a id="insn-00b9f0ec"></a> `00b9f0ec` | `5f 05 40 f2` | tst x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b9f0f0"></a> `00b9f0f0` | `80 00 00 54` | b.eq 0x00b9f100 | `CONDITIONAL_JUMP`
<a id="insn-00b9f0f4"></a> `00b9f0f4` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f0f8"></a> `00b9f0f8` | `8c 61 40 39` | ldrb w12,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00b9f0fc"></a> `00b9f0fc` | `8c d8 ff 35` | cbnz w12,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f100"></a> `00b9f100` | `ec 07 40 f9` | ldr x12,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f104"></a> `00b9f104` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f108"></a> `00b9f108` | `8c 05 40 f9` | ldr x12,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f10c"></a> `00b9f10c` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00b9f110"></a> `00b9f110` | `03 d8 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f114"></a> `00b9f114` | `8d 11 00 d1` | sub x13,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f118"></a> `00b9f118` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00b9f11c"></a> `00b9f11c` | `a3 d7 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f120"></a> `00b9f120` | `6b 69 6a b8` | ldr w11,[x11, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b9f124"></a> `00b9f124` | `7f 05 00 71` | cmp w11,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f128"></a> `00b9f128` | `2b d7 ff 54` | b.lt 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f12c"></a> `00b9f12c` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b9f130"></a> `00b9f130` | `8b 05 00 d1` | sub x11,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f134"></a> `00b9f134` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00b9f138"></a> `00b9f138` | `a3 d6 ff 54` | b.cc 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f13c"></a> `00b9f13c` | `0a 31 40 79` | ldrh w10,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b9f140"></a> `00b9f140` | `2a 0a 00 b4` | cbz x10,0x00b9f284 | `CONDITIONAL_JUMP`
<a id="insn-00b9f144"></a> `00b9f144` | `eb 03 40 f9` | ldr x11,[sp] | `FALL_THROUGH`
<a id="insn-00b9f148"></a> `00b9f148` | `6a 01 0a 8b` | add x10,x11,x10 | `FALL_THROUGH`
<a id="insn-00b9f14c"></a> `00b9f14c` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00b9f150"></a> `00b9f150` | `4c 01 0b ab` | adds x12,x10,x11 | `FALL_THROUGH`
<a id="insn-00b9f154"></a> `00b9f154` | `eb 07 40 f9` | ldr x11,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f158"></a> `00b9f158` | `80 03 00 54` | b.eq 0x00b9f1c8 | `CONDITIONAL_JUMP`
<a id="insn-00b9f15c"></a> `00b9f15c` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-00b9f160"></a> `00b9f160` | `8b 01 0b cb` | sub x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9f164"></a> `00b9f164` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00b9f168"></a> `00b9f168` | `80 00 00 54` | b.eq 0x00b9f178 | `CONDITIONAL_JUMP`
<a id="insn-00b9f16c"></a> `00b9f16c` | `ed 07 40 f9` | ldr x13,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f170"></a> `00b9f170` | `ad 61 40 39` | ldrb w13,[x13, #0x18] | `FALL_THROUGH`
<a id="insn-00b9f174"></a> `00b9f174` | `cd d4 ff 35` | cbnz w13,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f178"></a> `00b9f178` | `ed 07 40 f9` | ldr x13,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f17c"></a> `00b9f17c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f180"></a> `00b9f180` | `ad 05 40 f9` | ldr x13,[x13, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f184"></a> `00b9f184` | `bf 15 00 f1` | cmp x13,#0x5 | `FALL_THROUGH`
<a id="insn-00b9f188"></a> `00b9f188` | `43 d4 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f18c"></a> `00b9f18c` | `ae 11 00 d1` | sub x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f190"></a> `00b9f190` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00b9f194"></a> `00b9f194` | `ee 07 40 f9` | ldr x14,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f198"></a> `00b9f198` | `c3 d3 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f19c"></a> `00b9f19c` | `8c 01 40 b9` | ldr w12,[x12] | `FALL_THROUGH`
<a id="insn-00b9f1a0"></a> `00b9f1a0` | `ce 11 40 f9` | ldr x14,[x14, #0x20] | `FALL_THROUGH`
<a id="insn-00b9f1a4"></a> `00b9f1a4` | `9f 09 4e eb` | cmp x12,x14, LSR #0x2 | `FALL_THROUGH`
<a id="insn-00b9f1a8"></a> `00b9f1a8` | `22 d3 ff 54` | b.cs 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f1ac"></a> `00b9f1ac` | `8c f5 7e d3` | lsl x12,x12,#0x2 | `FALL_THROUGH`
<a id="insn-00b9f1b0"></a> `00b9f1b0` | `8c 11 00 91` | add x12,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f1b4"></a> `00b9f1b4` | `ac 01 0c eb` | subs x12,x13,x12 | `FALL_THROUGH`
<a id="insn-00b9f1b8"></a> `00b9f1b8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f1bc"></a> `00b9f1bc` | `a9 d2 ff 54` | b.ls 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f1c0"></a> `00b9f1c0` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b9f1c4"></a> `00b9f1c4` | `63 d2 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f1c8"></a> `00b9f1c8` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00b9f1cc"></a> `00b9f1cc` | `4a 01 0b ab` | adds x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b9f1d0"></a> `00b9f1d0` | `a0 05 00 54` | b.eq 0x00b9f284 | `CONDITIONAL_JUMP`
<a id="insn-00b9f1d4"></a> `00b9f1d4` | `40 45 40 b8` | ldr w0,[x10], #0x4 | `FALL_THROUGH`
<a id="insn-00b9f1d8"></a> `00b9f1d8` | `60 05 00 34` | cbz w0,0x00b9f284 | `CONDITIONAL_JUMP`
<a id="insn-00b9f1dc"></a> `00b9f1dc` | `ef 07 40 f9` | ldr x15,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f1e0"></a> `00b9f1e0` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00b9f1e4"></a> `00b9f1e4` | `01 f4 7e d3` | lsl x1,x0,#0x2 | `FALL_THROUGH`
<a id="insn-00b9f1e8"></a> `00b9f1e8` | `ed 31 40 a9` | ldp x13,x12,[x15] | `FALL_THROUGH`
<a id="insn-00b9f1ec"></a> `00b9f1ec` | `ee 61 40 39` | ldrb w14,[x15, #0x18] | `FALL_THROUGH`
<a id="insn-00b9f1f0"></a> `00b9f1f0` | `ef 11 40 f9` | ldr x15,[x15, #0x20] | `FALL_THROUGH`
<a id="insn-00b9f1f4"></a> `00b9f1f4` | `90 11 00 d1` | sub x16,x12,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f1f8"></a> `00b9f1f8` | `91 05 00 d1` | sub x17,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f1fc"></a> `00b9f1fc` | `60 75 7e 92` | and x0,x11,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00b9f200"></a> `00b9f200` | `40 01 00 8b` | add x0,x10,x0 | `FALL_THROUGH`
<a id="insn-00b9f204"></a> `00b9f204` | `02 00 40 b9` | ldr w2,[x0] | `FALL_THROUGH`
<a id="insn-00b9f208"></a> `00b9f208` | `df 01 00 71` | cmp w14,#0x0 | `FALL_THROUGH`
<a id="insn-00b9f20c"></a> `00b9f20c` | `e4 07 9f 1a` | cset w4,ne | `FALL_THROUGH`
<a id="insn-00b9f210"></a> `00b9f210` | `03 00 02 8b` | add x3,x0,x2 | `FALL_THROUGH`
<a id="insn-00b9f214"></a> `00b9f214` | `62 00 0d cb` | sub x2,x3,x13 | `FALL_THROUGH`
<a id="insn-00b9f218"></a> `00b9f218` | `5f 04 40 f2` | tst x2,#0x3 | `FALL_THROUGH`
<a id="insn-00b9f21c"></a> `00b9f21c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00b9f220"></a> `00b9f220` | `84 00 00 0a` | and w4,w4,w0 | `FALL_THROUGH`
<a id="insn-00b9f224"></a> `00b9f224` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f228"></a> `00b9f228` | `44 cf 07 37` | tbnz w4,#0x0,0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f22c"></a> `00b9f22c` | `9f 15 00 f1` | cmp x12,#0x5 | `FALL_THROUGH`
<a id="insn-00b9f230"></a> `00b9f230` | `03 cf ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f234"></a> `00b9f234` | `1f 02 02 eb` | cmp x16,x2 | `FALL_THROUGH`
<a id="insn-00b9f238"></a> `00b9f238` | `c3 ce ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f23c"></a> `00b9f23c` | `60 00 40 b9` | ldr w0,[x3] | `FALL_THROUGH`
<a id="insn-00b9f240"></a> `00b9f240` | `ff 01 00 eb` | cmp x15,x0 | `FALL_THROUGH`
<a id="insn-00b9f244"></a> `00b9f244` | `49 ce ff 54` | b.ls 0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f248"></a> `00b9f248` | `04 10 00 91` | add x4,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f24c"></a> `00b9f24c` | `83 00 02 8b` | add x3,x4,x2 | `FALL_THROUGH`
<a id="insn-00b9f250"></a> `00b9f250` | `3f 02 03 eb` | cmp x17,x3 | `FALL_THROUGH`
<a id="insn-00b9f254"></a> `00b9f254` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f258"></a> `00b9f258` | `c3 cd ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f25c"></a> `00b9f25c` | `9f 01 04 eb` | cmp x12,x4 | `FALL_THROUGH`
<a id="insn-00b9f260"></a> `00b9f260` | `89 cd ff 54` | b.ls 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f264"></a> `00b9f264` | `84 01 04 cb` | sub x4,x12,x4 | `FALL_THROUGH`
<a id="insn-00b9f268"></a> `00b9f268` | `9f 00 02 eb` | cmp x4,x2 | `FALL_THROUGH`
<a id="insn-00b9f26c"></a> `00b9f26c` | `23 cd ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f270"></a> `00b9f270` | `a0 69 63 38` | ldrb w0,[x13, x3, LSL ] | `FALL_THROUGH`
<a id="insn-00b9f274"></a> `00b9f274` | `c0 cc ff 35` | cbnz w0,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f278"></a> `00b9f278` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00b9f27c"></a> `00b9f27c` | `3f 00 0b eb` | cmp x1,x11 | `FALL_THROUGH`
<a id="insn-00b9f280"></a> `00b9f280` | `e1 fb ff 54` | b.ne 0x00b9f1fc | `CONDITIONAL_JUMP`
<a id="insn-00b9f284"></a> `00b9f284` | `eb 2b 40 a9` | ldp x11,x10,[sp] | `FALL_THROUGH`
<a id="insn-00b9f288"></a> `00b9f288` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00b9f28c"></a> `00b9f28c` | `23 06 00 54` | b.cc 0x00b9f350 | `CONDITIONAL_JUMP`
<a id="insn-00b9f290"></a> `00b9f290` | `0c 35 40 79` | ldrh w12,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00b9f294"></a> `00b9f294` | `8c 01 00 b4` | cbz x12,0x00b9f2c4 | `CONDITIONAL_JUMP`
<a id="insn-00b9f298"></a> `00b9f298` | `4d 05 40 f9` | ldr x13,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f29c"></a> `00b9f29c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f2a0"></a> `00b9f2a0` | `bf 09 00 f1` | cmp x13,#0x2 | `FALL_THROUGH`
<a id="insn-00b9f2a4"></a> `00b9f2a4` | `63 cb ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f2a8"></a> `00b9f2a8` | `eb 2b 40 a9` | ldp x11,x10,[sp] | `FALL_THROUGH`
<a id="insn-00b9f2ac"></a> `00b9f2ac` | `ad 05 00 d1` | sub x13,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f2b0"></a> `00b9f2b0` | `4e 01 40 f9` | ldr x14,[x10] | `FALL_THROUGH`
<a id="insn-00b9f2b4"></a> `00b9f2b4` | `8c 01 0b 8b` | add x12,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9f2b8"></a> `00b9f2b8` | `8c 01 0e cb` | sub x12,x12,x14 | `FALL_THROUGH`
<a id="insn-00b9f2bc"></a> `00b9f2bc` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b9f2c0"></a> `00b9f2c0` | `83 ca ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f2c4"></a> `00b9f2c4` | `3f 75 00 71` | cmp w9,#0x1d | `FALL_THROUGH`
<a id="insn-00b9f2c8"></a> `00b9f2c8` | `43 04 00 54` | b.cc 0x00b9f350 | `CONDITIONAL_JUMP`
<a id="insn-00b9f2cc"></a> `00b9f2cc` | `0c 39 40 79` | ldrh w12,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00b9f2d0"></a> `00b9f2d0` | `2c 02 00 b4` | cbz x12,0x00b9f314 | `CONDITIONAL_JUMP`
<a id="insn-00b9f2d4"></a> `00b9f2d4` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00b9f2d8"></a> `00b9f2d8` | `6a 01 0a cb` | sub x10,x11,x10 | `FALL_THROUGH`
<a id="insn-00b9f2dc"></a> `00b9f2dc` | `4a 01 0c 8b` | add x10,x10,x12 | `FALL_THROUGH`
<a id="insn-00b9f2e0"></a> `00b9f2e0` | `8a 00 00 36` | tbz w10,#0x0,0x00b9f2f0 | `CONDITIONAL_JUMP`
<a id="insn-00b9f2e4"></a> `00b9f2e4` | `eb 07 40 f9` | ldr x11,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f2e8"></a> `00b9f2e8` | `6b 61 40 39` | ldrb w11,[x11, #0x18] | `FALL_THROUGH`
<a id="insn-00b9f2ec"></a> `00b9f2ec` | `0b c9 ff 35` | cbnz w11,0x00b9ec0c | `CONDITIONAL_JUMP`
<a id="insn-00b9f2f0"></a> `00b9f2f0` | `eb 07 40 f9` | ldr x11,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f2f4"></a> `00b9f2f4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f2f8"></a> `00b9f2f8` | `6b 05 40 f9` | ldr x11,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f2fc"></a> `00b9f2fc` | `7f 0d 00 f1` | cmp x11,#0x3 | `FALL_THROUGH`
<a id="insn-00b9f300"></a> `00b9f300` | `83 c8 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f304"></a> `00b9f304` | `6b 09 00 d1` | sub x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b9f308"></a> `00b9f308` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00b9f30c"></a> `00b9f30c` | `ea 07 40 f9` | ldr x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f310"></a> `00b9f310` | `03 c8 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f314"></a> `00b9f314` | `3f 7d 00 71` | cmp w9,#0x1f | `FALL_THROUGH`
<a id="insn-00b9f318"></a> `00b9f318` | `c3 01 00 54` | b.cc 0x00b9f350 | `CONDITIONAL_JUMP`
<a id="insn-00b9f31c"></a> `00b9f31c` | `08 3d 40 79` | ldrh w8,[x8, #0x1e] | `FALL_THROUGH`
<a id="insn-00b9f320"></a> `00b9f320` | `88 01 00 b4` | cbz x8,0x00b9f350 | `CONDITIONAL_JUMP`
<a id="insn-00b9f324"></a> `00b9f324` | `49 05 40 f9` | ldr x9,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00b9f328"></a> `00b9f328` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b9f32c"></a> `00b9f32c` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00b9f330"></a> `00b9f330` | `03 c7 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f334"></a> `00b9f334` | `eb 2b 40 a9` | ldp x11,x10,[sp] | `FALL_THROUGH`
<a id="insn-00b9f338"></a> `00b9f338` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f33c"></a> `00b9f33c` | `4c 01 40 f9` | ldr x12,[x10] | `FALL_THROUGH`
<a id="insn-00b9f340"></a> `00b9f340` | `08 01 0b 8b` | add x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00b9f344"></a> `00b9f344` | `08 01 0c cb` | sub x8,x8,x12 | `FALL_THROUGH`
<a id="insn-00b9f348"></a> `00b9f348` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00b9f34c"></a> `00b9f34c` | `23 c6 ff 54` | b.cc 0x00b9ec10 | `CONDITIONAL_JUMP`
<a id="insn-00b9f350"></a> `00b9f350` | `48 39 40 b9` | ldr w8,[x10, #0x38] | `FALL_THROUGH`
<a id="insn-00b9f354"></a> `00b9f354` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f358"></a> `00b9f358` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b9f35c"></a> `00b9f35c` | `48 39 00 b9` | str w8,[x10, #0x38] | `FALL_THROUGH`
<a id="insn-00b9f360"></a> `00b9f360` | `2c fe ff 17` | b 0x00b9ec10 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b9eaec`](#insn-00b9eaec) 範囲 `[['00b9eaec', '00b9eaf3']]`
  - `FALL_THROUGH` [`00b9eaf0`](#insn-00b9eaf0) → [`00b9eaf4`](#insn-00b9eaf4)
- ブロック [`00b9eaf4`](#insn-00b9eaf4) 範囲 `[['00b9eaf4', '00b9eaf7']]`
  - `FALL_THROUGH` [`00b9eaf4`](#insn-00b9eaf4) → [`00b9eaf8`](#insn-00b9eaf8)
- ブロック [`00b9eaf8`](#insn-00b9eaf8) 範囲 `[['00b9eaf8', '00b9eafb']]`
  - `FALL_THROUGH` [`00b9eaf8`](#insn-00b9eaf8) → [`00b9eafc`](#insn-00b9eafc)
- ブロック [`00b9eafc`](#insn-00b9eafc) 範囲 `[['00b9eafc', '00b9eb13']]`
  - `CONDITIONAL_JUMP` [`00b9eb10`](#insn-00b9eb10) → [`00b9eb1c`](#insn-00b9eb1c)
  - `FALL_THROUGH` [`00b9eb10`](#insn-00b9eb10) → [`00b9eb14`](#insn-00b9eb14)
- ブロック [`00b9eb14`](#insn-00b9eb14) 範囲 `[['00b9eb14', '00b9eb1b']]`
  - `CONDITIONAL_JUMP` [`00b9eb18`](#insn-00b9eb18) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9eb18`](#insn-00b9eb18) → [`00b9eb1c`](#insn-00b9eb1c)
- ブロック [`00b9eb1c`](#insn-00b9eb1c) 範囲 `[['00b9eb1c', '00b9eb2b']]`
  - `CONDITIONAL_JUMP` [`00b9eb28`](#insn-00b9eb28) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9eb28`](#insn-00b9eb28) → [`00b9eb2c`](#insn-00b9eb2c)
- ブロック [`00b9eb2c`](#insn-00b9eb2c) 範囲 `[['00b9eb2c', '00b9eb37']]`
  - `CONDITIONAL_JUMP` [`00b9eb34`](#insn-00b9eb34) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9eb34`](#insn-00b9eb34) → [`00b9eb38`](#insn-00b9eb38)
- ブロック [`00b9eb38`](#insn-00b9eb38) 範囲 `[['00b9eb38', '00b9eb43']]`
  - `FALL_THROUGH` [`00b9eb40`](#insn-00b9eb40) → [`00b9eb44`](#insn-00b9eb44)
- ブロック [`00b9eb44`](#insn-00b9eb44) 範囲 `[['00b9eb44', '00b9eb47']]`
  - `FALL_THROUGH` [`00b9eb44`](#insn-00b9eb44) → [`00b9eb48`](#insn-00b9eb48)
- ブロック [`00b9eb48`](#insn-00b9eb48) 範囲 `[['00b9eb48', '00b9eb57']]`
  - `CONDITIONAL_JUMP` [`00b9eb54`](#insn-00b9eb54) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9eb54`](#insn-00b9eb54) → [`00b9eb58`](#insn-00b9eb58)
- ブロック [`00b9eb58`](#insn-00b9eb58) 範囲 `[['00b9eb58', '00b9eb5f']]`
  - `FALL_THROUGH` [`00b9eb5c`](#insn-00b9eb5c) → [`00b9eb60`](#insn-00b9eb60)
- ブロック [`00b9eb60`](#insn-00b9eb60) 範囲 `[['00b9eb60', '00b9eb63']]`
  - `CONDITIONAL_JUMP` [`00b9eb60`](#insn-00b9eb60) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9eb60`](#insn-00b9eb60) → [`00b9eb64`](#insn-00b9eb64)
- ブロック [`00b9eb64`](#insn-00b9eb64) 範囲 `[['00b9eb64', '00b9eb67']]`
  - `FALL_THROUGH` [`00b9eb64`](#insn-00b9eb64) → [`00b9eb68`](#insn-00b9eb68)
- ブロック [`00b9eb68`](#insn-00b9eb68) 範囲 `[['00b9eb68', '00b9eb6b']]`
  - `CONDITIONAL_JUMP` [`00b9eb68`](#insn-00b9eb68) → [`00b9eb74`](#insn-00b9eb74)
  - `FALL_THROUGH` [`00b9eb68`](#insn-00b9eb68) → [`00b9eb6c`](#insn-00b9eb6c)
- ブロック [`00b9eb6c`](#insn-00b9eb6c) 範囲 `[['00b9eb6c', '00b9eb6f']]`
  - `FALL_THROUGH` [`00b9eb6c`](#insn-00b9eb6c) → [`00b9eb70`](#insn-00b9eb70)
- ブロック [`00b9eb70`](#insn-00b9eb70) 範囲 `[['00b9eb70', '00b9eb73']]`
  - `CONDITIONAL_JUMP` [`00b9eb70`](#insn-00b9eb70) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9eb70`](#insn-00b9eb70) → [`00b9eb74`](#insn-00b9eb74)
- ブロック [`00b9eb74`](#insn-00b9eb74) 範囲 `[['00b9eb74', '00b9eb7b']]`
  - `FALL_THROUGH` [`00b9eb78`](#insn-00b9eb78) → [`00b9eb7c`](#insn-00b9eb7c)
- ブロック [`00b9eb7c`](#insn-00b9eb7c) 範囲 `[['00b9eb7c', '00b9eb7f']]`
  - `CONDITIONAL_JUMP` [`00b9eb7c`](#insn-00b9eb7c) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9eb7c`](#insn-00b9eb7c) → [`00b9eb80`](#insn-00b9eb80)
- ブロック [`00b9eb80`](#insn-00b9eb80) 範囲 `[['00b9eb80', '00b9eb83']]`
  - `FALL_THROUGH` [`00b9eb80`](#insn-00b9eb80) → [`00b9eb84`](#insn-00b9eb84)
- ブロック [`00b9eb84`](#insn-00b9eb84) 範囲 `[['00b9eb84', '00b9eb87']]`
  - `CONDITIONAL_JUMP` [`00b9eb84`](#insn-00b9eb84) → [`00b9eb90`](#insn-00b9eb90)
  - `FALL_THROUGH` [`00b9eb84`](#insn-00b9eb84) → [`00b9eb88`](#insn-00b9eb88)
- ブロック [`00b9eb88`](#insn-00b9eb88) 範囲 `[['00b9eb88', '00b9eb8b']]`
  - `FALL_THROUGH` [`00b9eb88`](#insn-00b9eb88) → [`00b9eb8c`](#insn-00b9eb8c)
- ブロック [`00b9eb8c`](#insn-00b9eb8c) 範囲 `[['00b9eb8c', '00b9eb8f']]`
  - `CONDITIONAL_JUMP` [`00b9eb8c`](#insn-00b9eb8c) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9eb8c`](#insn-00b9eb8c) → [`00b9eb90`](#insn-00b9eb90)
- ブロック [`00b9eb90`](#insn-00b9eb90) 範囲 `[['00b9eb90', '00b9eb93']]`
  - `CONDITIONAL_JUMP` [`00b9eb90`](#insn-00b9eb90) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9eb90`](#insn-00b9eb90) → [`00b9eb94`](#insn-00b9eb94)
- ブロック [`00b9eb94`](#insn-00b9eb94) 範囲 `[['00b9eb94', '00b9eb9f']]`
  - `CONDITIONAL_JUMP` [`00b9eb9c`](#insn-00b9eb9c) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9eb9c`](#insn-00b9eb9c) → [`00b9eba0`](#insn-00b9eba0)
- ブロック [`00b9eba0`](#insn-00b9eba0) 範囲 `[['00b9eba0', '00b9eba7']]`
  - `CONDITIONAL_JUMP` [`00b9eba4`](#insn-00b9eba4) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9eba4`](#insn-00b9eba4) → [`00b9eba8`](#insn-00b9eba8)
- ブロック [`00b9eba8`](#insn-00b9eba8) 範囲 `[['00b9eba8', '00b9ebb3']]`
  - `FALL_THROUGH` [`00b9ebb0`](#insn-00b9ebb0) → [`00b9ebb4`](#insn-00b9ebb4)
- ブロック [`00b9ebb4`](#insn-00b9ebb4) 範囲 `[['00b9ebb4', '00b9ebb7']]`
  - `FALL_THROUGH` [`00b9ebb4`](#insn-00b9ebb4) → [`00b9ebb8`](#insn-00b9ebb8)
- ブロック [`00b9ebb8`](#insn-00b9ebb8) 範囲 `[['00b9ebb8', '00b9ebbb']]`
  - `CONDITIONAL_JUMP` [`00b9ebb8`](#insn-00b9ebb8) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ebb8`](#insn-00b9ebb8) → [`00b9ebbc`](#insn-00b9ebbc)
- ブロック [`00b9ebbc`](#insn-00b9ebbc) 範囲 `[['00b9ebbc', '00b9ebbf']]`
  - `FALL_THROUGH` [`00b9ebbc`](#insn-00b9ebbc) → [`00b9ebc0`](#insn-00b9ebc0)
- ブロック [`00b9ebc0`](#insn-00b9ebc0) 範囲 `[['00b9ebc0', '00b9ebc3']]`
  - `CONDITIONAL_JUMP` [`00b9ebc0`](#insn-00b9ebc0) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ebc0`](#insn-00b9ebc0) → [`00b9ebc4`](#insn-00b9ebc4)
- ブロック [`00b9ebc4`](#insn-00b9ebc4) 範囲 `[['00b9ebc4', '00b9ebc7']]`
  - `FALL_THROUGH` [`00b9ebc4`](#insn-00b9ebc4) → [`00b9ebc8`](#insn-00b9ebc8)
- ブロック [`00b9ebc8`](#insn-00b9ebc8) 範囲 `[['00b9ebc8', '00b9ebcb']]`
  - `FALL_THROUGH` [`00b9ebc8`](#insn-00b9ebc8) → [`00b9ebcc`](#insn-00b9ebcc)
- ブロック [`00b9ebcc`](#insn-00b9ebcc) 範囲 `[['00b9ebcc', '00b9ebcf']]`
  - `CONDITIONAL_JUMP` [`00b9ebcc`](#insn-00b9ebcc) → [`00b9ebe8`](#insn-00b9ebe8)
  - `FALL_THROUGH` [`00b9ebcc`](#insn-00b9ebcc) → [`00b9ebd0`](#insn-00b9ebd0)
- ブロック [`00b9ebd0`](#insn-00b9ebd0) 範囲 `[['00b9ebd0', '00b9ebd3']]`
  - `FALL_THROUGH` [`00b9ebd0`](#insn-00b9ebd0) → [`00b9ebd4`](#insn-00b9ebd4)
- ブロック [`00b9ebd4`](#insn-00b9ebd4) 範囲 `[['00b9ebd4', '00b9ebdb']]`
  - `CONDITIONAL_JUMP` [`00b9ebd8`](#insn-00b9ebd8) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ebd8`](#insn-00b9ebd8) → [`00b9ebdc`](#insn-00b9ebdc)
- ブロック [`00b9ebdc`](#insn-00b9ebdc) 範囲 `[['00b9ebdc', '00b9ebe3']]`
  - `CONDITIONAL_JUMP` [`00b9ebe0`](#insn-00b9ebe0) → [`00b9ebf0`](#insn-00b9ebf0)
  - `FALL_THROUGH` [`00b9ebe0`](#insn-00b9ebe0) → [`00b9ebe4`](#insn-00b9ebe4)
- ブロック [`00b9ebe4`](#insn-00b9ebe4) 範囲 `[['00b9ebe4', '00b9ebe7']]`
  - `UNCONDITIONAL_JUMP` [`00b9ebe4`](#insn-00b9ebe4) → [`00b9ec10`](#insn-00b9ec10)
- ブロック [`00b9ebe8`](#insn-00b9ebe8) 範囲 `[['00b9ebe8', '00b9ebef']]`
  - `CONDITIONAL_JUMP` [`00b9ebec`](#insn-00b9ebec) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ebec`](#insn-00b9ebec) → [`00b9ebf0`](#insn-00b9ebf0)
- ブロック [`00b9ebf0`](#insn-00b9ebf0) 範囲 `[['00b9ebf0', '00b9ebfb']]`
  - `CONDITIONAL_JUMP` [`00b9ebf8`](#insn-00b9ebf8) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ebf8`](#insn-00b9ebf8) → [`00b9ebfc`](#insn-00b9ebfc)
- ブロック [`00b9ebfc`](#insn-00b9ebfc) 範囲 `[['00b9ebfc', '00b9ec0b']]`
  - `CONDITIONAL_JUMP` [`00b9ec08`](#insn-00b9ec08) → [`00b9ec24`](#insn-00b9ec24)
  - `FALL_THROUGH` [`00b9ec08`](#insn-00b9ec08) → [`00b9ec0c`](#insn-00b9ec0c)
- ブロック [`00b9ec0c`](#insn-00b9ec0c) 範囲 `[['00b9ec0c', '00b9ec0f']]`
  - `FALL_THROUGH` [`00b9ec0c`](#insn-00b9ec0c) → [`00b9ec10`](#insn-00b9ec10)
- ブロック [`00b9ec10`](#insn-00b9ec10) 範囲 `[['00b9ec10', '00b9ec23']]`
- ブロック [`00b9ec24`](#insn-00b9ec24) 範囲 `[['00b9ec24', '00b9ec33']]`
  - `CONDITIONAL_JUMP` [`00b9ec30`](#insn-00b9ec30) → [`00b9ec58`](#insn-00b9ec58)
  - `FALL_THROUGH` [`00b9ec30`](#insn-00b9ec30) → [`00b9ec34`](#insn-00b9ec34)
- ブロック [`00b9ec34`](#insn-00b9ec34) 範囲 `[['00b9ec34', '00b9ec3f']]`
  - `CONDITIONAL_JUMP` [`00b9ec3c`](#insn-00b9ec3c) → [`00b9ec94`](#insn-00b9ec94)
  - `FALL_THROUGH` [`00b9ec3c`](#insn-00b9ec3c) → [`00b9ec40`](#insn-00b9ec40)
- ブロック [`00b9ec40`](#insn-00b9ec40) 範囲 `[['00b9ec40', '00b9ec4b']]`
  - `CONDITIONAL_JUMP` [`00b9ec48`](#insn-00b9ec48) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ec48`](#insn-00b9ec48) → [`00b9ec4c`](#insn-00b9ec4c)
- ブロック [`00b9ec4c`](#insn-00b9ec4c) 範囲 `[['00b9ec4c', '00b9ec53']]`
  - `CONDITIONAL_JUMP` [`00b9ec50`](#insn-00b9ec50) → [`00b9ec9c`](#insn-00b9ec9c)
  - `FALL_THROUGH` [`00b9ec50`](#insn-00b9ec50) → [`00b9ec54`](#insn-00b9ec54)
- ブロック [`00b9ec54`](#insn-00b9ec54) 範囲 `[['00b9ec54', '00b9ec57']]`
  - `UNCONDITIONAL_JUMP` [`00b9ec54`](#insn-00b9ec54) → [`00b9ec10`](#insn-00b9ec10)
- ブロック [`00b9ec58`](#insn-00b9ec58) 範囲 `[['00b9ec58', '00b9ec5f']]`
  - `CONDITIONAL_JUMP` [`00b9ec5c`](#insn-00b9ec5c) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ec5c`](#insn-00b9ec5c) → [`00b9ec60`](#insn-00b9ec60)
- ブロック [`00b9ec60`](#insn-00b9ec60) 範囲 `[['00b9ec60', '00b9ec6b']]`
  - `CONDITIONAL_JUMP` [`00b9ec68`](#insn-00b9ec68) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ec68`](#insn-00b9ec68) → [`00b9ec6c`](#insn-00b9ec6c)
- ブロック [`00b9ec6c`](#insn-00b9ec6c) 範囲 `[['00b9ec6c', '00b9ec77']]`
  - `CONDITIONAL_JUMP` [`00b9ec74`](#insn-00b9ec74) → [`00b9ecf4`](#insn-00b9ecf4)
  - `FALL_THROUGH` [`00b9ec74`](#insn-00b9ec74) → [`00b9ec78`](#insn-00b9ec78)
- ブロック [`00b9ec78`](#insn-00b9ec78) 範囲 `[['00b9ec78', '00b9ec7b']]`
  - `FALL_THROUGH` [`00b9ec78`](#insn-00b9ec78) → [`00b9ec7c`](#insn-00b9ec7c)
- ブロック [`00b9ec7c`](#insn-00b9ec7c) 範囲 `[['00b9ec7c', '00b9ec87']]`
  - `CONDITIONAL_JUMP` [`00b9ec84`](#insn-00b9ec84) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ec84`](#insn-00b9ec84) → [`00b9ec88`](#insn-00b9ec88)
- ブロック [`00b9ec88`](#insn-00b9ec88) 範囲 `[['00b9ec88', '00b9ec8f']]`
  - `CONDITIONAL_JUMP` [`00b9ec8c`](#insn-00b9ec8c) → [`00b9ecfc`](#insn-00b9ecfc)
  - `FALL_THROUGH` [`00b9ec8c`](#insn-00b9ec8c) → [`00b9ec90`](#insn-00b9ec90)
- ブロック [`00b9ec90`](#insn-00b9ec90) 範囲 `[['00b9ec90', '00b9ec93']]`
  - `UNCONDITIONAL_JUMP` [`00b9ec90`](#insn-00b9ec90) → [`00b9ec10`](#insn-00b9ec10)
- ブロック [`00b9ec94`](#insn-00b9ec94) 範囲 `[['00b9ec94', '00b9ec9b']]`
  - `CONDITIONAL_JUMP` [`00b9ec98`](#insn-00b9ec98) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ec98`](#insn-00b9ec98) → [`00b9ec9c`](#insn-00b9ec9c)
- ブロック [`00b9ec9c`](#insn-00b9ec9c) 範囲 `[['00b9ec9c', '00b9ecaf']]`
  - `CONDITIONAL_JUMP` [`00b9ecac`](#insn-00b9ecac) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ecac`](#insn-00b9ecac) → [`00b9ecb0`](#insn-00b9ecb0)
- ブロック [`00b9ecb0`](#insn-00b9ecb0) 範囲 `[['00b9ecb0', '00b9ecc3']]`
  - `CONDITIONAL_JUMP` [`00b9ecc0`](#insn-00b9ecc0) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ecc0`](#insn-00b9ecc0) → [`00b9ecc4`](#insn-00b9ecc4)
- ブロック [`00b9ecc4`](#insn-00b9ecc4) 範囲 `[['00b9ecc4', '00b9eccb']]`
  - `CONDITIONAL_JUMP` [`00b9ecc8`](#insn-00b9ecc8) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ecc8`](#insn-00b9ecc8) → [`00b9eccc`](#insn-00b9eccc)
- ブロック [`00b9eccc`](#insn-00b9eccc) 範囲 `[['00b9eccc', '00b9ecd7']]`
  - `CONDITIONAL_JUMP` [`00b9ecd4`](#insn-00b9ecd4) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ecd4`](#insn-00b9ecd4) → [`00b9ecd8`](#insn-00b9ecd8)
- ブロック [`00b9ecd8`](#insn-00b9ecd8) 範囲 `[['00b9ecd8', '00b9ece3']]`
  - `CONDITIONAL_JUMP` [`00b9ece0`](#insn-00b9ece0) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ece0`](#insn-00b9ece0) → [`00b9ece4`](#insn-00b9ece4)
- ブロック [`00b9ece4`](#insn-00b9ece4) 範囲 `[['00b9ece4', '00b9ecef']]`
  - `CONDITIONAL_JUMP` [`00b9ecec`](#insn-00b9ecec) → [`00b9ec60`](#insn-00b9ec60)
  - `FALL_THROUGH` [`00b9ecec`](#insn-00b9ecec) → [`00b9ecf0`](#insn-00b9ecf0)
- ブロック [`00b9ecf0`](#insn-00b9ecf0) 範囲 `[['00b9ecf0', '00b9ecf3']]`
  - `UNCONDITIONAL_JUMP` [`00b9ecf0`](#insn-00b9ecf0) → [`00b9ec10`](#insn-00b9ec10)
- ブロック [`00b9ecf4`](#insn-00b9ecf4) 範囲 `[['00b9ecf4', '00b9ecfb']]`
  - `CONDITIONAL_JUMP` [`00b9ecf8`](#insn-00b9ecf8) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ecf8`](#insn-00b9ecf8) → [`00b9ecfc`](#insn-00b9ecfc)
- ブロック [`00b9ecfc`](#insn-00b9ecfc) 範囲 `[['00b9ecfc', '00b9ed07']]`
  - `CONDITIONAL_JUMP` [`00b9ed04`](#insn-00b9ed04) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ed04`](#insn-00b9ed04) → [`00b9ed08`](#insn-00b9ed08)
- ブロック [`00b9ed08`](#insn-00b9ed08) 範囲 `[['00b9ed08', '00b9ed13']]`
  - `CONDITIONAL_JUMP` [`00b9ed10`](#insn-00b9ed10) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ed10`](#insn-00b9ed10) → [`00b9ed14`](#insn-00b9ed14)
- ブロック [`00b9ed14`](#insn-00b9ed14) 範囲 `[['00b9ed14', '00b9ed27']]`
  - `CONDITIONAL_JUMP` [`00b9ed24`](#insn-00b9ed24) → [`00b9ed44`](#insn-00b9ed44)
  - `FALL_THROUGH` [`00b9ed24`](#insn-00b9ed24) → [`00b9ed28`](#insn-00b9ed28)
- ブロック [`00b9ed28`](#insn-00b9ed28) 範囲 `[['00b9ed28', '00b9ed33']]`
  - `CONDITIONAL_JUMP` [`00b9ed30`](#insn-00b9ed30) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ed30`](#insn-00b9ed30) → [`00b9ed34`](#insn-00b9ed34)
- ブロック [`00b9ed34`](#insn-00b9ed34) 範囲 `[['00b9ed34', '00b9ed43']]`
  - `UNCONDITIONAL_JUMP` [`00b9ed40`](#insn-00b9ed40) → [`00b9ed48`](#insn-00b9ed48)
- ブロック [`00b9ed44`](#insn-00b9ed44) 範囲 `[['00b9ed44', '00b9ed47']]`
  - `FALL_THROUGH` [`00b9ed44`](#insn-00b9ed44) → [`00b9ed48`](#insn-00b9ed48)
- ブロック [`00b9ed48`](#insn-00b9ed48) 範囲 `[['00b9ed48', '00b9ed5b']]`
  - `CONDITIONAL_JUMP` [`00b9ed58`](#insn-00b9ed58) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9ed58`](#insn-00b9ed58) → [`00b9ed5c`](#insn-00b9ed5c)
- ブロック [`00b9ed5c`](#insn-00b9ed5c) 範囲 `[['00b9ed5c', '00b9ed67']]`
  - `CONDITIONAL_JUMP` [`00b9ed64`](#insn-00b9ed64) → [`00b9eda4`](#insn-00b9eda4)
  - `FALL_THROUGH` [`00b9ed64`](#insn-00b9ed64) → [`00b9ed68`](#insn-00b9ed68)
- ブロック [`00b9ed68`](#insn-00b9ed68) 範囲 `[['00b9ed68', '00b9ed77']]`
  - `CONDITIONAL_JUMP` [`00b9ed74`](#insn-00b9ed74) → [`00b9ed84`](#insn-00b9ed84)
  - `FALL_THROUGH` [`00b9ed74`](#insn-00b9ed74) → [`00b9ed78`](#insn-00b9ed78)
- ブロック [`00b9ed78`](#insn-00b9ed78) 範囲 `[['00b9ed78', '00b9ed83']]`
  - `CONDITIONAL_JUMP` [`00b9ed80`](#insn-00b9ed80) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ed80`](#insn-00b9ed80) → [`00b9ed84`](#insn-00b9ed84)
- ブロック [`00b9ed84`](#insn-00b9ed84) 範囲 `[['00b9ed84', '00b9ed97']]`
  - `CONDITIONAL_JUMP` [`00b9ed94`](#insn-00b9ed94) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ed94`](#insn-00b9ed94) → [`00b9ed98`](#insn-00b9ed98)
- ブロック [`00b9ed98`](#insn-00b9ed98) 範囲 `[['00b9ed98', '00b9eda3']]`
  - `CONDITIONAL_JUMP` [`00b9eda0`](#insn-00b9eda0) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9eda0`](#insn-00b9eda0) → [`00b9eda4`](#insn-00b9eda4)
- ブロック [`00b9eda4`](#insn-00b9eda4) 範囲 `[['00b9eda4', '00b9edab']]`
  - `CONDITIONAL_JUMP` [`00b9eda8`](#insn-00b9eda8) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9eda8`](#insn-00b9eda8) → [`00b9edac`](#insn-00b9edac)
- ブロック [`00b9edac`](#insn-00b9edac) 範囲 `[['00b9edac', '00b9edb7']]`
  - `CONDITIONAL_JUMP` [`00b9edb4`](#insn-00b9edb4) → [`00b9edf4`](#insn-00b9edf4)
  - `FALL_THROUGH` [`00b9edb4`](#insn-00b9edb4) → [`00b9edb8`](#insn-00b9edb8)
- ブロック [`00b9edb8`](#insn-00b9edb8) 範囲 `[['00b9edb8', '00b9edc7']]`
  - `CONDITIONAL_JUMP` [`00b9edc4`](#insn-00b9edc4) → [`00b9edd4`](#insn-00b9edd4)
  - `FALL_THROUGH` [`00b9edc4`](#insn-00b9edc4) → [`00b9edc8`](#insn-00b9edc8)
- ブロック [`00b9edc8`](#insn-00b9edc8) 範囲 `[['00b9edc8', '00b9edd3']]`
  - `CONDITIONAL_JUMP` [`00b9edd0`](#insn-00b9edd0) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9edd0`](#insn-00b9edd0) → [`00b9edd4`](#insn-00b9edd4)
- ブロック [`00b9edd4`](#insn-00b9edd4) 範囲 `[['00b9edd4', '00b9ede3']]`
  - `FALL_THROUGH` [`00b9ede0`](#insn-00b9ede0) → [`00b9ede4`](#insn-00b9ede4)
- ブロック [`00b9ede4`](#insn-00b9ede4) 範囲 `[['00b9ede4', '00b9ede7']]`
  - `CONDITIONAL_JUMP` [`00b9ede4`](#insn-00b9ede4) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ede4`](#insn-00b9ede4) → [`00b9ede8`](#insn-00b9ede8)
- ブロック [`00b9ede8`](#insn-00b9ede8) 範囲 `[['00b9ede8', '00b9edeb']]`
  - `FALL_THROUGH` [`00b9ede8`](#insn-00b9ede8) → [`00b9edec`](#insn-00b9edec)
- ブロック [`00b9edec`](#insn-00b9edec) 範囲 `[['00b9edec', '00b9edf3']]`
  - `CONDITIONAL_JUMP` [`00b9edf0`](#insn-00b9edf0) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9edf0`](#insn-00b9edf0) → [`00b9edf4`](#insn-00b9edf4)
- ブロック [`00b9edf4`](#insn-00b9edf4) 範囲 `[['00b9edf4', '00b9edfb']]`
  - `CONDITIONAL_JUMP` [`00b9edf8`](#insn-00b9edf8) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9edf8`](#insn-00b9edf8) → [`00b9edfc`](#insn-00b9edfc)
- ブロック [`00b9edfc`](#insn-00b9edfc) 範囲 `[['00b9edfc', '00b9ee07']]`
  - `CONDITIONAL_JUMP` [`00b9ee04`](#insn-00b9ee04) → [`00b9ee48`](#insn-00b9ee48)
  - `FALL_THROUGH` [`00b9ee04`](#insn-00b9ee04) → [`00b9ee08`](#insn-00b9ee08)
- ブロック [`00b9ee08`](#insn-00b9ee08) 範囲 `[['00b9ee08', '00b9ee1b']]`
  - `CONDITIONAL_JUMP` [`00b9ee18`](#insn-00b9ee18) → [`00b9ee28`](#insn-00b9ee28)
  - `FALL_THROUGH` [`00b9ee18`](#insn-00b9ee18) → [`00b9ee1c`](#insn-00b9ee1c)
- ブロック [`00b9ee1c`](#insn-00b9ee1c) 範囲 `[['00b9ee1c', '00b9ee27']]`
  - `CONDITIONAL_JUMP` [`00b9ee24`](#insn-00b9ee24) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ee24`](#insn-00b9ee24) → [`00b9ee28`](#insn-00b9ee28)
- ブロック [`00b9ee28`](#insn-00b9ee28) 範囲 `[['00b9ee28', '00b9ee3b']]`
  - `CONDITIONAL_JUMP` [`00b9ee38`](#insn-00b9ee38) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ee38`](#insn-00b9ee38) → [`00b9ee3c`](#insn-00b9ee3c)
- ブロック [`00b9ee3c`](#insn-00b9ee3c) 範囲 `[['00b9ee3c', '00b9ee47']]`
  - `CONDITIONAL_JUMP` [`00b9ee44`](#insn-00b9ee44) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ee44`](#insn-00b9ee44) → [`00b9ee48`](#insn-00b9ee48)
- ブロック [`00b9ee48`](#insn-00b9ee48) 範囲 `[['00b9ee48', '00b9ee4f']]`
  - `CONDITIONAL_JUMP` [`00b9ee4c`](#insn-00b9ee4c) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9ee4c`](#insn-00b9ee4c) → [`00b9ee50`](#insn-00b9ee50)
- ブロック [`00b9ee50`](#insn-00b9ee50) 範囲 `[['00b9ee50', '00b9ee5b']]`
  - `CONDITIONAL_JUMP` [`00b9ee58`](#insn-00b9ee58) → [`00b9ee9c`](#insn-00b9ee9c)
  - `FALL_THROUGH` [`00b9ee58`](#insn-00b9ee58) → [`00b9ee5c`](#insn-00b9ee5c)
- ブロック [`00b9ee5c`](#insn-00b9ee5c) 範囲 `[['00b9ee5c', '00b9ee6b']]`
  - `FALL_THROUGH` [`00b9ee68`](#insn-00b9ee68) → [`00b9ee6c`](#insn-00b9ee6c)
- ブロック [`00b9ee6c`](#insn-00b9ee6c) 範囲 `[['00b9ee6c', '00b9ee6f']]`
  - `CONDITIONAL_JUMP` [`00b9ee6c`](#insn-00b9ee6c) → [`00b9ee7c`](#insn-00b9ee7c)
  - `FALL_THROUGH` [`00b9ee6c`](#insn-00b9ee6c) → [`00b9ee70`](#insn-00b9ee70)
- ブロック [`00b9ee70`](#insn-00b9ee70) 範囲 `[['00b9ee70', '00b9ee7b']]`
  - `CONDITIONAL_JUMP` [`00b9ee78`](#insn-00b9ee78) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ee78`](#insn-00b9ee78) → [`00b9ee7c`](#insn-00b9ee7c)
- ブロック [`00b9ee7c`](#insn-00b9ee7c) 範囲 `[['00b9ee7c', '00b9ee8f']]`
  - `CONDITIONAL_JUMP` [`00b9ee8c`](#insn-00b9ee8c) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ee8c`](#insn-00b9ee8c) → [`00b9ee90`](#insn-00b9ee90)
- ブロック [`00b9ee90`](#insn-00b9ee90) 範囲 `[['00b9ee90', '00b9ee9b']]`
  - `CONDITIONAL_JUMP` [`00b9ee98`](#insn-00b9ee98) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ee98`](#insn-00b9ee98) → [`00b9ee9c`](#insn-00b9ee9c)
- ブロック [`00b9ee9c`](#insn-00b9ee9c) 範囲 `[['00b9ee9c', '00b9eea3']]`
  - `CONDITIONAL_JUMP` [`00b9eea0`](#insn-00b9eea0) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9eea0`](#insn-00b9eea0) → [`00b9eea4`](#insn-00b9eea4)
- ブロック [`00b9eea4`](#insn-00b9eea4) 範囲 `[['00b9eea4', '00b9eeaf']]`
  - `CONDITIONAL_JUMP` [`00b9eeac`](#insn-00b9eeac) → [`00b9eee0`](#insn-00b9eee0)
  - `FALL_THROUGH` [`00b9eeac`](#insn-00b9eeac) → [`00b9eeb0`](#insn-00b9eeb0)
- ブロック [`00b9eeb0`](#insn-00b9eeb0) 範囲 `[['00b9eeb0', '00b9eebf']]`
  - `CONDITIONAL_JUMP` [`00b9eebc`](#insn-00b9eebc) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9eebc`](#insn-00b9eebc) → [`00b9eec0`](#insn-00b9eec0)
- ブロック [`00b9eec0`](#insn-00b9eec0) 範囲 `[['00b9eec0', '00b9eedf']]`
  - `CONDITIONAL_JUMP` [`00b9eedc`](#insn-00b9eedc) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9eedc`](#insn-00b9eedc) → [`00b9eee0`](#insn-00b9eee0)
- ブロック [`00b9eee0`](#insn-00b9eee0) 範囲 `[['00b9eee0', '00b9eee7']]`
  - `CONDITIONAL_JUMP` [`00b9eee4`](#insn-00b9eee4) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9eee4`](#insn-00b9eee4) → [`00b9eee8`](#insn-00b9eee8)
- ブロック [`00b9eee8`](#insn-00b9eee8) 範囲 `[['00b9eee8', '00b9eef3']]`
  - `CONDITIONAL_JUMP` [`00b9eef0`](#insn-00b9eef0) → [`00b9ef24`](#insn-00b9ef24)
  - `FALL_THROUGH` [`00b9eef0`](#insn-00b9eef0) → [`00b9eef4`](#insn-00b9eef4)
- ブロック [`00b9eef4`](#insn-00b9eef4) 範囲 `[['00b9eef4', '00b9ef03']]`
  - `CONDITIONAL_JUMP` [`00b9ef00`](#insn-00b9ef00) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ef00`](#insn-00b9ef00) → [`00b9ef04`](#insn-00b9ef04)
- ブロック [`00b9ef04`](#insn-00b9ef04) 範囲 `[['00b9ef04', '00b9ef23']]`
  - `CONDITIONAL_JUMP` [`00b9ef20`](#insn-00b9ef20) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ef20`](#insn-00b9ef20) → [`00b9ef24`](#insn-00b9ef24)
- ブロック [`00b9ef24`](#insn-00b9ef24) 範囲 `[['00b9ef24', '00b9ef2b']]`
  - `CONDITIONAL_JUMP` [`00b9ef28`](#insn-00b9ef28) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9ef28`](#insn-00b9ef28) → [`00b9ef2c`](#insn-00b9ef2c)
- ブロック [`00b9ef2c`](#insn-00b9ef2c) 範囲 `[['00b9ef2c', '00b9ef37']]`
  - `CONDITIONAL_JUMP` [`00b9ef34`](#insn-00b9ef34) → [`00b9ef68`](#insn-00b9ef68)
  - `FALL_THROUGH` [`00b9ef34`](#insn-00b9ef34) → [`00b9ef38`](#insn-00b9ef38)
- ブロック [`00b9ef38`](#insn-00b9ef38) 範囲 `[['00b9ef38', '00b9ef43']]`
  - `FALL_THROUGH` [`00b9ef40`](#insn-00b9ef40) → [`00b9ef44`](#insn-00b9ef44)
- ブロック [`00b9ef44`](#insn-00b9ef44) 範囲 `[['00b9ef44', '00b9ef47']]`
  - `CONDITIONAL_JUMP` [`00b9ef44`](#insn-00b9ef44) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ef44`](#insn-00b9ef44) → [`00b9ef48`](#insn-00b9ef48)
- ブロック [`00b9ef48`](#insn-00b9ef48) 範囲 `[['00b9ef48', '00b9ef4b']]`
  - `FALL_THROUGH` [`00b9ef48`](#insn-00b9ef48) → [`00b9ef4c`](#insn-00b9ef4c)
- ブロック [`00b9ef4c`](#insn-00b9ef4c) 範囲 `[['00b9ef4c', '00b9ef4f']]`
  - `FALL_THROUGH` [`00b9ef4c`](#insn-00b9ef4c) → [`00b9ef50`](#insn-00b9ef50)
- ブロック [`00b9ef50`](#insn-00b9ef50) 範囲 `[['00b9ef50', '00b9ef53']]`
  - `FALL_THROUGH` [`00b9ef50`](#insn-00b9ef50) → [`00b9ef54`](#insn-00b9ef54)
- ブロック [`00b9ef54`](#insn-00b9ef54) 範囲 `[['00b9ef54', '00b9ef57']]`
  - `FALL_THROUGH` [`00b9ef54`](#insn-00b9ef54) → [`00b9ef58`](#insn-00b9ef58)
- ブロック [`00b9ef58`](#insn-00b9ef58) 範囲 `[['00b9ef58', '00b9ef67']]`
  - `CONDITIONAL_JUMP` [`00b9ef64`](#insn-00b9ef64) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9ef64`](#insn-00b9ef64) → [`00b9ef68`](#insn-00b9ef68)
- ブロック [`00b9ef68`](#insn-00b9ef68) 範囲 `[['00b9ef68', '00b9ef6f']]`
  - `CONDITIONAL_JUMP` [`00b9ef6c`](#insn-00b9ef6c) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9ef6c`](#insn-00b9ef6c) → [`00b9ef70`](#insn-00b9ef70)
- ブロック [`00b9ef70`](#insn-00b9ef70) 範囲 `[['00b9ef70', '00b9ef77']]`
  - `CONDITIONAL_JUMP` [`00b9ef74`](#insn-00b9ef74) → [`00b9efd8`](#insn-00b9efd8)
  - `FALL_THROUGH` [`00b9ef74`](#insn-00b9ef74) → [`00b9ef78`](#insn-00b9ef78)
- ブロック [`00b9ef78`](#insn-00b9ef78) 範囲 `[['00b9ef78', '00b9ef8f']]`
  - `CONDITIONAL_JUMP` [`00b9ef8c`](#insn-00b9ef8c) → [`00b9ef9c`](#insn-00b9ef9c)
  - `FALL_THROUGH` [`00b9ef8c`](#insn-00b9ef8c) → [`00b9ef90`](#insn-00b9ef90)
- ブロック [`00b9ef90`](#insn-00b9ef90) 範囲 `[['00b9ef90', '00b9ef9b']]`
  - `CONDITIONAL_JUMP` [`00b9ef98`](#insn-00b9ef98) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9ef98`](#insn-00b9ef98) → [`00b9ef9c`](#insn-00b9ef9c)
- ブロック [`00b9ef9c`](#insn-00b9ef9c) 範囲 `[['00b9ef9c', '00b9efaf']]`
  - `CONDITIONAL_JUMP` [`00b9efac`](#insn-00b9efac) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9efac`](#insn-00b9efac) → [`00b9efb0`](#insn-00b9efb0)
- ブロック [`00b9efb0`](#insn-00b9efb0) 範囲 `[['00b9efb0', '00b9efbb']]`
  - `CONDITIONAL_JUMP` [`00b9efb8`](#insn-00b9efb8) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9efb8`](#insn-00b9efb8) → [`00b9efbc`](#insn-00b9efbc)
- ブロック [`00b9efbc`](#insn-00b9efbc) 範囲 `[['00b9efbc', '00b9efc7']]`
  - `CONDITIONAL_JUMP` [`00b9efc4`](#insn-00b9efc4) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9efc4`](#insn-00b9efc4) → [`00b9efc8`](#insn-00b9efc8)
- ブロック [`00b9efc8`](#insn-00b9efc8) 範囲 `[['00b9efc8', '00b9efd7']]`
  - `CONDITIONAL_JUMP` [`00b9efd4`](#insn-00b9efd4) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9efd4`](#insn-00b9efd4) → [`00b9efd8`](#insn-00b9efd8)
- ブロック [`00b9efd8`](#insn-00b9efd8) 範囲 `[['00b9efd8', '00b9efdf']]`
  - `CONDITIONAL_JUMP` [`00b9efdc`](#insn-00b9efdc) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9efdc`](#insn-00b9efdc) → [`00b9efe0`](#insn-00b9efe0)
- ブロック [`00b9efe0`](#insn-00b9efe0) 範囲 `[['00b9efe0', '00b9eff7']]`
  - `CONDITIONAL_JUMP` [`00b9eff4`](#insn-00b9eff4) → [`00b9f064`](#insn-00b9f064)
  - `FALL_THROUGH` [`00b9eff4`](#insn-00b9eff4) → [`00b9eff8`](#insn-00b9eff8)
- ブロック [`00b9eff8`](#insn-00b9eff8) 範囲 `[['00b9eff8', '00b9f007']]`
  - `CONDITIONAL_JUMP` [`00b9f004`](#insn-00b9f004) → [`00b9f014`](#insn-00b9f014)
  - `FALL_THROUGH` [`00b9f004`](#insn-00b9f004) → [`00b9f008`](#insn-00b9f008)
- ブロック [`00b9f008`](#insn-00b9f008) 範囲 `[['00b9f008', '00b9f013']]`
  - `CONDITIONAL_JUMP` [`00b9f010`](#insn-00b9f010) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f010`](#insn-00b9f010) → [`00b9f014`](#insn-00b9f014)
- ブロック [`00b9f014`](#insn-00b9f014) 範囲 `[['00b9f014', '00b9f027']]`
  - `CONDITIONAL_JUMP` [`00b9f024`](#insn-00b9f024) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f024`](#insn-00b9f024) → [`00b9f028`](#insn-00b9f028)
- ブロック [`00b9f028`](#insn-00b9f028) 範囲 `[['00b9f028', '00b9f037']]`
  - `CONDITIONAL_JUMP` [`00b9f034`](#insn-00b9f034) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f034`](#insn-00b9f034) → [`00b9f038`](#insn-00b9f038)
- ブロック [`00b9f038`](#insn-00b9f038) 範囲 `[['00b9f038', '00b9f047']]`
  - `CONDITIONAL_JUMP` [`00b9f044`](#insn-00b9f044) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f044`](#insn-00b9f044) → [`00b9f048`](#insn-00b9f048)
- ブロック [`00b9f048`](#insn-00b9f048) 範囲 `[['00b9f048', '00b9f05b']]`
  - `CONDITIONAL_JUMP` [`00b9f058`](#insn-00b9f058) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f058`](#insn-00b9f058) → [`00b9f05c`](#insn-00b9f05c)
- ブロック [`00b9f05c`](#insn-00b9f05c) 範囲 `[['00b9f05c', '00b9f063']]`
  - `CONDITIONAL_JUMP` [`00b9f060`](#insn-00b9f060) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f060`](#insn-00b9f060) → [`00b9f064`](#insn-00b9f064)
- ブロック [`00b9f064`](#insn-00b9f064) 範囲 `[['00b9f064', '00b9f06f']]`
  - `CONDITIONAL_JUMP` [`00b9f06c`](#insn-00b9f06c) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9f06c`](#insn-00b9f06c) → [`00b9f070`](#insn-00b9f070)
- ブロック [`00b9f070`](#insn-00b9f070) 範囲 `[['00b9f070', '00b9f077']]`
  - `CONDITIONAL_JUMP` [`00b9f074`](#insn-00b9f074) → [`00b9f0c0`](#insn-00b9f0c0)
  - `FALL_THROUGH` [`00b9f074`](#insn-00b9f074) → [`00b9f078`](#insn-00b9f078)
- ブロック [`00b9f078`](#insn-00b9f078) 範囲 `[['00b9f078', '00b9f083']]`
  - `FALL_THROUGH` [`00b9f080`](#insn-00b9f080) → [`00b9f084`](#insn-00b9f084)
- ブロック [`00b9f084`](#insn-00b9f084) 範囲 `[['00b9f084', '00b9f08f']]`
  - `FALL_THROUGH` [`00b9f08c`](#insn-00b9f08c) → [`00b9f090`](#insn-00b9f090)
- ブロック [`00b9f090`](#insn-00b9f090) 範囲 `[['00b9f090', '00b9f093']]`
  - `FALL_THROUGH` [`00b9f090`](#insn-00b9f090) → [`00b9f094`](#insn-00b9f094)
- ブロック [`00b9f094`](#insn-00b9f094) 範囲 `[['00b9f094', '00b9f09f']]`
  - `CONDITIONAL_JUMP` [`00b9f09c`](#insn-00b9f09c) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f09c`](#insn-00b9f09c) → [`00b9f0a0`](#insn-00b9f0a0)
- ブロック [`00b9f0a0`](#insn-00b9f0a0) 範囲 `[['00b9f0a0', '00b9f0b3']]`
  - `CONDITIONAL_JUMP` [`00b9f0b0`](#insn-00b9f0b0) → [`00b9f084`](#insn-00b9f084)
  - `FALL_THROUGH` [`00b9f0b0`](#insn-00b9f0b0) → [`00b9f0b4`](#insn-00b9f0b4)
- ブロック [`00b9f0b4`](#insn-00b9f0b4) 範囲 `[['00b9f0b4', '00b9f0bf']]`
  - `FALL_THROUGH` [`00b9f0bc`](#insn-00b9f0bc) → [`00b9f0c0`](#insn-00b9f0c0)
- ブロック [`00b9f0c0`](#insn-00b9f0c0) 範囲 `[['00b9f0c0', '00b9f0d3']]`
  - `CONDITIONAL_JUMP` [`00b9f0d0`](#insn-00b9f0d0) → [`00b9f350`](#insn-00b9f350)
  - `FALL_THROUGH` [`00b9f0d0`](#insn-00b9f0d0) → [`00b9f0d4`](#insn-00b9f0d4)
- ブロック [`00b9f0d4`](#insn-00b9f0d4) 範囲 `[['00b9f0d4', '00b9f0db']]`
  - `CONDITIONAL_JUMP` [`00b9f0d8`](#insn-00b9f0d8) → [`00b9f13c`](#insn-00b9f13c)
  - `FALL_THROUGH` [`00b9f0d8`](#insn-00b9f0d8) → [`00b9f0dc`](#insn-00b9f0dc)
- ブロック [`00b9f0dc`](#insn-00b9f0dc) 範囲 `[['00b9f0dc', '00b9f0f3']]`
  - `CONDITIONAL_JUMP` [`00b9f0f0`](#insn-00b9f0f0) → [`00b9f100`](#insn-00b9f100)
  - `FALL_THROUGH` [`00b9f0f0`](#insn-00b9f0f0) → [`00b9f0f4`](#insn-00b9f0f4)
- ブロック [`00b9f0f4`](#insn-00b9f0f4) 範囲 `[['00b9f0f4', '00b9f0f7']]`
  - `FALL_THROUGH` [`00b9f0f4`](#insn-00b9f0f4) → [`00b9f0f8`](#insn-00b9f0f8)
- ブロック [`00b9f0f8`](#insn-00b9f0f8) 範囲 `[['00b9f0f8', '00b9f0ff']]`
  - `CONDITIONAL_JUMP` [`00b9f0fc`](#insn-00b9f0fc) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f0fc`](#insn-00b9f0fc) → [`00b9f100`](#insn-00b9f100)
- ブロック [`00b9f100`](#insn-00b9f100) 範囲 `[['00b9f100', '00b9f113']]`
  - `CONDITIONAL_JUMP` [`00b9f110`](#insn-00b9f110) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f110`](#insn-00b9f110) → [`00b9f114`](#insn-00b9f114)
- ブロック [`00b9f114`](#insn-00b9f114) 範囲 `[['00b9f114', '00b9f11f']]`
  - `CONDITIONAL_JUMP` [`00b9f11c`](#insn-00b9f11c) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f11c`](#insn-00b9f11c) → [`00b9f120`](#insn-00b9f120)
- ブロック [`00b9f120`](#insn-00b9f120) 範囲 `[['00b9f120', '00b9f12b']]`
  - `CONDITIONAL_JUMP` [`00b9f128`](#insn-00b9f128) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f128`](#insn-00b9f128) → [`00b9f12c`](#insn-00b9f12c)
- ブロック [`00b9f12c`](#insn-00b9f12c) 範囲 `[['00b9f12c', '00b9f13b']]`
  - `CONDITIONAL_JUMP` [`00b9f138`](#insn-00b9f138) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f138`](#insn-00b9f138) → [`00b9f13c`](#insn-00b9f13c)
- ブロック [`00b9f13c`](#insn-00b9f13c) 範囲 `[['00b9f13c', '00b9f143']]`
  - `CONDITIONAL_JUMP` [`00b9f140`](#insn-00b9f140) → [`00b9f284`](#insn-00b9f284)
  - `FALL_THROUGH` [`00b9f140`](#insn-00b9f140) → [`00b9f144`](#insn-00b9f144)
- ブロック [`00b9f144`](#insn-00b9f144) 範囲 `[['00b9f144', '00b9f15b']]`
  - `CONDITIONAL_JUMP` [`00b9f158`](#insn-00b9f158) → [`00b9f1c8`](#insn-00b9f1c8)
  - `FALL_THROUGH` [`00b9f158`](#insn-00b9f158) → [`00b9f15c`](#insn-00b9f15c)
- ブロック [`00b9f15c`](#insn-00b9f15c) 範囲 `[['00b9f15c', '00b9f16b']]`
  - `CONDITIONAL_JUMP` [`00b9f168`](#insn-00b9f168) → [`00b9f178`](#insn-00b9f178)
  - `FALL_THROUGH` [`00b9f168`](#insn-00b9f168) → [`00b9f16c`](#insn-00b9f16c)
- ブロック [`00b9f16c`](#insn-00b9f16c) 範囲 `[['00b9f16c', '00b9f173']]`
  - `FALL_THROUGH` [`00b9f170`](#insn-00b9f170) → [`00b9f174`](#insn-00b9f174)
- ブロック [`00b9f174`](#insn-00b9f174) 範囲 `[['00b9f174', '00b9f177']]`
  - `CONDITIONAL_JUMP` [`00b9f174`](#insn-00b9f174) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f174`](#insn-00b9f174) → [`00b9f178`](#insn-00b9f178)
- ブロック [`00b9f178`](#insn-00b9f178) 範囲 `[['00b9f178', '00b9f18b']]`
  - `CONDITIONAL_JUMP` [`00b9f188`](#insn-00b9f188) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f188`](#insn-00b9f188) → [`00b9f18c`](#insn-00b9f18c)
- ブロック [`00b9f18c`](#insn-00b9f18c) 範囲 `[['00b9f18c', '00b9f19b']]`
  - `CONDITIONAL_JUMP` [`00b9f198`](#insn-00b9f198) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f198`](#insn-00b9f198) → [`00b9f19c`](#insn-00b9f19c)
- ブロック [`00b9f19c`](#insn-00b9f19c) 範囲 `[['00b9f19c', '00b9f19f']]`
  - `FALL_THROUGH` [`00b9f19c`](#insn-00b9f19c) → [`00b9f1a0`](#insn-00b9f1a0)
- ブロック [`00b9f1a0`](#insn-00b9f1a0) 範囲 `[['00b9f1a0', '00b9f1ab']]`
  - `CONDITIONAL_JUMP` [`00b9f1a8`](#insn-00b9f1a8) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f1a8`](#insn-00b9f1a8) → [`00b9f1ac`](#insn-00b9f1ac)
- ブロック [`00b9f1ac`](#insn-00b9f1ac) 範囲 `[['00b9f1ac', '00b9f1af']]`
  - `FALL_THROUGH` [`00b9f1ac`](#insn-00b9f1ac) → [`00b9f1b0`](#insn-00b9f1b0)
- ブロック [`00b9f1b0`](#insn-00b9f1b0) 範囲 `[['00b9f1b0', '00b9f1bf']]`
  - `CONDITIONAL_JUMP` [`00b9f1bc`](#insn-00b9f1bc) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f1bc`](#insn-00b9f1bc) → [`00b9f1c0`](#insn-00b9f1c0)
- ブロック [`00b9f1c0`](#insn-00b9f1c0) 範囲 `[['00b9f1c0', '00b9f1c7']]`
  - `CONDITIONAL_JUMP` [`00b9f1c4`](#insn-00b9f1c4) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f1c4`](#insn-00b9f1c4) → [`00b9f1c8`](#insn-00b9f1c8)
- ブロック [`00b9f1c8`](#insn-00b9f1c8) 範囲 `[['00b9f1c8', '00b9f1d3']]`
  - `CONDITIONAL_JUMP` [`00b9f1d0`](#insn-00b9f1d0) → [`00b9f284`](#insn-00b9f284)
  - `FALL_THROUGH` [`00b9f1d0`](#insn-00b9f1d0) → [`00b9f1d4`](#insn-00b9f1d4)
- ブロック [`00b9f1d4`](#insn-00b9f1d4) 範囲 `[['00b9f1d4', '00b9f1db']]`
  - `CONDITIONAL_JUMP` [`00b9f1d8`](#insn-00b9f1d8) → [`00b9f284`](#insn-00b9f284)
  - `FALL_THROUGH` [`00b9f1d8`](#insn-00b9f1d8) → [`00b9f1dc`](#insn-00b9f1dc)
- ブロック [`00b9f1dc`](#insn-00b9f1dc) 範囲 `[['00b9f1dc', '00b9f1fb']]`
  - `FALL_THROUGH` [`00b9f1f8`](#insn-00b9f1f8) → [`00b9f1fc`](#insn-00b9f1fc)
- ブロック [`00b9f1fc`](#insn-00b9f1fc) 範囲 `[['00b9f1fc', '00b9f21f']]`
  - `FALL_THROUGH` [`00b9f21c`](#insn-00b9f21c) → [`00b9f220`](#insn-00b9f220)
- ブロック [`00b9f220`](#insn-00b9f220) 範囲 `[['00b9f220', '00b9f22b']]`
  - `CONDITIONAL_JUMP` [`00b9f228`](#insn-00b9f228) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f228`](#insn-00b9f228) → [`00b9f22c`](#insn-00b9f22c)
- ブロック [`00b9f22c`](#insn-00b9f22c) 範囲 `[['00b9f22c', '00b9f233']]`
  - `CONDITIONAL_JUMP` [`00b9f230`](#insn-00b9f230) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f230`](#insn-00b9f230) → [`00b9f234`](#insn-00b9f234)
- ブロック [`00b9f234`](#insn-00b9f234) 範囲 `[['00b9f234', '00b9f23b']]`
  - `CONDITIONAL_JUMP` [`00b9f238`](#insn-00b9f238) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f238`](#insn-00b9f238) → [`00b9f23c`](#insn-00b9f23c)
- ブロック [`00b9f23c`](#insn-00b9f23c) 範囲 `[['00b9f23c', '00b9f247']]`
  - `CONDITIONAL_JUMP` [`00b9f244`](#insn-00b9f244) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f244`](#insn-00b9f244) → [`00b9f248`](#insn-00b9f248)
- ブロック [`00b9f248`](#insn-00b9f248) 範囲 `[['00b9f248', '00b9f25b']]`
  - `CONDITIONAL_JUMP` [`00b9f258`](#insn-00b9f258) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f258`](#insn-00b9f258) → [`00b9f25c`](#insn-00b9f25c)
- ブロック [`00b9f25c`](#insn-00b9f25c) 範囲 `[['00b9f25c', '00b9f263']]`
  - `CONDITIONAL_JUMP` [`00b9f260`](#insn-00b9f260) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f260`](#insn-00b9f260) → [`00b9f264`](#insn-00b9f264)
- ブロック [`00b9f264`](#insn-00b9f264) 範囲 `[['00b9f264', '00b9f26f']]`
  - `CONDITIONAL_JUMP` [`00b9f26c`](#insn-00b9f26c) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f26c`](#insn-00b9f26c) → [`00b9f270`](#insn-00b9f270)
- ブロック [`00b9f270`](#insn-00b9f270) 範囲 `[['00b9f270', '00b9f277']]`
  - `CONDITIONAL_JUMP` [`00b9f274`](#insn-00b9f274) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f274`](#insn-00b9f274) → [`00b9f278`](#insn-00b9f278)
- ブロック [`00b9f278`](#insn-00b9f278) 範囲 `[['00b9f278', '00b9f283']]`
  - `CONDITIONAL_JUMP` [`00b9f280`](#insn-00b9f280) → [`00b9f1fc`](#insn-00b9f1fc)
  - `FALL_THROUGH` [`00b9f280`](#insn-00b9f280) → [`00b9f284`](#insn-00b9f284)
- ブロック [`00b9f284`](#insn-00b9f284) 範囲 `[['00b9f284', '00b9f28f']]`
  - `CONDITIONAL_JUMP` [`00b9f28c`](#insn-00b9f28c) → [`00b9f350`](#insn-00b9f350)
  - `FALL_THROUGH` [`00b9f28c`](#insn-00b9f28c) → [`00b9f290`](#insn-00b9f290)
- ブロック [`00b9f290`](#insn-00b9f290) 範囲 `[['00b9f290', '00b9f297']]`
  - `CONDITIONAL_JUMP` [`00b9f294`](#insn-00b9f294) → [`00b9f2c4`](#insn-00b9f2c4)
  - `FALL_THROUGH` [`00b9f294`](#insn-00b9f294) → [`00b9f298`](#insn-00b9f298)
- ブロック [`00b9f298`](#insn-00b9f298) 範囲 `[['00b9f298', '00b9f2a7']]`
  - `CONDITIONAL_JUMP` [`00b9f2a4`](#insn-00b9f2a4) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f2a4`](#insn-00b9f2a4) → [`00b9f2a8`](#insn-00b9f2a8)
- ブロック [`00b9f2a8`](#insn-00b9f2a8) 範囲 `[['00b9f2a8', '00b9f2c3']]`
  - `CONDITIONAL_JUMP` [`00b9f2c0`](#insn-00b9f2c0) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f2c0`](#insn-00b9f2c0) → [`00b9f2c4`](#insn-00b9f2c4)
- ブロック [`00b9f2c4`](#insn-00b9f2c4) 範囲 `[['00b9f2c4', '00b9f2cb']]`
  - `CONDITIONAL_JUMP` [`00b9f2c8`](#insn-00b9f2c8) → [`00b9f350`](#insn-00b9f350)
  - `FALL_THROUGH` [`00b9f2c8`](#insn-00b9f2c8) → [`00b9f2cc`](#insn-00b9f2cc)
- ブロック [`00b9f2cc`](#insn-00b9f2cc) 範囲 `[['00b9f2cc', '00b9f2d3']]`
  - `CONDITIONAL_JUMP` [`00b9f2d0`](#insn-00b9f2d0) → [`00b9f314`](#insn-00b9f314)
  - `FALL_THROUGH` [`00b9f2d0`](#insn-00b9f2d0) → [`00b9f2d4`](#insn-00b9f2d4)
- ブロック [`00b9f2d4`](#insn-00b9f2d4) 範囲 `[['00b9f2d4', '00b9f2e3']]`
  - `CONDITIONAL_JUMP` [`00b9f2e0`](#insn-00b9f2e0) → [`00b9f2f0`](#insn-00b9f2f0)
  - `FALL_THROUGH` [`00b9f2e0`](#insn-00b9f2e0) → [`00b9f2e4`](#insn-00b9f2e4)
- ブロック [`00b9f2e4`](#insn-00b9f2e4) 範囲 `[['00b9f2e4', '00b9f2ef']]`
  - `CONDITIONAL_JUMP` [`00b9f2ec`](#insn-00b9f2ec) → [`00b9ec0c`](#insn-00b9ec0c)
  - `FALL_THROUGH` [`00b9f2ec`](#insn-00b9f2ec) → [`00b9f2f0`](#insn-00b9f2f0)
- ブロック [`00b9f2f0`](#insn-00b9f2f0) 範囲 `[['00b9f2f0', '00b9f303']]`
  - `CONDITIONAL_JUMP` [`00b9f300`](#insn-00b9f300) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f300`](#insn-00b9f300) → [`00b9f304`](#insn-00b9f304)
- ブロック [`00b9f304`](#insn-00b9f304) 範囲 `[['00b9f304', '00b9f307']]`
  - `FALL_THROUGH` [`00b9f304`](#insn-00b9f304) → [`00b9f308`](#insn-00b9f308)
- ブロック [`00b9f308`](#insn-00b9f308) 範囲 `[['00b9f308', '00b9f30f']]`
  - `FALL_THROUGH` [`00b9f30c`](#insn-00b9f30c) → [`00b9f310`](#insn-00b9f310)
- ブロック [`00b9f310`](#insn-00b9f310) 範囲 `[['00b9f310', '00b9f313']]`
  - `CONDITIONAL_JUMP` [`00b9f310`](#insn-00b9f310) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f310`](#insn-00b9f310) → [`00b9f314`](#insn-00b9f314)
- ブロック [`00b9f314`](#insn-00b9f314) 範囲 `[['00b9f314', '00b9f31b']]`
  - `CONDITIONAL_JUMP` [`00b9f318`](#insn-00b9f318) → [`00b9f350`](#insn-00b9f350)
  - `FALL_THROUGH` [`00b9f318`](#insn-00b9f318) → [`00b9f31c`](#insn-00b9f31c)
- ブロック [`00b9f31c`](#insn-00b9f31c) 範囲 `[['00b9f31c', '00b9f323']]`
  - `CONDITIONAL_JUMP` [`00b9f320`](#insn-00b9f320) → [`00b9f350`](#insn-00b9f350)
  - `FALL_THROUGH` [`00b9f320`](#insn-00b9f320) → [`00b9f324`](#insn-00b9f324)
- ブロック [`00b9f324`](#insn-00b9f324) 範囲 `[['00b9f324', '00b9f333']]`
  - `CONDITIONAL_JUMP` [`00b9f330`](#insn-00b9f330) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f330`](#insn-00b9f330) → [`00b9f334`](#insn-00b9f334)
- ブロック [`00b9f334`](#insn-00b9f334) 範囲 `[['00b9f334', '00b9f34f']]`
  - `CONDITIONAL_JUMP` [`00b9f34c`](#insn-00b9f34c) → [`00b9ec10`](#insn-00b9ec10)
  - `FALL_THROUGH` [`00b9f34c`](#insn-00b9f34c) → [`00b9f350`](#insn-00b9f350)
- ブロック [`00b9f350`](#insn-00b9f350) 範囲 `[['00b9f350', '00b9f363']]`
  - `UNCONDITIONAL_JUMP` [`00b9f360`](#insn-00b9f360) → [`00b9ec10`](#insn-00b9ec10)

## 命令位置別の参照

- [`00b9eaf0`](#insn-00b9eaf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eaf4`](#insn-00b9eaf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eaf8`](#insn-00b9eaf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb10`](#insn-00b9eb10) → [`00b9eb1c`](#insn-00b9eb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb18`](#insn-00b9eb18) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb28`](#insn-00b9eb28) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb34`](#insn-00b9eb34) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb54`](#insn-00b9eb54) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb60`](#insn-00b9eb60) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb68`](#insn-00b9eb68) → [`00b9eb74`](#insn-00b9eb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb70`](#insn-00b9eb70) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb7c`](#insn-00b9eb7c) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb84`](#insn-00b9eb84) → [`00b9eb90`](#insn-00b9eb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb8c`](#insn-00b9eb8c) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb90`](#insn-00b9eb90) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eb9c`](#insn-00b9eb9c) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eba4`](#insn-00b9eba4) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebb8`](#insn-00b9ebb8) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebc0`](#insn-00b9ebc0) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebcc`](#insn-00b9ebcc) → [`00b9ebe8`](#insn-00b9ebe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebd8`](#insn-00b9ebd8) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebe0`](#insn-00b9ebe0) → [`00b9ebf0`](#insn-00b9ebf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebe4`](#insn-00b9ebe4) → [`00b9ec10`](#insn-00b9ec10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebec`](#insn-00b9ebec) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ebf8`](#insn-00b9ebf8) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec08`](#insn-00b9ec08) → [`00b9ec24`](#insn-00b9ec24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec10`](#insn-00b9ec10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec14`](#insn-00b9ec14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec18`](#insn-00b9ec18) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec30`](#insn-00b9ec30) → [`00b9ec58`](#insn-00b9ec58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec3c`](#insn-00b9ec3c) → [`00b9ec94`](#insn-00b9ec94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec48`](#insn-00b9ec48) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec50`](#insn-00b9ec50) → [`00b9ec9c`](#insn-00b9ec9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec54`](#insn-00b9ec54) → [`00b9ec10`](#insn-00b9ec10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec5c`](#insn-00b9ec5c) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec60`](#insn-00b9ec60) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec68`](#insn-00b9ec68) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec74`](#insn-00b9ec74) → [`00b9ecf4`](#insn-00b9ecf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec78`](#insn-00b9ec78) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec84`](#insn-00b9ec84) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec8c`](#insn-00b9ec8c) → [`00b9ecfc`](#insn-00b9ecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec90`](#insn-00b9ec90) → [`00b9ec10`](#insn-00b9ec10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ec98`](#insn-00b9ec98) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ecac`](#insn-00b9ecac) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ecc0`](#insn-00b9ecc0) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ecc8`](#insn-00b9ecc8) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ecd4`](#insn-00b9ecd4) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ece0`](#insn-00b9ece0) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ecec`](#insn-00b9ecec) → [`00b9ec60`](#insn-00b9ec60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ecf0`](#insn-00b9ecf0) → [`00b9ec10`](#insn-00b9ec10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ecf8`](#insn-00b9ecf8) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed04`](#insn-00b9ed04) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed10`](#insn-00b9ed10) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed14`](#insn-00b9ed14) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed24`](#insn-00b9ed24) → [`00b9ed44`](#insn-00b9ed44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed28`](#insn-00b9ed28) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed2c`](#insn-00b9ed2c) → [`00c5c540`](../00c5c/00c5c540.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c540` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed30`](#insn-00b9ed30) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed34`](#insn-00b9ed34) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed40`](#insn-00b9ed40) → [`00b9ed48`](#insn-00b9ed48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed48`](#insn-00b9ed48) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed58`](#insn-00b9ed58) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed60`](#insn-00b9ed60) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed64`](#insn-00b9ed64) → [`00b9eda4`](#insn-00b9eda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed74`](#insn-00b9ed74) → [`00b9ed84`](#insn-00b9ed84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed78`](#insn-00b9ed78) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed80`](#insn-00b9ed80) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed84`](#insn-00b9ed84) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ed94`](#insn-00b9ed94) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eda0`](#insn-00b9eda0) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eda8`](#insn-00b9eda8) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edb0`](#insn-00b9edb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edb4`](#insn-00b9edb4) → [`00b9edf4`](#insn-00b9edf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edc4`](#insn-00b9edc4) → [`00b9edd4`](#insn-00b9edd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edc8`](#insn-00b9edc8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edd0`](#insn-00b9edd0) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edd4`](#insn-00b9edd4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ede4`](#insn-00b9ede4) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edf0`](#insn-00b9edf0) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9edf8`](#insn-00b9edf8) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee00`](#insn-00b9ee00) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee04`](#insn-00b9ee04) → [`00b9ee48`](#insn-00b9ee48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee18`](#insn-00b9ee18) → [`00b9ee28`](#insn-00b9ee28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee1c`](#insn-00b9ee1c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee24`](#insn-00b9ee24) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee28`](#insn-00b9ee28) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee38`](#insn-00b9ee38) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee44`](#insn-00b9ee44) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee4c`](#insn-00b9ee4c) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee54`](#insn-00b9ee54) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee58`](#insn-00b9ee58) → [`00b9ee9c`](#insn-00b9ee9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee6c`](#insn-00b9ee6c) → [`00b9ee7c`](#insn-00b9ee7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee70`](#insn-00b9ee70) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee78`](#insn-00b9ee78) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee7c`](#insn-00b9ee7c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee8c`](#insn-00b9ee8c) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ee98`](#insn-00b9ee98) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eea0`](#insn-00b9eea0) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eea8`](#insn-00b9eea8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eeac`](#insn-00b9eeac) → [`00b9eee0`](#insn-00b9eee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eebc`](#insn-00b9eebc) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eec0`](#insn-00b9eec0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eecc`](#insn-00b9eecc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eedc`](#insn-00b9eedc) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eee4`](#insn-00b9eee4) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eeec`](#insn-00b9eeec) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eef0`](#insn-00b9eef0) → [`00b9ef24`](#insn-00b9ef24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef00`](#insn-00b9ef00) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef04`](#insn-00b9ef04) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef10`](#insn-00b9ef10) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef20`](#insn-00b9ef20) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef28`](#insn-00b9ef28) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef30`](#insn-00b9ef30) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef34`](#insn-00b9ef34) → [`00b9ef68`](#insn-00b9ef68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef44`](#insn-00b9ef44) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef48`](#insn-00b9ef48) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef54`](#insn-00b9ef54) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef64`](#insn-00b9ef64) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef6c`](#insn-00b9ef6c) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef74`](#insn-00b9ef74) → [`00b9efd8`](#insn-00b9efd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef78`](#insn-00b9ef78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef8c`](#insn-00b9ef8c) → [`00b9ef9c`](#insn-00b9ef9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef90`](#insn-00b9ef90) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef98`](#insn-00b9ef98) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ef9c`](#insn-00b9ef9c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9efac`](#insn-00b9efac) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9efb8`](#insn-00b9efb8) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9efc4`](#insn-00b9efc4) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9efd4`](#insn-00b9efd4) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9efdc`](#insn-00b9efdc) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9efe0`](#insn-00b9efe0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eff0`](#insn-00b9eff0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9eff4`](#insn-00b9eff4) → [`00b9f064`](#insn-00b9f064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f004`](#insn-00b9f004) → [`00b9f014`](#insn-00b9f014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f008`](#insn-00b9f008) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f010`](#insn-00b9f010) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f014`](#insn-00b9f014) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f024`](#insn-00b9f024) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f030`](#insn-00b9f030) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f034`](#insn-00b9f034) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f044`](#insn-00b9f044) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f058`](#insn-00b9f058) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f060`](#insn-00b9f060) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f06c`](#insn-00b9f06c) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f074`](#insn-00b9f074) → [`00b9f0c0`](#insn-00b9f0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f090`](#insn-00b9f090) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f098`](#insn-00b9f098) → [`00c5c5b0`](../00c5c/00c5c5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c5b0` · 推定シンボル `None` · 推定型 `None`
- [`00b9f09c`](#insn-00b9f09c) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0b0`](#insn-00b9f0b0) → [`00b9f084`](#insn-00b9f084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0b4`](#insn-00b9f0b4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0c0`](#insn-00b9f0c0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0d0`](#insn-00b9f0d0) → [`00b9f350`](#insn-00b9f350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0d8`](#insn-00b9f0d8) → [`00b9f13c`](#insn-00b9f13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0dc`](#insn-00b9f0dc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0f0`](#insn-00b9f0f0) → [`00b9f100`](#insn-00b9f100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0f4`](#insn-00b9f0f4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f0fc`](#insn-00b9f0fc) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f100`](#insn-00b9f100) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f110`](#insn-00b9f110) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f11c`](#insn-00b9f11c) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f128`](#insn-00b9f128) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f138`](#insn-00b9f138) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f140`](#insn-00b9f140) → [`00b9f284`](#insn-00b9f284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f144`](#insn-00b9f144) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f154`](#insn-00b9f154) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f158`](#insn-00b9f158) → [`00b9f1c8`](#insn-00b9f1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f168`](#insn-00b9f168) → [`00b9f178`](#insn-00b9f178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f16c`](#insn-00b9f16c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f174`](#insn-00b9f174) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f178`](#insn-00b9f178) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f188`](#insn-00b9f188) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f194`](#insn-00b9f194) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f198`](#insn-00b9f198) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f1a8`](#insn-00b9f1a8) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f1bc`](#insn-00b9f1bc) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f1c4`](#insn-00b9f1c4) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f1d0`](#insn-00b9f1d0) → [`00b9f284`](#insn-00b9f284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f1d8`](#insn-00b9f1d8) → [`00b9f284`](#insn-00b9f284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f1dc`](#insn-00b9f1dc) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f228`](#insn-00b9f228) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f230`](#insn-00b9f230) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f238`](#insn-00b9f238) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f244`](#insn-00b9f244) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f258`](#insn-00b9f258) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f260`](#insn-00b9f260) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f26c`](#insn-00b9f26c) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f274`](#insn-00b9f274) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f280`](#insn-00b9f280) → [`00b9f1fc`](#insn-00b9f1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f284`](#insn-00b9f284) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f28c`](#insn-00b9f28c) → [`00b9f350`](#insn-00b9f350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f294`](#insn-00b9f294) → [`00b9f2c4`](#insn-00b9f2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2a4`](#insn-00b9f2a4) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2a8`](#insn-00b9f2a8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2c0`](#insn-00b9f2c0) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2c8`](#insn-00b9f2c8) → [`00b9f350`](#insn-00b9f350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2d0`](#insn-00b9f2d0) → [`00b9f314`](#insn-00b9f314) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2e0`](#insn-00b9f2e0) → [`00b9f2f0`](#insn-00b9f2f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2e4`](#insn-00b9f2e4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2ec`](#insn-00b9f2ec) → [`00b9ec0c`](#insn-00b9ec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f2f0`](#insn-00b9f2f0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f300`](#insn-00b9f300) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f30c`](#insn-00b9f30c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f310`](#insn-00b9f310) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f318`](#insn-00b9f318) → [`00b9f350`](#insn-00b9f350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f320`](#insn-00b9f320) → [`00b9f350`](#insn-00b9f350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f330`](#insn-00b9f330) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f334`](#insn-00b9f334) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f34c`](#insn-00b9f34c) → [`00b9ec10`](#insn-00b9ec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9f360`](#insn-00b9f360) → [`00b9ec10`](#insn-00b9ec10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b9eaf0`](#insn-00b9eaf0)

~~~json
{
  "source": "00b9eaf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eaf4`](#insn-00b9eaf4)

~~~json
{
  "source": "00b9eaf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eaf8`](#insn-00b9eaf8)

~~~json
{
  "source": "00b9eaf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb10`](#insn-00b9eb10)

~~~json
{
  "source": "00b9eb10",
  "target": "00b9eb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb18`](#insn-00b9eb18)

~~~json
{
  "source": "00b9eb18",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb28`](#insn-00b9eb28)

~~~json
{
  "source": "00b9eb28",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb34`](#insn-00b9eb34)

~~~json
{
  "source": "00b9eb34",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb54`](#insn-00b9eb54)

~~~json
{
  "source": "00b9eb54",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb60`](#insn-00b9eb60)

~~~json
{
  "source": "00b9eb60",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb68`](#insn-00b9eb68)

~~~json
{
  "source": "00b9eb68",
  "target": "00b9eb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb70`](#insn-00b9eb70)

~~~json
{
  "source": "00b9eb70",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb7c`](#insn-00b9eb7c)

~~~json
{
  "source": "00b9eb7c",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb84`](#insn-00b9eb84)

~~~json
{
  "source": "00b9eb84",
  "target": "00b9eb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb8c`](#insn-00b9eb8c)

~~~json
{
  "source": "00b9eb8c",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb90`](#insn-00b9eb90)

~~~json
{
  "source": "00b9eb90",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eb9c`](#insn-00b9eb9c)

~~~json
{
  "source": "00b9eb9c",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eba4`](#insn-00b9eba4)

~~~json
{
  "source": "00b9eba4",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebb8`](#insn-00b9ebb8)

~~~json
{
  "source": "00b9ebb8",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebc0`](#insn-00b9ebc0)

~~~json
{
  "source": "00b9ebc0",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebcc`](#insn-00b9ebcc)

~~~json
{
  "source": "00b9ebcc",
  "target": "00b9ebe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebd8`](#insn-00b9ebd8)

~~~json
{
  "source": "00b9ebd8",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebe0`](#insn-00b9ebe0)

~~~json
{
  "source": "00b9ebe0",
  "target": "00b9ebf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebe4`](#insn-00b9ebe4)

~~~json
{
  "source": "00b9ebe4",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebec`](#insn-00b9ebec)

~~~json
{
  "source": "00b9ebec",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ebf8`](#insn-00b9ebf8)

~~~json
{
  "source": "00b9ebf8",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec08`](#insn-00b9ec08)

~~~json
{
  "source": "00b9ec08",
  "target": "00b9ec24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec10`](#insn-00b9ec10)

~~~json
{
  "source": "00b9ec10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec14`](#insn-00b9ec14)

~~~json
{
  "source": "00b9ec14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec18`](#insn-00b9ec18)

~~~json
{
  "source": "00b9ec18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec30`](#insn-00b9ec30)

~~~json
{
  "source": "00b9ec30",
  "target": "00b9ec58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec3c`](#insn-00b9ec3c)

~~~json
{
  "source": "00b9ec3c",
  "target": "00b9ec94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec48`](#insn-00b9ec48)

~~~json
{
  "source": "00b9ec48",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec50`](#insn-00b9ec50)

~~~json
{
  "source": "00b9ec50",
  "target": "00b9ec9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec54`](#insn-00b9ec54)

~~~json
{
  "source": "00b9ec54",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec5c`](#insn-00b9ec5c)

~~~json
{
  "source": "00b9ec5c",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec60`](#insn-00b9ec60)

~~~json
{
  "source": "00b9ec60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec68`](#insn-00b9ec68)

~~~json
{
  "source": "00b9ec68",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec74`](#insn-00b9ec74)

~~~json
{
  "source": "00b9ec74",
  "target": "00b9ecf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec78`](#insn-00b9ec78)

~~~json
{
  "source": "00b9ec78",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec84`](#insn-00b9ec84)

~~~json
{
  "source": "00b9ec84",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec8c`](#insn-00b9ec8c)

~~~json
{
  "source": "00b9ec8c",
  "target": "00b9ecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec90`](#insn-00b9ec90)

~~~json
{
  "source": "00b9ec90",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ec98`](#insn-00b9ec98)

~~~json
{
  "source": "00b9ec98",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ecac`](#insn-00b9ecac)

~~~json
{
  "source": "00b9ecac",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ecc0`](#insn-00b9ecc0)

~~~json
{
  "source": "00b9ecc0",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ecc8`](#insn-00b9ecc8)

~~~json
{
  "source": "00b9ecc8",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ecd4`](#insn-00b9ecd4)

~~~json
{
  "source": "00b9ecd4",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ece0`](#insn-00b9ece0)

~~~json
{
  "source": "00b9ece0",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ecec`](#insn-00b9ecec)

~~~json
{
  "source": "00b9ecec",
  "target": "00b9ec60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ecf0`](#insn-00b9ecf0)

~~~json
{
  "source": "00b9ecf0",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ecf8`](#insn-00b9ecf8)

~~~json
{
  "source": "00b9ecf8",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed04`](#insn-00b9ed04)

~~~json
{
  "source": "00b9ed04",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed10`](#insn-00b9ed10)

~~~json
{
  "source": "00b9ed10",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed14`](#insn-00b9ed14)

~~~json
{
  "source": "00b9ed14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed24`](#insn-00b9ed24)

~~~json
{
  "source": "00b9ed24",
  "target": "00b9ed44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed28`](#insn-00b9ed28)

~~~json
{
  "source": "00b9ed28",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed2c`](#insn-00b9ed2c)

~~~json
{
  "source": "00b9ed2c",
  "target": "00c5c540",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b9ed30`](#insn-00b9ed30)

~~~json
{
  "source": "00b9ed30",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed34`](#insn-00b9ed34)

~~~json
{
  "source": "00b9ed34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed40`](#insn-00b9ed40)

~~~json
{
  "source": "00b9ed40",
  "target": "00b9ed48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed48`](#insn-00b9ed48)

~~~json
{
  "source": "00b9ed48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed58`](#insn-00b9ed58)

~~~json
{
  "source": "00b9ed58",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed60`](#insn-00b9ed60)

~~~json
{
  "source": "00b9ed60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed64`](#insn-00b9ed64)

~~~json
{
  "source": "00b9ed64",
  "target": "00b9eda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed74`](#insn-00b9ed74)

~~~json
{
  "source": "00b9ed74",
  "target": "00b9ed84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed78`](#insn-00b9ed78)

~~~json
{
  "source": "00b9ed78",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed80`](#insn-00b9ed80)

~~~json
{
  "source": "00b9ed80",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed84`](#insn-00b9ed84)

~~~json
{
  "source": "00b9ed84",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ed94`](#insn-00b9ed94)

~~~json
{
  "source": "00b9ed94",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eda0`](#insn-00b9eda0)

~~~json
{
  "source": "00b9eda0",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eda8`](#insn-00b9eda8)

~~~json
{
  "source": "00b9eda8",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edb0`](#insn-00b9edb0)

~~~json
{
  "source": "00b9edb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edb4`](#insn-00b9edb4)

~~~json
{
  "source": "00b9edb4",
  "target": "00b9edf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edc4`](#insn-00b9edc4)

~~~json
{
  "source": "00b9edc4",
  "target": "00b9edd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edc8`](#insn-00b9edc8)

~~~json
{
  "source": "00b9edc8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edd0`](#insn-00b9edd0)

~~~json
{
  "source": "00b9edd0",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edd4`](#insn-00b9edd4)

~~~json
{
  "source": "00b9edd4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ede4`](#insn-00b9ede4)

~~~json
{
  "source": "00b9ede4",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edf0`](#insn-00b9edf0)

~~~json
{
  "source": "00b9edf0",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9edf8`](#insn-00b9edf8)

~~~json
{
  "source": "00b9edf8",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee00`](#insn-00b9ee00)

~~~json
{
  "source": "00b9ee00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee04`](#insn-00b9ee04)

~~~json
{
  "source": "00b9ee04",
  "target": "00b9ee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee18`](#insn-00b9ee18)

~~~json
{
  "source": "00b9ee18",
  "target": "00b9ee28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee1c`](#insn-00b9ee1c)

~~~json
{
  "source": "00b9ee1c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee24`](#insn-00b9ee24)

~~~json
{
  "source": "00b9ee24",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee28`](#insn-00b9ee28)

~~~json
{
  "source": "00b9ee28",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee38`](#insn-00b9ee38)

~~~json
{
  "source": "00b9ee38",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee44`](#insn-00b9ee44)

~~~json
{
  "source": "00b9ee44",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee4c`](#insn-00b9ee4c)

~~~json
{
  "source": "00b9ee4c",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee54`](#insn-00b9ee54)

~~~json
{
  "source": "00b9ee54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee58`](#insn-00b9ee58)

~~~json
{
  "source": "00b9ee58",
  "target": "00b9ee9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee6c`](#insn-00b9ee6c)

~~~json
{
  "source": "00b9ee6c",
  "target": "00b9ee7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee70`](#insn-00b9ee70)

~~~json
{
  "source": "00b9ee70",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee78`](#insn-00b9ee78)

~~~json
{
  "source": "00b9ee78",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee7c`](#insn-00b9ee7c)

~~~json
{
  "source": "00b9ee7c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee8c`](#insn-00b9ee8c)

~~~json
{
  "source": "00b9ee8c",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ee98`](#insn-00b9ee98)

~~~json
{
  "source": "00b9ee98",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eea0`](#insn-00b9eea0)

~~~json
{
  "source": "00b9eea0",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eea8`](#insn-00b9eea8)

~~~json
{
  "source": "00b9eea8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eeac`](#insn-00b9eeac)

~~~json
{
  "source": "00b9eeac",
  "target": "00b9eee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eebc`](#insn-00b9eebc)

~~~json
{
  "source": "00b9eebc",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eec0`](#insn-00b9eec0)

~~~json
{
  "source": "00b9eec0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eecc`](#insn-00b9eecc)

~~~json
{
  "source": "00b9eecc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eedc`](#insn-00b9eedc)

~~~json
{
  "source": "00b9eedc",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eee4`](#insn-00b9eee4)

~~~json
{
  "source": "00b9eee4",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eeec`](#insn-00b9eeec)

~~~json
{
  "source": "00b9eeec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eef0`](#insn-00b9eef0)

~~~json
{
  "source": "00b9eef0",
  "target": "00b9ef24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef00`](#insn-00b9ef00)

~~~json
{
  "source": "00b9ef00",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef04`](#insn-00b9ef04)

~~~json
{
  "source": "00b9ef04",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef10`](#insn-00b9ef10)

~~~json
{
  "source": "00b9ef10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef20`](#insn-00b9ef20)

~~~json
{
  "source": "00b9ef20",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef28`](#insn-00b9ef28)

~~~json
{
  "source": "00b9ef28",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef30`](#insn-00b9ef30)

~~~json
{
  "source": "00b9ef30",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef34`](#insn-00b9ef34)

~~~json
{
  "source": "00b9ef34",
  "target": "00b9ef68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef44`](#insn-00b9ef44)

~~~json
{
  "source": "00b9ef44",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef48`](#insn-00b9ef48)

~~~json
{
  "source": "00b9ef48",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef54`](#insn-00b9ef54)

~~~json
{
  "source": "00b9ef54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef64`](#insn-00b9ef64)

~~~json
{
  "source": "00b9ef64",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef6c`](#insn-00b9ef6c)

~~~json
{
  "source": "00b9ef6c",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef74`](#insn-00b9ef74)

~~~json
{
  "source": "00b9ef74",
  "target": "00b9efd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef78`](#insn-00b9ef78)

~~~json
{
  "source": "00b9ef78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef8c`](#insn-00b9ef8c)

~~~json
{
  "source": "00b9ef8c",
  "target": "00b9ef9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef90`](#insn-00b9ef90)

~~~json
{
  "source": "00b9ef90",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef98`](#insn-00b9ef98)

~~~json
{
  "source": "00b9ef98",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ef9c`](#insn-00b9ef9c)

~~~json
{
  "source": "00b9ef9c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9efac`](#insn-00b9efac)

~~~json
{
  "source": "00b9efac",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9efb8`](#insn-00b9efb8)

~~~json
{
  "source": "00b9efb8",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9efc4`](#insn-00b9efc4)

~~~json
{
  "source": "00b9efc4",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9efd4`](#insn-00b9efd4)

~~~json
{
  "source": "00b9efd4",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9efdc`](#insn-00b9efdc)

~~~json
{
  "source": "00b9efdc",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9efe0`](#insn-00b9efe0)

~~~json
{
  "source": "00b9efe0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eff0`](#insn-00b9eff0)

~~~json
{
  "source": "00b9eff0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9eff4`](#insn-00b9eff4)

~~~json
{
  "source": "00b9eff4",
  "target": "00b9f064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f004`](#insn-00b9f004)

~~~json
{
  "source": "00b9f004",
  "target": "00b9f014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f008`](#insn-00b9f008)

~~~json
{
  "source": "00b9f008",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f010`](#insn-00b9f010)

~~~json
{
  "source": "00b9f010",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f014`](#insn-00b9f014)

~~~json
{
  "source": "00b9f014",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f024`](#insn-00b9f024)

~~~json
{
  "source": "00b9f024",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f030`](#insn-00b9f030)

~~~json
{
  "source": "00b9f030",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f034`](#insn-00b9f034)

~~~json
{
  "source": "00b9f034",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f044`](#insn-00b9f044)

~~~json
{
  "source": "00b9f044",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f058`](#insn-00b9f058)

~~~json
{
  "source": "00b9f058",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f060`](#insn-00b9f060)

~~~json
{
  "source": "00b9f060",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f06c`](#insn-00b9f06c)

~~~json
{
  "source": "00b9f06c",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f074`](#insn-00b9f074)

~~~json
{
  "source": "00b9f074",
  "target": "00b9f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f090`](#insn-00b9f090)

~~~json
{
  "source": "00b9f090",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f098`](#insn-00b9f098)

~~~json
{
  "source": "00b9f098",
  "target": "00c5c5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b9f09c`](#insn-00b9f09c)

~~~json
{
  "source": "00b9f09c",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0b0`](#insn-00b9f0b0)

~~~json
{
  "source": "00b9f0b0",
  "target": "00b9f084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0b4`](#insn-00b9f0b4)

~~~json
{
  "source": "00b9f0b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0c0`](#insn-00b9f0c0)

~~~json
{
  "source": "00b9f0c0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0d0`](#insn-00b9f0d0)

~~~json
{
  "source": "00b9f0d0",
  "target": "00b9f350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0d8`](#insn-00b9f0d8)

~~~json
{
  "source": "00b9f0d8",
  "target": "00b9f13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0dc`](#insn-00b9f0dc)

~~~json
{
  "source": "00b9f0dc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0f0`](#insn-00b9f0f0)

~~~json
{
  "source": "00b9f0f0",
  "target": "00b9f100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0f4`](#insn-00b9f0f4)

~~~json
{
  "source": "00b9f0f4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f0fc`](#insn-00b9f0fc)

~~~json
{
  "source": "00b9f0fc",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f100`](#insn-00b9f100)

~~~json
{
  "source": "00b9f100",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f110`](#insn-00b9f110)

~~~json
{
  "source": "00b9f110",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f11c`](#insn-00b9f11c)

~~~json
{
  "source": "00b9f11c",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f128`](#insn-00b9f128)

~~~json
{
  "source": "00b9f128",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f138`](#insn-00b9f138)

~~~json
{
  "source": "00b9f138",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f140`](#insn-00b9f140)

~~~json
{
  "source": "00b9f140",
  "target": "00b9f284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f144`](#insn-00b9f144)

~~~json
{
  "source": "00b9f144",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f154`](#insn-00b9f154)

~~~json
{
  "source": "00b9f154",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f158`](#insn-00b9f158)

~~~json
{
  "source": "00b9f158",
  "target": "00b9f1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f168`](#insn-00b9f168)

~~~json
{
  "source": "00b9f168",
  "target": "00b9f178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f16c`](#insn-00b9f16c)

~~~json
{
  "source": "00b9f16c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f174`](#insn-00b9f174)

~~~json
{
  "source": "00b9f174",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f178`](#insn-00b9f178)

~~~json
{
  "source": "00b9f178",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f188`](#insn-00b9f188)

~~~json
{
  "source": "00b9f188",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f194`](#insn-00b9f194)

~~~json
{
  "source": "00b9f194",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f198`](#insn-00b9f198)

~~~json
{
  "source": "00b9f198",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f1a8`](#insn-00b9f1a8)

~~~json
{
  "source": "00b9f1a8",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f1bc`](#insn-00b9f1bc)

~~~json
{
  "source": "00b9f1bc",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f1c4`](#insn-00b9f1c4)

~~~json
{
  "source": "00b9f1c4",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f1d0`](#insn-00b9f1d0)

~~~json
{
  "source": "00b9f1d0",
  "target": "00b9f284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f1d8`](#insn-00b9f1d8)

~~~json
{
  "source": "00b9f1d8",
  "target": "00b9f284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f1dc`](#insn-00b9f1dc)

~~~json
{
  "source": "00b9f1dc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f228`](#insn-00b9f228)

~~~json
{
  "source": "00b9f228",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f230`](#insn-00b9f230)

~~~json
{
  "source": "00b9f230",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f238`](#insn-00b9f238)

~~~json
{
  "source": "00b9f238",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f244`](#insn-00b9f244)

~~~json
{
  "source": "00b9f244",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f258`](#insn-00b9f258)

~~~json
{
  "source": "00b9f258",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f260`](#insn-00b9f260)

~~~json
{
  "source": "00b9f260",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f26c`](#insn-00b9f26c)

~~~json
{
  "source": "00b9f26c",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f274`](#insn-00b9f274)

~~~json
{
  "source": "00b9f274",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f280`](#insn-00b9f280)

~~~json
{
  "source": "00b9f280",
  "target": "00b9f1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f284`](#insn-00b9f284)

~~~json
{
  "source": "00b9f284",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f28c`](#insn-00b9f28c)

~~~json
{
  "source": "00b9f28c",
  "target": "00b9f350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f294`](#insn-00b9f294)

~~~json
{
  "source": "00b9f294",
  "target": "00b9f2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2a4`](#insn-00b9f2a4)

~~~json
{
  "source": "00b9f2a4",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2a8`](#insn-00b9f2a8)

~~~json
{
  "source": "00b9f2a8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2c0`](#insn-00b9f2c0)

~~~json
{
  "source": "00b9f2c0",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2c8`](#insn-00b9f2c8)

~~~json
{
  "source": "00b9f2c8",
  "target": "00b9f350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2d0`](#insn-00b9f2d0)

~~~json
{
  "source": "00b9f2d0",
  "target": "00b9f314",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2e0`](#insn-00b9f2e0)

~~~json
{
  "source": "00b9f2e0",
  "target": "00b9f2f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2e4`](#insn-00b9f2e4)

~~~json
{
  "source": "00b9f2e4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2ec`](#insn-00b9f2ec)

~~~json
{
  "source": "00b9f2ec",
  "target": "00b9ec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f2f0`](#insn-00b9f2f0)

~~~json
{
  "source": "00b9f2f0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f300`](#insn-00b9f300)

~~~json
{
  "source": "00b9f300",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f30c`](#insn-00b9f30c)

~~~json
{
  "source": "00b9f30c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f310`](#insn-00b9f310)

~~~json
{
  "source": "00b9f310",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f318`](#insn-00b9f318)

~~~json
{
  "source": "00b9f318",
  "target": "00b9f350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f320`](#insn-00b9f320)

~~~json
{
  "source": "00b9f320",
  "target": "00b9f350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f330`](#insn-00b9f330)

~~~json
{
  "source": "00b9f330",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f334`](#insn-00b9f334)

~~~json
{
  "source": "00b9f334",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f34c`](#insn-00b9f34c)

~~~json
{
  "source": "00b9f34c",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9f360`](#insn-00b9f360)

~~~json
{
  "source": "00b9f360",
  "target": "00b9ec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
