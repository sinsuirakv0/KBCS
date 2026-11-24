# 004fbefc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004fbebc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0010.md#compare-449dce8d90438f72ea9e96ec4ac1493a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004fbf3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fb/004fbf3c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0010.md#compare-408804c0f754911fd1bf25a02a8bf971)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004fbefc",
  "name": "_ZN5Botan19get_files_recursiveERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 1796,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f9e9de2d44bf01f6718453cc84ddc68510583dd41754b66438c552942deb56c",
  "source_text_sha256": "0f9e9de2d44bf01f6718453cc84ddc68510583dd41754b66438c552942deb56c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004fbefc",
        "004fc5fb"
      ],
      [
        "004fc6d8",
        "004fc6db"
      ]
    ],
    "bytes_sha256": "56172af25ac9419b70b1d76e866334d6148ae86da2187466a3009534fad32b5d",
    "instruction_count": 449,
    "instruction_bytes": 1796,
    "body_bytes": 1796,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59830](../00c59/00c59830.md)

## 呼び出し先

- [0043b764](../0043b/0043b764.md)
- [0043bb20](../0043b/0043bb20.md)
- [00459d74](../00459/00459d74.md)
- [00539f1c](../00539/00539f1c.md)
- [0053a0b4](../0053a/0053a0b4.md)
- [0053aa64](../0053a/0053aa64.md)
- [0053aa68](../0053a/0053aa68.md)
- [0053aa6c](../0053a/0053aa6c.md)
- [00540d7c](../00540/00540d7c.md)
- [00545c3c](../00545/00545c3c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c59840](../00c59/00c59840.md)
- [00c59850](../00c59/00c59850.md)
- [00c59860](../00c59/00c59860.md)

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
  FUN_0053a0b4(&local_f0);
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
    FUN_0043bb20(puVar9,*(undefined8 *)(param_2 + 0x10),*(undefined8 *)(param_2 + 8));
  }
  bVar7 = local_c8 == -1;
  local_c8 = local_c8 + 1;
  if (bVar7) {
    FUN_00539f1c(&local_f0);
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
        FUN_0043bb20(&local_110,puVar18[2],puVar18[1]);
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
      local_b0 = &PTR_FUN_00c6a348;
      local_a8 = PTR_closedir_00c9b0c0;
      local_90 = &local_b0;
      if (local_c0 == (DIR *)0x0) {
LAB_004fc4b4:
        lVar14 = 0x20;
        pppuVar13 = &local_b0;
LAB_004fc4bc:
        (**(code **)((long)*pppuVar13 + lVar14))();
      }
      else {
        while (pdVar10 = readdir(local_c0), pDVar6 = local_c0, pdVar10 != (dirent *)0x0) {
          sVar11 = strlen(pdVar10->d_name);
          if (0xfffffffffffffff7 < sVar11) {
            if (*(long *)(lVar4 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
              FUN_0043b764(&local_128);
            }
            goto LAB_004fc6d8;
          }
          if (sVar11 < 0x17) {
            local_128 = CONCAT71(local_128._1_7_,(char)((int)sVar11 << 1));
            psVar12 = psVar21;
            if (sVar11 != 0) goto LAB_004fc1b0;
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
LAB_004fc1b0:
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
            if (*psVar12 != 0x2e2e) goto LAB_004fc220;
          }
          else {
            if (sVar11 == 1) {
              psVar12 = psVar21;
              if ((local_128 & 1) != 0) {
                psVar12 = local_118;
              }
              if ((char)*psVar12 == '.') goto LAB_004fc440;
            }
LAB_004fc220:
            __n = local_110 >> 1 & 0x7f;
            if ((local_110 & 1) != 0) {
              __n = sStack_108;
            }
            uVar1 = __n + 1;
            if (0xfffffffffffffff7 < uVar1) {
              if (*(long *)(lVar4 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
                FUN_0043b764(&local_1c0);
              }
              goto LAB_004fc6d8;
            }
            if (uVar1 < 0x17) {
              local_1c0.st_ino = 0;
              local_1c0.st_nlink = 0;
              local_1c0.st_dev = (__dev_t)(byte)((int)uVar1 << 1);
              __dest = (void *)((ulong)&local_1c0 | 1);
              if (__n != 0) goto LAB_004fc298;
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
LAB_004fc298:
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
                    FUN_0043bb20(local_1d0,local_130,local_1c0.__unused[2]);
                    local_1d0 = puVar18 + 3;
                  }
                }
                else {
                  local_1d0 = (ulong *)FUN_00540d7c(&local_1d8,local_1c0.__unused + 1);
                }
              }
              else if (((uint)local_1c0.st_nlink & 0xf000) == 0x4000) {
                lVar14 = 0;
                if ((long)local_e0 - (long)puStack_e8 != 0) {
                  lVar14 = ((long)local_e0 - (long)puStack_e8 >> 3) * 0xaa + -1;
                }
                if (lVar14 == local_c8 + local_d0) {
                  FUN_0053a0b4(&local_f0);
                }
                if (local_e0 == puStack_e8) {
                  puVar18 = (ulong *)0x0;
                  if ((local_1c0.__unused[1] & 1U) != 0) goto LAB_004fc414;
LAB_004fc3b0:
                  puVar18[2] = (ulong)local_130;
                  puVar18[1] = local_1c0.__unused[2];
                  *puVar18 = local_1c0.__unused[1];
                }
                else {
                  puVar18 = (ulong *)(puStack_e8[(local_c8 + local_d0) / 0xaa] +
                                     ((local_c8 + local_d0) % 0xaa) * 0x18);
                  if ((local_1c0.__unused[1] & 1U) == 0) goto LAB_004fc3b0;
LAB_004fc414:
                  FUN_0043bb20(puVar18,local_130,local_1c0.__unused[2]);
                }
                local_c8 = local_c8 + 1;
              }
            }
            if ((local_1c0.__unused[1] & 1U) != 0) {
              _ZdlPv(local_130);
            }
            bVar20 = (byte)local_128 & 1;
          }
LAB_004fc440:
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
              FUN_00459d74();
            }
            goto LAB_004fc6d8;
          }
          (*(code *)(*local_90)[6])(local_90,&local_1c0);
        }
        if (local_90 == &local_b0) goto LAB_004fc4b4;
        if (local_90 != (undefined ***)0x0) {
          lVar14 = 0x28;
          pppuVar13 = local_90;
          goto LAB_004fc4bc;
        }
      }
      if ((local_110 & 1) != 0) {
        _ZdlPv(local_100);
      }
    } while (local_c8 != 0);
    pbVar16 = (byte *)*param_1;
    FUN_00539f1c(&local_f0);
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
  FUN_00545c3c(local_1d8,local_1d0,&local_1c0,lVar14,1);
  if (*(long *)(lVar4 + 0x28) == local_78) {
    return;
  }
