# 00abc6dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00abc6dc",
  "name": "FUN_00abc6dc",
  "size": 1348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1919a6683e4a8984809399acc0c061016070bee5efa93da4b5c852d5d5cb6c12",
  "source_text_sha256": "1919a6683e4a8984809399acc0c061016070bee5efa93da4b5c852d5d5cb6c12"
}
~~~

## 呼び出し元

- [00abe1c8](../00abe/00abe1c8.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [0046da08](../0046d/0046da08.md)
- [00470800](../00470/00470800.md)
- [0049f3b0](../0049f/0049f3b0.md)
- [00615c90](../00615/00615c90.md)
- [00728b2c](../00728/00728b2c.md)
- [0080b388](../0080b/0080b388.md)
- [00abccb8](../00abc/00abccb8.md)
- [00abce14](../00abc/00abce14.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c58050](../00c58/00c58050.md)

## 疑似コード / UTF-8 14365 bytes

~~~c

byte FUN_00abc6dc(int *param_1,long param_2,int param_3)

{
  undefined4 *puVar1;
  wchar_t *pwVar2;
  undefined4 *puVar3;
  ulong uVar4;
  byte bVar5;
  int iVar6;
  int *__ptr;
  int *piVar7;
  wchar_t *pwVar8;
  ulong uVar9;
  void *__dest;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 *__ptr_00;
  int *piVar12;
  ulong uVar13;
  undefined8 *extraout_x8;
  undefined8 *puVar14;
  ulong uVar15;
  ulong uVar16;
  undefined8 *puVar17;
  wchar_t *pwVar18;
  void *pvVar19;
  int *piVar20;
  ulong uVar21;
  undefined4 *puVar22;
  long lVar23;
  void *local_a0;
  void *pvStack_98;
  undefined8 local_90;
  undefined8 *local_80;
  undefined8 *local_78;
  undefined8 *local_70;
  long local_68;
  
                    /* catch() { ... } // from try @ 00abb854 with catch @ 00abc6e0 */
                    /* catch() { ... } // from try @ 00abb764 with catch @ 00abc6f4 */
  uVar4 = tpidr_el0;
                    /* catch() { ... } // from try @ 00abb674 with catch @ 00abc708 */
  local_68 = *(long *)(uVar4 + 0x28);
  __ptr = (int *)_Znwm(4);
                    /* catch() { ... } // from try @ 00abb3c4 with catch @ 00abc71c */
  iVar6 = *param_1;
  bVar5 = 0;
  *__ptr = 0;
                    /* catch() { ... } // from try @ 00abb2c8 with catch @ 00abc730 */
  piVar7 = __ptr;
  if (iVar6 < 2) {
    if (iVar6 == 0) {
      piVar7 = (int *)_Znwm(8);
LAB_00abc78c:
                    /* catch() { ... } // from try @ 00abb3b0 with catch @ 00abc78c */
      iVar6 = 3;
      goto LAB_00abc7ec;
    }
    if (iVar6 == 1) {
      iVar6 = param_1[0x1d];
                    /* catch() { ... } // from try @ 00abb840 with catch @ 00abc744 */
      piVar20 = __ptr + 1;
      if (iVar6 < 2) {
        if (iVar6 == 0) {
                    /* catch() { ... } // from try @ 00abb820 with catch @ 00abc7d0 */
                    /* catch() { ... } // from try @ 00abb730 with catch @ 00abc7d4 */
          piVar7 = (int *)_Znwm(8);
                    /* catch() { ... } // from try @ 00abb640 with catch @ 00abc7d8 */
          goto LAB_00abc78c;
        }
        if (iVar6 == 1) {
                    /* catch() { ... } // from try @ 00abb750 with catch @ 00abc75c */
          piVar7 = (int *)_Znwm(8);
LAB_00abc7c4:
                    /* catch() { ... } // from try @ 00abb654 with catch @ 00abc7c4 */
                    /* catch() { ... } // from try @ 00abb3a4 with catch @ 00abc7c8 */
          iVar6 = 1;
                    /* catch() { ... } // from try @ 00abb2a8 with catch @ 00abc7cc */
          goto LAB_00abc7ec;
        }
      }
      else {
        if (iVar6 == 2) {
                    /* catch() { ... } // from try @ 00abb390 with catch @ 00abc7dc */
                    /* catch() { ... } // from try @ 00abb294 with catch @ 00abc7e0 */
          piVar7 = (int *)_Znwm(8);
                    /* catch() { ... } // from try @ 00abb81c with catch @ 00abc7e4 */
                    /* catch() { ... } // from try @ 00abb728 with catch @ 00abc7e8 */
          iVar6 = 2;
          goto LAB_00abc7ec;
        }
        if (iVar6 == 4) {
                    /* catch() { ... } // from try @ 00abb834 with catch @ 00abc7bc */
                    /* catch() { ... } // from try @ 00abb744 with catch @ 00abc7c0 */
          piVar7 = (int *)_Znwm(8);
          goto LAB_00abc7c4;
        }
      }
      goto LAB_00abc808;
    }
  }
  else {
    if (iVar6 != 2) {
                    /* catch() { ... } // from try @ 00abb660 with catch @ 00abc774 */
      if (iVar6 != 3) goto LAB_00abc8cc;
      piVar7 = (int *)_Znwm(8);
      goto LAB_00abc78c;
    }
    piVar7 = (int *)_Znwm(8);
                    /* catch() { ... } // from try @ 00abb2b4 with catch @ 00abc7a4 */
    iVar6 = 4;
LAB_00abc7ec:
                    /* catch() { ... } // from try @ 00abb638 with catch @ 00abc7ec */
                    /* catch() { ... } // from try @ 00abb388 with catch @ 00abc7f0 */
                    /* catch() { ... } // from try @ 00abb28c with catch @ 00abc7f4 */
    piVar20 = piVar7 + 2;
                    /* catch() { ... } // from try @ 00abaeb8 with catch @ 00abc7f8 */
    *piVar7 = *__ptr;
    piVar7[1] = iVar6;
    _ZdlPv(__ptr);
    __ptr = piVar7;
LAB_00abc808:
    do {
      piVar12 = __ptr;
      if (*__ptr == param_3) break;
      __ptr = __ptr + 1;
      piVar12 = piVar20;
    } while (__ptr != piVar20);
    if (piVar12 == piVar20) {
LAB_00abc8c8:
      bVar5 = 0;
    }
    else {
      iVar6 = *param_1;
      if (iVar6 < 2) {
        if (iVar6 == 0) {
          local_80 = (undefined8 *)0x0;
          local_78 = (undefined8 *)0x0;
                    /* catch() { ... } // from try @ 00abb038 with catch @ 00abc910 */
          lVar23 = *(long *)(param_1 + 0x14);
          local_70 = (undefined8 *)0x0;
          if (*(long *)(param_1 + 0x16) == lVar23) {
LAB_00abca8c:
            bVar5 = 1;
          }
          else {
            uVar21 = 0;
            uVar10 = uVar4;
            do {
              if (-1 < *(int *)(lVar23 + uVar21 * 4)) {
                local_a0 = (void *)0x0;
                pvStack_98 = (void *)0x0;
                local_90 = 0;
                    /* catch() { ... } // from try @ 00abac98 with catch @ 00abc960 */
                if (local_78 < local_70) {
                  *local_78 = 0;
                  local_78[1] = 0;
                  local_78[2] = 0;
                  local_78[1] = 0;
                  *local_78 = 0;
                  local_78[2] = 0;
                  local_78 = local_78 + 3;
                }
                else {
                  local_78 = (undefined8 *)FUN_00615c90(&local_80,&local_a0);
                  if (local_a0 != (void *)0x0) {
                    pvStack_98 = local_a0;
                    _ZdlPv(local_a0);
                    /* catch() { ... } // from try @ 00abb19c with catch @ 00abc9b0 */
                  }
                }
              }
              puVar11 = local_78;
              if (local_78 == local_80) {
                if (*(long *)(uVar4 + 0x28) != local_68) goto LAB_00abccb4;
                FUN_0080b388(&local_80);
                goto LAB_00abcbd0;
              }
              if ((ulong)(*(long *)(param_1 + 0x16) - *(long *)(param_1 + 0x14) >> 2) <= uVar21) {
                if (*(long *)(uVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                  FUN_0049f3b0(param_1 + 0x14);
                }
                goto LAB_00abccb4;
              }
                    /* catch() { ... } // from try @ 00abb028 with catch @ 00abc9d4 */
              uVar9 = FUN_0046da08(*(undefined4 *)(*(long *)(param_1 + 0x14) + uVar21 * 4));
              puVar3 = (undefined4 *)puVar11[-2];
              if (puVar3 < (undefined4 *)puVar11[-1]) {
                puVar22 = puVar3 + 1;
                *puVar3 = (int)uVar9;
              }
              else {
                puVar14 = puVar11 + -3;
                pvVar19 = (void *)*puVar14;
                lVar23 = (long)puVar3 - (long)pvVar19 >> 2;
                uVar16 = lVar23 + 1;
                    /* catch() { ... } // from try @ 00abac88 with catch @ 00abc9f8 */
                if (uVar16 >> 0x3e != 0) goto LAB_00abcbe8;
                uVar13 = (long)puVar11[-1] - (long)pvVar19;
                uVar15 = (long)uVar13 >> 1;
                if (uVar15 <= uVar16) {
                  uVar15 = uVar16;
                }
                    /* catch() { ... } // from try @ 00abb190 with catch @ 00abca1c */
                if (0x7ffffffffffffffb < uVar13) {
                  uVar15 = 0x3fffffffffffffff;
                }
                if (uVar15 == 0) {
                  __dest = (void *)0x0;
                }
                else {
                  if (uVar15 >> 0x3e != 0) {
                    if (*(long *)(uVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                      FUN_00440e80();
                    }
                    goto LAB_00abccb4;
                  }
                  uVar9 = uVar9 & 0xffffffff;
                  __dest = (void *)_Znwm(uVar15 << 2);
                  uVar10 = uVar9;
                }
                puVar1 = (undefined4 *)((long)__dest + lVar23 * 4);
                puVar22 = puVar1 + 1;
                *puVar1 = (int)uVar9;
                    /* catch() { ... } // from try @ 00abb01c with catch @ 00abca60 */
                memcpy(__dest,pvVar19,(long)puVar3 - (long)pvVar19);
                puVar11[-3] = __dest;
                puVar11[-2] = puVar22;
                puVar11[-1] = (void *)((long)__dest + uVar15 * 4);
                if (pvVar19 != (void *)0x0) {
                  _ZdlPv(pvVar19);
                }
              }
              puVar11[-2] = puVar22;
              uVar21 = uVar21 + 1;
              lVar23 = *(long *)(param_1 + 0x14);
            } while (uVar21 < (ulong)(*(long *)(param_1 + 0x16) - lVar23 >> 2));
            puVar11 = local_80;
            if (local_78 != local_80) {
                    /* catch() { ... } // from try @ 00abac7c with catch @ 00abcaa4 */
              uVar21 = 0;
              do {
                uVar9 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
                uVar10 = uVar4;
                if (uVar9 < uVar21 || uVar9 - uVar21 == 0) goto LAB_00abcbd0;
                lVar23 = local_80[uVar21 * 3];
                if ((local_80 + uVar21 * 3)[1] == lVar23) {
LAB_00abcb34:
                    /* catch() { ... } // from try @ 00abb138 with catch @ 00abcb34 */
                  bVar5 = 0;
                    /* catch() { ... } // from try @ 00abafc4 with catch @ 00abcb38 */
                  __ptr_00 = local_78;
                  puVar11 = local_78;
                  puVar14 = local_80;
                    /* catch() { ... } // from try @ 00abac24 with catch @ 00abcb3c */
                  if (local_78 == local_80) goto LAB_00abcb8c;
                  goto LAB_00abcb70;
                }
                uVar9 = 0;
                while( true ) {
                  uVar10 = FUN_00abccb8(param_1,*(undefined4 *)(lVar23 + uVar9 * 4));
                    /* catch() { ... } // from try @ 00abb144 with catch @ 00abcae8 */
                  uVar16 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
                  if ((uVar10 & 1) != 0) break;
                    /* catch() { ... } // from try @ 00abafd0 with catch @ 00abcb00 */
                  uVar10 = uVar4;
                  if (uVar16 < uVar21 || uVar16 - uVar21 == 0) goto LAB_00abcbd0;
                  uVar9 = uVar9 + 1;
                  lVar23 = local_80[uVar21 * 3];
                    /* catch() { ... } // from try @ 00abac30 with catch @ 00abcb18 */
                  if ((ulong)((local_80 + uVar21 * 3)[1] - lVar23 >> 2) <= uVar9) goto LAB_00abcb34;
                }
                uVar21 = uVar21 + 1;
                puVar11 = local_78;
              } while (uVar21 <= uVar16 && uVar16 - uVar21 != 0);
            }
            bVar5 = 1;
                    /* catch() { ... } // from try @ 00abb114 with catch @ 00abcb50 */
            if (local_80 != (undefined8 *)0x0) {
                    /* catch() { ... } // from try @ 00abafa0 with catch @ 00abcb54 */
              __ptr_00 = puVar11;
              puVar14 = local_80;
                    /* catch() { ... } // from try @ 00abac00 with catch @ 00abcb58 */
              if (puVar11 != local_80) {
LAB_00abcb70:
                do {
                  puVar17 = puVar11 + -3;
                  pvVar19 = (void *)*puVar17;
                  if (pvVar19 != (void *)0x0) {
                    puVar11[-2] = pvVar19;
                    /* catch() { ... } // from try @ 00abbd00 with catch @ 00abcb80 */
                    _ZdlPv(pvVar19);
                    /* catch() { ... } // from try @ 00abbc40 with catch @ 00abcb84 */
                  }
                    /* catch() { ... } // from try @ 00abbd10 with catch @ 00abcb64 */
                  __ptr_00 = local_80;
                  puVar11 = puVar17;
                } while (puVar17 != puVar14);
              }
LAB_00abcb8c:
              local_78 = puVar14;
              _ZdlPv(__ptr_00);
            }
          }
        }
        else {
          if (iVar6 != 1) goto LAB_00abc8c8;
                    /* catch() { ... } // from try @ 00abaea8 with catch @ 00abc844 */
          iVar6 = FUN_00abce14(param_2,param_1[0x1d]);
          bVar5 = param_1[0x1e] <= iVar6;
        }
      }
      else {
                    /* catch() { ... } // from try @ 00abae9c with catch @ 00abc864 */
        if (iVar6 == 2) {
          bVar5 = FUN_00728b2c(param_1[0x1f]);
        }
        else {
          if (iVar6 != 3) goto LAB_00abc8c8;
          lVar23 = *(long *)(param_1 + 8);
          if (*(long *)(param_1 + 10) == lVar23) goto LAB_00abca8c;
          pwVar18 = *(wchar_t **)(param_2 + 0x38);
          uVar21 = 0;
          do {
            pwVar8 = wmemchr(*(wchar_t **)(param_2 + 0x30),*(wchar_t *)(lVar23 + uVar21 * 4),
                             (long)pwVar18 - (long)*(wchar_t **)(param_2 + 0x30) >> 2);
            pwVar2 = pwVar18;
            if (pwVar8 != (wchar_t *)0x0) {
              pwVar2 = pwVar8;
            }
            pwVar18 = *(wchar_t **)(param_2 + 0x38);
                    /* catch() { ... } // from try @ 00abae50 with catch @ 00abc8a4 */
            bVar5 = pwVar2 != pwVar18;
            if (pwVar2 == pwVar18) break;
            lVar23 = *(long *)(param_1 + 8);
            uVar21 = uVar21 + 1;
                    /* catch() { ... } // from try @ 00abae44 with catch @ 00abc8b8 */
                    /* catch() { ... } // from try @ 00abae18 with catch @ 00abc8bc */
                    /* catch() { ... } // from try @ 00abb1ac with catch @ 00abc8c0 */
          } while (uVar21 < (ulong)(*(long *)(param_1 + 10) - lVar23 >> 2));
        }
      }
    }
  }
LAB_00abc8cc:
  _ZdlPv(piVar7);
  if (*(long *)(uVar4 + 0x28) == local_68) {
    return bVar5 & 1;
  }
LAB_00abccb4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
LAB_00abcbd0:
  if (*(long *)(uVar10 + 0x28) == local_68) {
    FUN_0080b388(&local_80);
    puVar14 = extraout_x8;
LAB_00abcbe8:
    if (*(long *)(uVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(puVar14);
    }
  }
  goto LAB_00abccb4;
}

~~~
