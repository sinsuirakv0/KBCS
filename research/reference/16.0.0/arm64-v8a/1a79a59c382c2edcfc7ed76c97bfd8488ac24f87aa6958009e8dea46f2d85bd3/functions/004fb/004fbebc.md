# 004fbebc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004d9024`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0010.md#compare-8fb81ccb59f5dd72d0853d363ce719e8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004fbefc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0010.md#compare-449dce8d90438f72ea9e96ec4ac1493a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "ee99915e1c087a3494ff642a4067f8c293fef6fa4dcf6b2150c3a76c124b651b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004fbebc",
        "004fc5bb"
      ],
      [
        "004fc698",
        "004fc69b"
      ]
    ],
    "bytes_sha256": "07696e9cc42610eb59990b8b3bb18ae2ffebeabb2c2620c1aa8262881c2fc21a",
    "instruction_count": 449,
    "instruction_bytes": 1796,
    "body_bytes": 1796,
    "indirect": 2,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004fbebc"></a> `004fbebc` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-004fbec0"></a> `004fbec0` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fbec4"></a> `004fbec4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fbec8"></a> `004fbec8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fbecc"></a> `004fbecc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fbed0"></a> `004fbed0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fbed4"></a> `004fbed4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004fbed8"></a> `004fbed8` | `ff 83 06 d1` | sub sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-004fbedc"></a> `004fbedc` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-004fbee0"></a> `004fbee0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004fbee4"></a> `004fbee4` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004fbee8"></a> `004fbee8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fbeec"></a> `004fbeec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004fbef0"></a> `004fbef0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fbef4"></a> `004fbef4` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fbef8"></a> `004fbef8` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fbefc"></a> `004fbefc` | `3f 7f 00 a9` | stp xzr,xzr,[x25] | `FALL_THROUGH`
