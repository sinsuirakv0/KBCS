# 006cbacc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006cbacc",
  "name": "FUN_006cbacc",
  "size": 4012,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "775a518cfbee4363165aa72d1105c4029e4a35d179a4103ed66ceee26d947628",
  "source_text_sha256": "775a518cfbee4363165aa72d1105c4029e4a35d179a4103ed66ceee26d947628"
}
~~~

## 呼び出し元

- [006cdce0](../006cd/006cdce0.md)
- [009f8670](../009f8/009f8670.md)
- [009f8d00](../009f8/009f8d00.md)
- [00adf288](../00adf/00adf288.md)

## 呼び出し先

- [0043bbe4](../0043b/0043bbe4.md)
- [00440f00](../00440/00440f00.md)
- [00442970](../00442/00442970.md)
- [00470880](../00470/00470880.md)
- [005c17dc](../005c1/005c17dc.md)
- [005c3ebc](../005c3/005c3ebc.md)
- [00676aa0](../00676/00676aa0.md)
- [006cb10c](../006cb/006cb10c.md)
- [006cb36c](../006cb/006cb36c.md)
- [006cb598](../006cb/006cb598.md)
- [006cb8e4](../006cb/006cb8e4.md)
- [006d6370](../006d6/006d6370.md)
- [00851550](../00851/00851550.md)
- [009df918](../009df/009df918.md)
- [009e1014](../009e1/009e1014.md)
- [009e2fe8](../009e2/009e2fe8.md)
- [009e3efc](../009e3/009e3efc.md)
- [009f6268](../009f6/009f6268.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c58520](../00c58/00c58520.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 38552 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_006cbacc(undefined8 *param_1,undefined4 param_2)

{
  long *plVar1;
  int *piVar2;
  undefined4 uVar3;
  int iVar4;
  wchar_t wVar5;
  wchar_t wVar6;
  size_t __n;
  long lVar7;
  wchar_t *pwVar8;
  undefined8 *puVar9;
  bool bVar10;
  int iVar11;
  int iVar12;
  int *piVar13;
  undefined8 ******ppppppuVar14;
  long lVar15;
  ulong uVar16;
  long lVar17;
  long *plVar18;
  undefined8 *puVar19;
  undefined8 *******pppppppuVar20;
  undefined8 *******pppppppuVar21;
  undefined8 *******pppppppuVar22;
  void *pvVar23;
  wchar_t *pwVar24;
  undefined8 ******ppppppuVar25;
  undefined8 *******pppppppuVar26;
  long *plVar27;
  ulong uVar28;
  undefined8 *******pppppppuVar29;
  long *plVar30;
  ulong uVar31;
  long *plVar32;
  undefined8 *******pppppppuVar33;
  int *piVar34;
  wchar_t *pwVar35;
  wchar_t *pwVar36;
  int *piVar37;
  wchar_t *pwVar38;
  void *pvVar39;
  undefined8 *puVar40;
  undefined8 uVar41;
  int *piVar42;
  undefined8 *******local_180;
  undefined8 *******local_178;
  long local_170;
  long *local_168;
  long *local_160;
  undefined8 *******local_158;
  undefined8 *******local_150;
  long local_148;
  undefined8 *local_140;
  undefined8 local_138 [2];
  long *local_128;
  undefined8 *******local_120;
  long local_118;
  undefined1 uStack_109;
  undefined8 *******local_108;
  undefined8 *******local_100 [2];
  char local_f0;
  wchar_t *local_e8 [3];
  undefined8 local_d0;
  int *piStack_c8;
  int *local_c0;
  int *local_b8;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  undefined8 uStack_88;
  undefined8 uStack_80;
  undefined8 uStack_78;
  long local_70;
  
  lVar7 = tpidr_el0;
  local_70 = *(long *)(lVar7 + 0x28);
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  FUN_006cb36c(&local_140);
  local_150 = (undefined8 *******)0x0;
  local_148 = 0;
  local_158 = &local_150;
  puVar19 = local_140;
  while (puVar19 != local_138) {
    pvVar39 = (void *)puVar19[5];
    uVar3 = *(undefined4 *)(puVar19 + 4);
    local_c0 = (int *)0x0;
    local_b8 = (int *)0x0;
    uVar16 = (ulong)local_d0 >> 0x20;
    local_d0 = (int *)CONCAT44((int)uVar16,uVar3);
    __n = puVar19[6] - (long)pvVar39;
    piStack_c8 = (int *)0x0;
    if (__n == 0) {
      piVar13 = (int *)0x0;
    }
    else {
      if ((long)__n < 0) {
        if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
          FUN_00470880(&piStack_c8);
        }
        goto LAB_006ccbcc;
      }
      piVar13 = (int *)_Znwm(__n);
      piStack_c8 = piVar13;
      local_b8 = (int *)((long)piVar13 + __n);
      memcpy(piVar13,pvVar39,__n);
      local_c0 = (int *)((long)piVar13 + __n);
    }
    iVar11 = piVar13[2];
    pppppppuVar26 = &local_150;
    pppppppuVar21 = local_150;
    while (pppppppuVar22 = pppppppuVar26, pppppppuVar21 != (undefined8 *******)0x0) {
      while (pppppppuVar26 = pppppppuVar21, *(int *)((long)pppppppuVar26 + 0x1c) <= iVar11) {
        if (iVar11 <= *(int *)((long)pppppppuVar26 + 0x1c)) {
          *(undefined4 *)(pppppppuVar26 + 4) = uVar3;
          piVar37 = local_c0;
          goto joined_r0x006cbc7c;
        }
        pppppppuVar21 = (undefined8 *******)pppppppuVar26[1];
        if ((undefined8 *******)pppppppuVar26[1] == (undefined8 *******)0x0) {
          pppppppuVar22 = pppppppuVar26 + 1;
          goto LAB_006cbbe4;
        }
      }
      pppppppuVar21 = (undefined8 *******)*pppppppuVar26;
    }
LAB_006cbbe4:
    ppppppuVar14 = (undefined8 ******)_Znwm(0x28);
    *(int *)((long)ppppppuVar14 + 0x1c) = iVar11;
    *(undefined4 *)(ppppppuVar14 + 4) = 0;
    *ppppppuVar14 = (undefined8 *****)0x0;
    ppppppuVar14[1] = (undefined8 *****)0x0;
    ppppppuVar14[2] = pppppppuVar26;
    *pppppppuVar22 = ppppppuVar14;
    ppppppuVar25 = ppppppuVar14;
    if ((undefined8 *******)*local_158 != (undefined8 *******)0x0) {
      local_158 = (undefined8 *******)*local_158;
      ppppppuVar25 = *pppppppuVar22;
    }
    FUN_0043bbe4(local_150,ppppppuVar25);
    local_148 = local_148 + 1;
    *(undefined4 *)(ppppppuVar14 + 4) = uVar3;
    piVar13 = piStack_c8;
    piVar37 = local_c0;
joined_r0x006cbc7c:
    local_c0 = piVar13;
    if (local_c0 != (int *)0x0) {
      _ZdlPv(local_c0);
      piVar37 = local_c0;
    }
    local_c0 = piVar37;
    puVar9 = (undefined8 *)puVar19[1];
    puVar40 = puVar19;
    if ((undefined8 *)puVar19[1] == (undefined8 *)0x0) {
      do {
        puVar19 = (undefined8 *)puVar40[2];
        bVar10 = (undefined8 *)*puVar19 != puVar40;
        puVar40 = puVar19;
      } while (bVar10);
    }
    else {
      do {
        puVar19 = puVar9;
        puVar9 = (undefined8 *)*puVar19;
      } while ((undefined8 *)*puVar19 != (undefined8 *)0x0);
    }
  }
  lVar15 = FUN_00851550();
  uVar16 = FUN_009e1014(lVar15 + 0x50,0xffffffff,0xffffffff);
  if ((uVar16 & 1) == 0) {
    FUN_006cb598(&local_d0);
    piVar37 = piStack_c8;
    piVar13 = local_d0;
joined_r0x006cbfe8:
    if (piVar13 != piVar37) {
      uVar41 = *(undefined8 *)piVar13;
      lVar15 = FUN_00851550();
      iVar11 = (int)uVar41;
      if (*(int *)(*(long *)(*(long *)((long)&DWORD_003c9660 + lVar15) + (long)iVar11 * 0x18) + 4)
          == 0) {
        lVar15 = FUN_00851550();
        plVar18 = (long *)((long)&QWORD_00436bb1 + lVar15 + 7);
        plVar27 = (long *)*plVar18;
        plVar30 = plVar18;
        plVar32 = plVar27;
        if (plVar27 != (long *)0x0) {
          do {
            if (iVar11 <= *(int *)((long)plVar32 + 0x1c)) {
              plVar30 = plVar32;
            }
            plVar1 = plVar32 + (*(int *)((long)plVar32 + 0x1c) < iVar11);
            plVar32 = (long *)*plVar1;
          } while ((long *)*plVar1 != (long *)0x0);
          if ((plVar30 != plVar18) && (*(int *)((long)plVar30 + 0x1c) <= iVar11)) {
            do {
              if (iVar11 < *(int *)((long)plVar27 + 0x1c)) {
                plVar27 = (long *)*plVar27;
              }
              else {
                if (iVar11 <= *(int *)((long)plVar27 + 0x1c)) goto LAB_006cc814;
                plVar27 = (long *)plVar27[1];
              }
              if (plVar27 == (long *)0x0) {
                if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                  FUN_00442970("map::at:  key not found");
                }
                goto LAB_006ccbcc;
              }
            } while( true );
          }
        }
      }
      goto LAB_006cc778;
    }
    if (local_d0 != (int *)0x0) {
      piStack_c8 = local_d0;
      _ZdlPv(local_d0);
    }
  }
  else {
    lVar15 = FUN_00851550();
    lVar17 = FUN_009e2fe8(lVar15 + 0x50,0xffffffff,0xffffffff);
    lVar15 = FUN_00851550();
    FUN_009df918(&local_168,lVar15 + 0x50);
    lVar15 = 0;
    local_178 = (undefined8 *******)0x0;
    local_170 = 0;
    local_e8[0] = (wchar_t *)(lVar17 + 0x78);
    local_e8[1] = (wchar_t *)(lVar17 + 0x60);
    local_180 = &local_178;
    do {
      piVar37 = (int *)(*(undefined8 **)((long)local_e8 + lVar15))[1];
      for (piVar13 = (int *)**(undefined8 **)((long)local_e8 + lVar15); piVar13 != piVar37;
          piVar13 = piVar13 + 3) {
        if (*piVar13 == 1) {
          plVar18 = (long *)(**(code **)(*local_168 + 0x38))(local_168,piVar13[1]);
          puVar19 = (undefined8 *)(**(code **)(*plVar18 + 0x48))();
          plVar30 = (long *)puVar19[1];
          for (plVar18 = (long *)*puVar19; plVar18 != plVar30; plVar18 = plVar18 + 2) {
            if (((long *)*plVar18 != (long *)0x0) &&
               (iVar11 = (**(code **)(*(long *)*plVar18 + 0x10))(), iVar11 == 1)) {
              iVar11 = (**(code **)(*(long *)*plVar18 + 0x18))();
              pppppppuVar26 = &local_150;
              pppppppuVar21 = local_150;
              if (local_150 == (undefined8 *******)0x0) {
LAB_006cbe44:
                iVar12 = 0;
              }
              else {
                do {
                  pppppppuVar20 = pppppppuVar21;
                  pppppppuVar22 = pppppppuVar26;
                  iVar12 = *(int *)((long)pppppppuVar20 + 0x1c);
                  pppppppuVar26 = pppppppuVar22;
                  if (iVar11 <= iVar12) {
                    pppppppuVar26 = pppppppuVar20;
                  }
                  pppppppuVar21 = (undefined8 *******)pppppppuVar20[iVar12 < iVar11];
                } while ((undefined8 *******)pppppppuVar20[iVar12 < iVar11] !=
                         (undefined8 *******)0x0);
                if ((undefined8 ********)pppppppuVar26 == &local_150) goto LAB_006cbe44;
                if (iVar11 <= iVar12) {
                  pppppppuVar22 = pppppppuVar20;
                }
                pppppppuVar21 = &local_150;
                if (*(int *)((long)pppppppuVar22 + 0x1c) <= iVar11) {
                  pppppppuVar21 = pppppppuVar26;
                }
                pppppppuVar22 = local_150;
                pppppppuVar26 = &local_150;
                if (&local_150 == (undefined8 ********)pppppppuVar21) goto LAB_006cbe44;
                do {
                  pppppppuVar21 = pppppppuVar26;
                  pppppppuVar20 = pppppppuVar22;
                  iVar12 = *(int *)((long)pppppppuVar20 + 0x1c);
                  pppppppuVar26 = pppppppuVar21;
                  if (iVar11 <= iVar12) {
                    pppppppuVar26 = pppppppuVar20;
                  }
                  pppppppuVar22 = (undefined8 *******)pppppppuVar20[iVar12 < iVar11];
                } while ((undefined8 *******)pppppppuVar20[iVar12 < iVar11] !=
                         (undefined8 *******)0x0);
                pppppppuVar22 = &local_150;
                if ((undefined8 ********)pppppppuVar26 != &local_150) {
                  if (iVar11 <= iVar12) {
                    pppppppuVar21 = pppppppuVar20;
                  }
                  if (*(int *)((long)pppppppuVar21 + 0x1c) <= iVar11) {
                    pppppppuVar22 = pppppppuVar26;
                  }
                }
                iVar12 = *(int *)(pppppppuVar22 + 4);
              }
              lVar17 = FUN_00851550();
              FUN_009e3efc(&local_108,lVar17 + 0x50,param_2,iVar11,0xffffffff,0xffffffff);
              if (local_f0 != '\0') {
                    /* catch() { ... } // from try @ 006ca634 with catch @ 006cbe7c */
                    /* catch() { ... } // from try @ 006ca5e0 with catch @ 006cbe80 */
                uStack_a8 = _UNK_002dff00;
                local_b0 = _DAT_002dfef8;
                uStack_98 = _UNK_002dff10;
                local_a0 = _DAT_002dff08;
                    /* catch() { ... } // from try @ 006ca55c with catch @ 006cbe84 */
                    /* catch() { ... } // from try @ 006ca658 with catch @ 006cbe88 */
                uStack_88 = _UNK_002dff20;
                local_90 = _DAT_002dff18;
                uStack_78 = _UNK_002dff30;
                uStack_80 = _DAT_002dff28;
                piStack_c8 = _UNK_002dfee0;
                local_d0 = _DAT_002dfed8;
                    /* catch() { ... } // from try @ 006ca404 with catch @ 006cbe8c */
                    /* catch() { ... } // from try @ 006ca604 with catch @ 006cbe90 */
                local_b8 = _UNK_002dfef0;
                local_c0 = _DAT_002dfee8;
                    /* catch() { ... } // from try @ 006cb5f8 with catch @ 006cbe94 */
                FUN_006cb10c(&local_128,&local_d0,0xc,&uStack_109);
                pppppppuVar26 = &local_120;
                pppppppuVar21 = local_120;
                pppppppuVar22 = &local_178;
                if (local_120 == (undefined8 *******)0x0) {
LAB_006cbef4:
                    /* catch() { ... } // from try @ 006cb09c with catch @ 006cbef8 */
                  FUN_006d6370(&local_128);
                  pppppppuVar26 = local_178;
LAB_006cbf0c:
                  while (pppppppuVar21 = pppppppuVar22, pppppppuVar26 != (undefined8 *******)0x0) {
                    /* catch() { ... } // from try @ 006cae38 with catch @ 006cbf18 */
                    while (pppppppuVar22 = pppppppuVar26,
                          *(int *)((long)pppppppuVar22 + 0x1c) <= iVar12) {
                      if (iVar12 <= *(int *)((long)pppppppuVar22 + 0x1c)) goto LAB_006cbfb4;
                      pppppppuVar26 = (undefined8 *******)pppppppuVar22[1];
                      if ((undefined8 *******)pppppppuVar22[1] == (undefined8 *******)0x0) {
                        pppppppuVar21 = pppppppuVar22 + 1;
                        goto LAB_006cbf38;
                      }
                    }
                    pppppppuVar26 = (undefined8 *******)*pppppppuVar22;
                  }
LAB_006cbf38:
                  pppppppuVar20 = (undefined8 *******)_Znwm(0x28);
                  *(int *)((long)pppppppuVar20 + 0x1c) = iVar12;
                  *(undefined1 *)(pppppppuVar20 + 4) = 0;
                  *pppppppuVar20 = (undefined8 ******)0x0;
                  pppppppuVar20[1] = (undefined8 ******)0x0;
                  pppppppuVar20[2] = pppppppuVar22;
                    /* catch() { ... } // from try @ 006ca728 with catch @ 006cbf58 */
                  *pppppppuVar21 = pppppppuVar20;
                  pppppppuVar26 = pppppppuVar20;
                  if ((undefined8 *******)*local_180 != (undefined8 *******)0x0) {
                    pppppppuVar26 = (undefined8 *******)*pppppppuVar21;
                    local_180 = (undefined8 *******)*local_180;
                  }
                  FUN_0043bbe4(local_178,pppppppuVar26);
                  local_170 = local_170 + 1;
                  pppppppuVar22 = pppppppuVar20;
LAB_006cbfb4:
                    /* catch() { ... } // from try @ 006cac04 with catch @ 006cbfb8 */
                  *(undefined1 *)(pppppppuVar22 + 4) = 1;
                }
                else {
                  do {
                    pppppppuVar29 = pppppppuVar21;
                    pppppppuVar20 = pppppppuVar26;
                    /* catch() { ... } // from try @ 006cb438 with catch @ 006cbeb8 */
                    iVar4 = *(int *)((long)pppppppuVar29 + 0x1c);
                    /* catch() { ... } // from try @ 006cb32c with catch @ 006cbec0 */
                    pppppppuVar26 = pppppppuVar20;
                    if (iVar11 <= iVar4) {
                      pppppppuVar26 = pppppppuVar29;
                    }
                    pppppppuVar21 = (undefined8 *******)pppppppuVar29[iVar4 < iVar11];
                  } while ((undefined8 *******)pppppppuVar29[iVar4 < iVar11] !=
                           (undefined8 *******)0x0);
                    /* catch() { ... } // from try @ 006cb19c with catch @ 006cbedc */
                  if ((undefined8 ********)pppppppuVar26 == &local_120) goto LAB_006cbef4;
                  pppppppuVar26 = pppppppuVar20;
                  if (iVar11 <= iVar4) {
                    pppppppuVar26 = pppppppuVar29;
                  }
                  if (iVar11 < *(int *)((long)pppppppuVar26 + 0x1c)) goto LAB_006cbef4;
                  if (iVar11 <= iVar4) {
                    pppppppuVar20 = pppppppuVar29;
                  }
                  iVar11 = *(int *)(pppppppuVar20 + 4);
                    /* catch() { ... } // from try @ 006ca428 with catch @ 006cbf98 */
                  FUN_006d6370(&local_128);
                    /* catch() { ... } // from try @ 006cb45c with catch @ 006cbf9c */
                  pppppppuVar26 = local_178;
                    /* catch() { ... } // from try @ 006cb2fc with catch @ 006cbfa0 */
                  if (iVar11 == -1) goto LAB_006cbf0c;
                }
                    /* catch() { ... } // from try @ 006caaec with catch @ 006cbfc0 */
                    /* catch() { ... } // from try @ 006ca9d4 with catch @ 006cbfc8 */
                if ((local_f0 != '\0') && (local_108 != (undefined8 *******)0x0)) {
                  local_100[0] = local_108;
                    /* catch() { ... } // from try @ 006ca87c with catch @ 006cbfd0 */
                  _ZdlPv(local_108);
                }
              }
            }
          }
        }
      }
      lVar15 = lVar15 + 8;
    } while (lVar15 != 0x10);
    lVar15 = FUN_00851550();
    FUN_009f6268(&local_128,(long)&fde_0040ed10 + lVar15);
                    /* catch() { ... } // from try @ 006cb420 with catch @ 006cc010
                       catch() { ... } // from try @ 006cb5d0 with catch @ 006cc010 */
    FUN_006cb598(&local_d0);
    piVar13 = piStack_c8;
                    /* catch() { ... } // from try @ 006cb0c0 with catch @ 006cc018 */
    if (local_d0 != piStack_c8) {
      piVar37 = local_d0;
                    /* catch() { ... } // from try @ 006cb084 with catch @ 006cc030
                       catch() { ... } // from try @ 006cb168 with catch @ 006cc030 */
                    /* catch() { ... } // from try @ 006cad64 with catch @ 006cc034 */
LAB_006cc04c:
                    /* catch() { ... } // from try @ 006c9c1c with catch @ 006cc050 */
      iVar11 = *piVar37;
      pppppppuVar26 = &local_178;
      pppppppuVar21 = local_178;
      if (local_178 != (undefined8 *******)0x0) {
        do {
          pppppppuVar20 = pppppppuVar21;
          pppppppuVar22 = pppppppuVar26;
          iVar12 = *(int *)((long)pppppppuVar20 + 0x1c);
                    /* catch() { ... } // from try @ 006ca3c4 with catch @ 006cc064
                       catch() { ... } // from try @ 006ca454 with catch @ 006cc064
                       catch() { ... } // from try @ 006ca700 with catch @ 006cc064 */
                    /* catch() { ... } // from try @ 006cb754 with catch @ 006cc074 */
          pppppppuVar26 = pppppppuVar22;
          if (iVar11 <= iVar12) {
            pppppppuVar26 = pppppppuVar20;
          }
          pppppppuVar21 = (undefined8 *******)pppppppuVar20[iVar12 < iVar11];
        } while ((undefined8 *******)pppppppuVar20[iVar12 < iVar11] != (undefined8 *******)0x0);
                    /* catch() { ... } // from try @ 006cb520 with catch @ 006cc088 */
        if ((undefined8 ********)pppppppuVar26 != &local_178) {
          if (iVar11 <= iVar12) {
            pppppppuVar22 = pppppppuVar20;
          }
          pppppppuVar21 = &local_178;
          if (*(int *)((long)pppppppuVar22 + 0x1c) <= iVar11) {
            pppppppuVar21 = pppppppuVar26;
          }
          pppppppuVar26 = local_178;
          if (&local_178 != (undefined8 ********)pppppppuVar21) {
            do {
                    /* catch() { ... } // from try @ 006c9d24 with catch @ 006cc130 */
              if (iVar11 < *(int *)((long)pppppppuVar26 + 0x1c)) {
                pppppppuVar26 = (undefined8 *******)*pppppppuVar26;
              }
              else {
                    /* catch() { ... } // from try @ 006c9e2c with catch @ 006cc138 */
                if (iVar11 <= *(int *)((long)pppppppuVar26 + 0x1c)) goto LAB_006cc038;
                pppppppuVar26 = (undefined8 *******)pppppppuVar26[1];
              }
              if (pppppppuVar26 == (undefined8 *******)0x0) {
                if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                  FUN_00442970("map::at:  key not found");
                }
                goto LAB_006ccbcc;
              }
            } while( true );
          }
        }
      }
      goto LAB_006cc0b8;
    }
