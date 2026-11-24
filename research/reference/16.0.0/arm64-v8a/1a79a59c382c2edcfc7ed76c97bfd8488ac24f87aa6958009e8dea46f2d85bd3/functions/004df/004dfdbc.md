# 004dfdbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004bcf24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0009.md#compare-e120f8ff33580b11b4f4e26528b84cab)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004dfdfc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004dfdfc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0009.md#compare-27f90b113aafaf47693d401e87defc4c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004dfdbc",
  "name": "_ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE",
  "size": 1432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41bc9824e53a43b165bfeff373519f1e5dc34093cb47d3f0f6087333d8503940",
  "source_text_sha256": "41bc9824e53a43b165bfeff373519f1e5dc34093cb47d3f0f6087333d8503940",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004dfdbc",
        "004e034f"
      ],
      [
        "004e03e4",
        "004e03e7"
      ]
    ],
    "bytes_sha256": "5c397b3ef0c4f2239f8634c1dddb7ff5ce38b53991137641b44144a3ab943a51",
    "instruction_count": 358,
    "instruction_bytes": 1432,
    "body_bytes": 1432,
    "indirect": 3,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58f20](../00c58/00c58f20.md)

## 呼び出し先

- [0043dd98](../0043d/0043dd98.md)
- [004aec24](../004ae/004aec24.md)
- [004b8774](../004b8/004b8774.md)
- [004b9bf8](../004b9/004b9bf8.md)
- [005408e0](../00540/005408e0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57af0](../00c57/00c57af0.md)
- [00c57b10](../00c57/00c57b10.md)
- [00c57c90](../00c57/00c57c90.md)
- [00c58260](../00c58/00c58260.md)
- [00c586c0](../00c58/00c586c0.md)
- [00c586d0](../00c58/00c586d0.md)
- [00c58720](../00c58/00c58720.md)
- [00c58740](../00c58/00c58740.md)
- [00c58840](../00c58/00c58840.md)
- [00c588a0](../00c58/00c588a0.md)
- [00c588b0](../00c58/00c588b0.md)
- [00c588c0](../00c58/00c588c0.md)
- [0112a058](../0112a/0112a058.md)

## 関連文字列（未確認候補）

~~~text
"Modular_Reducer: Never initalized"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7948 bytes

~~~c

void _ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE
               (undefined8 *param_1,long *param_2,long *param_3)

