# 00bc0eec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc0eec",
  "name": "_ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 3408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54fae74135d323a0581958b38815605fb16cacce38670cc54567140c082649a7",
  "source_text_sha256": "54fae74135d323a0581958b38815605fb16cacce38670cc54567140c082649a7"
}
~~~

## 呼び出し元

- [00c5e590](../00c5e/00c5e590.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 41269 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  uint *puVar3;
  uint *puVar4;
  ushort uVar5;
  int iVar6;
  long lVar7;
  ulong uVar8;
  ulong uVar9;
  long lVar10;
  ulong uVar11;
  ulong uVar12;
  ulong uVar13;
  ulong uVar14;
  ushort *puVar15;
  
  lVar10 = *param_2;
  uVar13 = (long)param_1 - lVar10;
  if (((uVar13 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar11 = param_2[1];
                    /* try { // try from 00bc0f14 to 00cc0f1b has its CatchHandler @ 00bc13b4 */
    if (uVar11 < 5) {
      return 0;
    }
    uVar12 = uVar11 - 4;
                    /* try { // try from 00bc0f1c to 00cc0f2b has its CatchHandler @ 00bc12fc */
    if (uVar12 < uVar13) {
      return 0;
    }
    lVar7 = param_2[7];
                    /* try { // try from 00bc0f2c to 00cc0f57 has its CatchHandler @ 00bc12e4 */
    iVar6 = *param_1;
    uVar1 = (int)lVar7 + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
                    /* try { // try from 00bc0f58 to 00cc0ffb has its CatchHandler @ 00bc0b0c */
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar14 = uVar13 - (long)iVar6, (uVar14 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar14 <= uVar11 - 2)) {
      uVar5 = *(ushort *)(lVar10 + uVar14);
      if ((((uVar5 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar5 & 1) == 0)) {
        if (uVar11 <= uVar5) {
          return 0;
        }
        if (uVar11 - uVar5 < uVar14) {
          return 0;
        }
        puVar15 = (ushort *)((long)param_1 - (long)*param_1);
        uVar5 = *puVar15;
        if (4 < uVar5) {
          if ((ulong)puVar15[2] != 0) {
            uVar14 = uVar13 + puVar15[2];
            if ((uVar14 & 3) == 0) {
              if (uVar12 < uVar14) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar12 < uVar14) {
                return 0;
              }
            }
            if ((int)*(uint *)(lVar10 + uVar14) < 1) {
              return 0;
            }
            if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
              return 0;
            }
          }
                    /* try { // try from 00bc0ffc to 00cc1007 has its CatchHandler @ 00bc12e0 */
                    /* try { // try from 00bc1008 to 00cc11ff has its CatchHandler @ 00bc0b0c */
          if (((ulong)puVar15[2] != 0) &&
             (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[2]),
             puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
            uVar14 = (long)puVar3 - lVar10;
            if ((uVar14 & 3) == 0) {
              if (uVar12 < uVar14) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar12 < uVar14) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar3) {
              return 0;
            }
            uVar8 = (ulong)*puVar3 + 4;
            if (uVar11 - 1 < uVar8 + uVar14) {
              return 0;
            }
            if (uVar11 <= uVar8) {
              return 0;
            }
            if (uVar11 - uVar8 < uVar14) {
              return 0;
            }
            if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
              return 0;
            }
          }
          if (6 < uVar5) {
            if ((ulong)puVar15[3] != 0) {
              uVar14 = uVar13 + puVar15[3];
              if ((uVar14 & 3) == 0) {
                if (uVar12 < uVar14) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar12 < uVar14) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                return 0;
              }
              if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                return 0;
              }
            }
            if (((ulong)puVar15[3] != 0) &&
               (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[3]),
               puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
              uVar14 = (long)puVar3 - lVar10;
              if ((uVar14 & 3) == 0) {
                if (uVar12 < uVar14) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar12 < uVar14) {
                  return 0;
                }
              }
              if ((ulong)param_2[4] <= (ulong)*puVar3) {
                return 0;
              }
              uVar8 = (ulong)*puVar3 + 4;
              if (uVar11 - 1 < uVar8 + uVar14) {
                return 0;
              }
              if (uVar11 <= uVar8) {
                return 0;
              }
              if (uVar11 - uVar8 < uVar14) {
                return 0;
              }
              if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                return 0;
              }
            }
            if (8 < uVar5) {
              if ((ulong)puVar15[4] != 0) {
                uVar14 = uVar13 + puVar15[4];
                if ((uVar14 & 3) == 0) {
                  if (uVar12 < uVar14) {
                    return 0;
                  }
                }
                else {
                  if ((char)param_2[3] != '\0') {
                    return 0;
                  }
                  if (uVar12 < uVar14) {
                    return 0;
                  }
                }
                if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                  return 0;
                }
                if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                  return 0;
                }
              }
              if (((ulong)puVar15[4] != 0) &&
                 (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[4]),
                 puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
                uVar14 = (long)puVar3 - lVar10;
                if ((uVar14 & 3) == 0) {
                  if (uVar12 < uVar14) {
                    return 0;
                  }
                }
                else {
                  if ((char)param_2[3] != '\0') {
                    return 0;
                  }
                  if (uVar12 < uVar14) {
                    return 0;
                  }
                }
                    /* try { // try from 00bc1200 to 00cc1207 has its CatchHandler @ 00bc13d8 */
                if ((ulong)param_2[4] <= (ulong)*puVar3) {
                  return 0;
                }
                uVar8 = (ulong)*puVar3 + 4;
                if (uVar11 - 1 < uVar8 + uVar14) {
                  return 0;
                }
                if (uVar11 <= uVar8) {
                  return 0;
                }
                if (uVar11 - uVar8 < uVar14) {
                  return 0;
                }
                if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                  return 0;
                }
              }
              if (10 < uVar5) {
                if ((ulong)puVar15[5] != 0) {
                  uVar14 = uVar13 + puVar15[5];
                  if ((uVar14 & 3) == 0) {
                    if (uVar12 < uVar14) {
                      return 0;
                    }
                  }
                  else {
                    if ((char)param_2[3] != '\0') {
                      return 0;
                    }
                    if (uVar12 < uVar14) {
                      return 0;
                    }
                  }
                  if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                    return 0;
                  }
                  if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                    return 0;
                  }
                }
                if (((ulong)puVar15[5] != 0) &&
                   (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[5]),
                   puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
                  uVar14 = (long)puVar3 - lVar10;
                  if ((uVar14 & 3) == 0) {
                    if (uVar12 < uVar14) {
                      return 0;
                    }
                  }
                  else {
                    /* try { // try from 00bc12c0 to 00cc12df has its CatchHandler @ 00bc13b4 */
                    if ((char)param_2[3] != '\0') {
                      return 0;
                    }
                    if (uVar12 < uVar14) {
                      return 0;
                    }
                  }
                    /* catch() { ... } // from try @ 00bc0ffc with catch @ 00bc12e0
                       try { // try from 00bc12e0 to 00cc1407 has its CatchHandler @ 00bc0b0c */
                    /* catch() { ... } // from try @ 00bc0f2c with catch @ 00bc12e4 */
                  if ((ulong)param_2[4] <= (ulong)*puVar3) {
                    return 0;
                  }
                  uVar8 = (ulong)*puVar3 + 4;
                    /* catch() { ... } // from try @ 00bc0f1c with catch @ 00bc12fc */
                  if (uVar11 - 1 < uVar8 + uVar14) {
                    return 0;
                  }
                  if (uVar11 <= uVar8) {
                    return 0;
                  }
                    /* catch() { ... } // from try @ 00bc0e84 with catch @ 00bc1310 */
                  if (uVar11 - uVar8 < uVar14) {
                    return 0;
                  }
                  if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                    return 0;
                  }
                }
                    /* catch() { ... } // from try @ 00bc0dbc with catch @ 00bc1320 */
                if (0xc < uVar5) {
                  if ((ulong)puVar15[6] != 0) {
                    uVar14 = uVar13 + puVar15[6];
                    /* catch() { ... } // from try @ 00bc0dac with catch @ 00bc1338 */
                    if ((uVar14 & 3) == 0) {
                      if (uVar12 < uVar14) {
                        return 0;
                      }
                    }
                    else {
                    /* catch() { ... } // from try @ 00bc0ec0 with catch @ 00bc133c */
                    /* catch() { ... } // from try @ 00bc0d94 with catch @ 00bc1344 */
                      if ((char)param_2[3] != '\0') {
                        return 0;
                      }
                    /* catch() { ... } // from try @ 00bc0cdc with catch @ 00bc134c */
                      if (uVar12 < uVar14) {
                        return 0;
                      }
                    }
                    if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                      return 0;
                    }
                    if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                      return 0;
                    }
                  }
                  if (((ulong)puVar15[6] != 0) &&
                     (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[6]),
                     puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
                    /* catch() { ... } // from try @ 00bc0b9c with catch @ 00bc1390 */
                    uVar14 = (long)puVar3 - lVar10;
                    if ((uVar14 & 3) == 0) {
                    /* catch() { ... } // from try @ 00bc0f14 with catch @ 00bc13b4
                       catch() { ... } // from try @ 00bc12c0 with catch @ 00bc13b4 */
                      if (uVar12 < uVar14) {
                        return 0;
                      }
                    }
                    else {
                      if ((char)param_2[3] != '\0') {
                        return 0;
                      }
                      if (uVar12 < uVar14) {
                        return 0;
                      }
                    }
                    if ((ulong)param_2[4] <= (ulong)*puVar3) {
                      return 0;
                    }
                    uVar8 = (ulong)*puVar3 + 4;
                    /* catch() { ... } // from try @ 00bc0cb0 with catch @ 00bc13d8
                       catch() { ... } // from try @ 00bc1200 with catch @ 00bc13d8 */
                    if (uVar11 - 1 < uVar8 + uVar14) {
                      return 0;
                    }
                    if (uVar11 <= uVar8) {
                      return 0;
                    }
                    if (uVar11 - uVar8 < uVar14) {
                      return 0;
                    }
                    if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                      return 0;
                    }
                  }
                  if (0xe < uVar5) {
                    if ((ulong)puVar15[7] != 0) {
                      uVar14 = uVar13 + puVar15[7];
                      if ((uVar14 & 3) == 0) {
                        if (uVar12 < uVar14) {
                          return 0;
                        }
                      }
                      else {
                        if ((char)param_2[3] != '\0') {
                          return 0;
                        }
                        if (uVar12 < uVar14) {
                          return 0;
                        }
                      }
                      if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                        return 0;
                      }
                      if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                        return 0;
                      }
                    }
                    if (((ulong)puVar15[7] != 0) &&
                       (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[7]),
                       puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
                      uVar14 = (long)puVar3 - lVar10;
                      if ((uVar14 & 3) == 0) {
                        if (uVar12 < uVar14) {
                          return 0;
                        }
                      }
                      else {
                        if ((char)param_2[3] != '\0') {
                          return 0;
                        }
                        if (uVar12 < uVar14) {
                          return 0;
                        }
                      }
                      if ((ulong)param_2[4] <= (ulong)*puVar3) {
                        return 0;
                      }
                      uVar8 = (ulong)*puVar3 + 4;
                    /* try { // try from 00bc14b8 to 00cc1503 has its CatchHandler @ 00bc14b8
                       catch() { ... } // from try @ 00bc14b8 with catch @ 00bc14b8
                       catch() { ... } // from try @ 00bc150c with catch @ 00bc14b8
                       catch() { ... } // from try @ 00bc1588 with catch @ 00bc14b8
                       catch() { ... } // from try @ 00bc1630 with catch @ 00bc14b8
                       catch() { ... } // from try @ 00bc16a4 with catch @ 00bc14b8
                       catch() { ... } // from try @ 00bc17ac with catch @ 00bc14b8 */
                      if (uVar11 - 1 < uVar8 + uVar14) {
                        return 0;
                      }
                      if (uVar11 <= uVar8) {
                        return 0;
                      }
                      if (uVar11 - uVar8 < uVar14) {
                        return 0;
                      }
                      if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                        return 0;
                      }
                    }
                    if (0x10 < uVar5) {
                      if ((ulong)puVar15[8] != 0) {
                        uVar14 = uVar13 + puVar15[8];
                        if ((uVar14 & 3) == 0) {
                          if (uVar12 < uVar14) {
                            return 0;
                          }
                        }
                        else {
                    /* try { // try from 00bc1504 to 00cc150b has its CatchHandler @ 00bc1938 */
                          if ((char)param_2[3] != '\0') {
                            return 0;
                          }
                    /* try { // try from 00bc150c to 00cc157b has its CatchHandler @ 00bc14b8 */
                          if (uVar12 < uVar14) {
                            return 0;
                          }
                        }
                        if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                          return 0;
                        }
                        if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                          return 0;
                        }
                      }
                      if (((ulong)puVar15[8] != 0) &&
                         (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[8]),
                         puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
                        uVar14 = (long)puVar3 - lVar10;
                        if ((uVar14 & 3) == 0) {
                          if (uVar12 < uVar14) {
                            return 0;
                          }
                        }
                        else {
                          if ((char)param_2[3] != '\0') {
                            return 0;
                          }
                          if (uVar12 < uVar14) {
                            return 0;
                          }
                        }
                    /* try { // try from 00bc157c to 00cc1587 has its CatchHandler @ 00bc1900 */
                    /* try { // try from 00bc1588 to 00cc161b has its CatchHandler @ 00bc14b8 */
                        if ((ulong)param_2[4] <= (ulong)*puVar3) {
                          return 0;
                        }
                        uVar8 = (ulong)*puVar3 + 4;
                        if (uVar11 - 1 < uVar8 + uVar14) {
                          return 0;
                        }
                        if (uVar11 <= uVar8) {
                          return 0;
                        }
                        if (uVar11 - uVar8 < uVar14) {
                          return 0;
                        }
                        if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                          return 0;
                        }
                      }
                      if (0x12 < uVar5) {
                        if ((ulong)puVar15[9] != 0) {
                          uVar14 = uVar13 + puVar15[9];
                          if ((uVar14 & 3) == 0) {
                            if (uVar12 < uVar14) {
                              return 0;
                            }
                          }
                          else {
                            if ((char)param_2[3] != '\0') {
                              return 0;
                            }
                            if (uVar12 < uVar14) {
                              return 0;
                            }
                          }
                          if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                            return 0;
                          }
                          if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                            return 0;
                          }
                        }
                    /* try { // try from 00bc161c to 00cc162f has its CatchHandler @ 00bc18fc */
                        if (((ulong)puVar15[9] != 0) &&
                           (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[9]),
                           puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0))
                        {
                    /* try { // try from 00bc1630 to 00cc168f has its CatchHandler @ 00bc14b8 */
                          uVar14 = (long)puVar3 - lVar10;
                          if ((uVar14 & 3) == 0) {
                            if (uVar12 < uVar14) {
                              return 0;
                            }
                          }
                          else {
                            if ((char)param_2[3] != '\0') {
                              return 0;
                            }
                            if (uVar12 < uVar14) {
                              return 0;
                            }
                          }
                          if ((ulong)param_2[4] <= (ulong)*puVar3) {
                            return 0;
                          }
                          uVar8 = (ulong)*puVar3 + 4;
                          if (uVar11 - 1 < uVar8 + uVar14) {
                            return 0;
                          }
                          if (uVar11 <= uVar8) {
                            return 0;
                          }
                    /* try { // try from 00bc1690 to 00cc16a3 has its CatchHandler @ 00bc18f8 */
                          if (uVar11 - uVar8 < uVar14) {
                            return 0;
                          }
                          if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                            return 0;
                          }
                        }
                    /* try { // try from 00bc16a4 to 00cc1743 has its CatchHandler @ 00bc14b8 */
                        if (0x14 < uVar5) {
                          if ((ulong)puVar15[10] != 0) {
                            uVar14 = uVar13 + puVar15[10];
                            if ((uVar14 & 3) == 0) {
                              if (uVar12 < uVar14) {
                                return 0;
                              }
                            }
                            else {
                              if ((char)param_2[3] != '\0') {
                                return 0;
                              }
                              if (uVar12 < uVar14) {
                                return 0;
                              }
                            }
                            if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                              return 0;
                            }
                            if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                              return 0;
                            }
                          }
                          if (((ulong)puVar15[10] != 0) &&
                             (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[10]),
                             puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0
                             )) {
                            uVar14 = (long)puVar3 - lVar10;
                            if ((uVar14 & 3) == 0) {
                              if (uVar12 < uVar14) {
                                return 0;
                              }
                            }
                            else {
                              if ((char)param_2[3] != '\0') {
                                return 0;
                              }
                              if (uVar12 < uVar14) {
                                return 0;
                              }
                            }
                    /* try { // try from 00bc1744 to 00cc174b has its CatchHandler @ 00bc18e8 */
                            if ((ulong)param_2[4] <= (ulong)*puVar3) {
                              return 0;
                            }
                            uVar8 = (ulong)*puVar3 + 4;
                            if (uVar11 - 1 < uVar8 + uVar14) {
                              return 0;
                            }
                            if (uVar11 <= uVar8) {
                              return 0;
                            }
                            if (uVar11 - uVar8 < uVar14) {
                              return 0;
                            }
                            if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                              return 0;
                            }
                          }
                          if (0x16 < uVar5) {
                    /* try { // try from 00bc178c to 00cc17ab has its CatchHandler @ 00bc18a8 */
                            if ((ulong)puVar15[0xb] != 0) {
                              uVar14 = uVar13 + puVar15[0xb];
                              if ((uVar14 & 3) == 0) {
                                if (uVar12 < uVar14) {
                                  return 0;
                                }
                              }
                              else {
                                if ((char)param_2[3] != '\0') {
                                  return 0;
                                }
                    /* try { // try from 00bc17ac to 00cc195f has its CatchHandler @ 00bc14b8 */
                                if (uVar12 < uVar14) {
                                  return 0;
                                }
                              }
                              if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                                return 0;
                              }
                              if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                                return 0;
                              }
                            }
                            if ((ulong)puVar15[0xb] != 0) {
                              puVar4 = (uint *)((long)param_1 + (ulong)puVar15[0xb]);
                              puVar3 = (uint *)((long)puVar4 + (ulong)*puVar4);
                              if (puVar3 != (uint *)0x0) {
                                uVar14 = (long)puVar3 - lVar10;
                                if ((uVar14 & 3) == 0) {
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                                else {
                                  if ((char)param_2[3] != '\0') {
                                    return 0;
                                  }
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                                if ((ulong)param_2[4] >> 2 <= (ulong)*puVar3) {
                                  return 0;
                                }
                                uVar8 = (ulong)*puVar3 * 4 + 4;
                                if (uVar11 <= uVar8) {
                                  return 0;
                                }
                                if (uVar11 - uVar8 < uVar14) {
                                  return 0;
                                }
                              }
                              puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4);
                              if ((puVar4 != (uint *)0x0) && (*puVar4 != 0)) {
                                uVar14 = 0;
                                do {
                                  puVar3 = (uint *)((long)puVar4 + (uVar14 & 0xfffffffc) + 4);
                                  puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
                                  uVar8 = (long)puVar3 - lVar10;
                                  if ((char)param_2[3] != '\0' && (uVar8 & 3) != 0) {
                                    return 0;
                                  }
                                  if (uVar12 < uVar8) {
                                    return 0;
                                  }
                    /* catch() { ... } // from try @ 00bc178c with catch @ 00bc18a8 */
                                  uVar9 = (ulong)*puVar3;
                                  if ((ulong)param_2[4] <= uVar9) {
                                    return 0;
                                  }
                                  uVar9 = uVar9 + 4;
                                  if (uVar11 - 1 < uVar9 + uVar8) {
                                    return 0;
                                  }
                                  if (uVar11 <= uVar9) {
                                    return 0;
                                  }
                                  if (uVar11 - uVar9 < uVar8) {
                                    return 0;
                                  }
                                  if (*(char *)(lVar10 + uVar9 + uVar8) != '\0') {
                                    return 0;
                                  }
                                  uVar14 = uVar14 + 4;
                    /* catch() { ... } // from try @ 00bc1744 with catch @ 00bc18e8 */
                                } while ((ulong)*puVar4 * 4 - uVar14 != 0);
                              }
                            }
                            if (0x18 < uVar5) {
                    /* catch() { ... } // from try @ 00bc1690 with catch @ 00bc18f8 */
                    /* catch() { ... } // from try @ 00bc161c with catch @ 00bc18fc */
                              if ((ulong)puVar15[0xc] != 0) {
                    /* catch() { ... } // from try @ 00bc157c with catch @ 00bc1900 */
                                uVar14 = uVar13 + puVar15[0xc];
                                if ((uVar14 & 3) == 0) {
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                                else {
                                  if ((char)param_2[3] != '\0') {
                                    return 0;
                                  }
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                                if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                                  return 0;
                                }
                    /* catch() { ... } // from try @ 00bc1504 with catch @ 00bc1938 */
                                if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                                  return 0;
                                }
                              }
                              if (((ulong)puVar15[0xc] != 0) &&
                                 (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[0xc]),
                                 puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3),
                                 puVar3 != (uint *)0x0)) {
                    /* try { // try from 00bc1960 to 00cc1a2f has its CatchHandler @ 00bc1960
                       catch() { ... } // from try @ 00bc1960 with catch @ 00bc1960
                       catch() { ... } // from try @ 00bc1a48 with catch @ 00bc1960 */
                                uVar14 = (long)puVar3 - lVar10;
                                if ((uVar14 & 3) == 0) {
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                                else {
                                  if ((char)param_2[3] != '\0') {
                                    return 0;
                                  }
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                                if ((ulong)param_2[4] <= (ulong)*puVar3) {
                                  return 0;
                                }
                                uVar8 = (ulong)*puVar3 + 4;
                                if (uVar11 - 1 < uVar8 + uVar14) {
                                  return 0;
                                }
                                if (uVar11 <= uVar8) {
                                  return 0;
                                }
                                if (uVar11 - uVar8 < uVar14) {
                                  return 0;
                                }
                                if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                                  return 0;
                                }
                              }
                              if (0x1a < uVar5) {
                                if ((ulong)puVar15[0xd] != 0) {
                                  uVar14 = uVar13 + puVar15[0xd];
                                  if ((uVar14 & 3) == 0) {
                                    if (uVar12 < uVar14) {
                                      return 0;
                                    }
                                  }
                                  else {
                                    if ((char)param_2[3] != '\0') {
                                      return 0;
                                    }
                                    if (uVar12 < uVar14) {
                                      return 0;
                                    }
                                  }
                                  if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                                    return 0;
                                  }
                                  if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                                    return 0;
                                  }
                                }
                                if ((ulong)puVar15[0xd] != 0) {
                    /* try { // try from 00bc1a30 to 00cc1a47 has its CatchHandler @ 00bc1ac0 */
                                  puVar4 = (uint *)((long)param_1 + (ulong)puVar15[0xd]);
                                  puVar3 = (uint *)((long)puVar4 + (ulong)*puVar4);
                                  if (puVar3 != (uint *)0x0) {
                                    uVar14 = (long)puVar3 - lVar10;
                    /* try { // try from 00bc1a48 to 00cc1aff has its CatchHandler @ 00bc1960 */
                                    if ((uVar14 & 3) == 0) {
                                      if (uVar12 < uVar14) {
                                        return 0;
                                      }
                                    }
                                    else {
                                      if ((char)param_2[3] != '\0') {
                                        return 0;
                                      }
                                      if (uVar12 < uVar14) {
                                        return 0;
                                      }
                                    }
                                    if ((ulong)param_2[4] >> 2 <= (ulong)*puVar3) {
                                      return 0;
                                    }
                                    uVar8 = (ulong)*puVar3 * 4 + 4;
                                    if (uVar11 <= uVar8) {
                                      return 0;
                                    }
                                    if (uVar11 - uVar8 < uVar14) {
                                      return 0;
                                    }
                                  }
                                  puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4);
                                  if ((puVar4 != (uint *)0x0) && (*puVar4 != 0)) {
                                    uVar14 = 0;
                                    do {
                    /* catch() { ... } // from try @ 00bc1a30 with catch @ 00bc1ac0 */
                                      puVar3 = (uint *)((long)puVar4 + (uVar14 & 0xfffffffc) + 4);
                                      puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
                                      uVar8 = (long)puVar3 - lVar10;
                                      if ((char)param_2[3] != '\0' && (uVar8 & 3) != 0) {
                                        return 0;
                                      }
                                      if (uVar12 < uVar8) {
                                        return 0;
                                      }
                                      uVar9 = (ulong)*puVar3;
                                      if ((ulong)param_2[4] <= uVar9) {
                                        return 0;
                                      }
                                      uVar9 = uVar9 + 4;
                                      if (uVar11 - 1 < uVar9 + uVar8) {
                                        return 0;
                                      }
                                      if (uVar11 <= uVar9) {
                                        return 0;
                                      }
                                      if (uVar11 - uVar9 < uVar8) {
                                        return 0;
                                      }
                                      if (*(char *)(lVar10 + uVar9 + uVar8) != '\0') {
                                        return 0;
                                      }
                                      uVar14 = uVar14 + 4;
                                    } while ((ulong)*puVar4 * 4 - uVar14 != 0);
                                  }
                                }
                                if (0x1c < uVar5) {
                                  if ((ulong)puVar15[0xe] != 0) {
                                    uVar13 = uVar13 + puVar15[0xe];
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
                                    if ((int)*(uint *)(lVar10 + uVar13) < 1) {
                                      return 0;
                                    }
                                    if (uVar11 - 1 < uVar13 + *(uint *)(lVar10 + uVar13)) {
                                      return 0;
                                    }
                                  }
                                  if (((ulong)puVar15[0xe] != 0) &&
                                     (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[0xe]),
                                     puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3),
                                     puVar3 != (uint *)0x0)) {
                                    uVar13 = (long)puVar3 - lVar10;
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
                                    if ((ulong)param_2[4] <= (ulong)*puVar3) {
                                      return 0;
                                    }
                                    uVar12 = (ulong)*puVar3 + 4;
                                    if (uVar11 - 1 < uVar12 + uVar13) {
                                      return 0;
                                    }
                                    if (uVar11 <= uVar12) {
                                      return 0;
                                    }
                                    if (uVar11 - uVar12 < uVar13) {
                                      return 0;
                                    }
                                    if (*(char *)(lVar10 + uVar12 + uVar13) != '\0') {
                                      return 0;
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
                }
              }
            }
          }
        }
        *(int *)(param_2 + 7) = (int)lVar7;
        return 1;
      }
    }
  }
  return 0;
}

~~~
