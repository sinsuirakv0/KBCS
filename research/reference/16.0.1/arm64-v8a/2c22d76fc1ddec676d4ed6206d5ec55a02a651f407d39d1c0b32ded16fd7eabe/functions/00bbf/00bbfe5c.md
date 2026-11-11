# 00bbfe5c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bbfe5c",
  "name": "_ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 3408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "351b16e6892860fc2a687abdf220f8012882cf15639f804884899211930e61e2",
  "source_text_sha256": "351b16e6892860fc2a687abdf220f8012882cf15639f804884899211930e61e2"
}
~~~

## 呼び出し元

- [00c5d4f0](../00c5d/00c5d4f0.md)

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
  
                    /* try { // try from 00bbfe5c to 00cbfe67 has its CatchHandler @ 00bc02d8 */
  lVar10 = *param_2;
  uVar13 = (long)param_1 - lVar10;
  if (((uVar13 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar11 = param_2[1];
    if (uVar11 < 5) {
      return 0;
    }
    uVar12 = uVar11 - 4;
    if (uVar12 < uVar13) {
      return 0;
    }
    lVar7 = param_2[7];
    iVar6 = *param_1;
    uVar1 = (int)lVar7 + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
                    /* try { // try from 00bbfeb0 to 00cbfeb7 has its CatchHandler @ 00bc0350 */
                    /* try { // try from 00bbfeb8 to 00cbfec7 has its CatchHandler @ 00bc0298 */
                    /* try { // try from 00bbfec8 to 00cbfef3 has its CatchHandler @ 00bc0280 */
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar14 = uVar13 - (long)iVar6, (uVar14 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar14 <= uVar11 - 2)) {
      uVar5 = *(ushort *)(lVar10 + uVar14);
      if ((((uVar5 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar5 & 1) == 0)) {
                    /* try { // try from 00bbfef4 to 00cbff97 has its CatchHandler @ 00bbfaa8 */
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
          if (((ulong)puVar15[2] != 0) &&
             (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[2]),
             puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
            uVar14 = (long)puVar3 - lVar10;
            if ((uVar14 & 3) == 0) {
                    /* try { // try from 00bbffa4 to 00cc019b has its CatchHandler @ 00bbfaa8 */
              if (uVar12 < uVar14) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
                    /* try { // try from 00bbff98 to 00cbffa3 has its CatchHandler @ 00bc027c */
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
                    /* try { // try from 00bc019c to 00cc01a3 has its CatchHandler @ 00bc0374 */
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
                    /* try { // try from 00bc025c to 00cc027b has its CatchHandler @ 00bc0350 */
                  uVar8 = (ulong)*puVar3 + 4;
                  if (uVar11 - 1 < uVar8 + uVar14) {
                    return 0;
                  }
                  if (uVar11 <= uVar8) {
                    return 0;
                  }
                    /* catch() { ... } // from try @ 00bbff98 with catch @ 00bc027c
                       try { // try from 00bc027c to 00cc03a3 has its CatchHandler @ 00bbfaa8 */
                    /* catch() { ... } // from try @ 00bbfec8 with catch @ 00bc0280 */
                  if (uVar11 - uVar8 < uVar14) {
                    return 0;
                  }
                  if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                    return 0;
                  }
                }
                if (0xc < uVar5) {
                    /* catch() { ... } // from try @ 00bbfeb8 with catch @ 00bc0298 */
                  if ((ulong)puVar15[6] != 0) {
                    uVar14 = uVar13 + puVar15[6];
                    if ((uVar14 & 3) == 0) {
                      if (uVar12 < uVar14) {
                        return 0;
                      }
                    }
                    else {
                    /* catch() { ... } // from try @ 00bbfe20 with catch @ 00bc02ac */
                      if ((char)param_2[3] != '\0') {
                        return 0;
                      }
                    /* catch() { ... } // from try @ 00bbfd58 with catch @ 00bc02bc */
                      if (uVar12 < uVar14) {
                        return 0;
                      }
                    }
                    /* catch() { ... } // from try @ 00bbfd48 with catch @ 00bc02d4 */
                    if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                      return 0;
                    }
                    /* catch() { ... } // from try @ 00bbfe5c with catch @ 00bc02d8 */
                    /* catch() { ... } // from try @ 00bbfd30 with catch @ 00bc02e0 */
                    if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                      return 0;
                    }
                  }
                    /* catch() { ... } // from try @ 00bbfc78 with catch @ 00bc02e8 */
                  if (((ulong)puVar15[6] != 0) &&
                     (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[6]),
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
                    /* catch() { ... } // from try @ 00bbfb38 with catch @ 00bc032c */
                    if ((ulong)param_2[4] <= (ulong)*puVar3) {
                      return 0;
                    }
                    uVar8 = (ulong)*puVar3 + 4;
                    /* catch() { ... } // from try @ 00bbfeb0 with catch @ 00bc0350
                       catch() { ... } // from try @ 00bc025c with catch @ 00bc0350 */
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
                    /* catch() { ... } // from try @ 00bbfc4c with catch @ 00bc0374
                       catch() { ... } // from try @ 00bc019c with catch @ 00bc0374 */
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
                    /* try { // try from 00bc0454 to 00cc049f has its CatchHandler @ 00bc0454
                       catch() { ... } // from try @ 00bc0454 with catch @ 00bc0454
                       catch() { ... } // from try @ 00bc04a8 with catch @ 00bc0454
                       catch() { ... } // from try @ 00bc0524 with catch @ 00bc0454
                       catch() { ... } // from try @ 00bc05cc with catch @ 00bc0454
                       catch() { ... } // from try @ 00bc0640 with catch @ 00bc0454
                       catch() { ... } // from try @ 00bc0748 with catch @ 00bc0454 */
                    if (0x10 < uVar5) {
                      if ((ulong)puVar15[8] != 0) {
                        uVar14 = uVar13 + puVar15[8];
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
                    /* try { // try from 00bc04a0 to 00cc04a7 has its CatchHandler @ 00bc08d4 */
                        if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                          return 0;
                        }
                      }
                    /* try { // try from 00bc04a8 to 00cc0517 has its CatchHandler @ 00bc0454 */
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
                        if ((ulong)param_2[4] <= (ulong)*puVar3) {
                          return 0;
                        }
                        uVar8 = (ulong)*puVar3 + 4;
                        if (uVar11 - 1 < uVar8 + uVar14) {
                          return 0;
                        }
                    /* try { // try from 00bc0518 to 00cc0523 has its CatchHandler @ 00bc089c */
                        if (uVar11 <= uVar8) {
                          return 0;
                        }
                    /* try { // try from 00bc0524 to 00cc05b7 has its CatchHandler @ 00bc0454 */
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
                        if (((ulong)puVar15[9] != 0) &&
                           (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[9]),
                           puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0))
                        {
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
                    /* try { // try from 00bc05b8 to 00cc05cb has its CatchHandler @ 00bc0898 */
                            if (uVar12 < uVar14) {
                              return 0;
                            }
                          }
                    /* try { // try from 00bc05cc to 00cc062b has its CatchHandler @ 00bc0454 */
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
                        if (0x14 < uVar5) {
                          if ((ulong)puVar15[10] != 0) {
                            uVar14 = uVar13 + puVar15[10];
                            if ((uVar14 & 3) == 0) {
                              if (uVar12 < uVar14) {
                                return 0;
                              }
                            }
                            else {
                    /* try { // try from 00bc062c to 00cc063f has its CatchHandler @ 00bc0894 */
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
                    /* try { // try from 00bc06e0 to 00cc06e7 has its CatchHandler @ 00bc0884 */
                            if (uVar11 - uVar8 < uVar14) {
                              return 0;
                            }
                            if (*(char *)(lVar10 + uVar8 + uVar14) != '\0') {
                              return 0;
                            }
                          }
                          if (0x16 < uVar5) {
                            if ((ulong)puVar15[0xb] != 0) {
                              uVar14 = uVar13 + puVar15[0xb];
                              if ((uVar14 & 3) == 0) {
                    /* try { // try from 00bc0728 to 00cc0747 has its CatchHandler @ 00bc0844 */
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
                    /* try { // try from 00bc0748 to 00cc08fb has its CatchHandler @ 00bc0454 */
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
                    /* catch() { ... } // from try @ 00bc0728 with catch @ 00bc0844 */
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
                            if (0x18 < uVar5) {
                              if ((ulong)puVar15[0xc] != 0) {
                                uVar14 = uVar13 + puVar15[0xc];
                                if ((uVar14 & 3) == 0) {
                    /* catch() { ... } // from try @ 00bc062c with catch @ 00bc0894 */
                    /* catch() { ... } // from try @ 00bc05b8 with catch @ 00bc0898 */
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                                else {
                    /* catch() { ... } // from try @ 00bc06e0 with catch @ 00bc0884 */
                                  if ((char)param_2[3] != '\0') {
                                    return 0;
                                  }
                                  if (uVar12 < uVar14) {
                                    return 0;
                                  }
                                }
                    /* catch() { ... } // from try @ 00bc0518 with catch @ 00bc089c */
                                if ((int)*(uint *)(lVar10 + uVar14) < 1) {
                                  return 0;
                                }
                                if (uVar11 - 1 < uVar14 + *(uint *)(lVar10 + uVar14)) {
                                  return 0;
                                }
                              }
                              if (((ulong)puVar15[0xc] != 0) &&
                                 (puVar3 = (uint *)((long)param_1 + (ulong)puVar15[0xc]),
                                 puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3),
                                 puVar3 != (uint *)0x0)) {
                                uVar14 = (long)puVar3 - lVar10;
                    /* catch() { ... } // from try @ 00bc04a0 with catch @ 00bc08d4 */
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
                    /* try { // try from 00bc08fc to 00cc09cb has its CatchHandler @ 00bc08fc
                       catch() { ... } // from try @ 00bc08fc with catch @ 00bc08fc
                       catch() { ... } // from try @ 00bc09e4 with catch @ 00bc08fc */
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
                                  puVar4 = (uint *)((long)param_1 + (ulong)puVar15[0xd]);
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
                    /* try { // try from 00bc09cc to 00cc09e3 has its CatchHandler @ 00bc0a5c */
                                      if (uVar12 < uVar14) {
                                        return 0;
                                      }
                                    }
                    /* try { // try from 00bc09e4 to 00cc0a9b has its CatchHandler @ 00bc08fc */
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
                    /* catch() { ... } // from try @ 00bc09cc with catch @ 00bc0a5c */
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