LAB_006cc354:
                    /* try { // try from 006cc354 to 007cc553 has its CatchHandler @ 006cc1f4 */
    if (local_d0 != (int *)0x0) {
      piStack_c8 = local_d0;
      _ZdlPv(local_d0);
    }
    FUN_006cb598(local_e8);
    pwVar8 = local_e8[1];
    if (local_e8[0] != local_e8[1]) {
      pwVar38 = local_e8[0];
LAB_006cc3b0:
      wVar5 = *pwVar38;
      pppppppuVar26 = &local_120;
      pppppppuVar21 = local_120;
      while (pppppppuVar22 = pppppppuVar26, pppppppuVar21 != (undefined8 *******)0x0) {
        while (pppppppuVar26 = pppppppuVar21, *(wchar_t *)(pppppppuVar26 + 4) <= wVar5) {
          if (wVar5 <= *(wchar_t *)(pppppppuVar26 + 4)) goto LAB_006cc44c;
          pppppppuVar21 = (undefined8 *******)pppppppuVar26[1];
          if ((undefined8 *******)pppppppuVar26[1] == (undefined8 *******)0x0) {
            pppppppuVar22 = pppppppuVar26 + 1;
            goto LAB_006cc3f4;
          }
        }
        pppppppuVar21 = (undefined8 *******)*pppppppuVar26;
      }
LAB_006cc3f4:
      pppppppuVar21 = (undefined8 *******)_Znwm(0x40);
      *(wchar_t *)(pppppppuVar21 + 4) = wVar5;
      pppppppuVar21[6] = (undefined8 ******)0x0;
      pppppppuVar21[7] = (undefined8 ******)0x0;
      pppppppuVar21[5] = (undefined8 ******)0x0;
      *pppppppuVar21 = (undefined8 ******)0x0;
      pppppppuVar21[1] = (undefined8 ******)0x0;
      pppppppuVar21[2] = pppppppuVar26;
      *pppppppuVar22 = pppppppuVar21;
      pppppppuVar26 = pppppppuVar21;
      if ((long *)*local_128 != (long *)0x0) {
        local_128 = (long *)*local_128;
        pppppppuVar26 = (undefined8 *******)*pppppppuVar22;
      }
      FUN_0043bbe4(local_120,pppppppuVar26);
      local_118 = local_118 + 1;
      pppppppuVar26 = pppppppuVar21;
LAB_006cc44c:
      if ((*(int *)((long)pppppppuVar26[5] + 4) == 0) &&
         (pppppppuVar26 = &local_178, pppppppuVar21 = local_178,
         local_178 != (undefined8 *******)0x0)) {
        do {
          pppppppuVar20 = pppppppuVar21;
          pppppppuVar22 = pppppppuVar26;
          wVar6 = *(wchar_t *)((long)pppppppuVar20 + 0x1c);
          pppppppuVar26 = pppppppuVar22;
          if (wVar5 <= wVar6) {
            pppppppuVar26 = pppppppuVar20;
          }
          pppppppuVar21 = (undefined8 *******)pppppppuVar20[wVar6 < wVar5];
        } while ((undefined8 *******)pppppppuVar20[wVar6 < wVar5] != (undefined8 *******)0x0);
        if ((undefined8 ********)pppppppuVar26 != &local_178) {
          if (wVar5 <= wVar6) {
            pppppppuVar22 = pppppppuVar20;
          }
                    /* catch() { ... } // from try @ 006cc2ac with catch @ 006cc4a4 */
          pppppppuVar21 = &local_178;
          if (*(wchar_t *)((long)pppppppuVar22 + 0x1c) <= wVar5) {
            pppppppuVar21 = pppppppuVar26;
          }
          pppppppuVar26 = local_178;
                    /* catch() { ... } // from try @ 006cc338 with catch @ 006cc4ac */
          if (&local_178 != (undefined8 ********)pppppppuVar21) {
            do {
              if (wVar5 < *(wchar_t *)((long)pppppppuVar26 + 0x1c)) {
                pppppppuVar26 = (undefined8 *******)*pppppppuVar26;
              }
              else {
                if (wVar5 <= *(wchar_t *)((long)pppppppuVar26 + 0x1c)) goto LAB_006cc4e8;
                pppppppuVar26 = (undefined8 *******)pppppppuVar26[1];
              }
              if (pppppppuVar26 == (undefined8 *******)0x0) {
                if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                  FUN_00442970("map::at:  key not found");
                }
                goto LAB_006ccbcc;
              }
            } while( true );
          }
        }
      }
      goto LAB_006cc3a4;
    }
