# 00bbfef8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbfef8",
  "name": "_ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 3408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c72ff5f52184e74fff0f3e35a074e0bd0b5ae1a718ba2a13f15050de4929c423",
  "source_text_sha256": "c72ff5f52184e74fff0f3e35a074e0bd0b5ae1a718ba2a13f15050de4929c423"
}
~~~

## 呼び出し元

- [00c5d5c0](../00c5d/00c5d5c0.md)

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
                    /* try { // try from 00bbff20 to 00cbff27 has its CatchHandler @ 00bc03c0 */
    if (uVar11 < 5) {
      return 0;
    }
    uVar12 = uVar11 - 4;
                    /* try { // try from 00bbff28 to 00cbff37 has its CatchHandler @ 00bc0308 */
    if (uVar12 < uVar13) {
      return 0;
    }
    lVar7 = param_2[7];
                    /* try { // try from 00bbff38 to 00cbff63 has its CatchHandler @ 00bc02f0 */
    iVar6 = *param_1;
    uVar1 = (int)lVar7 + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
                    /* try { // try from 00bbff64 to 00cc0007 has its CatchHandler @ 00bbfb18 */
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
                    /* try { // try from 00bc0008 to 00cc0013 has its CatchHandler @ 00bc02ec */
                    /* try { // try from 00bc0014 to 00cc020b has its CatchHandler @ 00bbfb18 */
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
                    /* try { // try from 00bc020c to 00cc0213 has its CatchHandler @ 00bc03e4 */
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
                    /* try { // try from 00bc02cc to 00cc02eb has its CatchHandler @ 00bc03c0 */
                    if ((char)param_2[3] != '\0') {
                      return 0;
                    }
                    if (uVar12 < uVar14) {
                      return 0;
                    }
                  }
                    /* catch() { ... } // from try @ 00bc0008 with catch @ 00bc02ec
                       try { // try from 00bc02ec to 00cc0413 has its CatchHandler @ 00bbfb18 */
                    /* catch() { ... } // from try @ 00bbff38 with catch @ 00bc02f0 */
                  if ((ulong)param_2[4] <= (ulong)*puVar3) {
                    return 0;
                  }
                  uVar8 = (ulong)*puVar3 + 4;
                    /* catch() { ... } // from try @ 00bbff28 with catch @ 00bc0308 */
                  if (uVar11 - 1 < uVar8 + uVar14) {
                    return 0;
                  }
                  if (uVar11 <= uVar8) {
                    return 0;
                  }
                    /* catch() { ... } // from try @ 00bbfe90 with catch @ 00bc031c */
                  if (uVar11 - uVar8 < uVar14) {
                    return 0;
                  }
                  if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                    return 0;
                  }
                }
                    /* catch() { ... } // from try @ 00bbfdc8 with catch @ 00bc032c */
                if (0xc < uVar5) {
                  if ((ulong)puVar15[6] != 0) {
                    uVar14 = uVar13 + puVar15[6];
                    /* catch() { ... } // from try @ 00bbfdb8 with catch @ 00bc0344 */
                    if ((uVar14 & 3) == 0) {
                      if (uVar12 < uVar14) {
                        return 0;
                      }
                    }
                    else {
                    /* catch() { ... } // from try @ 00bbfecc with catch @ 00bc0348 */
                    /* catch() { ... } // from try @ 00bbfda0 with catch @ 00bc0350 */
                      if ((char)param_2[3] != '\0') {
                        return 0;
                      }
                    /* catch() { ... } // from try @ 00bbfce8 with catch @ 00bc0358 */
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
                    /* catch() { ... } // from try @ 00bbfba8 with catch @ 00bc039c */
                    uVar14 = (long)puVar3 - lVar10;
                    if ((uVar14 & 3) == 0) {
                    /* catch() { ... } // from try @ 00bbff20 with catch @ 00bc03c0
                       catch() { ... } // from try @ 00bc02cc with catch @ 00bc03c0 */
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
                    /* catch() { ... } // from try @ 00bbfcbc with catch @ 00bc03e4
                       catch() { ... } // from try @ 00bc020c with catch @ 00bc03e4 */
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
                    /* try { // try from 00bc04c4 to 00cc050f has its CatchHandler @ 00bc04c4
                       catch() { ... } // from try @ 00bc04c4 with catch @ 00bc04c4
                       catch() { ... } // from try @ 00bc0518 with catch @ 00bc04c4
                       catch() { ... } // from try @ 00bc0594 with catch @ 00bc04c4
                       catch() { ... } // from try @ 00bc063c with catch @ 00bc04c4
                       catch() { ... } // from try @ 00bc06b0 with catch @ 00bc04c4
                       catch() { ... } // from try @ 00bc07b8 with catch @ 00bc04c4 */
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
                    /* try { // try from 00bc0510 to 00cc0517 has its CatchHandler @ 00bc0944 */
                          if ((char)param_2[3] != '\0') {
                            return 0;
                          }
                    /* try { // try from 00bc0518 to 00cc0587 has its CatchHandler @ 00bc04c4 */
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
                    /* try { // try from 00bc0588 to 00cc0593 has its CatchHandler @ 00bc090c */
                    /* try { // try from 00bc0594 to 00cc0627 has its CatchHandler @ 00bc04c4 */
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
                    /* try { // try from 00bc0628 to 00cc063b has its CatchHandler @ 00bc0908 */
                        if (((ulong)puVar15[9] != 0) &&
                           (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[9]),
                           puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0))
                        {
                    /* try { // try from 00bc063c to 00cc069b has its CatchHandler @ 00bc04c4 */
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
                    /* try { // try from 00bc069c to 00cc06af has its CatchHandler @ 00bc0904 */
                          if (uVar11 - uVar8 < uVar14) {
                            return 0;
                          }
                          if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                            return 0;
                          }
                        }
                    /* try { // try from 00bc06b0 to 00cc074f has its CatchHandler @ 00bc04c4 */
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
                    /* try { // try from 00bc0750 to 00cc0757 has its CatchHandler @ 00bc08f4 */
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
                    /* try { // try from 00bc0798 to 00cc07b7 has its CatchHandler @ 00bc08b4 */
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
                    /* try { // try from 00bc07b8 to 00cc096b has its CatchHandler @ 00bc04c4 */
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
                    /* catch() { ... } // from try @ 00bc0798 with catch @ 00bc08b4 */
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
                    /* catch() { ... } // from try @ 00bc0750 with catch @ 00bc08f4 */
                                } while ((ulong)*puVar4 * 4 - uVar14 != 0);
                              }
                            }
                            if (0x18 < uVar5) {
                    /* catch() { ... } // from try @ 00bc069c with catch @ 00bc0904 */
                    /* catch() { ... } // from try @ 00bc0628 with catch @ 00bc0908 */
                              if ((ulong)puVar15[0xc] != 0) {
                    /* catch() { ... } // from try @ 00bc0588 with catch @ 00bc090c */
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
                    /* catch() { ... } // from try @ 00bc0510 with catch @ 00bc0944 */
                                if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                                  return 0;
                                }
                              }
                              if (((ulong)puVar15[0xc] != 0) &&
                                 (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[0xc]),
                                 puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3),
                                 puVar3 != (uint *)0x0)) {
                    /* try { // try from 00bc096c to 00cc0a3b has its CatchHandler @ 00bc096c
                       catch() { ... } // from try @ 00bc096c with catch @ 00bc096c
                       catch() { ... } // from try @ 00bc0a54 with catch @ 00bc096c */
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
                    /* try { // try from 00bc0a3c to 00cc0a53 has its CatchHandler @ 00bc0acc */
                                  puVar4 = (uint *)((long)param_1 + (ulong)puVar15[0xd]);
                                  puVar3 = (uint *)((long)puVar4 + (ulong)*puVar4);
                                  if (puVar3 != (uint *)0x0) {
                                    uVar14 = (long)puVar3 - lVar10;
                    /* try { // try from 00bc0a54 to 00cc0b0b has its CatchHandler @ 00bc096c */
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
                    /* catch() { ... } // from try @ 00bc0a3c with catch @ 00bc0acc */
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
