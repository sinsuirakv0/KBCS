# 00bbee2c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bbee2c",
  "name": "_ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 3496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bfb3a66d7a1da0f4851279f5a9f1f6a5cf49fe3bca16f41725c1ee7635d77761",
  "source_text_sha256": "bfb3a66d7a1da0f4851279f5a9f1f6a5cf49fe3bca16f41725c1ee7635d77761"
}
~~~

## 呼び出し元

- [00c5d4e0](../00c5d/00c5d4e0.md)

## 呼び出し先

- [00c5d4f0](../00c5d/00c5d4f0.md)
- [00c5d530](../00c5d/00c5d530.md)

## 疑似コード / UTF-8 30669 bytes

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
              if ((ulong)puVar14[4] != 0) {
                uVar8 = uVar13 + puVar14[4];
                if ((uVar8 & 3) == 0) {
                    /* try { // try from 00bbf0f4 to 00cbf0ff has its CatchHandler @ 00bbf484 */
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
                    /* try { // try from 00bbf124 to 00cbf14b has its CatchHandler @ 00bbf440 */
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
            if (uVar10 - 4 < uVar13) {
              return 0;
            }
            if ((ulong)param_2[4] <= (ulong)*puVar4) {
              return 0;
            }
            uVar12 = (ulong)*puVar4 + 4;
            if (uVar10 <= uVar12) {
              return 0;
            }
                    /* try { // try from 00bbf398 to 00cbf39f has its CatchHandler @ 00bbf3b4 */
            if (uVar10 - uVar12 < uVar13) {
              return 0;
            }
          }
                    /* catch() { ... } // from try @ 00bbec3c with catch @ 00bbf3a0
                       try { // try from 00bbf3a0 to 00cbf4af has its CatchHandler @ 00bbe7f8 */
          if (0xe < uVar6) {
            if ((ulong)puVar14[7] != 0) {
                    /* catch() { ... } // from try @ 00bbec6c with catch @ 00bbf3b0 */
                    /* catch() { ... } // from try @ 00bbf398 with catch @ 00bbf3b4 */
              uVar13 = (long)param_1 + ((ulong)puVar14[7] - *param_2);
                    /* catch() { ... } // from try @ 00bbed34 with catch @ 00bbf3b8 */
              if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                return 0;
              }
              uVar10 = param_2[1];
              if (uVar10 < 5) {
                return 0;
              }
                    /* catch() { ... } // from try @ 00bbec2c with catch @ 00bbf3e0 */
              if (uVar10 - 4 < uVar13) {
                return 0;
              }
                    /* catch() { ... } // from try @ 00bbeb4c with catch @ 00bbf3e4 */
              uVar1 = *(uint *)(*param_2 + uVar13);
              if ((int)uVar1 < 1) {
                return 0;
              }
              if (uVar10 - 1 < uVar13 + uVar1) {
                return 0;
              }
            }
            if (((ulong)puVar14[7] != 0) &&
               (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[7]),
               puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
              uVar13 = (long)puVar4 - *param_2;
                    /* catch() { ... } // from try @ 00bbeb18 with catch @ 00bbf428 */
              if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                return 0;
              }
              uVar10 = param_2[1];
              if (uVar10 < 5) {
                return 0;
              }
                    /* catch() { ... } // from try @ 00bbf124 with catch @ 00bbf440 */
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
                    /* catch() { ... } // from try @ 00bbf0f4 with catch @ 00bbf484 */
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
                    /* try { // try from 00bbf784 to 00cbf94f has its CatchHandler @ 00bbf784
                       catch() { ... } // from try @ 00bbf784 with catch @ 00bbf784
                       catch() { ... } // from try @ 00bbf95c with catch @ 00bbf784 */
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
                          uVar13 = _ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                             (lVar11,param_2);
                          if ((uVar13 & 1) == 0) {
                            return 0;
                          }
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
                    /* try { // try from 00bbf950 to 00cbf95b has its CatchHandler @ 00bbfa78 */
                    /* try { // try from 00bbf95c to 00cbfaa7 has its CatchHandler @ 00bbf784 */
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
                    /* catch() { ... } // from try @ 00bbf950 with catch @ 00bbfa78 */
              if ((ulong)puVar14[0x10] != 0) {
                uVar13 = (long)param_1 + ((ulong)puVar14[0x10] - *param_2);
                if (((uVar13 & 7) != 0) && ((char)param_2[3] != '\0')) {
                  return 0;
                }
                if ((ulong)param_2[1] < 9) {
                  return 0;
                }
                    /* catch() { ... } // from try @ 00bbfb58 with catch @ 00bbfaa8
                       catch() { ... } // from try @ 00bbfc98 with catch @ 00bbfaa8
                       catch() { ... } // from try @ 00bbfd84 with catch @ 00bbfaa8
                       catch() { ... } // from try @ 00bbfef4 with catch @ 00bbfaa8
                       catch() { ... } // from try @ 00bbffa4 with catch @ 00bbfaa8
                       catch() { ... } // from try @ 00bc027c with catch @ 00bbfaa8 */
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
                  if (uVar10 - 1 < uVar13 + uVar1) {
                    return 0;
                  }
                }
                if (((ulong)puVar14[0x11] != 0) &&
                   (puVar4 = (uint *)((long)param_1 + (ulong)puVar14[0x11]),
                   puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
                  uVar13 = (long)puVar4 - *param_2;
                    /* try { // try from 00bbfb38 to 00cbfb57 has its CatchHandler @ 00bc032c */
                  if (((uVar13 & 3) != 0) && ((char)param_2[3] != '\0')) {
                    return 0;
                  }
                  uVar10 = param_2[1];
                  if (uVar10 < 5) {
                    return 0;
                  }
                    /* try { // try from 00bbfb58 to 00cbfc4b has its CatchHandler @ 00bbfaa8 */
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