LAB_006cc710:
    if (local_e8[0] != (wchar_t *)0x0) {
      local_e8[1] = local_e8[0];
      _ZdlPv(local_e8[0]);
    }
    FUN_005c3ebc(&local_128,local_120);
    FUN_00676aa0(&local_180,local_178);
    if ((local_160 != (long *)0x0) &&
       (lVar15 = FUN_00c53da0(0xffffffffffffffff,local_160 + 1), lVar15 == 0)) {
      (**(code **)(*local_160 + 0x10))(local_160);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_160);
    }
  }
  FUN_005c17dc(&local_158,local_150);
  FUN_005c3ebc(&local_140,local_138[0]);
  if (*(long *)(lVar7 + 0x28) == local_70) {
    return;
  }
LAB_006ccbcc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
LAB_006cc814:
  if ((char)plVar27[4] != '\0') {
    piVar2 = (int *)param_1[1];
    if (piVar2 < (int *)param_1[2]) {
      piVar42 = piVar2 + 1;
      *piVar2 = iVar11;
    }
    else {
      pvVar39 = (void *)*param_1;
      lVar15 = (long)piVar2 - (long)pvVar39 >> 2;
      uVar16 = lVar15 + 1;
      if (uVar16 >> 0x3e != 0) {
        if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
          FUN_00470880(param_1);
        }
        goto LAB_006ccbcc;
      }
      uVar28 = (long)param_1[2] - (long)pvVar39;
      uVar31 = (long)uVar28 >> 1;
      if (uVar31 <= uVar16) {
        uVar31 = uVar16;
      }
      if (0x7ffffffffffffffb < uVar28) {
        uVar31 = 0x3fffffffffffffff;
      }
      if (uVar31 == 0) {
        pvVar23 = (void *)0x0;
      }
      else {
        if (uVar31 >> 0x3e != 0) {
          if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
            FUN_00440f00();
          }
          goto LAB_006ccbcc;
        }
        pvVar23 = (void *)_Znwm(uVar31 << 2);
      }
      piVar34 = (int *)((long)pvVar23 + lVar15 * 4);
      piVar42 = piVar34 + 1;
      *piVar34 = iVar11;
      memcpy(pvVar23,pvVar39,(long)piVar2 - (long)pvVar39);
      *param_1 = pvVar23;
      param_1[1] = piVar42;
      param_1[2] = (void *)((long)pvVar23 + uVar31 * 4);
      if (pvVar39 != (void *)0x0) {
        _ZdlPv(pvVar39);
      }
    }
    param_1[1] = piVar42;
  }
