# 004dfdfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004dfdbc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0009.md#compare-27f90b113aafaf47693d401e87defc4c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004dfe3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004dfe3c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0009.md#compare-081b8bdfbb58204d51f753fe57a8dc6c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004dfdfc",
  "name": "_ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE",
  "size": 1432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3b9ddd202beb206003f0b7ddc720ba41c067d390b320ccf3fecb9390e6803ac",
  "source_text_sha256": "c3b9ddd202beb206003f0b7ddc720ba41c067d390b320ccf3fecb9390e6803ac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004dfdfc",
        "004e038f"
      ],
      [
        "004e0424",
        "004e0427"
      ]
    ],
    "bytes_sha256": "e8eb802f877cf707c653081147abda2027e9169e625804d36acac1595279d08f",
    "instruction_count": 358,
    "instruction_bytes": 1432,
    "body_bytes": 1432,
    "indirect": 3,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59320](../00c59/00c59320.md)

## 呼び出し先

- [0043ddd8](../0043d/0043ddd8.md)
- [004aec64](../004ae/004aec64.md)
- [004b87b4](../004b8/004b87b4.md)
- [004b9c38](../004b9/004b9c38.md)
- [00540920](../00540/00540920.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57ef0](../00c57/00c57ef0.md)
- [00c57f10](../00c57/00c57f10.md)
- [00c58090](../00c58/00c58090.md)
- [00c58660](../00c58/00c58660.md)
- [00c58ac0](../00c58/00c58ac0.md)
- [00c58ad0](../00c58/00c58ad0.md)
- [00c58b20](../00c58/00c58b20.md)
- [00c58b40](../00c58/00c58b40.md)
- [00c58c40](../00c58/00c58c40.md)
- [00c58ca0](../00c58/00c58ca0.md)
- [00c58cb0](../00c58/00c58cb0.md)
- [00c58cc0](../00c58/00c58cc0.md)
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
    FUN_0043ddd8(&local_78,"Modular_Reducer: Never initalized");
    FUN_004aec64(uVar8,&local_78);
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar8,PTR__ZTIN5Botan13Invalid_StateE_00c9ad48,FUN_00535868);
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
    iVar7 = FUN_004b87b4(lVar9,lVar1);
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
      iVar7 = FUN_004b87b4(lVar9,lVar15);
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
          FUN_004b9c38(local_78,lVar9,uVar14 >> 5,0);
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          piVar4 = local_78;
          if ((long)local_70 - (long)local_78 == 0) {
joined_r0x004e0008:
            do {
              if (lVar9 == 0) goto LAB_004e001c;
              if (*piVar4 != 0) goto LAB_004e0024;
              lVar9 = lVar9 + -1;
              piVar4 = piVar4 + 1;
            } while( true );
          }
          do {
            if (local_78[lVar9 + -1] != 0) goto joined_r0x004e0008;
            lVar9 = lVar9 + -1;
          } while (lVar9 != 0);
LAB_004e001c:
          local_60 = 1;
        }
LAB_004e0024:
        _ZN5Botan6BigIntmLERKS0_(&local_78,param_2 + 8);
        uVar14 = param_2[0xc] * 0x20 + 0x20;
        if (uVar14 != 0) {
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          lVar12 = (long)local_70 - (long)local_78;
          while ((lVar12 != 0 && (local_78[lVar9 + -1] == 0))) {
            lVar9 = lVar9 + -1;
            lVar12 = lVar9;
          }
          FUN_004b9c38(local_78,lVar9,uVar14 >> 5,0);
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          piVar4 = local_78;
          if ((long)local_70 - (long)local_78 == 0) {
joined_r0x004e0098:
            do {
              if (lVar9 == 0) goto LAB_004e00ac;
              if (*piVar4 != 0) goto LAB_004e00b4;
              lVar9 = lVar9 + -1;
              piVar4 = piVar4 + 1;
            } while( true );
          }
          do {
            if (local_78[lVar9 + -1] != 0) goto joined_r0x004e0098;
            lVar9 = lVar9 + -1;
          } while (lVar9 != 0);
LAB_004e00ac:
          local_60 = 1;
        }
