# 004fbebc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004fbebc",
  "name": "_ZN5Botan19get_files_recursiveERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 1796,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee99915e1c087a3494ff642a4067f8c293fef6fa4dcf6b2150c3a76c124b651b",
  "source_text_sha256": "ee99915e1c087a3494ff642a4067f8c293fef6fa4dcf6b2150c3a76c124b651b"
}
~~~

## 呼び出し元

- [00c59430](../00c59/00c59430.md)

## 呼び出し先

- [0043b724](../0043b/0043b724.md)
- [0043bae0](../0043b/0043bae0.md)
- [00459d34](../00459/00459d34.md)
- [00539edc](../00539/00539edc.md)
- [0053a074](../0053a/0053a074.md)
- [0053aa24](../0053a/0053aa24.md)
- [0053aa28](../0053a/0053aa28.md)
- [0053aa2c](../0053a/0053aa2c.md)
- [00540d3c](../00540/00540d3c.md)
- [00545bfc](../00545/00545bfc.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57b40](../00c57/00c57b40.md)
- [00c57b80](../00c57/00c57b80.md)
- [00c57be0](../00c57/00c57be0.md)
- [00c59440](../00c59/00c59440.md)
- [00c59450](../00c59/00c59450.md)
- [00c59460](../00c59/00c59460.md)

## 疑似コード / UTF-8 11070 bytes

~~~c

void _ZN5Botan19get_files_recursiveERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
               (ulong *param_1,byte *param_2)