LAB_006cc778:
  piVar13 = piVar13 + 2;
  goto joined_r0x006cbfe8;
LAB_006cc038:
                    /* catch() { ... } // from try @ 006cab2c with catch @ 006cc038 */
                    /* catch() { ... } // from try @ 006ca990 with catch @ 006cc03c
                       catch() { ... } // from try @ 006cae0c with catch @ 006cc03c */
  if (*(char *)(pppppppuVar26 + 4) != '\0') goto LAB_006cc040;
LAB_006cc0b8:
  iVar12 = FUN_006cb8e4(iVar11);
  pppppppuVar26 = &local_120;
  pppppppuVar21 = local_120;
                    /* catch() { ... } // from try @ 006c9820 with catch @ 006cc0c8 */
                    /* catch() { ... } // from try @ 006c9ec4 with catch @ 006cc0cc */
  if ((iVar12 != -1) &&
     (pppppppuVar22 = &local_178, pppppppuVar20 = local_178, local_178 != (undefined8 *******)0x0))
  {
    do {
      pppppppuVar33 = pppppppuVar20;
      pppppppuVar29 = pppppppuVar22;
      iVar4 = *(int *)((long)pppppppuVar33 + 0x1c);
                    /* catch() { ... } // from try @ 006c9e74 with catch @ 006cc0e4 */
      pppppppuVar22 = pppppppuVar29;
      if (iVar12 <= iVar4) {
        pppppppuVar22 = pppppppuVar33;
      }
      pppppppuVar20 = (undefined8 *******)pppppppuVar33[iVar4 < iVar12];
    } while ((undefined8 *******)pppppppuVar33[iVar4 < iVar12] != (undefined8 *******)0x0);
    if ((undefined8 ********)pppppppuVar22 != &local_178) {
      if (iVar12 <= iVar4) {
        pppppppuVar29 = pppppppuVar33;
      }
      pppppppuVar20 = &local_178;
      if (*(int *)((long)pppppppuVar29 + 0x1c) <= iVar12) {
        pppppppuVar20 = pppppppuVar22;
      }
      pppppppuVar22 = local_178;
      if (&local_178 != (undefined8 ********)pppppppuVar20) {
        do {
                    /* catch() { ... } // from try @ 006c9648 with catch @ 006cc168 */
          if (iVar12 < *(int *)((long)pppppppuVar22 + 0x1c)) {
                    /* catch() { ... } // from try @ 006c9108 with catch @ 006cc158 */
            pppppppuVar22 = (undefined8 *******)*pppppppuVar22;
          }
          else {
                    /* catch() { ... } // from try @ 006c9988 with catch @ 006cc16c
                       catch() { ... } // from try @ 006c9b40 with catch @ 006cc16c */
            if (iVar12 <= *(int *)((long)pppppppuVar22 + 0x1c)) goto LAB_006cc180;
                    /* catch() { ... } // from try @ 006c9d60 with catch @ 006cc174
                       catch() { ... } // from try @ 006c9e1c with catch @ 006cc174 */
            pppppppuVar22 = (undefined8 *******)pppppppuVar22[1];
          }
          if (pppppppuVar22 == (undefined8 *******)0x0) {
            if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
              FUN_00442970("map::at:  key not found");
            }
            goto LAB_006ccbcc;
          }
        } while( true );
      }
    }
  }
  goto joined_r0x006cc194;