{
  long lVar1;
  long lVar2;
  long lVar3;
  int *piVar4;
  void *pvVar5;
  void *pvVar6;
  int iVar7;
  undefined8 uVar8;
  long lVar9;
  size_t sVar10;
  long lVar11;
  long lVar12;
  ulong uVar13;
  ulong uVar14;
  long lVar15;
  void *local_c0;
  void *local_b8;
  long local_b0;
  undefined4 local_a8;
  void *local_a0;
  void *pvStack_98;
  long local_90;
  int local_88;
  int *local_78;
  int *local_70;
  long local_68;
  undefined4 local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  if (param_2[0xc] == 0) {
    uVar8 = __cxa_allocate_exception(0x20);
    FUN_0043dd98(&local_78,"Modular_Reducer: Never initalized");
    FUN_004aec24(uVar8,&local_78);
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar8,PTR__ZTIN5Botan13Invalid_StateE_00c9a948,FUN_00535828);
    }
  }
  else {
    lVar9 = *param_3;
    lVar12 = param_3[1];
    lVar11 = lVar12 - lVar9;
    lVar15 = lVar11 >> 2;
    lVar1 = lVar15;
    while ((lVar11 != 0 && (*(int *)(lVar9 + -4 + lVar1 * 4) == 0))) {
      lVar1 = lVar1 + -1;
      lVar11 = lVar1;
    }
    lVar2 = param_2[1] - *param_2;
    lVar11 = lVar2 >> 2;
    if (lVar2 != 0) {
      do {
        if (*(int *)(*param_2 + -4 + lVar11 * 4) != 0) break;
        lVar11 = lVar11 + -1;
      } while (lVar11 != 0);
    }
    iVar7 = FUN_004b8774(lVar9,lVar1);
    if (iVar7 < 0) {
      if ((int)param_3[3] == 0) {
        if (*(long *)(lVar3 + 0x28) == local_58) {
          _ZN5BotanplERKNS_6BigIntES2_(param_1,param_3,param_2);
          return;
        }
      }
      else if (*(long *)(lVar3 + 0x28) == local_58) {
        _ZN5Botan6BigIntC2ERKS0_(param_1,param_3);
        return;
      }
    }
    else {
      if (lVar12 != lVar9) {
        do {
          if (*(int *)(lVar9 + -4 + lVar15 * 4) != 0) break;
          lVar15 = lVar15 + -1;
        } while (lVar15 != 0);
      }
      lVar1 = param_2[5] - param_2[4];
      lVar12 = lVar1 >> 2;
      if (lVar1 != 0) {
        do {
          if (*(int *)(param_2[4] + -4 + lVar12 * 4) != 0) break;
          lVar12 = lVar12 + -1;
        } while (lVar12 != 0);
      }
      iVar7 = FUN_004b8774(lVar9,lVar15);
      if (iVar7 < 0) {
        _ZN5Botan6BigIntC2ERKS0_(&local_78,param_3);
        local_60 = 1;
        uVar14 = param_2[0xc] * 0x20 - 0x20;
        if (uVar14 != 0) {
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          lVar12 = (long)local_70 - (long)local_78;
          while ((lVar12 != 0 && (local_78[lVar9 + -1] == 0))) {
            lVar9 = lVar9 + -1;
            lVar12 = lVar9;
          }
          FUN_004b9bf8(local_78,lVar9,uVar14 >> 5,0);
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          piVar4 = local_78;
          if ((long)local_70 - (long)local_78 == 0) {
joined_r0x004dffc8:
            do {
              if (lVar9 == 0) goto LAB_004dffdc;
              if (*piVar4 != 0) goto LAB_004dffe4;
              lVar9 = lVar9 + -1;
              piVar4 = piVar4 + 1;
            } while( true );
          }
          do {
            if (local_78[lVar9 + -1] != 0) goto joined_r0x004dffc8;
            lVar9 = lVar9 + -1;
          } while (lVar9 != 0);
LAB_004dffdc:
          local_60 = 1;
        }
LAB_004dffe4:
        _ZN5Botan6BigIntmLERKS0_(&local_78,param_2 + 8);
        uVar14 = param_2[0xc] * 0x20 + 0x20;
        if (uVar14 != 0) {
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          lVar12 = (long)local_70 - (long)local_78;
          while ((lVar12 != 0 && (local_78[lVar9 + -1] == 0))) {
            lVar9 = lVar9 + -1;
            lVar12 = lVar9;
          }
          FUN_004b9bf8(local_78,lVar9,uVar14 >> 5,0);
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          piVar4 = local_78;
          if ((long)local_70 - (long)local_78 == 0) {
joined_r0x004e0058:
            do {
              if (lVar9 == 0) goto LAB_004e006c;
              if (*piVar4 != 0) goto LAB_004e0074;
              lVar9 = lVar9 + -1;
              piVar4 = piVar4 + 1;
            } while( true );
          }
          do {
            if (local_78[lVar9 + -1] != 0) goto joined_r0x004e0058;
            lVar9 = lVar9 + -1;
          } while (lVar9 != 0);
LAB_004e006c:
          local_60 = 1;
        }
LAB_004e0074:
        _ZN5Botan6BigIntmLERKS0_(&local_78,param_2);
        uVar14 = param_2[0xc] * 0x20 + 0x20;
        if (uVar14 == 0) {
          if ((long)local_70 - (long)local_78 != 0) {
            memset(local_78,0,(long)local_70 - (long)local_78);
          }
        }
        else {
          uVar14 = uVar14 >> 5;
          uVar13 = (long)local_70 - (long)local_78 >> 2;
          if (uVar14 < uVar13) {
            lVar9 = uVar13 - (uVar14 + 1);
            if ((lVar9 != 0) && (sVar10 = lVar9 * 4, sVar10 != 0)) {
              memset(local_78 + uVar14 + 1,0,sVar10);
            }
            local_78[uVar14] = 0;
          }
        }
        _ZN5Botan6BigIntC2ERKS0_(&local_a0,param_3);
        local_88 = 1;
        uVar14 = param_2[0xc] * 0x20 + 0x20;
        if (uVar14 == 0) {
          if (pvStack_98 != local_a0) {
            memset(local_a0,0,(long)pvStack_98 - (long)local_a0);
          }
        }
        else {
          uVar13 = (long)pvStack_98 - (long)local_a0 >> 2;
          uVar14 = uVar14 >> 5;
          if (uVar14 < uVar13) {
            lVar9 = uVar13 - (uVar14 + 1);
            if ((lVar9 != 0) && (sVar10 = lVar9 * 4, sVar10 != 0)) {
              memset((void *)((long)local_a0 + (uVar14 + 1) * 4),0,sVar10);
            }
            *(undefined4 *)((long)local_a0 + uVar14 * 4) = 0;
          }
        }
        _ZN5Botan6BigIntmIERKS0_(&local_a0,&local_78);
        if (local_88 == 0) {
          local_b8 = (void *)0x0;
          local_b0 = 0;
          local_c0 = (void *)0x0;
          uVar13 = param_2[0xc] + 1U & 0x7ffffffffffffff;
          uVar14 = uVar13 + 1;
          local_a8 = 1;
          lVar9 = 0;
          if ((uVar14 & 7) != 0) {
            lVar9 = 8 - (uVar14 & 7);
          }
          FUN_005408e0(&local_c0,lVar9 + uVar14);
          lVar9 = uVar13 * 4;
          *(uint *)((long)local_c0 + lVar9) = *(uint *)((long)local_c0 + lVar9) | 1;
          _ZN5Botan6BigIntpLERKS0_(&local_a0,&local_c0);
          pvVar5 = local_c0;
          if (local_c0 != (void *)0x0) {
            local_b8 = local_c0;
            (*(code *)PTR_memset_00c67338)(local_c0,0,local_b0 - (long)local_c0);
            free(pvVar5);
          }
        }
        while (iVar7 = _ZNK5Botan6BigInt3cmpERKS0_b(&local_a0,param_2,1), lVar9 = local_90,
              pvVar6 = pvStack_98, pvVar5 = local_a0, -1 < iVar7) {
          _ZN5Botan6BigIntmIERKS0_(&local_a0,param_2);
        }
        if ((int)param_3[3] == 1) {
          local_a0 = (void *)0x0;
          pvStack_98 = (void *)0x0;
          local_90 = 0;
          param_1[2] = lVar9;
          param_1[1] = pvVar6;
          *param_1 = pvVar5;
          *(int *)(param_1 + 3) = local_88;
        }
        else {
          _ZN5BotanmiERKNS_6BigIntES2_(param_1,param_2,&local_a0);
          pvVar5 = local_a0;
          if (local_a0 != (void *)0x0) {
            pvStack_98 = local_a0;
            (*(code *)PTR_memset_00c67338)(local_a0,0,local_90 - (long)local_a0);
            free(pvVar5);
          }
        }
        if (local_78 != (int *)0x0) {
          local_70 = local_78;
          (*(code *)PTR_memset_00c67338)(local_78,0,local_68 - (long)local_78);
          free(local_78);
        }
        if (*(long *)(lVar3 + 0x28) == local_58) {
          return;
        }
      }
      else if (*(long *)(lVar3 + 0x28) == local_58) {
        _ZN5BotanrmERKNS_6BigIntES2_(param_1,param_3,param_2);
        return;
      }
    }
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004dfdbc"></a> `004dfdbc` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004dfdc0"></a> `004dfdc0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dfdc4"></a> `004dfdc4` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dfdc8"></a> `004dfdc8` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dfdcc"></a> `004dfdcc` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dfdd0"></a> `004dfdd0` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dfdd4"></a> `004dfdd4` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004dfdd8"></a> `004dfdd8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004dfddc"></a> `004dfddc` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dfde0"></a> `004dfde0` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dfde4"></a> `004dfde4` | `09 30 40 f9` | ldr x9,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-004dfde8"></a> `004dfde8` | `89 28 00 b4` | cbz x9,0x004e02f8 | `CONDITIONAL_JUMP`
<a id="insn-004dfdec"></a> `004dfdec` | `36 68 40 a9` | ldp x22,x26,[x1] | `FALL_THROUGH`
<a id="insn-004dfdf0"></a> `004dfdf0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004dfdf4"></a> `004dfdf4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-004dfdf8"></a> `004dfdf8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004dfdfc"></a> `004dfdfc` | `48 03 16 eb` | subs x8,x26,x22 | `FALL_THROUGH`
<a id="insn-004dfe00"></a> `004dfe00` | `d9 12 00 d1` | sub x25,x22,#0x4 | `FALL_THROUGH`
<a id="insn-004dfe04"></a> `004dfe04` | `17 fd 42 93` | asr x23,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004dfe08"></a> `004dfe08` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-004dfe0c"></a> `004dfe0c` | `c0 00 00 54` | b.eq 0x004dfe24 | `CONDITIONAL_JUMP`
<a id="insn-004dfe10"></a> `004dfe10` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-004dfe14"></a> `004dfe14` | `28 7b 61 b8` | ldr w8,[x25, x1, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfe18"></a> `004dfe18` | `68 00 00 35` | cbnz w8,0x004dfe24 | `CONDITIONAL_JUMP`
<a id="insn-004dfe1c"></a> `004dfe1c` | `21 04 00 f1` | subs x1,x1,#0x1 | `FALL_THROUGH`
<a id="insn-004dfe20"></a> `004dfe20` | `a1 ff ff 54` | b.ne 0x004dfe14 | `CONDITIONAL_JUMP`
<a id="insn-004dfe24"></a> `004dfe24` | `82 22 40 a9` | ldp x2,x8,[x20] | `FALL_THROUGH`
<a id="insn-004dfe28"></a> `004dfe28` | `08 01 02 eb` | subs x8,x8,x2 | `FALL_THROUGH`
<a id="insn-004dfe2c"></a> `004dfe2c` | `03 fd 42 93` | asr x3,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004dfe30"></a> `004dfe30` | `c0 00 00 54` | b.eq 0x004dfe48 | `CONDITIONAL_JUMP`
<a id="insn-004dfe34"></a> `004dfe34` | `48 10 00 d1` | sub x8,x2,#0x4 | `FALL_THROUGH`
<a id="insn-004dfe38"></a> `004dfe38` | `09 79 63 b8` | ldr w9,[x8, x3, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfe3c"></a> `004dfe3c` | `69 00 00 35` | cbnz w9,0x004dfe48 | `CONDITIONAL_JUMP`
<a id="insn-004dfe40"></a> `004dfe40` | `63 04 00 f1` | subs x3,x3,#0x1 | `FALL_THROUGH`
<a id="insn-004dfe44"></a> `004dfe44` | `a1 ff ff 54` | b.ne 0x004dfe38 | `CONDITIONAL_JUMP`
<a id="insn-004dfe48"></a> `004dfe48` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004dfe4c"></a> `004dfe4c` | `4a 62 ff 97` | bl 0x004b8774 | `UNCONDITIONAL_CALL`
<a id="insn-004dfe50"></a> `004dfe50` | `40 04 f8 37` | tbnz w0,#0x1f,0x004dfed8 | `CONDITIONAL_JUMP`
<a id="insn-004dfe54"></a> `004dfe54` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-004dfe58"></a> `004dfe58` | `a0 00 00 54` | b.eq 0x004dfe6c | `CONDITIONAL_JUMP`
<a id="insn-004dfe5c"></a> `004dfe5c` | `28 7b 77 b8` | ldr w8,[x25, x23, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfe60"></a> `004dfe60` | `68 00 00 35` | cbnz w8,0x004dfe6c | `CONDITIONAL_JUMP`
<a id="insn-004dfe64"></a> `004dfe64` | `f7 06 00 f1` | subs x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-004dfe68"></a> `004dfe68` | `a1 ff ff 54` | b.ne 0x004dfe5c | `CONDITIONAL_JUMP`
<a id="insn-004dfe6c"></a> `004dfe6c` | `82 22 42 a9` | ldp x2,x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-004dfe70"></a> `004dfe70` | `08 01 02 eb` | subs x8,x8,x2 | `FALL_THROUGH`
<a id="insn-004dfe74"></a> `004dfe74` | `03 fd 42 93` | asr x3,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004dfe78"></a> `004dfe78` | `c0 00 00 54` | b.eq 0x004dfe90 | `CONDITIONAL_JUMP`
<a id="insn-004dfe7c"></a> `004dfe7c` | `48 10 00 d1` | sub x8,x2,#0x4 | `FALL_THROUGH`
<a id="insn-004dfe80"></a> `004dfe80` | `09 79 63 b8` | ldr w9,[x8, x3, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfe84"></a> `004dfe84` | `69 00 00 35` | cbnz w9,0x004dfe90 | `CONDITIONAL_JUMP`
<a id="insn-004dfe88"></a> `004dfe88` | `63 04 00 f1` | subs x3,x3,#0x1 | `FALL_THROUGH`
<a id="insn-004dfe8c"></a> `004dfe8c` | `a1 ff ff 54` | b.ne 0x004dfe80 | `CONDITIONAL_JUMP`
<a id="insn-004dfe90"></a> `004dfe90` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004dfe94"></a> `004dfe94` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-004dfe98"></a> `004dfe98` | `37 62 ff 97` | bl 0x004b8774 | `UNCONDITIONAL_CALL`
<a id="insn-004dfe9c"></a> `004dfe9c` | `c0 03 f8 37` | tbnz w0,#0x1f,0x004dff14 | `CONDITIONAL_JUMP`
<a id="insn-004dfea0"></a> `004dfea0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dfea4"></a> `004dfea4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dfea8"></a> `004dfea8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004dfeac"></a> `004dfeac` | `c1 29 00 54` | b.ne 0x004e03e4 | `CONDITIONAL_JUMP`
<a id="insn-004dfeb0"></a> `004dfeb0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004dfeb4"></a> `004dfeb4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004dfeb8"></a> `004dfeb8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004dfebc"></a> `004dfebc` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dfec0"></a> `004dfec0` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dfec4"></a> `004dfec4` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dfec8"></a> `004dfec8` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dfecc"></a> `004dfecc` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dfed0"></a> `004dfed0` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004dfed4"></a> `004dfed4` | `73 e2 1d 14` | b 0x00c588a0 | `CALL_TERMINATOR`
<a id="insn-004dfed8"></a> `004dfed8` | `a8 1a 40 b9` | ldr w8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-004dfedc"></a> `004dfedc` | `a8 05 00 34` | cbz w8,0x004dff90 | `CONDITIONAL_JUMP`
<a id="insn-004dfee0"></a> `004dfee0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dfee4"></a> `004dfee4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dfee8"></a> `004dfee8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004dfeec"></a> `004dfeec` | `c1 27 00 54` | b.ne 0x004e03e4 | `CONDITIONAL_JUMP`
<a id="insn-004dfef0"></a> `004dfef0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004dfef4"></a> `004dfef4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004dfef8"></a> `004dfef8` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dfefc"></a> `004dfefc` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dff00"></a> `004dff00` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dff04"></a> `004dff04` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dff08"></a> `004dff08` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dff0c"></a> `004dff0c` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004dff10"></a> `004dff10` | `0c e2 1d 14` | b 0x00c58740 | `CALL_TERMINATOR`
<a id="insn-004dff14"></a> `004dff14` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004dff18"></a> `004dff18` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004dff1c"></a> `004dff1c` | `09 e2 1d 94` | bl 0x00c58740 | `UNCONDITIONAL_CALL`
<a id="insn-004dff20"></a> `004dff20` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004dff24"></a> `004dff24` | `a0 a7 7d a9` | ldp x0,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004dff28"></a> `004dff28` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-004dff2c"></a> `004dff2c` | `08 e9 7b d3` | lsl x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004dff30"></a> `004dff30` | `aa 03 1f b8` | stur w10,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004dff34"></a> `004dff34` | `08 81 00 f1` | subs x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-004dff38"></a> `004dff38` | `60 05 00 54` | b.eq 0x004dffe4 | `CONDITIONAL_JUMP`
<a id="insn-004dff3c"></a> `004dff3c` | `29 01 00 eb` | subs x9,x9,x0 | `FALL_THROUGH`
<a id="insn-004dff40"></a> `004dff40` | `02 fd 45 d3` | lsr x2,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004dff44"></a> `004dff44` | `21 fd 42 93` | asr x1,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004dff48"></a> `004dff48` | `c0 00 00 54` | b.eq 0x004dff60 | `CONDITIONAL_JUMP`
<a id="insn-004dff4c"></a> `004dff4c` | `08 10 00 d1` | sub x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-004dff50"></a> `004dff50` | `09 79 61 b8` | ldr w9,[x8, x1, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dff54"></a> `004dff54` | `69 00 00 35` | cbnz w9,0x004dff60 | `CONDITIONAL_JUMP`
<a id="insn-004dff58"></a> `004dff58` | `21 04 00 f1` | subs x1,x1,#0x1 | `FALL_THROUGH`
<a id="insn-004dff5c"></a> `004dff5c` | `a1 ff ff 54` | b.ne 0x004dff50 | `CONDITIONAL_JUMP`
<a id="insn-004dff60"></a> `004dff60` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-004dff64"></a> `004dff64` | `25 67 ff 97` | bl 0x004b9bf8 | `UNCONDITIONAL_CALL`
<a id="insn-004dff68"></a> `004dff68` | `a8 a7 7d a9` | ldp x8,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004dff6c"></a> `004dff6c` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004dff70"></a> `004dff70` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004dff74"></a> `004dff74` | `a0 02 00 54` | b.eq 0x004dffc8 | `CONDITIONAL_JUMP`
<a id="insn-004dff78"></a> `004dff78` | `0a 11 00 d1` | sub x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-004dff7c"></a> `004dff7c` | `4b 79 69 b8` | ldr w11,[x10, x9, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dff80"></a> `004dff80` | `4b 02 00 35` | cbnz w11,0x004dffc8 | `CONDITIONAL_JUMP`
<a id="insn-004dff84"></a> `004dff84` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004dff88"></a> `004dff88` | `a1 ff ff 54` | b.ne 0x004dff7c | `CONDITIONAL_JUMP`
<a id="insn-004dff8c"></a> `004dff8c` | `14 00 00 14` | b 0x004dffdc | `UNCONDITIONAL_JUMP`
<a id="insn-004dff90"></a> `004dff90` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dff94"></a> `004dff94` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dff98"></a> `004dff98` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004dff9c"></a> `004dff9c` | `41 22 00 54` | b.ne 0x004e03e4 | `CONDITIONAL_JUMP`
<a id="insn-004dffa0"></a> `004dffa0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004dffa4"></a> `004dffa4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004dffa8"></a> `004dffa8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004dffac"></a> `004dffac` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dffb0"></a> `004dffb0` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dffb4"></a> `004dffb4` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dffb8"></a> `004dffb8` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dffbc"></a> `004dffbc` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dffc0"></a> `004dffc0` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004dffc4"></a> `004dffc4` | `3b e2 1d 14` | b 0x00c588b0 | `CALL_TERMINATOR`
<a id="insn-004dffc8"></a> `004dffc8` | `a9 00 00 b4` | cbz x9,0x004dffdc | `CONDITIONAL_JUMP`
<a id="insn-004dffcc"></a> `004dffcc` | `0a 45 40 b8` | ldr w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-004dffd0"></a> `004dffd0` | `aa 00 00 35` | cbnz w10,0x004dffe4 | `CONDITIONAL_JUMP`
<a id="insn-004dffd4"></a> `004dffd4` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004dffd8"></a> `004dffd8` | `a1 ff ff 54` | b.ne 0x004dffcc | `CONDITIONAL_JUMP`
<a id="insn-004dffdc"></a> `004dffdc` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-004dffe0"></a> `004dffe0` | `a8 03 1f b8` | stur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004dffe4"></a> `004dffe4` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004dffe8"></a> `004dffe8` | `81 02 01 91` | add x1,x20,#0x40 | `FALL_THROUGH`
<a id="insn-004dffec"></a> `004dffec` | `b5 e1 1d 94` | bl 0x00c586c0 | `UNCONDITIONAL_CALL`
<a id="insn-004dfff0"></a> `004dfff0` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004dfff4"></a> `004dfff4` | `08 e9 7b d3` | lsl x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004dfff8"></a> `004dfff8` | `08 81 00 b1` | adds x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-004dfffc"></a> `004dfffc` | `c0 03 00 54` | b.eq 0x004e0074 | `CONDITIONAL_JUMP`
<a id="insn-004e0000"></a> `004e0000` | `a0 a7 7d a9` | ldp x0,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e0004"></a> `004e0004` | `02 fd 45 d3` | lsr x2,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004e0008"></a> `004e0008` | `29 01 00 eb` | subs x9,x9,x0 | `FALL_THROUGH`
<a id="insn-004e000c"></a> `004e000c` | `21 fd 42 93` | asr x1,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e0010"></a> `004e0010` | `c0 00 00 54` | b.eq 0x004e0028 | `CONDITIONAL_JUMP`
<a id="insn-004e0014"></a> `004e0014` | `08 10 00 d1` | sub x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-004e0018"></a> `004e0018` | `09 79 61 b8` | ldr w9,[x8, x1, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e001c"></a> `004e001c` | `69 00 00 35` | cbnz w9,0x004e0028 | `CONDITIONAL_JUMP`
<a id="insn-004e0020"></a> `004e0020` | `21 04 00 f1` | subs x1,x1,#0x1 | `FALL_THROUGH`
<a id="insn-004e0024"></a> `004e0024` | `a1 ff ff 54` | b.ne 0x004e0018 | `CONDITIONAL_JUMP`
<a id="insn-004e0028"></a> `004e0028` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-004e002c"></a> `004e002c` | `f3 66 ff 97` | bl 0x004b9bf8 | `UNCONDITIONAL_CALL`
<a id="insn-004e0030"></a> `004e0030` | `a8 a7 7d a9` | ldp x8,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e0034"></a> `004e0034` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004e0038"></a> `004e0038` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e003c"></a> `004e003c` | `e0 00 00 54` | b.eq 0x004e0058 | `CONDITIONAL_JUMP`
<a id="insn-004e0040"></a> `004e0040` | `0a 11 00 d1` | sub x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-004e0044"></a> `004e0044` | `4b 79 69 b8` | ldr w11,[x10, x9, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e0048"></a> `004e0048` | `8b 00 00 35` | cbnz w11,0x004e0058 | `CONDITIONAL_JUMP`
<a id="insn-004e004c"></a> `004e004c` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004e0050"></a> `004e0050` | `a1 ff ff 54` | b.ne 0x004e0044 | `CONDITIONAL_JUMP`
<a id="insn-004e0054"></a> `004e0054` | `06 00 00 14` | b 0x004e006c | `UNCONDITIONAL_JUMP`
<a id="insn-004e0058"></a> `004e0058` | `a9 00 00 b4` | cbz x9,0x004e006c | `CONDITIONAL_JUMP`
<a id="insn-004e005c"></a> `004e005c` | `0a 45 40 b8` | ldr w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-004e0060"></a> `004e0060` | `aa 00 00 35` | cbnz w10,0x004e0074 | `CONDITIONAL_JUMP`
<a id="insn-004e0064"></a> `004e0064` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004e0068"></a> `004e0068` | `a1 ff ff 54` | b.ne 0x004e005c | `CONDITIONAL_JUMP`
<a id="insn-004e006c"></a> `004e006c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-004e0070"></a> `004e0070` | `a8 03 1f b8` | stur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004e0074"></a> `004e0074` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e0078"></a> `004e0078` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004e007c"></a> `004e007c` | `91 e1 1d 94` | bl 0x00c586c0 | `UNCONDITIONAL_CALL`
<a id="insn-004e0080"></a> `004e0080` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004e0084"></a> `004e0084` | `a9 03 5e f8` | ldur x9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004e0088"></a> `004e0088` | `08 e9 7b d3` | lsl x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004e008c"></a> `004e008c` | `0a 81 00 b1` | adds x10,x8,#0x20 | `FALL_THROUGH`
<a id="insn-004e0090"></a> `004e0090` | `40 02 00 54` | b.eq 0x004e00d8 | `CONDITIONAL_JUMP`
<a id="insn-004e0094"></a> `004e0094` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e0098"></a> `004e0098` | `56 fd 45 d3` | lsr x22,x10,#0x5 | `FALL_THROUGH`
<a id="insn-004e009c"></a> `004e009c` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004e00a0"></a> `004e00a0` | `2a fd 42 93` | asr x10,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e00a4"></a> `004e00a4` | `df 02 0a eb` | cmp x22,x10 | `FALL_THROUGH`
<a id="insn-004e00a8"></a> `004e00a8` | `22 02 00 54` | b.cs 0x004e00ec | `CONDITIONAL_JUMP`
<a id="insn-004e00ac"></a> `004e00ac` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-004e00b0"></a> `004e00b0` | `4a 01 09 eb` | subs x10,x10,x9 | `FALL_THROUGH`
<a id="insn-004e00b4"></a> `004e00b4` | `e0 00 00 54` | b.eq 0x004e00d0 | `CONDITIONAL_JUMP`
<a id="insn-004e00b8"></a> `004e00b8` | `42 f5 7e d3` | lsl x2,x10,#0x2 | `FALL_THROUGH`
<a id="insn-004e00bc"></a> `004e00bc` | `a2 00 00 b4` | cbz x2,0x004e00d0 | `CONDITIONAL_JUMP`
<a id="insn-004e00c0"></a> `004e00c0` | `00 09 09 8b` | add x0,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-004e00c4"></a> `004e00c4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e00c8"></a> `004e00c8` | `f2 de 1d 94` | bl 0x00c57c90 | `UNCONDITIONAL_CALL`
<a id="insn-004e00cc"></a> `004e00cc` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e00d0"></a> `004e00d0` | `1f 79 36 b8` | str wzr,[x8, x22, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e00d4"></a> `004e00d4` | `06 00 00 14` | b 0x004e00ec | `UNCONDITIONAL_JUMP`
<a id="insn-004e00d8"></a> `004e00d8` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e00dc"></a> `004e00dc` | `22 01 00 eb` | subs x2,x9,x0 | `FALL_THROUGH`
<a id="insn-004e00e0"></a> `004e00e0` | `60 00 00 54` | b.eq 0x004e00ec | `CONDITIONAL_JUMP`
<a id="insn-004e00e4"></a> `004e00e4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e00e8"></a> `004e00e8` | `ea de 1d 94` | bl 0x00c57c90 | `UNCONDITIONAL_CALL`
<a id="insn-004e00ec"></a> `004e00ec` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e00f0"></a> `004e00f0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004e00f4"></a> `004e00f4` | `93 e1 1d 94` | bl 0x00c58740 | `UNCONDITIONAL_CALL`
<a id="insn-004e00f8"></a> `004e00f8` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004e00fc"></a> `004e00fc` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-004e0100"></a> `004e0100` | `eb 3b 00 b9` | str w11,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004e0104"></a> `004e0104` | `09 e9 7b d3` | lsl x9,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004e0108"></a> `004e0108` | `e0 23 42 a9` | ldp x0,x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e010c"></a> `004e010c` | `2a 81 00 b1` | adds x10,x9,#0x20 | `FALL_THROUGH`
<a id="insn-004e0110"></a> `004e0110` | `02 01 00 cb` | sub x2,x8,x0 | `FALL_THROUGH`
<a id="insn-004e0114"></a> `004e0114` | `00 02 00 54` | b.eq 0x004e0154 | `CONDITIONAL_JUMP`
<a id="insn-004e0118"></a> `004e0118` | `49 fc 42 93` | asr x9,x2,#0x2 | `FALL_THROUGH`
<a id="insn-004e011c"></a> `004e011c` | `56 fd 45 d3` | lsr x22,x10,#0x5 | `FALL_THROUGH`
<a id="insn-004e0120"></a> `004e0120` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-004e0124"></a> `004e0124` | `02 02 00 54` | b.cs 0x004e0164 | `CONDITIONAL_JUMP`
<a id="insn-004e0128"></a> `004e0128` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-004e012c"></a> `004e012c` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004e0130"></a> `004e0130` | `e0 00 00 54` | b.eq 0x004e014c | `CONDITIONAL_JUMP`
<a id="insn-004e0134"></a> `004e0134` | `22 f5 7e d3` | lsl x2,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e0138"></a> `004e0138` | `a2 00 00 b4` | cbz x2,0x004e014c | `CONDITIONAL_JUMP`
<a id="insn-004e013c"></a> `004e013c` | `00 08 08 8b` | add x0,x0,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-004e0140"></a> `004e0140` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e0144"></a> `004e0144` | `d3 de 1d 94` | bl 0x00c57c90 | `UNCONDITIONAL_CALL`
<a id="insn-004e0148"></a> `004e0148` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e014c"></a> `004e014c` | `1f 78 36 b8` | str wzr,[x0, x22, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e0150"></a> `004e0150` | `05 00 00 14` | b 0x004e0164 | `UNCONDITIONAL_JUMP`
<a id="insn-004e0154"></a> `004e0154` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-004e0158"></a> `004e0158` | `60 00 00 54` | b.eq 0x004e0164 | `CONDITIONAL_JUMP`
<a id="insn-004e015c"></a> `004e015c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e0160"></a> `004e0160` | `cc de 1d 94` | bl 0x00c57c90 | `UNCONDITIONAL_CALL`
<a id="insn-004e0164"></a> `004e0164` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e0168"></a> `004e0168` | `a1 a3 00 d1` | sub x1,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e016c"></a> `004e016c` | `b5 e1 1d 94` | bl 0x00c58840 | `UNCONDITIONAL_CALL`
<a id="insn-004e0170"></a> `004e0170` | `e8 3b 40 b9` | ldr w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004e0174"></a> `004e0174` | `a8 04 00 35` | cbnz w8,0x004e0208 | `CONDITIONAL_JUMP`
<a id="insn-004e0178"></a> `004e0178` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004e017c"></a> `004e017c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-004e0180"></a> `004e0180` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004e0184"></a> `004e0184` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-004e0188"></a> `004e0188` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004e018c"></a> `004e018c` | `16 e9 40 92` | and x22,x8,#0x7ffffffffffffff | `FALL_THROUGH`
<a id="insn-004e0190"></a> `004e0190` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-004e0194"></a> `004e0194` | `0a 09 40 f2` | ands x10,x8,#0x7 | `FALL_THROUGH`
<a id="insn-004e0198"></a> `004e0198` | `29 01 0a cb` | sub x9,x9,x10 | `FALL_THROUGH`
<a id="insn-004e019c"></a> `004e019c` | `1f 09 40 f2` | tst x8,#0x7 | `FALL_THROUGH`
<a id="insn-004e01a0"></a> `004e01a0` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-004e01a4"></a> `004e01a4` | `ea 1b 00 b9` | str w10,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004e01a8"></a> `004e01a8` | `e9 03 89 9a` | csel x9,xzr,x9,eq | `FALL_THROUGH`
<a id="insn-004e01ac"></a> `004e01ac` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004e01b0"></a> `004e01b0` | `21 01 08 8b` | add x1,x9,x8 | `FALL_THROUGH`
<a id="insn-004e01b4"></a> `004e01b4` | `cb 81 01 94` | bl 0x005408e0 | `UNCONDITIONAL_CALL`
<a id="insn-004e01b8"></a> `004e01b8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-004e01bc"></a> `004e01bc` | `c9 f6 7e d3` | lsl x9,x22,#0x2 | `FALL_THROUGH`
<a id="insn-004e01c0"></a> `004e01c0` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004e01c4"></a> `004e01c4` | `4a 01 00 32` | orr w10,w10,#0x1 | `FALL_THROUGH`
<a id="insn-004e01c8"></a> `004e01c8` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004e01cc"></a> `004e01cc` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e01d0"></a> `004e01d0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004e01d4"></a> `004e01d4` | `3f e1 1d 94` | bl 0x00c586d0 | `UNCONDITIONAL_CALL`
<a id="insn-004e01d8"></a> `004e01d8` | `f6 03 40 f9` | ldr x22,[sp] | `FALL_THROUGH`
<a id="insn-004e01dc"></a> `004e01dc` | `76 01 00 b4` | cbz x22,0x004e0208 | `CONDITIONAL_JUMP`
<a id="insn-004e01e0"></a> `004e01e0` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004e01e4"></a> `004e01e4` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004e01e8"></a> `004e01e8` | `29 3c 00 f0` | adrp x9,0xc67000 | `FALL_THROUGH`
<a id="insn-004e01ec"></a> `004e01ec` | `29 9d 41 f9` | ldr x9,[x9, #0x338] | `FALL_THROUGH`
<a id="insn-004e01f0"></a> `004e01f0` | `02 01 16 cb` | sub x2,x8,x22 | `FALL_THROUGH`
<a id="insn-004e01f4"></a> `004e01f4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004e01f8"></a> `004e01f8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e01fc"></a> `004e01fc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004e0200"></a> `004e0200` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004e0204"></a> `004e0204` | `17 e0 1d 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-004e0208"></a> `004e0208` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e020c"></a> `004e020c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004e0210"></a> `004e0210` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004e0214"></a> `004e0214` | `43 e1 1d 94` | bl 0x00c58720 | `UNCONDITIONAL_CALL`
<a id="insn-004e0218"></a> `004e0218` | `a0 00 f8 37` | tbnz w0,#0x1f,0x004e022c | `CONDITIONAL_JUMP`
<a id="insn-004e021c"></a> `004e021c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e0220"></a> `004e0220` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004e0224"></a> `004e0224` | `87 e1 1d 94` | bl 0x00c58840 | `UNCONDITIONAL_CALL`
<a id="insn-004e0228"></a> `004e0228` | `f8 ff ff 17` | b 0x004e0208 | `UNCONDITIONAL_JUMP`
<a id="insn-004e022c"></a> `004e022c` | `a8 1a 40 b9` | ldr w8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-004e0230"></a> `004e0230` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-004e0234"></a> `004e0234` | `41 01 00 54` | b.ne 0x004e025c | `CONDITIONAL_JUMP`
<a id="insn-004e0238"></a> `004e0238` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004e023c"></a> `004e023c` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e0240"></a> `004e0240` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e0244"></a> `004e0244` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004e0248"></a> `004e0248` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004e024c"></a> `004e024c` | `e8 3b 40 b9` | ldr w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004e0250"></a> `004e0250` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-004e0254"></a> `004e0254` | `68 1a 00 b9` | str w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-004e0258"></a> `004e0258` | `11 00 00 14` | b 0x004e029c | `UNCONDITIONAL_JUMP`
<a id="insn-004e025c"></a> `004e025c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e0260"></a> `004e0260` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004e0264"></a> `004e0264` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004e0268"></a> `004e0268` | `96 e1 1d 94` | bl 0x00c588c0 | `UNCONDITIONAL_CALL`
<a id="insn-004e026c"></a> `004e026c` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e0270"></a> `004e0270` | `73 01 00 b4` | cbz x19,0x004e029c | `CONDITIONAL_JUMP`
<a id="insn-004e0274"></a> `004e0274` | `f3 17 00 f9` | str x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004e0278"></a> `004e0278` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004e027c"></a> `004e027c` | `29 3c 00 f0` | adrp x9,0xc67000 | `FALL_THROUGH`
<a id="insn-004e0280"></a> `004e0280` | `29 9d 41 f9` | ldr x9,[x9, #0x338] | `FALL_THROUGH`
<a id="insn-004e0284"></a> `004e0284` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004e0288"></a> `004e0288` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e028c"></a> `004e028c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e0290"></a> `004e0290` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004e0294"></a> `004e0294` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e0298"></a> `004e0298` | `f2 df 1d 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-004e029c"></a> `004e029c` | `b3 83 5d f8` | ldur x19,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e02a0"></a> `004e02a0` | `73 01 00 b4` | cbz x19,0x004e02cc | `CONDITIONAL_JUMP`
<a id="insn-004e02a4"></a> `004e02a4` | `b3 03 1e f8` | stur x19,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004e02a8"></a> `004e02a8` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004e02ac"></a> `004e02ac` | `29 3c 00 f0` | adrp x9,0xc67000 | `FALL_THROUGH`
<a id="insn-004e02b0"></a> `004e02b0` | `29 9d 41 f9` | ldr x9,[x9, #0x338] | `FALL_THROUGH`
<a id="insn-004e02b4"></a> `004e02b4` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004e02b8"></a> `004e02b8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e02bc"></a> `004e02bc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e02c0"></a> `004e02c0` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004e02c4"></a> `004e02c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e02c8"></a> `004e02c8` | `e6 df 1d 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-004e02cc"></a> `004e02cc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004e02d0"></a> `004e02d0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004e02d4"></a> `004e02d4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004e02d8"></a> `004e02d8` | `61 08 00 54` | b.ne 0x004e03e4 | `CONDITIONAL_JUMP`
<a id="insn-004e02dc"></a> `004e02dc` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004e02e0"></a> `004e02e0` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004e02e4"></a> `004e02e4` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004e02e8"></a> `004e02e8` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004e02ec"></a> `004e02ec` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004e02f0"></a> `004e02f0` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004e02f4"></a> `004e02f4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004e02f8"></a> `004e02f8` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004e02fc"></a> `004e02fc` | `fd dd 1d 94` | bl 0x00c57af0 | `UNCONDITIONAL_CALL`
<a id="insn-004e0300"></a> `004e0300` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004e0304"></a> `004e0304` | `e1 ee ff b0` | adrp x1,0x2bd000 | `FALL_THROUGH`
<a id="insn-004e0308"></a> `004e0308` | `21 0c 24 91` | add x1,x1,#0x903 | `FALL_THROUGH`
<a id="insn-004e030c"></a> `004e030c` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e0310"></a> `004e0310` | `a2 76 fd 97` | bl 0x0043dd98 | `UNCONDITIONAL_CALL`
<a id="insn-004e0314"></a> `004e0314` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004e0318"></a> `004e0318` | `a1 a3 00 d1` | sub x1,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e031c"></a> `004e031c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004e0320"></a> `004e0320` | `41 3a ff 97` | bl 0x004aec24 | `UNCONDITIONAL_CALL`
<a id="insn-004e0324"></a> `004e0324` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004e0328"></a> `004e0328` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004e032c"></a> `004e032c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004e0330"></a> `004e0330` | `a1 05 00 54` | b.ne 0x004e03e4 | `CONDITIONAL_JUMP`
<a id="insn-004e0334"></a> `004e0334` | `c1 3d 00 d0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004e0338"></a> `004e0338` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004e033c"></a> `004e033c` | `62 a7 2a 10` | adr x2,0x535828 | `FALL_THROUGH`
<a id="insn-004e0340"></a> `004e0340` | `21 a4 44 f9` | ldr x1,[x1, #0x948] | `FALL_THROUGH`
<a id="insn-004e0344"></a> `004e0344` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004e0348"></a> `004e0348` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004e034c"></a> `004e034c` | `f1 dd 1d 94` | bl 0x00c57b10 | `CALL_TERMINATOR`
<a id="insn-004e03e4"></a> `004e03e4` | `bf dd 1d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004dfdbc`](#insn-004dfdbc) 範囲 `[['004dfdbc', '004dfdeb']]`
  - `CONDITIONAL_JUMP` [`004dfde8`](#insn-004dfde8) → [`004e02f8`](#insn-004e02f8)
  - `FALL_THROUGH` [`004dfde8`](#insn-004dfde8) → [`004dfdec`](#insn-004dfdec)
- ブロック [`004dfdec`](#insn-004dfdec) 範囲 `[['004dfdec', '004dfe0f']]`
  - `CONDITIONAL_JUMP` [`004dfe0c`](#insn-004dfe0c) → [`004dfe24`](#insn-004dfe24)
  - `FALL_THROUGH` [`004dfe0c`](#insn-004dfe0c) → [`004dfe10`](#insn-004dfe10)
- ブロック [`004dfe10`](#insn-004dfe10) 範囲 `[['004dfe10', '004dfe13']]`
  - `FALL_THROUGH` [`004dfe10`](#insn-004dfe10) → [`004dfe14`](#insn-004dfe14)
- ブロック [`004dfe14`](#insn-004dfe14) 範囲 `[['004dfe14', '004dfe1b']]`
  - `CONDITIONAL_JUMP` [`004dfe18`](#insn-004dfe18) → [`004dfe24`](#insn-004dfe24)
  - `FALL_THROUGH` [`004dfe18`](#insn-004dfe18) → [`004dfe1c`](#insn-004dfe1c)
- ブロック [`004dfe1c`](#insn-004dfe1c) 範囲 `[['004dfe1c', '004dfe23']]`
  - `CONDITIONAL_JUMP` [`004dfe20`](#insn-004dfe20) → [`004dfe14`](#insn-004dfe14)
  - `FALL_THROUGH` [`004dfe20`](#insn-004dfe20) → [`004dfe24`](#insn-004dfe24)
- ブロック [`004dfe24`](#insn-004dfe24) 範囲 `[['004dfe24', '004dfe33']]`
  - `CONDITIONAL_JUMP` [`004dfe30`](#insn-004dfe30) → [`004dfe48`](#insn-004dfe48)
  - `FALL_THROUGH` [`004dfe30`](#insn-004dfe30) → [`004dfe34`](#insn-004dfe34)
- ブロック [`004dfe34`](#insn-004dfe34) 範囲 `[['004dfe34', '004dfe37']]`
  - `FALL_THROUGH` [`004dfe34`](#insn-004dfe34) → [`004dfe38`](#insn-004dfe38)
- ブロック [`004dfe38`](#insn-004dfe38) 範囲 `[['004dfe38', '004dfe3f']]`
  - `CONDITIONAL_JUMP` [`004dfe3c`](#insn-004dfe3c) → [`004dfe48`](#insn-004dfe48)
  - `FALL_THROUGH` [`004dfe3c`](#insn-004dfe3c) → [`004dfe40`](#insn-004dfe40)
- ブロック [`004dfe40`](#insn-004dfe40) 範囲 `[['004dfe40', '004dfe47']]`
  - `CONDITIONAL_JUMP` [`004dfe44`](#insn-004dfe44) → [`004dfe38`](#insn-004dfe38)
  - `FALL_THROUGH` [`004dfe44`](#insn-004dfe44) → [`004dfe48`](#insn-004dfe48)
- ブロック [`004dfe48`](#insn-004dfe48) 範囲 `[['004dfe48', '004dfe53']]`
  - `CONDITIONAL_JUMP` [`004dfe50`](#insn-004dfe50) → [`004dfed8`](#insn-004dfed8)
  - `FALL_THROUGH` [`004dfe50`](#insn-004dfe50) → [`004dfe54`](#insn-004dfe54)
- ブロック [`004dfe54`](#insn-004dfe54) 範囲 `[['004dfe54', '004dfe5b']]`
  - `CONDITIONAL_JUMP` [`004dfe58`](#insn-004dfe58) → [`004dfe6c`](#insn-004dfe6c)
  - `FALL_THROUGH` [`004dfe58`](#insn-004dfe58) → [`004dfe5c`](#insn-004dfe5c)
- ブロック [`004dfe5c`](#insn-004dfe5c) 範囲 `[['004dfe5c', '004dfe63']]`
  - `CONDITIONAL_JUMP` [`004dfe60`](#insn-004dfe60) → [`004dfe6c`](#insn-004dfe6c)
  - `FALL_THROUGH` [`004dfe60`](#insn-004dfe60) → [`004dfe64`](#insn-004dfe64)
- ブロック [`004dfe64`](#insn-004dfe64) 範囲 `[['004dfe64', '004dfe6b']]`
  - `CONDITIONAL_JUMP` [`004dfe68`](#insn-004dfe68) → [`004dfe5c`](#insn-004dfe5c)
  - `FALL_THROUGH` [`004dfe68`](#insn-004dfe68) → [`004dfe6c`](#insn-004dfe6c)
- ブロック [`004dfe6c`](#insn-004dfe6c) 範囲 `[['004dfe6c', '004dfe7b']]`
  - `CONDITIONAL_JUMP` [`004dfe78`](#insn-004dfe78) → [`004dfe90`](#insn-004dfe90)
  - `FALL_THROUGH` [`004dfe78`](#insn-004dfe78) → [`004dfe7c`](#insn-004dfe7c)
- ブロック [`004dfe7c`](#insn-004dfe7c) 範囲 `[['004dfe7c', '004dfe7f']]`
  - `FALL_THROUGH` [`004dfe7c`](#insn-004dfe7c) → [`004dfe80`](#insn-004dfe80)
- ブロック [`004dfe80`](#insn-004dfe80) 範囲 `[['004dfe80', '004dfe87']]`
  - `CONDITIONAL_JUMP` [`004dfe84`](#insn-004dfe84) → [`004dfe90`](#insn-004dfe90)
  - `FALL_THROUGH` [`004dfe84`](#insn-004dfe84) → [`004dfe88`](#insn-004dfe88)
- ブロック [`004dfe88`](#insn-004dfe88) 範囲 `[['004dfe88', '004dfe8f']]`
  - `CONDITIONAL_JUMP` [`004dfe8c`](#insn-004dfe8c) → [`004dfe80`](#insn-004dfe80)
  - `FALL_THROUGH` [`004dfe8c`](#insn-004dfe8c) → [`004dfe90`](#insn-004dfe90)
- ブロック [`004dfe90`](#insn-004dfe90) 範囲 `[['004dfe90', '004dfe9f']]`
  - `CONDITIONAL_JUMP` [`004dfe9c`](#insn-004dfe9c) → [`004dff14`](#insn-004dff14)
  - `FALL_THROUGH` [`004dfe9c`](#insn-004dfe9c) → [`004dfea0`](#insn-004dfea0)
- ブロック [`004dfea0`](#insn-004dfea0) 範囲 `[['004dfea0', '004dfeaf']]`
  - `CONDITIONAL_JUMP` [`004dfeac`](#insn-004dfeac) → [`004e03e4`](#insn-004e03e4)
  - `FALL_THROUGH` [`004dfeac`](#insn-004dfeac) → [`004dfeb0`](#insn-004dfeb0)
- ブロック [`004dfeb0`](#insn-004dfeb0) 範囲 `[['004dfeb0', '004dfed7']]`
- ブロック [`004dfed8`](#insn-004dfed8) 範囲 `[['004dfed8', '004dfedf']]`
  - `CONDITIONAL_JUMP` [`004dfedc`](#insn-004dfedc) → [`004dff90`](#insn-004dff90)
  - `FALL_THROUGH` [`004dfedc`](#insn-004dfedc) → [`004dfee0`](#insn-004dfee0)
- ブロック [`004dfee0`](#insn-004dfee0) 範囲 `[['004dfee0', '004dfeef']]`
  - `CONDITIONAL_JUMP` [`004dfeec`](#insn-004dfeec) → [`004e03e4`](#insn-004e03e4)
  - `FALL_THROUGH` [`004dfeec`](#insn-004dfeec) → [`004dfef0`](#insn-004dfef0)
- ブロック [`004dfef0`](#insn-004dfef0) 範囲 `[['004dfef0', '004dff13']]`
- ブロック [`004dff14`](#insn-004dff14) 範囲 `[['004dff14', '004dff3b']]`
  - `CONDITIONAL_JUMP` [`004dff38`](#insn-004dff38) → [`004dffe4`](#insn-004dffe4)
  - `FALL_THROUGH` [`004dff38`](#insn-004dff38) → [`004dff3c`](#insn-004dff3c)
- ブロック [`004dff3c`](#insn-004dff3c) 範囲 `[['004dff3c', '004dff4b']]`
  - `CONDITIONAL_JUMP` [`004dff48`](#insn-004dff48) → [`004dff60`](#insn-004dff60)
  - `FALL_THROUGH` [`004dff48`](#insn-004dff48) → [`004dff4c`](#insn-004dff4c)
- ブロック [`004dff4c`](#insn-004dff4c) 範囲 `[['004dff4c', '004dff4f']]`
  - `FALL_THROUGH` [`004dff4c`](#insn-004dff4c) → [`004dff50`](#insn-004dff50)
- ブロック [`004dff50`](#insn-004dff50) 範囲 `[['004dff50', '004dff57']]`
  - `CONDITIONAL_JUMP` [`004dff54`](#insn-004dff54) → [`004dff60`](#insn-004dff60)
  - `FALL_THROUGH` [`004dff54`](#insn-004dff54) → [`004dff58`](#insn-004dff58)
- ブロック [`004dff58`](#insn-004dff58) 範囲 `[['004dff58', '004dff5f']]`
  - `CONDITIONAL_JUMP` [`004dff5c`](#insn-004dff5c) → [`004dff50`](#insn-004dff50)
  - `FALL_THROUGH` [`004dff5c`](#insn-004dff5c) → [`004dff60`](#insn-004dff60)
- ブロック [`004dff60`](#insn-004dff60) 範囲 `[['004dff60', '004dff77']]`
  - `CONDITIONAL_JUMP` [`004dff74`](#insn-004dff74) → [`004dffc8`](#insn-004dffc8)
  - `FALL_THROUGH` [`004dff74`](#insn-004dff74) → [`004dff78`](#insn-004dff78)
- ブロック [`004dff78`](#insn-004dff78) 範囲 `[['004dff78', '004dff7b']]`
  - `FALL_THROUGH` [`004dff78`](#insn-004dff78) → [`004dff7c`](#insn-004dff7c)
- ブロック [`004dff7c`](#insn-004dff7c) 範囲 `[['004dff7c', '004dff83']]`
  - `CONDITIONAL_JUMP` [`004dff80`](#insn-004dff80) → [`004dffc8`](#insn-004dffc8)
  - `FALL_THROUGH` [`004dff80`](#insn-004dff80) → [`004dff84`](#insn-004dff84)
- ブロック [`004dff84`](#insn-004dff84) 範囲 `[['004dff84', '004dff8b']]`
  - `CONDITIONAL_JUMP` [`004dff88`](#insn-004dff88) → [`004dff7c`](#insn-004dff7c)
  - `FALL_THROUGH` [`004dff88`](#insn-004dff88) → [`004dff8c`](#insn-004dff8c)
- ブロック [`004dff8c`](#insn-004dff8c) 範囲 `[['004dff8c', '004dff8f']]`
  - `UNCONDITIONAL_JUMP` [`004dff8c`](#insn-004dff8c) → [`004dffdc`](#insn-004dffdc)
- ブロック [`004dff90`](#insn-004dff90) 範囲 `[['004dff90', '004dff9f']]`
  - `CONDITIONAL_JUMP` [`004dff9c`](#insn-004dff9c) → [`004e03e4`](#insn-004e03e4)
  - `FALL_THROUGH` [`004dff9c`](#insn-004dff9c) → [`004dffa0`](#insn-004dffa0)
- ブロック [`004dffa0`](#insn-004dffa0) 範囲 `[['004dffa0', '004dffc7']]`
- ブロック [`004dffc8`](#insn-004dffc8) 範囲 `[['004dffc8', '004dffcb']]`
  - `CONDITIONAL_JUMP` [`004dffc8`](#insn-004dffc8) → [`004dffdc`](#insn-004dffdc)
  - `FALL_THROUGH` [`004dffc8`](#insn-004dffc8) → [`004dffcc`](#insn-004dffcc)
- ブロック [`004dffcc`](#insn-004dffcc) 範囲 `[['004dffcc', '004dffd3']]`
  - `CONDITIONAL_JUMP` [`004dffd0`](#insn-004dffd0) → [`004dffe4`](#insn-004dffe4)
  - `FALL_THROUGH` [`004dffd0`](#insn-004dffd0) → [`004dffd4`](#insn-004dffd4)
- ブロック [`004dffd4`](#insn-004dffd4) 範囲 `[['004dffd4', '004dffdb']]`
  - `CONDITIONAL_JUMP` [`004dffd8`](#insn-004dffd8) → [`004dffcc`](#insn-004dffcc)
  - `FALL_THROUGH` [`004dffd8`](#insn-004dffd8) → [`004dffdc`](#insn-004dffdc)
- ブロック [`004dffdc`](#insn-004dffdc) 範囲 `[['004dffdc', '004dffe3']]`
  - `FALL_THROUGH` [`004dffe0`](#insn-004dffe0) → [`004dffe4`](#insn-004dffe4)
- ブロック [`004dffe4`](#insn-004dffe4) 範囲 `[['004dffe4', '004dffff']]`
  - `CONDITIONAL_JUMP` [`004dfffc`](#insn-004dfffc) → [`004e0074`](#insn-004e0074)
  - `FALL_THROUGH` [`004dfffc`](#insn-004dfffc) → [`004e0000`](#insn-004e0000)
- ブロック [`004e0000`](#insn-004e0000) 範囲 `[['004e0000', '004e0013']]`
  - `CONDITIONAL_JUMP` [`004e0010`](#insn-004e0010) → [`004e0028`](#insn-004e0028)
  - `FALL_THROUGH` [`004e0010`](#insn-004e0010) → [`004e0014`](#insn-004e0014)
- ブロック [`004e0014`](#insn-004e0014) 範囲 `[['004e0014', '004e0017']]`
  - `FALL_THROUGH` [`004e0014`](#insn-004e0014) → [`004e0018`](#insn-004e0018)
- ブロック [`004e0018`](#insn-004e0018) 範囲 `[['004e0018', '004e001f']]`
  - `CONDITIONAL_JUMP` [`004e001c`](#insn-004e001c) → [`004e0028`](#insn-004e0028)
  - `FALL_THROUGH` [`004e001c`](#insn-004e001c) → [`004e0020`](#insn-004e0020)
- ブロック [`004e0020`](#insn-004e0020) 範囲 `[['004e0020', '004e0027']]`
  - `CONDITIONAL_JUMP` [`004e0024`](#insn-004e0024) → [`004e0018`](#insn-004e0018)
  - `FALL_THROUGH` [`004e0024`](#insn-004e0024) → [`004e0028`](#insn-004e0028)
- ブロック [`004e0028`](#insn-004e0028) 範囲 `[['004e0028', '004e003f']]`
  - `CONDITIONAL_JUMP` [`004e003c`](#insn-004e003c) → [`004e0058`](#insn-004e0058)
  - `FALL_THROUGH` [`004e003c`](#insn-004e003c) → [`004e0040`](#insn-004e0040)
- ブロック [`004e0040`](#insn-004e0040) 範囲 `[['004e0040', '004e0043']]`
  - `FALL_THROUGH` [`004e0040`](#insn-004e0040) → [`004e0044`](#insn-004e0044)
- ブロック [`004e0044`](#insn-004e0044) 範囲 `[['004e0044', '004e004b']]`
  - `CONDITIONAL_JUMP` [`004e0048`](#insn-004e0048) → [`004e0058`](#insn-004e0058)
  - `FALL_THROUGH` [`004e0048`](#insn-004e0048) → [`004e004c`](#insn-004e004c)
- ブロック [`004e004c`](#insn-004e004c) 範囲 `[['004e004c', '004e0053']]`
  - `CONDITIONAL_JUMP` [`004e0050`](#insn-004e0050) → [`004e0044`](#insn-004e0044)
  - `FALL_THROUGH` [`004e0050`](#insn-004e0050) → [`004e0054`](#insn-004e0054)
- ブロック [`004e0054`](#insn-004e0054) 範囲 `[['004e0054', '004e0057']]`
  - `UNCONDITIONAL_JUMP` [`004e0054`](#insn-004e0054) → [`004e006c`](#insn-004e006c)
- ブロック [`004e0058`](#insn-004e0058) 範囲 `[['004e0058', '004e005b']]`
  - `CONDITIONAL_JUMP` [`004e0058`](#insn-004e0058) → [`004e006c`](#insn-004e006c)
  - `FALL_THROUGH` [`004e0058`](#insn-004e0058) → [`004e005c`](#insn-004e005c)
- ブロック [`004e005c`](#insn-004e005c) 範囲 `[['004e005c', '004e0063']]`
  - `CONDITIONAL_JUMP` [`004e0060`](#insn-004e0060) → [`004e0074`](#insn-004e0074)
  - `FALL_THROUGH` [`004e0060`](#insn-004e0060) → [`004e0064`](#insn-004e0064)
- ブロック [`004e0064`](#insn-004e0064) 範囲 `[['004e0064', '004e006b']]`
  - `CONDITIONAL_JUMP` [`004e0068`](#insn-004e0068) → [`004e005c`](#insn-004e005c)
  - `FALL_THROUGH` [`004e0068`](#insn-004e0068) → [`004e006c`](#insn-004e006c)
- ブロック [`004e006c`](#insn-004e006c) 範囲 `[['004e006c', '004e0073']]`
  - `FALL_THROUGH` [`004e0070`](#insn-004e0070) → [`004e0074`](#insn-004e0074)
- ブロック [`004e0074`](#insn-004e0074) 範囲 `[['004e0074', '004e0093']]`
  - `CONDITIONAL_JUMP` [`004e0090`](#insn-004e0090) → [`004e00d8`](#insn-004e00d8)
  - `FALL_THROUGH` [`004e0090`](#insn-004e0090) → [`004e0094`](#insn-004e0094)
- ブロック [`004e0094`](#insn-004e0094) 範囲 `[['004e0094', '004e00ab']]`
  - `CONDITIONAL_JUMP` [`004e00a8`](#insn-004e00a8) → [`004e00ec`](#insn-004e00ec)
  - `FALL_THROUGH` [`004e00a8`](#insn-004e00a8) → [`004e00ac`](#insn-004e00ac)
- ブロック [`004e00ac`](#insn-004e00ac) 範囲 `[['004e00ac', '004e00b7']]`
  - `CONDITIONAL_JUMP` [`004e00b4`](#insn-004e00b4) → [`004e00d0`](#insn-004e00d0)
  - `FALL_THROUGH` [`004e00b4`](#insn-004e00b4) → [`004e00b8`](#insn-004e00b8)
- ブロック [`004e00b8`](#insn-004e00b8) 範囲 `[['004e00b8', '004e00bf']]`
  - `CONDITIONAL_JUMP` [`004e00bc`](#insn-004e00bc) → [`004e00d0`](#insn-004e00d0)
  - `FALL_THROUGH` [`004e00bc`](#insn-004e00bc) → [`004e00c0`](#insn-004e00c0)
- ブロック [`004e00c0`](#insn-004e00c0) 範囲 `[['004e00c0', '004e00cf']]`
  - `FALL_THROUGH` [`004e00cc`](#insn-004e00cc) → [`004e00d0`](#insn-004e00d0)
- ブロック [`004e00d0`](#insn-004e00d0) 範囲 `[['004e00d0', '004e00d7']]`
  - `UNCONDITIONAL_JUMP` [`004e00d4`](#insn-004e00d4) → [`004e00ec`](#insn-004e00ec)
- ブロック [`004e00d8`](#insn-004e00d8) 範囲 `[['004e00d8', '004e00e3']]`
  - `CONDITIONAL_JUMP` [`004e00e0`](#insn-004e00e0) → [`004e00ec`](#insn-004e00ec)
  - `FALL_THROUGH` [`004e00e0`](#insn-004e00e0) → [`004e00e4`](#insn-004e00e4)
- ブロック [`004e00e4`](#insn-004e00e4) 範囲 `[['004e00e4', '004e00eb']]`
  - `FALL_THROUGH` [`004e00e8`](#insn-004e00e8) → [`004e00ec`](#insn-004e00ec)
- ブロック [`004e00ec`](#insn-004e00ec) 範囲 `[['004e00ec', '004e0117']]`
  - `CONDITIONAL_JUMP` [`004e0114`](#insn-004e0114) → [`004e0154`](#insn-004e0154)
  - `FALL_THROUGH` [`004e0114`](#insn-004e0114) → [`004e0118`](#insn-004e0118)
- ブロック [`004e0118`](#insn-004e0118) 範囲 `[['004e0118', '004e0127']]`
  - `CONDITIONAL_JUMP` [`004e0124`](#insn-004e0124) → [`004e0164`](#insn-004e0164)
  - `FALL_THROUGH` [`004e0124`](#insn-004e0124) → [`004e0128`](#insn-004e0128)
- ブロック [`004e0128`](#insn-004e0128) 範囲 `[['004e0128', '004e0133']]`
  - `CONDITIONAL_JUMP` [`004e0130`](#insn-004e0130) → [`004e014c`](#insn-004e014c)
  - `FALL_THROUGH` [`004e0130`](#insn-004e0130) → [`004e0134`](#insn-004e0134)
- ブロック [`004e0134`](#insn-004e0134) 範囲 `[['004e0134', '004e013b']]`
  - `CONDITIONAL_JUMP` [`004e0138`](#insn-004e0138) → [`004e014c`](#insn-004e014c)
  - `FALL_THROUGH` [`004e0138`](#insn-004e0138) → [`004e013c`](#insn-004e013c)
- ブロック [`004e013c`](#insn-004e013c) 範囲 `[['004e013c', '004e014b']]`
  - `FALL_THROUGH` [`004e0148`](#insn-004e0148) → [`004e014c`](#insn-004e014c)
- ブロック [`004e014c`](#insn-004e014c) 範囲 `[['004e014c', '004e0153']]`
  - `UNCONDITIONAL_JUMP` [`004e0150`](#insn-004e0150) → [`004e0164`](#insn-004e0164)
- ブロック [`004e0154`](#insn-004e0154) 範囲 `[['004e0154', '004e015b']]`
  - `CONDITIONAL_JUMP` [`004e0158`](#insn-004e0158) → [`004e0164`](#insn-004e0164)
  - `FALL_THROUGH` [`004e0158`](#insn-004e0158) → [`004e015c`](#insn-004e015c)
- ブロック [`004e015c`](#insn-004e015c) 範囲 `[['004e015c', '004e0163']]`
  - `FALL_THROUGH` [`004e0160`](#insn-004e0160) → [`004e0164`](#insn-004e0164)
- ブロック [`004e0164`](#insn-004e0164) 範囲 `[['004e0164', '004e0177']]`
  - `CONDITIONAL_JUMP` [`004e0174`](#insn-004e0174) → [`004e0208`](#insn-004e0208)
  - `FALL_THROUGH` [`004e0174`](#insn-004e0174) → [`004e0178`](#insn-004e0178)
- ブロック [`004e0178`](#insn-004e0178) 範囲 `[['004e0178', '004e01df']]`
  - `CONDITIONAL_JUMP` [`004e01dc`](#insn-004e01dc) → [`004e0208`](#insn-004e0208)
  - `FALL_THROUGH` [`004e01dc`](#insn-004e01dc) → [`004e01e0`](#insn-004e01e0)
- ブロック [`004e01e0`](#insn-004e01e0) 範囲 `[['004e01e0', '004e0207']]`
  - `FALL_THROUGH` [`004e0204`](#insn-004e0204) → [`004e0208`](#insn-004e0208)
- ブロック [`004e0208`](#insn-004e0208) 範囲 `[['004e0208', '004e021b']]`
  - `CONDITIONAL_JUMP` [`004e0218`](#insn-004e0218) → [`004e022c`](#insn-004e022c)
  - `FALL_THROUGH` [`004e0218`](#insn-004e0218) → [`004e021c`](#insn-004e021c)
- ブロック [`004e021c`](#insn-004e021c) 範囲 `[['004e021c', '004e022b']]`
  - `UNCONDITIONAL_JUMP` [`004e0228`](#insn-004e0228) → [`004e0208`](#insn-004e0208)
- ブロック [`004e022c`](#insn-004e022c) 範囲 `[['004e022c', '004e0237']]`
  - `CONDITIONAL_JUMP` [`004e0234`](#insn-004e0234) → [`004e025c`](#insn-004e025c)
  - `FALL_THROUGH` [`004e0234`](#insn-004e0234) → [`004e0238`](#insn-004e0238)
- ブロック [`004e0238`](#insn-004e0238) 範囲 `[['004e0238', '004e025b']]`
  - `UNCONDITIONAL_JUMP` [`004e0258`](#insn-004e0258) → [`004e029c`](#insn-004e029c)
- ブロック [`004e025c`](#insn-004e025c) 範囲 `[['004e025c', '004e0273']]`
  - `CONDITIONAL_JUMP` [`004e0270`](#insn-004e0270) → [`004e029c`](#insn-004e029c)
  - `FALL_THROUGH` [`004e0270`](#insn-004e0270) → [`004e0274`](#insn-004e0274)
- ブロック [`004e0274`](#insn-004e0274) 範囲 `[['004e0274', '004e029b']]`
  - `FALL_THROUGH` [`004e0298`](#insn-004e0298) → [`004e029c`](#insn-004e029c)
- ブロック [`004e029c`](#insn-004e029c) 範囲 `[['004e029c', '004e02a3']]`
  - `CONDITIONAL_JUMP` [`004e02a0`](#insn-004e02a0) → [`004e02cc`](#insn-004e02cc)
  - `FALL_THROUGH` [`004e02a0`](#insn-004e02a0) → [`004e02a4`](#insn-004e02a4)
- ブロック [`004e02a4`](#insn-004e02a4) 範囲 `[['004e02a4', '004e02cb']]`
  - `FALL_THROUGH` [`004e02c8`](#insn-004e02c8) → [`004e02cc`](#insn-004e02cc)
- ブロック [`004e02cc`](#insn-004e02cc) 範囲 `[['004e02cc', '004e02db']]`
  - `CONDITIONAL_JUMP` [`004e02d8`](#insn-004e02d8) → [`004e03e4`](#insn-004e03e4)
  - `FALL_THROUGH` [`004e02d8`](#insn-004e02d8) → [`004e02dc`](#insn-004e02dc)
- ブロック [`004e02dc`](#insn-004e02dc) 範囲 `[['004e02dc', '004e02f7']]`
- ブロック [`004e02f8`](#insn-004e02f8) 範囲 `[['004e02f8', '004e0333']]`
  - `CONDITIONAL_JUMP` [`004e0330`](#insn-004e0330) → [`004e03e4`](#insn-004e03e4)
  - `FALL_THROUGH` [`004e0330`](#insn-004e0330) → [`004e0334`](#insn-004e0334)
- ブロック [`004e0334`](#insn-004e0334) 範囲 `[['004e0334', '004e034f']]`
- ブロック [`004e03e4`](#insn-004e03e4) 範囲 `[['004e03e4', '004e03e7']]`

## 命令位置別の参照

- [`004dfdc0`](#insn-004dfdc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfdc4`](#insn-004dfdc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfdc8`](#insn-004dfdc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfdcc`](#insn-004dfdcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfdd0`](#insn-004dfdd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfde0`](#insn-004dfde0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfde8`](#insn-004dfde8) → [`004e02f8`](#insn-004e02f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe0c`](#insn-004dfe0c) → [`004dfe24`](#insn-004dfe24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe18`](#insn-004dfe18) → [`004dfe24`](#insn-004dfe24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe20`](#insn-004dfe20) → [`004dfe14`](#insn-004dfe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe30`](#insn-004dfe30) → [`004dfe48`](#insn-004dfe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe3c`](#insn-004dfe3c) → [`004dfe48`](#insn-004dfe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe44`](#insn-004dfe44) → [`004dfe38`](#insn-004dfe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe4c`](#insn-004dfe4c) → [`004b8774`](../004b8/004b8774.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b8774` · 推定シンボル `None` · 推定型 `None`
- [`004dfe50`](#insn-004dfe50) → [`004dfed8`](#insn-004dfed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe58`](#insn-004dfe58) → [`004dfe6c`](#insn-004dfe6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe60`](#insn-004dfe60) → [`004dfe6c`](#insn-004dfe6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe68`](#insn-004dfe68) → [`004dfe5c`](#insn-004dfe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe78`](#insn-004dfe78) → [`004dfe90`](#insn-004dfe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe84`](#insn-004dfe84) → [`004dfe90`](#insn-004dfe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe8c`](#insn-004dfe8c) → [`004dfe80`](#insn-004dfe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe98`](#insn-004dfe98) → [`004b8774`](../004b8/004b8774.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b8774` · 推定シンボル `None` · 推定型 `None`
- [`004dfe9c`](#insn-004dfe9c) → [`004dff14`](#insn-004dff14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfea4`](#insn-004dfea4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfeac`](#insn-004dfeac) → [`004e03e4`](#insn-004e03e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfebc`](#insn-004dfebc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfec0`](#insn-004dfec0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfec4`](#insn-004dfec4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfec8`](#insn-004dfec8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfecc`](#insn-004dfecc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfed4`](#insn-004dfed4) → [`00c588a0`](../00c58/00c588a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c588a0` · 推定シンボル `None` · 推定型 `None`
- [`004dfedc`](#insn-004dfedc) → [`004dff90`](#insn-004dff90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfee4`](#insn-004dfee4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfeec`](#insn-004dfeec) → [`004e03e4`](#insn-004e03e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfef8`](#insn-004dfef8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfefc`](#insn-004dfefc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff00`](#insn-004dff00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff04`](#insn-004dff04) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff08`](#insn-004dff08) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff10`](#insn-004dff10) → [`00c58740`](../00c58/00c58740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58740` · 推定シンボル `None` · 推定型 `None`
- [`004dff1c`](#insn-004dff1c) → [`00c58740`](../00c58/00c58740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58740` · 推定シンボル `None` · 推定型 `None`
- [`004dff24`](#insn-004dff24) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff30`](#insn-004dff30) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff38`](#insn-004dff38) → [`004dffe4`](#insn-004dffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff48`](#insn-004dff48) → [`004dff60`](#insn-004dff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff54`](#insn-004dff54) → [`004dff60`](#insn-004dff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff5c`](#insn-004dff5c) → [`004dff50`](#insn-004dff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff64`](#insn-004dff64) → [`004b9bf8`](../004b9/004b9bf8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b9bf8` · 推定シンボル `None` · 推定型 `None`
- [`004dff68`](#insn-004dff68) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff74`](#insn-004dff74) → [`004dffc8`](#insn-004dffc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff80`](#insn-004dff80) → [`004dffc8`](#insn-004dffc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff88`](#insn-004dff88) → [`004dff7c`](#insn-004dff7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff8c`](#insn-004dff8c) → [`004dffdc`](#insn-004dffdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff94`](#insn-004dff94) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff9c`](#insn-004dff9c) → [`004e03e4`](#insn-004e03e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffac`](#insn-004dffac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffb0`](#insn-004dffb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffb4`](#insn-004dffb4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffb8`](#insn-004dffb8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffbc`](#insn-004dffbc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffc4`](#insn-004dffc4) → [`00c588b0`](../00c58/00c588b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c588b0` · 推定シンボル `None` · 推定型 `None`
- [`004dffc8`](#insn-004dffc8) → [`004dffdc`](#insn-004dffdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffd0`](#insn-004dffd0) → [`004dffe4`](#insn-004dffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffd8`](#insn-004dffd8) → [`004dffcc`](#insn-004dffcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffe0`](#insn-004dffe0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffec`](#insn-004dffec) → [`00c586c0`](../00c58/00c586c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586c0` · 推定シンボル `None` · 推定型 `None`
- [`004dfffc`](#insn-004dfffc) → [`004e0074`](#insn-004e0074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0000`](#insn-004e0000) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0010`](#insn-004e0010) → [`004e0028`](#insn-004e0028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e001c`](#insn-004e001c) → [`004e0028`](#insn-004e0028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0024`](#insn-004e0024) → [`004e0018`](#insn-004e0018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e002c`](#insn-004e002c) → [`004b9bf8`](../004b9/004b9bf8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b9bf8` · 推定シンボル `None` · 推定型 `None`
- [`004e0030`](#insn-004e0030) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e003c`](#insn-004e003c) → [`004e0058`](#insn-004e0058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0048`](#insn-004e0048) → [`004e0058`](#insn-004e0058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0050`](#insn-004e0050) → [`004e0044`](#insn-004e0044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0054`](#insn-004e0054) → [`004e006c`](#insn-004e006c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0058`](#insn-004e0058) → [`004e006c`](#insn-004e006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0060`](#insn-004e0060) → [`004e0074`](#insn-004e0074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0068`](#insn-004e0068) → [`004e005c`](#insn-004e005c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0070`](#insn-004e0070) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e007c`](#insn-004e007c) → [`00c586c0`](../00c58/00c586c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586c0` · 推定シンボル `None` · 推定型 `None`
- [`004e0084`](#insn-004e0084) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0090`](#insn-004e0090) → [`004e00d8`](#insn-004e00d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0094`](#insn-004e0094) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00a8`](#insn-004e00a8) → [`004e00ec`](#insn-004e00ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00b4`](#insn-004e00b4) → [`004e00d0`](#insn-004e00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00bc`](#insn-004e00bc) → [`004e00d0`](#insn-004e00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00c8`](#insn-004e00c8) → [`00c57c90`](../00c57/00c57c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c90` · 推定シンボル `None` · 推定型 `None`
- [`004e00cc`](#insn-004e00cc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00d4`](#insn-004e00d4) → [`004e00ec`](#insn-004e00ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00d8`](#insn-004e00d8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00e0`](#insn-004e00e0) → [`004e00ec`](#insn-004e00ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00e8`](#insn-004e00e8) → [`00c57c90`](../00c57/00c57c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c90` · 推定シンボル `None` · 推定型 `None`
- [`004e00f4`](#insn-004e00f4) → [`00c58740`](../00c58/00c58740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58740` · 推定シンボル `None` · 推定型 `None`
- [`004e0100`](#insn-004e0100) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0108`](#insn-004e0108) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0114`](#insn-004e0114) → [`004e0154`](#insn-004e0154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0124`](#insn-004e0124) → [`004e0164`](#insn-004e0164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0130`](#insn-004e0130) → [`004e014c`](#insn-004e014c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0138`](#insn-004e0138) → [`004e014c`](#insn-004e014c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0144`](#insn-004e0144) → [`00c57c90`](../00c57/00c57c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c90` · 推定シンボル `None` · 推定型 `None`
- [`004e0148`](#insn-004e0148) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0150`](#insn-004e0150) → [`004e0164`](#insn-004e0164) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0158`](#insn-004e0158) → [`004e0164`](#insn-004e0164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0160`](#insn-004e0160) → [`00c57c90`](../00c57/00c57c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c90` · 推定シンボル `None` · 推定型 `None`
- [`004e016c`](#insn-004e016c) → [`00c58840`](../00c58/00c58840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58840` · 推定シンボル `None` · 推定型 `None`
- [`004e0170`](#insn-004e0170) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0174`](#insn-004e0174) → [`004e0208`](#insn-004e0208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0180`](#insn-004e0180) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0184`](#insn-004e0184) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01a4`](#insn-004e01a4) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01b4`](#insn-004e01b4) → [`005408e0`](../00540/005408e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005408e0` · 推定シンボル `None` · 推定型 `None`
- [`004e01b8`](#insn-004e01b8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01d4`](#insn-004e01d4) → [`00c586d0`](../00c58/00c586d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586d0` · 推定シンボル `None` · 推定型 `None`
- [`004e01d8`](#insn-004e01d8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01dc`](#insn-004e01dc) → [`004e0208`](#insn-004e0208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01e0`](#insn-004e01e0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01e4`](#insn-004e01e4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01ec`](#insn-004e01ec) → `00c67338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e01fc`](#insn-004e01fc) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004e0204`](#insn-004e0204) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`004e0214`](#insn-004e0214) → [`00c58720`](../00c58/00c58720.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58720` · 推定シンボル `None` · 推定型 `None`
- [`004e0218`](#insn-004e0218) → [`004e022c`](#insn-004e022c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0224`](#insn-004e0224) → [`00c58840`](../00c58/00c58840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58840` · 推定シンボル `None` · 推定型 `None`
- [`004e0228`](#insn-004e0228) → [`004e0208`](#insn-004e0208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0234`](#insn-004e0234) → [`004e025c`](#insn-004e025c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0238`](#insn-004e0238) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e023c`](#insn-004e023c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0240`](#insn-004e0240) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0244`](#insn-004e0244) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e024c`](#insn-004e024c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0258`](#insn-004e0258) → [`004e029c`](#insn-004e029c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0268`](#insn-004e0268) → [`00c588c0`](../00c58/00c588c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c588c0` · 推定シンボル `None` · 推定型 `None`
- [`004e026c`](#insn-004e026c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0270`](#insn-004e0270) → [`004e029c`](#insn-004e029c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0274`](#insn-004e0274) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0278`](#insn-004e0278) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0280`](#insn-004e0280) → `00c67338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e0290`](#insn-004e0290) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004e0298`](#insn-004e0298) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`004e029c`](#insn-004e029c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02a0`](#insn-004e02a0) → [`004e02cc`](#insn-004e02cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02a4`](#insn-004e02a4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02a8`](#insn-004e02a8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02b0`](#insn-004e02b0) → `00c67338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e02c0`](#insn-004e02c0) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004e02c8`](#insn-004e02c8) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`004e02d0`](#insn-004e02d0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02d8`](#insn-004e02d8) → [`004e03e4`](#insn-004e03e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02dc`](#insn-004e02dc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02e0`](#insn-004e02e0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02e4`](#insn-004e02e4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02e8`](#insn-004e02e8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02ec`](#insn-004e02ec) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02fc`](#insn-004e02fc) → [`00c57af0`](../00c57/00c57af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57af0` · 推定シンボル `None` · 推定型 `None`
- [`004e0308`](#insn-004e0308) → `002bd903`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004e0310`](#insn-004e0310) → [`0043dd98`](../0043d/0043dd98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043dd98` · 推定シンボル `None` · 推定型 `None`
- [`004e0320`](#insn-004e0320) → [`004aec24`](../004ae/004aec24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004aec24` · 推定シンボル `None` · 推定型 `None`
- [`004e0328`](#insn-004e0328) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0330`](#insn-004e0330) → [`004e03e4`](#insn-004e03e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e033c`](#insn-004e033c) → [`00535828`](../00535/00535828.md) · `PARAM` · `ANALYSIS` · 関数 `00535828` · 推定シンボル `None` · 推定型 `None`
- [`004e0340`](#insn-004e0340) → `00c9a948`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e0340`](#insn-004e0340) → `00c65f98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan13Invalid_StateE` · 推定型 `pointer __((offset(0x10)))`
- [`004e034c`](#insn-004e034c) → [`00c57b10`](../00c57/00c57b10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b10` · 推定シンボル `None` · 推定型 `None`
- [`004e03e4`](#insn-004e03e4) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004dfdc0`](#insn-004dfdc0)

~~~json
{
  "source": "004dfdc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfdc4`](#insn-004dfdc4)

~~~json
{
  "source": "004dfdc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfdc8`](#insn-004dfdc8)

~~~json
{
  "source": "004dfdc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfdcc`](#insn-004dfdcc)

~~~json
{
  "source": "004dfdcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfdd0`](#insn-004dfdd0)

~~~json
{
  "source": "004dfdd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfde0`](#insn-004dfde0)

~~~json
{
  "source": "004dfde0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfde8`](#insn-004dfde8)

~~~json
{
  "source": "004dfde8",
  "target": "004e02f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe0c`](#insn-004dfe0c)

~~~json
{
  "source": "004dfe0c",
  "target": "004dfe24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe18`](#insn-004dfe18)

~~~json
{
  "source": "004dfe18",
  "target": "004dfe24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe20`](#insn-004dfe20)

~~~json
{
  "source": "004dfe20",
  "target": "004dfe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe30`](#insn-004dfe30)

~~~json
{
  "source": "004dfe30",
  "target": "004dfe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe3c`](#insn-004dfe3c)

~~~json
{
  "source": "004dfe3c",
  "target": "004dfe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe44`](#insn-004dfe44)

~~~json
{
  "source": "004dfe44",
  "target": "004dfe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe4c`](#insn-004dfe4c)

~~~json
{
  "source": "004dfe4c",
  "target": "004b8774",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfe50`](#insn-004dfe50)

~~~json
{
  "source": "004dfe50",
  "target": "004dfed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe58`](#insn-004dfe58)

~~~json
{
  "source": "004dfe58",
  "target": "004dfe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe60`](#insn-004dfe60)

~~~json
{
  "source": "004dfe60",
  "target": "004dfe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe68`](#insn-004dfe68)

~~~json
{
  "source": "004dfe68",
  "target": "004dfe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe78`](#insn-004dfe78)

~~~json
{
  "source": "004dfe78",
  "target": "004dfe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe84`](#insn-004dfe84)

~~~json
{
  "source": "004dfe84",
  "target": "004dfe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe8c`](#insn-004dfe8c)

~~~json
{
  "source": "004dfe8c",
  "target": "004dfe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe98`](#insn-004dfe98)

~~~json
{
  "source": "004dfe98",
  "target": "004b8774",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfe9c`](#insn-004dfe9c)

~~~json
{
  "source": "004dfe9c",
  "target": "004dff14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfea4`](#insn-004dfea4)

~~~json
{
  "source": "004dfea4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfeac`](#insn-004dfeac)

~~~json
{
  "source": "004dfeac",
  "target": "004e03e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfebc`](#insn-004dfebc)

~~~json
{
  "source": "004dfebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfec0`](#insn-004dfec0)

~~~json
{
  "source": "004dfec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfec4`](#insn-004dfec4)

~~~json
{
  "source": "004dfec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfec8`](#insn-004dfec8)

~~~json
{
  "source": "004dfec8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfecc`](#insn-004dfecc)

~~~json
{
  "source": "004dfecc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfed4`](#insn-004dfed4)

~~~json
{
  "source": "004dfed4",
  "target": "00c588a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfedc`](#insn-004dfedc)

~~~json
{
  "source": "004dfedc",
  "target": "004dff90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfee4`](#insn-004dfee4)

~~~json
{
  "source": "004dfee4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfeec`](#insn-004dfeec)

~~~json
{
  "source": "004dfeec",
  "target": "004e03e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfef8`](#insn-004dfef8)

~~~json
{
  "source": "004dfef8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfefc`](#insn-004dfefc)

~~~json
{
  "source": "004dfefc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff00`](#insn-004dff00)

~~~json
{
  "source": "004dff00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff04`](#insn-004dff04)

~~~json
{
  "source": "004dff04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff08`](#insn-004dff08)

~~~json
{
  "source": "004dff08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff10`](#insn-004dff10)

~~~json
{
  "source": "004dff10",
  "target": "00c58740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dff1c`](#insn-004dff1c)

~~~json
{
  "source": "004dff1c",
  "target": "00c58740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dff24`](#insn-004dff24)

~~~json
{
  "source": "004dff24",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff30`](#insn-004dff30)

~~~json
{
  "source": "004dff30",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff38`](#insn-004dff38)

~~~json
{
  "source": "004dff38",
  "target": "004dffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff48`](#insn-004dff48)

~~~json
{
  "source": "004dff48",
  "target": "004dff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff54`](#insn-004dff54)

~~~json
{
  "source": "004dff54",
  "target": "004dff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff5c`](#insn-004dff5c)

~~~json
{
  "source": "004dff5c",
  "target": "004dff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff64`](#insn-004dff64)

~~~json
{
  "source": "004dff64",
  "target": "004b9bf8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dff68`](#insn-004dff68)

~~~json
{
  "source": "004dff68",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff74`](#insn-004dff74)

~~~json
{
  "source": "004dff74",
  "target": "004dffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff80`](#insn-004dff80)

~~~json
{
  "source": "004dff80",
  "target": "004dffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff88`](#insn-004dff88)

~~~json
{
  "source": "004dff88",
  "target": "004dff7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff8c`](#insn-004dff8c)

~~~json
{
  "source": "004dff8c",
  "target": "004dffdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff94`](#insn-004dff94)

~~~json
{
  "source": "004dff94",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff9c`](#insn-004dff9c)

~~~json
{
  "source": "004dff9c",
  "target": "004e03e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffac`](#insn-004dffac)

~~~json
{
  "source": "004dffac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffb0`](#insn-004dffb0)

~~~json
{
  "source": "004dffb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffb4`](#insn-004dffb4)

~~~json
{
  "source": "004dffb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffb8`](#insn-004dffb8)

~~~json
{
  "source": "004dffb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffbc`](#insn-004dffbc)

~~~json
{
  "source": "004dffbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffc4`](#insn-004dffc4)

~~~json
{
  "source": "004dffc4",
  "target": "00c588b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dffc8`](#insn-004dffc8)

~~~json
{
  "source": "004dffc8",
  "target": "004dffdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffd0`](#insn-004dffd0)

~~~json
{
  "source": "004dffd0",
  "target": "004dffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffd8`](#insn-004dffd8)

~~~json
{
  "source": "004dffd8",
  "target": "004dffcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffe0`](#insn-004dffe0)

~~~json
{
  "source": "004dffe0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffec`](#insn-004dffec)

~~~json
{
  "source": "004dffec",
  "target": "00c586c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfffc`](#insn-004dfffc)

~~~json
{
  "source": "004dfffc",
  "target": "004e0074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0000`](#insn-004e0000)

~~~json
{
  "source": "004e0000",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0010`](#insn-004e0010)

~~~json
{
  "source": "004e0010",
  "target": "004e0028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e001c`](#insn-004e001c)

~~~json
{
  "source": "004e001c",
  "target": "004e0028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0024`](#insn-004e0024)

~~~json
{
  "source": "004e0024",
  "target": "004e0018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e002c`](#insn-004e002c)

~~~json
{
  "source": "004e002c",
  "target": "004b9bf8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0030`](#insn-004e0030)

~~~json
{
  "source": "004e0030",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e003c`](#insn-004e003c)

~~~json
{
  "source": "004e003c",
  "target": "004e0058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0048`](#insn-004e0048)

~~~json
{
  "source": "004e0048",
  "target": "004e0058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0050`](#insn-004e0050)

~~~json
{
  "source": "004e0050",
  "target": "004e0044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0054`](#insn-004e0054)

~~~json
{
  "source": "004e0054",
  "target": "004e006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0058`](#insn-004e0058)

~~~json
{
  "source": "004e0058",
  "target": "004e006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0060`](#insn-004e0060)

~~~json
{
  "source": "004e0060",
  "target": "004e0074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0068`](#insn-004e0068)

~~~json
{
  "source": "004e0068",
  "target": "004e005c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0070`](#insn-004e0070)

~~~json
{
  "source": "004e0070",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e007c`](#insn-004e007c)

~~~json
{
  "source": "004e007c",
  "target": "00c586c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0084`](#insn-004e0084)

~~~json
{
  "source": "004e0084",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0090`](#insn-004e0090)

~~~json
{
  "source": "004e0090",
  "target": "004e00d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0094`](#insn-004e0094)

~~~json
{
  "source": "004e0094",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00a8`](#insn-004e00a8)

~~~json
{
  "source": "004e00a8",
  "target": "004e00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00b4`](#insn-004e00b4)

~~~json
{
  "source": "004e00b4",
  "target": "004e00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00bc`](#insn-004e00bc)

~~~json
{
  "source": "004e00bc",
  "target": "004e00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00c8`](#insn-004e00c8)

~~~json
{
  "source": "004e00c8",
  "target": "00c57c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e00cc`](#insn-004e00cc)

~~~json
{
  "source": "004e00cc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00d4`](#insn-004e00d4)

~~~json
{
  "source": "004e00d4",
  "target": "004e00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00d8`](#insn-004e00d8)

~~~json
{
  "source": "004e00d8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00e0`](#insn-004e00e0)

~~~json
{
  "source": "004e00e0",
  "target": "004e00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00e8`](#insn-004e00e8)

~~~json
{
  "source": "004e00e8",
  "target": "00c57c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e00f4`](#insn-004e00f4)

~~~json
{
  "source": "004e00f4",
  "target": "00c58740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0100`](#insn-004e0100)

~~~json
{
  "source": "004e0100",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0108`](#insn-004e0108)

~~~json
{
  "source": "004e0108",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0114`](#insn-004e0114)

~~~json
{
  "source": "004e0114",
  "target": "004e0154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0124`](#insn-004e0124)

~~~json
{
  "source": "004e0124",
  "target": "004e0164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0130`](#insn-004e0130)

~~~json
{
  "source": "004e0130",
  "target": "004e014c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0138`](#insn-004e0138)

~~~json
{
  "source": "004e0138",
  "target": "004e014c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0144`](#insn-004e0144)

~~~json
{
  "source": "004e0144",
  "target": "00c57c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0148`](#insn-004e0148)

~~~json
{
  "source": "004e0148",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0150`](#insn-004e0150)

~~~json
{
  "source": "004e0150",
  "target": "004e0164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0158`](#insn-004e0158)

~~~json
{
  "source": "004e0158",
  "target": "004e0164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0160`](#insn-004e0160)

~~~json
{
  "source": "004e0160",
  "target": "00c57c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e016c`](#insn-004e016c)

~~~json
{
  "source": "004e016c",
  "target": "00c58840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0170`](#insn-004e0170)

~~~json
{
  "source": "004e0170",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0174`](#insn-004e0174)

~~~json
{
  "source": "004e0174",
  "target": "004e0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0180`](#insn-004e0180)

~~~json
{
  "source": "004e0180",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0184`](#insn-004e0184)

~~~json
{
  "source": "004e0184",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01a4`](#insn-004e01a4)

~~~json
{
  "source": "004e01a4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01b4`](#insn-004e01b4)

~~~json
{
  "source": "004e01b4",
  "target": "005408e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e01b8`](#insn-004e01b8)

~~~json
{
  "source": "004e01b8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01d4`](#insn-004e01d4)

~~~json
{
  "source": "004e01d4",
  "target": "00c586d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e01d8`](#insn-004e01d8)

~~~json
{
  "source": "004e01d8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01dc`](#insn-004e01dc)

~~~json
{
  "source": "004e01dc",
  "target": "004e0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01e0`](#insn-004e01e0)

~~~json
{
  "source": "004e01e0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01e4`](#insn-004e01e4)

~~~json
{
  "source": "004e01e4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01ec`](#insn-004e01ec)

~~~json
{
  "source": "004e01ec",
  "target": "00c67338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67338",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e01fc`](#insn-004e01fc)

~~~json
{
  "source": "004e01fc",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0204`](#insn-004e0204)

~~~json
{
  "source": "004e0204",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0214`](#insn-004e0214)

~~~json
{
  "source": "004e0214",
  "target": "00c58720",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0218`](#insn-004e0218)

~~~json
{
  "source": "004e0218",
  "target": "004e022c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0224`](#insn-004e0224)

~~~json
{
  "source": "004e0224",
  "target": "00c58840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0228`](#insn-004e0228)

~~~json
{
  "source": "004e0228",
  "target": "004e0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0234`](#insn-004e0234)

~~~json
{
  "source": "004e0234",
  "target": "004e025c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0238`](#insn-004e0238)

~~~json
{
  "source": "004e0238",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e023c`](#insn-004e023c)

~~~json
{
  "source": "004e023c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0240`](#insn-004e0240)

~~~json
{
  "source": "004e0240",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0244`](#insn-004e0244)

~~~json
{
  "source": "004e0244",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e024c`](#insn-004e024c)

~~~json
{
  "source": "004e024c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0258`](#insn-004e0258)

~~~json
{
  "source": "004e0258",
  "target": "004e029c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0268`](#insn-004e0268)

~~~json
{
  "source": "004e0268",
  "target": "00c588c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e026c`](#insn-004e026c)

~~~json
{
  "source": "004e026c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0270`](#insn-004e0270)

~~~json
{
  "source": "004e0270",
  "target": "004e029c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0274`](#insn-004e0274)

~~~json
{
  "source": "004e0274",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0278`](#insn-004e0278)

~~~json
{
  "source": "004e0278",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0280`](#insn-004e0280)

~~~json
{
  "source": "004e0280",
  "target": "00c67338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67338",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e0290`](#insn-004e0290)

~~~json
{
  "source": "004e0290",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0298`](#insn-004e0298)

~~~json
{
  "source": "004e0298",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e029c`](#insn-004e029c)

~~~json
{
  "source": "004e029c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02a0`](#insn-004e02a0)

~~~json
{
  "source": "004e02a0",
  "target": "004e02cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02a4`](#insn-004e02a4)

~~~json
{
  "source": "004e02a4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02a8`](#insn-004e02a8)

~~~json
{
  "source": "004e02a8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02b0`](#insn-004e02b0)

~~~json
{
  "source": "004e02b0",
  "target": "00c67338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67338",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e02c0`](#insn-004e02c0)

~~~json
{
  "source": "004e02c0",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e02c8`](#insn-004e02c8)

~~~json
{
  "source": "004e02c8",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e02d0`](#insn-004e02d0)

~~~json
{
  "source": "004e02d0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02d8`](#insn-004e02d8)

~~~json
{
  "source": "004e02d8",
  "target": "004e03e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02dc`](#insn-004e02dc)

~~~json
{
  "source": "004e02dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02e0`](#insn-004e02e0)

~~~json
{
  "source": "004e02e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02e4`](#insn-004e02e4)

~~~json
{
  "source": "004e02e4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02e8`](#insn-004e02e8)

~~~json
{
  "source": "004e02e8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02ec`](#insn-004e02ec)

~~~json
{
  "source": "004e02ec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02fc`](#insn-004e02fc)

~~~json
{
  "source": "004e02fc",
  "target": "00c57af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0308`](#insn-004e0308)

~~~json
{
  "source": "004e0308",
  "target": "002bd903",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bd903",
  "offset": 0,
  "size": 34,
  "datatype": "string",
  "bytes": "4d6f64756c61725f526564756365723a204e6576657220696e6974616c697a65",
  "capture_start": "002bd903",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004e0310`](#insn-004e0310)

~~~json
{
  "source": "004e0310",
  "target": "0043dd98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0320`](#insn-004e0320)

~~~json
{
  "source": "004e0320",
  "target": "004aec24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0328`](#insn-004e0328)

~~~json
{
  "source": "004e0328",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0330`](#insn-004e0330)

~~~json
{
  "source": "004e0330",
  "target": "004e03e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e033c`](#insn-004e033c)

~~~json
{
  "source": "004e033c",
  "target": "00535828",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0340`](#insn-004e0340)

~~~json
{
  "source": "004e0340",
  "target": "00c9a948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a948",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e0340`](#insn-004e0340)

~~~json
{
  "source": "004e0340",
  "target": "00c65f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e034c`](#insn-004e034c)

~~~json
{
  "source": "004e034c",
  "target": "00c57b10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e03e4`](#insn-004e03e4)

~~~json
{
  "source": "004e03e4",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