{
  ulong uVar1;
  size_t __n;
  ulong uVar2;
  char *pcVar3;
  long lVar4;
  byte *pbVar5;
  DIR *pDVar6;
  bool bVar7;
  int iVar8;
  undefined8 *puVar9;
  dirent *pdVar10;
  size_t sVar11;
  short *psVar12;
  void *__dest;
  undefined ***pppuVar13;
  long lVar14;
  ulong uVar15;
  byte *pbVar16;
  ulong uVar17;
  ulong *puVar18;
  byte *pbVar19;
  byte bVar20;
  short *psVar21;
  undefined8 uVar22;
  undefined8 uVar23;
  ulong *local_1d8;
  ulong *local_1d0;
  ulong *puStack_1c8;
  stat local_1c0;
  char *local_130;
  ulong local_128;
  size_t local_120;
  short *local_118;
  ulong local_110;
  size_t sStack_108;
  char *local_100;
  undefined8 local_f0;
  undefined8 *puStack_e8;
  undefined8 *local_e0;
  undefined8 uStack_d8;
  ulong local_d0;
  long local_c8;
  DIR *local_c0;
  undefined **local_b0;
  undefined *local_a8;
  undefined ***local_90;
  long local_78;
  
  lVar4 = tpidr_el0;
  local_78 = *(long *)(lVar4 + 0x28);
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  local_1d8 = (ulong *)0x0;
  local_1d0 = (ulong *)0x0;
  puStack_1c8 = (ulong *)0x0;
  uStack_d8 = 0;
  local_e0 = (undefined8 *)0x0;
  local_c8 = 0;
  local_d0 = 0;
  puStack_e8 = (undefined8 *)0x0;
  local_f0 = 0;
  FUN_0053a074(&local_f0);
  if (local_e0 == puStack_e8) {
    puVar9 = (undefined8 *)0x0;
    bVar20 = *param_2;
  }
  else {
    puVar9 = (undefined8 *)
             (puStack_e8[(local_c8 + local_d0) / 0xaa] + ((local_c8 + local_d0) % 0xaa) * 0x18);
    bVar20 = *param_2;
  }
  if ((bVar20 & 1) == 0) {
    uVar23 = *(undefined8 *)(param_2 + 8);
    uVar22 = *(undefined8 *)param_2;
    puVar9[2] = *(undefined8 *)(param_2 + 0x10);
    puVar9[1] = uVar23;
    *puVar9 = uVar22;
  }
  else {
    FUN_0043bae0(puVar9,*(undefined8 *)(param_2 + 0x10),*(undefined8 *)(param_2 + 8));
  }
  bVar7 = local_c8 == -1;
  local_c8 = local_c8 + 1;
  if (bVar7) {
    FUN_00539edc(&local_f0);
  }
  else {
    psVar21 = (short *)((ulong)&local_128 | 1);
    do {
      uVar15 = local_d0 / 0xaa;
      uVar17 = local_d0 % 0xaa;
      puVar18 = (ulong *)(puStack_e8[uVar15] + uVar17 * 0x18);
      if ((*puVar18 & 1) == 0) {
        local_100 = (char *)puVar18[2];
        sStack_108 = puVar18[1];
        local_110 = *puVar18;
      }
      else {
        FUN_0043bae0(&local_110,puVar18[2],puVar18[1]);
        uVar15 = local_d0 / 0xaa;
        uVar17 = local_d0 % 0xaa;
      }
      pbVar16 = (byte *)(puStack_e8[uVar15] + uVar17 * 0x18);
      if ((*pbVar16 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar16 + 0x10));
      }
      local_d0 = local_d0 + 1;
      local_c8 = local_c8 + -1;
      if (0x153 < local_d0) {
        _ZdlPv((void *)*puStack_e8);
        puStack_e8 = puStack_e8 + 1;
        local_d0 = local_d0 - 0xaa;
      }
      pcVar3 = (char *)((ulong)&local_110 | 1);
      if ((local_110 & 1) != 0) {
        pcVar3 = local_100;
      }
      local_c0 = opendir(pcVar3);
      local_b0 = &PTR_FUN_00c69f48;
      local_a8 = PTR_closedir_00c9acc0;
      local_90 = &local_b0;
      if (local_c0 == (DIR *)0x0) {
LAB_004fc474:
        lVar14 = 0x20;
        pppuVar13 = &local_b0;
LAB_004fc47c:
        (**(code **)((long)*pppuVar13 + lVar14))();
      }
      else {
        while (pdVar10 = readdir(local_c0), pDVar6 = local_c0, pdVar10 != (dirent *)0x0) {
          sVar11 = strlen(pdVar10->d_name);
          if (0xfffffffffffffff7 < sVar11) {
            if (*(long *)(lVar4 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
              FUN_0043b724(&local_128);
            }
            goto LAB_004fc698;
          }
          if (sVar11 < 0x17) {
            local_128 = CONCAT71(local_128._1_7_,(char)((int)sVar11 << 1));
            psVar12 = psVar21;
            if (sVar11 != 0) goto LAB_004fc170;
          }
          else {
            uVar15 = (sVar11 & 0xfffffffffffffff8) + 8;
            if ((sVar11 | 7) != 0x17) {
              uVar15 = sVar11 | 7;
            }
            psVar12 = (short *)_Znwm(uVar15 + 1);
            local_128 = uVar15 + 1 | 1;
            local_120 = sVar11;
            local_118 = psVar12;
LAB_004fc170:
            memmove(psVar12,pdVar10->d_name,sVar11);
          }
          uVar17 = local_110;
          *(char *)((long)psVar12 + sVar11) = '\0';
          uVar15 = local_128 & 1;
          bVar20 = (byte)local_128 & 1;
          sVar11 = (ulong)((byte)local_128 >> 1);
          if ((local_128 & 1) != 0) {
            sVar11 = local_120;
          }
          if (sVar11 == 2) {
            psVar12 = psVar21;
            if ((local_128 & 1) != 0) {
              psVar12 = local_118;
            }
            if (*psVar12 != 0x2e2e) goto LAB_004fc1e0;
          }
          else {
            if (sVar11 == 1) {
              psVar12 = psVar21;
              if ((local_128 & 1) != 0) {
                psVar12 = local_118;
              }
              if ((char)*psVar12 == '.') goto LAB_004fc400;
            }
LAB_004fc1e0:
            __n = local_110 >> 1 & 0x7f;
            if ((local_110 & 1) != 0) {
              __n = sStack_108;
            }
            uVar1 = __n + 1;
            if (0xfffffffffffffff7 < uVar1) {
              if (*(long *)(lVar4 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
                FUN_0043b724(&local_1c0);
              }
              goto LAB_004fc698;
            }
            if (uVar1 < 0x17) {
              local_1c0.st_ino = 0;
              local_1c0.st_nlink = 0;
              local_1c0.st_dev = (__dev_t)(byte)((int)uVar1 << 1);
              __dest = (void *)((ulong)&local_1c0 | 1);
              if (__n != 0) goto LAB_004fc258;
            }
            else {
              uVar2 = (uVar1 & 0xfffffffffffffff8) + 8;
              if ((uVar1 | 7) != 0x17) {
                uVar2 = uVar1 | 7;
              }
              __dest = (void *)_Znwm(uVar2 + 1);
              local_1c0.st_dev = uVar2 + 1 | 1;
              local_1c0.st_ino = uVar1;
              local_1c0.st_nlink = (__nlink_t)__dest;
LAB_004fc258:
              pcVar3 = (char *)((ulong)&local_110 | 1);
              if ((uVar17 & 1) != 0) {
                pcVar3 = local_100;
              }
              memmove(__dest,pcVar3,__n);
            }
            *(undefined2 *)((long)__dest + __n) = 0x2f;
            psVar12 = psVar21;
            if (uVar15 != 0) {
              psVar12 = local_118;
            }
            puVar18 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                         (&local_1c0,psVar12,sVar11);
            local_130 = (char *)puVar18[2];
            local_1c0.__unused[2] = puVar18[1];
            local_1c0.__unused[1] = *puVar18;
            puVar18[1] = 0;
            puVar18[2] = 0;
            *puVar18 = 0;
            if ((local_1c0.st_dev & 1) != 0) {
              _ZdlPv((void *)local_1c0.st_nlink);
            }
            pcVar3 = (char *)((ulong)(local_1c0.__unused + 1) | 1);
            if ((local_1c0.__unused[1] & 1U) != 0) {
              pcVar3 = local_130;
            }
            iVar8 = stat(pcVar3,&local_1c0);
            puVar18 = local_1d0;
            if (iVar8 != -1) {
              if (((uint)local_1c0.st_nlink & 0xf000) == 0x8000) {
                if (local_1d0 < puStack_1c8) {
                  if ((local_1c0.__unused[1] & 1U) == 0) {
                    local_1d0[2] = (ulong)local_130;
                    local_1d0[1] = local_1c0.__unused[2];
                    *local_1d0 = local_1c0.__unused[1];
                    local_1d0 = local_1d0 + 3;
                  }
                  else {
                    FUN_0043bae0(local_1d0,local_130,local_1c0.__unused[2]);
                    local_1d0 = puVar18 + 3;
                  }
                }
                else {
                  local_1d0 = (ulong *)FUN_00540d3c(&local_1d8,local_1c0.__unused + 1);
                }
              }
              else if (((uint)local_1c0.st_nlink & 0xf000) == 0x4000) {
                lVar14 = 0;
                if ((long)local_e0 - (long)puStack_e8 != 0) {
                  lVar14 = ((long)local_e0 - (long)puStack_e8 >> 3) * 0xaa + -1;
                }
                if (lVar14 == local_c8 + local_d0) {
                  FUN_0053a074(&local_f0);
                }
                if (local_e0 == puStack_e8) {
                  puVar18 = (ulong *)0x0;
                  if ((local_1c0.__unused[1] & 1U) != 0) goto LAB_004fc3d4;
LAB_004fc370:
                  puVar18[2] = (ulong)local_130;
                  puVar18[1] = local_1c0.__unused[2];
                  *puVar18 = local_1c0.__unused[1];
                }
                else {
                  puVar18 = (ulong *)(puStack_e8[(local_c8 + local_d0) / 0xaa] +
                                     ((local_c8 + local_d0) % 0xaa) * 0x18);
                  if ((local_1c0.__unused[1] & 1U) == 0) goto LAB_004fc370;
LAB_004fc3d4:
                  FUN_0043bae0(puVar18,local_130,local_1c0.__unused[2]);
                }
                local_c8 = local_c8 + 1;
              }
            }
            if ((local_1c0.__unused[1] & 1U) != 0) {
              _ZdlPv(local_130);
            }
            bVar20 = (byte)local_128 & 1;
          }
LAB_004fc400:
          if (bVar20 != 0) {
            _ZdlPv(local_118);
          }
        }
        local_c0 = (DIR *)0x0;
        if (pDVar6 != (DIR *)0x0) {
          local_1c0.st_dev = (__dev_t)pDVar6;
          if (local_90 == (undefined ***)0x0) {
            if (*(long *)(lVar4 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
              FUN_00459d34();
            }
            goto LAB_004fc698;
          }
          (*(code *)(*local_90)[6])(local_90,&local_1c0);
        }
        if (local_90 == &local_b0) goto LAB_004fc474;
        if (local_90 != (undefined ***)0x0) {
          lVar14 = 0x28;
          pppuVar13 = local_90;
          goto LAB_004fc47c;
        }
      }
      if ((local_110 & 1) != 0) {
        _ZdlPv(local_100);
      }
    } while (local_c8 != 0);
    pbVar16 = (byte *)*param_1;
    FUN_00539edc(&local_f0);
    if (pbVar16 != (byte *)0x0) {
      pbVar19 = (byte *)param_1[1];
      while (pbVar5 = pbVar19, pbVar5 != pbVar16) {
        pbVar19 = pbVar5 + -0x18;
        if ((*pbVar19 & 1) != 0) {
          _ZdlPv(*(void **)(pbVar5 + -8));
        }
      }
      param_1[1] = (ulong)pbVar16;
      _ZdlPv(pbVar16);
    }
  }
  param_1[2] = (ulong)puStack_1c8;
  param_1[1] = (ulong)local_1d0;
  *param_1 = (ulong)local_1d8;
  lVar14 = 0;
  if (local_1d0 != local_1d8) {
    lVar14 = LZCOUNT(((long)local_1d0 - (long)local_1d8 >> 3) * -0x5555555555555555) * -2 + 0x7e;
  }
  FUN_00545bfc(local_1d8,local_1d0,&local_1c0,lVar14,1);
  if (*(long *)(lVar4 + 0x28) == local_78) {
    return;
  }
LAB_004fc698:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