LAB_006cc180:
  if (*(char *)(pppppppuVar22 + 4) != '\0') goto LAB_006cc040;
joined_r0x006cc194:
  while (pppppppuVar22 = pppppppuVar26, pppppppuVar21 != (undefined8 *******)0x0) {
    while (pppppppuVar26 = pppppppuVar21, *(int *)(pppppppuVar26 + 4) <= iVar11) {
      if (iVar11 <= *(int *)(pppppppuVar26 + 4)) goto LAB_006cc220;
                    /* catch() { ... } // from try @ 006c93a4 with catch @ 006cc1bc */
      pppppppuVar21 = (undefined8 *******)pppppppuVar26[1];
      if ((undefined8 *******)pppppppuVar26[1] == (undefined8 *******)0x0) {
        pppppppuVar22 = pppppppuVar26 + 1;
        goto LAB_006cc1c8;
      }
    }
                    /* catch() { ... } // from try @ 006c949c with catch @ 006cc19c
                       catch() { ... } // from try @ 006c957c with catch @ 006cc19c
                       catch() { ... } // from try @ 006c975c with catch @ 006cc19c
                       catch() { ... } // from try @ 006c98cc with catch @ 006cc19c
                       catch() { ... } // from try @ 006c9a84 with catch @ 006cc19c */
                    /* catch() { ... } // from try @ 006c9ecc with catch @ 006cc1a0
                       catch() { ... } // from try @ 006c9fb4 with catch @ 006cc1a0
                       catch() { ... } // from try @ 006ca070 with catch @ 006cc1a0
                       catch() { ... } // from try @ 006ca114 with catch @ 006cc1a0
                       catch() { ... } // from try @ 006ca1e0 with catch @ 006cc1a0 */
    pppppppuVar21 = (undefined8 *******)*pppppppuVar26;
  }
