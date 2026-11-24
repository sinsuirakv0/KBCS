# 009acfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009acf68`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009acf68.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0057.md#compare-b4765c8b2d318fb993e48eed01c9ec3c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `009adf68`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009adf68.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0024.md#compare-9272e7907da4a27ba98f79e428c52c88)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009acfbc",
  "name": "FUN_009acfbc",
  "size": 1284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "958c25bc65b1be87ed8b26e49158c4c58632388420545f9d11638bfdfe1415fb",
  "source_text_sha256": "958c25bc65b1be87ed8b26e49158c4c58632388420545f9d11638bfdfe1415fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009acfbc",
        "009ad48f"
      ],
      [
        "009ad4c8",
        "009ad4f7"
      ]
    ],
    "bytes_sha256": "78fe7719276c1bf2f5ea27a5affb211715247f03ab2eece25bc154742600bcf3",
    "instruction_count": 321,
    "instruction_bytes": 1284,
    "body_bytes": 1284,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

- [0075ebd8](../0075e/0075ebd8.md)

## 呼び出し先

- [00440f00](../00440/00440f00.md)
- [006b8c9c](../006b8/006b8c9c.md)
- [0080666c](../00806/0080666c.md)
- [009b0c3c](../009b0/009b0c3c.md)
- [009b0d98](../009b0/009b0d98.md)
- [009b0dac](../009b0/009b0dac.md)
- [009b1e30](../009b1/009b1e30.md)
- [009b41a8](../009b4/009b41a8.md)
- [009b5ce8](../009b5/009b5ce8.md)
- [009b5cf8](../009b5/009b5cf8.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 8994 bytes

~~~c

void FUN_009acfbc(undefined8 *param_1)

{
  undefined8 *puVar1;
  long **pplVar2;
  undefined8 *puVar3;
  long lVar4;
  ulong *puVar5;
  ulong *puVar6;
  ulong *__src;
  ulong *puVar7;
  int iVar8;
  undefined4 uVar9;
  ulong uVar10;
  ulong *puVar11;
  long *plVar12;
  ulong uVar13;
  long *plVar14;
  undefined8 uVar15;
  long lVar16;
  ulong uVar17;
  long *plVar18;
  long *local_a8;
  long *local_a0;
  long local_98;
  ulong *local_90;
  ulong *local_88;
  ulong *local_80;
  long **local_78;
  long *local_70;
  long local_68;
  
                    /* catch() { ... } // from try @ 009ace88 with catch @ 009acfbc */
  lVar4 = tpidr_el0;
  local_68 = *(long *)(lVar4 + 0x28);
  puVar1 = (undefined8 *)*param_1;
  puVar3 = (undefined8 *)param_1[1];
  local_90 = (ulong *)0x0;
  local_88 = (ulong *)0x0;
  local_80 = (ulong *)0x0;
  puVar11 = local_90;
  for (; local_90 = puVar11, puVar1 != puVar3; puVar1 = puVar1 + 2) {
    plVar14 = (long *)*puVar1;
    plVar18 = (long *)puVar1[1];
    local_a8 = plVar14;
    local_a0 = plVar18;
    puVar5 = puVar11;
    puVar6 = local_88;
    if (plVar18 != (long *)0x0) {
      FUN_00c53d70(1,plVar18 + 1);
      puVar11 = local_90;
      puVar5 = local_90;
      puVar6 = local_88;
    }
    for (; puVar7 = local_88, __src = local_90, local_90 = puVar5, puVar11 != local_88;
        puVar11 = puVar11 + 1) {
      uVar10 = *puVar11;
      local_88 = puVar6;
      iVar8 = FUN_009b41a8(plVar14);
      puVar5 = local_88;
      if ((int)uVar10 == iVar8) goto joined_r0x009ad0a0;
      puVar5 = local_90;
      puVar6 = local_88;
      local_88 = puVar7;
      local_90 = __src;
    }
    local_88 = puVar6;
    iVar8 = FUN_009b5cf8(plVar14);
    puVar5 = local_88;
    if (iVar8 != 0) {
      uVar10 = FUN_009b41a8(plVar14);
      lVar16 = FUN_009b5ce8(plVar14);
      uVar10 = uVar10 & 0xffffffff | lVar16 << 0x20;
      if (puVar7 < local_80) {
        *puVar7 = uVar10;
        puVar5 = puVar7 + 1;
      }
      else {
        lVar16 = (long)puVar7 - (long)__src >> 3;
        uVar13 = lVar16 + 1;
        if (uVar13 >> 0x3d != 0) {
                    /* try { // try from 009ad43c to 00aad443 has its CatchHandler @ 009ad5c8 */
          if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* try { // try from 009ad444 to 00aad47f has its CatchHandler @ 009ad5f0 */
            FUN_006b8c9c(&local_90);
LAB_009ad44c:
            if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00440f00();
            }
          }
          goto LAB_009ad4f4;
        }
                    /* catch() { ... } // from try @ 009ad11c with catch @ 009ad0e4 */
        uVar17 = (long)local_80 - (long)__src >> 2;
        if (uVar17 <= uVar13) {
          uVar17 = uVar13;
        }
        if (0x7ffffffffffffff7 < (ulong)((long)local_80 - (long)__src)) {
          uVar17 = 0x1fffffffffffffff;
        }
        if (uVar17 == 0) {
          puVar11 = (ulong *)0x0;
        }
        else {
          if (uVar17 >> 0x3d != 0) goto LAB_009ad44c;
                    /* try { // try from 009ad114 to 00aad11b has its CatchHandler @ 009ad168 */
          puVar11 = (ulong *)_Znwm(uVar17 << 3);
                    /* try { // try from 009ad11c to 00aad1b7 has its CatchHandler @ 009ad0e4 */
        }
        puVar5 = puVar11 + lVar16;
        *puVar5 = uVar10;
        memcpy(puVar11,__src,(long)puVar7 - (long)__src);
        local_90 = puVar11;
        puVar5 = puVar5 + 1;
        local_80 = puVar11 + uVar17;
        if (__src != (ulong *)0x0) {
          _ZdlPv(__src);
        }
      }
    }
joined_r0x009ad0a0:
    local_88 = puVar5;
    if ((plVar18 != (long *)0x0) &&
       (lVar16 = FUN_00c53da0(0xffffffffffffffff,plVar18 + 1), lVar16 == 0)) {
      (**(code **)(*plVar18 + 0x10))(plVar18);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
    }
    puVar11 = local_90;
  }
                    /* catch() { ... } // from try @ 009ad114 with catch @ 009ad168 */
  lVar16 = 0;
  if (local_88 != puVar11) {
    lVar16 = LZCOUNT((long)local_88 - (long)puVar11 >> 3) * -2 + 0x7e;
  }
  FUN_009b0dac(local_88,local_88,puVar11,puVar11,lVar16,1);
  plVar14 = (long *)*param_1;
  plVar18 = (long *)param_1[1];
  local_78 = &local_a8;
  local_a8 = (long *)0x0;
  local_a0 = (long *)0x0;
  local_98 = 0;
  lVar16 = (long)plVar18 - (long)plVar14;
  local_70 = (long *)((ulong)local_70 & 0xffffffffffffff00);
  if (lVar16 != 0) {
    if (lVar16 < 0) {
      if (*(long *)(lVar4 + 0x28) == local_68) {
        uVar15 = FUN_009b0d98(&local_a8);
        FUN_009b1e30(&local_78);
        if (local_90 != (ulong *)0x0) {
          local_88 = local_90;
          _ZdlPv(local_90);
        }
                    /* try { // try from 009ad4e0 to 00aad6e3 has its CatchHandler @ 009ad368 */
        if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_00c53ffc(uVar15);
        }
      }
      goto LAB_009ad4f4;
    }
    plVar12 = (long *)_Znwm(lVar16);
    local_98 = (long)plVar12 + lVar16;
    local_a8 = plVar12;
    local_a0 = plVar12;
    do {
      *plVar12 = *plVar14;
      lVar16 = plVar14[1];
      plVar12[1] = lVar16;
      if (lVar16 != 0) {
        FUN_00c53d70(1,lVar16 + 8);
      }
      plVar14 = plVar14 + 2;
      plVar12 = plVar12 + 2;
    } while (plVar14 != plVar18);
    plVar14 = (long *)*param_1;
    local_a0 = plVar12;
    for (plVar18 = (long *)param_1[1]; plVar18 != plVar14; plVar18 = plVar18 + -2) {
      plVar12 = (long *)plVar18[-1];
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c53da0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
                    /* catch() { ... } // from try @ 009ad264 with catch @ 009ad220 */
      puVar11 = local_90;
    }
  }
  puVar5 = local_88;
                    /* try { // try from 009ad264 to 00aad2ff has its CatchHandler @ 009ad220 */
  param_1[1] = plVar14;
  plVar14 = local_a8;
  plVar18 = local_a0;
  for (; local_a8 = plVar14, local_a0 = plVar18, puVar11 != puVar5; puVar11 = puVar11 + 1) {
    if (plVar14 != plVar18) {
      uVar10 = *puVar11;
      do {
        pplVar2 = (long **)*plVar14;
        local_70 = (long *)plVar14[1];
        local_78 = pplVar2;
        if (local_70 != (long *)0x0) {
          FUN_00c53d70(1,local_70 + 1);
        }
        iVar8 = FUN_009b41a8(pplVar2);
        if ((int)uVar10 == iVar8) {
          uVar9 = FUN_009b5ce8(local_78);
          uVar13 = FUN_0080666c(4,uVar9);
          if ((uVar13 & 1) != 0) {
            plVar14 = (long *)param_1[1];
            if (plVar14 < (long *)param_1[2]) {
              *plVar14 = (long)local_78;
              plVar14[1] = (long)local_70;
              if (local_70 != (long *)0x0) {
                FUN_00c53d70(1,local_70 + 1);
              }
              plVar14 = plVar14 + 2;
            }
            else {
                    /* try { // try from 009ad368 to 00aad3ef has its CatchHandler @ 009ad368
                       catch() { ... } // from try @ 009ad368 with catch @ 009ad368
                       catch() { ... } // from try @ 009ad4e0 with catch @ 009ad368 */
              plVar14 = (long *)FUN_009b0c3c(param_1,&local_78);
            }
            plVar18 = local_70;
            param_1[1] = plVar14;
            if ((local_70 != (long *)0x0) &&
               (lVar16 = FUN_00c53da0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
              (**(code **)(*plVar18 + 0x10))(plVar18);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
            }
            break;
          }
        }
        plVar12 = local_70;
        if ((local_70 != (long *)0x0) &&
           (lVar16 = FUN_00c53da0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
          (**(code **)(*plVar12 + 0x10))(plVar12);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
        }
        plVar14 = plVar14 + 2;
                    /* catch() { ... } // from try @ 009ad25c with catch @ 009ad2b0 */
      } while (plVar14 != plVar18);
    }
    plVar14 = local_a8;
    plVar18 = local_a0;
  }
  if (plVar14 != (long *)0x0) {
    for (; plVar18 != plVar14; plVar18 = plVar18 + -2) {
      plVar12 = (long *)plVar18[-1];
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c53da0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
    }
    local_a0 = plVar14;
    _ZdlPv(local_a8);
  }
                    /* try { // try from 009ad3f0 to 00aad3fb has its CatchHandler @ 009ad5e0 */
  if (local_90 != (ulong *)0x0) {
    _ZdlPv(local_90);
  }
  if (*(long *)(lVar4 + 0x28) == local_68) {
    return;
  }
LAB_009ad4f4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009acfbc"></a> `009acfbc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-009acfc0"></a> `009acfc0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009acfc4"></a> `009acfc4` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009acfc8"></a> `009acfc8` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009acfcc"></a> `009acfcc` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009acfd0"></a> `009acfd0` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009acfd4"></a> `009acfd4` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009acfd8"></a> `009acfd8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-009acfdc"></a> `009acfdc` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009acfe0"></a> `009acfe0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009acfe4"></a> `009acfe4` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-009acfe8"></a> `009acfe8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009acfec"></a> `009acfec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009acff0"></a> `009acff0` | `19 68 40 a9` | ldp x25,x26,[x0] | `FALL_THROUGH`
<a id="insn-009acff4"></a> `009acff4` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009acff8"></a> `009acff8` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009acffc"></a> `009acffc` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009ad000"></a> `009ad000` | `e1 00 00 54` | b.ne 0x009ad01c | `CONDITIONAL_JUMP`
<a id="insn-009ad004"></a> `009ad004` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-009ad008"></a> `009ad008` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-009ad00c"></a> `009ad00c` | `56 00 00 14` | b 0x009ad164 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad010"></a> `009ad010` | `39 43 00 91` | add x25,x25,#0x10 | `FALL_THROUGH`
<a id="insn-009ad014"></a> `009ad014` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009ad018"></a> `009ad018` | `40 0a 00 54` | b.eq 0x009ad160 | `CONDITIONAL_JUMP`
<a id="insn-009ad01c"></a> `009ad01c` | `36 53 40 a9` | ldp x22,x20,[x25] | `FALL_THROUGH`
<a id="insn-009ad020"></a> `009ad020` | `f6 d3 00 a9` | stp x22,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad024"></a> `009ad024` | `94 00 00 b4` | cbz x20,0x009ad034 | `CONDITIONAL_JUMP`
<a id="insn-009ad028"></a> `009ad028` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009ad02c"></a> `009ad02c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ad030"></a> `009ad030` | `50 9b 0a 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-009ad034"></a> `009ad034` | `f5 63 42 a9` | ldp x21,x24,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad038"></a> `009ad038` | `bf 02 18 eb` | cmp x21,x24 | `FALL_THROUGH`
<a id="insn-009ad03c"></a> `009ad03c` | `f7 03 15 aa` | mov x23,x21 | `FALL_THROUGH`
<a id="insn-009ad040"></a> `009ad040` | `20 01 00 54` | b.eq 0x009ad064 | `CONDITIONAL_JUMP`
<a id="insn-009ad044"></a> `009ad044` | `fb 02 40 b9` | ldr w27,[x23] | `FALL_THROUGH`
<a id="insn-009ad048"></a> `009ad048` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ad04c"></a> `009ad04c` | `57 1c 00 94` | bl 0x009b41a8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad050"></a> `009ad050` | `7f 03 00 6b` | cmp w27,w0 | `FALL_THROUGH`
<a id="insn-009ad054"></a> `009ad054` | `60 02 00 54` | b.eq 0x009ad0a0 | `CONDITIONAL_JUMP`
<a id="insn-009ad058"></a> `009ad058` | `f7 22 00 91` | add x23,x23,#0x8 | `FALL_THROUGH`
<a id="insn-009ad05c"></a> `009ad05c` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009ad060"></a> `009ad060` | `21 ff ff 54` | b.ne 0x009ad044 | `CONDITIONAL_JUMP`
<a id="insn-009ad064"></a> `009ad064` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ad068"></a> `009ad068` | `24 23 00 94` | bl 0x009b5cf8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad06c"></a> `009ad06c` | `a0 01 00 34` | cbz w0,0x009ad0a0 | `CONDITIONAL_JUMP`
<a id="insn-009ad070"></a> `009ad070` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ad074"></a> `009ad074` | `4d 1c 00 94` | bl 0x009b41a8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad078"></a> `009ad078` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009ad07c"></a> `009ad07c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ad080"></a> `009ad080` | `1a 23 00 94` | bl 0x009b5ce8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad084"></a> `009ad084` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ad088"></a> `009ad088` | `e9 03 17 2a` | mov w9,w23 | `FALL_THROUGH`
<a id="insn-009ad08c"></a> `009ad08c` | `3b 81 00 aa` | orr x27,x9,x0, LSL #0x20 | `FALL_THROUGH`
<a id="insn-009ad090"></a> `009ad090` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-009ad094"></a> `009ad094` | `e2 01 00 54` | b.cs 0x009ad0d0 | `CONDITIONAL_JUMP`
<a id="insn-009ad098"></a> `009ad098` | `1b 87 00 f8` | str x27,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-009ad09c"></a> `009ad09c` | `f8 17 00 f9` | str x24,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009ad0a0"></a> `009ad0a0` | `94 fb ff b4` | cbz x20,0x009ad010 | `CONDITIONAL_JUMP`
<a id="insn-009ad0a4"></a> `009ad0a4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009ad0a8"></a> `009ad0a8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad0ac"></a> `009ad0ac` | `3d 9b 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad0b0"></a> `009ad0b0` | `00 fb ff b5` | cbnz x0,0x009ad010 | `CONDITIONAL_JUMP`
<a id="insn-009ad0b4"></a> `009ad0b4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009ad0b8"></a> `009ad0b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad0bc"></a> `009ad0bc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad0c0"></a> `009ad0c0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad0c4"></a> `009ad0c4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad0c8"></a> `009ad0c8` | `a2 ab 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009ad0cc"></a> `009ad0cc` | `d1 ff ff 17` | b 0x009ad010 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad0d0"></a> `009ad0d0` | `16 03 15 cb` | sub x22,x24,x21 | `FALL_THROUGH`
<a id="insn-009ad0d4"></a> `009ad0d4` | `d8 fe 43 93` | asr x24,x22,#0x3 | `FALL_THROUGH`
<a id="insn-009ad0d8"></a> `009ad0d8` | `09 07 00 91` | add x9,x24,#0x1 | `FALL_THROUGH`
<a id="insn-009ad0dc"></a> `009ad0dc` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-009ad0e0"></a> `009ad0e0` | `8a 1a 00 b5` | cbnz x10,0x009ad430 | `CONDITIONAL_JUMP`
<a id="insn-009ad0e4"></a> `009ad0e4` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-009ad0e8"></a> `009ad0e8` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-009ad0ec"></a> `009ad0ec` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-009ad0f0"></a> `009ad0f0` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-009ad0f4"></a> `009ad0f4` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-009ad0f8"></a> `009ad0f8` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-009ad0fc"></a> `009ad0fc` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-009ad100"></a> `009ad100` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-009ad104"></a> `009ad104` | `fc 00 00 b4` | cbz x28,0x009ad120 | `CONDITIONAL_JUMP`
<a id="insn-009ad108"></a> `009ad108` | `88 ff 7d d3` | lsr x8,x28,#0x3d | `FALL_THROUGH`
<a id="insn-009ad10c"></a> `009ad10c` | `08 1a 00 b5` | cbnz x8,0x009ad44c | `CONDITIONAL_JUMP`
<a id="insn-009ad110"></a> `009ad110` | `80 f3 7d d3` | lsl x0,x28,#0x3 | `FALL_THROUGH`
<a id="insn-009ad114"></a> `009ad114` | `93 ab 0a 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-009ad118"></a> `009ad118` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-009ad11c"></a> `009ad11c` | `02 00 00 14` | b 0x009ad124 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad120"></a> `009ad120` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-009ad124"></a> `009ad124` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-009ad128"></a> `009ad128` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-009ad12c"></a> `009ad12c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009ad130"></a> `009ad130` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-009ad134"></a> `009ad134` | `fc 0e 1c 8b` | add x28,x23,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-009ad138"></a> `009ad138` | `1b 87 00 f8` | str x27,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-009ad13c"></a> `009ad13c` | `e5 ab 0a 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad140"></a> `009ad140` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad144"></a> `009ad144` | `fc 1b 00 f9` | str x28,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ad148"></a> `009ad148` | `75 00 00 b4` | cbz x21,0x009ad154 | `CONDITIONAL_JUMP`
<a id="insn-009ad14c"></a> `009ad14c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad150"></a> `009ad150` | `8c ab 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad154"></a> `009ad154` | `f8 17 00 f9` | str x24,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009ad158"></a> `009ad158` | `74 fa ff b5` | cbnz x20,0x009ad0a4 | `CONDITIONAL_JUMP`
<a id="insn-009ad15c"></a> `009ad15c` | `ad ff ff 17` | b 0x009ad010 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad160"></a> `009ad160` | `f4 03 42 a9` | ldp x20,x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad164"></a> `009ad164` | `08 00 14 eb` | subs x8,x0,x20 | `FALL_THROUGH`
<a id="insn-009ad168"></a> `009ad168` | `c9 0f 80 52` | mov w9,#0x7e | `FALL_THROUGH`
<a id="insn-009ad16c"></a> `009ad16c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-009ad170"></a> `009ad170` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-009ad174"></a> `009ad174` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-009ad178"></a> `009ad178` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-009ad17c"></a> `009ad17c` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-009ad180"></a> `009ad180` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-009ad184"></a> `009ad184` | `08 11 c0 da` | clz x8,x8 | `FALL_THROUGH`
<a id="insn-009ad188"></a> `009ad188` | `28 05 08 cb` | sub x8,x9,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-009ad18c"></a> `009ad18c` | `e4 03 88 9a` | csel x4,xzr,x8,eq | `FALL_THROUGH`
<a id="insn-009ad190"></a> `009ad190` | `07 0f 00 94` | bl 0x009b0dac | `UNCONDITIONAL_CALL`
<a id="insn-009ad194"></a> `009ad194` | `77 62 40 a9` | ldp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-009ad198"></a> `009ad198` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009ad19c"></a> `009ad19c` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad1a0"></a> `009ad1a0` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009ad1a4"></a> `009ad1a4` | `16 03 17 eb` | subs x22,x24,x23 | `FALL_THROUGH`
<a id="insn-009ad1a8"></a> `009ad1a8` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009ad1ac"></a> `009ad1ac` | `bf 03 1f 38` | sturb wzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009ad1b0"></a> `009ad1b0` | `80 05 00 54` | b.eq 0x009ad260 | `CONDITIONAL_JUMP`
<a id="insn-009ad1b4"></a> `009ad1b4` | `96 15 f8 b7` | tbnz x22,#0x3f,0x009ad464 | `CONDITIONAL_JUMP`
<a id="insn-009ad1b8"></a> `009ad1b8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ad1bc"></a> `009ad1bc` | `69 ab 0a 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-009ad1c0"></a> `009ad1c0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009ad1c4"></a> `009ad1c4` | `08 00 16 8b` | add x8,x0,x22 | `FALL_THROUGH`
<a id="insn-009ad1c8"></a> `009ad1c8` | `e0 83 00 a9` | stp x0,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad1cc"></a> `009ad1cc` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009ad1d0"></a> `009ad1d0` | `05 00 00 14` | b 0x009ad1e4 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad1d4"></a> `009ad1d4` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009ad1d8"></a> `009ad1d8` | `b5 42 00 91` | add x21,x21,#0x10 | `FALL_THROUGH`
<a id="insn-009ad1dc"></a> `009ad1dc` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009ad1e0"></a> `009ad1e0` | `40 01 00 54` | b.eq 0x009ad208 | `CONDITIONAL_JUMP`
<a id="insn-009ad1e4"></a> `009ad1e4` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-009ad1e8"></a> `009ad1e8` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-009ad1ec"></a> `009ad1ec` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-009ad1f0"></a> `009ad1f0` | `a8 06 00 f9` | str x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-009ad1f4"></a> `009ad1f4` | `08 ff ff b4` | cbz x8,0x009ad1d4 | `CONDITIONAL_JUMP`
<a id="insn-009ad1f8"></a> `009ad1f8` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-009ad1fc"></a> `009ad1fc` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ad200"></a> `009ad200` | `dc 9a 0a 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-009ad204"></a> `009ad204` | `f4 ff ff 17` | b 0x009ad1d4 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad208"></a> `009ad208` | `77 5a 40 a9` | ldp x23,x22,[x19] | `FALL_THROUGH`
<a id="insn-009ad20c"></a> `009ad20c` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ad210"></a> `009ad210` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-009ad214"></a> `009ad214` | `a1 00 00 54` | b.ne 0x009ad228 | `CONDITIONAL_JUMP`
<a id="insn-009ad218"></a> `009ad218` | `12 00 00 14` | b 0x009ad260 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad21c"></a> `009ad21c` | `d6 42 00 d1` | sub x22,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009ad220"></a> `009ad220` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-009ad224"></a> `009ad224` | `c0 01 00 54` | b.eq 0x009ad25c | `CONDITIONAL_JUMP`
<a id="insn-009ad228"></a> `009ad228` | `d4 82 5f f8` | ldur x20,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad22c"></a> `009ad22c` | `94 ff ff b4` | cbz x20,0x009ad21c | `CONDITIONAL_JUMP`
<a id="insn-009ad230"></a> `009ad230` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009ad234"></a> `009ad234` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad238"></a> `009ad238` | `da 9a 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad23c"></a> `009ad23c` | `00 ff ff b5` | cbnz x0,0x009ad21c | `CONDITIONAL_JUMP`
<a id="insn-009ad240"></a> `009ad240` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009ad244"></a> `009ad244` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad248"></a> `009ad248` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad24c"></a> `009ad24c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad250"></a> `009ad250` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad254"></a> `009ad254` | `3f ab 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009ad258"></a> `009ad258` | `f1 ff ff 17` | b 0x009ad21c | `UNCONDITIONAL_JUMP`
<a id="insn-009ad25c"></a> `009ad25c` | `f4 13 40 f9` | ldr x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad260"></a> `009ad260` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009ad264"></a> `009ad264` | `77 06 00 f9` | str x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-009ad268"></a> `009ad268` | `9f 02 16 eb` | cmp x20,x22 | `FALL_THROUGH`
<a id="insn-009ad26c"></a> `009ad26c` | `61 01 00 54` | b.ne 0x009ad298 | `CONDITIONAL_JUMP`
<a id="insn-009ad270"></a> `009ad270` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad274"></a> `009ad274` | `f4 0b 00 b4` | cbz x20,0x009ad3f0 | `CONDITIONAL_JUMP`
<a id="insn-009ad278"></a> `009ad278` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ad27c"></a> `009ad27c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad280"></a> `009ad280` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-009ad284"></a> `009ad284` | `61 09 00 54` | b.ne 0x009ad3b0 | `CONDITIONAL_JUMP`
<a id="insn-009ad288"></a> `009ad288` | `58 00 00 14` | b 0x009ad3e8 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad28c"></a> `009ad28c` | `94 22 00 91` | add x20,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009ad290"></a> `009ad290` | `9f 02 16 eb` | cmp x20,x22 | `FALL_THROUGH`
<a id="insn-009ad294"></a> `009ad294` | `e0 fe ff 54` | b.eq 0x009ad270 | `CONDITIONAL_JUMP`
<a id="insn-009ad298"></a> `009ad298` | `f7 e3 40 a9` | ldp x23,x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad29c"></a> `009ad29c` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009ad2a0"></a> `009ad2a0` | `60 ff ff 54` | b.eq 0x009ad28c | `CONDITIONAL_JUMP`
<a id="insn-009ad2a4"></a> `009ad2a4` | `99 02 40 b9` | ldr w25,[x20] | `FALL_THROUGH`
<a id="insn-009ad2a8"></a> `009ad2a8` | `04 00 00 14` | b 0x009ad2b8 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad2ac"></a> `009ad2ac` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009ad2b0"></a> `009ad2b0` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009ad2b4"></a> `009ad2b4` | `c0 fe ff 54` | b.eq 0x009ad28c | `CONDITIONAL_JUMP`
<a id="insn-009ad2b8"></a> `009ad2b8` | `f5 22 40 a9` | ldp x21,x8,[x23] | `FALL_THROUGH`
<a id="insn-009ad2bc"></a> `009ad2bc` | `b5 a3 3e a9` | stp x21,x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009ad2c0"></a> `009ad2c0` | `88 00 00 b4` | cbz x8,0x009ad2d0 | `CONDITIONAL_JUMP`
<a id="insn-009ad2c4"></a> `009ad2c4` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-009ad2c8"></a> `009ad2c8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ad2cc"></a> `009ad2cc` | `a9 9a 0a 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-009ad2d0"></a> `009ad2d0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad2d4"></a> `009ad2d4` | `b5 1b 00 94` | bl 0x009b41a8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad2d8"></a> `009ad2d8` | `3f 03 00 6b` | cmp w25,w0 | `FALL_THROUGH`
<a id="insn-009ad2dc"></a> `009ad2dc` | `e1 00 00 54` | b.ne 0x009ad2f8 | `CONDITIONAL_JUMP`
<a id="insn-009ad2e0"></a> `009ad2e0` | `a0 83 5e f8` | ldur x0,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009ad2e4"></a> `009ad2e4` | `81 22 00 94` | bl 0x009b5ce8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad2e8"></a> `009ad2e8` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-009ad2ec"></a> `009ad2ec` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-009ad2f0"></a> `009ad2f0` | `df 64 f9 97` | bl 0x0080666c | `UNCONDITIONAL_CALL`
<a id="insn-009ad2f4"></a> `009ad2f4` | `c0 01 00 37` | tbnz w0,#0x0,0x009ad32c | `CONDITIONAL_JUMP`
<a id="insn-009ad2f8"></a> `009ad2f8` | `b5 03 5f f8` | ldur x21,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009ad2fc"></a> `009ad2fc` | `95 fd ff b4` | cbz x21,0x009ad2ac | `CONDITIONAL_JUMP`
<a id="insn-009ad300"></a> `009ad300` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009ad304"></a> `009ad304` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad308"></a> `009ad308` | `a6 9a 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad30c"></a> `009ad30c` | `00 fd ff b5` | cbnz x0,0x009ad2ac | `CONDITIONAL_JUMP`
<a id="insn-009ad310"></a> `009ad310` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009ad314"></a> `009ad314` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad318"></a> `009ad318` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad31c"></a> `009ad31c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad320"></a> `009ad320` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad324"></a> `009ad324` | `0b ab 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009ad328"></a> `009ad328` | `e1 ff ff 17` | b 0x009ad2ac | `UNCONDITIONAL_JUMP`
<a id="insn-009ad32c"></a> `009ad32c` | `75 a2 40 a9` | ldp x21,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-009ad330"></a> `009ad330` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-009ad334"></a> `009ad334` | `62 01 00 54` | b.cs 0x009ad360 | `CONDITIONAL_JUMP`
<a id="insn-009ad338"></a> `009ad338` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009ad33c"></a> `009ad33c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-009ad340"></a> `009ad340` | `a8 03 5f f8` | ldur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009ad344"></a> `009ad344` | `a8 06 00 f9` | str x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-009ad348"></a> `009ad348` | `88 00 00 b4` | cbz x8,0x009ad358 | `CONDITIONAL_JUMP`
<a id="insn-009ad34c"></a> `009ad34c` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-009ad350"></a> `009ad350` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ad354"></a> `009ad354` | `87 9a 0a 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-009ad358"></a> `009ad358` | `a0 42 00 91` | add x0,x21,#0x10 | `FALL_THROUGH`
<a id="insn-009ad35c"></a> `009ad35c` | `04 00 00 14` | b 0x009ad36c | `UNCONDITIONAL_JUMP`
<a id="insn-009ad360"></a> `009ad360` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-009ad364"></a> `009ad364` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad368"></a> `009ad368` | `35 0e 00 94` | bl 0x009b0c3c | `UNCONDITIONAL_CALL`
<a id="insn-009ad36c"></a> `009ad36c` | `b5 03 5f f8` | ldur x21,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009ad370"></a> `009ad370` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-009ad374"></a> `009ad374` | `d5 f8 ff b4` | cbz x21,0x009ad28c | `CONDITIONAL_JUMP`
<a id="insn-009ad378"></a> `009ad378` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009ad37c"></a> `009ad37c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad380"></a> `009ad380` | `88 9a 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad384"></a> `009ad384` | `40 f8 ff b5` | cbnz x0,0x009ad28c | `CONDITIONAL_JUMP`
<a id="insn-009ad388"></a> `009ad388` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009ad38c"></a> `009ad38c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad390"></a> `009ad390` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad394"></a> `009ad394` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad398"></a> `009ad398` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad39c"></a> `009ad39c` | `ed aa 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009ad3a0"></a> `009ad3a0` | `bb ff ff 17` | b 0x009ad28c | `UNCONDITIONAL_JUMP`
<a id="insn-009ad3a4"></a> `009ad3a4` | `b5 42 00 d1` | sub x21,x21,#0x10 | `FALL_THROUGH`
<a id="insn-009ad3a8"></a> `009ad3a8` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-009ad3ac"></a> `009ad3ac` | `c0 01 00 54` | b.eq 0x009ad3e4 | `CONDITIONAL_JUMP`
<a id="insn-009ad3b0"></a> `009ad3b0` | `b3 82 5f f8` | ldur x19,[x21, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad3b4"></a> `009ad3b4` | `93 ff ff b4` | cbz x19,0x009ad3a4 | `CONDITIONAL_JUMP`
<a id="insn-009ad3b8"></a> `009ad3b8` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-009ad3bc"></a> `009ad3bc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad3c0"></a> `009ad3c0` | `78 9a 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad3c4"></a> `009ad3c4` | `00 ff ff b5` | cbnz x0,0x009ad3a4 | `CONDITIONAL_JUMP`
<a id="insn-009ad3c8"></a> `009ad3c8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-009ad3cc"></a> `009ad3cc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad3d0"></a> `009ad3d0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad3d4"></a> `009ad3d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad3d8"></a> `009ad3d8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad3dc"></a> `009ad3dc` | `dd aa 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009ad3e0"></a> `009ad3e0` | `f1 ff ff 17` | b 0x009ad3a4 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad3e4"></a> `009ad3e4` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad3e8"></a> `009ad3e8` | `f4 0b 00 f9` | str x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ad3ec"></a> `009ad3ec` | `e5 aa 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad3f0"></a> `009ad3f0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad3f4"></a> `009ad3f4` | `40 00 00 b4` | cbz x0,0x009ad3fc | `CONDITIONAL_JUMP`
<a id="insn-009ad3f8"></a> `009ad3f8` | `e2 aa 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad3fc"></a> `009ad3fc` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad400"></a> `009ad400` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad404"></a> `009ad404` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad408"></a> `009ad408` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad40c"></a> `009ad40c` | `41 07 00 54` | b.ne 0x009ad4f4 | `CONDITIONAL_JUMP`
<a id="insn-009ad410"></a> `009ad410` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009ad414"></a> `009ad414` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009ad418"></a> `009ad418` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009ad41c"></a> `009ad41c` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009ad420"></a> `009ad420` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009ad424"></a> `009ad424` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009ad428"></a> `009ad428` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-009ad42c"></a> `009ad42c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009ad430"></a> `009ad430` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad434"></a> `009ad434` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad438"></a> `009ad438` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad43c"></a> `009ad43c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad440"></a> `009ad440` | `a1 05 00 54` | b.ne 0x009ad4f4 | `CONDITIONAL_JUMP`
<a id="insn-009ad444"></a> `009ad444` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009ad448"></a> `009ad448` | `15 2e f4 97` | bl 0x006b8c9c | `UNCONDITIONAL_CALL`
<a id="insn-009ad44c"></a> `009ad44c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad450"></a> `009ad450` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad454"></a> `009ad454` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad458"></a> `009ad458` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad45c"></a> `009ad45c` | `c1 04 00 54` | b.ne 0x009ad4f4 | `CONDITIONAL_JUMP`
<a id="insn-009ad460"></a> `009ad460` | `a8 4e ea 97` | bl 0x00440f00 | `CALL_TERMINATOR`
<a id="insn-009ad464"></a> `009ad464` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad468"></a> `009ad468` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad46c"></a> `009ad46c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad470"></a> `009ad470` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad474"></a> `009ad474` | `01 04 00 54` | b.ne 0x009ad4f4 | `CONDITIONAL_JUMP`
<a id="insn-009ad478"></a> `009ad478` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009ad47c"></a> `009ad47c` | `47 0e 00 94` | bl 0x009b0d98 | `UNCONDITIONAL_CALL`
<a id="insn-009ad480"></a> `009ad480` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009ad484"></a> `009ad484` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-009ad488"></a> `009ad488` | `6a 12 00 94` | bl 0x009b1e30 | `UNCONDITIONAL_CALL`
<a id="insn-009ad48c"></a> `009ad48c` | `0f 00 00 14` | b 0x009ad4c8 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad4c8"></a> `009ad4c8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad4cc"></a> `009ad4cc` | `60 00 00 b4` | cbz x0,0x009ad4d8 | `CONDITIONAL_JUMP`
<a id="insn-009ad4d0"></a> `009ad4d0` | `e0 17 00 f9` | str x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009ad4d4"></a> `009ad4d4` | `ab aa 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad4d8"></a> `009ad4d8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad4dc"></a> `009ad4dc` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad4e0"></a> `009ad4e0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad4e4"></a> `009ad4e4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad4e8"></a> `009ad4e8` | `61 00 00 54` | b.ne 0x009ad4f4 | `CONDITIONAL_JUMP`
<a id="insn-009ad4ec"></a> `009ad4ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad4f0"></a> `009ad4f0` | `c3 9a 0a 94` | bl 0x00c53ffc | `CALL_TERMINATOR`
<a id="insn-009ad4f4"></a> `009ad4f4` | `af aa 0a 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009acfbc`](#insn-009acfbc) 範囲 `[['009acfbc', '009ad003']]`
  - `CONDITIONAL_JUMP` [`009ad000`](#insn-009ad000) → [`009ad01c`](#insn-009ad01c)
  - `FALL_THROUGH` [`009ad000`](#insn-009ad000) → [`009ad004`](#insn-009ad004)
- ブロック [`009ad004`](#insn-009ad004) 範囲 `[['009ad004', '009ad00f']]`
  - `UNCONDITIONAL_JUMP` [`009ad00c`](#insn-009ad00c) → [`009ad164`](#insn-009ad164)
- ブロック [`009ad010`](#insn-009ad010) 範囲 `[['009ad010', '009ad01b']]`
  - `CONDITIONAL_JUMP` [`009ad018`](#insn-009ad018) → [`009ad160`](#insn-009ad160)
  - `FALL_THROUGH` [`009ad018`](#insn-009ad018) → [`009ad01c`](#insn-009ad01c)
- ブロック [`009ad01c`](#insn-009ad01c) 範囲 `[['009ad01c', '009ad027']]`
  - `CONDITIONAL_JUMP` [`009ad024`](#insn-009ad024) → [`009ad034`](#insn-009ad034)
  - `FALL_THROUGH` [`009ad024`](#insn-009ad024) → [`009ad028`](#insn-009ad028)
- ブロック [`009ad028`](#insn-009ad028) 範囲 `[['009ad028', '009ad033']]`
  - `FALL_THROUGH` [`009ad030`](#insn-009ad030) → [`009ad034`](#insn-009ad034)
- ブロック [`009ad034`](#insn-009ad034) 範囲 `[['009ad034', '009ad043']]`
  - `CONDITIONAL_JUMP` [`009ad040`](#insn-009ad040) → [`009ad064`](#insn-009ad064)
  - `FALL_THROUGH` [`009ad040`](#insn-009ad040) → [`009ad044`](#insn-009ad044)
- ブロック [`009ad044`](#insn-009ad044) 範囲 `[['009ad044', '009ad057']]`
  - `CONDITIONAL_JUMP` [`009ad054`](#insn-009ad054) → [`009ad0a0`](#insn-009ad0a0)
  - `FALL_THROUGH` [`009ad054`](#insn-009ad054) → [`009ad058`](#insn-009ad058)
- ブロック [`009ad058`](#insn-009ad058) 範囲 `[['009ad058', '009ad063']]`
  - `CONDITIONAL_JUMP` [`009ad060`](#insn-009ad060) → [`009ad044`](#insn-009ad044)
  - `FALL_THROUGH` [`009ad060`](#insn-009ad060) → [`009ad064`](#insn-009ad064)
- ブロック [`009ad064`](#insn-009ad064) 範囲 `[['009ad064', '009ad06f']]`
  - `CONDITIONAL_JUMP` [`009ad06c`](#insn-009ad06c) → [`009ad0a0`](#insn-009ad0a0)
  - `FALL_THROUGH` [`009ad06c`](#insn-009ad06c) → [`009ad070`](#insn-009ad070)
- ブロック [`009ad070`](#insn-009ad070) 範囲 `[['009ad070', '009ad097']]`
  - `CONDITIONAL_JUMP` [`009ad094`](#insn-009ad094) → [`009ad0d0`](#insn-009ad0d0)
  - `FALL_THROUGH` [`009ad094`](#insn-009ad094) → [`009ad098`](#insn-009ad098)
- ブロック [`009ad098`](#insn-009ad098) 範囲 `[['009ad098', '009ad09f']]`
  - `FALL_THROUGH` [`009ad09c`](#insn-009ad09c) → [`009ad0a0`](#insn-009ad0a0)
- ブロック [`009ad0a0`](#insn-009ad0a0) 範囲 `[['009ad0a0', '009ad0a3']]`
  - `CONDITIONAL_JUMP` [`009ad0a0`](#insn-009ad0a0) → [`009ad010`](#insn-009ad010)
  - `FALL_THROUGH` [`009ad0a0`](#insn-009ad0a0) → [`009ad0a4`](#insn-009ad0a4)
- ブロック [`009ad0a4`](#insn-009ad0a4) 範囲 `[['009ad0a4', '009ad0b3']]`
  - `CONDITIONAL_JUMP` [`009ad0b0`](#insn-009ad0b0) → [`009ad010`](#insn-009ad010)
  - `FALL_THROUGH` [`009ad0b0`](#insn-009ad0b0) → [`009ad0b4`](#insn-009ad0b4)
- ブロック [`009ad0b4`](#insn-009ad0b4) 範囲 `[['009ad0b4', '009ad0cf']]`
  - `UNCONDITIONAL_JUMP` [`009ad0cc`](#insn-009ad0cc) → [`009ad010`](#insn-009ad010)
- ブロック [`009ad0d0`](#insn-009ad0d0) 範囲 `[['009ad0d0', '009ad0e3']]`
  - `CONDITIONAL_JUMP` [`009ad0e0`](#insn-009ad0e0) → [`009ad430`](#insn-009ad430)
  - `FALL_THROUGH` [`009ad0e0`](#insn-009ad0e0) → [`009ad0e4`](#insn-009ad0e4)
- ブロック [`009ad0e4`](#insn-009ad0e4) 範囲 `[['009ad0e4', '009ad107']]`
  - `CONDITIONAL_JUMP` [`009ad104`](#insn-009ad104) → [`009ad120`](#insn-009ad120)
  - `FALL_THROUGH` [`009ad104`](#insn-009ad104) → [`009ad108`](#insn-009ad108)
- ブロック [`009ad108`](#insn-009ad108) 範囲 `[['009ad108', '009ad10f']]`
  - `CONDITIONAL_JUMP` [`009ad10c`](#insn-009ad10c) → [`009ad44c`](#insn-009ad44c)
  - `FALL_THROUGH` [`009ad10c`](#insn-009ad10c) → [`009ad110`](#insn-009ad110)
- ブロック [`009ad110`](#insn-009ad110) 範囲 `[['009ad110', '009ad113']]`
  - `FALL_THROUGH` [`009ad110`](#insn-009ad110) → [`009ad114`](#insn-009ad114)
- ブロック [`009ad114`](#insn-009ad114) 範囲 `[['009ad114', '009ad11b']]`
  - `FALL_THROUGH` [`009ad118`](#insn-009ad118) → [`009ad11c`](#insn-009ad11c)
- ブロック [`009ad11c`](#insn-009ad11c) 範囲 `[['009ad11c', '009ad11f']]`
  - `UNCONDITIONAL_JUMP` [`009ad11c`](#insn-009ad11c) → [`009ad124`](#insn-009ad124)
- ブロック [`009ad120`](#insn-009ad120) 範囲 `[['009ad120', '009ad123']]`
  - `FALL_THROUGH` [`009ad120`](#insn-009ad120) → [`009ad124`](#insn-009ad124)
- ブロック [`009ad124`](#insn-009ad124) 範囲 `[['009ad124', '009ad14b']]`
  - `CONDITIONAL_JUMP` [`009ad148`](#insn-009ad148) → [`009ad154`](#insn-009ad154)
  - `FALL_THROUGH` [`009ad148`](#insn-009ad148) → [`009ad14c`](#insn-009ad14c)
- ブロック [`009ad14c`](#insn-009ad14c) 範囲 `[['009ad14c', '009ad153']]`
  - `FALL_THROUGH` [`009ad150`](#insn-009ad150) → [`009ad154`](#insn-009ad154)
- ブロック [`009ad154`](#insn-009ad154) 範囲 `[['009ad154', '009ad15b']]`
  - `CONDITIONAL_JUMP` [`009ad158`](#insn-009ad158) → [`009ad0a4`](#insn-009ad0a4)
  - `FALL_THROUGH` [`009ad158`](#insn-009ad158) → [`009ad15c`](#insn-009ad15c)
- ブロック [`009ad15c`](#insn-009ad15c) 範囲 `[['009ad15c', '009ad15f']]`
  - `UNCONDITIONAL_JUMP` [`009ad15c`](#insn-009ad15c) → [`009ad010`](#insn-009ad010)
- ブロック [`009ad160`](#insn-009ad160) 範囲 `[['009ad160', '009ad163']]`
  - `FALL_THROUGH` [`009ad160`](#insn-009ad160) → [`009ad164`](#insn-009ad164)
- ブロック [`009ad164`](#insn-009ad164) 範囲 `[['009ad164', '009ad167']]`
  - `FALL_THROUGH` [`009ad164`](#insn-009ad164) → [`009ad168`](#insn-009ad168)
- ブロック [`009ad168`](#insn-009ad168) 範囲 `[['009ad168', '009ad1b3']]`
  - `CONDITIONAL_JUMP` [`009ad1b0`](#insn-009ad1b0) → [`009ad260`](#insn-009ad260)
  - `FALL_THROUGH` [`009ad1b0`](#insn-009ad1b0) → [`009ad1b4`](#insn-009ad1b4)
- ブロック [`009ad1b4`](#insn-009ad1b4) 範囲 `[['009ad1b4', '009ad1b7']]`
  - `CONDITIONAL_JUMP` [`009ad1b4`](#insn-009ad1b4) → [`009ad464`](#insn-009ad464)
  - `FALL_THROUGH` [`009ad1b4`](#insn-009ad1b4) → [`009ad1b8`](#insn-009ad1b8)
- ブロック [`009ad1b8`](#insn-009ad1b8) 範囲 `[['009ad1b8', '009ad1d3']]`
  - `UNCONDITIONAL_JUMP` [`009ad1d0`](#insn-009ad1d0) → [`009ad1e4`](#insn-009ad1e4)
- ブロック [`009ad1d4`](#insn-009ad1d4) 範囲 `[['009ad1d4', '009ad1e3']]`
  - `CONDITIONAL_JUMP` [`009ad1e0`](#insn-009ad1e0) → [`009ad208`](#insn-009ad208)
  - `FALL_THROUGH` [`009ad1e0`](#insn-009ad1e0) → [`009ad1e4`](#insn-009ad1e4)
- ブロック [`009ad1e4`](#insn-009ad1e4) 範囲 `[['009ad1e4', '009ad1f7']]`
  - `CONDITIONAL_JUMP` [`009ad1f4`](#insn-009ad1f4) → [`009ad1d4`](#insn-009ad1d4)
  - `FALL_THROUGH` [`009ad1f4`](#insn-009ad1f4) → [`009ad1f8`](#insn-009ad1f8)
- ブロック [`009ad1f8`](#insn-009ad1f8) 範囲 `[['009ad1f8', '009ad207']]`
  - `UNCONDITIONAL_JUMP` [`009ad204`](#insn-009ad204) → [`009ad1d4`](#insn-009ad1d4)
- ブロック [`009ad208`](#insn-009ad208) 範囲 `[['009ad208', '009ad217']]`
  - `CONDITIONAL_JUMP` [`009ad214`](#insn-009ad214) → [`009ad228`](#insn-009ad228)
  - `FALL_THROUGH` [`009ad214`](#insn-009ad214) → [`009ad218`](#insn-009ad218)
- ブロック [`009ad218`](#insn-009ad218) 範囲 `[['009ad218', '009ad21b']]`
  - `UNCONDITIONAL_JUMP` [`009ad218`](#insn-009ad218) → [`009ad260`](#insn-009ad260)
- ブロック [`009ad21c`](#insn-009ad21c) 範囲 `[['009ad21c', '009ad21f']]`
  - `FALL_THROUGH` [`009ad21c`](#insn-009ad21c) → [`009ad220`](#insn-009ad220)
- ブロック [`009ad220`](#insn-009ad220) 範囲 `[['009ad220', '009ad227']]`
  - `CONDITIONAL_JUMP` [`009ad224`](#insn-009ad224) → [`009ad25c`](#insn-009ad25c)
  - `FALL_THROUGH` [`009ad224`](#insn-009ad224) → [`009ad228`](#insn-009ad228)
- ブロック [`009ad228`](#insn-009ad228) 範囲 `[['009ad228', '009ad22f']]`
  - `CONDITIONAL_JUMP` [`009ad22c`](#insn-009ad22c) → [`009ad21c`](#insn-009ad21c)
  - `FALL_THROUGH` [`009ad22c`](#insn-009ad22c) → [`009ad230`](#insn-009ad230)
- ブロック [`009ad230`](#insn-009ad230) 範囲 `[['009ad230', '009ad23f']]`
  - `CONDITIONAL_JUMP` [`009ad23c`](#insn-009ad23c) → [`009ad21c`](#insn-009ad21c)
  - `FALL_THROUGH` [`009ad23c`](#insn-009ad23c) → [`009ad240`](#insn-009ad240)
- ブロック [`009ad240`](#insn-009ad240) 範囲 `[['009ad240', '009ad25b']]`
  - `UNCONDITIONAL_JUMP` [`009ad258`](#insn-009ad258) → [`009ad21c`](#insn-009ad21c)
- ブロック [`009ad25c`](#insn-009ad25c) 範囲 `[['009ad25c', '009ad25f']]`
  - `FALL_THROUGH` [`009ad25c`](#insn-009ad25c) → [`009ad260`](#insn-009ad260)
- ブロック [`009ad260`](#insn-009ad260) 範囲 `[['009ad260', '009ad263']]`
  - `FALL_THROUGH` [`009ad260`](#insn-009ad260) → [`009ad264`](#insn-009ad264)
- ブロック [`009ad264`](#insn-009ad264) 範囲 `[['009ad264', '009ad26f']]`
  - `CONDITIONAL_JUMP` [`009ad26c`](#insn-009ad26c) → [`009ad298`](#insn-009ad298)
  - `FALL_THROUGH` [`009ad26c`](#insn-009ad26c) → [`009ad270`](#insn-009ad270)
- ブロック [`009ad270`](#insn-009ad270) 範囲 `[['009ad270', '009ad277']]`
  - `CONDITIONAL_JUMP` [`009ad274`](#insn-009ad274) → [`009ad3f0`](#insn-009ad3f0)
  - `FALL_THROUGH` [`009ad274`](#insn-009ad274) → [`009ad278`](#insn-009ad278)
- ブロック [`009ad278`](#insn-009ad278) 範囲 `[['009ad278', '009ad287']]`
  - `CONDITIONAL_JUMP` [`009ad284`](#insn-009ad284) → [`009ad3b0`](#insn-009ad3b0)
  - `FALL_THROUGH` [`009ad284`](#insn-009ad284) → [`009ad288`](#insn-009ad288)
- ブロック [`009ad288`](#insn-009ad288) 範囲 `[['009ad288', '009ad28b']]`
  - `UNCONDITIONAL_JUMP` [`009ad288`](#insn-009ad288) → [`009ad3e8`](#insn-009ad3e8)
- ブロック [`009ad28c`](#insn-009ad28c) 範囲 `[['009ad28c', '009ad297']]`
  - `CONDITIONAL_JUMP` [`009ad294`](#insn-009ad294) → [`009ad270`](#insn-009ad270)
  - `FALL_THROUGH` [`009ad294`](#insn-009ad294) → [`009ad298`](#insn-009ad298)
- ブロック [`009ad298`](#insn-009ad298) 範囲 `[['009ad298', '009ad2a3']]`
  - `CONDITIONAL_JUMP` [`009ad2a0`](#insn-009ad2a0) → [`009ad28c`](#insn-009ad28c)
  - `FALL_THROUGH` [`009ad2a0`](#insn-009ad2a0) → [`009ad2a4`](#insn-009ad2a4)
- ブロック [`009ad2a4`](#insn-009ad2a4) 範囲 `[['009ad2a4', '009ad2ab']]`
  - `UNCONDITIONAL_JUMP` [`009ad2a8`](#insn-009ad2a8) → [`009ad2b8`](#insn-009ad2b8)
- ブロック [`009ad2ac`](#insn-009ad2ac) 範囲 `[['009ad2ac', '009ad2af']]`
  - `FALL_THROUGH` [`009ad2ac`](#insn-009ad2ac) → [`009ad2b0`](#insn-009ad2b0)
- ブロック [`009ad2b0`](#insn-009ad2b0) 範囲 `[['009ad2b0', '009ad2b7']]`
  - `CONDITIONAL_JUMP` [`009ad2b4`](#insn-009ad2b4) → [`009ad28c`](#insn-009ad28c)
  - `FALL_THROUGH` [`009ad2b4`](#insn-009ad2b4) → [`009ad2b8`](#insn-009ad2b8)
- ブロック [`009ad2b8`](#insn-009ad2b8) 範囲 `[['009ad2b8', '009ad2c3']]`
  - `CONDITIONAL_JUMP` [`009ad2c0`](#insn-009ad2c0) → [`009ad2d0`](#insn-009ad2d0)
  - `FALL_THROUGH` [`009ad2c0`](#insn-009ad2c0) → [`009ad2c4`](#insn-009ad2c4)
- ブロック [`009ad2c4`](#insn-009ad2c4) 範囲 `[['009ad2c4', '009ad2cf']]`
  - `FALL_THROUGH` [`009ad2cc`](#insn-009ad2cc) → [`009ad2d0`](#insn-009ad2d0)
- ブロック [`009ad2d0`](#insn-009ad2d0) 範囲 `[['009ad2d0', '009ad2df']]`
  - `CONDITIONAL_JUMP` [`009ad2dc`](#insn-009ad2dc) → [`009ad2f8`](#insn-009ad2f8)
  - `FALL_THROUGH` [`009ad2dc`](#insn-009ad2dc) → [`009ad2e0`](#insn-009ad2e0)
- ブロック [`009ad2e0`](#insn-009ad2e0) 範囲 `[['009ad2e0', '009ad2f7']]`
  - `CONDITIONAL_JUMP` [`009ad2f4`](#insn-009ad2f4) → [`009ad32c`](#insn-009ad32c)
  - `FALL_THROUGH` [`009ad2f4`](#insn-009ad2f4) → [`009ad2f8`](#insn-009ad2f8)
- ブロック [`009ad2f8`](#insn-009ad2f8) 範囲 `[['009ad2f8', '009ad2ff']]`
  - `CONDITIONAL_JUMP` [`009ad2fc`](#insn-009ad2fc) → [`009ad2ac`](#insn-009ad2ac)
  - `FALL_THROUGH` [`009ad2fc`](#insn-009ad2fc) → [`009ad300`](#insn-009ad300)
- ブロック [`009ad300`](#insn-009ad300) 範囲 `[['009ad300', '009ad30f']]`
  - `CONDITIONAL_JUMP` [`009ad30c`](#insn-009ad30c) → [`009ad2ac`](#insn-009ad2ac)
  - `FALL_THROUGH` [`009ad30c`](#insn-009ad30c) → [`009ad310`](#insn-009ad310)
- ブロック [`009ad310`](#insn-009ad310) 範囲 `[['009ad310', '009ad32b']]`
  - `UNCONDITIONAL_JUMP` [`009ad328`](#insn-009ad328) → [`009ad2ac`](#insn-009ad2ac)
- ブロック [`009ad32c`](#insn-009ad32c) 範囲 `[['009ad32c', '009ad337']]`
  - `CONDITIONAL_JUMP` [`009ad334`](#insn-009ad334) → [`009ad360`](#insn-009ad360)
  - `FALL_THROUGH` [`009ad334`](#insn-009ad334) → [`009ad338`](#insn-009ad338)
- ブロック [`009ad338`](#insn-009ad338) 範囲 `[['009ad338', '009ad34b']]`
  - `CONDITIONAL_JUMP` [`009ad348`](#insn-009ad348) → [`009ad358`](#insn-009ad358)
  - `FALL_THROUGH` [`009ad348`](#insn-009ad348) → [`009ad34c`](#insn-009ad34c)
- ブロック [`009ad34c`](#insn-009ad34c) 範囲 `[['009ad34c', '009ad357']]`
  - `FALL_THROUGH` [`009ad354`](#insn-009ad354) → [`009ad358`](#insn-009ad358)
- ブロック [`009ad358`](#insn-009ad358) 範囲 `[['009ad358', '009ad35f']]`
  - `UNCONDITIONAL_JUMP` [`009ad35c`](#insn-009ad35c) → [`009ad36c`](#insn-009ad36c)
- ブロック [`009ad360`](#insn-009ad360) 範囲 `[['009ad360', '009ad367']]`
  - `FALL_THROUGH` [`009ad364`](#insn-009ad364) → [`009ad368`](#insn-009ad368)
- ブロック [`009ad368`](#insn-009ad368) 範囲 `[['009ad368', '009ad36b']]`
  - `FALL_THROUGH` [`009ad368`](#insn-009ad368) → [`009ad36c`](#insn-009ad36c)
- ブロック [`009ad36c`](#insn-009ad36c) 範囲 `[['009ad36c', '009ad377']]`
  - `CONDITIONAL_JUMP` [`009ad374`](#insn-009ad374) → [`009ad28c`](#insn-009ad28c)
  - `FALL_THROUGH` [`009ad374`](#insn-009ad374) → [`009ad378`](#insn-009ad378)
- ブロック [`009ad378`](#insn-009ad378) 範囲 `[['009ad378', '009ad387']]`
  - `CONDITIONAL_JUMP` [`009ad384`](#insn-009ad384) → [`009ad28c`](#insn-009ad28c)
  - `FALL_THROUGH` [`009ad384`](#insn-009ad384) → [`009ad388`](#insn-009ad388)
- ブロック [`009ad388`](#insn-009ad388) 範囲 `[['009ad388', '009ad3a3']]`
  - `UNCONDITIONAL_JUMP` [`009ad3a0`](#insn-009ad3a0) → [`009ad28c`](#insn-009ad28c)
- ブロック [`009ad3a4`](#insn-009ad3a4) 範囲 `[['009ad3a4', '009ad3af']]`
  - `CONDITIONAL_JUMP` [`009ad3ac`](#insn-009ad3ac) → [`009ad3e4`](#insn-009ad3e4)
  - `FALL_THROUGH` [`009ad3ac`](#insn-009ad3ac) → [`009ad3b0`](#insn-009ad3b0)
- ブロック [`009ad3b0`](#insn-009ad3b0) 範囲 `[['009ad3b0', '009ad3b7']]`
  - `CONDITIONAL_JUMP` [`009ad3b4`](#insn-009ad3b4) → [`009ad3a4`](#insn-009ad3a4)
  - `FALL_THROUGH` [`009ad3b4`](#insn-009ad3b4) → [`009ad3b8`](#insn-009ad3b8)
- ブロック [`009ad3b8`](#insn-009ad3b8) 範囲 `[['009ad3b8', '009ad3c7']]`
  - `CONDITIONAL_JUMP` [`009ad3c4`](#insn-009ad3c4) → [`009ad3a4`](#insn-009ad3a4)
  - `FALL_THROUGH` [`009ad3c4`](#insn-009ad3c4) → [`009ad3c8`](#insn-009ad3c8)
- ブロック [`009ad3c8`](#insn-009ad3c8) 範囲 `[['009ad3c8', '009ad3e3']]`
  - `UNCONDITIONAL_JUMP` [`009ad3e0`](#insn-009ad3e0) → [`009ad3a4`](#insn-009ad3a4)
- ブロック [`009ad3e4`](#insn-009ad3e4) 範囲 `[['009ad3e4', '009ad3e7']]`
  - `FALL_THROUGH` [`009ad3e4`](#insn-009ad3e4) → [`009ad3e8`](#insn-009ad3e8)
- ブロック [`009ad3e8`](#insn-009ad3e8) 範囲 `[['009ad3e8', '009ad3ef']]`
  - `FALL_THROUGH` [`009ad3ec`](#insn-009ad3ec) → [`009ad3f0`](#insn-009ad3f0)
- ブロック [`009ad3f0`](#insn-009ad3f0) 範囲 `[['009ad3f0', '009ad3f7']]`
  - `CONDITIONAL_JUMP` [`009ad3f4`](#insn-009ad3f4) → [`009ad3fc`](#insn-009ad3fc)
  - `FALL_THROUGH` [`009ad3f4`](#insn-009ad3f4) → [`009ad3f8`](#insn-009ad3f8)
- ブロック [`009ad3f8`](#insn-009ad3f8) 範囲 `[['009ad3f8', '009ad3fb']]`
  - `FALL_THROUGH` [`009ad3f8`](#insn-009ad3f8) → [`009ad3fc`](#insn-009ad3fc)
- ブロック [`009ad3fc`](#insn-009ad3fc) 範囲 `[['009ad3fc', '009ad40f']]`
  - `CONDITIONAL_JUMP` [`009ad40c`](#insn-009ad40c) → [`009ad4f4`](#insn-009ad4f4)
  - `FALL_THROUGH` [`009ad40c`](#insn-009ad40c) → [`009ad410`](#insn-009ad410)
- ブロック [`009ad410`](#insn-009ad410) 範囲 `[['009ad410', '009ad42f']]`
- ブロック [`009ad430`](#insn-009ad430) 範囲 `[['009ad430', '009ad43b']]`
  - `FALL_THROUGH` [`009ad438`](#insn-009ad438) → [`009ad43c`](#insn-009ad43c)
- ブロック [`009ad43c`](#insn-009ad43c) 範囲 `[['009ad43c', '009ad443']]`
  - `CONDITIONAL_JUMP` [`009ad440`](#insn-009ad440) → [`009ad4f4`](#insn-009ad4f4)
  - `FALL_THROUGH` [`009ad440`](#insn-009ad440) → [`009ad444`](#insn-009ad444)
- ブロック [`009ad444`](#insn-009ad444) 範囲 `[['009ad444', '009ad44b']]`
  - `FALL_THROUGH` [`009ad448`](#insn-009ad448) → [`009ad44c`](#insn-009ad44c)
- ブロック [`009ad44c`](#insn-009ad44c) 範囲 `[['009ad44c', '009ad45f']]`
  - `CONDITIONAL_JUMP` [`009ad45c`](#insn-009ad45c) → [`009ad4f4`](#insn-009ad4f4)
  - `FALL_THROUGH` [`009ad45c`](#insn-009ad45c) → [`009ad460`](#insn-009ad460)
- ブロック [`009ad460`](#insn-009ad460) 範囲 `[['009ad460', '009ad463']]`
- ブロック [`009ad464`](#insn-009ad464) 範囲 `[['009ad464', '009ad477']]`
  - `CONDITIONAL_JUMP` [`009ad474`](#insn-009ad474) → [`009ad4f4`](#insn-009ad4f4)
  - `FALL_THROUGH` [`009ad474`](#insn-009ad474) → [`009ad478`](#insn-009ad478)
- ブロック [`009ad478`](#insn-009ad478) 範囲 `[['009ad478', '009ad48f']]`
  - `UNCONDITIONAL_JUMP` [`009ad48c`](#insn-009ad48c) → [`009ad4c8`](#insn-009ad4c8)
- ブロック [`009ad4c8`](#insn-009ad4c8) 範囲 `[['009ad4c8', '009ad4cf']]`
  - `CONDITIONAL_JUMP` [`009ad4cc`](#insn-009ad4cc) → [`009ad4d8`](#insn-009ad4d8)
  - `FALL_THROUGH` [`009ad4cc`](#insn-009ad4cc) → [`009ad4d0`](#insn-009ad4d0)
- ブロック [`009ad4d0`](#insn-009ad4d0) 範囲 `[['009ad4d0', '009ad4d7']]`
  - `FALL_THROUGH` [`009ad4d4`](#insn-009ad4d4) → [`009ad4d8`](#insn-009ad4d8)
- ブロック [`009ad4d8`](#insn-009ad4d8) 範囲 `[['009ad4d8', '009ad4df']]`
  - `FALL_THROUGH` [`009ad4dc`](#insn-009ad4dc) → [`009ad4e0`](#insn-009ad4e0)
- ブロック [`009ad4e0`](#insn-009ad4e0) 範囲 `[['009ad4e0', '009ad4eb']]`
  - `CONDITIONAL_JUMP` [`009ad4e8`](#insn-009ad4e8) → [`009ad4f4`](#insn-009ad4f4)
  - `FALL_THROUGH` [`009ad4e8`](#insn-009ad4e8) → [`009ad4ec`](#insn-009ad4ec)
- ブロック [`009ad4ec`](#insn-009ad4ec) 範囲 `[['009ad4ec', '009ad4f3']]`
- ブロック [`009ad4f4`](#insn-009ad4f4) 範囲 `[['009ad4f4', '009ad4f7']]`

## 命令位置別の参照

- [`009acfc0`](#insn-009acfc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfc4`](#insn-009acfc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfc8`](#insn-009acfc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfcc`](#insn-009acfcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfd0`](#insn-009acfd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfd4`](#insn-009acfd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfe4`](#insn-009acfe4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfec`](#insn-009acfec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acff4`](#insn-009acff4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acff8`](#insn-009acff8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad000`](#insn-009ad000) → [`009ad01c`](#insn-009ad01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad00c`](#insn-009ad00c) → [`009ad164`](#insn-009ad164) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad018`](#insn-009ad018) → [`009ad160`](#insn-009ad160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad020`](#insn-009ad020) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad024`](#insn-009ad024) → [`009ad034`](#insn-009ad034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad030`](#insn-009ad030) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`009ad034`](#insn-009ad034) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad040`](#insn-009ad040) → [`009ad064`](#insn-009ad064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad04c`](#insn-009ad04c) → [`009b41a8`](../009b4/009b41a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b41a8` · 推定シンボル `None` · 推定型 `None`
- [`009ad054`](#insn-009ad054) → [`009ad0a0`](#insn-009ad0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad060`](#insn-009ad060) → [`009ad044`](#insn-009ad044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad068`](#insn-009ad068) → [`009b5cf8`](../009b5/009b5cf8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5cf8` · 推定シンボル `None` · 推定型 `None`
- [`009ad06c`](#insn-009ad06c) → [`009ad0a0`](#insn-009ad0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad074`](#insn-009ad074) → [`009b41a8`](../009b4/009b41a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b41a8` · 推定シンボル `None` · 推定型 `None`
- [`009ad080`](#insn-009ad080) → [`009b5ce8`](../009b5/009b5ce8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5ce8` · 推定シンボル `None` · 推定型 `None`
- [`009ad084`](#insn-009ad084) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad094`](#insn-009ad094) → [`009ad0d0`](#insn-009ad0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad09c`](#insn-009ad09c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0a0`](#insn-009ad0a0) → [`009ad010`](#insn-009ad010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0ac`](#insn-009ad0ac) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009ad0b0`](#insn-009ad0b0) → [`009ad010`](#insn-009ad010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0c8`](#insn-009ad0c8) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009ad0cc`](#insn-009ad0cc) → [`009ad010`](#insn-009ad010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0e0`](#insn-009ad0e0) → [`009ad430`](#insn-009ad430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad104`](#insn-009ad104) → [`009ad120`](#insn-009ad120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad10c`](#insn-009ad10c) → [`009ad44c`](#insn-009ad44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad114`](#insn-009ad114) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`009ad11c`](#insn-009ad11c) → [`009ad124`](#insn-009ad124) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad13c`](#insn-009ad13c) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`009ad140`](#insn-009ad140) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad144`](#insn-009ad144) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad148`](#insn-009ad148) → [`009ad154`](#insn-009ad154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad150`](#insn-009ad150) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009ad154`](#insn-009ad154) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad158`](#insn-009ad158) → [`009ad0a4`](#insn-009ad0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad15c`](#insn-009ad15c) → [`009ad010`](#insn-009ad010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad160`](#insn-009ad160) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad190`](#insn-009ad190) → [`009b0dac`](../009b0/009b0dac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b0dac` · 推定シンボル `None` · 推定型 `None`
- [`009ad19c`](#insn-009ad19c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1a0`](#insn-009ad1a0) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1a8`](#insn-009ad1a8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1ac`](#insn-009ad1ac) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1b0`](#insn-009ad1b0) → [`009ad260`](#insn-009ad260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1b4`](#insn-009ad1b4) → [`009ad464`](#insn-009ad464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1bc`](#insn-009ad1bc) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`009ad1c8`](#insn-009ad1c8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1cc`](#insn-009ad1cc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1d0`](#insn-009ad1d0) → [`009ad1e4`](#insn-009ad1e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1e0`](#insn-009ad1e0) → [`009ad208`](#insn-009ad208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1f4`](#insn-009ad1f4) → [`009ad1d4`](#insn-009ad1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad200`](#insn-009ad200) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`009ad204`](#insn-009ad204) → [`009ad1d4`](#insn-009ad1d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad20c`](#insn-009ad20c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad214`](#insn-009ad214) → [`009ad228`](#insn-009ad228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad218`](#insn-009ad218) → [`009ad260`](#insn-009ad260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad224`](#insn-009ad224) → [`009ad25c`](#insn-009ad25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad22c`](#insn-009ad22c) → [`009ad21c`](#insn-009ad21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad238`](#insn-009ad238) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009ad23c`](#insn-009ad23c) → [`009ad21c`](#insn-009ad21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad254`](#insn-009ad254) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009ad258`](#insn-009ad258) → [`009ad21c`](#insn-009ad21c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad25c`](#insn-009ad25c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad260`](#insn-009ad260) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad26c`](#insn-009ad26c) → [`009ad298`](#insn-009ad298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad270`](#insn-009ad270) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad274`](#insn-009ad274) → [`009ad3f0`](#insn-009ad3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad278`](#insn-009ad278) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad284`](#insn-009ad284) → [`009ad3b0`](#insn-009ad3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad288`](#insn-009ad288) → [`009ad3e8`](#insn-009ad3e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad294`](#insn-009ad294) → [`009ad270`](#insn-009ad270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad298`](#insn-009ad298) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2a0`](#insn-009ad2a0) → [`009ad28c`](#insn-009ad28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2a8`](#insn-009ad2a8) → [`009ad2b8`](#insn-009ad2b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2b4`](#insn-009ad2b4) → [`009ad28c`](#insn-009ad28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2bc`](#insn-009ad2bc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2c0`](#insn-009ad2c0) → [`009ad2d0`](#insn-009ad2d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2cc`](#insn-009ad2cc) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`009ad2d4`](#insn-009ad2d4) → [`009b41a8`](../009b4/009b41a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b41a8` · 推定シンボル `None` · 推定型 `None`
- [`009ad2dc`](#insn-009ad2dc) → [`009ad2f8`](#insn-009ad2f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2e0`](#insn-009ad2e0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2e4`](#insn-009ad2e4) → [`009b5ce8`](../009b5/009b5ce8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5ce8` · 推定シンボル `None` · 推定型 `None`
- [`009ad2f0`](#insn-009ad2f0) → [`0080666c`](../00806/0080666c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080666c` · 推定シンボル `None` · 推定型 `None`
- [`009ad2f4`](#insn-009ad2f4) → [`009ad32c`](#insn-009ad32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2f8`](#insn-009ad2f8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2fc`](#insn-009ad2fc) → [`009ad2ac`](#insn-009ad2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad308`](#insn-009ad308) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009ad30c`](#insn-009ad30c) → [`009ad2ac`](#insn-009ad2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad324`](#insn-009ad324) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009ad328`](#insn-009ad328) → [`009ad2ac`](#insn-009ad2ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad334`](#insn-009ad334) → [`009ad360`](#insn-009ad360) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad338`](#insn-009ad338) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad340`](#insn-009ad340) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad348`](#insn-009ad348) → [`009ad358`](#insn-009ad358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad354`](#insn-009ad354) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`009ad35c`](#insn-009ad35c) → [`009ad36c`](#insn-009ad36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad368`](#insn-009ad368) → [`009b0c3c`](../009b0/009b0c3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b0c3c` · 推定シンボル `None` · 推定型 `None`
- [`009ad36c`](#insn-009ad36c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad374`](#insn-009ad374) → [`009ad28c`](#insn-009ad28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad380`](#insn-009ad380) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009ad384`](#insn-009ad384) → [`009ad28c`](#insn-009ad28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad39c`](#insn-009ad39c) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009ad3a0`](#insn-009ad3a0) → [`009ad28c`](#insn-009ad28c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3ac`](#insn-009ad3ac) → [`009ad3e4`](#insn-009ad3e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3b4`](#insn-009ad3b4) → [`009ad3a4`](#insn-009ad3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3c0`](#insn-009ad3c0) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009ad3c4`](#insn-009ad3c4) → [`009ad3a4`](#insn-009ad3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3dc`](#insn-009ad3dc) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009ad3e0`](#insn-009ad3e0) → [`009ad3a4`](#insn-009ad3a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3e4`](#insn-009ad3e4) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3e8`](#insn-009ad3e8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3ec`](#insn-009ad3ec) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009ad3f0`](#insn-009ad3f0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3f4`](#insn-009ad3f4) → [`009ad3fc`](#insn-009ad3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad3f8`](#insn-009ad3f8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009ad3fc`](#insn-009ad3fc) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad404`](#insn-009ad404) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad40c`](#insn-009ad40c) → [`009ad4f4`](#insn-009ad4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad410`](#insn-009ad410) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad414`](#insn-009ad414) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad418`](#insn-009ad418) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad41c`](#insn-009ad41c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad420`](#insn-009ad420) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad424`](#insn-009ad424) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad430`](#insn-009ad430) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad438`](#insn-009ad438) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad440`](#insn-009ad440) → [`009ad4f4`](#insn-009ad4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad448`](#insn-009ad448) → [`006b8c9c`](../006b8/006b8c9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b8c9c` · 推定シンボル `None` · 推定型 `None`
- [`009ad44c`](#insn-009ad44c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad454`](#insn-009ad454) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad45c`](#insn-009ad45c) → [`009ad4f4`](#insn-009ad4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad460`](#insn-009ad460) → [`00440f00`](../00440/00440f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440f00` · 推定シンボル `None` · 推定型 `None`
- [`009ad464`](#insn-009ad464) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad46c`](#insn-009ad46c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad474`](#insn-009ad474) → [`009ad4f4`](#insn-009ad4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad47c`](#insn-009ad47c) → [`009b0d98`](../009b0/009b0d98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b0d98` · 推定シンボル `None` · 推定型 `None`
- [`009ad488`](#insn-009ad488) → [`009b1e30`](../009b1/009b1e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b1e30` · 推定シンボル `None` · 推定型 `None`
- [`009ad48c`](#insn-009ad48c) → [`009ad4c8`](#insn-009ad4c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad4c8`](#insn-009ad4c8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad4cc`](#insn-009ad4cc) → [`009ad4d8`](#insn-009ad4d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad4d0`](#insn-009ad4d0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad4d4`](#insn-009ad4d4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009ad4d8`](#insn-009ad4d8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad4e0`](#insn-009ad4e0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad4e8`](#insn-009ad4e8) → [`009ad4f4`](#insn-009ad4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad4f0`](#insn-009ad4f0) → [`00c53ffc`](../00c53/00c53ffc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53ffc` · 推定シンボル `None` · 推定型 `None`
- [`009ad4f4`](#insn-009ad4f4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009acfc0`](#insn-009acfc0)

~~~json
{
  "source": "009acfc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfc4`](#insn-009acfc4)

~~~json
{
  "source": "009acfc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfc8`](#insn-009acfc8)

~~~json
{
  "source": "009acfc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfcc`](#insn-009acfcc)

~~~json
{
  "source": "009acfcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfd0`](#insn-009acfd0)

~~~json
{
  "source": "009acfd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfd4`](#insn-009acfd4)

~~~json
{
  "source": "009acfd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfe4`](#insn-009acfe4)

~~~json
{
  "source": "009acfe4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfec`](#insn-009acfec)

~~~json
{
  "source": "009acfec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acff4`](#insn-009acff4)

~~~json
{
  "source": "009acff4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acff8`](#insn-009acff8)

~~~json
{
  "source": "009acff8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad000`](#insn-009ad000)

~~~json
{
  "source": "009ad000",
  "target": "009ad01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad00c`](#insn-009ad00c)

~~~json
{
  "source": "009ad00c",
  "target": "009ad164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad018`](#insn-009ad018)

~~~json
{
  "source": "009ad018",
  "target": "009ad160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad020`](#insn-009ad020)

~~~json
{
  "source": "009ad020",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad024`](#insn-009ad024)

~~~json
{
  "source": "009ad024",
  "target": "009ad034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad030`](#insn-009ad030)

~~~json
{
  "source": "009ad030",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad034`](#insn-009ad034)

~~~json
{
  "source": "009ad034",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad040`](#insn-009ad040)

~~~json
{
  "source": "009ad040",
  "target": "009ad064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad04c`](#insn-009ad04c)

~~~json
{
  "source": "009ad04c",
  "target": "009b41a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad054`](#insn-009ad054)

~~~json
{
  "source": "009ad054",
  "target": "009ad0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad060`](#insn-009ad060)

~~~json
{
  "source": "009ad060",
  "target": "009ad044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad068`](#insn-009ad068)

~~~json
{
  "source": "009ad068",
  "target": "009b5cf8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad06c`](#insn-009ad06c)

~~~json
{
  "source": "009ad06c",
  "target": "009ad0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad074`](#insn-009ad074)

~~~json
{
  "source": "009ad074",
  "target": "009b41a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad080`](#insn-009ad080)

~~~json
{
  "source": "009ad080",
  "target": "009b5ce8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad084`](#insn-009ad084)

~~~json
{
  "source": "009ad084",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad094`](#insn-009ad094)

~~~json
{
  "source": "009ad094",
  "target": "009ad0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad09c`](#insn-009ad09c)

~~~json
{
  "source": "009ad09c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0a0`](#insn-009ad0a0)

~~~json
{
  "source": "009ad0a0",
  "target": "009ad010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0ac`](#insn-009ad0ac)

~~~json
{
  "source": "009ad0ac",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad0b0`](#insn-009ad0b0)

~~~json
{
  "source": "009ad0b0",
  "target": "009ad010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0c8`](#insn-009ad0c8)

~~~json
{
  "source": "009ad0c8",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad0cc`](#insn-009ad0cc)

~~~json
{
  "source": "009ad0cc",
  "target": "009ad010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0e0`](#insn-009ad0e0)

~~~json
{
  "source": "009ad0e0",
  "target": "009ad430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad104`](#insn-009ad104)

~~~json
{
  "source": "009ad104",
  "target": "009ad120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad10c`](#insn-009ad10c)

~~~json
{
  "source": "009ad10c",
  "target": "009ad44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad114`](#insn-009ad114)

~~~json
{
  "source": "009ad114",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad11c`](#insn-009ad11c)

~~~json
{
  "source": "009ad11c",
  "target": "009ad124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad13c`](#insn-009ad13c)

~~~json
{
  "source": "009ad13c",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad140`](#insn-009ad140)

~~~json
{
  "source": "009ad140",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad144`](#insn-009ad144)

~~~json
{
  "source": "009ad144",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad148`](#insn-009ad148)

~~~json
{
  "source": "009ad148",
  "target": "009ad154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad150`](#insn-009ad150)

~~~json
{
  "source": "009ad150",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad154`](#insn-009ad154)

~~~json
{
  "source": "009ad154",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad158`](#insn-009ad158)

~~~json
{
  "source": "009ad158",
  "target": "009ad0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad15c`](#insn-009ad15c)

~~~json
{
  "source": "009ad15c",
  "target": "009ad010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad160`](#insn-009ad160)

~~~json
{
  "source": "009ad160",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad190`](#insn-009ad190)

~~~json
{
  "source": "009ad190",
  "target": "009b0dac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad19c`](#insn-009ad19c)

~~~json
{
  "source": "009ad19c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1a0`](#insn-009ad1a0)

~~~json
{
  "source": "009ad1a0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1a8`](#insn-009ad1a8)

~~~json
{
  "source": "009ad1a8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1ac`](#insn-009ad1ac)

~~~json
{
  "source": "009ad1ac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1b0`](#insn-009ad1b0)

~~~json
{
  "source": "009ad1b0",
  "target": "009ad260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1b4`](#insn-009ad1b4)

~~~json
{
  "source": "009ad1b4",
  "target": "009ad464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1bc`](#insn-009ad1bc)

~~~json
{
  "source": "009ad1bc",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad1c8`](#insn-009ad1c8)

~~~json
{
  "source": "009ad1c8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1cc`](#insn-009ad1cc)

~~~json
{
  "source": "009ad1cc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1d0`](#insn-009ad1d0)

~~~json
{
  "source": "009ad1d0",
  "target": "009ad1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1e0`](#insn-009ad1e0)

~~~json
{
  "source": "009ad1e0",
  "target": "009ad208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1f4`](#insn-009ad1f4)

~~~json
{
  "source": "009ad1f4",
  "target": "009ad1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad200`](#insn-009ad200)

~~~json
{
  "source": "009ad200",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad204`](#insn-009ad204)

~~~json
{
  "source": "009ad204",
  "target": "009ad1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad20c`](#insn-009ad20c)

~~~json
{
  "source": "009ad20c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad214`](#insn-009ad214)

~~~json
{
  "source": "009ad214",
  "target": "009ad228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad218`](#insn-009ad218)

~~~json
{
  "source": "009ad218",
  "target": "009ad260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad224`](#insn-009ad224)

~~~json
{
  "source": "009ad224",
  "target": "009ad25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad22c`](#insn-009ad22c)

~~~json
{
  "source": "009ad22c",
  "target": "009ad21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad238`](#insn-009ad238)

~~~json
{
  "source": "009ad238",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad23c`](#insn-009ad23c)

~~~json
{
  "source": "009ad23c",
  "target": "009ad21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad254`](#insn-009ad254)

~~~json
{
  "source": "009ad254",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad258`](#insn-009ad258)

~~~json
{
  "source": "009ad258",
  "target": "009ad21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad25c`](#insn-009ad25c)

~~~json
{
  "source": "009ad25c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad260`](#insn-009ad260)

~~~json
{
  "source": "009ad260",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad26c`](#insn-009ad26c)

~~~json
{
  "source": "009ad26c",
  "target": "009ad298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad270`](#insn-009ad270)

~~~json
{
  "source": "009ad270",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad274`](#insn-009ad274)

~~~json
{
  "source": "009ad274",
  "target": "009ad3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad278`](#insn-009ad278)

~~~json
{
  "source": "009ad278",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad284`](#insn-009ad284)

~~~json
{
  "source": "009ad284",
  "target": "009ad3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad288`](#insn-009ad288)

~~~json
{
  "source": "009ad288",
  "target": "009ad3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad294`](#insn-009ad294)

~~~json
{
  "source": "009ad294",
  "target": "009ad270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad298`](#insn-009ad298)

~~~json
{
  "source": "009ad298",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2a0`](#insn-009ad2a0)

~~~json
{
  "source": "009ad2a0",
  "target": "009ad28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2a8`](#insn-009ad2a8)

~~~json
{
  "source": "009ad2a8",
  "target": "009ad2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2b4`](#insn-009ad2b4)

~~~json
{
  "source": "009ad2b4",
  "target": "009ad28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2bc`](#insn-009ad2bc)

~~~json
{
  "source": "009ad2bc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2c0`](#insn-009ad2c0)

~~~json
{
  "source": "009ad2c0",
  "target": "009ad2d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2cc`](#insn-009ad2cc)

~~~json
{
  "source": "009ad2cc",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad2d4`](#insn-009ad2d4)

~~~json
{
  "source": "009ad2d4",
  "target": "009b41a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad2dc`](#insn-009ad2dc)

~~~json
{
  "source": "009ad2dc",
  "target": "009ad2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2e0`](#insn-009ad2e0)

~~~json
{
  "source": "009ad2e0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2e4`](#insn-009ad2e4)

~~~json
{
  "source": "009ad2e4",
  "target": "009b5ce8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad2f0`](#insn-009ad2f0)

~~~json
{
  "source": "009ad2f0",
  "target": "0080666c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad2f4`](#insn-009ad2f4)

~~~json
{
  "source": "009ad2f4",
  "target": "009ad32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2f8`](#insn-009ad2f8)

~~~json
{
  "source": "009ad2f8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2fc`](#insn-009ad2fc)

~~~json
{
  "source": "009ad2fc",
  "target": "009ad2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad308`](#insn-009ad308)

~~~json
{
  "source": "009ad308",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad30c`](#insn-009ad30c)

~~~json
{
  "source": "009ad30c",
  "target": "009ad2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad324`](#insn-009ad324)

~~~json
{
  "source": "009ad324",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad328`](#insn-009ad328)

~~~json
{
  "source": "009ad328",
  "target": "009ad2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad334`](#insn-009ad334)

~~~json
{
  "source": "009ad334",
  "target": "009ad360",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad338`](#insn-009ad338)

~~~json
{
  "source": "009ad338",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad340`](#insn-009ad340)

~~~json
{
  "source": "009ad340",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad348`](#insn-009ad348)

~~~json
{
  "source": "009ad348",
  "target": "009ad358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad354`](#insn-009ad354)

~~~json
{
  "source": "009ad354",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad35c`](#insn-009ad35c)

~~~json
{
  "source": "009ad35c",
  "target": "009ad36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad368`](#insn-009ad368)

~~~json
{
  "source": "009ad368",
  "target": "009b0c3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad36c`](#insn-009ad36c)

~~~json
{
  "source": "009ad36c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad374`](#insn-009ad374)

~~~json
{
  "source": "009ad374",
  "target": "009ad28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad380`](#insn-009ad380)

~~~json
{
  "source": "009ad380",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad384`](#insn-009ad384)

~~~json
{
  "source": "009ad384",
  "target": "009ad28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad39c`](#insn-009ad39c)

~~~json
{
  "source": "009ad39c",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad3a0`](#insn-009ad3a0)

~~~json
{
  "source": "009ad3a0",
  "target": "009ad28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3ac`](#insn-009ad3ac)

~~~json
{
  "source": "009ad3ac",
  "target": "009ad3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3b4`](#insn-009ad3b4)

~~~json
{
  "source": "009ad3b4",
  "target": "009ad3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3c0`](#insn-009ad3c0)

~~~json
{
  "source": "009ad3c0",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad3c4`](#insn-009ad3c4)

~~~json
{
  "source": "009ad3c4",
  "target": "009ad3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3dc`](#insn-009ad3dc)

~~~json
{
  "source": "009ad3dc",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad3e0`](#insn-009ad3e0)

~~~json
{
  "source": "009ad3e0",
  "target": "009ad3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3e4`](#insn-009ad3e4)

~~~json
{
  "source": "009ad3e4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3e8`](#insn-009ad3e8)

~~~json
{
  "source": "009ad3e8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3ec`](#insn-009ad3ec)

~~~json
{
  "source": "009ad3ec",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad3f0`](#insn-009ad3f0)

~~~json
{
  "source": "009ad3f0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3f4`](#insn-009ad3f4)

~~~json
{
  "source": "009ad3f4",
  "target": "009ad3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad3f8`](#insn-009ad3f8)

~~~json
{
  "source": "009ad3f8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad3fc`](#insn-009ad3fc)

~~~json
{
  "source": "009ad3fc",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad404`](#insn-009ad404)

~~~json
{
  "source": "009ad404",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad40c`](#insn-009ad40c)

~~~json
{
  "source": "009ad40c",
  "target": "009ad4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad410`](#insn-009ad410)

~~~json
{
  "source": "009ad410",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad414`](#insn-009ad414)

~~~json
{
  "source": "009ad414",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad418`](#insn-009ad418)

~~~json
{
  "source": "009ad418",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad41c`](#insn-009ad41c)

~~~json
{
  "source": "009ad41c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad420`](#insn-009ad420)

~~~json
{
  "source": "009ad420",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad424`](#insn-009ad424)

~~~json
{
  "source": "009ad424",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad430`](#insn-009ad430)

~~~json
{
  "source": "009ad430",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad438`](#insn-009ad438)

~~~json
{
  "source": "009ad438",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad440`](#insn-009ad440)

~~~json
{
  "source": "009ad440",
  "target": "009ad4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad448`](#insn-009ad448)

~~~json
{
  "source": "009ad448",
  "target": "006b8c9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad44c`](#insn-009ad44c)

~~~json
{
  "source": "009ad44c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad454`](#insn-009ad454)

~~~json
{
  "source": "009ad454",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad45c`](#insn-009ad45c)

~~~json
{
  "source": "009ad45c",
  "target": "009ad4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad460`](#insn-009ad460)

~~~json
{
  "source": "009ad460",
  "target": "00440f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad464`](#insn-009ad464)

~~~json
{
  "source": "009ad464",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad46c`](#insn-009ad46c)

~~~json
{
  "source": "009ad46c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad474`](#insn-009ad474)

~~~json
{
  "source": "009ad474",
  "target": "009ad4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad47c`](#insn-009ad47c)

~~~json
{
  "source": "009ad47c",
  "target": "009b0d98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad488`](#insn-009ad488)

~~~json
{
  "source": "009ad488",
  "target": "009b1e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad48c`](#insn-009ad48c)

~~~json
{
  "source": "009ad48c",
  "target": "009ad4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad4c8`](#insn-009ad4c8)

~~~json
{
  "source": "009ad4c8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad4cc`](#insn-009ad4cc)

~~~json
{
  "source": "009ad4cc",
  "target": "009ad4d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad4d0`](#insn-009ad4d0)

~~~json
{
  "source": "009ad4d0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad4d4`](#insn-009ad4d4)

~~~json
{
  "source": "009ad4d4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad4d8`](#insn-009ad4d8)

~~~json
{
  "source": "009ad4d8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad4e0`](#insn-009ad4e0)

~~~json
{
  "source": "009ad4e0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad4e8`](#insn-009ad4e8)

~~~json
{
  "source": "009ad4e8",
  "target": "009ad4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad4f0`](#insn-009ad4f0)

~~~json
{
  "source": "009ad4f0",
  "target": "00c53ffc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad4f4`](#insn-009ad4f4)

~~~json
{
  "source": "009ad4f4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