LAB_004e00b4:
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
          FUN_00540920(&local_c0,lVar9 + uVar14);
          lVar9 = uVar13 * 4;
          *(uint *)((long)local_c0 + lVar9) = *(uint *)((long)local_c0 + lVar9) | 1;
          _ZN5Botan6BigIntpLERKS0_(&local_a0,&local_c0);
          pvVar5 = local_c0;
          if (local_c0 != (void *)0x0) {
            local_b8 = local_c0;
            (*(code *)PTR_memset_00c67738)(local_c0,0,local_b0 - (long)local_c0);
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
            (*(code *)PTR_memset_00c67738)(local_a0,0,local_90 - (long)local_a0);
            free(pvVar5);
          }
        }
        if (local_78 != (int *)0x0) {
          local_70 = local_78;
          (*(code *)PTR_memset_00c67738)(local_78,0,local_68 - (long)local_78);
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
<a id="insn-004dfdfc"></a> `004dfdfc` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004dfe00"></a> `004dfe00` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dfe04"></a> `004dfe04` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dfe08"></a> `004dfe08` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dfe0c"></a> `004dfe0c` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dfe10"></a> `004dfe10` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dfe14"></a> `004dfe14` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004dfe18"></a> `004dfe18` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004dfe1c"></a> `004dfe1c` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dfe20"></a> `004dfe20` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dfe24"></a> `004dfe24` | `09 30 40 f9` | ldr x9,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-004dfe28"></a> `004dfe28` | `89 28 00 b4` | cbz x9,0x004e0338 | `CONDITIONAL_JUMP`
<a id="insn-004dfe2c"></a> `004dfe2c` | `36 68 40 a9` | ldp x22,x26,[x1] | `FALL_THROUGH`
<a id="insn-004dfe30"></a> `004dfe30` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004dfe34"></a> `004dfe34` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-004dfe38"></a> `004dfe38` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004dfe3c"></a> `004dfe3c` | `48 03 16 eb` | subs x8,x26,x22 | `FALL_THROUGH`
<a id="insn-004dfe40"></a> `004dfe40` | `d9 12 00 d1` | sub x25,x22,#0x4 | `FALL_THROUGH`
<a id="insn-004dfe44"></a> `004dfe44` | `17 fd 42 93` | asr x23,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004dfe48"></a> `004dfe48` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-004dfe4c"></a> `004dfe4c` | `c0 00 00 54` | b.eq 0x004dfe64 | `CONDITIONAL_JUMP`
<a id="insn-004dfe50"></a> `004dfe50` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-004dfe54"></a> `004dfe54` | `28 7b 61 b8` | ldr w8,[x25, x1, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfe58"></a> `004dfe58` | `68 00 00 35` | cbnz w8,0x004dfe64 | `CONDITIONAL_JUMP`
<a id="insn-004dfe5c"></a> `004dfe5c` | `21 04 00 f1` | subs x1,x1,#0x1 | `FALL_THROUGH`
<a id="insn-004dfe60"></a> `004dfe60` | `a1 ff ff 54` | b.ne 0x004dfe54 | `CONDITIONAL_JUMP`
<a id="insn-004dfe64"></a> `004dfe64` | `82 22 40 a9` | ldp x2,x8,[x20] | `FALL_THROUGH`
<a id="insn-004dfe68"></a> `004dfe68` | `08 01 02 eb` | subs x8,x8,x2 | `FALL_THROUGH`
<a id="insn-004dfe6c"></a> `004dfe6c` | `03 fd 42 93` | asr x3,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004dfe70"></a> `004dfe70` | `c0 00 00 54` | b.eq 0x004dfe88 | `CONDITIONAL_JUMP`
<a id="insn-004dfe74"></a> `004dfe74` | `48 10 00 d1` | sub x8,x2,#0x4 | `FALL_THROUGH`
<a id="insn-004dfe78"></a> `004dfe78` | `09 79 63 b8` | ldr w9,[x8, x3, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfe7c"></a> `004dfe7c` | `69 00 00 35` | cbnz w9,0x004dfe88 | `CONDITIONAL_JUMP`
<a id="insn-004dfe80"></a> `004dfe80` | `63 04 00 f1` | subs x3,x3,#0x1 | `FALL_THROUGH`
<a id="insn-004dfe84"></a> `004dfe84` | `a1 ff ff 54` | b.ne 0x004dfe78 | `CONDITIONAL_JUMP`
<a id="insn-004dfe88"></a> `004dfe88` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004dfe8c"></a> `004dfe8c` | `4a 62 ff 97` | bl 0x004b87b4 | `UNCONDITIONAL_CALL`
<a id="insn-004dfe90"></a> `004dfe90` | `40 04 f8 37` | tbnz w0,#0x1f,0x004dff18 | `CONDITIONAL_JUMP`
<a id="insn-004dfe94"></a> `004dfe94` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-004dfe98"></a> `004dfe98` | `a0 00 00 54` | b.eq 0x004dfeac | `CONDITIONAL_JUMP`
<a id="insn-004dfe9c"></a> `004dfe9c` | `28 7b 77 b8` | ldr w8,[x25, x23, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfea0"></a> `004dfea0` | `68 00 00 35` | cbnz w8,0x004dfeac | `CONDITIONAL_JUMP`
<a id="insn-004dfea4"></a> `004dfea4` | `f7 06 00 f1` | subs x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-004dfea8"></a> `004dfea8` | `a1 ff ff 54` | b.ne 0x004dfe9c | `CONDITIONAL_JUMP`
<a id="insn-004dfeac"></a> `004dfeac` | `82 22 42 a9` | ldp x2,x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-004dfeb0"></a> `004dfeb0` | `08 01 02 eb` | subs x8,x8,x2 | `FALL_THROUGH`
<a id="insn-004dfeb4"></a> `004dfeb4` | `03 fd 42 93` | asr x3,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004dfeb8"></a> `004dfeb8` | `c0 00 00 54` | b.eq 0x004dfed0 | `CONDITIONAL_JUMP`
<a id="insn-004dfebc"></a> `004dfebc` | `48 10 00 d1` | sub x8,x2,#0x4 | `FALL_THROUGH`
<a id="insn-004dfec0"></a> `004dfec0` | `09 79 63 b8` | ldr w9,[x8, x3, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dfec4"></a> `004dfec4` | `69 00 00 35` | cbnz w9,0x004dfed0 | `CONDITIONAL_JUMP`
<a id="insn-004dfec8"></a> `004dfec8` | `63 04 00 f1` | subs x3,x3,#0x1 | `FALL_THROUGH`
<a id="insn-004dfecc"></a> `004dfecc` | `a1 ff ff 54` | b.ne 0x004dfec0 | `CONDITIONAL_JUMP`
<a id="insn-004dfed0"></a> `004dfed0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004dfed4"></a> `004dfed4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-004dfed8"></a> `004dfed8` | `37 62 ff 97` | bl 0x004b87b4 | `UNCONDITIONAL_CALL`
<a id="insn-004dfedc"></a> `004dfedc` | `c0 03 f8 37` | tbnz w0,#0x1f,0x004dff54 | `CONDITIONAL_JUMP`
<a id="insn-004dfee0"></a> `004dfee0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dfee4"></a> `004dfee4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dfee8"></a> `004dfee8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004dfeec"></a> `004dfeec` | `c1 29 00 54` | b.ne 0x004e0424 | `CONDITIONAL_JUMP`
<a id="insn-004dfef0"></a> `004dfef0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004dfef4"></a> `004dfef4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004dfef8"></a> `004dfef8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004dfefc"></a> `004dfefc` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dff00"></a> `004dff00` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dff04"></a> `004dff04` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dff08"></a> `004dff08` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dff0c"></a> `004dff0c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dff10"></a> `004dff10` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004dff14"></a> `004dff14` | `63 e3 1d 14` | b 0x00c58ca0 | `CALL_TERMINATOR`
<a id="insn-004dff18"></a> `004dff18` | `a8 1a 40 b9` | ldr w8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-004dff1c"></a> `004dff1c` | `a8 05 00 34` | cbz w8,0x004dffd0 | `CONDITIONAL_JUMP`
<a id="insn-004dff20"></a> `004dff20` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dff24"></a> `004dff24` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dff28"></a> `004dff28` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004dff2c"></a> `004dff2c` | `c1 27 00 54` | b.ne 0x004e0424 | `CONDITIONAL_JUMP`
<a id="insn-004dff30"></a> `004dff30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004dff34"></a> `004dff34` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004dff38"></a> `004dff38` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dff3c"></a> `004dff3c` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dff40"></a> `004dff40` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dff44"></a> `004dff44` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dff48"></a> `004dff48` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dff4c"></a> `004dff4c` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004dff50"></a> `004dff50` | `fc e2 1d 14` | b 0x00c58b40 | `CALL_TERMINATOR`
<a id="insn-004dff54"></a> `004dff54` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004dff58"></a> `004dff58` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004dff5c"></a> `004dff5c` | `f9 e2 1d 94` | bl 0x00c58b40 | `UNCONDITIONAL_CALL`
<a id="insn-004dff60"></a> `004dff60` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004dff64"></a> `004dff64` | `a0 a7 7d a9` | ldp x0,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004dff68"></a> `004dff68` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-004dff6c"></a> `004dff6c` | `08 e9 7b d3` | lsl x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004dff70"></a> `004dff70` | `aa 03 1f b8` | stur w10,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004dff74"></a> `004dff74` | `08 81 00 f1` | subs x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-004dff78"></a> `004dff78` | `60 05 00 54` | b.eq 0x004e0024 | `CONDITIONAL_JUMP`
<a id="insn-004dff7c"></a> `004dff7c` | `29 01 00 eb` | subs x9,x9,x0 | `FALL_THROUGH`
<a id="insn-004dff80"></a> `004dff80` | `02 fd 45 d3` | lsr x2,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004dff84"></a> `004dff84` | `21 fd 42 93` | asr x1,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004dff88"></a> `004dff88` | `c0 00 00 54` | b.eq 0x004dffa0 | `CONDITIONAL_JUMP`
<a id="insn-004dff8c"></a> `004dff8c` | `08 10 00 d1` | sub x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-004dff90"></a> `004dff90` | `09 79 61 b8` | ldr w9,[x8, x1, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dff94"></a> `004dff94` | `69 00 00 35` | cbnz w9,0x004dffa0 | `CONDITIONAL_JUMP`
<a id="insn-004dff98"></a> `004dff98` | `21 04 00 f1` | subs x1,x1,#0x1 | `FALL_THROUGH`
<a id="insn-004dff9c"></a> `004dff9c` | `a1 ff ff 54` | b.ne 0x004dff90 | `CONDITIONAL_JUMP`
<a id="insn-004dffa0"></a> `004dffa0` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-004dffa4"></a> `004dffa4` | `25 67 ff 97` | bl 0x004b9c38 | `UNCONDITIONAL_CALL`
<a id="insn-004dffa8"></a> `004dffa8` | `a8 a7 7d a9` | ldp x8,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004dffac"></a> `004dffac` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004dffb0"></a> `004dffb0` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004dffb4"></a> `004dffb4` | `a0 02 00 54` | b.eq 0x004e0008 | `CONDITIONAL_JUMP`
<a id="insn-004dffb8"></a> `004dffb8` | `0a 11 00 d1` | sub x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-004dffbc"></a> `004dffbc` | `4b 79 69 b8` | ldr w11,[x10, x9, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004dffc0"></a> `004dffc0` | `4b 02 00 35` | cbnz w11,0x004e0008 | `CONDITIONAL_JUMP`
<a id="insn-004dffc4"></a> `004dffc4` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004dffc8"></a> `004dffc8` | `a1 ff ff 54` | b.ne 0x004dffbc | `CONDITIONAL_JUMP`
<a id="insn-004dffcc"></a> `004dffcc` | `14 00 00 14` | b 0x004e001c | `UNCONDITIONAL_JUMP`
<a id="insn-004dffd0"></a> `004dffd0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004dffd4"></a> `004dffd4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dffd8"></a> `004dffd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004dffdc"></a> `004dffdc` | `41 22 00 54` | b.ne 0x004e0424 | `CONDITIONAL_JUMP`
<a id="insn-004dffe0"></a> `004dffe0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004dffe4"></a> `004dffe4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004dffe8"></a> `004dffe8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004dffec"></a> `004dffec` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004dfff0"></a> `004dfff0` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004dfff4"></a> `004dfff4` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004dfff8"></a> `004dfff8` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004dfffc"></a> `004dfffc` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004e0000"></a> `004e0000` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004e0004"></a> `004e0004` | `2b e3 1d 14` | b 0x00c58cb0 | `CALL_TERMINATOR`
<a id="insn-004e0008"></a> `004e0008` | `a9 00 00 b4` | cbz x9,0x004e001c | `CONDITIONAL_JUMP`
<a id="insn-004e000c"></a> `004e000c` | `0a 45 40 b8` | ldr w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-004e0010"></a> `004e0010` | `aa 00 00 35` | cbnz w10,0x004e0024 | `CONDITIONAL_JUMP`
<a id="insn-004e0014"></a> `004e0014` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004e0018"></a> `004e0018` | `a1 ff ff 54` | b.ne 0x004e000c | `CONDITIONAL_JUMP`
<a id="insn-004e001c"></a> `004e001c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-004e0020"></a> `004e0020` | `a8 03 1f b8` | stur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004e0024"></a> `004e0024` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e0028"></a> `004e0028` | `81 02 01 91` | add x1,x20,#0x40 | `FALL_THROUGH`
<a id="insn-004e002c"></a> `004e002c` | `a5 e2 1d 94` | bl 0x00c58ac0 | `UNCONDITIONAL_CALL`
<a id="insn-004e0030"></a> `004e0030` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004e0034"></a> `004e0034` | `08 e9 7b d3` | lsl x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004e0038"></a> `004e0038` | `08 81 00 b1` | adds x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-004e003c"></a> `004e003c` | `c0 03 00 54` | b.eq 0x004e00b4 | `CONDITIONAL_JUMP`
<a id="insn-004e0040"></a> `004e0040` | `a0 a7 7d a9` | ldp x0,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e0044"></a> `004e0044` | `02 fd 45 d3` | lsr x2,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004e0048"></a> `004e0048` | `29 01 00 eb` | subs x9,x9,x0 | `FALL_THROUGH`
<a id="insn-004e004c"></a> `004e004c` | `21 fd 42 93` | asr x1,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e0050"></a> `004e0050` | `c0 00 00 54` | b.eq 0x004e0068 | `CONDITIONAL_JUMP`
<a id="insn-004e0054"></a> `004e0054` | `08 10 00 d1` | sub x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-004e0058"></a> `004e0058` | `09 79 61 b8` | ldr w9,[x8, x1, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e005c"></a> `004e005c` | `69 00 00 35` | cbnz w9,0x004e0068 | `CONDITIONAL_JUMP`
<a id="insn-004e0060"></a> `004e0060` | `21 04 00 f1` | subs x1,x1,#0x1 | `FALL_THROUGH`
<a id="insn-004e0064"></a> `004e0064` | `a1 ff ff 54` | b.ne 0x004e0058 | `CONDITIONAL_JUMP`
<a id="insn-004e0068"></a> `004e0068` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-004e006c"></a> `004e006c` | `f3 66 ff 97` | bl 0x004b9c38 | `UNCONDITIONAL_CALL`
<a id="insn-004e0070"></a> `004e0070` | `a8 a7 7d a9` | ldp x8,x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e0074"></a> `004e0074` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004e0078"></a> `004e0078` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e007c"></a> `004e007c` | `e0 00 00 54` | b.eq 0x004e0098 | `CONDITIONAL_JUMP`
<a id="insn-004e0080"></a> `004e0080` | `0a 11 00 d1` | sub x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-004e0084"></a> `004e0084` | `4b 79 69 b8` | ldr w11,[x10, x9, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e0088"></a> `004e0088` | `8b 00 00 35` | cbnz w11,0x004e0098 | `CONDITIONAL_JUMP`
<a id="insn-004e008c"></a> `004e008c` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004e0090"></a> `004e0090` | `a1 ff ff 54` | b.ne 0x004e0084 | `CONDITIONAL_JUMP`
<a id="insn-004e0094"></a> `004e0094` | `06 00 00 14` | b 0x004e00ac | `UNCONDITIONAL_JUMP`
<a id="insn-004e0098"></a> `004e0098` | `a9 00 00 b4` | cbz x9,0x004e00ac | `CONDITIONAL_JUMP`
<a id="insn-004e009c"></a> `004e009c` | `0a 45 40 b8` | ldr w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-004e00a0"></a> `004e00a0` | `aa 00 00 35` | cbnz w10,0x004e00b4 | `CONDITIONAL_JUMP`
<a id="insn-004e00a4"></a> `004e00a4` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004e00a8"></a> `004e00a8` | `a1 ff ff 54` | b.ne 0x004e009c | `CONDITIONAL_JUMP`
<a id="insn-004e00ac"></a> `004e00ac` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-004e00b0"></a> `004e00b0` | `a8 03 1f b8` | stur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004e00b4"></a> `004e00b4` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e00b8"></a> `004e00b8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004e00bc"></a> `004e00bc` | `81 e2 1d 94` | bl 0x00c58ac0 | `UNCONDITIONAL_CALL`
<a id="insn-004e00c0"></a> `004e00c0` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004e00c4"></a> `004e00c4` | `a9 03 5e f8` | ldur x9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004e00c8"></a> `004e00c8` | `08 e9 7b d3` | lsl x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004e00cc"></a> `004e00cc` | `0a 81 00 b1` | adds x10,x8,#0x20 | `FALL_THROUGH`
<a id="insn-004e00d0"></a> `004e00d0` | `40 02 00 54` | b.eq 0x004e0118 | `CONDITIONAL_JUMP`
<a id="insn-004e00d4"></a> `004e00d4` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e00d8"></a> `004e00d8` | `56 fd 45 d3` | lsr x22,x10,#0x5 | `FALL_THROUGH`
<a id="insn-004e00dc"></a> `004e00dc` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004e00e0"></a> `004e00e0` | `2a fd 42 93` | asr x10,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e00e4"></a> `004e00e4` | `df 02 0a eb` | cmp x22,x10 | `FALL_THROUGH`
<a id="insn-004e00e8"></a> `004e00e8` | `22 02 00 54` | b.cs 0x004e012c | `CONDITIONAL_JUMP`
<a id="insn-004e00ec"></a> `004e00ec` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-004e00f0"></a> `004e00f0` | `4a 01 09 eb` | subs x10,x10,x9 | `FALL_THROUGH`
<a id="insn-004e00f4"></a> `004e00f4` | `e0 00 00 54` | b.eq 0x004e0110 | `CONDITIONAL_JUMP`
<a id="insn-004e00f8"></a> `004e00f8` | `42 f5 7e d3` | lsl x2,x10,#0x2 | `FALL_THROUGH`
<a id="insn-004e00fc"></a> `004e00fc` | `a2 00 00 b4` | cbz x2,0x004e0110 | `CONDITIONAL_JUMP`
<a id="insn-004e0100"></a> `004e0100` | `00 09 09 8b` | add x0,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-004e0104"></a> `004e0104` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e0108"></a> `004e0108` | `e2 df 1d 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-004e010c"></a> `004e010c` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e0110"></a> `004e0110` | `1f 79 36 b8` | str wzr,[x8, x22, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e0114"></a> `004e0114` | `06 00 00 14` | b 0x004e012c | `UNCONDITIONAL_JUMP`
<a id="insn-004e0118"></a> `004e0118` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e011c"></a> `004e011c` | `22 01 00 eb` | subs x2,x9,x0 | `FALL_THROUGH`
<a id="insn-004e0120"></a> `004e0120` | `60 00 00 54` | b.eq 0x004e012c | `CONDITIONAL_JUMP`
<a id="insn-004e0124"></a> `004e0124` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e0128"></a> `004e0128` | `da df 1d 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-004e012c"></a> `004e012c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e0130"></a> `004e0130` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004e0134"></a> `004e0134` | `83 e2 1d 94` | bl 0x00c58b40 | `UNCONDITIONAL_CALL`
<a id="insn-004e0138"></a> `004e0138` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004e013c"></a> `004e013c` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-004e0140"></a> `004e0140` | `eb 3b 00 b9` | str w11,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004e0144"></a> `004e0144` | `09 e9 7b d3` | lsl x9,x8,#0x5 | `FALL_THROUGH`
<a id="insn-004e0148"></a> `004e0148` | `e0 23 42 a9` | ldp x0,x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e014c"></a> `004e014c` | `2a 81 00 b1` | adds x10,x9,#0x20 | `FALL_THROUGH`
<a id="insn-004e0150"></a> `004e0150` | `02 01 00 cb` | sub x2,x8,x0 | `FALL_THROUGH`
<a id="insn-004e0154"></a> `004e0154` | `00 02 00 54` | b.eq 0x004e0194 | `CONDITIONAL_JUMP`
<a id="insn-004e0158"></a> `004e0158` | `49 fc 42 93` | asr x9,x2,#0x2 | `FALL_THROUGH`
<a id="insn-004e015c"></a> `004e015c` | `56 fd 45 d3` | lsr x22,x10,#0x5 | `FALL_THROUGH`
<a id="insn-004e0160"></a> `004e0160` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-004e0164"></a> `004e0164` | `02 02 00 54` | b.cs 0x004e01a4 | `CONDITIONAL_JUMP`
<a id="insn-004e0168"></a> `004e0168` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-004e016c"></a> `004e016c` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004e0170"></a> `004e0170` | `e0 00 00 54` | b.eq 0x004e018c | `CONDITIONAL_JUMP`
<a id="insn-004e0174"></a> `004e0174` | `22 f5 7e d3` | lsl x2,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004e0178"></a> `004e0178` | `a2 00 00 b4` | cbz x2,0x004e018c | `CONDITIONAL_JUMP`
<a id="insn-004e017c"></a> `004e017c` | `00 08 08 8b` | add x0,x0,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-004e0180"></a> `004e0180` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e0184"></a> `004e0184` | `c3 df 1d 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-004e0188"></a> `004e0188` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e018c"></a> `004e018c` | `1f 78 36 b8` | str wzr,[x0, x22, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004e0190"></a> `004e0190` | `05 00 00 14` | b 0x004e01a4 | `UNCONDITIONAL_JUMP`
<a id="insn-004e0194"></a> `004e0194` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-004e0198"></a> `004e0198` | `60 00 00 54` | b.eq 0x004e01a4 | `CONDITIONAL_JUMP`
<a id="insn-004e019c"></a> `004e019c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e01a0"></a> `004e01a0` | `bc df 1d 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-004e01a4"></a> `004e01a4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e01a8"></a> `004e01a8` | `a1 a3 00 d1` | sub x1,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e01ac"></a> `004e01ac` | `a5 e2 1d 94` | bl 0x00c58c40 | `UNCONDITIONAL_CALL`
<a id="insn-004e01b0"></a> `004e01b0` | `e8 3b 40 b9` | ldr w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004e01b4"></a> `004e01b4` | `a8 04 00 35` | cbnz w8,0x004e0248 | `CONDITIONAL_JUMP`
<a id="insn-004e01b8"></a> `004e01b8` | `88 32 40 f9` | ldr x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-004e01bc"></a> `004e01bc` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-004e01c0"></a> `004e01c0` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004e01c4"></a> `004e01c4` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-004e01c8"></a> `004e01c8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004e01cc"></a> `004e01cc` | `16 e9 40 92` | and x22,x8,#0x7ffffffffffffff | `FALL_THROUGH`
<a id="insn-004e01d0"></a> `004e01d0` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-004e01d4"></a> `004e01d4` | `0a 09 40 f2` | ands x10,x8,#0x7 | `FALL_THROUGH`
<a id="insn-004e01d8"></a> `004e01d8` | `29 01 0a cb` | sub x9,x9,x10 | `FALL_THROUGH`
<a id="insn-004e01dc"></a> `004e01dc` | `1f 09 40 f2` | tst x8,#0x7 | `FALL_THROUGH`
<a id="insn-004e01e0"></a> `004e01e0` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-004e01e4"></a> `004e01e4` | `ea 1b 00 b9` | str w10,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004e01e8"></a> `004e01e8` | `e9 03 89 9a` | csel x9,xzr,x9,eq | `FALL_THROUGH`
<a id="insn-004e01ec"></a> `004e01ec` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004e01f0"></a> `004e01f0` | `21 01 08 8b` | add x1,x9,x8 | `FALL_THROUGH`
<a id="insn-004e01f4"></a> `004e01f4` | `cb 81 01 94` | bl 0x00540920 | `UNCONDITIONAL_CALL`
<a id="insn-004e01f8"></a> `004e01f8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-004e01fc"></a> `004e01fc` | `c9 f6 7e d3` | lsl x9,x22,#0x2 | `FALL_THROUGH`
<a id="insn-004e0200"></a> `004e0200` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004e0204"></a> `004e0204` | `4a 01 00 32` | orr w10,w10,#0x1 | `FALL_THROUGH`
<a id="insn-004e0208"></a> `004e0208` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004e020c"></a> `004e020c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e0210"></a> `004e0210` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004e0214"></a> `004e0214` | `2f e2 1d 94` | bl 0x00c58ad0 | `UNCONDITIONAL_CALL`
<a id="insn-004e0218"></a> `004e0218` | `f6 03 40 f9` | ldr x22,[sp] | `FALL_THROUGH`
<a id="insn-004e021c"></a> `004e021c` | `76 01 00 b4` | cbz x22,0x004e0248 | `CONDITIONAL_JUMP`
<a id="insn-004e0220"></a> `004e0220` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004e0224"></a> `004e0224` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004e0228"></a> `004e0228` | `29 3c 00 f0` | adrp x9,0xc67000 | `FALL_THROUGH`
<a id="insn-004e022c"></a> `004e022c` | `29 9d 43 f9` | ldr x9,[x9, #0x738] | `FALL_THROUGH`
<a id="insn-004e0230"></a> `004e0230` | `02 01 16 cb` | sub x2,x8,x22 | `FALL_THROUGH`
<a id="insn-004e0234"></a> `004e0234` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004e0238"></a> `004e0238` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e023c"></a> `004e023c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004e0240"></a> `004e0240` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004e0244"></a> `004e0244` | `07 e1 1d 94` | bl 0x00c58660 | `UNCONDITIONAL_CALL`
<a id="insn-004e0248"></a> `004e0248` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e024c"></a> `004e024c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004e0250"></a> `004e0250` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004e0254"></a> `004e0254` | `33 e2 1d 94` | bl 0x00c58b20 | `UNCONDITIONAL_CALL`
<a id="insn-004e0258"></a> `004e0258` | `a0 00 f8 37` | tbnz w0,#0x1f,0x004e026c | `CONDITIONAL_JUMP`
<a id="insn-004e025c"></a> `004e025c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e0260"></a> `004e0260` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004e0264"></a> `004e0264` | `77 e2 1d 94` | bl 0x00c58c40 | `UNCONDITIONAL_CALL`
<a id="insn-004e0268"></a> `004e0268` | `f8 ff ff 17` | b 0x004e0248 | `UNCONDITIONAL_JUMP`
<a id="insn-004e026c"></a> `004e026c` | `a8 1a 40 b9` | ldr w8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-004e0270"></a> `004e0270` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-004e0274"></a> `004e0274` | `41 01 00 54` | b.ne 0x004e029c | `CONDITIONAL_JUMP`
<a id="insn-004e0278"></a> `004e0278` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004e027c"></a> `004e027c` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e0280"></a> `004e0280` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e0284"></a> `004e0284` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004e0288"></a> `004e0288` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004e028c"></a> `004e028c` | `e8 3b 40 b9` | ldr w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004e0290"></a> `004e0290` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-004e0294"></a> `004e0294` | `68 1a 00 b9` | str w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-004e0298"></a> `004e0298` | `11 00 00 14` | b 0x004e02dc | `UNCONDITIONAL_JUMP`
<a id="insn-004e029c"></a> `004e029c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004e02a0"></a> `004e02a0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004e02a4"></a> `004e02a4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004e02a8"></a> `004e02a8` | `86 e2 1d 94` | bl 0x00c58cc0 | `UNCONDITIONAL_CALL`
<a id="insn-004e02ac"></a> `004e02ac` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004e02b0"></a> `004e02b0` | `73 01 00 b4` | cbz x19,0x004e02dc | `CONDITIONAL_JUMP`
<a id="insn-004e02b4"></a> `004e02b4` | `f3 17 00 f9` | str x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004e02b8"></a> `004e02b8` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004e02bc"></a> `004e02bc` | `29 3c 00 f0` | adrp x9,0xc67000 | `FALL_THROUGH`
<a id="insn-004e02c0"></a> `004e02c0` | `29 9d 43 f9` | ldr x9,[x9, #0x738] | `FALL_THROUGH`
<a id="insn-004e02c4"></a> `004e02c4` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004e02c8"></a> `004e02c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e02cc"></a> `004e02cc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e02d0"></a> `004e02d0` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004e02d4"></a> `004e02d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e02d8"></a> `004e02d8` | `e2 e0 1d 94` | bl 0x00c58660 | `UNCONDITIONAL_CALL`
<a id="insn-004e02dc"></a> `004e02dc` | `b3 83 5d f8` | ldur x19,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004e02e0"></a> `004e02e0` | `73 01 00 b4` | cbz x19,0x004e030c | `CONDITIONAL_JUMP`
<a id="insn-004e02e4"></a> `004e02e4` | `b3 03 1e f8` | stur x19,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004e02e8"></a> `004e02e8` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004e02ec"></a> `004e02ec` | `29 3c 00 f0` | adrp x9,0xc67000 | `FALL_THROUGH`
<a id="insn-004e02f0"></a> `004e02f0` | `29 9d 43 f9` | ldr x9,[x9, #0x738] | `FALL_THROUGH`
<a id="insn-004e02f4"></a> `004e02f4` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004e02f8"></a> `004e02f8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e02fc"></a> `004e02fc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004e0300"></a> `004e0300` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004e0304"></a> `004e0304` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004e0308"></a> `004e0308` | `d6 e0 1d 94` | bl 0x00c58660 | `UNCONDITIONAL_CALL`
<a id="insn-004e030c"></a> `004e030c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004e0310"></a> `004e0310` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004e0314"></a> `004e0314` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004e0318"></a> `004e0318` | `61 08 00 54` | b.ne 0x004e0424 | `CONDITIONAL_JUMP`
<a id="insn-004e031c"></a> `004e031c` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004e0320"></a> `004e0320` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004e0324"></a> `004e0324` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004e0328"></a> `004e0328` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004e032c"></a> `004e032c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004e0330"></a> `004e0330` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-004e0334"></a> `004e0334` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004e0338"></a> `004e0338` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004e033c"></a> `004e033c` | `ed de 1d 94` | bl 0x00c57ef0 | `UNCONDITIONAL_CALL`
<a id="insn-004e0340"></a> `004e0340` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004e0344"></a> `004e0344` | `e1 ee ff b0` | adrp x1,0x2bd000 | `FALL_THROUGH`
<a id="insn-004e0348"></a> `004e0348` | `21 0c 25 91` | add x1,x1,#0x943 | `FALL_THROUGH`
<a id="insn-004e034c"></a> `004e034c` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e0350"></a> `004e0350` | `a2 76 fd 97` | bl 0x0043ddd8 | `UNCONDITIONAL_CALL`
<a id="insn-004e0354"></a> `004e0354` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004e0358"></a> `004e0358` | `a1 a3 00 d1` | sub x1,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004e035c"></a> `004e035c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004e0360"></a> `004e0360` | `41 3a ff 97` | bl 0x004aec64 | `UNCONDITIONAL_CALL`
<a id="insn-004e0364"></a> `004e0364` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004e0368"></a> `004e0368` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004e036c"></a> `004e036c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004e0370"></a> `004e0370` | `a1 05 00 54` | b.ne 0x004e0424 | `CONDITIONAL_JUMP`
<a id="insn-004e0374"></a> `004e0374` | `c1 3d 00 d0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004e0378"></a> `004e0378` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004e037c"></a> `004e037c` | `62 a7 2a 10` | adr x2,0x535868 | `FALL_THROUGH`
<a id="insn-004e0380"></a> `004e0380` | `21 a4 46 f9` | ldr x1,[x1, #0xd48] | `FALL_THROUGH`
<a id="insn-004e0384"></a> `004e0384` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004e0388"></a> `004e0388` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004e038c"></a> `004e038c` | `e1 de 1d 94` | bl 0x00c57f10 | `CALL_TERMINATOR`
<a id="insn-004e0424"></a> `004e0424` | `af de 1d 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004dfdfc`](#insn-004dfdfc) 範囲 `[['004dfdfc', '004dfe2b']]`
  - `CONDITIONAL_JUMP` [`004dfe28`](#insn-004dfe28) → [`004e0338`](#insn-004e0338)
  - `FALL_THROUGH` [`004dfe28`](#insn-004dfe28) → [`004dfe2c`](#insn-004dfe2c)
- ブロック [`004dfe2c`](#insn-004dfe2c) 範囲 `[['004dfe2c', '004dfe4f']]`
  - `CONDITIONAL_JUMP` [`004dfe4c`](#insn-004dfe4c) → [`004dfe64`](#insn-004dfe64)
  - `FALL_THROUGH` [`004dfe4c`](#insn-004dfe4c) → [`004dfe50`](#insn-004dfe50)
- ブロック [`004dfe50`](#insn-004dfe50) 範囲 `[['004dfe50', '004dfe53']]`
  - `FALL_THROUGH` [`004dfe50`](#insn-004dfe50) → [`004dfe54`](#insn-004dfe54)
- ブロック [`004dfe54`](#insn-004dfe54) 範囲 `[['004dfe54', '004dfe5b']]`
  - `CONDITIONAL_JUMP` [`004dfe58`](#insn-004dfe58) → [`004dfe64`](#insn-004dfe64)
  - `FALL_THROUGH` [`004dfe58`](#insn-004dfe58) → [`004dfe5c`](#insn-004dfe5c)
- ブロック [`004dfe5c`](#insn-004dfe5c) 範囲 `[['004dfe5c', '004dfe63']]`
  - `CONDITIONAL_JUMP` [`004dfe60`](#insn-004dfe60) → [`004dfe54`](#insn-004dfe54)
  - `FALL_THROUGH` [`004dfe60`](#insn-004dfe60) → [`004dfe64`](#insn-004dfe64)
- ブロック [`004dfe64`](#insn-004dfe64) 範囲 `[['004dfe64', '004dfe73']]`
  - `CONDITIONAL_JUMP` [`004dfe70`](#insn-004dfe70) → [`004dfe88`](#insn-004dfe88)
  - `FALL_THROUGH` [`004dfe70`](#insn-004dfe70) → [`004dfe74`](#insn-004dfe74)
- ブロック [`004dfe74`](#insn-004dfe74) 範囲 `[['004dfe74', '004dfe77']]`
  - `FALL_THROUGH` [`004dfe74`](#insn-004dfe74) → [`004dfe78`](#insn-004dfe78)
- ブロック [`004dfe78`](#insn-004dfe78) 範囲 `[['004dfe78', '004dfe7f']]`
  - `CONDITIONAL_JUMP` [`004dfe7c`](#insn-004dfe7c) → [`004dfe88`](#insn-004dfe88)
  - `FALL_THROUGH` [`004dfe7c`](#insn-004dfe7c) → [`004dfe80`](#insn-004dfe80)
- ブロック [`004dfe80`](#insn-004dfe80) 範囲 `[['004dfe80', '004dfe87']]`
  - `CONDITIONAL_JUMP` [`004dfe84`](#insn-004dfe84) → [`004dfe78`](#insn-004dfe78)
  - `FALL_THROUGH` [`004dfe84`](#insn-004dfe84) → [`004dfe88`](#insn-004dfe88)
- ブロック [`004dfe88`](#insn-004dfe88) 範囲 `[['004dfe88', '004dfe93']]`
  - `CONDITIONAL_JUMP` [`004dfe90`](#insn-004dfe90) → [`004dff18`](#insn-004dff18)
  - `FALL_THROUGH` [`004dfe90`](#insn-004dfe90) → [`004dfe94`](#insn-004dfe94)
- ブロック [`004dfe94`](#insn-004dfe94) 範囲 `[['004dfe94', '004dfe9b']]`
  - `CONDITIONAL_JUMP` [`004dfe98`](#insn-004dfe98) → [`004dfeac`](#insn-004dfeac)
  - `FALL_THROUGH` [`004dfe98`](#insn-004dfe98) → [`004dfe9c`](#insn-004dfe9c)
- ブロック [`004dfe9c`](#insn-004dfe9c) 範囲 `[['004dfe9c', '004dfea3']]`
  - `CONDITIONAL_JUMP` [`004dfea0`](#insn-004dfea0) → [`004dfeac`](#insn-004dfeac)
  - `FALL_THROUGH` [`004dfea0`](#insn-004dfea0) → [`004dfea4`](#insn-004dfea4)
- ブロック [`004dfea4`](#insn-004dfea4) 範囲 `[['004dfea4', '004dfeab']]`
  - `CONDITIONAL_JUMP` [`004dfea8`](#insn-004dfea8) → [`004dfe9c`](#insn-004dfe9c)
  - `FALL_THROUGH` [`004dfea8`](#insn-004dfea8) → [`004dfeac`](#insn-004dfeac)
- ブロック [`004dfeac`](#insn-004dfeac) 範囲 `[['004dfeac', '004dfebb']]`
  - `CONDITIONAL_JUMP` [`004dfeb8`](#insn-004dfeb8) → [`004dfed0`](#insn-004dfed0)
  - `FALL_THROUGH` [`004dfeb8`](#insn-004dfeb8) → [`004dfebc`](#insn-004dfebc)
- ブロック [`004dfebc`](#insn-004dfebc) 範囲 `[['004dfebc', '004dfebf']]`
  - `FALL_THROUGH` [`004dfebc`](#insn-004dfebc) → [`004dfec0`](#insn-004dfec0)
- ブロック [`004dfec0`](#insn-004dfec0) 範囲 `[['004dfec0', '004dfec7']]`
  - `CONDITIONAL_JUMP` [`004dfec4`](#insn-004dfec4) → [`004dfed0`](#insn-004dfed0)
  - `FALL_THROUGH` [`004dfec4`](#insn-004dfec4) → [`004dfec8`](#insn-004dfec8)
- ブロック [`004dfec8`](#insn-004dfec8) 範囲 `[['004dfec8', '004dfecf']]`
  - `CONDITIONAL_JUMP` [`004dfecc`](#insn-004dfecc) → [`004dfec0`](#insn-004dfec0)
  - `FALL_THROUGH` [`004dfecc`](#insn-004dfecc) → [`004dfed0`](#insn-004dfed0)
- ブロック [`004dfed0`](#insn-004dfed0) 範囲 `[['004dfed0', '004dfedf']]`
  - `CONDITIONAL_JUMP` [`004dfedc`](#insn-004dfedc) → [`004dff54`](#insn-004dff54)
  - `FALL_THROUGH` [`004dfedc`](#insn-004dfedc) → [`004dfee0`](#insn-004dfee0)
- ブロック [`004dfee0`](#insn-004dfee0) 範囲 `[['004dfee0', '004dfeef']]`
  - `CONDITIONAL_JUMP` [`004dfeec`](#insn-004dfeec) → [`004e0424`](#insn-004e0424)
  - `FALL_THROUGH` [`004dfeec`](#insn-004dfeec) → [`004dfef0`](#insn-004dfef0)
- ブロック [`004dfef0`](#insn-004dfef0) 範囲 `[['004dfef0', '004dff17']]`
- ブロック [`004dff18`](#insn-004dff18) 範囲 `[['004dff18', '004dff1f']]`
  - `CONDITIONAL_JUMP` [`004dff1c`](#insn-004dff1c) → [`004dffd0`](#insn-004dffd0)
  - `FALL_THROUGH` [`004dff1c`](#insn-004dff1c) → [`004dff20`](#insn-004dff20)
- ブロック [`004dff20`](#insn-004dff20) 範囲 `[['004dff20', '004dff2f']]`
  - `CONDITIONAL_JUMP` [`004dff2c`](#insn-004dff2c) → [`004e0424`](#insn-004e0424)
  - `FALL_THROUGH` [`004dff2c`](#insn-004dff2c) → [`004dff30`](#insn-004dff30)
- ブロック [`004dff30`](#insn-004dff30) 範囲 `[['004dff30', '004dff53']]`
- ブロック [`004dff54`](#insn-004dff54) 範囲 `[['004dff54', '004dff7b']]`
  - `CONDITIONAL_JUMP` [`004dff78`](#insn-004dff78) → [`004e0024`](#insn-004e0024)
  - `FALL_THROUGH` [`004dff78`](#insn-004dff78) → [`004dff7c`](#insn-004dff7c)
- ブロック [`004dff7c`](#insn-004dff7c) 範囲 `[['004dff7c', '004dff8b']]`
  - `CONDITIONAL_JUMP` [`004dff88`](#insn-004dff88) → [`004dffa0`](#insn-004dffa0)
  - `FALL_THROUGH` [`004dff88`](#insn-004dff88) → [`004dff8c`](#insn-004dff8c)
- ブロック [`004dff8c`](#insn-004dff8c) 範囲 `[['004dff8c', '004dff8f']]`
  - `FALL_THROUGH` [`004dff8c`](#insn-004dff8c) → [`004dff90`](#insn-004dff90)
- ブロック [`004dff90`](#insn-004dff90) 範囲 `[['004dff90', '004dff97']]`
  - `CONDITIONAL_JUMP` [`004dff94`](#insn-004dff94) → [`004dffa0`](#insn-004dffa0)
  - `FALL_THROUGH` [`004dff94`](#insn-004dff94) → [`004dff98`](#insn-004dff98)
- ブロック [`004dff98`](#insn-004dff98) 範囲 `[['004dff98', '004dff9f']]`
  - `CONDITIONAL_JUMP` [`004dff9c`](#insn-004dff9c) → [`004dff90`](#insn-004dff90)
  - `FALL_THROUGH` [`004dff9c`](#insn-004dff9c) → [`004dffa0`](#insn-004dffa0)
- ブロック [`004dffa0`](#insn-004dffa0) 範囲 `[['004dffa0', '004dffb7']]`
  - `CONDITIONAL_JUMP` [`004dffb4`](#insn-004dffb4) → [`004e0008`](#insn-004e0008)
  - `FALL_THROUGH` [`004dffb4`](#insn-004dffb4) → [`004dffb8`](#insn-004dffb8)
- ブロック [`004dffb8`](#insn-004dffb8) 範囲 `[['004dffb8', '004dffbb']]`
  - `FALL_THROUGH` [`004dffb8`](#insn-004dffb8) → [`004dffbc`](#insn-004dffbc)
- ブロック [`004dffbc`](#insn-004dffbc) 範囲 `[['004dffbc', '004dffc3']]`
  - `CONDITIONAL_JUMP` [`004dffc0`](#insn-004dffc0) → [`004e0008`](#insn-004e0008)
  - `FALL_THROUGH` [`004dffc0`](#insn-004dffc0) → [`004dffc4`](#insn-004dffc4)
- ブロック [`004dffc4`](#insn-004dffc4) 範囲 `[['004dffc4', '004dffcb']]`
  - `CONDITIONAL_JUMP` [`004dffc8`](#insn-004dffc8) → [`004dffbc`](#insn-004dffbc)
  - `FALL_THROUGH` [`004dffc8`](#insn-004dffc8) → [`004dffcc`](#insn-004dffcc)
- ブロック [`004dffcc`](#insn-004dffcc) 範囲 `[['004dffcc', '004dffcf']]`
  - `UNCONDITIONAL_JUMP` [`004dffcc`](#insn-004dffcc) → [`004e001c`](#insn-004e001c)
- ブロック [`004dffd0`](#insn-004dffd0) 範囲 `[['004dffd0', '004dffdf']]`
  - `CONDITIONAL_JUMP` [`004dffdc`](#insn-004dffdc) → [`004e0424`](#insn-004e0424)
  - `FALL_THROUGH` [`004dffdc`](#insn-004dffdc) → [`004dffe0`](#insn-004dffe0)
- ブロック [`004dffe0`](#insn-004dffe0) 範囲 `[['004dffe0', '004e0007']]`
- ブロック [`004e0008`](#insn-004e0008) 範囲 `[['004e0008', '004e000b']]`
  - `CONDITIONAL_JUMP` [`004e0008`](#insn-004e0008) → [`004e001c`](#insn-004e001c)
  - `FALL_THROUGH` [`004e0008`](#insn-004e0008) → [`004e000c`](#insn-004e000c)
- ブロック [`004e000c`](#insn-004e000c) 範囲 `[['004e000c', '004e0013']]`
  - `CONDITIONAL_JUMP` [`004e0010`](#insn-004e0010) → [`004e0024`](#insn-004e0024)
  - `FALL_THROUGH` [`004e0010`](#insn-004e0010) → [`004e0014`](#insn-004e0014)
- ブロック [`004e0014`](#insn-004e0014) 範囲 `[['004e0014', '004e001b']]`
  - `CONDITIONAL_JUMP` [`004e0018`](#insn-004e0018) → [`004e000c`](#insn-004e000c)
  - `FALL_THROUGH` [`004e0018`](#insn-004e0018) → [`004e001c`](#insn-004e001c)
- ブロック [`004e001c`](#insn-004e001c) 範囲 `[['004e001c', '004e0023']]`
  - `FALL_THROUGH` [`004e0020`](#insn-004e0020) → [`004e0024`](#insn-004e0024)
- ブロック [`004e0024`](#insn-004e0024) 範囲 `[['004e0024', '004e003f']]`
  - `CONDITIONAL_JUMP` [`004e003c`](#insn-004e003c) → [`004e00b4`](#insn-004e00b4)
  - `FALL_THROUGH` [`004e003c`](#insn-004e003c) → [`004e0040`](#insn-004e0040)
- ブロック [`004e0040`](#insn-004e0040) 範囲 `[['004e0040', '004e0053']]`
  - `CONDITIONAL_JUMP` [`004e0050`](#insn-004e0050) → [`004e0068`](#insn-004e0068)
  - `FALL_THROUGH` [`004e0050`](#insn-004e0050) → [`004e0054`](#insn-004e0054)
- ブロック [`004e0054`](#insn-004e0054) 範囲 `[['004e0054', '004e0057']]`
  - `FALL_THROUGH` [`004e0054`](#insn-004e0054) → [`004e0058`](#insn-004e0058)
- ブロック [`004e0058`](#insn-004e0058) 範囲 `[['004e0058', '004e005f']]`
  - `CONDITIONAL_JUMP` [`004e005c`](#insn-004e005c) → [`004e0068`](#insn-004e0068)
  - `FALL_THROUGH` [`004e005c`](#insn-004e005c) → [`004e0060`](#insn-004e0060)
- ブロック [`004e0060`](#insn-004e0060) 範囲 `[['004e0060', '004e0067']]`
  - `CONDITIONAL_JUMP` [`004e0064`](#insn-004e0064) → [`004e0058`](#insn-004e0058)
  - `FALL_THROUGH` [`004e0064`](#insn-004e0064) → [`004e0068`](#insn-004e0068)
- ブロック [`004e0068`](#insn-004e0068) 範囲 `[['004e0068', '004e007f']]`
  - `CONDITIONAL_JUMP` [`004e007c`](#insn-004e007c) → [`004e0098`](#insn-004e0098)
  - `FALL_THROUGH` [`004e007c`](#insn-004e007c) → [`004e0080`](#insn-004e0080)
- ブロック [`004e0080`](#insn-004e0080) 範囲 `[['004e0080', '004e0083']]`
  - `FALL_THROUGH` [`004e0080`](#insn-004e0080) → [`004e0084`](#insn-004e0084)
- ブロック [`004e0084`](#insn-004e0084) 範囲 `[['004e0084', '004e008b']]`
  - `CONDITIONAL_JUMP` [`004e0088`](#insn-004e0088) → [`004e0098`](#insn-004e0098)
  - `FALL_THROUGH` [`004e0088`](#insn-004e0088) → [`004e008c`](#insn-004e008c)
- ブロック [`004e008c`](#insn-004e008c) 範囲 `[['004e008c', '004e0093']]`
  - `CONDITIONAL_JUMP` [`004e0090`](#insn-004e0090) → [`004e0084`](#insn-004e0084)
  - `FALL_THROUGH` [`004e0090`](#insn-004e0090) → [`004e0094`](#insn-004e0094)
- ブロック [`004e0094`](#insn-004e0094) 範囲 `[['004e0094', '004e0097']]`
  - `UNCONDITIONAL_JUMP` [`004e0094`](#insn-004e0094) → [`004e00ac`](#insn-004e00ac)
- ブロック [`004e0098`](#insn-004e0098) 範囲 `[['004e0098', '004e009b']]`
  - `CONDITIONAL_JUMP` [`004e0098`](#insn-004e0098) → [`004e00ac`](#insn-004e00ac)
  - `FALL_THROUGH` [`004e0098`](#insn-004e0098) → [`004e009c`](#insn-004e009c)
- ブロック [`004e009c`](#insn-004e009c) 範囲 `[['004e009c', '004e00a3']]`
  - `CONDITIONAL_JUMP` [`004e00a0`](#insn-004e00a0) → [`004e00b4`](#insn-004e00b4)
  - `FALL_THROUGH` [`004e00a0`](#insn-004e00a0) → [`004e00a4`](#insn-004e00a4)
- ブロック [`004e00a4`](#insn-004e00a4) 範囲 `[['004e00a4', '004e00ab']]`
  - `CONDITIONAL_JUMP` [`004e00a8`](#insn-004e00a8) → [`004e009c`](#insn-004e009c)
  - `FALL_THROUGH` [`004e00a8`](#insn-004e00a8) → [`004e00ac`](#insn-004e00ac)
- ブロック [`004e00ac`](#insn-004e00ac) 範囲 `[['004e00ac', '004e00b3']]`
  - `FALL_THROUGH` [`004e00b0`](#insn-004e00b0) → [`004e00b4`](#insn-004e00b4)
- ブロック [`004e00b4`](#insn-004e00b4) 範囲 `[['004e00b4', '004e00d3']]`
  - `CONDITIONAL_JUMP` [`004e00d0`](#insn-004e00d0) → [`004e0118`](#insn-004e0118)
  - `FALL_THROUGH` [`004e00d0`](#insn-004e00d0) → [`004e00d4`](#insn-004e00d4)
- ブロック [`004e00d4`](#insn-004e00d4) 範囲 `[['004e00d4', '004e00eb']]`
  - `CONDITIONAL_JUMP` [`004e00e8`](#insn-004e00e8) → [`004e012c`](#insn-004e012c)
  - `FALL_THROUGH` [`004e00e8`](#insn-004e00e8) → [`004e00ec`](#insn-004e00ec)
- ブロック [`004e00ec`](#insn-004e00ec) 範囲 `[['004e00ec', '004e00f7']]`
  - `CONDITIONAL_JUMP` [`004e00f4`](#insn-004e00f4) → [`004e0110`](#insn-004e0110)
  - `FALL_THROUGH` [`004e00f4`](#insn-004e00f4) → [`004e00f8`](#insn-004e00f8)
- ブロック [`004e00f8`](#insn-004e00f8) 範囲 `[['004e00f8', '004e00ff']]`
  - `CONDITIONAL_JUMP` [`004e00fc`](#insn-004e00fc) → [`004e0110`](#insn-004e0110)
  - `FALL_THROUGH` [`004e00fc`](#insn-004e00fc) → [`004e0100`](#insn-004e0100)
- ブロック [`004e0100`](#insn-004e0100) 範囲 `[['004e0100', '004e010f']]`
  - `FALL_THROUGH` [`004e010c`](#insn-004e010c) → [`004e0110`](#insn-004e0110)
- ブロック [`004e0110`](#insn-004e0110) 範囲 `[['004e0110', '004e0117']]`
  - `UNCONDITIONAL_JUMP` [`004e0114`](#insn-004e0114) → [`004e012c`](#insn-004e012c)
- ブロック [`004e0118`](#insn-004e0118) 範囲 `[['004e0118', '004e0123']]`
  - `CONDITIONAL_JUMP` [`004e0120`](#insn-004e0120) → [`004e012c`](#insn-004e012c)
  - `FALL_THROUGH` [`004e0120`](#insn-004e0120) → [`004e0124`](#insn-004e0124)
- ブロック [`004e0124`](#insn-004e0124) 範囲 `[['004e0124', '004e012b']]`
  - `FALL_THROUGH` [`004e0128`](#insn-004e0128) → [`004e012c`](#insn-004e012c)
- ブロック [`004e012c`](#insn-004e012c) 範囲 `[['004e012c', '004e0157']]`
  - `CONDITIONAL_JUMP` [`004e0154`](#insn-004e0154) → [`004e0194`](#insn-004e0194)
  - `FALL_THROUGH` [`004e0154`](#insn-004e0154) → [`004e0158`](#insn-004e0158)
- ブロック [`004e0158`](#insn-004e0158) 範囲 `[['004e0158', '004e0167']]`
  - `CONDITIONAL_JUMP` [`004e0164`](#insn-004e0164) → [`004e01a4`](#insn-004e01a4)
  - `FALL_THROUGH` [`004e0164`](#insn-004e0164) → [`004e0168`](#insn-004e0168)
- ブロック [`004e0168`](#insn-004e0168) 範囲 `[['004e0168', '004e0173']]`
  - `CONDITIONAL_JUMP` [`004e0170`](#insn-004e0170) → [`004e018c`](#insn-004e018c)
  - `FALL_THROUGH` [`004e0170`](#insn-004e0170) → [`004e0174`](#insn-004e0174)
- ブロック [`004e0174`](#insn-004e0174) 範囲 `[['004e0174', '004e017b']]`
  - `CONDITIONAL_JUMP` [`004e0178`](#insn-004e0178) → [`004e018c`](#insn-004e018c)
  - `FALL_THROUGH` [`004e0178`](#insn-004e0178) → [`004e017c`](#insn-004e017c)
- ブロック [`004e017c`](#insn-004e017c) 範囲 `[['004e017c', '004e018b']]`
  - `FALL_THROUGH` [`004e0188`](#insn-004e0188) → [`004e018c`](#insn-004e018c)
- ブロック [`004e018c`](#insn-004e018c) 範囲 `[['004e018c', '004e0193']]`
  - `UNCONDITIONAL_JUMP` [`004e0190`](#insn-004e0190) → [`004e01a4`](#insn-004e01a4)
- ブロック [`004e0194`](#insn-004e0194) 範囲 `[['004e0194', '004e019b']]`
  - `CONDITIONAL_JUMP` [`004e0198`](#insn-004e0198) → [`004e01a4`](#insn-004e01a4)
  - `FALL_THROUGH` [`004e0198`](#insn-004e0198) → [`004e019c`](#insn-004e019c)
- ブロック [`004e019c`](#insn-004e019c) 範囲 `[['004e019c', '004e01a3']]`
  - `FALL_THROUGH` [`004e01a0`](#insn-004e01a0) → [`004e01a4`](#insn-004e01a4)
- ブロック [`004e01a4`](#insn-004e01a4) 範囲 `[['004e01a4', '004e01b7']]`
  - `CONDITIONAL_JUMP` [`004e01b4`](#insn-004e01b4) → [`004e0248`](#insn-004e0248)
  - `FALL_THROUGH` [`004e01b4`](#insn-004e01b4) → [`004e01b8`](#insn-004e01b8)
- ブロック [`004e01b8`](#insn-004e01b8) 範囲 `[['004e01b8', '004e021f']]`
  - `CONDITIONAL_JUMP` [`004e021c`](#insn-004e021c) → [`004e0248`](#insn-004e0248)
  - `FALL_THROUGH` [`004e021c`](#insn-004e021c) → [`004e0220`](#insn-004e0220)
- ブロック [`004e0220`](#insn-004e0220) 範囲 `[['004e0220', '004e0247']]`
  - `FALL_THROUGH` [`004e0244`](#insn-004e0244) → [`004e0248`](#insn-004e0248)
- ブロック [`004e0248`](#insn-004e0248) 範囲 `[['004e0248', '004e025b']]`
  - `CONDITIONAL_JUMP` [`004e0258`](#insn-004e0258) → [`004e026c`](#insn-004e026c)
  - `FALL_THROUGH` [`004e0258`](#insn-004e0258) → [`004e025c`](#insn-004e025c)
- ブロック [`004e025c`](#insn-004e025c) 範囲 `[['004e025c', '004e026b']]`
  - `UNCONDITIONAL_JUMP` [`004e0268`](#insn-004e0268) → [`004e0248`](#insn-004e0248)
- ブロック [`004e026c`](#insn-004e026c) 範囲 `[['004e026c', '004e0277']]`
  - `CONDITIONAL_JUMP` [`004e0274`](#insn-004e0274) → [`004e029c`](#insn-004e029c)
  - `FALL_THROUGH` [`004e0274`](#insn-004e0274) → [`004e0278`](#insn-004e0278)
- ブロック [`004e0278`](#insn-004e0278) 範囲 `[['004e0278', '004e029b']]`
  - `UNCONDITIONAL_JUMP` [`004e0298`](#insn-004e0298) → [`004e02dc`](#insn-004e02dc)
- ブロック [`004e029c`](#insn-004e029c) 範囲 `[['004e029c', '004e02b3']]`
  - `CONDITIONAL_JUMP` [`004e02b0`](#insn-004e02b0) → [`004e02dc`](#insn-004e02dc)
  - `FALL_THROUGH` [`004e02b0`](#insn-004e02b0) → [`004e02b4`](#insn-004e02b4)
- ブロック [`004e02b4`](#insn-004e02b4) 範囲 `[['004e02b4', '004e02db']]`
  - `FALL_THROUGH` [`004e02d8`](#insn-004e02d8) → [`004e02dc`](#insn-004e02dc)
- ブロック [`004e02dc`](#insn-004e02dc) 範囲 `[['004e02dc', '004e02e3']]`
  - `CONDITIONAL_JUMP` [`004e02e0`](#insn-004e02e0) → [`004e030c`](#insn-004e030c)
  - `FALL_THROUGH` [`004e02e0`](#insn-004e02e0) → [`004e02e4`](#insn-004e02e4)
- ブロック [`004e02e4`](#insn-004e02e4) 範囲 `[['004e02e4', '004e030b']]`
  - `FALL_THROUGH` [`004e0308`](#insn-004e0308) → [`004e030c`](#insn-004e030c)
- ブロック [`004e030c`](#insn-004e030c) 範囲 `[['004e030c', '004e031b']]`
  - `CONDITIONAL_JUMP` [`004e0318`](#insn-004e0318) → [`004e0424`](#insn-004e0424)
  - `FALL_THROUGH` [`004e0318`](#insn-004e0318) → [`004e031c`](#insn-004e031c)
- ブロック [`004e031c`](#insn-004e031c) 範囲 `[['004e031c', '004e0337']]`
- ブロック [`004e0338`](#insn-004e0338) 範囲 `[['004e0338', '004e0373']]`
  - `CONDITIONAL_JUMP` [`004e0370`](#insn-004e0370) → [`004e0424`](#insn-004e0424)
  - `FALL_THROUGH` [`004e0370`](#insn-004e0370) → [`004e0374`](#insn-004e0374)
- ブロック [`004e0374`](#insn-004e0374) 範囲 `[['004e0374', '004e038f']]`
- ブロック [`004e0424`](#insn-004e0424) 範囲 `[['004e0424', '004e0427']]`

## 命令位置別の参照

- [`004dfe00`](#insn-004dfe00) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe04`](#insn-004dfe04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe08`](#insn-004dfe08) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe0c`](#insn-004dfe0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe10`](#insn-004dfe10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe20`](#insn-004dfe20) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe28`](#insn-004dfe28) → [`004e0338`](#insn-004e0338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe4c`](#insn-004dfe4c) → [`004dfe64`](#insn-004dfe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe58`](#insn-004dfe58) → [`004dfe64`](#insn-004dfe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe60`](#insn-004dfe60) → [`004dfe54`](#insn-004dfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe70`](#insn-004dfe70) → [`004dfe88`](#insn-004dfe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe7c`](#insn-004dfe7c) → [`004dfe88`](#insn-004dfe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe84`](#insn-004dfe84) → [`004dfe78`](#insn-004dfe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe8c`](#insn-004dfe8c) → [`004b87b4`](../004b8/004b87b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b87b4` · 推定シンボル `None` · 推定型 `None`
- [`004dfe90`](#insn-004dfe90) → [`004dff18`](#insn-004dff18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfe98`](#insn-004dfe98) → [`004dfeac`](#insn-004dfeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfea0`](#insn-004dfea0) → [`004dfeac`](#insn-004dfeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfea8`](#insn-004dfea8) → [`004dfe9c`](#insn-004dfe9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfeb8`](#insn-004dfeb8) → [`004dfed0`](#insn-004dfed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfec4`](#insn-004dfec4) → [`004dfed0`](#insn-004dfed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfecc`](#insn-004dfecc) → [`004dfec0`](#insn-004dfec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfed8`](#insn-004dfed8) → [`004b87b4`](../004b8/004b87b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b87b4` · 推定シンボル `None` · 推定型 `None`
- [`004dfedc`](#insn-004dfedc) → [`004dff54`](#insn-004dff54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfee4`](#insn-004dfee4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfeec`](#insn-004dfeec) → [`004e0424`](#insn-004e0424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfefc`](#insn-004dfefc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff00`](#insn-004dff00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff04`](#insn-004dff04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff08`](#insn-004dff08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff0c`](#insn-004dff0c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff14`](#insn-004dff14) → [`00c58ca0`](../00c58/00c58ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ca0` · 推定シンボル `None` · 推定型 `None`
- [`004dff1c`](#insn-004dff1c) → [`004dffd0`](#insn-004dffd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff24`](#insn-004dff24) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff2c`](#insn-004dff2c) → [`004e0424`](#insn-004e0424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff38`](#insn-004dff38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff3c`](#insn-004dff3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff40`](#insn-004dff40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff44`](#insn-004dff44) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff48`](#insn-004dff48) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff50`](#insn-004dff50) → [`00c58b40`](../00c58/00c58b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b40` · 推定シンボル `None` · 推定型 `None`
- [`004dff5c`](#insn-004dff5c) → [`00c58b40`](../00c58/00c58b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b40` · 推定シンボル `None` · 推定型 `None`
- [`004dff64`](#insn-004dff64) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff70`](#insn-004dff70) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff78`](#insn-004dff78) → [`004e0024`](#insn-004e0024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff88`](#insn-004dff88) → [`004dffa0`](#insn-004dffa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff94`](#insn-004dff94) → [`004dffa0`](#insn-004dffa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dff9c`](#insn-004dff9c) → [`004dff90`](#insn-004dff90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffa4`](#insn-004dffa4) → [`004b9c38`](../004b9/004b9c38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b9c38` · 推定シンボル `None` · 推定型 `None`
- [`004dffa8`](#insn-004dffa8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffb4`](#insn-004dffb4) → [`004e0008`](#insn-004e0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffc0`](#insn-004dffc0) → [`004e0008`](#insn-004e0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffc8`](#insn-004dffc8) → [`004dffbc`](#insn-004dffbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffcc`](#insn-004dffcc) → [`004e001c`](#insn-004e001c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffd4`](#insn-004dffd4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffdc`](#insn-004dffdc) → [`004e0424`](#insn-004e0424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dffec`](#insn-004dffec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfff0`](#insn-004dfff0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfff4`](#insn-004dfff4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfff8`](#insn-004dfff8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfffc`](#insn-004dfffc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0004`](#insn-004e0004) → [`00c58cb0`](../00c58/00c58cb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58cb0` · 推定シンボル `None` · 推定型 `None`
- [`004e0008`](#insn-004e0008) → [`004e001c`](#insn-004e001c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0010`](#insn-004e0010) → [`004e0024`](#insn-004e0024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0018`](#insn-004e0018) → [`004e000c`](#insn-004e000c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0020`](#insn-004e0020) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e002c`](#insn-004e002c) → [`00c58ac0`](../00c58/00c58ac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ac0` · 推定シンボル `None` · 推定型 `None`
- [`004e003c`](#insn-004e003c) → [`004e00b4`](#insn-004e00b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0040`](#insn-004e0040) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0050`](#insn-004e0050) → [`004e0068`](#insn-004e0068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e005c`](#insn-004e005c) → [`004e0068`](#insn-004e0068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0064`](#insn-004e0064) → [`004e0058`](#insn-004e0058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e006c`](#insn-004e006c) → [`004b9c38`](../004b9/004b9c38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b9c38` · 推定シンボル `None` · 推定型 `None`
- [`004e0070`](#insn-004e0070) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e007c`](#insn-004e007c) → [`004e0098`](#insn-004e0098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0088`](#insn-004e0088) → [`004e0098`](#insn-004e0098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0090`](#insn-004e0090) → [`004e0084`](#insn-004e0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0094`](#insn-004e0094) → [`004e00ac`](#insn-004e00ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0098`](#insn-004e0098) → [`004e00ac`](#insn-004e00ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00a0`](#insn-004e00a0) → [`004e00b4`](#insn-004e00b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00a8`](#insn-004e00a8) → [`004e009c`](#insn-004e009c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00b0`](#insn-004e00b0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00bc`](#insn-004e00bc) → [`00c58ac0`](../00c58/00c58ac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ac0` · 推定シンボル `None` · 推定型 `None`
- [`004e00c4`](#insn-004e00c4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00d0`](#insn-004e00d0) → [`004e0118`](#insn-004e0118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00d4`](#insn-004e00d4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00e8`](#insn-004e00e8) → [`004e012c`](#insn-004e012c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00f4`](#insn-004e00f4) → [`004e0110`](#insn-004e0110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e00fc`](#insn-004e00fc) → [`004e0110`](#insn-004e0110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0108`](#insn-004e0108) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`004e010c`](#insn-004e010c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0114`](#insn-004e0114) → [`004e012c`](#insn-004e012c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0118`](#insn-004e0118) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0120`](#insn-004e0120) → [`004e012c`](#insn-004e012c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0128`](#insn-004e0128) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`004e0134`](#insn-004e0134) → [`00c58b40`](../00c58/00c58b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b40` · 推定シンボル `None` · 推定型 `None`
- [`004e0140`](#insn-004e0140) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0148`](#insn-004e0148) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0154`](#insn-004e0154) → [`004e0194`](#insn-004e0194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0164`](#insn-004e0164) → [`004e01a4`](#insn-004e01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0170`](#insn-004e0170) → [`004e018c`](#insn-004e018c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0178`](#insn-004e0178) → [`004e018c`](#insn-004e018c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0184`](#insn-004e0184) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`004e0188`](#insn-004e0188) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0190`](#insn-004e0190) → [`004e01a4`](#insn-004e01a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0198`](#insn-004e0198) → [`004e01a4`](#insn-004e01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01a0`](#insn-004e01a0) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`004e01ac`](#insn-004e01ac) → [`00c58c40`](../00c58/00c58c40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58c40` · 推定シンボル `None` · 推定型 `None`
- [`004e01b0`](#insn-004e01b0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01b4`](#insn-004e01b4) → [`004e0248`](#insn-004e0248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01c0`](#insn-004e01c0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01c4`](#insn-004e01c4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01e4`](#insn-004e01e4) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e01f4`](#insn-004e01f4) → [`00540920`](../00540/00540920.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00540920` · 推定シンボル `None` · 推定型 `None`
- [`004e01f8`](#insn-004e01f8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0214`](#insn-004e0214) → [`00c58ad0`](../00c58/00c58ad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ad0` · 推定シンボル `None` · 推定型 `None`
- [`004e0218`](#insn-004e0218) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e021c`](#insn-004e021c) → [`004e0248`](#insn-004e0248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0220`](#insn-004e0220) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0224`](#insn-004e0224) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e022c`](#insn-004e022c) → `00c67738`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e023c`](#insn-004e023c) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004e0244`](#insn-004e0244) → [`00c58660`](../00c58/00c58660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58660` · 推定シンボル `None` · 推定型 `None`
- [`004e0254`](#insn-004e0254) → [`00c58b20`](../00c58/00c58b20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b20` · 推定シンボル `None` · 推定型 `None`
- [`004e0258`](#insn-004e0258) → [`004e026c`](#insn-004e026c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0264`](#insn-004e0264) → [`00c58c40`](../00c58/00c58c40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58c40` · 推定シンボル `None` · 推定型 `None`
- [`004e0268`](#insn-004e0268) → [`004e0248`](#insn-004e0248) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0274`](#insn-004e0274) → [`004e029c`](#insn-004e029c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0278`](#insn-004e0278) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e027c`](#insn-004e027c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0280`](#insn-004e0280) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0284`](#insn-004e0284) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e028c`](#insn-004e028c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0298`](#insn-004e0298) → [`004e02dc`](#insn-004e02dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02a8`](#insn-004e02a8) → [`00c58cc0`](../00c58/00c58cc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58cc0` · 推定シンボル `None` · 推定型 `None`
- [`004e02ac`](#insn-004e02ac) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02b0`](#insn-004e02b0) → [`004e02dc`](#insn-004e02dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02b4`](#insn-004e02b4) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02b8`](#insn-004e02b8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02c0`](#insn-004e02c0) → `00c67738`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e02d0`](#insn-004e02d0) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004e02d8`](#insn-004e02d8) → [`00c58660`](../00c58/00c58660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58660` · 推定シンボル `None` · 推定型 `None`
- [`004e02dc`](#insn-004e02dc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02e0`](#insn-004e02e0) → [`004e030c`](#insn-004e030c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02e4`](#insn-004e02e4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02e8`](#insn-004e02e8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e02f0`](#insn-004e02f0) → `00c67738`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e0300`](#insn-004e0300) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004e0308`](#insn-004e0308) → [`00c58660`](../00c58/00c58660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58660` · 推定シンボル `None` · 推定型 `None`
- [`004e0310`](#insn-004e0310) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0318`](#insn-004e0318) → [`004e0424`](#insn-004e0424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e031c`](#insn-004e031c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0320`](#insn-004e0320) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0324`](#insn-004e0324) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0328`](#insn-004e0328) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e032c`](#insn-004e032c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e033c`](#insn-004e033c) → [`00c57ef0`](../00c57/00c57ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ef0` · 推定シンボル `None` · 推定型 `None`
- [`004e0348`](#insn-004e0348) → `002bd943`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004e0350`](#insn-004e0350) → [`0043ddd8`](../0043d/0043ddd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043ddd8` · 推定シンボル `None` · 推定型 `None`
- [`004e0360`](#insn-004e0360) → [`004aec64`](../004ae/004aec64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004aec64` · 推定シンボル `None` · 推定型 `None`
- [`004e0368`](#insn-004e0368) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e0370`](#insn-004e0370) → [`004e0424`](#insn-004e0424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004e037c`](#insn-004e037c) → [`00535868`](../00535/00535868.md) · `PARAM` · `ANALYSIS` · 関数 `00535868` · 推定シンボル `None` · 推定型 `None`
- [`004e0380`](#insn-004e0380) → `00c9ad48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004e0380`](#insn-004e0380) → `00c66398`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan13Invalid_StateE` · 推定型 `pointer __((offset(0x10)))`
- [`004e038c`](#insn-004e038c) → [`00c57f10`](../00c57/00c57f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f10` · 推定シンボル `None` · 推定型 `None`
- [`004e0424`](#insn-004e0424) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004dfe00`](#insn-004dfe00)

~~~json
{
  "source": "004dfe00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe04`](#insn-004dfe04)

~~~json
{
  "source": "004dfe04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe08`](#insn-004dfe08)

~~~json
{
  "source": "004dfe08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe0c`](#insn-004dfe0c)

~~~json
{
  "source": "004dfe0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe10`](#insn-004dfe10)

~~~json
{
  "source": "004dfe10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe20`](#insn-004dfe20)

~~~json
{
  "source": "004dfe20",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe28`](#insn-004dfe28)

~~~json
{
  "source": "004dfe28",
  "target": "004e0338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe4c`](#insn-004dfe4c)

~~~json
{
  "source": "004dfe4c",
  "target": "004dfe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe58`](#insn-004dfe58)

~~~json
{
  "source": "004dfe58",
  "target": "004dfe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe60`](#insn-004dfe60)

~~~json
{
  "source": "004dfe60",
  "target": "004dfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe70`](#insn-004dfe70)

~~~json
{
  "source": "004dfe70",
  "target": "004dfe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe7c`](#insn-004dfe7c)

~~~json
{
  "source": "004dfe7c",
  "target": "004dfe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe84`](#insn-004dfe84)

~~~json
{
  "source": "004dfe84",
  "target": "004dfe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe8c`](#insn-004dfe8c)

~~~json
{
  "source": "004dfe8c",
  "target": "004b87b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfe90`](#insn-004dfe90)

~~~json
{
  "source": "004dfe90",
  "target": "004dff18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfe98`](#insn-004dfe98)

~~~json
{
  "source": "004dfe98",
  "target": "004dfeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfea0`](#insn-004dfea0)

~~~json
{
  "source": "004dfea0",
  "target": "004dfeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfea8`](#insn-004dfea8)

~~~json
{
  "source": "004dfea8",
  "target": "004dfe9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfeb8`](#insn-004dfeb8)

~~~json
{
  "source": "004dfeb8",
  "target": "004dfed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfec4`](#insn-004dfec4)

~~~json
{
  "source": "004dfec4",
  "target": "004dfed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfecc`](#insn-004dfecc)

~~~json
{
  "source": "004dfecc",
  "target": "004dfec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfed8`](#insn-004dfed8)

~~~json
{
  "source": "004dfed8",
  "target": "004b87b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfedc`](#insn-004dfedc)

~~~json
{
  "source": "004dfedc",
  "target": "004dff54",
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
  "target": "004e0424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfefc`](#insn-004dfefc)

~~~json
{
  "source": "004dfefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff00`](#insn-004dff00)

~~~json
{
  "source": "004dff00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff04`](#insn-004dff04)

~~~json
{
  "source": "004dff04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff08`](#insn-004dff08)

~~~json
{
  "source": "004dff08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff0c`](#insn-004dff0c)

~~~json
{
  "source": "004dff0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff14`](#insn-004dff14)

~~~json
{
  "source": "004dff14",
  "target": "00c58ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dff1c`](#insn-004dff1c)

~~~json
{
  "source": "004dff1c",
  "target": "004dffd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff24`](#insn-004dff24)

~~~json
{
  "source": "004dff24",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff2c`](#insn-004dff2c)

~~~json
{
  "source": "004dff2c",
  "target": "004e0424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff38`](#insn-004dff38)

~~~json
{
  "source": "004dff38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff3c`](#insn-004dff3c)

~~~json
{
  "source": "004dff3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff40`](#insn-004dff40)

~~~json
{
  "source": "004dff40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff44`](#insn-004dff44)

~~~json
{
  "source": "004dff44",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff48`](#insn-004dff48)

~~~json
{
  "source": "004dff48",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff50`](#insn-004dff50)

~~~json
{
  "source": "004dff50",
  "target": "00c58b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dff5c`](#insn-004dff5c)

~~~json
{
  "source": "004dff5c",
  "target": "00c58b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dff64`](#insn-004dff64)

~~~json
{
  "source": "004dff64",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff70`](#insn-004dff70)

~~~json
{
  "source": "004dff70",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff78`](#insn-004dff78)

~~~json
{
  "source": "004dff78",
  "target": "004e0024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff88`](#insn-004dff88)

~~~json
{
  "source": "004dff88",
  "target": "004dffa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff94`](#insn-004dff94)

~~~json
{
  "source": "004dff94",
  "target": "004dffa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dff9c`](#insn-004dff9c)

~~~json
{
  "source": "004dff9c",
  "target": "004dff90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffa4`](#insn-004dffa4)

~~~json
{
  "source": "004dffa4",
  "target": "004b9c38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dffa8`](#insn-004dffa8)

~~~json
{
  "source": "004dffa8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffb4`](#insn-004dffb4)

~~~json
{
  "source": "004dffb4",
  "target": "004e0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffc0`](#insn-004dffc0)

~~~json
{
  "source": "004dffc0",
  "target": "004e0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffc8`](#insn-004dffc8)

~~~json
{
  "source": "004dffc8",
  "target": "004dffbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffcc`](#insn-004dffcc)

~~~json
{
  "source": "004dffcc",
  "target": "004e001c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffd4`](#insn-004dffd4)

~~~json
{
  "source": "004dffd4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffdc`](#insn-004dffdc)

~~~json
{
  "source": "004dffdc",
  "target": "004e0424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dffec`](#insn-004dffec)

~~~json
{
  "source": "004dffec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfff0`](#insn-004dfff0)

~~~json
{
  "source": "004dfff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfff4`](#insn-004dfff4)

~~~json
{
  "source": "004dfff4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfff8`](#insn-004dfff8)

~~~json
{
  "source": "004dfff8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfffc`](#insn-004dfffc)

~~~json
{
  "source": "004dfffc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0004`](#insn-004e0004)

~~~json
{
  "source": "004e0004",
  "target": "00c58cb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0008`](#insn-004e0008)

~~~json
{
  "source": "004e0008",
  "target": "004e001c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0010`](#insn-004e0010)

~~~json
{
  "source": "004e0010",
  "target": "004e0024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0018`](#insn-004e0018)

~~~json
{
  "source": "004e0018",
  "target": "004e000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0020`](#insn-004e0020)

~~~json
{
  "source": "004e0020",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e002c`](#insn-004e002c)

~~~json
{
  "source": "004e002c",
  "target": "00c58ac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e003c`](#insn-004e003c)

~~~json
{
  "source": "004e003c",
  "target": "004e00b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0040`](#insn-004e0040)

~~~json
{
  "source": "004e0040",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0050`](#insn-004e0050)

~~~json
{
  "source": "004e0050",
  "target": "004e0068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e005c`](#insn-004e005c)

~~~json
{
  "source": "004e005c",
  "target": "004e0068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0064`](#insn-004e0064)

~~~json
{
  "source": "004e0064",
  "target": "004e0058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e006c`](#insn-004e006c)

~~~json
{
  "source": "004e006c",
  "target": "004b9c38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0070`](#insn-004e0070)

~~~json
{
  "source": "004e0070",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e007c`](#insn-004e007c)

~~~json
{
  "source": "004e007c",
  "target": "004e0098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0088`](#insn-004e0088)

~~~json
{
  "source": "004e0088",
  "target": "004e0098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0090`](#insn-004e0090)

~~~json
{
  "source": "004e0090",
  "target": "004e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0094`](#insn-004e0094)

~~~json
{
  "source": "004e0094",
  "target": "004e00ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0098`](#insn-004e0098)

~~~json
{
  "source": "004e0098",
  "target": "004e00ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00a0`](#insn-004e00a0)

~~~json
{
  "source": "004e00a0",
  "target": "004e00b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00a8`](#insn-004e00a8)

~~~json
{
  "source": "004e00a8",
  "target": "004e009c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00b0`](#insn-004e00b0)

~~~json
{
  "source": "004e00b0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00bc`](#insn-004e00bc)

~~~json
{
  "source": "004e00bc",
  "target": "00c58ac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e00c4`](#insn-004e00c4)

~~~json
{
  "source": "004e00c4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00d0`](#insn-004e00d0)

~~~json
{
  "source": "004e00d0",
  "target": "004e0118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00d4`](#insn-004e00d4)

~~~json
{
  "source": "004e00d4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00e8`](#insn-004e00e8)

~~~json
{
  "source": "004e00e8",
  "target": "004e012c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00f4`](#insn-004e00f4)

~~~json
{
  "source": "004e00f4",
  "target": "004e0110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e00fc`](#insn-004e00fc)

~~~json
{
  "source": "004e00fc",
  "target": "004e0110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0108`](#insn-004e0108)

~~~json
{
  "source": "004e0108",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e010c`](#insn-004e010c)

~~~json
{
  "source": "004e010c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0114`](#insn-004e0114)

~~~json
{
  "source": "004e0114",
  "target": "004e012c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0118`](#insn-004e0118)

~~~json
{
  "source": "004e0118",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0120`](#insn-004e0120)

~~~json
{
  "source": "004e0120",
  "target": "004e012c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0128`](#insn-004e0128)

~~~json
{
  "source": "004e0128",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0134`](#insn-004e0134)

~~~json
{
  "source": "004e0134",
  "target": "00c58b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0140`](#insn-004e0140)

~~~json
{
  "source": "004e0140",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
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
- 参照命令 [`004e0154`](#insn-004e0154)

~~~json
{
  "source": "004e0154",
  "target": "004e0194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0164`](#insn-004e0164)

~~~json
{
  "source": "004e0164",
  "target": "004e01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0170`](#insn-004e0170)

~~~json
{
  "source": "004e0170",
  "target": "004e018c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0178`](#insn-004e0178)

~~~json
{
  "source": "004e0178",
  "target": "004e018c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0184`](#insn-004e0184)

~~~json
{
  "source": "004e0184",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0188`](#insn-004e0188)

~~~json
{
  "source": "004e0188",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0190`](#insn-004e0190)

~~~json
{
  "source": "004e0190",
  "target": "004e01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0198`](#insn-004e0198)

~~~json
{
  "source": "004e0198",
  "target": "004e01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01a0`](#insn-004e01a0)

~~~json
{
  "source": "004e01a0",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e01ac`](#insn-004e01ac)

~~~json
{
  "source": "004e01ac",
  "target": "00c58c40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e01b0`](#insn-004e01b0)

~~~json
{
  "source": "004e01b0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01b4`](#insn-004e01b4)

~~~json
{
  "source": "004e01b4",
  "target": "004e0248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01c0`](#insn-004e01c0)

~~~json
{
  "source": "004e01c0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01c4`](#insn-004e01c4)

~~~json
{
  "source": "004e01c4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01e4`](#insn-004e01e4)

~~~json
{
  "source": "004e01e4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e01f4`](#insn-004e01f4)

~~~json
{
  "source": "004e01f4",
  "target": "00540920",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e01f8`](#insn-004e01f8)

~~~json
{
  "source": "004e01f8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0214`](#insn-004e0214)

~~~json
{
  "source": "004e0214",
  "target": "00c58ad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0218`](#insn-004e0218)

~~~json
{
  "source": "004e0218",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e021c`](#insn-004e021c)

~~~json
{
  "source": "004e021c",
  "target": "004e0248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0220`](#insn-004e0220)

~~~json
{
  "source": "004e0220",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0224`](#insn-004e0224)

~~~json
{
  "source": "004e0224",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e022c`](#insn-004e022c)

~~~json
{
  "source": "004e022c",
  "target": "00c67738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67738",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e023c`](#insn-004e023c)

~~~json
{
  "source": "004e023c",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0244`](#insn-004e0244)

~~~json
{
  "source": "004e0244",
  "target": "00c58660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0254`](#insn-004e0254)

~~~json
{
  "source": "004e0254",
  "target": "00c58b20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0258`](#insn-004e0258)

~~~json
{
  "source": "004e0258",
  "target": "004e026c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0264`](#insn-004e0264)

~~~json
{
  "source": "004e0264",
  "target": "00c58c40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0268`](#insn-004e0268)

~~~json
{
  "source": "004e0268",
  "target": "004e0248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0274`](#insn-004e0274)

~~~json
{
  "source": "004e0274",
  "target": "004e029c",
  "target_space": "ram",
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
- 参照命令 [`004e027c`](#insn-004e027c)

~~~json
{
  "source": "004e027c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0280`](#insn-004e0280)

~~~json
{
  "source": "004e0280",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0284`](#insn-004e0284)

~~~json
{
  "source": "004e0284",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e028c`](#insn-004e028c)

~~~json
{
  "source": "004e028c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0298`](#insn-004e0298)

~~~json
{
  "source": "004e0298",
  "target": "004e02dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02a8`](#insn-004e02a8)

~~~json
{
  "source": "004e02a8",
  "target": "00c58cc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e02ac`](#insn-004e02ac)

~~~json
{
  "source": "004e02ac",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02b0`](#insn-004e02b0)

~~~json
{
  "source": "004e02b0",
  "target": "004e02dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02b4`](#insn-004e02b4)

~~~json
{
  "source": "004e02b4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02b8`](#insn-004e02b8)

~~~json
{
  "source": "004e02b8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02c0`](#insn-004e02c0)

~~~json
{
  "source": "004e02c0",
  "target": "00c67738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67738",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e02d0`](#insn-004e02d0)

~~~json
{
  "source": "004e02d0",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e02d8`](#insn-004e02d8)

~~~json
{
  "source": "004e02d8",
  "target": "00c58660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e02dc`](#insn-004e02dc)

~~~json
{
  "source": "004e02dc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02e0`](#insn-004e02e0)

~~~json
{
  "source": "004e02e0",
  "target": "004e030c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02e4`](#insn-004e02e4)

~~~json
{
  "source": "004e02e4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02e8`](#insn-004e02e8)

~~~json
{
  "source": "004e02e8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e02f0`](#insn-004e02f0)

~~~json
{
  "source": "004e02f0",
  "target": "00c67738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67738",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e0300`](#insn-004e0300)

~~~json
{
  "source": "004e0300",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0308`](#insn-004e0308)

~~~json
{
  "source": "004e0308",
  "target": "00c58660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0310`](#insn-004e0310)

~~~json
{
  "source": "004e0310",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0318`](#insn-004e0318)

~~~json
{
  "source": "004e0318",
  "target": "004e0424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e031c`](#insn-004e031c)

~~~json
{
  "source": "004e031c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0320`](#insn-004e0320)

~~~json
{
  "source": "004e0320",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0324`](#insn-004e0324)

~~~json
{
  "source": "004e0324",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0328`](#insn-004e0328)

~~~json
{
  "source": "004e0328",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e032c`](#insn-004e032c)

~~~json
{
  "source": "004e032c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e033c`](#insn-004e033c)

~~~json
{
  "source": "004e033c",
  "target": "00c57ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0348`](#insn-004e0348)

~~~json
{
  "source": "004e0348",
  "target": "002bd943",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bd943",
  "offset": 0,
  "size": 34,
  "datatype": "string",
  "bytes": "4d6f64756c61725f526564756365723a204e6576657220696e6974616c697a65",
  "capture_start": "002bd943",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004e0350`](#insn-004e0350)

~~~json
{
  "source": "004e0350",
  "target": "0043ddd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0360`](#insn-004e0360)

~~~json
{
  "source": "004e0360",
  "target": "004aec64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0368`](#insn-004e0368)

~~~json
{
  "source": "004e0368",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e0370`](#insn-004e0370)

~~~json
{
  "source": "004e0370",
  "target": "004e0424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004e037c`](#insn-004e037c)

~~~json
{
  "source": "004e037c",
  "target": "00535868",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0380`](#insn-004e0380)

~~~json
{
  "source": "004e0380",
  "target": "00c9ad48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ad48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e0380`](#insn-004e0380)

~~~json
{
  "source": "004e0380",
  "target": "00c66398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66398",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004e038c`](#insn-004e038c)

~~~json
{
  "source": "004e038c",
  "target": "00c57f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004e0424`](#insn-004e0424)

~~~json
{
  "source": "004e0424",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