LAB_006cc1c8:
  pppppppuVar21 = (undefined8 *******)_Znwm(0x40);
  *(int *)(pppppppuVar21 + 4) = iVar11;
  pppppppuVar21[6] = (undefined8 ******)0x0;
  pppppppuVar21[7] = (undefined8 ******)0x0;
  pppppppuVar21[5] = (undefined8 ******)0x0;
  *pppppppuVar21 = (undefined8 ******)0x0;
  pppppppuVar21[1] = (undefined8 ******)0x0;
  pppppppuVar21[2] = pppppppuVar26;
  *pppppppuVar22 = pppppppuVar21;
                    /* try { // try from 006cc1f4 to 007cc2ab has its CatchHandler @ 006cc1f4
                       catch() { ... } // from try @ 006cc1f4 with catch @ 006cc1f4
                       catch() { ... } // from try @ 006cc354 with catch @ 006cc1f4 */
  pppppppuVar26 = pppppppuVar21;
  if ((long *)*local_128 != (long *)0x0) {
    local_128 = (long *)*local_128;
    pppppppuVar26 = (undefined8 *******)*pppppppuVar22;
  }
  FUN_0043bbe4(local_120,pppppppuVar26);
  local_118 = local_118 + 1;
  pppppppuVar26 = pppppppuVar21;
