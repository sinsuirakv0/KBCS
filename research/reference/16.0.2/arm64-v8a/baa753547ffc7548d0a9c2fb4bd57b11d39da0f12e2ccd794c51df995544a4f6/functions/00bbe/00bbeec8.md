# 00bbeec8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
  "source_text_sha256": "4a304915e7765e133441ae9e15e99f388671a7bae4f58c114aa4888bf9bfd93a"
}
~~~

## 呼び出し元

- [00c5d5b0](../00c5d/00c5d5b0.md)

## 呼び出し先

- [00c5d5c0](../00c5d/00c5d5c0.md)
- [00c5d600](../00c5d/00c5d600.md)

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
