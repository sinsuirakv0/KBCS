# 00b9eaec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
  "source_text_sha256": "1eb2cd145dd4472f86d9e1a35191549663587366ce992c4842ab7d7657060f62"
}
~~~

## 呼び出し元

- [00c5c550](../00c5c/00c5c550.md)

## 呼び出し先

- [00c5c540](../00c5c/00c5c540.md)
- [00c5c5b0](../00c5c/00c5c5b0.md)

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