LAB_006cc220:
  if (*(int *)((long)pppppppuVar26[5] + 4) == 0) {
    lVar15 = FUN_00851550();
    plVar18 = (long *)((long)&QWORD_00436bb1 + lVar15 + 7);
    plVar27 = (long *)*plVar18;
    plVar30 = plVar18;
    plVar32 = plVar27;
    if (plVar27 != (long *)0x0) {
      do {
        if (iVar11 <= *(int *)((long)plVar32 + 0x1c)) {
          plVar30 = plVar32;
        }
        plVar1 = plVar32 + (*(int *)((long)plVar32 + 0x1c) < iVar11);
        plVar32 = (long *)*plVar1;
      } while ((long *)*plVar1 != (long *)0x0);
      if ((plVar30 != plVar18) && (*(int *)((long)plVar30 + 0x1c) <= iVar11)) {
        do {
          if (iVar11 < *(int *)((long)plVar27 + 0x1c)) {
            plVar27 = (long *)*plVar27;
          }
          else {
            if (iVar11 <= *(int *)((long)plVar27 + 0x1c)) goto LAB_006cc298;
            plVar27 = (long *)plVar27[1];
          }
          if (plVar27 == (long *)0x0) {
            if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
              FUN_00442970("map::at:  key not found");
            }
            goto LAB_006ccbcc;
          }
        } while( true );
      }
    }
  }
LAB_006cc040:
  piVar37 = piVar37 + 2;
                    /* catch() { ... } // from try @ 006caa14 with catch @ 006cc044 */
                    /* catch() { ... } // from try @ 006ca840 with catch @ 006cc048 */
  if (piVar37 == piVar13) goto LAB_006cc354;
  goto LAB_006cc04c;
LAB_006cc298:
  if ((char)plVar27[4] != '\0') {
    piVar2 = (int *)param_1[1];
                    /* try { // try from 006cc2ac to 007cc2b3 has its CatchHandler @ 006cc4a4 */
    if (piVar2 < (int *)param_1[2]) {
      piVar34 = piVar2 + 1;
      *piVar2 = iVar11;
    }
    else {
      pvVar39 = (void *)*param_1;
      lVar15 = (long)piVar2 - (long)pvVar39 >> 2;
      uVar16 = lVar15 + 1;
      if (uVar16 >> 0x3e != 0) {
        if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
          FUN_00470880(param_1);
        }
        goto LAB_006ccbcc;
      }
      uVar28 = (long)param_1[2] - (long)pvVar39;
      uVar31 = (long)uVar28 >> 1;
      if (uVar31 <= uVar16) {
        uVar31 = uVar16;
      }
      if (0x7ffffffffffffffb < uVar28) {
        uVar31 = 0x3fffffffffffffff;
      }
      if (uVar31 == 0) {
        pvVar23 = (void *)0x0;
      }
      else {
        if (uVar31 >> 0x3e != 0) {
          if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
            FUN_00440f00();
          }
          goto LAB_006ccbcc;
        }
        pvVar23 = (void *)_Znwm(uVar31 << 2);
                    /* try { // try from 006cc304 to 007cc313 has its CatchHandler @ 006cc534 */
      }
      piVar42 = (int *)((long)pvVar23 + lVar15 * 4);
      piVar34 = piVar42 + 1;
      *piVar42 = iVar11;
      memcpy(pvVar23,pvVar39,(long)piVar2 - (long)pvVar39);
      *param_1 = pvVar23;
      param_1[1] = piVar34;
      param_1[2] = (void *)((long)pvVar23 + uVar31 * 4);
                    /* try { // try from 006cc338 to 007cc353 has its CatchHandler @ 006cc4ac */
      if (pvVar39 != (void *)0x0) {
        _ZdlPv(pvVar39);
      }
    }
    param_1[1] = piVar34;
  }
  goto LAB_006cc040;
LAB_006cc4e8:
  pppppppuVar21 = &local_120;
  pppppppuVar22 = local_120;
  if (*(char *)(pppppppuVar26 + 4) == '\0') goto LAB_006cc3a4;
  while (pppppppuVar26 = pppppppuVar21, pppppppuVar22 != (undefined8 *******)0x0) {
    while (pppppppuVar21 = pppppppuVar22, *(wchar_t *)(pppppppuVar21 + 4) <= wVar5) {
      if (wVar5 <= *(wchar_t *)(pppppppuVar21 + 4)) goto LAB_006cc588;
      pppppppuVar22 = (undefined8 *******)pppppppuVar21[1];
      if ((undefined8 *******)pppppppuVar21[1] == (undefined8 *******)0x0) {
        pppppppuVar26 = pppppppuVar21 + 1;
        goto LAB_006cc530;
      }
    }
    pppppppuVar22 = (undefined8 *******)*pppppppuVar21;
  }