LAB_004fc6d8:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004fbefc"></a> `004fbefc` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-004fbf00"></a> `004fbf00` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fbf04"></a> `004fbf04` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fbf08"></a> `004fbf08` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fbf0c"></a> `004fbf0c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fbf10"></a> `004fbf10` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fbf14"></a> `004fbf14` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004fbf18"></a> `004fbf18` | `ff 83 06 d1` | sub sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-004fbf1c"></a> `004fbf1c` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-004fbf20"></a> `004fbf20` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004fbf24"></a> `004fbf24` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004fbf28"></a> `004fbf28` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fbf2c"></a> `004fbf2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004fbf30"></a> `004fbf30` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fbf34"></a> `004fbf34` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fbf38"></a> `004fbf38` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fbf3c"></a> `004fbf3c` | `3f 7f 00 a9` | stp xzr,xzr,[x25] | `FALL_THROUGH`
<a id="insn-004fbf40"></a> `004fbf40` | `3f 0b 00 f9` | str xzr,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-004fbf44"></a> `004fbf44` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fbf48"></a> `004fbf48` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004fbf4c"></a> `004fbf4c` | `00 01 03 ad` | stp q0,q0,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-004fbf50"></a> `004fbf50` | `00 15 80 3d` | str q0,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-004fbf54"></a> `004fbf54` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fbf58"></a> `004fbf58` | `57 f8 00 94` | bl 0x0053a0b4 | `UNCONDITIONAL_CALL`
<a id="insn-004fbf5c"></a> `004fbf5c` | `a8 a7 77 a9` | ldp x8,x9,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fbf60"></a> `004fbf60` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-004fbf64"></a> `004fbf64` | `80 02 00 54` | b.eq 0x004fbfb4 | `CONDITIONAL_JUMP`
<a id="insn-004fbf68"></a> `004fbf68` | `a9 2b 79 a9` | ldp x9,x10,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fbf6c"></a> `004fbf6c` | `4b 15 80 52` | mov w11,#0xaa | `FALL_THROUGH`
<a id="insn-004fbf70"></a> `004fbf70` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-004fbf74"></a> `004fbf74` | `ea c7 02 b2` | orr x10,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fbf78"></a> `004fbf78` | `2a 18 98 f2` | movk x10,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fbf7c"></a> `004fbf7c` | `2a 7d ca 9b` | umulh x10,x9,x10 | `FALL_THROUGH`
<a id="insn-004fbf80"></a> `004fbf80` | `4a fd 47 d3` | lsr x10,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004fbf84"></a> `004fbf84` | `49 a5 0b 9b` | msub x9,x10,x11,x9 | `FALL_THROUGH`
<a id="insn-004fbf88"></a> `004fbf88` | `0b 03 80 52` | mov w11,#0x18 | `FALL_THROUGH`
<a id="insn-004fbf8c"></a> `004fbf8c` | `08 79 6a f8` | ldr x8,[x8, x10, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fbf90"></a> `004fbf90` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004fbf94"></a> `004fbf94` | `20 21 0b 9b` | madd x0,x9,x11,x8 | `FALL_THROUGH`
<a id="insn-004fbf98"></a> `004fbf98` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-004fbf9c"></a> `004fbf9c` | `28 01 00 37` | tbnz w8,#0x0,0x004fbfc0 | `CONDITIONAL_JUMP`
<a id="insn-004fbfa0"></a> `004fbfa0` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004fbfa4"></a> `004fbfa4` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-004fbfa8"></a> `004fbfa8` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fbfac"></a> `004fbfac` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-004fbfb0"></a> `004fbfb0` | `06 00 00 14` | b 0x004fbfc8 | `UNCONDITIONAL_JUMP`
<a id="insn-004fbfb4"></a> `004fbfb4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-004fbfb8"></a> `004fbfb8` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-004fbfbc"></a> `004fbfbc` | `28 ff 07 36` | tbz w8,#0x0,0x004fbfa0 | `CONDITIONAL_JUMP`
<a id="insn-004fbfc0"></a> `004fbfc0` | `82 86 40 a9` | ldp x2,x1,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004fbfc4"></a> `004fbfc4` | `d7 fe fc 97` | bl 0x0043bb20 | `UNCONDITIONAL_CALL`
<a id="insn-004fbfc8"></a> `004fbfc8` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fbfcc"></a> `004fbfcc` | `08 05 00 b1` | adds x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fbfd0"></a> `004fbfd0` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fbfd4"></a> `004fbfd4` | `83 00 00 54` | b.cc 0x004fbfe4 | `CONDITIONAL_JUMP`
<a id="insn-004fbfd8"></a> `004fbfd8` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fbfdc"></a> `004fbfdc` | `d0 f7 00 94` | bl 0x00539f1c | `UNCONDITIONAL_CALL`
<a id="insn-004fbfe0"></a> `004fbfe0` | `53 01 00 14` | b 0x004fc52c | `UNCONDITIONAL_JUMP`
<a id="insn-004fbfe4"></a> `004fbfe4` | `a8 c3 02 d1` | sub x8,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-004fbfe8"></a> `004fbfe8` | `a9 83 01 d1` | sub x9,x29,#0x60 | `FALL_THROUGH`
<a id="insn-004fbfec"></a> `004fbfec` | `aa 23 03 d1` | sub x10,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-004fbff0"></a> `004fbff0` | `08 01 40 b2` | orr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fbff4"></a> `004fbff4` | `eb 03 01 91` | add x11,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fbff8"></a> `004fbff8` | `5c 01 40 b2` | orr x28,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004fbffc"></a> `004fbffc` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fc000"></a> `004fc000` | `28 41 00 91` | add x8,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004fc004"></a> `004fc004` | `69 01 40 b2` | orr x9,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004fc008"></a> `004fc008` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fc00c"></a> `004fc00c` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc010"></a> `004fc010` | `13 01 40 b2` | orr x19,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc014"></a> `004fc014` | `e9 0f 00 f9` | str x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fc018"></a> `004fc018` | `03 00 00 14` | b 0x004fc024 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc01c"></a> `004fc01c` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fc020"></a> `004fc020` | `e8 25 00 b4` | cbz x8,0x004fc4dc | `CONDITIONAL_JUMP`
<a id="insn-004fc024"></a> `004fc024` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc028"></a> `004fc028` | `e9 c7 02 b2` | orr x9,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fc02c"></a> `004fc02c` | `4b 15 80 52` | mov w11,#0xaa | `FALL_THROUGH`
<a id="insn-004fc030"></a> `004fc030` | `29 18 98 f2` | movk x9,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fc034"></a> `004fc034` | `aa 83 57 f8` | ldur x10,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc038"></a> `004fc038` | `0d 03 80 52` | mov w13,#0x18 | `FALL_THROUGH`
<a id="insn-004fc03c"></a> `004fc03c` | `09 7d c9 9b` | umulh x9,x8,x9 | `FALL_THROUGH`
<a id="insn-004fc040"></a> `004fc040` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-004fc044"></a> `004fc044` | `2b a1 0b 9b` | msub x11,x9,x11,x8 | `FALL_THROUGH`
<a id="insn-004fc048"></a> `004fc048` | `4c 79 69 f8` | ldr x12,[x10, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fc04c"></a> `004fc04c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004fc050"></a> `004fc050` | `6c 31 0d 9b` | madd x12,x11,x13,x12 | `FALL_THROUGH`
<a id="insn-004fc054"></a> `004fc054` | `8d 01 40 39` | ldrb w13,[x12] | `FALL_THROUGH`
<a id="insn-004fc058"></a> `004fc058` | `ed 00 00 37` | tbnz w13,#0x0,0x004fc074 | `CONDITIONAL_JUMP`
<a id="insn-004fc05c"></a> `004fc05c` | `8d 09 40 f9` | ldr x13,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-004fc060"></a> `004fc060` | `80 01 c0 3d` | ldr q0,[x12] | `FALL_THROUGH`
<a id="insn-004fc064"></a> `004fc064` | `ec 03 03 91` | add x12,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc068"></a> `004fc068` | `ad 03 16 f8` | stur x13,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc06c"></a> `004fc06c` | `80 0d 80 3d` | str q0,[x12, #0x30] | `FALL_THROUGH`
<a id="insn-004fc070"></a> `004fc070` | `0c 00 00 14` | b 0x004fc0a0 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc074"></a> `004fc074` | `82 85 40 a9` | ldp x2,x1,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-004fc078"></a> `004fc078` | `a0 c3 02 d1` | sub x0,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-004fc07c"></a> `004fc07c` | `a9 fe fc 97` | bl 0x0043bb20 | `UNCONDITIONAL_CALL`
<a id="insn-004fc080"></a> `004fc080` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc084"></a> `004fc084` | `e9 c7 02 b2` | orr x9,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fc088"></a> `004fc088` | `4a 15 80 52` | mov w10,#0xaa | `FALL_THROUGH`
<a id="insn-004fc08c"></a> `004fc08c` | `29 18 98 f2` | movk x9,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fc090"></a> `004fc090` | `09 7d c9 9b` | umulh x9,x8,x9 | `FALL_THROUGH`
<a id="insn-004fc094"></a> `004fc094` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-004fc098"></a> `004fc098` | `2b a1 0a 9b` | msub x11,x9,x10,x8 | `FALL_THROUGH`
<a id="insn-004fc09c"></a> `004fc09c` | `aa 83 57 f8` | ldur x10,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc0a0"></a> `004fc0a0` | `49 79 69 f8` | ldr x9,[x10, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fc0a4"></a> `004fc0a4` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-004fc0a8"></a> `004fc0a8` | `69 25 0a 9b` | madd x9,x11,x10,x9 | `FALL_THROUGH`
<a id="insn-004fc0ac"></a> `004fc0ac` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-004fc0b0"></a> `004fc0b0` | `8a 00 00 36` | tbz w10,#0x0,0x004fc0c0 | `CONDITIONAL_JUMP`
<a id="insn-004fc0b4"></a> `004fc0b4` | `20 09 40 f9` | ldr x0,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-004fc0b8"></a> `004fc0b8` | `7e 6f 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc0bc"></a> `004fc0bc` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc0c0"></a> `004fc0c0` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fc0c4"></a> `004fc0c4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc0c8"></a> `004fc0c8` | `1f 51 05 f1` | cmp x8,#0x154 | `FALL_THROUGH`
<a id="insn-004fc0cc"></a> `004fc0cc` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004fc0d0"></a> `004fc0d0` | `a8 27 39 a9` | stp x8,x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc0d4"></a> `004fc0d4` | `43 01 00 54` | b.cc 0x004fc0fc | `CONDITIONAL_JUMP`
<a id="insn-004fc0d8"></a> `004fc0d8` | `a8 83 57 f8` | ldur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc0dc"></a> `004fc0dc` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-004fc0e0"></a> `004fc0e0` | `74 6f 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc0e4"></a> `004fc0e4` | `a8 83 57 f8` | ldur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc0e8"></a> `004fc0e8` | `a9 03 59 f8` | ldur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc0ec"></a> `004fc0ec` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004fc0f0"></a> `004fc0f0` | `29 a9 02 d1` | sub x9,x9,#0xaa | `FALL_THROUGH`
<a id="insn-004fc0f4"></a> `004fc0f4` | `a8 83 17 f8` | stur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc0f8"></a> `004fc0f8` | `a9 03 19 f8` | stur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc0fc"></a> `004fc0fc` | `a8 03 55 38` | ldurb w8,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-004fc100"></a> `004fc100` | `a9 03 56 f8` | ldur x9,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc104"></a> `004fc104` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc108"></a> `004fc108` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fc10c"></a> `004fc10c` | `00 01 89 9a` | csel x0,x8,x9,eq | `FALL_THROUGH`
<a id="insn-004fc110"></a> `004fc110` | `cc 75 1d 94` | bl 0x00c59840 | `UNCONDITIONAL_CALL`
<a id="insn-004fc114"></a> `004fc114` | `68 3b 00 d0` | adrp x8,0xc6a000 | `FALL_THROUGH`
<a id="insn-004fc118"></a> `004fc118` | `08 21 0d 91` | add x8,x8,#0x348 | `FALL_THROUGH`
<a id="insn-004fc11c"></a> `004fc11c` | `a0 03 1a f8` | stur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc120"></a> `004fc120` | `a8 03 1b f8` | stur x8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004fc124"></a> `004fc124` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fc128"></a> `004fc128` | `e9 3c 00 f0` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-004fc12c"></a> `004fc12c` | `a8 03 1d f8` | stur x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fc130"></a> `004fc130` | `29 61 40 f9` | ldr x9,[x9, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc134"></a> `004fc134` | `a9 83 1b f8` | stur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-004fc138"></a> `004fc138` | `60 00 00 b5` | cbnz x0,0x004fc144 | `CONDITIONAL_JUMP`
<a id="insn-004fc13c"></a> `004fc13c` | `de 00 00 14` | b 0x004fc4b4 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc140"></a> `004fc140` | `a0 03 5a f8` | ldur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc144"></a> `004fc144` | `c3 75 1d 94` | bl 0x00c59850 | `UNCONDITIONAL_CALL`
<a id="insn-004fc148"></a> `004fc148` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004fc14c"></a> `004fc14c` | `20 19 00 b4` | cbz x0,0x004fc470 | `CONDITIONAL_JUMP`
<a id="insn-004fc150"></a> `004fc150` | `80 4e 00 91` | add x0,x20,#0x13 | `FALL_THROUGH`
<a id="insn-004fc154"></a> `004fc154` | `a3 6f 1d 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc158"></a> `004fc158` | `1f 20 00 b1` | cmn x0,#0x8 | `FALL_THROUGH`
<a id="insn-004fc15c"></a> `004fc15c` | `62 22 00 54` | b.cs 0x004fc5a8 | `CONDITIONAL_JUMP`
<a id="insn-004fc160"></a> `004fc160` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004fc164"></a> `004fc164` | `1f 5c 00 f1` | cmp x0,#0x17 | `FALL_THROUGH`
<a id="insn-004fc168"></a> `004fc168` | `c2 00 00 54` | b.cs 0x004fc180 | `CONDITIONAL_JUMP`
<a id="insn-004fc16c"></a> `004fc16c` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-004fc170"></a> `004fc170` | `f6 03 1c aa` | mov x22,x28 | `FALL_THROUGH`
<a id="insn-004fc174"></a> `004fc174` | `a8 83 13 38` | sturb w8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc178"></a> `004fc178` | `d5 01 00 b5` | cbnz x21,0x004fc1b0 | `CONDITIONAL_JUMP`
<a id="insn-004fc17c"></a> `004fc17c` | `11 00 00 14` | b 0x004fc1c0 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc180"></a> `004fc180` | `a8 f2 7d 92` | and x8,x21,#-0x8 | `FALL_THROUGH`
<a id="insn-004fc184"></a> `004fc184` | `a9 0a 40 b2` | orr x9,x21,#0x7 | `FALL_THROUGH`
<a id="insn-004fc188"></a> `004fc188` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004fc18c"></a> `004fc18c` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-004fc190"></a> `004fc190` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-004fc194"></a> `004fc194` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc198"></a> `004fc198` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004fc19c"></a> `004fc19c` | `3d 6f 1d 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-004fc1a0"></a> `004fc1a0` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1a4"></a> `004fc1a4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-004fc1a8"></a> `004fc1a8` | `b5 03 34 a9` | stp x21,x0,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-004fc1ac"></a> `004fc1ac` | `a8 83 13 f8` | stur x8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc1b0"></a> `004fc1b0` | `81 4e 00 91` | add x1,x20,#0x13 | `FALL_THROUGH`
<a id="insn-004fc1b4"></a> `004fc1b4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004fc1b8"></a> `004fc1b8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004fc1bc"></a> `004fc1bc` | `61 6f 1d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-004fc1c0"></a> `004fc1c0` | `df 6a 35 38` | strb wzr,[x22, x21, LSL ] | `FALL_THROUGH`
<a id="insn-004fc1c4"></a> `004fc1c4` | `a8 83 53 38` | ldurb w8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc1c8"></a> `004fc1c8` | `a9 03 54 f8` | ldur x9,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-004fc1cc"></a> `004fc1cc` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1d0"></a> `004fc1d0` | `18 01 00 72` | ands w24,w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1d4"></a> `004fc1d4` | `54 01 89 9a` | csel x20,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004fc1d8"></a> `004fc1d8` | `9f 0a 00 f1` | cmp x20,#0x2 | `FALL_THROUGH`
<a id="insn-004fc1dc"></a> `004fc1dc` | `40 01 00 54` | b.eq 0x004fc204 | `CONDITIONAL_JUMP`
<a id="insn-004fc1e0"></a> `004fc1e0` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-004fc1e4"></a> `004fc1e4` | `e1 01 00 54` | b.ne 0x004fc220 | `CONDITIONAL_JUMP`
<a id="insn-004fc1e8"></a> `004fc1e8` | `a8 83 54 f8` | ldur x8,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc1ec"></a> `004fc1ec` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-004fc1f0"></a> `004fc1f0` | `88 03 88 9a` | csel x8,x28,x8,eq | `FALL_THROUGH`
<a id="insn-004fc1f4"></a> `004fc1f4` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-004fc1f8"></a> `004fc1f8` | `1f b9 00 71` | cmp w8,#0x2e | `FALL_THROUGH`
<a id="insn-004fc1fc"></a> `004fc1fc` | `21 01 00 54` | b.ne 0x004fc220 | `CONDITIONAL_JUMP`
<a id="insn-004fc200"></a> `004fc200` | `90 00 00 14` | b 0x004fc440 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc204"></a> `004fc204` | `a8 83 54 f8` | ldur x8,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc208"></a> `004fc208` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-004fc20c"></a> `004fc20c` | `c9 c5 85 52` | mov w9,#0x2e2e | `FALL_THROUGH`
<a id="insn-004fc210"></a> `004fc210` | `88 03 88 9a` | csel x8,x28,x8,eq | `FALL_THROUGH`
<a id="insn-004fc214"></a> `004fc214` | `08 01 40 79` | ldrh w8,[x8] | `FALL_THROUGH`
<a id="insn-004fc218"></a> `004fc218` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-004fc21c"></a> `004fc21c` | `20 11 00 54` | b.eq 0x004fc440 | `CONDITIONAL_JUMP`
<a id="insn-004fc220"></a> `004fc220` | `bb 03 55 38` | ldurb w27,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-004fc224"></a> `004fc224` | `a8 83 55 f8` | ldur x8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-004fc228"></a> `004fc228` | `fa 03 19 aa` | mov x26,x25 | `FALL_THROUGH`
<a id="insn-004fc22c"></a> `004fc22c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-004fc230"></a> `004fc230` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-004fc234"></a> `004fc234` | `35 01 88 9a` | csel x21,x9,x8,eq | `FALL_THROUGH`
<a id="insn-004fc238"></a> `004fc238` | `b9 06 00 91` | add x25,x21,#0x1 | `FALL_THROUGH`
<a id="insn-004fc23c"></a> `004fc23c` | `3f 23 00 b1` | cmn x25,#0x8 | `FALL_THROUGH`
<a id="insn-004fc240"></a> `004fc240` | `22 1c 00 54` | b.cs 0x004fc5c4 | `CONDITIONAL_JUMP`
<a id="insn-004fc244"></a> `004fc244` | `3f 5f 00 f1` | cmp x25,#0x17 | `FALL_THROUGH`
<a id="insn-004fc248"></a> `004fc248` | `02 01 00 54` | b.cs 0x004fc268 | `CONDITIONAL_JUMP`
<a id="insn-004fc24c"></a> `004fc24c` | `28 7b 1f 53` | lsl w8,w25,#0x1 | `FALL_THROUGH`
<a id="insn-004fc250"></a> `004fc250` | `f6 0f 40 f9` | ldr x22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fc254"></a> `004fc254` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc258"></a> `004fc258` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc25c"></a> `004fc25c` | `e8 03 01 39` | strb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc260"></a> `004fc260` | `d5 01 00 b5` | cbnz x21,0x004fc298 | `CONDITIONAL_JUMP`
<a id="insn-004fc264"></a> `004fc264` | `14 00 00 14` | b 0x004fc2b4 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc268"></a> `004fc268` | `28 f3 7d 92` | and x8,x25,#-0x8 | `FALL_THROUGH`
<a id="insn-004fc26c"></a> `004fc26c` | `29 0b 40 b2` | orr x9,x25,#0x7 | `FALL_THROUGH`
<a id="insn-004fc270"></a> `004fc270` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-004fc274"></a> `004fc274` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-004fc278"></a> `004fc278` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-004fc27c"></a> `004fc27c` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc280"></a> `004fc280` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004fc284"></a> `004fc284` | `03 6f 1d 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-004fc288"></a> `004fc288` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-004fc28c"></a> `004fc28c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-004fc290"></a> `004fc290` | `f9 83 04 a9` | stp x25,x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004fc294"></a> `004fc294` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc298"></a> `004fc298` | `a8 03 56 f8` | ldur x8,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc29c"></a> `004fc29c` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fc2a0"></a> `004fc2a0` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-004fc2a4"></a> `004fc2a4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004fc2a8"></a> `004fc2a8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004fc2ac"></a> `004fc2ac` | `21 01 88 9a` | csel x1,x9,x8,eq | `FALL_THROUGH`
<a id="insn-004fc2b0"></a> `004fc2b0` | `24 6f 1d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-004fc2b4"></a> `004fc2b4` | `a8 83 54 f8` | ldur x8,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc2b8"></a> `004fc2b8` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-004fc2bc"></a> `004fc2bc` | `e9 05 80 52` | mov w9,#0x2f | `FALL_THROUGH`
<a id="insn-004fc2c0"></a> `004fc2c0` | `c9 6a 35 78` | strh w9,[x22, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004fc2c4"></a> `004fc2c4` | `81 03 88 9a` | csel x1,x28,x8,eq | `FALL_THROUGH`
<a id="insn-004fc2c8"></a> `004fc2c8` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc2cc"></a> `004fc2cc` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-004fc2d0"></a> `004fc2d0` | `2c 6f 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004fc2d4"></a> `004fc2d4` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fc2d8"></a> `004fc2d8` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004fc2dc"></a> `004fc2dc` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-004fc2e0"></a> `004fc2e0` | `e8 6b 00 f9` | str x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc2e4"></a> `004fc2e4` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc2e8"></a> `004fc2e8` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-004fc2ec"></a> `004fc2ec` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004fc2f0"></a> `004fc2f0` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004fc2f4"></a> `004fc2f4` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc2f8"></a> `004fc2f8` | `68 00 00 36` | tbz w8,#0x0,0x004fc304 | `CONDITIONAL_JUMP`
<a id="insn-004fc2fc"></a> `004fc2fc` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc300"></a> `004fc300` | `ec 6e 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc304"></a> `004fc304` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc308"></a> `004fc308` | `e9 6b 40 f9` | ldr x9,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc30c"></a> `004fc30c` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc310"></a> `004fc310` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc314"></a> `004fc314` | `60 02 89 9a` | csel x0,x19,x9,eq | `FALL_THROUGH`
<a id="insn-004fc318"></a> `004fc318` | `52 75 1d 94` | bl 0x00c59860 | `UNCONDITIONAL_CALL`
<a id="insn-004fc31c"></a> `004fc31c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-004fc320"></a> `004fc320` | `40 08 00 54` | b.eq 0x004fc428 | `CONDITIONAL_JUMP`
<a id="insn-004fc324"></a> `004fc324` | `e8 53 40 b9` | ldr w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc328"></a> `004fc328` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-004fc32c"></a> `004fc32c` | `1f 21 40 71` | cmp w8,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-004fc330"></a> `004fc330` | `c0 04 00 54` | b.eq 0x004fc3c8 | `CONDITIONAL_JUMP`
<a id="insn-004fc334"></a> `004fc334` | `1f 11 40 71` | cmp w8,#0x4, LSL #12 | `FALL_THROUGH`
<a id="insn-004fc338"></a> `004fc338` | `81 07 00 54` | b.ne 0x004fc428 | `CONDITIONAL_JUMP`
<a id="insn-004fc33c"></a> `004fc33c` | `a8 a7 77 a9` | ldp x8,x9,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc340"></a> `004fc340` | `4c 15 80 52` | mov w12,#0xaa | `FALL_THROUGH`
<a id="insn-004fc344"></a> `004fc344` | `0b 00 80 92` | mov x11,#-0x1 | `FALL_THROUGH`
<a id="insn-004fc348"></a> `004fc348` | `2a 01 08 eb` | subs x10,x9,x8 | `FALL_THROUGH`
<a id="insn-004fc34c"></a> `004fc34c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-004fc350"></a> `004fc350` | `4a 2d 0c 9b` | madd x10,x10,x12,x11 | `FALL_THROUGH`
<a id="insn-004fc354"></a> `004fc354` | `ab 33 79 a9` | ldp x11,x12,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc358"></a> `004fc358` | `8b 01 0b 8b` | add x11,x12,x11 | `FALL_THROUGH`
<a id="insn-004fc35c"></a> `004fc35c` | `ea 03 8a 9a` | csel x10,xzr,x10,eq | `FALL_THROUGH`
<a id="insn-004fc360"></a> `004fc360` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-004fc364"></a> `004fc364` | `81 00 00 54` | b.ne 0x004fc374 | `CONDITIONAL_JUMP`
<a id="insn-004fc368"></a> `004fc368` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fc36c"></a> `004fc36c` | `52 f7 00 94` | bl 0x0053a0b4 | `UNCONDITIONAL_CALL`
<a id="insn-004fc370"></a> `004fc370` | `a8 a7 77 a9` | ldp x8,x9,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-004fc374"></a> `004fc374` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-004fc378"></a> `004fc378` | `80 04 00 54` | b.eq 0x004fc408 | `CONDITIONAL_JUMP`
<a id="insn-004fc37c"></a> `004fc37c` | `a9 2b 79 a9` | ldp x9,x10,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004fc380"></a> `004fc380` | `4b 15 80 52` | mov w11,#0xaa | `FALL_THROUGH`
<a id="insn-004fc384"></a> `004fc384` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-004fc388"></a> `004fc388` | `ea c7 02 b2` | orr x10,xzr,#-0x3f3f3f3f3f3f3f40 | `FALL_THROUGH`
<a id="insn-004fc38c"></a> `004fc38c` | `2a 18 98 f2` | movk x10,#0xc0c1 | `FALL_THROUGH`
<a id="insn-004fc390"></a> `004fc390` | `2a 7d ca 9b` | umulh x10,x9,x10 | `FALL_THROUGH`
<a id="insn-004fc394"></a> `004fc394` | `4a fd 47 d3` | lsr x10,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004fc398"></a> `004fc398` | `49 a5 0b 9b` | msub x9,x10,x11,x9 | `FALL_THROUGH`
<a id="insn-004fc39c"></a> `004fc39c` | `08 79 6a f8` | ldr x8,[x8, x10, LSL #0x3] | `FALL_THROUGH`
<a id="insn-004fc3a0"></a> `004fc3a0` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-004fc3a4"></a> `004fc3a4` | `20 21 0a 9b` | madd x0,x9,x10,x8 | `FALL_THROUGH`
<a id="insn-004fc3a8"></a> `004fc3a8` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc3ac"></a> `004fc3ac` | `48 03 00 37` | tbnz w8,#0x0,0x004fc414 | `CONDITIONAL_JUMP`
<a id="insn-004fc3b0"></a> `004fc3b0` | `e9 03 03 91` | add x9,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc3b4"></a> `004fc3b4` | `e8 6b 40 f9` | ldr x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc3b8"></a> `004fc3b8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-004fc3bc"></a> `004fc3bc` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fc3c0"></a> `004fc3c0` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-004fc3c4"></a> `004fc3c4` | `16 00 00 14` | b 0x004fc41c | `UNCONDITIONAL_JUMP`
<a id="insn-004fc3c8"></a> `004fc3c8` | `f5 23 43 a9` | ldp x21,x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc3cc"></a> `004fc3cc` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-004fc3d0"></a> `004fc3d0` | `42 01 00 54` | b.cs 0x004fc3f8 | `CONDITIONAL_JUMP`
<a id="insn-004fc3d4"></a> `004fc3d4` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc3d8"></a> `004fc3d8` | `c8 03 00 37` | tbnz w8,#0x0,0x004fc450 | `CONDITIONAL_JUMP`
<a id="insn-004fc3dc"></a> `004fc3dc` | `e9 03 03 91` | add x9,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc3e0"></a> `004fc3e0` | `e8 6b 40 f9` | ldr x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc3e4"></a> `004fc3e4` | `a0 62 00 91` | add x0,x21,#0x18 | `FALL_THROUGH`
<a id="insn-004fc3e8"></a> `004fc3e8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-004fc3ec"></a> `004fc3ec` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-004fc3f0"></a> `004fc3f0` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-004fc3f4"></a> `004fc3f4` | `1b 00 00 14` | b 0x004fc460 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc3f8"></a> `004fc3f8` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004fc3fc"></a> `004fc3fc` | `e1 03 03 91` | add x1,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004fc400"></a> `004fc400` | `5f 12 01 94` | bl 0x00540d7c | `UNCONDITIONAL_CALL`
<a id="insn-004fc404"></a> `004fc404` | `17 00 00 14` | b 0x004fc460 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc408"></a> `004fc408` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-004fc40c"></a> `004fc40c` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc410"></a> `004fc410` | `08 fd 07 36` | tbz w8,#0x0,0x004fc3b0 | `CONDITIONAL_JUMP`
<a id="insn-004fc414"></a> `004fc414` | `e2 87 4c a9` | ldp x2,x1,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-004fc418"></a> `004fc418` | `c2 fd fc 97` | bl 0x0043bb20 | `UNCONDITIONAL_CALL`
<a id="insn-004fc41c"></a> `004fc41c` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fc420"></a> `004fc420` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc424"></a> `004fc424` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004fc428"></a> `004fc428` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc42c"></a> `004fc42c` | `68 00 00 36` | tbz w8,#0x0,0x004fc438 | `CONDITIONAL_JUMP`
<a id="insn-004fc430"></a> `004fc430` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004fc434"></a> `004fc434` | `9f 6e 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc438"></a> `004fc438` | `a8 83 53 38` | ldurb w8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-004fc43c"></a> `004fc43c` | `18 01 00 12` | and w24,w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fc440"></a> `004fc440` | `18 e8 ff 34` | cbz w24,0x004fc140 | `CONDITIONAL_JUMP`
<a id="insn-004fc444"></a> `004fc444` | `a0 83 54 f8` | ldur x0,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-004fc448"></a> `004fc448` | `9a 6e 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc44c"></a> `004fc44c` | `3d ff ff 17` | b 0x004fc140 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc450"></a> `004fc450` | `e2 87 4c a9` | ldp x2,x1,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-004fc454"></a> `004fc454` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004fc458"></a> `004fc458` | `b2 fd fc 97` | bl 0x0043bb20 | `UNCONDITIONAL_CALL`
<a id="insn-004fc45c"></a> `004fc45c` | `a0 62 00 91` | add x0,x21,#0x18 | `FALL_THROUGH`
<a id="insn-004fc460"></a> `004fc460` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc464"></a> `004fc464` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004fc468"></a> `004fc468` | `48 fe 07 37` | tbnz w8,#0x0,0x004fc430 | `CONDITIONAL_JUMP`
<a id="insn-004fc46c"></a> `004fc46c` | `f3 ff ff 17` | b 0x004fc438 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc470"></a> `004fc470` | `a8 03 5a f8` | ldur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc474"></a> `004fc474` | `bf 03 1a f8` | stur xzr,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-004fc478"></a> `004fc478` | `08 01 00 b4` | cbz x8,0x004fc498 | `CONDITIONAL_JUMP`
<a id="insn-004fc47c"></a> `004fc47c` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fc480"></a> `004fc480` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc484"></a> `004fc484` | `00 0b 00 b4` | cbz x0,0x004fc5e4 | `CONDITIONAL_JUMP`
<a id="insn-004fc488"></a> `004fc488` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004fc48c"></a> `004fc48c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-004fc490"></a> `004fc490` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc494"></a> `004fc494` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004fc498"></a> `004fc498` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fc49c"></a> `004fc49c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fc4a0"></a> `004fc4a0` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-004fc4a4"></a> `004fc4a4` | `80 00 00 54` | b.eq 0x004fc4b4 | `CONDITIONAL_JUMP`
<a id="insn-004fc4a8"></a> `004fc4a8` | `00 01 00 b4` | cbz x0,0x004fc4c8 | `CONDITIONAL_JUMP`
<a id="insn-004fc4ac"></a> `004fc4ac` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-004fc4b0"></a> `004fc4b0` | `03 00 00 14` | b 0x004fc4bc | `UNCONDITIONAL_JUMP`
<a id="insn-004fc4b4"></a> `004fc4b4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-004fc4b8"></a> `004fc4b8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-004fc4bc"></a> `004fc4bc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-004fc4c0"></a> `004fc4c0` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004fc4c4"></a> `004fc4c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004fc4c8"></a> `004fc4c8` | `a8 03 55 38` | ldurb w8,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-004fc4cc"></a> `004fc4cc` | `88 da 07 36` | tbz w8,#0x0,0x004fc01c | `CONDITIONAL_JUMP`
<a id="insn-004fc4d0"></a> `004fc4d0` | `a0 03 56 f8` | ldur x0,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-004fc4d4"></a> `004fc4d4` | `77 6e 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc4d8"></a> `004fc4d8` | `d1 fe ff 17` | b 0x004fc01c | `UNCONDITIONAL_JUMP`
<a id="insn-004fc4dc"></a> `004fc4dc` | `34 03 40 f9` | ldr x20,[x25] | `FALL_THROUGH`
<a id="insn-004fc4e0"></a> `004fc4e0` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-004fc4e4"></a> `004fc4e4` | `8e f6 00 94` | bl 0x00539f1c | `UNCONDITIONAL_CALL`
<a id="insn-004fc4e8"></a> `004fc4e8` | `34 02 00 b4` | cbz x20,0x004fc52c | `CONDITIONAL_JUMP`
<a id="insn-004fc4ec"></a> `004fc4ec` | `28 07 40 f9` | ldr x8,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-004fc4f0"></a> `004fc4f0` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-004fc4f4"></a> `004fc4f4` | `60 01 00 54` | b.eq 0x004fc520 | `CONDITIONAL_JUMP`
<a id="insn-004fc4f8"></a> `004fc4f8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004fc4fc"></a> `004fc4fc` | `04 00 00 14` | b 0x004fc50c | `UNCONDITIONAL_JUMP`
<a id="insn-004fc500"></a> `004fc500` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004fc504"></a> `004fc504` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004fc508"></a> `004fc508` | `c0 00 00 54` | b.eq 0x004fc520 | `CONDITIONAL_JUMP`
<a id="insn-004fc50c"></a> `004fc50c` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-004fc510"></a> `004fc510` | `89 ff 07 36` | tbz w9,#0x0,0x004fc500 | `CONDITIONAL_JUMP`
<a id="insn-004fc514"></a> `004fc514` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-004fc518"></a> `004fc518` | `66 6e 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc51c"></a> `004fc51c` | `f9 ff ff 17` | b 0x004fc500 | `UNCONDITIONAL_JUMP`
<a id="insn-004fc520"></a> `004fc520` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004fc524"></a> `004fc524` | `34 07 00 f9` | str x20,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-004fc528"></a> `004fc528` | `62 6e 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fc52c"></a> `004fc52c` | `e0 03 c3 3c` | ldur q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc530"></a> `004fc530` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fc534"></a> `004fc534` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-004fc538"></a> `004fc538` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-004fc53c"></a> `004fc53c` | `01 00 66 9e` | fmov x1,d0 | `FALL_THROUGH`
<a id="insn-004fc540"></a> `004fc540` | `20 83 80 3c` | stur q0,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-004fc544"></a> `004fc544` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-004fc548"></a> `004fc548` | `28 00 00 eb` | subs x8,x1,x0 | `FALL_THROUGH`
<a id="insn-004fc54c"></a> `004fc54c` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-004fc550"></a> `004fc550` | `3f 00 00 eb` | cmp x1,x0 | `FALL_THROUGH`
<a id="insn-004fc554"></a> `004fc554` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-004fc558"></a> `004fc558` | `c9 0f 80 52` | mov w9,#0x7e | `FALL_THROUGH`
<a id="insn-004fc55c"></a> `004fc55c` | `08 11 c0 da` | clz x8,x8 | `FALL_THROUGH`
<a id="insn-004fc560"></a> `004fc560` | `28 05 08 cb` | sub x8,x9,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-004fc564"></a> `004fc564` | `e3 03 88 9a` | csel x3,xzr,x8,eq | `FALL_THROUGH`
<a id="insn-004fc568"></a> `004fc568` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc56c"></a> `004fc56c` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-004fc570"></a> `004fc570` | `b3 25 01 94` | bl 0x00545c3c | `UNCONDITIONAL_CALL`
<a id="insn-004fc574"></a> `004fc574` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc578"></a> `004fc578` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc57c"></a> `004fc57c` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc580"></a> `004fc580` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc584"></a> `004fc584` | `a1 0a 00 54` | b.ne 0x004fc6d8 | `CONDITIONAL_JUMP`
<a id="insn-004fc588"></a> `004fc588` | `ff 83 06 91` | add sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-004fc58c"></a> `004fc58c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fc590"></a> `004fc590` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fc594"></a> `004fc594` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fc598"></a> `004fc598` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fc59c"></a> `004fc59c` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fc5a0"></a> `004fc5a0` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-004fc5a4"></a> `004fc5a4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fc5a8"></a> `004fc5a8` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc5ac"></a> `004fc5ac` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc5b0"></a> `004fc5b0` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc5b4"></a> `004fc5b4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc5b8"></a> `004fc5b8` | `01 09 00 54` | b.ne 0x004fc6d8 | `CONDITIONAL_JUMP`
<a id="insn-004fc5bc"></a> `004fc5bc` | `a0 23 03 d1` | sub x0,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-004fc5c0"></a> `004fc5c0` | `69 fc fc 97` | bl 0x0043b764 | `CALL_TERMINATOR`
<a id="insn-004fc5c4"></a> `004fc5c4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc5c8"></a> `004fc5c8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc5cc"></a> `004fc5cc` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc5d0"></a> `004fc5d0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc5d4"></a> `004fc5d4` | `21 08 00 54` | b.ne 0x004fc6d8 | `CONDITIONAL_JUMP`
<a id="insn-004fc5d8"></a> `004fc5d8` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fc5dc"></a> `004fc5dc` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-004fc5e0"></a> `004fc5e0` | `61 fc fc 97` | bl 0x0043b764 | `CALL_TERMINATOR`
<a id="insn-004fc5e4"></a> `004fc5e4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fc5e8"></a> `004fc5e8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004fc5ec"></a> `004fc5ec` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fc5f0"></a> `004fc5f0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fc5f4"></a> `004fc5f4` | `21 07 00 54` | b.ne 0x004fc6d8 | `CONDITIONAL_JUMP`
<a id="insn-004fc5f8"></a> `004fc5f8` | `df 75 fd 97` | bl 0x00459d74 | `CALL_TERMINATOR`
<a id="insn-004fc6d8"></a> `004fc6d8` | `02 6e 1d 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004fbefc`](#insn-004fbefc) 範囲 `[['004fbefc', '004fbf67']]`
  - `CONDITIONAL_JUMP` [`004fbf64`](#insn-004fbf64) → [`004fbfb4`](#insn-004fbfb4)
  - `FALL_THROUGH` [`004fbf64`](#insn-004fbf64) → [`004fbf68`](#insn-004fbf68)
- ブロック [`004fbf68`](#insn-004fbf68) 範囲 `[['004fbf68', '004fbf9f']]`
  - `CONDITIONAL_JUMP` [`004fbf9c`](#insn-004fbf9c) → [`004fbfc0`](#insn-004fbfc0)
  - `FALL_THROUGH` [`004fbf9c`](#insn-004fbf9c) → [`004fbfa0`](#insn-004fbfa0)
- ブロック [`004fbfa0`](#insn-004fbfa0) 範囲 `[['004fbfa0', '004fbfb3']]`
  - `UNCONDITIONAL_JUMP` [`004fbfb0`](#insn-004fbfb0) → [`004fbfc8`](#insn-004fbfc8)
- ブロック [`004fbfb4`](#insn-004fbfb4) 範囲 `[['004fbfb4', '004fbfbf']]`
  - `CONDITIONAL_JUMP` [`004fbfbc`](#insn-004fbfbc) → [`004fbfa0`](#insn-004fbfa0)
  - `FALL_THROUGH` [`004fbfbc`](#insn-004fbfbc) → [`004fbfc0`](#insn-004fbfc0)
- ブロック [`004fbfc0`](#insn-004fbfc0) 範囲 `[['004fbfc0', '004fbfc7']]`
  - `FALL_THROUGH` [`004fbfc4`](#insn-004fbfc4) → [`004fbfc8`](#insn-004fbfc8)
- ブロック [`004fbfc8`](#insn-004fbfc8) 範囲 `[['004fbfc8', '004fbfd7']]`
  - `CONDITIONAL_JUMP` [`004fbfd4`](#insn-004fbfd4) → [`004fbfe4`](#insn-004fbfe4)
  - `FALL_THROUGH` [`004fbfd4`](#insn-004fbfd4) → [`004fbfd8`](#insn-004fbfd8)
- ブロック [`004fbfd8`](#insn-004fbfd8) 範囲 `[['004fbfd8', '004fbfe3']]`
  - `UNCONDITIONAL_JUMP` [`004fbfe0`](#insn-004fbfe0) → [`004fc52c`](#insn-004fc52c)
- ブロック [`004fbfe4`](#insn-004fbfe4) 範囲 `[['004fbfe4', '004fc01b']]`
  - `UNCONDITIONAL_JUMP` [`004fc018`](#insn-004fc018) → [`004fc024`](#insn-004fc024)
- ブロック [`004fc01c`](#insn-004fc01c) 範囲 `[['004fc01c', '004fc023']]`
  - `CONDITIONAL_JUMP` [`004fc020`](#insn-004fc020) → [`004fc4dc`](#insn-004fc4dc)
  - `FALL_THROUGH` [`004fc020`](#insn-004fc020) → [`004fc024`](#insn-004fc024)
- ブロック [`004fc024`](#insn-004fc024) 範囲 `[['004fc024', '004fc05b']]`
  - `CONDITIONAL_JUMP` [`004fc058`](#insn-004fc058) → [`004fc074`](#insn-004fc074)
  - `FALL_THROUGH` [`004fc058`](#insn-004fc058) → [`004fc05c`](#insn-004fc05c)
- ブロック [`004fc05c`](#insn-004fc05c) 範囲 `[['004fc05c', '004fc073']]`
  - `UNCONDITIONAL_JUMP` [`004fc070`](#insn-004fc070) → [`004fc0a0`](#insn-004fc0a0)
- ブロック [`004fc074`](#insn-004fc074) 範囲 `[['004fc074', '004fc09f']]`
  - `FALL_THROUGH` [`004fc09c`](#insn-004fc09c) → [`004fc0a0`](#insn-004fc0a0)
- ブロック [`004fc0a0`](#insn-004fc0a0) 範囲 `[['004fc0a0', '004fc0b3']]`
  - `CONDITIONAL_JUMP` [`004fc0b0`](#insn-004fc0b0) → [`004fc0c0`](#insn-004fc0c0)
  - `FALL_THROUGH` [`004fc0b0`](#insn-004fc0b0) → [`004fc0b4`](#insn-004fc0b4)
- ブロック [`004fc0b4`](#insn-004fc0b4) 範囲 `[['004fc0b4', '004fc0bf']]`
  - `FALL_THROUGH` [`004fc0bc`](#insn-004fc0bc) → [`004fc0c0`](#insn-004fc0c0)
- ブロック [`004fc0c0`](#insn-004fc0c0) 範囲 `[['004fc0c0', '004fc0d7']]`
  - `CONDITIONAL_JUMP` [`004fc0d4`](#insn-004fc0d4) → [`004fc0fc`](#insn-004fc0fc)
  - `FALL_THROUGH` [`004fc0d4`](#insn-004fc0d4) → [`004fc0d8`](#insn-004fc0d8)
- ブロック [`004fc0d8`](#insn-004fc0d8) 範囲 `[['004fc0d8', '004fc0fb']]`
  - `FALL_THROUGH` [`004fc0f8`](#insn-004fc0f8) → [`004fc0fc`](#insn-004fc0fc)
- ブロック [`004fc0fc`](#insn-004fc0fc) 範囲 `[['004fc0fc', '004fc13b']]`
  - `CONDITIONAL_JUMP` [`004fc138`](#insn-004fc138) → [`004fc144`](#insn-004fc144)
  - `FALL_THROUGH` [`004fc138`](#insn-004fc138) → [`004fc13c`](#insn-004fc13c)
- ブロック [`004fc13c`](#insn-004fc13c) 範囲 `[['004fc13c', '004fc13f']]`
  - `UNCONDITIONAL_JUMP` [`004fc13c`](#insn-004fc13c) → [`004fc4b4`](#insn-004fc4b4)
- ブロック [`004fc140`](#insn-004fc140) 範囲 `[['004fc140', '004fc143']]`
  - `FALL_THROUGH` [`004fc140`](#insn-004fc140) → [`004fc144`](#insn-004fc144)
- ブロック [`004fc144`](#insn-004fc144) 範囲 `[['004fc144', '004fc14f']]`
  - `CONDITIONAL_JUMP` [`004fc14c`](#insn-004fc14c) → [`004fc470`](#insn-004fc470)
  - `FALL_THROUGH` [`004fc14c`](#insn-004fc14c) → [`004fc150`](#insn-004fc150)
- ブロック [`004fc150`](#insn-004fc150) 範囲 `[['004fc150', '004fc15f']]`
  - `CONDITIONAL_JUMP` [`004fc15c`](#insn-004fc15c) → [`004fc5a8`](#insn-004fc5a8)
  - `FALL_THROUGH` [`004fc15c`](#insn-004fc15c) → [`004fc160`](#insn-004fc160)
- ブロック [`004fc160`](#insn-004fc160) 範囲 `[['004fc160', '004fc16b']]`
  - `CONDITIONAL_JUMP` [`004fc168`](#insn-004fc168) → [`004fc180`](#insn-004fc180)
  - `FALL_THROUGH` [`004fc168`](#insn-004fc168) → [`004fc16c`](#insn-004fc16c)
- ブロック [`004fc16c`](#insn-004fc16c) 範囲 `[['004fc16c', '004fc17b']]`
  - `CONDITIONAL_JUMP` [`004fc178`](#insn-004fc178) → [`004fc1b0`](#insn-004fc1b0)
  - `FALL_THROUGH` [`004fc178`](#insn-004fc178) → [`004fc17c`](#insn-004fc17c)
- ブロック [`004fc17c`](#insn-004fc17c) 範囲 `[['004fc17c', '004fc17f']]`
  - `UNCONDITIONAL_JUMP` [`004fc17c`](#insn-004fc17c) → [`004fc1c0`](#insn-004fc1c0)
- ブロック [`004fc180`](#insn-004fc180) 範囲 `[['004fc180', '004fc1af']]`
  - `FALL_THROUGH` [`004fc1ac`](#insn-004fc1ac) → [`004fc1b0`](#insn-004fc1b0)
- ブロック [`004fc1b0`](#insn-004fc1b0) 範囲 `[['004fc1b0', '004fc1bf']]`
  - `FALL_THROUGH` [`004fc1bc`](#insn-004fc1bc) → [`004fc1c0`](#insn-004fc1c0)
- ブロック [`004fc1c0`](#insn-004fc1c0) 範囲 `[['004fc1c0', '004fc1df']]`
  - `CONDITIONAL_JUMP` [`004fc1dc`](#insn-004fc1dc) → [`004fc204`](#insn-004fc204)
  - `FALL_THROUGH` [`004fc1dc`](#insn-004fc1dc) → [`004fc1e0`](#insn-004fc1e0)
- ブロック [`004fc1e0`](#insn-004fc1e0) 範囲 `[['004fc1e0', '004fc1e7']]`
  - `CONDITIONAL_JUMP` [`004fc1e4`](#insn-004fc1e4) → [`004fc220`](#insn-004fc220)
  - `FALL_THROUGH` [`004fc1e4`](#insn-004fc1e4) → [`004fc1e8`](#insn-004fc1e8)
- ブロック [`004fc1e8`](#insn-004fc1e8) 範囲 `[['004fc1e8', '004fc1ff']]`
  - `CONDITIONAL_JUMP` [`004fc1fc`](#insn-004fc1fc) → [`004fc220`](#insn-004fc220)
  - `FALL_THROUGH` [`004fc1fc`](#insn-004fc1fc) → [`004fc200`](#insn-004fc200)
- ブロック [`004fc200`](#insn-004fc200) 範囲 `[['004fc200', '004fc203']]`
  - `UNCONDITIONAL_JUMP` [`004fc200`](#insn-004fc200) → [`004fc440`](#insn-004fc440)
- ブロック [`004fc204`](#insn-004fc204) 範囲 `[['004fc204', '004fc21f']]`
  - `CONDITIONAL_JUMP` [`004fc21c`](#insn-004fc21c) → [`004fc440`](#insn-004fc440)
  - `FALL_THROUGH` [`004fc21c`](#insn-004fc21c) → [`004fc220`](#insn-004fc220)
- ブロック [`004fc220`](#insn-004fc220) 範囲 `[['004fc220', '004fc243']]`
  - `CONDITIONAL_JUMP` [`004fc240`](#insn-004fc240) → [`004fc5c4`](#insn-004fc5c4)
  - `FALL_THROUGH` [`004fc240`](#insn-004fc240) → [`004fc244`](#insn-004fc244)
- ブロック [`004fc244`](#insn-004fc244) 範囲 `[['004fc244', '004fc24b']]`
  - `CONDITIONAL_JUMP` [`004fc248`](#insn-004fc248) → [`004fc268`](#insn-004fc268)
  - `FALL_THROUGH` [`004fc248`](#insn-004fc248) → [`004fc24c`](#insn-004fc24c)
- ブロック [`004fc24c`](#insn-004fc24c) 範囲 `[['004fc24c', '004fc263']]`
  - `CONDITIONAL_JUMP` [`004fc260`](#insn-004fc260) → [`004fc298`](#insn-004fc298)
  - `FALL_THROUGH` [`004fc260`](#insn-004fc260) → [`004fc264`](#insn-004fc264)
- ブロック [`004fc264`](#insn-004fc264) 範囲 `[['004fc264', '004fc267']]`
  - `UNCONDITIONAL_JUMP` [`004fc264`](#insn-004fc264) → [`004fc2b4`](#insn-004fc2b4)
- ブロック [`004fc268`](#insn-004fc268) 範囲 `[['004fc268', '004fc297']]`
  - `FALL_THROUGH` [`004fc294`](#insn-004fc294) → [`004fc298`](#insn-004fc298)
- ブロック [`004fc298`](#insn-004fc298) 範囲 `[['004fc298', '004fc2b3']]`
  - `FALL_THROUGH` [`004fc2b0`](#insn-004fc2b0) → [`004fc2b4`](#insn-004fc2b4)
- ブロック [`004fc2b4`](#insn-004fc2b4) 範囲 `[['004fc2b4', '004fc2fb']]`
  - `CONDITIONAL_JUMP` [`004fc2f8`](#insn-004fc2f8) → [`004fc304`](#insn-004fc304)
  - `FALL_THROUGH` [`004fc2f8`](#insn-004fc2f8) → [`004fc2fc`](#insn-004fc2fc)
- ブロック [`004fc2fc`](#insn-004fc2fc) 範囲 `[['004fc2fc', '004fc303']]`
  - `FALL_THROUGH` [`004fc300`](#insn-004fc300) → [`004fc304`](#insn-004fc304)
- ブロック [`004fc304`](#insn-004fc304) 範囲 `[['004fc304', '004fc323']]`
  - `CONDITIONAL_JUMP` [`004fc320`](#insn-004fc320) → [`004fc428`](#insn-004fc428)
  - `FALL_THROUGH` [`004fc320`](#insn-004fc320) → [`004fc324`](#insn-004fc324)
- ブロック [`004fc324`](#insn-004fc324) 範囲 `[['004fc324', '004fc333']]`
  - `CONDITIONAL_JUMP` [`004fc330`](#insn-004fc330) → [`004fc3c8`](#insn-004fc3c8)
  - `FALL_THROUGH` [`004fc330`](#insn-004fc330) → [`004fc334`](#insn-004fc334)
- ブロック [`004fc334`](#insn-004fc334) 範囲 `[['004fc334', '004fc33b']]`
  - `CONDITIONAL_JUMP` [`004fc338`](#insn-004fc338) → [`004fc428`](#insn-004fc428)
  - `FALL_THROUGH` [`004fc338`](#insn-004fc338) → [`004fc33c`](#insn-004fc33c)
- ブロック [`004fc33c`](#insn-004fc33c) 範囲 `[['004fc33c', '004fc367']]`
  - `CONDITIONAL_JUMP` [`004fc364`](#insn-004fc364) → [`004fc374`](#insn-004fc374)
  - `FALL_THROUGH` [`004fc364`](#insn-004fc364) → [`004fc368`](#insn-004fc368)
- ブロック [`004fc368`](#insn-004fc368) 範囲 `[['004fc368', '004fc373']]`
  - `FALL_THROUGH` [`004fc370`](#insn-004fc370) → [`004fc374`](#insn-004fc374)
- ブロック [`004fc374`](#insn-004fc374) 範囲 `[['004fc374', '004fc37b']]`
  - `CONDITIONAL_JUMP` [`004fc378`](#insn-004fc378) → [`004fc408`](#insn-004fc408)
  - `FALL_THROUGH` [`004fc378`](#insn-004fc378) → [`004fc37c`](#insn-004fc37c)
- ブロック [`004fc37c`](#insn-004fc37c) 範囲 `[['004fc37c', '004fc3af']]`
  - `CONDITIONAL_JUMP` [`004fc3ac`](#insn-004fc3ac) → [`004fc414`](#insn-004fc414)
  - `FALL_THROUGH` [`004fc3ac`](#insn-004fc3ac) → [`004fc3b0`](#insn-004fc3b0)
- ブロック [`004fc3b0`](#insn-004fc3b0) 範囲 `[['004fc3b0', '004fc3c7']]`
  - `UNCONDITIONAL_JUMP` [`004fc3c4`](#insn-004fc3c4) → [`004fc41c`](#insn-004fc41c)
- ブロック [`004fc3c8`](#insn-004fc3c8) 範囲 `[['004fc3c8', '004fc3d3']]`
  - `CONDITIONAL_JUMP` [`004fc3d0`](#insn-004fc3d0) → [`004fc3f8`](#insn-004fc3f8)
  - `FALL_THROUGH` [`004fc3d0`](#insn-004fc3d0) → [`004fc3d4`](#insn-004fc3d4)
- ブロック [`004fc3d4`](#insn-004fc3d4) 範囲 `[['004fc3d4', '004fc3db']]`
  - `CONDITIONAL_JUMP` [`004fc3d8`](#insn-004fc3d8) → [`004fc450`](#insn-004fc450)
  - `FALL_THROUGH` [`004fc3d8`](#insn-004fc3d8) → [`004fc3dc`](#insn-004fc3dc)
- ブロック [`004fc3dc`](#insn-004fc3dc) 範囲 `[['004fc3dc', '004fc3f7']]`
  - `UNCONDITIONAL_JUMP` [`004fc3f4`](#insn-004fc3f4) → [`004fc460`](#insn-004fc460)
- ブロック [`004fc3f8`](#insn-004fc3f8) 範囲 `[['004fc3f8', '004fc407']]`
  - `UNCONDITIONAL_JUMP` [`004fc404`](#insn-004fc404) → [`004fc460`](#insn-004fc460)
- ブロック [`004fc408`](#insn-004fc408) 範囲 `[['004fc408', '004fc413']]`
  - `CONDITIONAL_JUMP` [`004fc410`](#insn-004fc410) → [`004fc3b0`](#insn-004fc3b0)
  - `FALL_THROUGH` [`004fc410`](#insn-004fc410) → [`004fc414`](#insn-004fc414)
- ブロック [`004fc414`](#insn-004fc414) 範囲 `[['004fc414', '004fc41b']]`
  - `FALL_THROUGH` [`004fc418`](#insn-004fc418) → [`004fc41c`](#insn-004fc41c)
- ブロック [`004fc41c`](#insn-004fc41c) 範囲 `[['004fc41c', '004fc427']]`
  - `FALL_THROUGH` [`004fc424`](#insn-004fc424) → [`004fc428`](#insn-004fc428)
- ブロック [`004fc428`](#insn-004fc428) 範囲 `[['004fc428', '004fc42f']]`
  - `CONDITIONAL_JUMP` [`004fc42c`](#insn-004fc42c) → [`004fc438`](#insn-004fc438)
  - `FALL_THROUGH` [`004fc42c`](#insn-004fc42c) → [`004fc430`](#insn-004fc430)
- ブロック [`004fc430`](#insn-004fc430) 範囲 `[['004fc430', '004fc437']]`
  - `FALL_THROUGH` [`004fc434`](#insn-004fc434) → [`004fc438`](#insn-004fc438)
- ブロック [`004fc438`](#insn-004fc438) 範囲 `[['004fc438', '004fc43f']]`
  - `FALL_THROUGH` [`004fc43c`](#insn-004fc43c) → [`004fc440`](#insn-004fc440)
- ブロック [`004fc440`](#insn-004fc440) 範囲 `[['004fc440', '004fc443']]`
  - `CONDITIONAL_JUMP` [`004fc440`](#insn-004fc440) → [`004fc140`](#insn-004fc140)
  - `FALL_THROUGH` [`004fc440`](#insn-004fc440) → [`004fc444`](#insn-004fc444)
- ブロック [`004fc444`](#insn-004fc444) 範囲 `[['004fc444', '004fc44f']]`
  - `UNCONDITIONAL_JUMP` [`004fc44c`](#insn-004fc44c) → [`004fc140`](#insn-004fc140)
- ブロック [`004fc450`](#insn-004fc450) 範囲 `[['004fc450', '004fc45f']]`
  - `FALL_THROUGH` [`004fc45c`](#insn-004fc45c) → [`004fc460`](#insn-004fc460)
- ブロック [`004fc460`](#insn-004fc460) 範囲 `[['004fc460', '004fc46b']]`
  - `CONDITIONAL_JUMP` [`004fc468`](#insn-004fc468) → [`004fc430`](#insn-004fc430)
  - `FALL_THROUGH` [`004fc468`](#insn-004fc468) → [`004fc46c`](#insn-004fc46c)
- ブロック [`004fc46c`](#insn-004fc46c) 範囲 `[['004fc46c', '004fc46f']]`
  - `UNCONDITIONAL_JUMP` [`004fc46c`](#insn-004fc46c) → [`004fc438`](#insn-004fc438)
- ブロック [`004fc470`](#insn-004fc470) 範囲 `[['004fc470', '004fc47b']]`
  - `CONDITIONAL_JUMP` [`004fc478`](#insn-004fc478) → [`004fc498`](#insn-004fc498)
  - `FALL_THROUGH` [`004fc478`](#insn-004fc478) → [`004fc47c`](#insn-004fc47c)
- ブロック [`004fc47c`](#insn-004fc47c) 範囲 `[['004fc47c', '004fc487']]`
  - `CONDITIONAL_JUMP` [`004fc484`](#insn-004fc484) → [`004fc5e4`](#insn-004fc5e4)
  - `FALL_THROUGH` [`004fc484`](#insn-004fc484) → [`004fc488`](#insn-004fc488)
- ブロック [`004fc488`](#insn-004fc488) 範囲 `[['004fc488', '004fc497']]`
  - `FALL_THROUGH` [`004fc494`](#insn-004fc494) → [`004fc498`](#insn-004fc498)
- ブロック [`004fc498`](#insn-004fc498) 範囲 `[['004fc498', '004fc4a7']]`
  - `CONDITIONAL_JUMP` [`004fc4a4`](#insn-004fc4a4) → [`004fc4b4`](#insn-004fc4b4)
  - `FALL_THROUGH` [`004fc4a4`](#insn-004fc4a4) → [`004fc4a8`](#insn-004fc4a8)
- ブロック [`004fc4a8`](#insn-004fc4a8) 範囲 `[['004fc4a8', '004fc4ab']]`
  - `CONDITIONAL_JUMP` [`004fc4a8`](#insn-004fc4a8) → [`004fc4c8`](#insn-004fc4c8)
  - `FALL_THROUGH` [`004fc4a8`](#insn-004fc4a8) → [`004fc4ac`](#insn-004fc4ac)
- ブロック [`004fc4ac`](#insn-004fc4ac) 範囲 `[['004fc4ac', '004fc4b3']]`
  - `UNCONDITIONAL_JUMP` [`004fc4b0`](#insn-004fc4b0) → [`004fc4bc`](#insn-004fc4bc)
- ブロック [`004fc4b4`](#insn-004fc4b4) 範囲 `[['004fc4b4', '004fc4bb']]`
  - `FALL_THROUGH` [`004fc4b8`](#insn-004fc4b8) → [`004fc4bc`](#insn-004fc4bc)
- ブロック [`004fc4bc`](#insn-004fc4bc) 範囲 `[['004fc4bc', '004fc4c7']]`
  - `FALL_THROUGH` [`004fc4c4`](#insn-004fc4c4) → [`004fc4c8`](#insn-004fc4c8)
- ブロック [`004fc4c8`](#insn-004fc4c8) 範囲 `[['004fc4c8', '004fc4cf']]`
  - `CONDITIONAL_JUMP` [`004fc4cc`](#insn-004fc4cc) → [`004fc01c`](#insn-004fc01c)
  - `FALL_THROUGH` [`004fc4cc`](#insn-004fc4cc) → [`004fc4d0`](#insn-004fc4d0)
- ブロック [`004fc4d0`](#insn-004fc4d0) 範囲 `[['004fc4d0', '004fc4db']]`
  - `UNCONDITIONAL_JUMP` [`004fc4d8`](#insn-004fc4d8) → [`004fc01c`](#insn-004fc01c)
- ブロック [`004fc4dc`](#insn-004fc4dc) 範囲 `[['004fc4dc', '004fc4eb']]`
  - `CONDITIONAL_JUMP` [`004fc4e8`](#insn-004fc4e8) → [`004fc52c`](#insn-004fc52c)
  - `FALL_THROUGH` [`004fc4e8`](#insn-004fc4e8) → [`004fc4ec`](#insn-004fc4ec)
- ブロック [`004fc4ec`](#insn-004fc4ec) 範囲 `[['004fc4ec', '004fc4f7']]`
  - `CONDITIONAL_JUMP` [`004fc4f4`](#insn-004fc4f4) → [`004fc520`](#insn-004fc520)
  - `FALL_THROUGH` [`004fc4f4`](#insn-004fc4f4) → [`004fc4f8`](#insn-004fc4f8)
- ブロック [`004fc4f8`](#insn-004fc4f8) 範囲 `[['004fc4f8', '004fc4ff']]`
  - `UNCONDITIONAL_JUMP` [`004fc4fc`](#insn-004fc4fc) → [`004fc50c`](#insn-004fc50c)
- ブロック [`004fc500`](#insn-004fc500) 範囲 `[['004fc500', '004fc50b']]`
  - `CONDITIONAL_JUMP` [`004fc508`](#insn-004fc508) → [`004fc520`](#insn-004fc520)
  - `FALL_THROUGH` [`004fc508`](#insn-004fc508) → [`004fc50c`](#insn-004fc50c)
- ブロック [`004fc50c`](#insn-004fc50c) 範囲 `[['004fc50c', '004fc513']]`
  - `CONDITIONAL_JUMP` [`004fc510`](#insn-004fc510) → [`004fc500`](#insn-004fc500)
  - `FALL_THROUGH` [`004fc510`](#insn-004fc510) → [`004fc514`](#insn-004fc514)
- ブロック [`004fc514`](#insn-004fc514) 範囲 `[['004fc514', '004fc51f']]`
  - `UNCONDITIONAL_JUMP` [`004fc51c`](#insn-004fc51c) → [`004fc500`](#insn-004fc500)
- ブロック [`004fc520`](#insn-004fc520) 範囲 `[['004fc520', '004fc52b']]`
  - `FALL_THROUGH` [`004fc528`](#insn-004fc528) → [`004fc52c`](#insn-004fc52c)
- ブロック [`004fc52c`](#insn-004fc52c) 範囲 `[['004fc52c', '004fc587']]`
  - `CONDITIONAL_JUMP` [`004fc584`](#insn-004fc584) → [`004fc6d8`](#insn-004fc6d8)
  - `FALL_THROUGH` [`004fc584`](#insn-004fc584) → [`004fc588`](#insn-004fc588)
- ブロック [`004fc588`](#insn-004fc588) 範囲 `[['004fc588', '004fc5a7']]`
- ブロック [`004fc5a8`](#insn-004fc5a8) 範囲 `[['004fc5a8', '004fc5bb']]`
  - `CONDITIONAL_JUMP` [`004fc5b8`](#insn-004fc5b8) → [`004fc6d8`](#insn-004fc6d8)
  - `FALL_THROUGH` [`004fc5b8`](#insn-004fc5b8) → [`004fc5bc`](#insn-004fc5bc)
- ブロック [`004fc5bc`](#insn-004fc5bc) 範囲 `[['004fc5bc', '004fc5c3']]`
- ブロック [`004fc5c4`](#insn-004fc5c4) 範囲 `[['004fc5c4', '004fc5d7']]`
  - `CONDITIONAL_JUMP` [`004fc5d4`](#insn-004fc5d4) → [`004fc6d8`](#insn-004fc6d8)
  - `FALL_THROUGH` [`004fc5d4`](#insn-004fc5d4) → [`004fc5d8`](#insn-004fc5d8)
- ブロック [`004fc5d8`](#insn-004fc5d8) 範囲 `[['004fc5d8', '004fc5e3']]`
- ブロック [`004fc5e4`](#insn-004fc5e4) 範囲 `[['004fc5e4', '004fc5f7']]`
  - `CONDITIONAL_JUMP` [`004fc5f4`](#insn-004fc5f4) → [`004fc6d8`](#insn-004fc6d8)
  - `FALL_THROUGH` [`004fc5f4`](#insn-004fc5f4) → [`004fc5f8`](#insn-004fc5f8)
- ブロック [`004fc5f8`](#insn-004fc5f8) 範囲 `[['004fc5f8', '004fc5fb']]`
- ブロック [`004fc6d8`](#insn-004fc6d8) 範囲 `[['004fc6d8', '004fc6db']]`

## 命令位置別の参照

- [`004fbefc`](#insn-004fbefc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf00`](#insn-004fbf00) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf04`](#insn-004fbf04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf08`](#insn-004fbf08) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf0c`](#insn-004fbf0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf10`](#insn-004fbf10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf28`](#insn-004fbf28) → `Stack[-0x1f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf34`](#insn-004fbf34) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf44`](#insn-004fbf44) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf48`](#insn-004fbf48) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf4c`](#insn-004fbf4c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf50`](#insn-004fbf50) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf58`](#insn-004fbf58) → [`0053a0b4`](../0053a/0053a0b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053a0b4` · 推定シンボル `None` · 推定型 `None`
- [`004fbf5c`](#insn-004fbf5c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf64`](#insn-004fbf64) → [`004fbfb4`](#insn-004fbfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf68`](#insn-004fbf68) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbf9c`](#insn-004fbf9c) → [`004fbfc0`](#insn-004fbfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfb0`](#insn-004fbfb0) → [`004fbfc8`](#insn-004fbfc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfbc`](#insn-004fbfbc) → [`004fbfa0`](#insn-004fbfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfc4`](#insn-004fbfc4) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`
- [`004fbfc8`](#insn-004fbfc8) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfd0`](#insn-004fbfd0) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfd4`](#insn-004fbfd4) → [`004fbfe4`](#insn-004fbfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbfdc`](#insn-004fbfdc) → [`00539f1c`](../00539/00539f1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00539f1c` · 推定シンボル `None` · 推定型 `None`
- [`004fbfe0`](#insn-004fbfe0) → [`004fc52c`](#insn-004fc52c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbffc`](#insn-004fbffc) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc008`](#insn-004fc008) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc014`](#insn-004fc014) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc018`](#insn-004fc018) → [`004fc024`](#insn-004fc024) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc01c`](#insn-004fc01c) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc020`](#insn-004fc020) → [`004fc4dc`](#insn-004fc4dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc024`](#insn-004fc024) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc034`](#insn-004fc034) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc058`](#insn-004fc058) → [`004fc074`](#insn-004fc074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc068`](#insn-004fc068) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc06c`](#insn-004fc06c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc070`](#insn-004fc070) → [`004fc0a0`](#insn-004fc0a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc07c`](#insn-004fc07c) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`
- [`004fc080`](#insn-004fc080) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc09c`](#insn-004fc09c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0b0`](#insn-004fc0b0) → [`004fc0c0`](#insn-004fc0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0b8`](#insn-004fc0b8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc0bc`](#insn-004fc0bc) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0c0`](#insn-004fc0c0) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0d0`](#insn-004fc0d0) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0d4`](#insn-004fc0d4) → [`004fc0fc`](#insn-004fc0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0d8`](#insn-004fc0d8) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0e0`](#insn-004fc0e0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc0e4`](#insn-004fc0e4) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0e8`](#insn-004fc0e8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0f4`](#insn-004fc0f4) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0f8`](#insn-004fc0f8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc0fc`](#insn-004fc0fc) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc100`](#insn-004fc100) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc108`](#insn-004fc108) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc110`](#insn-004fc110) → [`00c59840`](../00c59/00c59840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59840` · 推定シンボル `None` · 推定型 `None`
- [`004fc11c`](#insn-004fc11c) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc120`](#insn-004fc120) → `00c6a348`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004fc120`](#insn-004fc120) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc124`](#insn-004fc124) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc12c`](#insn-004fc12c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc130`](#insn-004fc130) → `00c9b0c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fc134`](#insn-004fc134) → [`0112a148`](../0112a/0112a148.md) · `DATA` · `ANALYSIS` · 関数 `0112a148` · 推定シンボル `None` · 推定型 `None`
- [`004fc134`](#insn-004fc134) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc138`](#insn-004fc138) → [`004fc144`](#insn-004fc144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc13c`](#insn-004fc13c) → [`004fc4b4`](#insn-004fc4b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc140`](#insn-004fc140) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc144`](#insn-004fc144) → [`00c59850`](../00c59/00c59850.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59850` · 推定シンボル `None` · 推定型 `None`
- [`004fc14c`](#insn-004fc14c) → [`004fc470`](#insn-004fc470) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc154`](#insn-004fc154) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`004fc15c`](#insn-004fc15c) → [`004fc5a8`](#insn-004fc5a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc168`](#insn-004fc168) → [`004fc180`](#insn-004fc180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc174`](#insn-004fc174) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc178`](#insn-004fc178) → [`004fc1b0`](#insn-004fc1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc17c`](#insn-004fc17c) → [`004fc1c0`](#insn-004fc1c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc19c`](#insn-004fc19c) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`004fc1a8`](#insn-004fc1a8) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1ac`](#insn-004fc1ac) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1bc`](#insn-004fc1bc) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`004fc1c4`](#insn-004fc1c4) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1c8`](#insn-004fc1c8) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1dc`](#insn-004fc1dc) → [`004fc204`](#insn-004fc204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1e4`](#insn-004fc1e4) → [`004fc220`](#insn-004fc220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1e8`](#insn-004fc1e8) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc1fc`](#insn-004fc1fc) → [`004fc220`](#insn-004fc220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc200`](#insn-004fc200) → [`004fc440`](#insn-004fc440) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc204`](#insn-004fc204) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc21c`](#insn-004fc21c) → [`004fc440`](#insn-004fc440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc220`](#insn-004fc220) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc224`](#insn-004fc224) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc240`](#insn-004fc240) → [`004fc5c4`](#insn-004fc5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc248`](#insn-004fc248) → [`004fc268`](#insn-004fc268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc250`](#insn-004fc250) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc254`](#insn-004fc254) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc258`](#insn-004fc258) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc25c`](#insn-004fc25c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc260`](#insn-004fc260) → [`004fc298`](#insn-004fc298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc264`](#insn-004fc264) → [`004fc2b4`](#insn-004fc2b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc284`](#insn-004fc284) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`004fc290`](#insn-004fc290) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc294`](#insn-004fc294) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc298`](#insn-004fc298) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc29c`](#insn-004fc29c) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2b0`](#insn-004fc2b0) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`004fc2b4`](#insn-004fc2b4) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2d0`](#insn-004fc2d0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004fc2e0`](#insn-004fc2e0) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2e8`](#insn-004fc2e8) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2f4`](#insn-004fc2f4) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2f8`](#insn-004fc2f8) → [`004fc304`](#insn-004fc304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc2fc`](#insn-004fc2fc) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc300`](#insn-004fc300) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc304`](#insn-004fc304) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc308`](#insn-004fc308) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc318`](#insn-004fc318) → [`00c59860`](../00c59/00c59860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59860` · 推定シンボル `None` · 推定型 `None`
- [`004fc320`](#insn-004fc320) → [`004fc428`](#insn-004fc428) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc324`](#insn-004fc324) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc330`](#insn-004fc330) → [`004fc3c8`](#insn-004fc3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc338`](#insn-004fc338) → [`004fc428`](#insn-004fc428) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc33c`](#insn-004fc33c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc354`](#insn-004fc354) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc364`](#insn-004fc364) → [`004fc374`](#insn-004fc374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc36c`](#insn-004fc36c) → [`0053a0b4`](../0053a/0053a0b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053a0b4` · 推定シンボル `None` · 推定型 `None`
- [`004fc370`](#insn-004fc370) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc378`](#insn-004fc378) → [`004fc408`](#insn-004fc408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc37c`](#insn-004fc37c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3a8`](#insn-004fc3a8) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3ac`](#insn-004fc3ac) → [`004fc414`](#insn-004fc414) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3b4`](#insn-004fc3b4) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3b8`](#insn-004fc3b8) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3c4`](#insn-004fc3c4) → [`004fc41c`](#insn-004fc41c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3c8`](#insn-004fc3c8) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3d0`](#insn-004fc3d0) → [`004fc3f8`](#insn-004fc3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3d4`](#insn-004fc3d4) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3d8`](#insn-004fc3d8) → [`004fc450`](#insn-004fc450) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3e0`](#insn-004fc3e0) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3e8`](#insn-004fc3e8) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc3f4`](#insn-004fc3f4) → [`004fc460`](#insn-004fc460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc400`](#insn-004fc400) → [`00540d7c`](../00540/00540d7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00540d7c` · 推定シンボル `None` · 推定型 `None`
- [`004fc404`](#insn-004fc404) → [`004fc460`](#insn-004fc460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc40c`](#insn-004fc40c) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc410`](#insn-004fc410) → [`004fc3b0`](#insn-004fc3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc414`](#insn-004fc414) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc418`](#insn-004fc418) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`
- [`004fc41c`](#insn-004fc41c) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc424`](#insn-004fc424) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc428`](#insn-004fc428) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc42c`](#insn-004fc42c) → [`004fc438`](#insn-004fc438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc430`](#insn-004fc430) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc434`](#insn-004fc434) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc438`](#insn-004fc438) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc440`](#insn-004fc440) → [`004fc140`](#insn-004fc140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc444`](#insn-004fc444) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc448`](#insn-004fc448) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc44c`](#insn-004fc44c) → [`004fc140`](#insn-004fc140) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc450`](#insn-004fc450) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc458`](#insn-004fc458) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`
- [`004fc460`](#insn-004fc460) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc464`](#insn-004fc464) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc468`](#insn-004fc468) → [`004fc430`](#insn-004fc430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc46c`](#insn-004fc46c) → [`004fc438`](#insn-004fc438) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc470`](#insn-004fc470) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc474`](#insn-004fc474) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc478`](#insn-004fc478) → [`004fc498`](#insn-004fc498) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc47c`](#insn-004fc47c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc480`](#insn-004fc480) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc484`](#insn-004fc484) → [`004fc5e4`](#insn-004fc5e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc488`](#insn-004fc488) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc48c`](#insn-004fc48c) → `00c6a378`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004fc494`](#insn-004fc494) → [`0053aa6c`](../0053a/0053aa6c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0053aa6c` · 推定シンボル `None` · 推定型 `None`
- [`004fc498`](#insn-004fc498) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc49c`](#insn-004fc49c) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4a4`](#insn-004fc4a4) → [`004fc4b4`](#insn-004fc4b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4a8`](#insn-004fc4a8) → [`004fc4c8`](#insn-004fc4c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4b0`](#insn-004fc4b0) → [`004fc4bc`](#insn-004fc4bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4bc`](#insn-004fc4bc) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4c0`](#insn-004fc4c0) → `00c6a368`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fc4c0`](#insn-004fc4c0) → `00c6a370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fc4c4`](#insn-004fc4c4) → [`0053aa64`](../0053a/0053aa64.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0053aa64` · 推定シンボル `None` · 推定型 `None`
- [`004fc4c4`](#insn-004fc4c4) → [`0053aa68`](../0053a/0053aa68.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0053aa68` · 推定シンボル `None` · 推定型 `None`
- [`004fc4c8`](#insn-004fc4c8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4cc`](#insn-004fc4cc) → [`004fc01c`](#insn-004fc01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4d0`](#insn-004fc4d0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4d4`](#insn-004fc4d4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc4d8`](#insn-004fc4d8) → [`004fc01c`](#insn-004fc01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4e4`](#insn-004fc4e4) → [`00539f1c`](../00539/00539f1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00539f1c` · 推定シンボル `None` · 推定型 `None`
- [`004fc4e8`](#insn-004fc4e8) → [`004fc52c`](#insn-004fc52c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4f4`](#insn-004fc4f4) → [`004fc520`](#insn-004fc520) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc4fc`](#insn-004fc4fc) → [`004fc50c`](#insn-004fc50c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc508`](#insn-004fc508) → [`004fc520`](#insn-004fc520) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc510`](#insn-004fc510) → [`004fc500`](#insn-004fc500) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc518`](#insn-004fc518) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc51c`](#insn-004fc51c) → [`004fc500`](#insn-004fc500) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc528`](#insn-004fc528) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fc52c`](#insn-004fc52c) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc530`](#insn-004fc530) → `Stack[-0x1d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc570`](#insn-004fc570) → [`00545c3c`](../00545/00545c3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00545c3c` · 推定シンボル `None` · 推定型 `None`
- [`004fc574`](#insn-004fc574) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc57c`](#insn-004fc57c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc584`](#insn-004fc584) → [`004fc6d8`](#insn-004fc6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc58c`](#insn-004fc58c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc590`](#insn-004fc590) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc594`](#insn-004fc594) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc598`](#insn-004fc598) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc59c`](#insn-004fc59c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5a0`](#insn-004fc5a0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5a8`](#insn-004fc5a8) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5b0`](#insn-004fc5b0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5b8`](#insn-004fc5b8) → [`004fc6d8`](#insn-004fc6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5c0`](#insn-004fc5c0) → [`0043b764`](../0043b/0043b764.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b764` · 推定シンボル `None` · 推定型 `None`
- [`004fc5c4`](#insn-004fc5c4) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5cc`](#insn-004fc5cc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5d4`](#insn-004fc5d4) → [`004fc6d8`](#insn-004fc6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5e0`](#insn-004fc5e0) → [`0043b764`](../0043b/0043b764.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b764` · 推定シンボル `None` · 推定型 `None`
- [`004fc5e4`](#insn-004fc5e4) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5ec`](#insn-004fc5ec) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5f4`](#insn-004fc5f4) → [`004fc6d8`](#insn-004fc6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fc5f8`](#insn-004fc5f8) → [`00459d74`](../00459/00459d74.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459d74` · 推定シンボル `None` · 推定型 `None`
- [`004fc6d8`](#insn-004fc6d8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004fbefc`](#insn-004fbefc)

~~~json
{
  "source": "004fbefc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf00`](#insn-004fbf00)

~~~json
{
  "source": "004fbf00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf04`](#insn-004fbf04)

~~~json
{
  "source": "004fbf04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf08`](#insn-004fbf08)

~~~json
{
  "source": "004fbf08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf0c`](#insn-004fbf0c)

~~~json
{
  "source": "004fbf0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf10`](#insn-004fbf10)

~~~json
{
  "source": "004fbf10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf28`](#insn-004fbf28)

~~~json
{
  "source": "004fbf28",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf34`](#insn-004fbf34)

~~~json
{
  "source": "004fbf34",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf44`](#insn-004fbf44)

~~~json
{
  "source": "004fbf44",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf48`](#insn-004fbf48)

~~~json
{
  "source": "004fbf48",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf4c`](#insn-004fbf4c)

~~~json
{
  "source": "004fbf4c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf50`](#insn-004fbf50)

~~~json
{
  "source": "004fbf50",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf58`](#insn-004fbf58)

~~~json
{
  "source": "004fbf58",
  "target": "0053a0b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbf5c`](#insn-004fbf5c)

~~~json
{
  "source": "004fbf5c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf64`](#insn-004fbf64)

~~~json
{
  "source": "004fbf64",
  "target": "004fbfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf68`](#insn-004fbf68)

~~~json
{
  "source": "004fbf68",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbf9c`](#insn-004fbf9c)

~~~json
{
  "source": "004fbf9c",
  "target": "004fbfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfb0`](#insn-004fbfb0)

~~~json
{
  "source": "004fbfb0",
  "target": "004fbfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfbc`](#insn-004fbfbc)

~~~json
{
  "source": "004fbfbc",
  "target": "004fbfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfc4`](#insn-004fbfc4)

~~~json
{
  "source": "004fbfc4",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbfc8`](#insn-004fbfc8)

~~~json
{
  "source": "004fbfc8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfd0`](#insn-004fbfd0)

~~~json
{
  "source": "004fbfd0",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfd4`](#insn-004fbfd4)

~~~json
{
  "source": "004fbfd4",
  "target": "004fbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbfdc`](#insn-004fbfdc)

~~~json
{
  "source": "004fbfdc",
  "target": "00539f1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbfe0`](#insn-004fbfe0)

~~~json
{
  "source": "004fbfe0",
  "target": "004fc52c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbffc`](#insn-004fbffc)

~~~json
{
  "source": "004fbffc",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc008`](#insn-004fc008)

~~~json
{
  "source": "004fc008",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc014`](#insn-004fc014)

~~~json
{
  "source": "004fc014",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc018`](#insn-004fc018)

~~~json
{
  "source": "004fc018",
  "target": "004fc024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc01c`](#insn-004fc01c)

~~~json
{
  "source": "004fc01c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc020`](#insn-004fc020)

~~~json
{
  "source": "004fc020",
  "target": "004fc4dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc024`](#insn-004fc024)

~~~json
{
  "source": "004fc024",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc034`](#insn-004fc034)

~~~json
{
  "source": "004fc034",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc058`](#insn-004fc058)

~~~json
{
  "source": "004fc058",
  "target": "004fc074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc068`](#insn-004fc068)

~~~json
{
  "source": "004fc068",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc06c`](#insn-004fc06c)

~~~json
{
  "source": "004fc06c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc070`](#insn-004fc070)

~~~json
{
  "source": "004fc070",
  "target": "004fc0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc07c`](#insn-004fc07c)

~~~json
{
  "source": "004fc07c",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc080`](#insn-004fc080)

~~~json
{
  "source": "004fc080",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc09c`](#insn-004fc09c)

~~~json
{
  "source": "004fc09c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0b0`](#insn-004fc0b0)

~~~json
{
  "source": "004fc0b0",
  "target": "004fc0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0b8`](#insn-004fc0b8)

~~~json
{
  "source": "004fc0b8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc0bc`](#insn-004fc0bc)

~~~json
{
  "source": "004fc0bc",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0c0`](#insn-004fc0c0)

~~~json
{
  "source": "004fc0c0",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0d0`](#insn-004fc0d0)

~~~json
{
  "source": "004fc0d0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0d4`](#insn-004fc0d4)

~~~json
{
  "source": "004fc0d4",
  "target": "004fc0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0d8`](#insn-004fc0d8)

~~~json
{
  "source": "004fc0d8",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0e0`](#insn-004fc0e0)

~~~json
{
  "source": "004fc0e0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc0e4`](#insn-004fc0e4)

~~~json
{
  "source": "004fc0e4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0e8`](#insn-004fc0e8)

~~~json
{
  "source": "004fc0e8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0f4`](#insn-004fc0f4)

~~~json
{
  "source": "004fc0f4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0f8`](#insn-004fc0f8)

~~~json
{
  "source": "004fc0f8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc0fc`](#insn-004fc0fc)

~~~json
{
  "source": "004fc0fc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc100`](#insn-004fc100)

~~~json
{
  "source": "004fc100",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc108`](#insn-004fc108)

~~~json
{
  "source": "004fc108",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc110`](#insn-004fc110)

~~~json
{
  "source": "004fc110",
  "target": "00c59840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc11c`](#insn-004fc11c)

~~~json
{
  "source": "004fc11c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc120`](#insn-004fc120)

~~~json
{
  "source": "004fc120",
  "target": "00c6a348",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6a348",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc120`](#insn-004fc120)

~~~json
{
  "source": "004fc120",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc124`](#insn-004fc124)

~~~json
{
  "source": "004fc124",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc12c`](#insn-004fc12c)

~~~json
{
  "source": "004fc12c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc130`](#insn-004fc130)

~~~json
{
  "source": "004fc130",
  "target": "00c9b0c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b0c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc134`](#insn-004fc134)

~~~json
{
  "source": "004fc134",
  "target": "0112a148",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc134`](#insn-004fc134)

~~~json
{
  "source": "004fc134",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc138`](#insn-004fc138)

~~~json
{
  "source": "004fc138",
  "target": "004fc144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc13c`](#insn-004fc13c)

~~~json
{
  "source": "004fc13c",
  "target": "004fc4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc140`](#insn-004fc140)

~~~json
{
  "source": "004fc140",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc144`](#insn-004fc144)

~~~json
{
  "source": "004fc144",
  "target": "00c59850",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc14c`](#insn-004fc14c)

~~~json
{
  "source": "004fc14c",
  "target": "004fc470",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc154`](#insn-004fc154)

~~~json
{
  "source": "004fc154",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc15c`](#insn-004fc15c)

~~~json
{
  "source": "004fc15c",
  "target": "004fc5a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc168`](#insn-004fc168)

~~~json
{
  "source": "004fc168",
  "target": "004fc180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc174`](#insn-004fc174)

~~~json
{
  "source": "004fc174",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc178`](#insn-004fc178)

~~~json
{
  "source": "004fc178",
  "target": "004fc1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc17c`](#insn-004fc17c)

~~~json
{
  "source": "004fc17c",
  "target": "004fc1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc19c`](#insn-004fc19c)

~~~json
{
  "source": "004fc19c",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc1a8`](#insn-004fc1a8)

~~~json
{
  "source": "004fc1a8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1ac`](#insn-004fc1ac)

~~~json
{
  "source": "004fc1ac",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1bc`](#insn-004fc1bc)

~~~json
{
  "source": "004fc1bc",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc1c4`](#insn-004fc1c4)

~~~json
{
  "source": "004fc1c4",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1c8`](#insn-004fc1c8)

~~~json
{
  "source": "004fc1c8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1dc`](#insn-004fc1dc)

~~~json
{
  "source": "004fc1dc",
  "target": "004fc204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1e4`](#insn-004fc1e4)

~~~json
{
  "source": "004fc1e4",
  "target": "004fc220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1e8`](#insn-004fc1e8)

~~~json
{
  "source": "004fc1e8",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc1fc`](#insn-004fc1fc)

~~~json
{
  "source": "004fc1fc",
  "target": "004fc220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc200`](#insn-004fc200)

~~~json
{
  "source": "004fc200",
  "target": "004fc440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc204`](#insn-004fc204)

~~~json
{
  "source": "004fc204",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc21c`](#insn-004fc21c)

~~~json
{
  "source": "004fc21c",
  "target": "004fc440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc220`](#insn-004fc220)

~~~json
{
  "source": "004fc220",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc224`](#insn-004fc224)

~~~json
{
  "source": "004fc224",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc240`](#insn-004fc240)

~~~json
{
  "source": "004fc240",
  "target": "004fc5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc248`](#insn-004fc248)

~~~json
{
  "source": "004fc248",
  "target": "004fc268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc250`](#insn-004fc250)

~~~json
{
  "source": "004fc250",
  "target": "Stack[-0x1e8]",
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
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc25c`](#insn-004fc25c)

~~~json
{
  "source": "004fc25c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc260`](#insn-004fc260)

~~~json
{
  "source": "004fc260",
  "target": "004fc298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc264`](#insn-004fc264)

~~~json
{
  "source": "004fc264",
  "target": "004fc2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc284`](#insn-004fc284)

~~~json
{
  "source": "004fc284",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc290`](#insn-004fc290)

~~~json
{
  "source": "004fc290",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc294`](#insn-004fc294)

~~~json
{
  "source": "004fc294",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc298`](#insn-004fc298)

~~~json
{
  "source": "004fc298",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc29c`](#insn-004fc29c)

~~~json
{
  "source": "004fc29c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2b0`](#insn-004fc2b0)

~~~json
{
  "source": "004fc2b0",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc2b4`](#insn-004fc2b4)

~~~json
{
  "source": "004fc2b4",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2d0`](#insn-004fc2d0)

~~~json
{
  "source": "004fc2d0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc2e0`](#insn-004fc2e0)

~~~json
{
  "source": "004fc2e0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2e8`](#insn-004fc2e8)

~~~json
{
  "source": "004fc2e8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2f4`](#insn-004fc2f4)

~~~json
{
  "source": "004fc2f4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2f8`](#insn-004fc2f8)

~~~json
{
  "source": "004fc2f8",
  "target": "004fc304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc2fc`](#insn-004fc2fc)

~~~json
{
  "source": "004fc2fc",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc300`](#insn-004fc300)

~~~json
{
  "source": "004fc300",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc304`](#insn-004fc304)

~~~json
{
  "source": "004fc304",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc308`](#insn-004fc308)

~~~json
{
  "source": "004fc308",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc318`](#insn-004fc318)

~~~json
{
  "source": "004fc318",
  "target": "00c59860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc320`](#insn-004fc320)

~~~json
{
  "source": "004fc320",
  "target": "004fc428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc324`](#insn-004fc324)

~~~json
{
  "source": "004fc324",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc330`](#insn-004fc330)

~~~json
{
  "source": "004fc330",
  "target": "004fc3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc338`](#insn-004fc338)

~~~json
{
  "source": "004fc338",
  "target": "004fc428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc33c`](#insn-004fc33c)

~~~json
{
  "source": "004fc33c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc354`](#insn-004fc354)

~~~json
{
  "source": "004fc354",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc364`](#insn-004fc364)

~~~json
{
  "source": "004fc364",
  "target": "004fc374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc36c`](#insn-004fc36c)

~~~json
{
  "source": "004fc36c",
  "target": "0053a0b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc370`](#insn-004fc370)

~~~json
{
  "source": "004fc370",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc378`](#insn-004fc378)

~~~json
{
  "source": "004fc378",
  "target": "004fc408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc37c`](#insn-004fc37c)

~~~json
{
  "source": "004fc37c",
  "target": "Stack[-0xd0]",
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
- 参照命令 [`004fc3ac`](#insn-004fc3ac)

~~~json
{
  "source": "004fc3ac",
  "target": "004fc414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3b4`](#insn-004fc3b4)

~~~json
{
  "source": "004fc3b4",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3b8`](#insn-004fc3b8)

~~~json
{
  "source": "004fc3b8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3c4`](#insn-004fc3c4)

~~~json
{
  "source": "004fc3c4",
  "target": "004fc41c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3c8`](#insn-004fc3c8)

~~~json
{
  "source": "004fc3c8",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3d0`](#insn-004fc3d0)

~~~json
{
  "source": "004fc3d0",
  "target": "004fc3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3d4`](#insn-004fc3d4)

~~~json
{
  "source": "004fc3d4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3d8`](#insn-004fc3d8)

~~~json
{
  "source": "004fc3d8",
  "target": "004fc450",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc3e0`](#insn-004fc3e0)

~~~json
{
  "source": "004fc3e0",
  "target": "Stack[-0x130]",
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
- 参照命令 [`004fc3f4`](#insn-004fc3f4)

~~~json
{
  "source": "004fc3f4",
  "target": "004fc460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc400`](#insn-004fc400)

~~~json
{
  "source": "004fc400",
  "target": "00540d7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc404`](#insn-004fc404)

~~~json
{
  "source": "004fc404",
  "target": "004fc460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc40c`](#insn-004fc40c)

~~~json
{
  "source": "004fc40c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc410`](#insn-004fc410)

~~~json
{
  "source": "004fc410",
  "target": "004fc3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc414`](#insn-004fc414)

~~~json
{
  "source": "004fc414",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc418`](#insn-004fc418)

~~~json
{
  "source": "004fc418",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc41c`](#insn-004fc41c)

~~~json
{
  "source": "004fc41c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc424`](#insn-004fc424)

~~~json
{
  "source": "004fc424",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc428`](#insn-004fc428)

~~~json
{
  "source": "004fc428",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc42c`](#insn-004fc42c)

~~~json
{
  "source": "004fc42c",
  "target": "004fc438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc430`](#insn-004fc430)

~~~json
{
  "source": "004fc430",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc434`](#insn-004fc434)

~~~json
{
  "source": "004fc434",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc438`](#insn-004fc438)

~~~json
{
  "source": "004fc438",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc440`](#insn-004fc440)

~~~json
{
  "source": "004fc440",
  "target": "004fc140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc444`](#insn-004fc444)

~~~json
{
  "source": "004fc444",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc448`](#insn-004fc448)

~~~json
{
  "source": "004fc448",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc44c`](#insn-004fc44c)

~~~json
{
  "source": "004fc44c",
  "target": "004fc140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc450`](#insn-004fc450)

~~~json
{
  "source": "004fc450",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc458`](#insn-004fc458)

~~~json
{
  "source": "004fc458",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc460`](#insn-004fc460)

~~~json
{
  "source": "004fc460",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc464`](#insn-004fc464)

~~~json
{
  "source": "004fc464",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc468`](#insn-004fc468)

~~~json
{
  "source": "004fc468",
  "target": "004fc430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc46c`](#insn-004fc46c)

~~~json
{
  "source": "004fc46c",
  "target": "004fc438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc470`](#insn-004fc470)

~~~json
{
  "source": "004fc470",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc474`](#insn-004fc474)

~~~json
{
  "source": "004fc474",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc478`](#insn-004fc478)

~~~json
{
  "source": "004fc478",
  "target": "004fc498",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc47c`](#insn-004fc47c)

~~~json
{
  "source": "004fc47c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc480`](#insn-004fc480)

~~~json
{
  "source": "004fc480",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc484`](#insn-004fc484)

~~~json
{
  "source": "004fc484",
  "target": "004fc5e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc488`](#insn-004fc488)

~~~json
{
  "source": "004fc488",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc48c`](#insn-004fc48c)

~~~json
{
  "source": "004fc48c",
  "target": "00c6a378",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6a378",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc494`](#insn-004fc494)

~~~json
{
  "source": "004fc494",
  "target": "0053aa6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc498`](#insn-004fc498)

~~~json
{
  "source": "004fc498",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc49c`](#insn-004fc49c)

~~~json
{
  "source": "004fc49c",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4a4`](#insn-004fc4a4)

~~~json
{
  "source": "004fc4a4",
  "target": "004fc4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4a8`](#insn-004fc4a8)

~~~json
{
  "source": "004fc4a8",
  "target": "004fc4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4b0`](#insn-004fc4b0)

~~~json
{
  "source": "004fc4b0",
  "target": "004fc4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4bc`](#insn-004fc4bc)

~~~json
{
  "source": "004fc4bc",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4c0`](#insn-004fc4c0)

~~~json
{
  "source": "004fc4c0",
  "target": "00c6a368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6a368",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc4c0`](#insn-004fc4c0)

~~~json
{
  "source": "004fc4c0",
  "target": "00c6a370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6a370",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fc4c4`](#insn-004fc4c4)

~~~json
{
  "source": "004fc4c4",
  "target": "0053aa64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc4c4`](#insn-004fc4c4)

~~~json
{
  "source": "004fc4c4",
  "target": "0053aa68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc4c8`](#insn-004fc4c8)

~~~json
{
  "source": "004fc4c8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4cc`](#insn-004fc4cc)

~~~json
{
  "source": "004fc4cc",
  "target": "004fc01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4d0`](#insn-004fc4d0)

~~~json
{
  "source": "004fc4d0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4d4`](#insn-004fc4d4)

~~~json
{
  "source": "004fc4d4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc4d8`](#insn-004fc4d8)

~~~json
{
  "source": "004fc4d8",
  "target": "004fc01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4e4`](#insn-004fc4e4)

~~~json
{
  "source": "004fc4e4",
  "target": "00539f1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc4e8`](#insn-004fc4e8)

~~~json
{
  "source": "004fc4e8",
  "target": "004fc52c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4f4`](#insn-004fc4f4)

~~~json
{
  "source": "004fc4f4",
  "target": "004fc520",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc4fc`](#insn-004fc4fc)

~~~json
{
  "source": "004fc4fc",
  "target": "004fc50c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc508`](#insn-004fc508)

~~~json
{
  "source": "004fc508",
  "target": "004fc520",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc510`](#insn-004fc510)

~~~json
{
  "source": "004fc510",
  "target": "004fc500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc518`](#insn-004fc518)

~~~json
{
  "source": "004fc518",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc51c`](#insn-004fc51c)

~~~json
{
  "source": "004fc51c",
  "target": "004fc500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc528`](#insn-004fc528)

~~~json
{
  "source": "004fc528",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc52c`](#insn-004fc52c)

~~~json
{
  "source": "004fc52c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc530`](#insn-004fc530)

~~~json
{
  "source": "004fc530",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc570`](#insn-004fc570)

~~~json
{
  "source": "004fc570",
  "target": "00545c3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc574`](#insn-004fc574)

~~~json
{
  "source": "004fc574",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc57c`](#insn-004fc57c)

~~~json
{
  "source": "004fc57c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc584`](#insn-004fc584)

~~~json
{
  "source": "004fc584",
  "target": "004fc6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc58c`](#insn-004fc58c)

~~~json
{
  "source": "004fc58c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc590`](#insn-004fc590)

~~~json
{
  "source": "004fc590",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc594`](#insn-004fc594)

~~~json
{
  "source": "004fc594",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc598`](#insn-004fc598)

~~~json
{
  "source": "004fc598",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc59c`](#insn-004fc59c)

~~~json
{
  "source": "004fc59c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5a0`](#insn-004fc5a0)

~~~json
{
  "source": "004fc5a0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5a8`](#insn-004fc5a8)

~~~json
{
  "source": "004fc5a8",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5b0`](#insn-004fc5b0)

~~~json
{
  "source": "004fc5b0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5b8`](#insn-004fc5b8)

~~~json
{
  "source": "004fc5b8",
  "target": "004fc6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5c0`](#insn-004fc5c0)

~~~json
{
  "source": "004fc5c0",
  "target": "0043b764",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc5c4`](#insn-004fc5c4)

~~~json
{
  "source": "004fc5c4",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5cc`](#insn-004fc5cc)

~~~json
{
  "source": "004fc5cc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5d4`](#insn-004fc5d4)

~~~json
{
  "source": "004fc5d4",
  "target": "004fc6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5e0`](#insn-004fc5e0)

~~~json
{
  "source": "004fc5e0",
  "target": "0043b764",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc5e4`](#insn-004fc5e4)

~~~json
{
  "source": "004fc5e4",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5ec`](#insn-004fc5ec)

~~~json
{
  "source": "004fc5ec",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5f4`](#insn-004fc5f4)

~~~json
{
  "source": "004fc5f4",
  "target": "004fc6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fc5f8`](#insn-004fc5f8)

~~~json
{
  "source": "004fc5f8",
  "target": "00459d74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fc6d8`](#insn-004fc6d8)

~~~json
{
  "source": "004fc6d8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