<a id="insn-004fbf00"></a> `004fbf00` | `3f 0b 00 f9` | str xzr,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-004fbf04"></a> `004fbf04` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fbf08"></a> `004fbf08` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004fbf0c"></a> `004fbf0c` | `00 01 03 ad` | stp q0,q0,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-004fbf10"></a> `004fbf10` | `00 15 80 3d` | str q0,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-004fbf14"></a> `004fbf14` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fbf18"></a> `004fbf18` | `57 f8 00 94` | bl 0x0053a074 | `UNCONDITIONAL_CALL`
<a id="insn-004fbf1c"></a> `004fbf1c` | `a8 a7 77 a9` | ldp x8,x9,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fbf20"></a> `004fbf20` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-004fbf24"></a> `004fbf24` | `80 02 00 54` | b.eq 0x004fbf74 | `CONDITIONAL_JUMP`
<a id="insn-004fbf28"></a> `004fbf28` | `a9 2b 79 a9` | ldp x9,x10,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fbf2c"></a> `004fbf2c` | `4b 15 80 52` | mov w11,#0xaa | `FALL_THROUGH`
<a id="insn-004fbf30"></a> `004fbf30` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-004fbf34"></a> `004fbf34` | `ea c7 02 b2` | orr x10,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fbf38"></a> `004fbf38` | `2a 18 98 f2` | movk x10,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fbf3c"></a> `004fbf3c` | `2a 7d ca 9b` | umulh x10,x9,x10 | `FALL_THROUGH`
<a id="insn-004fbf40"></a> `004fbf40` | `4a fd 47 d3` | lsr x10,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004fbf44"></a> `004fbf44` | `49 a5 0b 9b` | msub x9,x10,x11,x9 | `FALL_THROUGH`
<a id="insn-004fbf48"></a> `004fbf48` | `0b 03 80 52` | mov w11,#0x18 | `FALL_THROUGH`
<a id="insn-004fbf4c"></a> `004fbf4c` | `08 79 6a f8` | ldr x8,[x8, x10, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fbf50"></a> `004fbf50` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004fbf54"></a> `004fbf54` | `20 21 0b 9b` | madd x0,x9,x11,x8 | `FALL_THROUGH`
<a id="insn-004fbf58"></a> `004fbf58` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-004fbf5c"></a> `004fbf5c` | `28 01 00 37` | tbnz w8,#0x0,0x004fbf80 | `CONDITIONAL_JUMP`
<a id="insn-004fbf60"></a> `004fbf60` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004fbf64"></a> `004fbf64` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-004fbf68"></a> `004fbf68` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fbf6c"></a> `004fbf6c` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-004fbf70"></a> `004fbf70` | `06 00 00 14` | b 0x004fbf88 | `UNCONDITIONAL_JUMP`
<a id="insn-004fbf74"></a> `004fbf74` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-004fbf78"></a> `004fbf78` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-004fbf7c"></a> `004fbf7c` | `28 ff 07 36` | tbz w8,#0x0,0x004fbf60 | `CONDITIONAL_JUMP`
<a id="insn-004fbf80"></a> `004fbf80` | `82 86 40 a9` | ldp x2,x1,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004fbf84"></a> `004fbf84` | `d7 fe fc 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbf88"></a> `004fbf88` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fbf8c"></a> `004fbf8c` | `08 05 00 b1` | adds x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fbf90"></a> `004fbf90` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fbf94"></a> `004fbf94` | `83 00 00 54` | b.cc 0x004fbfa4 | `CONDITIONAL_JUMP`
<a id="insn-004fbf98"></a> `004fbf98` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fbf9c"></a> `004fbf9c` | `d0 f7 00 94` | bl 0x00539edc | `UNCONDITIONAL_CALL`
<a id="insn-004fbfa0"></a> `004fbfa0` | `53 01 00 14` | b 0x004fc4ec | `UNCONDITIONAL_JUMP`
<a id="insn-004fbfa4"></a> `004fbfa4` | `a8 c3 02 d1` | sub x8,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-004fbfa8"></a> `004fbfa8` | `a9 83 01 d1` | sub x9,x29,#0x60 | `FALL_THROUGH`
<a id="insn-004fbfac"></a> `004fbfac` | `aa 23 03 d1` | sub x10,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-004fbfb0"></a> `004fbfb0` | `08 01 40 b2` | orr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fbfb4"></a> `004fbfb4` | `eb 03 01 91` | add x11,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fbfb8"></a> `004fbfb8` | `5c 01 40 b2` | orr x28,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004fbfbc"></a> `004fbfbc` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fbfc0"></a> `004fbfc0` | `28 41 00 91` | add x8,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004fbfc4"></a> `004fbfc4` | `69 01 40 b2` | orr x9,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004fbfc8"></a> `004fbfc8` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fbfcc"></a> `004fbfcc` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fbfd0"></a> `004fbfd0` | `13 01 40 b2` | orr x19,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fbfd4"></a> `004fbfd4` | `e9 0f 00 f9` | str x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fbfd8"></a> `004fbfd8` | `03 00 00 14` | b 0x004fbfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-004fbfdc"></a> `004fbfdc` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fbfe0"></a> `004fbfe0` | `e8 25 00 b4` | cbz x8,0x004fc49c | `CONDITIONAL_JUMP`
<a id="insn-004fbfe4"></a> `004fbfe4` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fbfe8"></a> `004fbfe8` | `e9 c7 02 b2` | orr x9,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fbfec"></a> `004fbfec` | `4b 15 80 52` | mov w11,#0xaa | `FALL_THROUGH`
<a id="insn-004fbff0"></a> `004fbff0` | `29 18 98 f2` | movk x9,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fbff4"></a> `004fbff4` | `aa 83 57 f8` | ldur x10,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fbff8"></a> `004fbff8` | `0d 03 80 52` | mov w13,#0x18 | `FALL_THROUGH`
<a id="insn-004fbffc"></a> `004fbffc` | `09 7d c9 9b` | umulh x9,x8,x9 | `FALL_THROUGH`
<a id="insn-004fc000"></a> `004fc000` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-004fc004"></a> `004fc004` | `2b a1 0b 9b` | msub x11,x9,x11,x8 | `FALL_THROUGH`
<a id="insn-004fc008"></a> `004fc008` | `4c 79 69 f8` | ldr x12,[x10, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fc00c"></a> `004fc00c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004fc010"></a> `004fc010` | `6c 31 0d 9b` | madd x12,x11,x13,x12 | `FALL_THROUGH`
<a id="insn-004fc014"></a> `004fc014` | `8d 01 40 39` | ldrb w13,[x12] | `FALL_THROUGH`
<a id="insn-004fc018"></a> `004fc018` | `ed 00 00 37` | tbnz w13,#0x0,0x004fc034 | `CONDITIONAL_JUMP`
<a id="insn-004fc01c"></a> `004fc01c` | `8d 09 40 f9` | ldr x13,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-004fc020"></a> `004fc020` | `80 01 c0 3d` | ldr q0,[x12] | `FALL_THROUGH`
<a id="insn-004fc024"></a> `004fc024` | `ec 03 03 91` | add x12,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc028"></a> `004fc028` | `ad 03 16 f8` | stur x13,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc02c"></a> `004fc02c` | `80 0d 80 3d` | str q0,[x12, #0x30] | `FALL_THROUGH`
<a id="insn-004fc030"></a> `004fc030` | `0c 00 00 14` | b 0x004fc060 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc034"></a> `004fc034` | `82 85 40 a9` | ldp x2,x1,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-004fc038"></a> `004fc038` | `a0 c3 02 d1` | sub x0,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-004fc03c"></a> `004fc03c` | `a9 fe fc 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc040"></a> `004fc040` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc044"></a> `004fc044` | `e9 c7 02 b2` | orr x9,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fc048"></a> `004fc048` | `4a 15 80 52` | mov w10,#0xaa | `FALL_THROUGH`
<a id="insn-004fc04c"></a> `004fc04c` | `29 18 98 f2` | movk x9,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fc050"></a> `004fc050` | `09 7d c9 9b` | umulh x9,x8,x9 | `FALL_THROUGH`
<a id="insn-004fc054"></a> `004fc054` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-004fc058"></a> `004fc058` | `2b a1 0a 9b` | msub x11,x9,x10,x8 | `FALL_THROUGH`
<a id="insn-004fc05c"></a> `004fc05c` | `aa 83 57 f8` | ldur x10,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc060"></a> `004fc060` | `49 79 69 f8` | ldr x9,[x10, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fc064"></a> `004fc064` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-004fc068"></a> `004fc068` | `69 25 0a 9b` | madd x9,x11,x10,x9 | `FALL_THROUGH`
<a id="insn-004fc06c"></a> `004fc06c` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-004fc070"></a> `004fc070` | `8a 00 00 36` | tbz w10,#0x0,0x004fc080 | `CONDITIONAL_JUMP`
<a id="insn-004fc074"></a> `004fc074` | `20 09 40 f9` | ldr x0,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-004fc078"></a> `004fc078` | `8e 6e 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc07c"></a> `004fc07c` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc080"></a> `004fc080` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fc084"></a> `004fc084` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc088"></a> `004fc088` | `1f 51 05 f1` | cmp x8,#0x154 | `FALL_THROUGH`
<a id="insn-004fc08c"></a> `004fc08c` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004fc090"></a> `004fc090` | `a8 27 39 a9` | stp x8,x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc094"></a> `004fc094` | `43 01 00 54` | b.cc 0x004fc0bc | `CONDITIONAL_JUMP`
<a id="insn-004fc098"></a> `004fc098` | `a8 83 57 f8` | ldur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc09c"></a> `004fc09c` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-004fc0a0"></a> `004fc0a0` | `84 6e 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc0a4"></a> `004fc0a4` | `a8 83 57 f8` | ldur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc0a8"></a> `004fc0a8` | `a9 03 59 f8` | ldur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc0ac"></a> `004fc0ac` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004fc0b0"></a> `004fc0b0` | `29 a9 02 d1` | sub x9,x9,#0xaa | `FALL_THROUGH`
<a id="insn-004fc0b4"></a> `004fc0b4` | `a8 83 17 f8` | stur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc0b8"></a> `004fc0b8` | `a9 03 19 f8` | stur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc0bc"></a> `004fc0bc` | `a8 03 55 38` | ldurb w8,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-004fc0c0"></a> `004fc0c0` | `a9 03 56 f8` | ldur x9,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc0c4"></a> `004fc0c4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc0c8"></a> `004fc0c8` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fc0cc"></a> `004fc0cc` | `00 01 89 9a` | csel x0,x8,x9,eq | `FALL_THROUGH`
<a id="insn-004fc0d0"></a> `004fc0d0` | `dc 74 1d 94` | bl 0x00c59440 | `UNCONDITIONAL_CALL`
<a id="insn-004fc0d4"></a> `004fc0d4` | `68 3b 00 b0` | adrp x8,0xc69000 | `FALL_THROUGH`
<a id="insn-004fc0d8"></a> `004fc0d8` | `08 21 3d 91` | add x8,x8,#0xf48 | `FALL_THROUGH`
<a id="insn-004fc0dc"></a> `004fc0dc` | `a0 03 1a f8` | stur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc0e0"></a> `004fc0e0` | `a8 03 1b f8` | stur x8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004fc0e4"></a> `004fc0e4` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fc0e8"></a> `004fc0e8` | `e9 3c 00 d0` | adrp x9,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fc0ec"></a> `004fc0ec` | `a8 03 1d f8` | stur x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fc0f0"></a> `004fc0f0` | `29 61 46 f9` | ldr x9,[x9, #0xcc0] | `FALL_THROUGH`
<a id="insn-004fc0f4"></a> `004fc0f4` | `a9 83 1b f8` | stur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-004fc0f8"></a> `004fc0f8` | `60 00 00 b5` | cbnz x0,0x004fc104 | `CONDITIONAL_JUMP`
<a id="insn-004fc0fc"></a> `004fc0fc` | `de 00 00 14` | b 0x004fc474 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc100"></a> `004fc100` | `a0 03 5a f8` | ldur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc104"></a> `004fc104` | `d3 74 1d 94` | bl 0x00c59450 | `UNCONDITIONAL_CALL`
<a id="insn-004fc108"></a> `004fc108` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004fc10c"></a> `004fc10c` | `20 19 00 b4` | cbz x0,0x004fc430 | `CONDITIONAL_JUMP`
<a id="insn-004fc110"></a> `004fc110` | `80 4e 00 91` | add x0,x20,#0x13 | `FALL_THROUGH`
<a id="insn-004fc114"></a> `004fc114` | `b3 6e 1d 94` | bl 0x00c57be0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc118"></a> `004fc118` | `1f 20 00 b1` | cmn x0,#0x8 | `FALL_THROUGH`
<a id="insn-004fc11c"></a> `004fc11c` | `62 22 00 54` | b.cs 0x004fc568 | `CONDITIONAL_JUMP`
<a id="insn-004fc120"></a> `004fc120` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004fc124"></a> `004fc124` | `1f 5c 00 f1` | cmp x0,#0x17 | `FALL_THROUGH`
<a id="insn-004fc128"></a> `004fc128` | `c2 00 00 54` | b.cs 0x004fc140 | `CONDITIONAL_JUMP`
<a id="insn-004fc12c"></a> `004fc12c` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-004fc130"></a> `004fc130` | `f6 03 1c aa` | mov x22,x28 | `FALL_THROUGH`
<a id="insn-004fc134"></a> `004fc134` | `a8 83 13 38` | sturb w8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc138"></a> `004fc138` | `d5 01 00 b5` | cbnz x21,0x004fc170 | `CONDITIONAL_JUMP`
<a id="insn-004fc13c"></a> `004fc13c` | `11 00 00 14` | b 0x004fc180 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc140"></a> `004fc140` | `a8 f2 7d 92` | and x8,x21,#-0x8 | `FALL_THROUGH`
<a id="insn-004fc144"></a> `004fc144` | `a9 0a 40 b2` | orr x9,x21,#0x7 | `FALL_THROUGH`
<a id="insn-004fc148"></a> `004fc148` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004fc14c"></a> `004fc14c` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-004fc150"></a> `004fc150` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-004fc154"></a> `004fc154` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc158"></a> `004fc158` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004fc15c"></a> `004fc15c` | `4d 6e 1d 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-004fc160"></a> `004fc160` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-004fc164"></a> `004fc164` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-004fc168"></a> `004fc168` | `b5 03 34 a9` | stp x21,x0,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-004fc16c"></a> `004fc16c` | `a8 83 13 f8` | stur x8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc170"></a> `004fc170` | `81 4e 00 91` | add x1,x20,#0x13 | `FALL_THROUGH`
<a id="insn-004fc174"></a> `004fc174` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004fc178"></a> `004fc178` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004fc17c"></a> `004fc17c` | `71 6e 1d 94` | bl 0x00c57b40 | `UNCONDITIONAL_CALL`
<a id="insn-004fc180"></a> `004fc180` | `df 6a 35 38` | strb wzr,[x22, x21, LSL ] | `FALL_THROUGH`
<a id="insn-004fc184"></a> `004fc184` | `a8 83 53 38` | ldurb w8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc188"></a> `004fc188` | `a9 03 54 f8` | ldur x9,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-004fc18c"></a> `004fc18c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc190"></a> `004fc190` | `18 01 00 72` | ands w24,w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc194"></a> `004fc194` | `54 01 89 9a` | csel x20,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004fc198"></a> `004fc198` | `9f 0a 00 f1` | cmp x20,#0x2 | `FALL_THROUGH`
<a id="insn-004fc19c"></a> `004fc19c` | `40 01 00 54` | b.eq 0x004fc1c4 | `CONDITIONAL_JUMP`
<a id="insn-004fc1a0"></a> `004fc1a0` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1a4"></a> `004fc1a4` | `e1 01 00 54` | b.ne 0x004fc1e0 | `CONDITIONAL_JUMP`
<a id="insn-004fc1a8"></a> `004fc1a8` | `a8 83 54 f8` | ldur x8,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc1ac"></a> `004fc1ac` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-004fc1b0"></a> `004fc1b0` | `88 03 88 9a` | csel x8,x28,x8,eq | `FALL_THROUGH`
<a id="insn-004fc1b4"></a> `004fc1b4` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-004fc1b8"></a> `004fc1b8` | `1f b9 00 71` | cmp w8,#0x2e | `FALL_THROUGH`
<a id="insn-004fc1bc"></a> `004fc1bc` | `21 01 00 54` | b.ne 0x004fc1e0 | `CONDITIONAL_JUMP`
<a id="insn-004fc1c0"></a> `004fc1c0` | `90 00 00 14` | b 0x004fc400 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc1c4"></a> `004fc1c4` | `a8 83 54 f8` | ldur x8,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc1c8"></a> `004fc1c8` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-004fc1cc"></a> `004fc1cc` | `c9 c5 85 52` | mov w9,#0x2e2e | `FALL_THROUGH`
<a id="insn-004fc1d0"></a> `004fc1d0` | `88 03 88 9a` | csel x8,x28,x8,eq | `FALL_THROUGH`
<a id="insn-004fc1d4"></a> `004fc1d4` | `08 01 40 79` | ldrh w8,[x8] | `FALL_THROUGH`
<a id="insn-004fc1d8"></a> `004fc1d8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-004fc1dc"></a> `004fc1dc` | `20 11 00 54` | b.eq 0x004fc400 | `CONDITIONAL_JUMP`
<a id="insn-004fc1e0"></a> `004fc1e0` | `bb 03 55 38` | ldurb w27,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-004fc1e4"></a> `004fc1e4` | `a8 83 55 f8` | ldur x8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-004fc1e8"></a> `004fc1e8` | `fa 03 19 aa` | mov x26,x25 | `FALL_THROUGH`
<a id="insn-004fc1ec"></a> `004fc1ec` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1f0"></a> `004fc1f0` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1f4"></a> `004fc1f4` | `35 01 88 9a` | csel x21,x9,x8,eq | `FALL_THROUGH`
<a id="insn-004fc1f8"></a> `004fc1f8` | `b9 06 00 91` | add x25,x21,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1fc"></a> `004fc1fc` | `3f 23 00 b1` | cmn x25,#0x8 | `FALL_THROUGH`
<a id="insn-004fc200"></a> `004fc200` | `22 1c 00 54` | b.cs 0x004fc584 | `CONDITIONAL_JUMP`
<a id="insn-004fc204"></a> `004fc204` | `3f 5f 00 f1` | cmp x25,#0x17 | `FALL_THROUGH`
<a id="insn-004fc208"></a> `004fc208` | `02 01 00 54` | b.cs 0x004fc228 | `CONDITIONAL_JUMP`
<a id="insn-004fc20c"></a> `004fc20c` | `28 7b 1f 53` | lsl w8,w25,#0x1 | `FALL_THROUGH`
<a id="insn-004fc210"></a> `004fc210` | `f6 0f 40 f9` | ldr x22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fc214"></a> `004fc214` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc218"></a> `004fc218` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc21c"></a> `004fc21c` | `e8 03 01 39` | strb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc220"></a> `004fc220` | `d5 01 00 b5` | cbnz x21,0x004fc258 | `CONDITIONAL_JUMP`
<a id="insn-004fc224"></a> `004fc224` | `14 00 00 14` | b 0x004fc274 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc228"></a> `004fc228` | `28 f3 7d 92` | and x8,x25,#-0x8 | `FALL_THROUGH`
<a id="insn-004fc22c"></a> `004fc22c` | `29 0b 40 b2` | orr x9,x25,#0x7 | `FALL_THROUGH`
<a id="insn-004fc230"></a> `004fc230` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004fc234"></a> `004fc234` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-004fc238"></a> `004fc238` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-004fc23c"></a> `004fc23c` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc240"></a> `004fc240` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004fc244"></a> `004fc244` | `13 6e 1d 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-004fc248"></a> `004fc248` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-004fc24c"></a> `004fc24c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-004fc250"></a> `004fc250` | `f9 83 04 a9` | stp x25,x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004fc254"></a> `004fc254` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc258"></a> `004fc258` | `a8 03 56 f8` | ldur x8,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc25c"></a> `004fc25c` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fc260"></a> `004fc260` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-004fc264"></a> `004fc264` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004fc268"></a> `004fc268` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004fc26c"></a> `004fc26c` | `21 01 88 9a` | csel x1,x9,x8,eq | `FALL_THROUGH`
<a id="insn-004fc270"></a> `004fc270` | `34 6e 1d 94` | bl 0x00c57b40 | `UNCONDITIONAL_CALL`
<a id="insn-004fc274"></a> `004fc274` | `a8 83 54 f8` | ldur x8,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc278"></a> `004fc278` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-004fc27c"></a> `004fc27c` | `e9 05 80 52` | mov w9,#0x2f | `FALL_THROUGH`
<a id="insn-004fc280"></a> `004fc280` | `c9 6a 35 78` | strh w9,[x22, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004fc284"></a> `004fc284` | `81 03 88 9a` | csel x1,x28,x8,eq | `FALL_THROUGH`
<a id="insn-004fc288"></a> `004fc288` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc28c"></a> `004fc28c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-004fc290"></a> `004fc290` | `3c 6e 1d 94` | bl 0x00c57b80 | `UNCONDITIONAL_CALL`
<a id="insn-004fc294"></a> `004fc294` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fc298"></a> `004fc298` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004fc29c"></a> `004fc29c` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-004fc2a0"></a> `004fc2a0` | `e8 6b 00 f9` | str x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc2a4"></a> `004fc2a4` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc2a8"></a> `004fc2a8` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-004fc2ac"></a> `004fc2ac` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004fc2b0"></a> `004fc2b0` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004fc2b4"></a> `004fc2b4` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc2b8"></a> `004fc2b8` | `68 00 00 36` | tbz w8,#0x0,0x004fc2c4 | `CONDITIONAL_JUMP`
<a id="insn-004fc2bc"></a> `004fc2bc` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc2c0"></a> `004fc2c0` | `fc 6d 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc2c4"></a> `004fc2c4` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc2c8"></a> `004fc2c8` | `e9 6b 40 f9` | ldr x9,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc2cc"></a> `004fc2cc` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc2d0"></a> `004fc2d0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc2d4"></a> `004fc2d4` | `60 02 89 9a` | csel x0,x19,x9,eq | `FALL_THROUGH`
<a id="insn-004fc2d8"></a> `004fc2d8` | `62 74 1d 94` | bl 0x00c59460 | `UNCONDITIONAL_CALL`
<a id="insn-004fc2dc"></a> `004fc2dc` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-004fc2e0"></a> `004fc2e0` | `40 08 00 54` | b.eq 0x004fc3e8 | `CONDITIONAL_JUMP`
<a id="insn-004fc2e4"></a> `004fc2e4` | `e8 53 40 b9` | ldr w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc2e8"></a> `004fc2e8` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-004fc2ec"></a> `004fc2ec` | `1f 21 40 71` | cmp w8,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-004fc2f0"></a> `004fc2f0` | `c0 04 00 54` | b.eq 0x004fc388 | `CONDITIONAL_JUMP`
<a id="insn-004fc2f4"></a> `004fc2f4` | `1f 11 40 71` | cmp w8,#0x4, LSL #12 | `FALL_THROUGH`
<a id="insn-004fc2f8"></a> `004fc2f8` | `81 07 00 54` | b.ne 0x004fc3e8 | `CONDITIONAL_JUMP`
<a id="insn-004fc2fc"></a> `004fc2fc` | `a8 a7 77 a9` | ldp x8,x9,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc300"></a> `004fc300` | `4c 15 80 52` | mov w12,#0xaa | `FALL_THROUGH`
<a id="insn-004fc304"></a> `004fc304` | `0b 00 80 92` | mov x11,#-0x1 | `FALL_THROUGH`
<a id="insn-004fc308"></a> `004fc308` | `2a 01 08 eb` | subs x10,x9,x8 | `FALL_THROUGH`
<a id="insn-004fc30c"></a> `004fc30c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-004fc310"></a> `004fc310` | `4a 2d 0c 9b` | madd x10,x10,x12,x11 | `FALL_THROUGH`
<a id="insn-004fc314"></a> `004fc314` | `ab 33 79 a9` | ldp x11,x12,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc318"></a> `004fc318` | `8b 01 0b 8b` | add x11,x12,x11 | `FALL_THROUGH`
<a id="insn-004fc31c"></a> `004fc31c` | `ea 03 8a 9a` | csel x10,xzr,x10,eq | `FALL_THROUGH`
<a id="insn-004fc320"></a> `004fc320` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-004fc324"></a> `004fc324` | `81 00 00 54` | b.ne 0x004fc334 | `CONDITIONAL_JUMP`
<a id="insn-004fc328"></a> `004fc328` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fc32c"></a> `004fc32c` | `52 f7 00 94` | bl 0x0053a074 | `UNCONDITIONAL_CALL`
<a id="insn-004fc330"></a> `004fc330` | `a8 a7 77 a9` | ldp x8,x9,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc334"></a> `004fc334` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-004fc338"></a> `004fc338` | `80 04 00 54` | b.eq 0x004fc3c8 | `CONDITIONAL_JUMP`
<a id="insn-004fc33c"></a> `004fc33c` | `a9 2b 79 a9` | ldp x9,x10,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc340"></a> `004fc340` | `4b 15 80 52` | mov w11,#0xaa | `FALL_THROUGH`
<a id="insn-004fc344"></a> `004fc344` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-004fc348"></a> `004fc348` | `ea c7 02 b2` | orr x10,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fc34c"></a> `004fc34c` | `2a 18 98 f2` | movk x10,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fc350"></a> `004fc350` | `2a 7d ca 9b` | umulh x10,x9,x10 | `FALL_THROUGH`
<a id="insn-004fc354"></a> `004fc354` | `4a fd 47 d3` | lsr x10,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004fc358"></a> `004fc358` | `49 a5 0b 9b` | msub x9,x10,x11,x9 | `FALL_THROUGH`
<a id="insn-004fc35c"></a> `004fc35c` | `08 79 6a f8` | ldr x8,[x8, x10, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fc360"></a> `004fc360` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-004fc364"></a> `004fc364` | `20 21 0a 9b` | madd x0,x9,x10,x8 | `FALL_THROUGH`
<a id="insn-004fc368"></a> `004fc368` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc36c"></a> `004fc36c` | `48 03 00 37` | tbnz w8,#0x0,0x004fc3d4 | `CONDITIONAL_JUMP`
<a id="insn-004fc370"></a> `004fc370` | `e9 03 03 91` | add x9,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc374"></a> `004fc374` | `e8 6b 40 f9` | ldr x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc378"></a> `004fc378` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-004fc37c"></a> `004fc37c` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fc380"></a> `004fc380` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-004fc384"></a> `004fc384` | `16 00 00 14` | b 0x004fc3dc | `UNCONDITIONAL_JUMP`
<a id="insn-004fc388"></a> `004fc388` | `f5 23 43 a9` | ldp x21,x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc38c"></a> `004fc38c` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-004fc390"></a> `004fc390` | `42 01 00 54` | b.cs 0x004fc3b8 | `CONDITIONAL_JUMP`
<a id="insn-004fc394"></a> `004fc394` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc398"></a> `004fc398` | `c8 03 00 37` | tbnz w8,#0x0,0x004fc410 | `CONDITIONAL_JUMP`
<a id="insn-004fc39c"></a> `004fc39c` | `e9 03 03 91` | add x9,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc3a0"></a> `004fc3a0` | `e8 6b 40 f9` | ldr x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc3a4"></a> `004fc3a4` | `a0 62 00 91` | add x0,x21,#0x18 | `FALL_THROUGH`
<a id="insn-004fc3a8"></a> `004fc3a8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-004fc3ac"></a> `004fc3ac` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-004fc3b0"></a> `004fc3b0` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-004fc3b4"></a> `004fc3b4` | `1b 00 00 14` | b 0x004fc420 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc3b8"></a> `004fc3b8` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004fc3bc"></a> `004fc3bc` | `e1 03 03 91` | add x1,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc3c0"></a> `004fc3c0` | `5f 12 01 94` | bl 0x00540d3c | `UNCONDITIONAL_CALL`
<a id="insn-004fc3c4"></a> `004fc3c4` | `17 00 00 14` | b 0x004fc420 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc3c8"></a> `004fc3c8` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-004fc3cc"></a> `004fc3cc` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc3d0"></a> `004fc3d0` | `08 fd 07 36` | tbz w8,#0x0,0x004fc370 | `CONDITIONAL_JUMP`
<a id="insn-004fc3d4"></a> `004fc3d4` | `e2 87 4c a9` | ldp x2,x1,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-004fc3d8"></a> `004fc3d8` | `c2 fd fc 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc3dc"></a> `004fc3dc` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fc3e0"></a> `004fc3e0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc3e4"></a> `004fc3e4` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fc3e8"></a> `004fc3e8` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc3ec"></a> `004fc3ec` | `68 00 00 36` | tbz w8,#0x0,0x004fc3f8 | `CONDITIONAL_JUMP`
<a id="insn-004fc3f0"></a> `004fc3f0` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc3f4"></a> `004fc3f4` | `af 6d 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc3f8"></a> `004fc3f8` | `a8 83 53 38` | ldurb w8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc3fc"></a> `004fc3fc` | `18 01 00 12` | and w24,w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc400"></a> `004fc400` | `18 e8 ff 34` | cbz w24,0x004fc100 | `CONDITIONAL_JUMP`
<a id="insn-004fc404"></a> `004fc404` | `a0 83 54 f8` | ldur x0,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc408"></a> `004fc408` | `aa 6d 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc40c"></a> `004fc40c` | `3d ff ff 17` | b 0x004fc100 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc410"></a> `004fc410` | `e2 87 4c a9` | ldp x2,x1,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-004fc414"></a> `004fc414` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004fc418"></a> `004fc418` | `b2 fd fc 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc41c"></a> `004fc41c` | `a0 62 00 91` | add x0,x21,#0x18 | `FALL_THROUGH`
<a id="insn-004fc420"></a> `004fc420` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc424"></a> `004fc424` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc428"></a> `004fc428` | `48 fe 07 37` | tbnz w8,#0x0,0x004fc3f0 | `CONDITIONAL_JUMP`
<a id="insn-004fc42c"></a> `004fc42c` | `f3 ff ff 17` | b 0x004fc3f8 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc430"></a> `004fc430` | `a8 03 5a f8` | ldur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc434"></a> `004fc434` | `bf 03 1a f8` | stur xzr,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc438"></a> `004fc438` | `08 01 00 b4` | cbz x8,0x004fc458 | `CONDITIONAL_JUMP`
<a id="insn-004fc43c"></a> `004fc43c` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fc440"></a> `004fc440` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc444"></a> `004fc444` | `00 0b 00 b4` | cbz x0,0x004fc5a4 | `CONDITIONAL_JUMP`
<a id="insn-004fc448"></a> `004fc448` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004fc44c"></a> `004fc44c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-004fc450"></a> `004fc450` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc454"></a> `004fc454` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004fc458"></a> `004fc458` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fc45c"></a> `004fc45c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fc460"></a> `004fc460` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-004fc464"></a> `004fc464` | `80 00 00 54` | b.eq 0x004fc474 | `CONDITIONAL_JUMP`
<a id="insn-004fc468"></a> `004fc468` | `00 01 00 b4` | cbz x0,0x004fc488 | `CONDITIONAL_JUMP`
<a id="insn-004fc46c"></a> `004fc46c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-004fc470"></a> `004fc470` | `03 00 00 14` | b 0x004fc47c | `UNCONDITIONAL_JUMP`
<a id="insn-004fc474"></a> `004fc474` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-004fc478"></a> `004fc478` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-004fc47c"></a> `004fc47c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-004fc480"></a> `004fc480` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004fc484"></a> `004fc484` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004fc488"></a> `004fc488` | `a8 03 55 38` | ldurb w8,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-004fc48c"></a> `004fc48c` | `88 da 07 36` | tbz w8,#0x0,0x004fbfdc | `CONDITIONAL_JUMP`
<a id="insn-004fc490"></a> `004fc490` | `a0 03 56 f8` | ldur x0,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc494"></a> `004fc494` | `87 6d 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc498"></a> `004fc498` | `d1 fe ff 17` | b 0x004fbfdc | `UNCONDITIONAL_JUMP`
<a id="insn-004fc49c"></a> `004fc49c` | `34 03 40 f9` | ldr x20,[x25] | `FALL_THROUGH`
<a id="insn-004fc4a0"></a> `004fc4a0` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fc4a4"></a> `004fc4a4` | `8e f6 00 94` | bl 0x00539edc | `UNCONDITIONAL_CALL`
<a id="insn-004fc4a8"></a> `004fc4a8` | `34 02 00 b4` | cbz x20,0x004fc4ec | `CONDITIONAL_JUMP`
<a id="insn-004fc4ac"></a> `004fc4ac` | `28 07 40 f9` | ldr x8,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-004fc4b0"></a> `004fc4b0` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-004fc4b4"></a> `004fc4b4` | `60 01 00 54` | b.eq 0x004fc4e0 | `CONDITIONAL_JUMP`
<a id="insn-004fc4b8"></a> `004fc4b8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004fc4bc"></a> `004fc4bc` | `04 00 00 14` | b 0x004fc4cc | `UNCONDITIONAL_JUMP`
<a id="insn-004fc4c0"></a> `004fc4c0` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004fc4c4"></a> `004fc4c4` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004fc4c8"></a> `004fc4c8` | `c0 00 00 54` | b.eq 0x004fc4e0 | `CONDITIONAL_JUMP`
<a id="insn-004fc4cc"></a> `004fc4cc` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-004fc4d0"></a> `004fc4d0` | `89 ff 07 36` | tbz w9,#0x0,0x004fc4c0 | `CONDITIONAL_JUMP`
<a id="insn-004fc4d4"></a> `004fc4d4` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-004fc4d8"></a> `004fc4d8` | `76 6d 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc4dc"></a> `004fc4dc` | `f9 ff ff 17` | b 0x004fc4c0 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc4e0"></a> `004fc4e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004fc4e4"></a> `004fc4e4` | `34 07 00 f9` | str x20,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-004fc4e8"></a> `004fc4e8` | `72 6d 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc4ec"></a> `004fc4ec` | `e0 03 c3 3c` | ldur q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc4f0"></a> `004fc4f0` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fc4f4"></a> `004fc4f4` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-004fc4f8"></a> `004fc4f8` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-004fc4fc"></a> `004fc4fc` | `01 00 66 9e` | fmov x1,d0 | `FALL_THROUGH`
<a id="insn-004fc500"></a> `004fc500` | `20 83 80 3c` | stur q0,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-004fc504"></a> `004fc504` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-004fc508"></a> `004fc508` | `28 00 00 eb` | subs x8,x1,x0 | `FALL_THROUGH`
<a id="insn-004fc50c"></a> `004fc50c` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-004fc510"></a> `004fc510` | `3f 00 00 eb` | cmp x1,x0 | `FALL_THROUGH`
<a id="insn-004fc514"></a> `004fc514` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-004fc518"></a> `004fc518` | `c9 0f 80 52` | mov w9,#0x7e | `FALL_THROUGH`
<a id="insn-004fc51c"></a> `004fc51c` | `08 11 c0 da` | clz x8,x8 | `FALL_THROUGH`
<a id="insn-004fc520"></a> `004fc520` | `28 05 08 cb` | sub x8,x9,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-004fc524"></a> `004fc524` | `e3 03 88 9a` | csel x3,xzr,x8,eq | `FALL_THROUGH`
<a id="insn-004fc528"></a> `004fc528` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc52c"></a> `004fc52c` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-004fc530"></a> `004fc530` | `b3 25 01 94` | bl 0x00545bfc | `UNCONDITIONAL_CALL`
<a id="insn-004fc534"></a> `004fc534` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc538"></a> `004fc538` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc53c"></a> `004fc53c` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc540"></a> `004fc540` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc544"></a> `004fc544` | `a1 0a 00 54` | b.ne 0x004fc698 | `CONDITIONAL_JUMP`
<a id="insn-004fc548"></a> `004fc548` | `ff 83 06 91` | add sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-004fc54c"></a> `004fc54c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc550"></a> `004fc550` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc554"></a> `004fc554` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc558"></a> `004fc558` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fc55c"></a> `004fc55c` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fc560"></a> `004fc560` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-004fc564"></a> `004fc564` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fc568"></a> `004fc568` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc56c"></a> `004fc56c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc570"></a> `004fc570` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc574"></a> `004fc574` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc578"></a> `004fc578` | `01 09 00 54` | b.ne 0x004fc698 | `CONDITIONAL_JUMP`
<a id="insn-004fc57c"></a> `004fc57c` | `a0 23 03 d1` | sub x0,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-004fc580"></a> `004fc580` | `69 fc fc 97` | bl 0x0043b724 | `CALL_TERMINATOR`
<a id="insn-004fc584"></a> `004fc584` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc588"></a> `004fc588` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc58c"></a> `004fc58c` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc590"></a> `004fc590` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc594"></a> `004fc594` | `21 08 00 54` | b.ne 0x004fc698 | `CONDITIONAL_JUMP`
<a id="insn-004fc598"></a> `004fc598` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc59c"></a> `004fc59c` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-004fc5a0"></a> `004fc5a0` | `61 fc fc 97` | bl 0x0043b724 | `CALL_TERMINATOR`
<a id="insn-004fc5a4"></a> `004fc5a4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc5a8"></a> `004fc5a8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc5ac"></a> `004fc5ac` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc5b0"></a> `004fc5b0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc5b4"></a> `004fc5b4` | `21 07 00 54` | b.ne 0x004fc698 | `CONDITIONAL_JUMP`
<a id="insn-004fc5b8"></a> `004fc5b8` | `df 75 fd 97` | bl 0x00459d34 | `CALL_TERMINATOR`
<a id="insn-004fc698"></a> `004fc698` | `12 6d 1d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004fbebc`](#insn-004fbebc) 範囲 `[['004fbebc', '004fbf27']]`
  - `CONDITIONAL_JUMP` [`004fbf24`](#insn-004fbf24) → [`004fbf74`](#insn-004fbf74)
  - `FALL_THROUGH` [`004fbf24`](#insn-004fbf24) → [`004fbf28`](#insn-004fbf28)
- ブロック [`004fbf28`](#insn-004fbf28) 範囲 `[['004fbf28', '004fbf5f']]`
  - `CONDITIONAL_JUMP` [`004fbf5c`](#insn-004fbf5c) → [`004fbf80`](#insn-004fbf80)
  - `FALL_THROUGH` [`004fbf5c`](#insn-004fbf5c) → [`004fbf60`](#insn-004fbf60)
- ブロック [`004fbf60`](#insn-004fbf60) 範囲 `[['004fbf60', '004fbf73']]`
  - `UNCONDITIONAL_JUMP` [`004fbf70`](#insn-004fbf70) → [`004fbf88`](#insn-004fbf88)
- ブロック [`004fbf74`](#insn-004fbf74) 範囲 `[['004fbf74', '004fbf7f']]`
  - `CONDITIONAL_JUMP` [`004fbf7c`](#insn-004fbf7c) → [`004fbf60`](#insn-004fbf60)
  - `FALL_THROUGH` [`004fbf7c`](#insn-004fbf7c) → [`004fbf80`](#insn-004fbf80)
- ブロック [`004fbf80`](#insn-004fbf80) 範囲 `[['004fbf80', '004fbf87']]`
  - `FALL_THROUGH` [`004fbf84`](#insn-004fbf84) → [`004fbf88`](#insn-004fbf88)
- ブロック [`004fbf88`](#insn-004fbf88) 範囲 `[['004fbf88', '004fbf97']]`
  - `CONDITIONAL_JUMP` [`004fbf94`](#insn-004fbf94) → [`004fbfa4`](#insn-004fbfa4)
  - `FALL_THROUGH` [`004fbf94`](#insn-004fbf94) → [`004fbf98`](#insn-004fbf98)
- ブロック [`004fbf98`](#insn-004fbf98) 範囲 `[['004fbf98', '004fbfa3']]`
  - `UNCONDITIONAL_JUMP` [`004fbfa0`](#insn-004fbfa0) → [`004fc4ec`](#insn-004fc4ec)
- ブロック [`004fbfa4`](#insn-004fbfa4) 範囲 `[['004fbfa4', '004fbfdb']]`
  - `UNCONDITIONAL_JUMP` [`004fbfd8`](#insn-004fbfd8) → [`004fbfe4`](#insn-004fbfe4)
- ブロック [`004fbfdc`](#insn-004fbfdc) 範囲 `[['004fbfdc', '004fbfe3']]`
  - `CONDITIONAL_JUMP` [`004fbfe0`](#insn-004fbfe0) → [`004fc49c`](#insn-004fc49c)
  - `FALL_THROUGH` [`004fbfe0`](#insn-004fbfe0) → [`004fbfe4`](#insn-004fbfe4)
- ブロック [`004fbfe4`](#insn-004fbfe4) 範囲 `[['004fbfe4', '004fc01b']]`
  - `CONDITIONAL_JUMP` [`004fc018`](#insn-004fc018) → [`004fc034`](#insn-004fc034)
  - `FALL_THROUGH` [`004fc018`](#insn-004fc018) → [`004fc01c`](#insn-004fc01c)
- ブロック [`004fc01c`](#insn-004fc01c) 範囲 `[['004fc01c', '004fc033']]`
  - `UNCONDITIONAL_JUMP` [`004fc030`](#insn-004fc030) → [`004fc060`](#insn-004fc060)
- ブロック [`004fc034`](#insn-004fc034) 範囲 `[['004fc034', '004fc05f']]`
  - `FALL_THROUGH` [`004fc05c`](#insn-004fc05c) → [`004fc060`](#insn-004fc060)
- ブロック [`004fc060`](#insn-004fc060) 範囲 `[['004fc060', '004fc073']]`
  - `CONDITIONAL_JUMP` [`004fc070`](#insn-004fc070) → [`004fc080`](#insn-004fc080)
  - `FALL_THROUGH` [`004fc070`](#insn-004fc070) → [`004fc074`](#insn-004fc074)
- ブロック [`004fc074`](#insn-004fc074) 範囲 `[['004fc074', '004fc07f']]`
  - `FALL_THROUGH` [`004fc07c`](#insn-004fc07c) → [`004fc080`](#insn-004fc080)
- ブロック [`004fc080`](#insn-004fc080) 範囲 `[['004fc080', '004fc097']]`
  - `CONDITIONAL_JUMP` [`004fc094`](#insn-004fc094) → [`004fc0bc`](#insn-004fc0bc)
  - `FALL_THROUGH` [`004fc094`](#insn-004fc094) → [`004fc098`](#insn-004fc098)
- ブロック [`004fc098`](#insn-004fc098) 範囲 `[['004fc098', '004fc0bb']]`
  - `FALL_THROUGH` [`004fc0b8`](#insn-004fc0b8) → [`004fc0bc`](#insn-004fc0bc)
- ブロック [`004fc0bc`](#insn-004fc0bc) 範囲 `[['004fc0bc', '004fc0fb']]`
  - `CONDITIONAL_JUMP` [`004fc0f8`](#insn-004fc0f8) → [`004fc104`](#insn-004fc104)
  - `FALL_THROUGH` [`004fc0f8`](#insn-004fc0f8) → [`004fc0fc`](#insn-004fc0fc)
- ブロック [`004fc0fc`](#insn-004fc0fc) 範囲 `[['004fc0fc', '004fc0ff']]`
  - `UNCONDITIONAL_JUMP` [`004fc0fc`](#insn-004fc0fc) → [`004fc474`](#insn-004fc474)
- ブロック [`004fc100`](#insn-004fc100) 範囲 `[['004fc100', '004fc103']]`
  - `FALL_THROUGH` [`004fc100`](#insn-004fc100) → [`004fc104`](#insn-004fc104)
- ブロック [`004fc104`](#insn-004fc104) 範囲 `[['004fc104', '004fc10f']]`
  - `CONDITIONAL_JUMP` [`004fc10c`](#insn-004fc10c) → [`004fc430`](#insn-004fc430)
  - `FALL_THROUGH` [`004fc10c`](#insn-004fc10c) → [`004fc110`](#insn-004fc110)
- ブロック [`004fc110`](#insn-004fc110) 範囲 `[['004fc110', '004fc11f']]`
  - `CONDITIONAL_JUMP` [`004fc11c`](#insn-004fc11c) → [`004fc568`](#insn-004fc568)
  - `FALL_THROUGH` [`004fc11c`](#insn-004fc11c) → [`004fc120`](#insn-004fc120)
- ブロック [`004fc120`](#insn-004fc120) 範囲 `[['004fc120', '004fc12b']]`
  - `CONDITIONAL_JUMP` [`004fc128`](#insn-004fc128) → [`004fc140`](#insn-004fc140)
  - `FALL_THROUGH` [`004fc128`](#insn-004fc128) → [`004fc12c`](#insn-004fc12c)
- ブロック [`004fc12c`](#insn-004fc12c) 範囲 `[['004fc12c', '004fc13b']]`
  - `CONDITIONAL_JUMP` [`004fc138`](#insn-004fc138) → [`004fc170`](#insn-004fc170)
  - `FALL_THROUGH` [`004fc138`](#insn-004fc138) → [`004fc13c`](#insn-004fc13c)
- ブロック [`004fc13c`](#insn-004fc13c) 範囲 `[['004fc13c', '004fc13f']]`
  - `UNCONDITIONAL_JUMP` [`004fc13c`](#insn-004fc13c) → [`004fc180`](#insn-004fc180)
- ブロック [`004fc140`](#insn-004fc140) 範囲 `[['004fc140', '004fc16f']]`
  - `FALL_THROUGH` [`004fc16c`](#insn-004fc16c) → [`004fc170`](#insn-004fc170)
- ブロック [`004fc170`](#insn-004fc170) 範囲 `[['004fc170', '004fc17f']]`
  - `FALL_THROUGH` [`004fc17c`](#insn-004fc17c) → [`004fc180`](#insn-004fc180)
- ブロック [`004fc180`](#insn-004fc180) 範囲 `[['004fc180', '004fc19f']]`
  - `CONDITIONAL_JUMP` [`004fc19c`](#insn-004fc19c) → [`004fc1c4`](#insn-004fc1c4)
  - `FALL_THROUGH` [`004fc19c`](#insn-004fc19c) → [`004fc1a0`](#insn-004fc1a0)
- ブロック [`004fc1a0`](#insn-004fc1a0) 範囲 `[['004fc1a0', '004fc1a7']]`
  - `CONDITIONAL_JUMP` [`004fc1a4`](#insn-004fc1a4) → [`004fc1e0`](#insn-004fc1e0)
  - `FALL_THROUGH` [`004fc1a4`](#insn-004fc1a4) → [`004fc1a8`](#insn-004fc1a8)
- ブロック [`004fc1a8`](#insn-004fc1a8) 範囲 `[['004fc1a8', '004fc1bf']]`
  - `CONDITIONAL_JUMP` [`004fc1bc`](#insn-004fc1bc) → [`004fc1e0`](#insn-004fc1e0)
  - `FALL_THROUGH` [`004fc1bc`](#insn-004fc1bc) → [`004fc1c0`](#insn-004fc1c0)
- ブロック [`004fc1c0`](#insn-004fc1c0) 範囲 `[['004fc1c0', '004fc1c3']]`
  - `UNCONDITIONAL_JUMP` [`004fc1c0`](#insn-004fc1c0) → [`004fc400`](#insn-004fc400)
- ブロック [`004fc1c4`](#insn-004fc1c4) 範囲 `[['004fc1c4', '004fc1df']]`
  - `CONDITIONAL_JUMP` [`004fc1dc`](#insn-004fc1dc) → [`004fc400`](#insn-004fc400)
  - `FALL_THROUGH` [`004fc1dc`](#insn-004fc1dc) → [`004fc1e0`](#insn-004fc1e0)
- ブロック [`004fc1e0`](#insn-004fc1e0) 範囲 `[['004fc1e0', '004fc203']]`
  - `CONDITIONAL_JUMP` [`004fc200`](#insn-004fc200) → [`004fc584`](#insn-004fc584)
  - `FALL_THROUGH` [`004fc200`](#insn-004fc200) → [`004fc204`](#insn-004fc204)
- ブロック [`004fc204`](#insn-004fc204) 範囲 `[['004fc204', '004fc20b']]`
  - `CONDITIONAL_JUMP` [`004fc208`](#insn-004fc208) → [`004fc228`](#insn-004fc228)
  - `FALL_THROUGH` [`004fc208`](#insn-004fc208) → [`004fc20c`](#insn-004fc20c)
- ブロック [`004fc20c`](#insn-004fc20c) 範囲 `[['004fc20c', '004fc223']]`
  - `CONDITIONAL_JUMP` [`004fc220`](#insn-004fc220) → [`004fc258`](#insn-004fc258)
  - `FALL_THROUGH` [`004fc220`](#insn-004fc220) → [`004fc224`](#insn-004fc224)
- ブロック [`004fc224`](#insn-004fc224) 範囲 `[['004fc224', '004fc227']]`
  - `UNCONDITIONAL_JUMP` [`004fc224`](#insn-004fc224) → [`004fc274`](#insn-004fc274)
- ブロック [`004fc228`](#insn-004fc228) 範囲 `[['004fc228', '004fc257']]`
  - `FALL_THROUGH` [`004fc254`](#insn-004fc254) → [`004fc258`](#insn-004fc258)
- ブロック [`004fc258`](#insn-004fc258) 範囲 `[['004fc258', '004fc273']]`
  - `FALL_THROUGH` [`004fc270`](#insn-004fc270) → [`004fc274`](#insn-004fc274)
- ブロック [`004fc274`](#insn-004fc274) 範囲 `[['004fc274', '004fc2bb']]`
  - `CONDITIONAL_JUMP` [`004fc2b8`](#insn-004fc2b8) → [`004fc2c4`](#insn-004fc2c4)
  - `FALL_THROUGH` [`004fc2b8`](#insn-004fc2b8) → [`004fc2bc`](#insn-004fc2bc)
- ブロック [`004fc2bc`](#insn-004fc2bc) 範囲 `[['004fc2bc', '004fc2c3']]`
  - `FALL_THROUGH` [`004fc2c0`](#insn-004fc2c0) → [`004fc2c4`](#insn-004fc2c4)
- ブロック [`004fc2c4`](#insn-004fc2c4) 範囲 `[['004fc2c4', '004fc2e3']]`
  - `CONDITIONAL_JUMP` [`004fc2e0`](#insn-004fc2e0) → [`004fc3e8`](#insn-004fc3e8)
  - `FALL_THROUGH` [`004fc2e0`](#insn-004fc2e0) → [`004fc2e4`](#insn-004fc2e4)
- ブロック [`004fc2e4`](#insn-004fc2e4) 範囲 `[['004fc2e4', '004fc2f3']]`
  - `CONDITIONAL_JUMP` [`004fc2f0`](#insn-004fc2f0) → [`004fc388`](#insn-004fc388)
  - `FALL_THROUGH` [`004fc2f0`](#insn-004fc2f0) → [`004fc2f4`](#insn-004fc2f4)
- ブロック [`004fc2f4`](#insn-004fc2f4) 範囲 `[['004fc2f4', '004fc2fb']]`
  - `CONDITIONAL_JUMP` [`004fc2f8`](#insn-004fc2f8) → [`004fc3e8`](#insn-004fc3e8)
  - `FALL_THROUGH` [`004fc2f8`](#insn-004fc2f8) → [`004fc2fc`](#insn-004fc2fc)
- ブロック [`004fc2fc`](#insn-004fc2fc) 範囲 `[['004fc2fc', '004fc327']]`
  - `CONDITIONAL_JUMP` [`004fc324`](#insn-004fc324) → [`004fc334`](#insn-004fc334)
  - `FALL_THROUGH` [`004fc324`](#insn-004fc324) → [`004fc328`](#insn-004fc328)
- ブロック [`004fc328`](#insn-004fc328) 範囲 `[['004fc328', '004fc333']]`
  - `FALL_THROUGH` [`004fc330`](#insn-004fc330) → [`004fc334`](#insn-004fc334)
- ブロック [`004fc334`](#insn-004fc334) 範囲 `[['004fc334', '004fc33b']]`
  - `CONDITIONAL_JUMP` [`004fc338`](#insn-004fc338) → [`004fc3c8`](#insn-004fc3c8)
  - `FALL_THROUGH` [`004fc338`](#insn-004fc338) → [`004fc33c`](#insn-004fc33c)
- ブロック [`004fc33c`](#insn-004fc33c) 範囲 `[['004fc33c', '004fc36f']]`
  - `CONDITIONAL_JUMP` [`004fc36c`](#insn-004fc36c) → [`004fc3d4`](#insn-004fc3d4)
  - `FALL_THROUGH` [`004fc36c`](#insn-004fc36c) → [`004fc370`](#insn-004fc370)
- ブロック [`004fc370`](#insn-004fc370) 範囲 `[['004fc370', '004fc387']]`
  - `UNCONDITIONAL_JUMP` [`004fc384`](#insn-004fc384) → [`004fc3dc`](#insn-004fc3dc)
- ブロック [`004fc388`](#insn-004fc388) 範囲 `[['004fc388', '004fc393']]`
  - `CONDITIONAL_JUMP` [`004fc390`](#insn-004fc390) → [`004fc3b8`](#insn-004fc3b8)
  - `FALL_THROUGH` [`004fc390`](#insn-004fc390) → [`004fc394`](#insn-004fc394)
- ブロック [`004fc394`](#insn-004fc394) 範囲 `[['004fc394', '004fc39b']]`
  - `CONDITIONAL_JUMP` [`004fc398`](#insn-004fc398) → [`004fc410`](#insn-004fc410)
  - `FALL_THROUGH` [`004fc398`](#insn-004fc398) → [`004fc39c`](#insn-004fc39c)
- ブロック [`004fc39c`](#insn-004fc39c) 範囲 `[['004fc39c', '004fc3b7']]`
  - `UNCONDITIONAL_JUMP` [`004fc3b4`](#insn-004fc3b4) → [`004fc420`](#insn-004fc420)
- ブロック [`004fc3b8`](#insn-004fc3b8) 範囲 `[['004fc3b8', '004fc3c7']]`
  - `UNCONDITIONAL_JUMP` [`004fc3c4`](#insn-004fc3c4) → [`004fc420`](#insn-004fc420)
- ブロック [`004fc3c8`](#insn-004fc3c8) 範囲 `[['004fc3c8', '004fc3d3']]`
  - `CONDITIONAL_JUMP` [`004fc3d0`](#insn-004fc3d0) → [`004fc370`](#insn-004fc370)
  - `FALL_THROUGH` [`004fc3d0`](#insn-004fc3d0) → [`004fc3d4`](#insn-004fc3d4)
- ブロック [`004fc3d4`](#insn-004fc3d4) 範囲 `[['004fc3d4', '004fc3db']]`
  - `FALL_THROUGH` [`004fc3d8`](#insn-004fc3d8) → [`004fc3dc`](#insn-004fc3dc)
- ブロック [`004fc3dc`](#insn-004fc3dc) 範囲 `[['004fc3dc', '004fc3e7']]`
  - `FALL_THROUGH` [`004fc3e4`](#insn-004fc3e4) → [`004fc3e8`](#insn-004fc3e8)
- ブロック [`004fc3e8`](#insn-004fc3e8) 範囲 `[['004fc3e8', '004fc3ef']]`
  - `CONDITIONAL_JUMP` [`004fc3ec`](#insn-004fc3ec) → [`004fc3f8`](#insn-004fc3f8)
  - `FALL_THROUGH` [`004fc3ec`](#insn-004fc3ec) → [`004fc3f0`](#insn-004fc3f0)
- ブロック [`004fc3f0`](#insn-004fc3f0) 範囲 `[['004fc3f0', '004fc3f7']]`
  - `FALL_THROUGH` [`004fc3f4`](#insn-004fc3f4) → [`004fc3f8`](#insn-004fc3f8)
- ブロック [`004fc3f8`](#insn-004fc3f8) 範囲 `[['004fc3f8', '004fc3ff']]`
  - `FALL_THROUGH` [`004fc3fc`](#insn-004fc3fc) → [`004fc400`](#insn-004fc400)
- ブロック [`004fc400`](#insn-004fc400) 範囲 `[['004fc400', '004fc403']]`
  - `CONDITIONAL_JUMP` [`004fc400`](#insn-004fc400) → [`004fc100`](#insn-004fc100)
  - `FALL_THROUGH` [`004fc400`](#insn-004fc400) → [`004fc404`](#insn-004fc404)
- ブロック [`004fc404`](#insn-004fc404) 範囲 `[['004fc404', '004fc40f']]`
  - `UNCONDITIONAL_JUMP` [`004fc40c`](#insn-004fc40c) → [`004fc100`](#insn-004fc100)
- ブロック [`004fc410`](#insn-004fc410) 範囲 `[['004fc410', '004fc41f']]`
  - `FALL_THROUGH` [`004fc41c`](#insn-004fc41c) → [`004fc420`](#insn-004fc420)
- ブロック [`004fc420`](#insn-004fc420) 範囲 `[['004fc420', '004fc42b']]`
  - `CONDITIONAL_JUMP` [`004fc428`](#insn-004fc428) → [`004fc3f0`](#insn-004fc3f0)
  - `FALL_THROUGH` [`004fc428`](#insn-004fc428) → [`004fc42c`](#insn-004fc42c)
- ブロック [`004fc42c`](#insn-004fc42c) 範囲 `[['004fc42c', '004fc42f']]`
  - `UNCONDITIONAL_JUMP` [`004fc42c`](#insn-004fc42c) → [`004fc3f8`](#insn-004fc3f8)
- ブロック [`004fc430`](#insn-004fc430) 範囲 `[['004fc430', '004fc43b']]`
  - `CONDITIONAL_JUMP` [`004fc438`](#insn-004fc438) → [`004fc458`](#insn-004fc458)
  - `FALL_THROUGH` [`004fc438`](#insn-004fc438) → [`004fc43c`](#insn-004fc43c)
- ブロック [`004fc43c`](#insn-004fc43c) 範囲 `[['004fc43c', '004fc447']]`
  - `CONDITIONAL_JUMP` [`004fc444`](#insn-004fc444) → [`004fc5a4`](#insn-004fc5a4)
  - `FALL_THROUGH` [`004fc444`](#insn-004fc444) → [`004fc448`](#insn-004fc448)
- ブロック [`004fc448`](#insn-004fc448) 範囲 `[['004fc448', '004fc457']]`
  - `FALL_THROUGH` [`004fc454`](#insn-004fc454) → [`004fc458`](#insn-004fc458)
- ブロック [`004fc458`](#insn-004fc458) 範囲 `[['004fc458', '004fc467']]`
  - `CONDITIONAL_JUMP` [`004fc464`](#insn-004fc464) → [`004fc474`](#insn-004fc474)
  - `FALL_THROUGH` [`004fc464`](#insn-004fc464) → [`004fc468`](#insn-004fc468)
- ブロック [`004fc468`](#insn-004fc468) 範囲 `[['004fc468', '004fc46b']]`
  - `CONDITIONAL_JUMP` [`004fc468`](#insn-004fc468) → [`004fc488`](#insn-004fc488)
  - `FALL_THROUGH` [`004fc468`](#insn-004fc468) → [`004fc46c`](#insn-004fc46c)
- ブロック [`004fc46c`](#insn-004fc46c) 範囲 `[['004fc46c', '004fc473']]`
  - `UNCONDITIONAL_JUMP` [`004fc470`](#insn-004fc470) → [`004fc47c`](#insn-004fc47c)
- ブロック [`004fc474`](#insn-004fc474) 範囲 `[['004fc474', '004fc47b']]`
  - `FALL_THROUGH` [`004fc478`](#insn-004fc478) → [`004fc47c`](#insn-004fc47c)
- ブロック [`004fc47c`](#insn-004fc47c) 範囲 `[['004fc47c', '004fc487']]`
  - `FALL_THROUGH` [`004fc484`](#insn-004fc484) → [`004fc488`](#insn-004fc488)
- ブロック [`004fc488`](#insn-004fc488) 範囲 `[['004fc488', '004fc48f']]`
  - `CONDITIONAL_JUMP` [`004fc48c`](#insn-004fc48c) → [`004fbfdc`](#insn-004fbfdc)
  - `FALL_THROUGH` [`004fc48c`](#insn-004fc48c) → [`004fc490`](#insn-004fc490)
- ブロック [`004fc490`](#insn-004fc490) 範囲 `[['004fc490', '004fc49b']]`
  - `UNCONDITIONAL_JUMP` [`004fc498`](#insn-004fc498) → [`004fbfdc`](#insn-004fbfdc)
- ブロック [`004fc49c`](#insn-004fc49c) 範囲 `[['004fc49c', '004fc4ab']]`
  - `CONDITIONAL_JUMP` [`004fc4a8`](#insn-004fc4a8) → [`004fc4ec`](#insn-004fc4ec)
  - `FALL_THROUGH` [`004fc4a8`](#insn-004fc4a8) → [`004fc4ac`](#insn-004fc4ac)
- ブロック [`004fc4ac`](#insn-004fc4ac) 範囲 `[['004fc4ac', '004fc4b7']]`
  - `CONDITIONAL_JUMP` [`004fc4b4`](#insn-004fc4b4) → [`004fc4e0`](#insn-004fc4e0)
  - `FALL_THROUGH` [`004fc4b4`](#insn-004fc4b4) → [`004fc4b8`](#insn-004fc4b8)
- ブロック [`004fc4b8`](#insn-004fc4b8) 範囲 `[['004fc4b8', '004fc4bf']]`
  - `UNCONDITIONAL_JUMP` [`004fc4bc`](#insn-004fc4bc) → [`004fc4cc`](#insn-004fc4cc)
- ブロック [`004fc4c0`](#insn-004fc4c0) 範囲 `[['004fc4c0', '004fc4cb']]`
  - `CONDITIONAL_JUMP` [`004fc4c8`](#insn-004fc4c8) → [`004fc4e0`](#insn-004fc4e0)
  - `FALL_THROUGH` [`004fc4c8`](#insn-004fc4c8) → [`004fc4cc`](#insn-004fc4cc)
- ブロック [`004fc4cc`](#insn-004fc4cc) 範囲 `[['004fc4cc', '004fc4d3']]`
  - `CONDITIONAL_JUMP` [`004fc4d0`](#insn-004fc4d0) → [`004fc4c0`](#insn-004fc4c0)
  - `FALL_THROUGH` [`004fc4d0`](#insn-004fc4d0) → [`004fc4d4`](#insn-004fc4d4)
- ブロック [`004fc4d4`](#insn-004fc4d4) 範囲 `[['004fc4d4', '004fc4df']]`
  - `UNCONDITIONAL_JUMP` [`004fc4dc`](#insn-004fc4dc) → [`004fc4c0`](#insn-004fc4c0)
- ブロック [`004fc4e0`](#insn-004fc4e0) 範囲 `[['004fc4e0', '004fc4eb']]`
  - `FALL_THROUGH` [`004fc4e8`](#insn-004fc4e8) → [`004fc4ec`](#insn-004fc4ec)
- ブロック [`004fc4ec`](#insn-004fc4ec) 範囲 `[['004fc4ec', '004fc547']]`
  - `CONDITIONAL_JUMP` [`004fc544`](#insn-004fc544) → [`004fc698`](#insn-004fc698)
  - `FALL_THROUGH` [`004fc544`](#insn-004fc544) → [`004fc548`](#insn-004fc548)
- ブロック [`004fc548`](#insn-004fc548) 範囲 `[['004fc548', '004fc567']]`
- ブロック [`004fc568`](#insn-004fc568) 範囲 `[['004fc568', '004fc57b']]`
  - `CONDITIONAL_JUMP` [`004fc578`](#insn-004fc578) → [`004fc698`](#insn-004fc698)
  - `FALL_THROUGH` [`004fc578`](#insn-004fc578) → [`004fc57c`](#insn-004fc57c)
- ブロック [`004fc57c`](#insn-004fc57c) 範囲 `[['004fc57c', '004fc583']]`
- ブロック [`004fc584`](#insn-004fc584) 範囲 `[['004fc584', '004fc597']]`
  - `CONDITIONAL_JUMP` [`004fc594`](#insn-004fc594) → [`004fc698`](#insn-004fc698)
  - `FALL_THROUGH` [`004fc594`](#insn-004fc594) → [`004fc598`](#insn-004fc598)
- ブロック [`004fc598`](#insn-004fc598) 範囲 `[['004fc598', '004fc5a3']]`
- ブロック [`004fc5a4`](#insn-004fc5a4) 範囲 `[['004fc5a4', '004fc5b7']]`
  - `CONDITIONAL_JUMP` [`004fc5b4`](#insn-004fc5b4) → [`004fc698`](#insn-004fc698)
  - `FALL_THROUGH` [`004fc5b4`](#insn-004fc5b4) → [`004fc5b8`](#insn-004fc5b8)
- ブロック [`004fc5b8`](#insn-004fc5b8) 範囲 `[['004fc5b8', '004fc5bb']]`
- ブロック [`004fc698`](#insn-004fc698) 範囲 `[['004fc698', '004fc69b']]`

## 命令位置別の参照

- [`004fbebc`](#insn-004fbebc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbec0`](#insn-004fbec0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbec4`](#insn-004fbec4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbec8`](#insn-004fbec8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbecc`](#insn-004fbecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbed0`](#insn-004fbed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbee8`](#insn-004fbee8) → `Stack[-0x1f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbef4`](#insn-004fbef4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf04`](#insn-004fbf04) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf08`](#insn-004fbf08) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf0c`](#insn-004fbf0c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf10`](#insn-004fbf10) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf18`](#insn-004fbf18) → [`0053a074`](../0053a/0053a074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053a074` · 推定シンボル `None` · 推定型 `None`
- [`004fbf1c`](#insn-004fbf1c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf24`](#insn-004fbf24) → [`004fbf74`](#insn-004fbf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf28`](#insn-004fbf28) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf5c`](#insn-004fbf5c) → [`004fbf80`](#insn-004fbf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf70`](#insn-004fbf70) → [`004fbf88`](#insn-004fbf88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf7c`](#insn-004fbf7c) → [`004fbf60`](#insn-004fbf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf84`](#insn-004fbf84) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`004fbf88`](#insn-004fbf88) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf90`](#insn-004fbf90) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf94`](#insn-004fbf94) → [`004fbfa4`](#insn-004fbfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf9c`](#insn-004fbf9c) → [`00539edc`](../00539/00539edc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00539edc` · 推定シンボル `None` · 推定型 `None`
- [`004fbfa0`](#insn-004fbfa0) → [`004fc4ec`](#insn-004fc4ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfbc`](#insn-004fbfbc) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfc8`](#insn-004fbfc8) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfd4`](#insn-004fbfd4) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfd8`](#insn-004fbfd8) → [`004fbfe4`](#insn-004fbfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfdc`](#insn-004fbfdc) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfe0`](#insn-004fbfe0) → [`004fc49c`](#insn-004fc49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfe4`](#insn-004fbfe4) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbff4`](#insn-004fbff4) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc018`](#insn-004fc018) → [`004fc034`](#insn-004fc034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc028`](#insn-004fc028) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc02c`](#insn-004fc02c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc030`](#insn-004fc030) → [`004fc060`](#insn-004fc060) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc03c`](#insn-004fc03c) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`004fc040`](#insn-004fc040) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc05c`](#insn-004fc05c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc070`](#insn-004fc070) → [`004fc080`](#insn-004fc080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc078`](#insn-004fc078) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc07c`](#insn-004fc07c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc080`](#insn-004fc080) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc090`](#insn-004fc090) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc094`](#insn-004fc094) → [`004fc0bc`](#insn-004fc0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc098`](#insn-004fc098) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0a0`](#insn-004fc0a0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc0a4`](#insn-004fc0a4) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0a8`](#insn-004fc0a8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0b4`](#insn-004fc0b4) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0b8`](#insn-004fc0b8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0bc`](#insn-004fc0bc) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0c0`](#insn-004fc0c0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0c8`](#insn-004fc0c8) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0d0`](#insn-004fc0d0) → [`00c59440`](../00c59/00c59440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59440` · 推定シンボル `None` · 推定型 `None`
- [`004fc0dc`](#insn-004fc0dc) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0e0`](#insn-004fc0e0) → `00c69f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004fc0e0`](#insn-004fc0e0) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0e4`](#insn-004fc0e4) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0ec`](#insn-004fc0ec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0f0`](#insn-004fc0f0) → `00c9acc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fc0f4`](#insn-004fc0f4) → [`0112a148`](../0112a/0112a148.md) · `DATA` · `ANALYSIS` · 関数 `0112a148` · 推定シンボル `None` · 推定型 `None`
- [`004fc0f4`](#insn-004fc0f4) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0f8`](#insn-004fc0f8) → [`004fc104`](#insn-004fc104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0fc`](#insn-004fc0fc) → [`004fc474`](#insn-004fc474) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc100`](#insn-004fc100) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc104`](#insn-004fc104) → [`00c59450`](../00c59/00c59450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59450` · 推定シンボル `None` · 推定型 `None`
- [`004fc10c`](#insn-004fc10c) → [`004fc430`](#insn-004fc430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc114`](#insn-004fc114) → [`00c57be0`](../00c57/00c57be0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57be0` · 推定シンボル `None` · 推定型 `None`
- [`004fc11c`](#insn-004fc11c) → [`004fc568`](#insn-004fc568) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc128`](#insn-004fc128) → [`004fc140`](#insn-004fc140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc134`](#insn-004fc134) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc138`](#insn-004fc138) → [`004fc170`](#insn-004fc170) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc13c`](#insn-004fc13c) → [`004fc180`](#insn-004fc180) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc15c`](#insn-004fc15c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`004fc168`](#insn-004fc168) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc16c`](#insn-004fc16c) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc17c`](#insn-004fc17c) → [`00c57b40`](../00c57/00c57b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b40` · 推定シンボル `None` · 推定型 `None`
- [`004fc184`](#insn-004fc184) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc188`](#insn-004fc188) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc19c`](#insn-004fc19c) → [`004fc1c4`](#insn-004fc1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1a4`](#insn-004fc1a4) → [`004fc1e0`](#insn-004fc1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1a8`](#insn-004fc1a8) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1bc`](#insn-004fc1bc) → [`004fc1e0`](#insn-004fc1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1c0`](#insn-004fc1c0) → [`004fc400`](#insn-004fc400) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1c4`](#insn-004fc1c4) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1dc`](#insn-004fc1dc) → [`004fc400`](#insn-004fc400) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1e0`](#insn-004fc1e0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1e4`](#insn-004fc1e4) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc200`](#insn-004fc200) → [`004fc584`](#insn-004fc584) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc208`](#insn-004fc208) → [`004fc228`](#insn-004fc228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc210`](#insn-004fc210) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc214`](#insn-004fc214) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc218`](#insn-004fc218) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc21c`](#insn-004fc21c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc220`](#insn-004fc220) → [`004fc258`](#insn-004fc258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc224`](#insn-004fc224) → [`004fc274`](#insn-004fc274) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc244`](#insn-004fc244) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`004fc250`](#insn-004fc250) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc254`](#insn-004fc254) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc258`](#insn-004fc258) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc25c`](#insn-004fc25c) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc270`](#insn-004fc270) → [`00c57b40`](../00c57/00c57b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b40` · 推定シンボル `None` · 推定型 `None`
- [`004fc274`](#insn-004fc274) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc290`](#insn-004fc290) → [`00c57b80`](../00c57/00c57b80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b80` · 推定シンボル `None` · 推定型 `None`
- [`004fc2a0`](#insn-004fc2a0) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2a8`](#insn-004fc2a8) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2b4`](#insn-004fc2b4) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2b8`](#insn-004fc2b8) → [`004fc2c4`](#insn-004fc2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2bc`](#insn-004fc2bc) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2c0`](#insn-004fc2c0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc2c4`](#insn-004fc2c4) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2c8`](#insn-004fc2c8) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2d8`](#insn-004fc2d8) → [`00c59460`](../00c59/00c59460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59460` · 推定シンボル `None` · 推定型 `None`
- [`004fc2e0`](#insn-004fc2e0) → [`004fc3e8`](#insn-004fc3e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2e4`](#insn-004fc2e4) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2f0`](#insn-004fc2f0) → [`004fc388`](#insn-004fc388) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2f8`](#insn-004fc2f8) → [`004fc3e8`](#insn-004fc3e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2fc`](#insn-004fc2fc) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc314`](#insn-004fc314) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc324`](#insn-004fc324) → [`004fc334`](#insn-004fc334) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc32c`](#insn-004fc32c) → [`0053a074`](../0053a/0053a074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053a074` · 推定シンボル `None` · 推定型 `None`
- [`004fc330`](#insn-004fc330) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc338`](#insn-004fc338) → [`004fc3c8`](#insn-004fc3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc33c`](#insn-004fc33c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc368`](#insn-004fc368) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc36c`](#insn-004fc36c) → [`004fc3d4`](#insn-004fc3d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc374`](#insn-004fc374) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc378`](#insn-004fc378) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc384`](#insn-004fc384) → [`004fc3dc`](#insn-004fc3dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc388`](#insn-004fc388) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc390`](#insn-004fc390) → [`004fc3b8`](#insn-004fc3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc394`](#insn-004fc394) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc398`](#insn-004fc398) → [`004fc410`](#insn-004fc410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3a0`](#insn-004fc3a0) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3a8`](#insn-004fc3a8) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3b4`](#insn-004fc3b4) → [`004fc420`](#insn-004fc420) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3c0`](#insn-004fc3c0) → [`00540d3c`](../00540/00540d3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00540d3c` · 推定シンボル `None` · 推定型 `None`
- [`004fc3c4`](#insn-004fc3c4) → [`004fc420`](#insn-004fc420) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3cc`](#insn-004fc3cc) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3d0`](#insn-004fc3d0) → [`004fc370`](#insn-004fc370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3d4`](#insn-004fc3d4) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3d8`](#insn-004fc3d8) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`004fc3dc`](#insn-004fc3dc) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3e4`](#insn-004fc3e4) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3e8`](#insn-004fc3e8) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3ec`](#insn-004fc3ec) → [`004fc3f8`](#insn-004fc3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3f0`](#insn-004fc3f0) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3f4`](#insn-004fc3f4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc3f8`](#insn-004fc3f8) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc400`](#insn-004fc400) → [`004fc100`](#insn-004fc100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc404`](#insn-004fc404) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc408`](#insn-004fc408) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc40c`](#insn-004fc40c) → [`004fc100`](#insn-004fc100) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc410`](#insn-004fc410) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc418`](#insn-004fc418) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`004fc420`](#insn-004fc420) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc424`](#insn-004fc424) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc428`](#insn-004fc428) → [`004fc3f0`](#insn-004fc3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc42c`](#insn-004fc42c) → [`004fc3f8`](#insn-004fc3f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc430`](#insn-004fc430) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc434`](#insn-004fc434) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc438`](#insn-004fc438) → [`004fc458`](#insn-004fc458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc43c`](#insn-004fc43c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc440`](#insn-004fc440) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc444`](#insn-004fc444) → [`004fc5a4`](#insn-004fc5a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc448`](#insn-004fc448) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc44c`](#insn-004fc44c) → `00c69f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004fc454`](#insn-004fc454) → [`0053aa2c`](../0053a/0053aa2c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0053aa2c` · 推定シンボル `None` · 推定型 `None`
- [`004fc458`](#insn-004fc458) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc45c`](#insn-004fc45c) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc464`](#insn-004fc464) → [`004fc474`](#insn-004fc474) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc468`](#insn-004fc468) → [`004fc488`](#insn-004fc488) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc470`](#insn-004fc470) → [`004fc47c`](#insn-004fc47c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc47c`](#insn-004fc47c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc480`](#insn-004fc480) → `00c69f68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fc480`](#insn-004fc480) → `00c69f70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fc484`](#insn-004fc484) → [`0053aa24`](../0053a/0053aa24.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0053aa24` · 推定シンボル `None` · 推定型 `None`
- [`004fc484`](#insn-004fc484) → [`0053aa28`](../0053a/0053aa28.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0053aa28` · 推定シンボル `None` · 推定型 `None`
- [`004fc488`](#insn-004fc488) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc48c`](#insn-004fc48c) → [`004fbfdc`](#insn-004fbfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc490`](#insn-004fc490) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc494`](#insn-004fc494) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc498`](#insn-004fc498) → [`004fbfdc`](#insn-004fbfdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4a4`](#insn-004fc4a4) → [`00539edc`](../00539/00539edc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00539edc` · 推定シンボル `None` · 推定型 `None`
- [`004fc4a8`](#insn-004fc4a8) → [`004fc4ec`](#insn-004fc4ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4b4`](#insn-004fc4b4) → [`004fc4e0`](#insn-004fc4e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4bc`](#insn-004fc4bc) → [`004fc4cc`](#insn-004fc4cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4c8`](#insn-004fc4c8) → [`004fc4e0`](#insn-004fc4e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4d0`](#insn-004fc4d0) → [`004fc4c0`](#insn-004fc4c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4d8`](#insn-004fc4d8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc4dc`](#insn-004fc4dc) → [`004fc4c0`](#insn-004fc4c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4e8`](#insn-004fc4e8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fc4ec`](#insn-004fc4ec) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4f0`](#insn-004fc4f0) → `Stack[-0x1d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc530`](#insn-004fc530) → [`00545bfc`](../00545/00545bfc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00545bfc` · 推定シンボル `None` · 推定型 `None`
- [`004fc534`](#insn-004fc534) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc53c`](#insn-004fc53c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc544`](#insn-004fc544) → [`004fc698`](#insn-004fc698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc54c`](#insn-004fc54c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc550`](#insn-004fc550) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc554`](#insn-004fc554) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc558`](#insn-004fc558) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc55c`](#insn-004fc55c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc560`](#insn-004fc560) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc568`](#insn-004fc568) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc570`](#insn-004fc570) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc578`](#insn-004fc578) → [`004fc698`](#insn-004fc698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc580`](#insn-004fc580) → [`0043b724`](../0043b/0043b724.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b724` · 推定シンボル `None` · 推定型 `None`
- [`004fc584`](#insn-004fc584) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc58c`](#insn-004fc58c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc594`](#insn-004fc594) → [`004fc698`](#insn-004fc698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5a0`](#insn-004fc5a0) → [`0043b724`](../0043b/0043b724.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b724` · 推定シンボル `None` · 推定型 `None`
- [`004fc5a4`](#insn-004fc5a4) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5ac`](#insn-004fc5ac) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5b4`](#insn-004fc5b4) → [`004fc698`](#insn-004fc698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5b8`](#insn-004fc5b8) → [`00459d34`](../00459/00459d34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459d34` · 推定シンボル `None` · 推定型 `None`
- [`004fc698`](#insn-004fc698) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004fbebc`](#insn-004fbebc)

~~~json
{
  "source": "004fbebc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbec0`](#insn-004fbec0)

~~~json
{
  "source": "004fbec0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbec4`](#insn-004fbec4)

~~~json
{
  "source": "004fbec4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbec8`](#insn-004fbec8)

~~~json
{
  "source": "004fbec8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbecc`](#insn-004fbecc)

~~~json
{
  "source": "004fbecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbed0`](#insn-004fbed0)

~~~json
{
  "source": "004fbed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbee8`](#insn-004fbee8)

~~~json
{
  "source": "004fbee8",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbef4`](#insn-004fbef4)

~~~json
{
  "source": "004fbef4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf04`](#insn-004fbf04)

~~~json
{
  "source": "004fbf04",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf08`](#insn-004fbf08)

~~~json
{
  "source": "004fbf08",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf0c`](#insn-004fbf0c)

~~~json
{
  "source": "004fbf0c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf10`](#insn-004fbf10)

~~~json
{
  "source": "004fbf10",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf18`](#insn-004fbf18)

~~~json
{
  "source": "004fbf18",
  "target": "0053a074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbf1c`](#insn-004fbf1c)

~~~json
{
  "source": "004fbf1c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf24`](#insn-004fbf24)

~~~json
{
  "source": "004fbf24",
  "target": "004fbf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf28`](#insn-004fbf28)

~~~json
{
  "source": "004fbf28",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf5c`](#insn-004fbf5c)

~~~json
{
  "source": "004fbf5c",
  "target": "004fbf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf70`](#insn-004fbf70)

~~~json
{
  "source": "004fbf70",
  "target": "004fbf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf7c`](#insn-004fbf7c)

~~~json
{
  "source": "004fbf7c",
  "target": "004fbf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf84`](#insn-004fbf84)

~~~json
{
  "source": "004fbf84",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbf88`](#insn-004fbf88)

~~~json
{
  "source": "004fbf88",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf90`](#insn-004fbf90)

~~~json
{
  "source": "004fbf90",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf94`](#insn-004fbf94)

~~~json
{
  "source": "004fbf94",
  "target": "004fbfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf9c`](#insn-004fbf9c)

~~~json
{
  "source": "004fbf9c",
  "target": "00539edc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbfa0`](#insn-004fbfa0)

~~~json
{
  "source": "004fbfa0",
  "target": "004fc4ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfbc`](#insn-004fbfbc)

~~~json
{
  "source": "004fbfbc",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfc8`](#insn-004fbfc8)

~~~json
{
  "source": "004fbfc8",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfd4`](#insn-004fbfd4)

~~~json
{
  "source": "004fbfd4",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfd8`](#insn-004fbfd8)

~~~json
{
  "source": "004fbfd8",
  "target": "004fbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfdc`](#insn-004fbfdc)

~~~json
{
  "source": "004fbfdc",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfe0`](#insn-004fbfe0)

~~~json
{
  "source": "004fbfe0",
  "target": "004fc49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfe4`](#insn-004fbfe4)

~~~json
{
  "source": "004fbfe4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbff4`](#insn-004fbff4)

~~~json
{
  "source": "004fbff4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc018`](#insn-004fc018)

~~~json
{
  "source": "004fc018",
  "target": "004fc034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc028`](#insn-004fc028)

~~~json
{
  "source": "004fc028",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc02c`](#insn-004fc02c)

~~~json
{
  "source": "004fc02c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc030`](#insn-004fc030)

~~~json
{
  "source": "004fc030",
  "target": "004fc060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc03c`](#insn-004fc03c)

~~~json
{
  "source": "004fc03c",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc040`](#insn-004fc040)

~~~json
{
  "source": "004fc040",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc05c`](#insn-004fc05c)

~~~json
{
  "source": "004fc05c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc070`](#insn-004fc070)

~~~json
{
  "source": "004fc070",
  "target": "004fc080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc078`](#insn-004fc078)

~~~json
{
  "source": "004fc078",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc07c`](#insn-004fc07c)

~~~json
{
  "source": "004fc07c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc080`](#insn-004fc080)

~~~json
{
  "source": "004fc080",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc090`](#insn-004fc090)

~~~json
{
  "source": "004fc090",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc094`](#insn-004fc094)

~~~json
{
  "source": "004fc094",
  "target": "004fc0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc098`](#insn-004fc098)

~~~json
{
  "source": "004fc098",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0a0`](#insn-004fc0a0)

~~~json
{
  "source": "004fc0a0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc0a4`](#insn-004fc0a4)

~~~json
{
  "source": "004fc0a4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0a8`](#insn-004fc0a8)

~~~json
{
  "source": "004fc0a8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0b4`](#insn-004fc0b4)

~~~json
{
  "source": "004fc0b4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0b8`](#insn-004fc0b8)

~~~json
{
  "source": "004fc0b8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0bc`](#insn-004fc0bc)

~~~json
{
  "source": "004fc0bc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0c0`](#insn-004fc0c0)

~~~json
{
  "source": "004fc0c0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0c8`](#insn-004fc0c8)

~~~json
{
  "source": "004fc0c8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0d0`](#insn-004fc0d0)

~~~json
{
  "source": "004fc0d0",
  "target": "00c59440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc0dc`](#insn-004fc0dc)

~~~json
{
  "source": "004fc0dc",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0e0`](#insn-004fc0e0)

~~~json
{
  "source": "004fc0e0",
  "target": "00c69f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c69f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc0e0`](#insn-004fc0e0)

~~~json
{
  "source": "004fc0e0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0e4`](#insn-004fc0e4)

~~~json
{
  "source": "004fc0e4",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0ec`](#insn-004fc0ec)

~~~json
{
  "source": "004fc0ec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0f0`](#insn-004fc0f0)

~~~json
{
  "source": "004fc0f0",
  "target": "00c9acc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9acc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc0f4`](#insn-004fc0f4)

~~~json
{
  "source": "004fc0f4",
  "target": "0112a148",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc0f4`](#insn-004fc0f4)

~~~json
{
  "source": "004fc0f4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0f8`](#insn-004fc0f8)

~~~json
{
  "source": "004fc0f8",
  "target": "004fc104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0fc`](#insn-004fc0fc)

~~~json
{
  "source": "004fc0fc",
  "target": "004fc474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc100`](#insn-004fc100)

~~~json
{
  "source": "004fc100",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc104`](#insn-004fc104)

~~~json
{
  "source": "004fc104",
  "target": "00c59450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc10c`](#insn-004fc10c)

~~~json
{
  "source": "004fc10c",
  "target": "004fc430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc114`](#insn-004fc114)

~~~json
{
  "source": "004fc114",
  "target": "00c57be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc11c`](#insn-004fc11c)

~~~json
{
  "source": "004fc11c",
  "target": "004fc568",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc128`](#insn-004fc128)

~~~json
{
  "source": "004fc128",
  "target": "004fc140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc134`](#insn-004fc134)

~~~json
{
  "source": "004fc134",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc138`](#insn-004fc138)

~~~json
{
  "source": "004fc138",
  "target": "004fc170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc13c`](#insn-004fc13c)

~~~json
{
  "source": "004fc13c",
  "target": "004fc180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc15c`](#insn-004fc15c)

~~~json
{
  "source": "004fc15c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc168`](#insn-004fc168)

~~~json
{
  "source": "004fc168",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc16c`](#insn-004fc16c)

~~~json
{
  "source": "004fc16c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc17c`](#insn-004fc17c)

~~~json
{
  "source": "004fc17c",
  "target": "00c57b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc184`](#insn-004fc184)

~~~json
{
  "source": "004fc184",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc188`](#insn-004fc188)

~~~json
{
  "source": "004fc188",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc19c`](#insn-004fc19c)

~~~json
{
  "source": "004fc19c",
  "target": "004fc1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1a4`](#insn-004fc1a4)

~~~json
{
  "source": "004fc1a4",
  "target": "004fc1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1a8`](#insn-004fc1a8)

~~~json
{
  "source": "004fc1a8",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1bc`](#insn-004fc1bc)

~~~json
{
  "source": "004fc1bc",
  "target": "004fc1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1c0`](#insn-004fc1c0)

~~~json
{
  "source": "004fc1c0",
  "target": "004fc400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1c4`](#insn-004fc1c4)

~~~json
{
  "source": "004fc1c4",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1dc`](#insn-004fc1dc)

~~~json
{
  "source": "004fc1dc",
  "target": "004fc400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1e0`](#insn-004fc1e0)

~~~json
{
  "source": "004fc1e0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1e4`](#insn-004fc1e4)

~~~json
{
  "source": "004fc1e4",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc200`](#insn-004fc200)

~~~json
{
  "source": "004fc200",
  "target": "004fc584",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc208`](#insn-004fc208)

~~~json
{
  "source": "004fc208",
  "target": "004fc228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc210`](#insn-004fc210)

~~~json
{
  "source": "004fc210",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc214`](#insn-004fc214)

~~~json
{
  "source": "004fc214",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc218`](#insn-004fc218)

~~~json
{
  "source": "004fc218",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc21c`](#insn-004fc21c)

~~~json
{
  "source": "004fc21c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc220`](#insn-004fc220)

~~~json
{
  "source": "004fc220",
  "target": "004fc258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc224`](#insn-004fc224)

~~~json
{
  "source": "004fc224",
  "target": "004fc274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc244`](#insn-004fc244)

~~~json
{
  "source": "004fc244",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc250`](#insn-004fc250)

~~~json
{
  "source": "004fc250",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc254`](#insn-004fc254)

~~~json
{
  "source": "004fc254",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc258`](#insn-004fc258)

~~~json
{
  "source": "004fc258",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc25c`](#insn-004fc25c)

~~~json
{
  "source": "004fc25c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc270`](#insn-004fc270)

~~~json
{
  "source": "004fc270",
  "target": "00c57b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc274`](#insn-004fc274)

~~~json
{
  "source": "004fc274",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc290`](#insn-004fc290)

~~~json
{
  "source": "004fc290",
  "target": "00c57b80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc2a0`](#insn-004fc2a0)

~~~json
{
  "source": "004fc2a0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2a8`](#insn-004fc2a8)

~~~json
{
  "source": "004fc2a8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2b4`](#insn-004fc2b4)

~~~json
{
  "source": "004fc2b4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2b8`](#insn-004fc2b8)

~~~json
{
  "source": "004fc2b8",
  "target": "004fc2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2bc`](#insn-004fc2bc)

~~~json
{
  "source": "004fc2bc",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2c0`](#insn-004fc2c0)

~~~json
{
  "source": "004fc2c0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc2c4`](#insn-004fc2c4)

~~~json
{
  "source": "004fc2c4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2c8`](#insn-004fc2c8)

~~~json
{
  "source": "004fc2c8",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2d8`](#insn-004fc2d8)

~~~json
{
  "source": "004fc2d8",
  "target": "00c59460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc2e0`](#insn-004fc2e0)

~~~json
{
  "source": "004fc2e0",
  "target": "004fc3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2e4`](#insn-004fc2e4)

~~~json
{
  "source": "004fc2e4",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2f0`](#insn-004fc2f0)

~~~json
{
  "source": "004fc2f0",
  "target": "004fc388",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2f8`](#insn-004fc2f8)

~~~json
{
  "source": "004fc2f8",
  "target": "004fc3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2fc`](#insn-004fc2fc)

~~~json
{
  "source": "004fc2fc",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc314`](#insn-004fc314)

~~~json
{
  "source": "004fc314",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc324`](#insn-004fc324)

~~~json
{
  "source": "004fc324",
  "target": "004fc334",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc32c`](#insn-004fc32c)

~~~json
{
  "source": "004fc32c",
  "target": "0053a074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc330`](#insn-004fc330)

~~~json
{
  "source": "004fc330",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc338`](#insn-004fc338)

~~~json
{
  "source": "004fc338",
  "target": "004fc3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc33c`](#insn-004fc33c)

~~~json
{
  "source": "004fc33c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc368`](#insn-004fc368)

~~~json
{
  "source": "004fc368",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc36c`](#insn-004fc36c)

~~~json
{
  "source": "004fc36c",
  "target": "004fc3d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc374`](#insn-004fc374)

~~~json
{
  "source": "004fc374",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc378`](#insn-004fc378)

~~~json
{
  "source": "004fc378",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc384`](#insn-004fc384)

~~~json
{
  "source": "004fc384",
  "target": "004fc3dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc388`](#insn-004fc388)

~~~json
{
  "source": "004fc388",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc390`](#insn-004fc390)

~~~json
{
  "source": "004fc390",
  "target": "004fc3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc394`](#insn-004fc394)

~~~json
{
  "source": "004fc394",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc398`](#insn-004fc398)

~~~json
{
  "source": "004fc398",
  "target": "004fc410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3a0`](#insn-004fc3a0)

~~~json
{
  "source": "004fc3a0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3a8`](#insn-004fc3a8)

~~~json
{
  "source": "004fc3a8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3b4`](#insn-004fc3b4)

~~~json
{
  "source": "004fc3b4",
  "target": "004fc420",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3c0`](#insn-004fc3c0)

~~~json
{
  "source": "004fc3c0",
  "target": "00540d3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc3c4`](#insn-004fc3c4)

~~~json
{
  "source": "004fc3c4",
  "target": "004fc420",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3cc`](#insn-004fc3cc)

~~~json
{
  "source": "004fc3cc",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3d0`](#insn-004fc3d0)

~~~json
{
  "source": "004fc3d0",
  "target": "004fc370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3d4`](#insn-004fc3d4)

~~~json
{
  "source": "004fc3d4",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3d8`](#insn-004fc3d8)

~~~json
{
  "source": "004fc3d8",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc3dc`](#insn-004fc3dc)

~~~json
{
  "source": "004fc3dc",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3e4`](#insn-004fc3e4)

~~~json
{
  "source": "004fc3e4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3e8`](#insn-004fc3e8)

~~~json
{
  "source": "004fc3e8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3ec`](#insn-004fc3ec)

~~~json
{
  "source": "004fc3ec",
  "target": "004fc3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3f0`](#insn-004fc3f0)

~~~json
{
  "source": "004fc3f0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3f4`](#insn-004fc3f4)

~~~json
{
  "source": "004fc3f4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc3f8`](#insn-004fc3f8)

~~~json
{
  "source": "004fc3f8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc400`](#insn-004fc400)

~~~json
{
  "source": "004fc400",
  "target": "004fc100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc404`](#insn-004fc404)

~~~json
{
  "source": "004fc404",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc408`](#insn-004fc408)

~~~json
{
  "source": "004fc408",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc40c`](#insn-004fc40c)

~~~json
{
  "source": "004fc40c",
  "target": "004fc100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc410`](#insn-004fc410)

~~~json
{
  "source": "004fc410",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc418`](#insn-004fc418)

~~~json
{
  "source": "004fc418",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc420`](#insn-004fc420)

~~~json
{
  "source": "004fc420",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc424`](#insn-004fc424)

~~~json
{
  "source": "004fc424",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc428`](#insn-004fc428)

~~~json
{
  "source": "004fc428",
  "target": "004fc3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc42c`](#insn-004fc42c)

~~~json
{
  "source": "004fc42c",
  "target": "004fc3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc430`](#insn-004fc430)

~~~json
{
  "source": "004fc430",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc434`](#insn-004fc434)

~~~json
{
  "source": "004fc434",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc438`](#insn-004fc438)

~~~json
{
  "source": "004fc438",
  "target": "004fc458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc43c`](#insn-004fc43c)

~~~json
{
  "source": "004fc43c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc440`](#insn-004fc440)

~~~json
{
  "source": "004fc440",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc444`](#insn-004fc444)

~~~json
{
  "source": "004fc444",
  "target": "004fc5a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc448`](#insn-004fc448)

~~~json
{
  "source": "004fc448",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc44c`](#insn-004fc44c)

~~~json
{
  "source": "004fc44c",
  "target": "00c69f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c69f78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc454`](#insn-004fc454)

~~~json
{
  "source": "004fc454",
  "target": "0053aa2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc458`](#insn-004fc458)

~~~json
{
  "source": "004fc458",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc45c`](#insn-004fc45c)

~~~json
{
  "source": "004fc45c",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc464`](#insn-004fc464)

~~~json
{
  "source": "004fc464",
  "target": "004fc474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc468`](#insn-004fc468)

~~~json
{
  "source": "004fc468",
  "target": "004fc488",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc470`](#insn-004fc470)

~~~json
{
  "source": "004fc470",
  "target": "004fc47c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc47c`](#insn-004fc47c)

~~~json
{
  "source": "004fc47c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc480`](#insn-004fc480)

~~~json
{
  "source": "004fc480",
  "target": "00c69f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c69f68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc480`](#insn-004fc480)

~~~json
{
  "source": "004fc480",
  "target": "00c69f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c69f70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc484`](#insn-004fc484)

~~~json
{
  "source": "004fc484",
  "target": "0053aa24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc484`](#insn-004fc484)

~~~json
{
  "source": "004fc484",
  "target": "0053aa28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc488`](#insn-004fc488)

~~~json
{
  "source": "004fc488",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc48c`](#insn-004fc48c)

~~~json
{
  "source": "004fc48c",
  "target": "004fbfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc490`](#insn-004fc490)

~~~json
{
  "source": "004fc490",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc494`](#insn-004fc494)

~~~json
{
  "source": "004fc494",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc498`](#insn-004fc498)

~~~json
{
  "source": "004fc498",
  "target": "004fbfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4a4`](#insn-004fc4a4)

~~~json
{
  "source": "004fc4a4",
  "target": "00539edc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc4a8`](#insn-004fc4a8)

~~~json
{
  "source": "004fc4a8",
  "target": "004fc4ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4b4`](#insn-004fc4b4)

~~~json
{
  "source": "004fc4b4",
  "target": "004fc4e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4bc`](#insn-004fc4bc)

~~~json
{
  "source": "004fc4bc",
  "target": "004fc4cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4c8`](#insn-004fc4c8)

~~~json
{
  "source": "004fc4c8",
  "target": "004fc4e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4d0`](#insn-004fc4d0)

~~~json
{
  "source": "004fc4d0",
  "target": "004fc4c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4d8`](#insn-004fc4d8)

~~~json
{
  "source": "004fc4d8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc4dc`](#insn-004fc4dc)

~~~json
{
  "source": "004fc4dc",
  "target": "004fc4c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4e8`](#insn-004fc4e8)

~~~json
{
  "source": "004fc4e8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc4ec`](#insn-004fc4ec)

~~~json
{
  "source": "004fc4ec",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4f0`](#insn-004fc4f0)

~~~json
{
  "source": "004fc4f0",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc530`](#insn-004fc530)

~~~json
{
  "source": "004fc530",
  "target": "00545bfc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc534`](#insn-004fc534)

~~~json
{
  "source": "004fc534",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc53c`](#insn-004fc53c)

~~~json
{
  "source": "004fc53c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc544`](#insn-004fc544)

~~~json
{
  "source": "004fc544",
  "target": "004fc698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc54c`](#insn-004fc54c)

~~~json
{
  "source": "004fc54c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc550`](#insn-004fc550)

~~~json
{
  "source": "004fc550",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc554`](#insn-004fc554)

~~~json
{
  "source": "004fc554",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc558`](#insn-004fc558)

~~~json
{
  "source": "004fc558",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc55c`](#insn-004fc55c)

~~~json
{
  "source": "004fc55c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc560`](#insn-004fc560)

~~~json
{
  "source": "004fc560",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc568`](#insn-004fc568)

~~~json
{
  "source": "004fc568",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc570`](#insn-004fc570)

~~~json
{
  "source": "004fc570",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc578`](#insn-004fc578)

~~~json
{
  "source": "004fc578",
  "target": "004fc698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc580`](#insn-004fc580)

~~~json
{
  "source": "004fc580",
  "target": "0043b724",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc584`](#insn-004fc584)

~~~json
{
  "source": "004fc584",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc58c`](#insn-004fc58c)

~~~json
{
  "source": "004fc58c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc594`](#insn-004fc594)

~~~json
{
  "source": "004fc594",
  "target": "004fc698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5a0`](#insn-004fc5a0)

~~~json
{
  "source": "004fc5a0",
  "target": "0043b724",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc5a4`](#insn-004fc5a4)

~~~json
{
  "source": "004fc5a4",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5ac`](#insn-004fc5ac)

~~~json
{
  "source": "004fc5ac",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5b4`](#insn-004fc5b4)

~~~json
{
  "source": "004fc5b4",
  "target": "004fc698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5b8`](#insn-004fc5b8)

~~~json
{
  "source": "004fc5b8",
  "target": "00459d34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc698`](#insn-004fc698)

~~~json
{
  "source": "004fc698",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
