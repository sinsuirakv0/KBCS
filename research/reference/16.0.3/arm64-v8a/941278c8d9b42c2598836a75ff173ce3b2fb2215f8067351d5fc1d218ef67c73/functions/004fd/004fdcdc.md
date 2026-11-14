# 004fdcdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004fdcdc",
  "name": "_ZN5Botan19host_wildcard_matchERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_",
  "size": 2052,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f13bd8d65a2d0b66c13eab2d9e6c16ddbc686cc0ed67c6e340f72ab53895707",
  "source_text_sha256": "1f13bd8d65a2d0b66c13eab2d9e6c16ddbc686cc0ed67c6e340f72ab53895707"
}
~~~

## 呼び出し元

- [00c5a9c0](../00c5a/00c5a9c0.md)

## 呼び出し先

- [0043be80](../0043b/0043be80.md)
- [0043e138](../0043e/0043e138.md)
- [00440e60](../00440/00440e60.md)
- [00442120](../00442/00442120.md)
- [004421f4](../00442/004421f4.md)
- [004738a0](../00473/004738a0.md)
- [004c0a64](../004c0/004c0a64.md)
- [004c3bb0](../004c3/004c3bb0.md)
- [004fca3c](../004fc/004fca3c.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590f0](../00c59/00c590f0.md)
- [00c59670](../00c59/00c59670.md)
- [00c5a330](../00c5a/00c5a330.md)
- [00c5a9d0](../00c5a/00c5a9d0.md)

## 疑似コード / UTF-8 14659 bytes

~~~c

void _ZN5Botan19host_wildcard_matchERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_
               (byte *param_1,byte *param_2)