LAB_006cc530:
                    /* catch() { ... } // from try @ 006cc304 with catch @ 006cc534 */
  pppppppuVar22 = (undefined8 *******)_Znwm(0x40);
  *(wchar_t *)(pppppppuVar22 + 4) = wVar5;
  pppppppuVar22[6] = (undefined8 ******)0x0;
  pppppppuVar22[7] = (undefined8 ******)0x0;
  pppppppuVar22[5] = (undefined8 ******)0x0;
  *pppppppuVar22 = (undefined8 ******)0x0;
  pppppppuVar22[1] = (undefined8 ******)0x0;
  pppppppuVar22[2] = pppppppuVar21;
  *pppppppuVar26 = pppppppuVar22;
  pppppppuVar21 = pppppppuVar22;
  if ((long *)*local_128 != (long *)0x0) {
    local_128 = (long *)*local_128;
    pppppppuVar21 = (undefined8 *******)*pppppppuVar26;
  }
  FUN_0043bbe4(local_120,pppppppuVar21);
  local_118 = local_118 + 1;
  pppppppuVar21 = pppppppuVar22;
LAB_006cc588:
  iVar11 = *(int *)(pppppppuVar21[5] + 1);
  piStack_c8 = _UNK_002dff40;
  local_d0 = _DAT_002dff38;
  local_b8 = _UNK_002dff50;
  local_c0 = _DAT_002dff48;
  uStack_a8 = _UNK_002dff60;
  local_b0 = _DAT_002dff58;
  local_a0 = 0x3ef;
  FUN_006cb10c(&local_108,&local_d0,7,&uStack_109);
  pppppppuVar26 = local_100;
  pppppppuVar21 = local_100[0];
  if (local_100[0] == (undefined8 *******)0x0) {
LAB_006cc60c:
    FUN_006d6370(&local_108);
    pwVar36 = (wchar_t *)param_1[1];
  }
  else {
    do {
      pppppppuVar20 = pppppppuVar21;
      pppppppuVar22 = pppppppuVar26;
      iVar12 = *(int *)((long)pppppppuVar20 + 0x1c);
      pppppppuVar26 = pppppppuVar22;
      if (iVar11 <= iVar12) {
        pppppppuVar26 = pppppppuVar20;
      }
      pppppppuVar21 = (undefined8 *******)pppppppuVar20[iVar12 < iVar11];
    } while ((undefined8 *******)pppppppuVar20[iVar12 < iVar11] != (undefined8 *******)0x0);
    if ((undefined8 ********)pppppppuVar26 == local_100) goto LAB_006cc60c;
    pppppppuVar26 = pppppppuVar22;
    if (iVar11 <= iVar12) {
      pppppppuVar26 = pppppppuVar20;
    }
    if (iVar11 < *(int *)((long)pppppppuVar26 + 0x1c)) goto LAB_006cc60c;
    if (iVar11 <= iVar12) {
      pppppppuVar22 = pppppppuVar20;
    }
    wVar6 = *(wchar_t *)(pppppppuVar22 + 4);
    FUN_006d6370(&local_108);
    pwVar36 = (wchar_t *)param_1[1];
    if (wVar6 != L'\xffffffff') {
      pwVar24 = wmemchr((wchar_t *)*param_1,wVar6,(long)pwVar36 - (long)*param_1 >> 2);
      pwVar35 = pwVar36;
      if (pwVar24 != (wchar_t *)0x0) {
        pwVar35 = pwVar24;
      }
      pwVar36 = (wchar_t *)param_1[1];
      if (pwVar35 == pwVar36) goto LAB_006cc3a4;
    }
  }
  if (pwVar36 < (wchar_t *)param_1[2]) {
    pwVar35 = pwVar36 + 1;
    *pwVar36 = wVar5;
  }
  else {
    pvVar39 = (void *)*param_1;
    lVar15 = (long)pwVar36 - (long)pvVar39 >> 2;
    uVar16 = lVar15 + 1;
    if (uVar16 >> 0x3e != 0) {
      if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
        FUN_00470880(param_1);
      }
      goto LAB_006ccbcc;
    }
    uVar28 = (long)param_1[2] - (long)pvVar39;
    uVar31 = (long)uVar28 >> 1;
    if (uVar31 <= uVar16) {
      uVar31 = uVar16;
    }
    if (0x7ffffffffffffffb < uVar28) {
      uVar31 = 0x3fffffffffffffff;
    }
    if (uVar31 == 0) {
      pvVar23 = (void *)0x0;
    }
    else {
      if (uVar31 >> 0x3e != 0) {
        if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
          FUN_00440f00();
        }
        goto LAB_006ccbcc;
      }
      pvVar23 = (void *)_Znwm(uVar31 << 2);
    }
    pwVar24 = (wchar_t *)((long)pvVar23 + lVar15 * 4);
    pwVar35 = pwVar24 + 1;
    *pwVar24 = wVar5;
    memcpy(pvVar23,pvVar39,(long)pwVar36 - (long)pvVar39);
    *param_1 = pvVar23;
    param_1[1] = pwVar35;
    param_1[2] = (void *)((long)pvVar23 + uVar31 * 4);
    if (pvVar39 != (void *)0x0) {
      _ZdlPv(pvVar39);
    }
  }
  param_1[1] = pwVar35;
LAB_006cc3a4:
  pwVar38 = pwVar38 + 2;
  if (pwVar38 == pwVar8) goto LAB_006cc710;
  goto LAB_006cc3b0;
}

~~~