{
  char *pcVar1;
  byte bVar2;
  long lVar3;
  bool bVar4;
  int iVar5;
  uint uVar6;
  long lVar7;
  long lVar8;
  ulong uVar9;
  byte bVar10;
  ulong uVar11;
  ulong uVar12;
  byte *pbVar13;
  byte *pbVar14;
  byte *pbVar15;
  ulong uVar16;
  long lVar17;
  long lVar18;
  long lVar19;
  long lVar20;
  long lVar21;
  long lVar22;
  long lVar23;
  long lVar24;
  long lVar25;
  undefined8 uVar26;
  long lVar27;
  long lVar28;
  long lVar29;
  long lVar30;
  long lVar31;
  long lVar32;
  long lVar33;
  long lVar34;
  long lVar35;
  long lVar36;
  long lVar37;
  long lVar38;
  long lVar39;
  long lVar40;
  long lVar41;
  long lVar42;
  long lVar43;
  long lVar44;
  long lVar45;
  long lVar46;
  long lVar47;
  undefined8 uVar48;
  undefined8 uVar49;
  undefined8 uVar50;
  byte local_148 [16];
  void *local_138;
  ulong local_130;
  ulong uStack_128;
  void *local_120;
  ulong *local_118;
  long lStack_110;
  undefined8 local_108;
  byte local_100;
  char local_ff [7];
  ulong local_f8;
  char *local_f0;
  byte local_e8 [8];
  ulong local_e0;
  void *local_d8;
  byte local_d0 [16];
  void *local_c0;
  byte local_b8 [16];
  void *local_a8;
  ulong local_a0;
  ulong uStack_98;
  void *local_90;
  byte local_88 [16];
  void *local_78;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  bVar10 = *param_1;
  bVar2 = *param_2;
  uVar11 = (ulong)(bVar10 >> 1);
  uVar9 = uVar11;
  if ((bVar10 & 1) != 0) {
    uVar9 = *(size_t *)(param_1 + 8);
  }
  uVar12 = (ulong)(bVar2 >> 1);
  if ((bVar2 & 1) != 0) {
    uVar12 = *(ulong *)(param_2 + 8);
  }
  if (uVar9 == uVar12) {
    pbVar13 = *(byte **)(param_2 + 0x10);
    if ((bVar2 & 1) == 0) {
      pbVar13 = param_2 + 1;
    }
    if ((bVar10 & 1) == 0) {
      pbVar14 = param_1;
      if (1 < bVar10) {
        do {
          if (pbVar14[1] != *pbVar13) goto LAB_004fdd90;
          uVar11 = uVar11 - 1;
          pbVar13 = pbVar13 + 1;
          pbVar14 = pbVar14 + 1;
        } while (uVar11 != 0);
      }
    }
    else {
      iVar5 = memcmp(*(void **)(param_1 + 0x10),pbVar13,*(size_t *)(param_1 + 8));
      if (iVar5 != 0) goto LAB_004fdd90;
    }
    bVar4 = true;
    goto LAB_004fe474;
  }
LAB_004fdd90:
  pbVar13 = *(byte **)(param_1 + 0x10);
  if ((bVar10 & 1) == 0) {
    pbVar13 = param_1 + 1;
  }
  if (uVar9 != 0) {
    if (uVar9 < 8) {
      uVar11 = 0;
      pbVar14 = pbVar13;
LAB_004fe024:
      do {
        pbVar15 = pbVar14 + 1;
        if (*pbVar14 == 0x2a) {
          uVar11 = uVar11 + 1;
        }
        pbVar14 = pbVar15;
      } while (pbVar15 != pbVar13 + uVar9);
    }
    else if (uVar9 < 0x20) {
      uVar11 = 0;
      uVar12 = 0;
LAB_004fdf84:
      lVar8 = 0;
      lVar17 = 0;
      lVar18 = 0;
      lVar19 = 0;
      lVar20 = 0;
      lVar21 = 0;
      lVar22 = 0;
      uVar16 = uVar9 & 0xfffffffffffffff8;
      pbVar14 = pbVar13 + uVar16;
      lVar7 = uVar12 - uVar16;
      pbVar15 = pbVar13 + uVar12;
      do {
        uVar26 = *(undefined8 *)pbVar15;
        lVar7 = lVar7 + 8;
        lVar21 = lVar21 + (ulong)(-((char)((ulong)uVar26 >> 0x30) == '*') & 1);
        lVar22 = lVar22 + (ulong)(-((char)((ulong)uVar26 >> 0x38) == '*') & 1);
        lVar17 = lVar17 + (ulong)(-((char)((ulong)uVar26 >> 0x10) == '*') & 1);
        lVar18 = lVar18 + (ulong)(-((char)((ulong)uVar26 >> 0x18) == '*') & 1);
        uVar11 = uVar11 + (-((char)uVar26 == '*') & 1);
        lVar8 = lVar8 + (ulong)(-((char)((ulong)uVar26 >> 8) == '*') & 1);
        lVar19 = lVar19 + (ulong)(-((char)((ulong)uVar26 >> 0x20) == '*') & 1);
        lVar20 = lVar20 + (ulong)(-((char)((ulong)uVar26 >> 0x28) == '*') & 1);
        pbVar15 = pbVar15 + 8;
      } while (lVar7 != 0);
      uVar11 = uVar11 + lVar19 + lVar17 + lVar21 + lVar8 + lVar20 + lVar18 + lVar22;
      if (uVar9 != uVar16) goto LAB_004fe024;
    }
    else {
      lVar7 = 0;
      lVar8 = 0;
      lVar25 = 0;
      lVar27 = 0;
      lVar17 = 0;
      lVar18 = 0;
      pbVar14 = pbVar13 + 0x10;
      lVar32 = 0;
      lVar33 = 0;
      lVar21 = 0;
      lVar22 = 0;
      lVar23 = 0;
      lVar24 = 0;
      lVar19 = 0;
      lVar20 = 0;
      lVar40 = 0;
      lVar41 = 0;
      lVar30 = 0;
      lVar31 = 0;
      lVar42 = 0;
      lVar43 = 0;
      lVar28 = 0;
      lVar29 = 0;
      lVar44 = 0;
      lVar45 = 0;
      lVar36 = 0;
      lVar37 = 0;
      lVar38 = 0;
      lVar39 = 0;
      lVar34 = 0;
      lVar35 = 0;
      lVar46 = 0;
      lVar47 = 0;
      uVar12 = uVar9 & 0xffffffffffffffe0;
      uVar11 = uVar12;
      do {
        uVar48 = *(undefined8 *)(pbVar14 + -8);
        uVar26 = *(undefined8 *)(pbVar14 + -0x10);
        uVar50 = *(undefined8 *)(pbVar14 + 8);
        uVar49 = *(undefined8 *)pbVar14;
        uVar11 = uVar11 - 0x20;
        pbVar14 = pbVar14 + 0x20;
        lVar19 = lVar19 + (ulong)(-((char)((ulong)uVar48 >> 0x20) == '*') & 1);
        lVar20 = lVar20 + (ulong)(-((char)((ulong)uVar48 >> 0x28) == '*') & 1);
        lVar40 = lVar40 + (ulong)(-((char)((ulong)uVar48 >> 0x30) == '*') & 1);
        lVar41 = lVar41 + (ulong)(-((char)((ulong)uVar48 >> 0x38) == '*') & 1);
        lVar23 = lVar23 + (ulong)(-((char)((ulong)uVar48 >> 0x10) == '*') & 1);
        lVar24 = lVar24 + (ulong)(-((char)((ulong)uVar48 >> 0x18) == '*') & 1);
        lVar32 = lVar32 + (ulong)(-((char)((ulong)uVar26 >> 0x30) == '*') & 1);
        lVar33 = lVar33 + (ulong)(-((char)((ulong)uVar26 >> 0x38) == '*') & 1);
        lVar21 = lVar21 + (ulong)(-((char)uVar48 == '*') & 1);
        lVar22 = lVar22 + (ulong)(-((char)((ulong)uVar48 >> 8) == '*') & 1);
        lVar17 = lVar17 + (ulong)(-((char)((ulong)uVar26 >> 0x20) == '*') & 1);
        lVar18 = lVar18 + (ulong)(-((char)((ulong)uVar26 >> 0x28) == '*') & 1);
        lVar25 = lVar25 + (ulong)(-((char)((ulong)uVar26 >> 0x10) == '*') & 1);
        lVar27 = lVar27 + (ulong)(-((char)((ulong)uVar26 >> 0x18) == '*') & 1);
        lVar7 = lVar7 + (ulong)(-((char)uVar26 == '*') & 1);
        lVar8 = lVar8 + (ulong)(-((char)((ulong)uVar26 >> 8) == '*') & 1);
        lVar36 = lVar36 + (ulong)(-((char)uVar50 == '*') & 1);
        lVar37 = lVar37 + (ulong)(-((char)((ulong)uVar50 >> 8) == '*') & 1);
        lVar46 = lVar46 + (ulong)(-((char)((ulong)uVar50 >> 0x30) == '*') & 1);
        lVar47 = lVar47 + (ulong)(-((char)((ulong)uVar50 >> 0x38) == '*') & 1);
        lVar34 = lVar34 + (ulong)(-((char)((ulong)uVar50 >> 0x20) == '*') & 1);
        lVar35 = lVar35 + (ulong)(-((char)((ulong)uVar50 >> 0x28) == '*') & 1);
        lVar44 = lVar44 + (ulong)(-((char)((ulong)uVar49 >> 0x30) == '*') & 1);
        lVar45 = lVar45 + (ulong)(-((char)((ulong)uVar49 >> 0x38) == '*') & 1);
        lVar38 = lVar38 + (ulong)(-((char)((ulong)uVar50 >> 0x10) == '*') & 1);
        lVar39 = lVar39 + (ulong)(-((char)((ulong)uVar50 >> 0x18) == '*') & 1);
        lVar42 = lVar42 + (ulong)(-((char)((ulong)uVar49 >> 0x10) == '*') & 1);
        lVar43 = lVar43 + (ulong)(-((char)((ulong)uVar49 >> 0x18) == '*') & 1);
        lVar30 = lVar30 + (ulong)(-((char)uVar49 == '*') & 1);
        lVar31 = lVar31 + (ulong)(-((char)((ulong)uVar49 >> 8) == '*') & 1);
        lVar28 = lVar28 + (ulong)(-((char)((ulong)uVar49 >> 0x20) == '*') & 1);
        lVar29 = lVar29 + (ulong)(-((char)((ulong)uVar49 >> 0x28) == '*') & 1);
      } while (uVar11 != 0);
      uVar11 = lVar30 + lVar7 + lVar36 + lVar21 + lVar28 + lVar17 + lVar34 + lVar19 +
               lVar42 + lVar25 + lVar38 + lVar23 + lVar44 + lVar32 + lVar46 + lVar40 +
               lVar31 + lVar8 + lVar37 + lVar22 + lVar29 + lVar18 + lVar35 + lVar20 +
               lVar43 + lVar27 + lVar39 + lVar24 + lVar45 + lVar33 + lVar47 + lVar41;
      if (uVar9 != uVar12) {
        if ((uVar9 & 0x18) == 0) {
          pbVar14 = pbVar13 + uVar12;
          goto LAB_004fe024;
        }
        goto LAB_004fdf84;
      }
    }
    if (((uVar11 < 2) && (2 < uVar9)) &&
       (lVar7 = _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
                          (param_2,0x2e,0), lVar7 != -1)) {
      uVar9 = (ulong)(*param_2 >> 1);
      if ((*param_2 & 1) != 0) {
        uVar9 = *(ulong *)(param_2 + 8);
      }
      if ((lVar7 != uVar9 - 1) &&
         (lVar8 = _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
                            (param_1,0x2e,0), lVar8 != -1)) {
        uVar9 = (ulong)(*param_1 >> 1);
        if ((*param_1 & 1) != 0) {
          uVar9 = *(ulong *)(param_1 + 8);
        }
        if (lVar8 != uVar9 - 1) {
          FUN_00442120(local_b8,param_2,lVar7 + 1,0xffffffffffffffff);
          FUN_00442120(local_d0,param_1,lVar8 + 1,0xffffffffffffffff);
          uVar9 = FUN_004c0a64(local_b8,local_d0);
          if ((uVar9 & 1) == 0) {
            FUN_00442120(local_e8,param_2,0,lVar7);
            uVar9 = (ulong)(local_e8[0] >> 1);
            if ((local_e8[0] & 1) != 0) {
              uVar9 = local_e0;
            }
            if (uVar9 == 0) {
              uVar6 = 0;
              bVar4 = false;
            }
            else {
              FUN_00442120(&local_100,param_1,0,lVar8);
              uVar9 = FUN_004421f4(&local_100,&DAT_002b7499);
              if ((uVar9 & 1) == 0) {
                local_118 = (ulong *)0x0;
                lStack_110 = 0;
                local_108 = 0;
                pcVar1 = local_f0;
                if ((local_100 & 1) == 0) {
                  pcVar1 = local_ff;
                }
                if (*pcVar1 == '*') {
                  FUN_0043e138(&local_a0,&DAT_002a64e6);
                  uVar9 = (ulong)(local_100 >> 1);
                  if ((local_100 & 1) != 0) {
                    uVar9 = local_f8;
                  }
                  FUN_00442120(local_88,&local_100,1,uVar9);
                  FUN_004738a0(&local_130,&local_a0,2);
LAB_004fe244:
                  FUN_004fca3c(&local_118,&local_130);
                  FUN_00440e60(&local_130);
                  if ((local_88[0] & 1) != 0) {
                    _ZdlPv(local_78);
                  }
                  if ((local_a0 & 1) != 0) {
                    _ZdlPv(local_90);
                  }
                }
                else {
                  uVar9 = (ulong)(local_100 >> 1);
                  if ((local_100 & 1) != 0) {
                    uVar9 = local_f8;
                  }
                  if (pcVar1[uVar9 - 1] == '*') {
                    FUN_00442120(&local_a0,&local_100,0);
                    FUN_0043e138(local_88,&DAT_002a64e6);
                    FUN_004738a0(&local_130,&local_a0,2);
                    goto LAB_004fe244;
                  }
                  _ZN5Botan8split_onERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc
                            (&local_a0,&local_100,0x2a);
                  FUN_004fca3c(&local_118,&local_a0);
                  FUN_00440e60(&local_a0);
                }
                bVar4 = lStack_110 - (long)local_118 == 0x30;
                if (bVar4) {
                  if ((*local_118 & 1) == 0) {
                    local_90 = (void *)local_118[2];
                    uStack_98 = local_118[1];
                    local_a0 = *local_118;
                  }
                  else {
                    FUN_0043be80(&local_a0,local_118[2],local_118[1]);
                  }
                  if ((local_118[3] & 1) == 0) {
                    uStack_128 = local_118[4];
                    local_130 = local_118[3];
                    local_120 = (void *)local_118[5];
                  }
                  else {
                    FUN_0043be80(&local_130,local_118[5],local_118[4]);
                  }
                  uVar9 = local_a0 >> 1 & 0x7f;
                  if ((local_a0 & 1) != 0) {
                    uVar9 = uStack_98;
                  }
                  FUN_00442120(local_148,local_e8,0,uVar9);
                  uVar9 = FUN_004c3bb0(local_148,&local_a0);
                  if ((local_148[0] & 1) != 0) {
                    _ZdlPv(local_138);
                  }
                  if ((uVar9 & 1) != 0) {
                    uVar9 = local_a0 >> 1 & 0x7f;
                    if ((local_a0 & 1) != 0) {
                      uVar9 = uStack_98;
                    }
                    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
                              (local_e8,0,uVar9);
                  }
                  bVar10 = (byte)local_130 & 1;
                  uVar9 = (ulong)((byte)local_130 >> 1);
                  if ((local_130 & 1) != 0) {
                    uVar9 = uStack_128;
                  }
                  if (uVar9 == 0) {
                    uVar6 = 0;
                  }
                  else {
                    uVar11 = (ulong)(local_e8[0] >> 1);
                    if ((local_e8[0] & 1) != 0) {
                      uVar11 = local_e0;
                    }
                    if (uVar11 < uVar9) {
                      uVar6 = 1;
                    }
                    else {
                      FUN_00442120(local_148,local_e8,uVar11 - uVar9);
                      uVar6 = FUN_004c3bb0(local_148,&local_130);
                      if ((local_148[0] & 1) != 0) {
                        _ZdlPv(local_138);
                      }
                      uVar6 = uVar6 ^ 1;
                      bVar10 = (byte)local_130 & 1;
                    }
                  }
                  if (bVar10 != 0) {
                    _ZdlPv(local_120);
                  }
                  if ((local_a0 & 1) != 0) {
                    _ZdlPv(local_90);
                  }
                }
                else {
                  uVar6 = 0;
                }
                FUN_00440e60(&local_118);
              }
              else {
                uVar6 = 0;
                bVar4 = true;
              }
              if ((local_100 & 1) != 0) {
                _ZdlPv(local_f0);
              }
            }
            if ((local_e8[0] & 1) != 0) {
              _ZdlPv(local_d8);
            }
          }
          else {
            uVar6 = 0;
            bVar4 = false;
          }
          if ((local_d0[0] & 1) != 0) {
            _ZdlPv(local_c0);
          }
          if ((local_b8[0] & 1) != 0) {
            _ZdlPv(local_a8);
          }
          if ((uVar6 & 1) == 0) goto LAB_004fe474;
        }
      }
    }
  }
  bVar4 = false;
LAB_004fe474:
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(bVar4);
}

~~~
