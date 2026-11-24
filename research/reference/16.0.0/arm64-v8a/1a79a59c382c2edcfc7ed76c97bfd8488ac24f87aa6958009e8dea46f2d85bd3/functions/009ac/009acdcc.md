# 009acdcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009772ec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/009772ec.md) · 移動量 `+0x35ae0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0047.md#compare-ca461c9b8ceb557f2a76c4f63147e53a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009acf68`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009acf68.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0055.md#compare-3b989a12c3c7543fb8c447347e22e14c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009acdcc",
  "name": "FUN_009acdcc",
  "size": 1284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23a007eee0ea7b9c4eb42853c6722f4063d95b1423b313faa001a7ab37622243",
  "source_text_sha256": "23a007eee0ea7b9c4eb42853c6722f4063d95b1423b313faa001a7ab37622243",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009acdcc",
        "009ad29f"
      ],
      [
        "009ad2d8",
        "009ad307"
      ]
    ],
    "bytes_sha256": "b56b17953b4a814cadccc662c9e157719713beb5fc696b85eb8cc581b4a7b553",
    "instruction_count": 321,
    "instruction_bytes": 1284,
    "body_bytes": 1284,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

- [0075eb40](../0075e/0075eb40.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [006b8c04](../006b8/006b8c04.md)
- [008065d4](../00806/008065d4.md)
- [009b0a4c](../009b0/009b0a4c.md)
- [009b0ba8](../009b0/009b0ba8.md)
- [009b0bbc](../009b0/009b0bbc.md)
- [009b1c40](../009b1/009b1c40.md)
- [009b3fb8](../009b3/009b3fb8.md)
- [009b5af8](../009b5/009b5af8.md)
- [009b5b08](../009b5/009b5b08.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c53b3c](../00c53/00c53b3c.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57c00](../00c57/00c57c00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 8816 bytes

~~~c

void FUN_009acdcc(undefined8 *param_1)

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
  
                    /* try { // try from 009acdec to 00aacdf7 has its CatchHandler @ 009acf20 */
  lVar4 = tpidr_el0;
  local_68 = *(long *)(lVar4 + 0x28);
  puVar1 = (undefined8 *)*param_1;
  puVar3 = (undefined8 *)param_1[1];
  local_90 = (ulong *)0x0;
  local_88 = (ulong *)0x0;
  local_80 = (ulong *)0x0;
  puVar11 = local_90;
                    /* try { // try from 009ace10 to 00aace2b has its CatchHandler @ 009ace9c */
  for (; local_90 = puVar11, puVar1 != puVar3; puVar1 = puVar1 + 2) {
                    /* try { // try from 009ace2c to 00aacf2f has its CatchHandler @ 009acd10 */
    plVar14 = (long *)*puVar1;
    plVar18 = (long *)puVar1[1];
    local_a8 = plVar14;
    local_a0 = plVar18;
    puVar5 = puVar11;
    puVar6 = local_88;
    if (plVar18 != (long *)0x0) {
      FUN_00c538b0(1,plVar18 + 1);
      puVar11 = local_90;
      puVar5 = local_90;
      puVar6 = local_88;
    }
    for (; puVar7 = local_88, __src = local_90, local_90 = puVar5, puVar11 != local_88;
        puVar11 = puVar11 + 1) {
      uVar10 = *puVar11;
      local_88 = puVar6;
      iVar8 = FUN_009b3fb8(plVar14);
      puVar5 = local_88;
      if ((int)uVar10 == iVar8) goto joined_r0x009aceb0;
      puVar5 = local_90;
      puVar6 = local_88;
      local_88 = puVar7;
      local_90 = __src;
    }
    local_88 = puVar6;
    iVar8 = FUN_009b5b08(plVar14);
    puVar5 = local_88;
    if (iVar8 != 0) {
      uVar10 = FUN_009b3fb8(plVar14);
      lVar16 = FUN_009b5af8(plVar14);
                    /* catch() { ... } // from try @ 009ace10 with catch @ 009ace9c */
      uVar10 = uVar10 & 0xffffffff | lVar16 << 0x20;
      if (puVar7 < local_80) {
        *puVar7 = uVar10;
        puVar5 = puVar7 + 1;
      }
      else {
        lVar16 = (long)puVar7 - (long)__src >> 3;
        uVar13 = lVar16 + 1;
        if (uVar13 >> 0x3d != 0) {
          if (*(long *)(lVar4 + 0x28) == local_68) {
            FUN_006b8c04(&local_90);
LAB_009ad25c:
            if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00440e80();
            }
          }
          goto LAB_009ad304;
        }
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
          if (uVar17 >> 0x3d != 0) goto LAB_009ad25c;
                    /* catch() { ... } // from try @ 009acdec with catch @ 009acf20 */
          puVar11 = (ulong *)_Znwm(uVar17 << 3);
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
joined_r0x009aceb0:
    local_88 = puVar5;
    if ((plVar18 != (long *)0x0) &&
       (lVar16 = FUN_00c538e0(0xffffffffffffffff,plVar18 + 1), lVar16 == 0)) {
      (**(code **)(*plVar18 + 0x10))(plVar18);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
    }
    puVar11 = local_90;
  }
  lVar16 = 0;
  if (local_88 != puVar11) {
    lVar16 = LZCOUNT((long)local_88 - (long)puVar11 >> 3) * -2 + 0x7e;
  }
  FUN_009b0bbc(local_88,local_88,puVar11,puVar11,lVar16,1);
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
        uVar15 = FUN_009b0ba8(&local_a8);
        FUN_009b1c40(&local_78);
        if (local_90 != (ulong *)0x0) {
          local_88 = local_90;
          _ZdlPv(local_90);
        }
        if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_00c53b3c(uVar15);
        }
      }
      goto LAB_009ad304;
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
        FUN_00c538b0(1,lVar16 + 8);
      }
      plVar14 = plVar14 + 2;
      plVar12 = plVar12 + 2;
    } while (plVar14 != plVar18);
    plVar14 = (long *)*param_1;
    local_a0 = plVar12;
    for (plVar18 = (long *)param_1[1]; plVar18 != plVar14; plVar18 = plVar18 + -2) {
      plVar12 = (long *)plVar18[-1];
                    /* catch() { ... } // from try @ 009ad080 with catch @ 009ad048 */
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c538e0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
      puVar11 = local_90;
    }
  }
  puVar5 = local_88;
  param_1[1] = plVar14;
  plVar14 = local_a8;
  plVar18 = local_a0;
                    /* try { // try from 009ad078 to 00aad07f has its CatchHandler @ 009ad0cc */
  for (; local_a8 = plVar14, local_a0 = plVar18, puVar11 != puVar5; puVar11 = puVar11 + 1) {
    if (plVar14 != plVar18) {
      uVar10 = *puVar11;
      do {
        pplVar2 = (long **)*plVar14;
        local_70 = (long *)plVar14[1];
                    /* catch() { ... } // from try @ 009ad078 with catch @ 009ad0cc */
        local_78 = pplVar2;
        if (local_70 != (long *)0x0) {
          FUN_00c538b0(1,local_70 + 1);
        }
        iVar8 = FUN_009b3fb8(pplVar2);
        if ((int)uVar10 == iVar8) {
          uVar9 = FUN_009b5af8(local_78);
          uVar13 = FUN_008065d4(4,uVar9);
          if ((uVar13 & 1) != 0) {
            plVar14 = (long *)param_1[1];
            if (plVar14 < (long *)param_1[2]) {
              *plVar14 = (long)local_78;
              plVar14[1] = (long)local_70;
              if (local_70 != (long *)0x0) {
                FUN_00c538b0(1,local_70 + 1);
              }
              plVar14 = plVar14 + 2;
            }
            else {
              plVar14 = (long *)FUN_009b0a4c(param_1,&local_78);
            }
            plVar18 = local_70;
            param_1[1] = plVar14;
                    /* catch() { ... } // from try @ 009ad1c8 with catch @ 009ad184 */
            if ((local_70 != (long *)0x0) &&
               (lVar16 = FUN_00c538e0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
              (**(code **)(*plVar18 + 0x10))(plVar18);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
            }
            break;
          }
        }
        plVar12 = local_70;
        if ((local_70 != (long *)0x0) &&
           (lVar16 = FUN_00c538e0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
          (**(code **)(*plVar12 + 0x10))(plVar12);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
        }
        plVar14 = plVar14 + 2;
      } while (plVar14 != plVar18);
    }
    plVar14 = local_a8;
    plVar18 = local_a0;
  }
                    /* try { // try from 009ad080 to 00aad11b has its CatchHandler @ 009ad048 */
  if (plVar14 != (long *)0x0) {
    for (; plVar18 != plVar14; plVar18 = plVar18 + -2) {
                    /* try { // try from 009ad1c0 to 00aad1c7 has its CatchHandler @ 009ad214 */
      plVar12 = (long *)plVar18[-1];
                    /* try { // try from 009ad1c8 to 00aad263 has its CatchHandler @ 009ad184 */
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c538e0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
    }
    local_a0 = plVar14;
    _ZdlPv(local_a8);
  }
  if (local_90 != (ulong *)0x0) {
    _ZdlPv(local_90);
  }
                    /* catch() { ... } // from try @ 009ad1c0 with catch @ 009ad214 */
  if (*(long *)(lVar4 + 0x28) == local_68) {
    return;
  }
LAB_009ad304:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009acdcc"></a> `009acdcc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-009acdd0"></a> `009acdd0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009acdd4"></a> `009acdd4` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009acdd8"></a> `009acdd8` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009acddc"></a> `009acddc` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009acde0"></a> `009acde0` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009acde4"></a> `009acde4` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009acde8"></a> `009acde8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-009acdec"></a> `009acdec` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009acdf0"></a> `009acdf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009acdf4"></a> `009acdf4` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-009acdf8"></a> `009acdf8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009acdfc"></a> `009acdfc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ace00"></a> `009ace00` | `19 68 40 a9` | ldp x25,x26,[x0] | `FALL_THROUGH`
<a id="insn-009ace04"></a> `009ace04` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ace08"></a> `009ace08` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ace0c"></a> `009ace0c` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009ace10"></a> `009ace10` | `e1 00 00 54` | b.ne 0x009ace2c | `CONDITIONAL_JUMP`
<a id="insn-009ace14"></a> `009ace14` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-009ace18"></a> `009ace18` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-009ace1c"></a> `009ace1c` | `56 00 00 14` | b 0x009acf74 | `UNCONDITIONAL_JUMP`
<a id="insn-009ace20"></a> `009ace20` | `39 43 00 91` | add x25,x25,#0x10 | `FALL_THROUGH`
<a id="insn-009ace24"></a> `009ace24` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009ace28"></a> `009ace28` | `40 0a 00 54` | b.eq 0x009acf70 | `CONDITIONAL_JUMP`
<a id="insn-009ace2c"></a> `009ace2c` | `36 53 40 a9` | ldp x22,x20,[x25] | `FALL_THROUGH`
<a id="insn-009ace30"></a> `009ace30` | `f6 d3 00 a9` | stp x22,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ace34"></a> `009ace34` | `94 00 00 b4` | cbz x20,0x009ace44 | `CONDITIONAL_JUMP`
<a id="insn-009ace38"></a> `009ace38` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009ace3c"></a> `009ace3c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ace40"></a> `009ace40` | `9c 9a 0a 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-009ace44"></a> `009ace44` | `f5 63 42 a9` | ldp x21,x24,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ace48"></a> `009ace48` | `bf 02 18 eb` | cmp x21,x24 | `FALL_THROUGH`
<a id="insn-009ace4c"></a> `009ace4c` | `f7 03 15 aa` | mov x23,x21 | `FALL_THROUGH`
<a id="insn-009ace50"></a> `009ace50` | `20 01 00 54` | b.eq 0x009ace74 | `CONDITIONAL_JUMP`
<a id="insn-009ace54"></a> `009ace54` | `fb 02 40 b9` | ldr w27,[x23] | `FALL_THROUGH`
<a id="insn-009ace58"></a> `009ace58` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ace5c"></a> `009ace5c` | `57 1c 00 94` | bl 0x009b3fb8 | `UNCONDITIONAL_CALL`
<a id="insn-009ace60"></a> `009ace60` | `7f 03 00 6b` | cmp w27,w0 | `FALL_THROUGH`
<a id="insn-009ace64"></a> `009ace64` | `60 02 00 54` | b.eq 0x009aceb0 | `CONDITIONAL_JUMP`
<a id="insn-009ace68"></a> `009ace68` | `f7 22 00 91` | add x23,x23,#0x8 | `FALL_THROUGH`
<a id="insn-009ace6c"></a> `009ace6c` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009ace70"></a> `009ace70` | `21 ff ff 54` | b.ne 0x009ace54 | `CONDITIONAL_JUMP`
<a id="insn-009ace74"></a> `009ace74` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ace78"></a> `009ace78` | `24 23 00 94` | bl 0x009b5b08 | `UNCONDITIONAL_CALL`
<a id="insn-009ace7c"></a> `009ace7c` | `a0 01 00 34` | cbz w0,0x009aceb0 | `CONDITIONAL_JUMP`
<a id="insn-009ace80"></a> `009ace80` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ace84"></a> `009ace84` | `4d 1c 00 94` | bl 0x009b3fb8 | `UNCONDITIONAL_CALL`
<a id="insn-009ace88"></a> `009ace88` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009ace8c"></a> `009ace8c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ace90"></a> `009ace90` | `1a 23 00 94` | bl 0x009b5af8 | `UNCONDITIONAL_CALL`
<a id="insn-009ace94"></a> `009ace94` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ace98"></a> `009ace98` | `e9 03 17 2a` | mov w9,w23 | `FALL_THROUGH`
<a id="insn-009ace9c"></a> `009ace9c` | `3b 81 00 aa` | orr x27,x9,x0, LSL #0x20 | `FALL_THROUGH`
<a id="insn-009acea0"></a> `009acea0` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-009acea4"></a> `009acea4` | `e2 01 00 54` | b.cs 0x009acee0 | `CONDITIONAL_JUMP`
<a id="insn-009acea8"></a> `009acea8` | `1b 87 00 f8` | str x27,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-009aceac"></a> `009aceac` | `f8 17 00 f9` | str x24,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009aceb0"></a> `009aceb0` | `94 fb ff b4` | cbz x20,0x009ace20 | `CONDITIONAL_JUMP`
<a id="insn-009aceb4"></a> `009aceb4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009aceb8"></a> `009aceb8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009acebc"></a> `009acebc` | `89 9a 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009acec0"></a> `009acec0` | `00 fb ff b5` | cbnz x0,0x009ace20 | `CONDITIONAL_JUMP`
<a id="insn-009acec4"></a> `009acec4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009acec8"></a> `009acec8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009acecc"></a> `009acecc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009aced0"></a> `009aced0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009aced4"></a> `009aced4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009aced8"></a> `009aced8` | `ea aa 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009acedc"></a> `009acedc` | `d1 ff ff 17` | b 0x009ace20 | `UNCONDITIONAL_JUMP`
<a id="insn-009acee0"></a> `009acee0` | `16 03 15 cb` | sub x22,x24,x21 | `FALL_THROUGH`
<a id="insn-009acee4"></a> `009acee4` | `d8 fe 43 93` | asr x24,x22,#0x3 | `FALL_THROUGH`
<a id="insn-009acee8"></a> `009acee8` | `09 07 00 91` | add x9,x24,#0x1 | `FALL_THROUGH`
<a id="insn-009aceec"></a> `009aceec` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-009acef0"></a> `009acef0` | `8a 1a 00 b5` | cbnz x10,0x009ad240 | `CONDITIONAL_JUMP`
<a id="insn-009acef4"></a> `009acef4` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-009acef8"></a> `009acef8` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-009acefc"></a> `009acefc` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-009acf00"></a> `009acf00` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-009acf04"></a> `009acf04` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-009acf08"></a> `009acf08` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-009acf0c"></a> `009acf0c` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-009acf10"></a> `009acf10` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-009acf14"></a> `009acf14` | `fc 00 00 b4` | cbz x28,0x009acf30 | `CONDITIONAL_JUMP`
<a id="insn-009acf18"></a> `009acf18` | `88 ff 7d d3` | lsr x8,x28,#0x3d | `FALL_THROUGH`
<a id="insn-009acf1c"></a> `009acf1c` | `08 1a 00 b5` | cbnz x8,0x009ad25c | `CONDITIONAL_JUMP`
<a id="insn-009acf20"></a> `009acf20` | `80 f3 7d d3` | lsl x0,x28,#0x3 | `FALL_THROUGH`
<a id="insn-009acf24"></a> `009acf24` | `db aa 0a 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-009acf28"></a> `009acf28` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-009acf2c"></a> `009acf2c` | `02 00 00 14` | b 0x009acf34 | `UNCONDITIONAL_JUMP`
<a id="insn-009acf30"></a> `009acf30` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-009acf34"></a> `009acf34` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-009acf38"></a> `009acf38` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-009acf3c"></a> `009acf3c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009acf40"></a> `009acf40` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-009acf44"></a> `009acf44` | `fc 0e 1c 8b` | add x28,x23,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-009acf48"></a> `009acf48` | `1b 87 00 f8` | str x27,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-009acf4c"></a> `009acf4c` | `2d ab 0a 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-009acf50"></a> `009acf50` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009acf54"></a> `009acf54` | `fc 1b 00 f9` | str x28,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009acf58"></a> `009acf58` | `75 00 00 b4` | cbz x21,0x009acf64 | `CONDITIONAL_JUMP`
<a id="insn-009acf5c"></a> `009acf5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009acf60"></a> `009acf60` | `d4 aa 0a 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-009acf64"></a> `009acf64` | `f8 17 00 f9` | str x24,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009acf68"></a> `009acf68` | `74 fa ff b5` | cbnz x20,0x009aceb4 | `CONDITIONAL_JUMP`
<a id="insn-009acf6c"></a> `009acf6c` | `ad ff ff 17` | b 0x009ace20 | `UNCONDITIONAL_JUMP`
<a id="insn-009acf70"></a> `009acf70` | `f4 03 42 a9` | ldp x20,x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009acf74"></a> `009acf74` | `08 00 14 eb` | subs x8,x0,x20 | `FALL_THROUGH`
<a id="insn-009acf78"></a> `009acf78` | `c9 0f 80 52` | mov w9,#0x7e | `FALL_THROUGH`
<a id="insn-009acf7c"></a> `009acf7c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-009acf80"></a> `009acf80` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-009acf84"></a> `009acf84` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-009acf88"></a> `009acf88` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-009acf8c"></a> `009acf8c` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-009acf90"></a> `009acf90` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-009acf94"></a> `009acf94` | `08 11 c0 da` | clz x8,x8 | `FALL_THROUGH`
<a id="insn-009acf98"></a> `009acf98` | `28 05 08 cb` | sub x8,x9,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-009acf9c"></a> `009acf9c` | `e4 03 88 9a` | csel x4,xzr,x8,eq | `FALL_THROUGH`
<a id="insn-009acfa0"></a> `009acfa0` | `07 0f 00 94` | bl 0x009b0bbc | `UNCONDITIONAL_CALL`
<a id="insn-009acfa4"></a> `009acfa4` | `77 62 40 a9` | ldp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-009acfa8"></a> `009acfa8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009acfac"></a> `009acfac` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009acfb0"></a> `009acfb0` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009acfb4"></a> `009acfb4` | `16 03 17 eb` | subs x22,x24,x23 | `FALL_THROUGH`
<a id="insn-009acfb8"></a> `009acfb8` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009acfbc"></a> `009acfbc` | `bf 03 1f 38` | sturb wzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009acfc0"></a> `009acfc0` | `80 05 00 54` | b.eq 0x009ad070 | `CONDITIONAL_JUMP`
<a id="insn-009acfc4"></a> `009acfc4` | `96 15 f8 b7` | tbnz x22,#0x3f,0x009ad274 | `CONDITIONAL_JUMP`
<a id="insn-009acfc8"></a> `009acfc8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009acfcc"></a> `009acfcc` | `b1 aa 0a 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-009acfd0"></a> `009acfd0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009acfd4"></a> `009acfd4` | `08 00 16 8b` | add x8,x0,x22 | `FALL_THROUGH`
<a id="insn-009acfd8"></a> `009acfd8` | `e0 83 00 a9` | stp x0,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009acfdc"></a> `009acfdc` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009acfe0"></a> `009acfe0` | `05 00 00 14` | b 0x009acff4 | `UNCONDITIONAL_JUMP`
<a id="insn-009acfe4"></a> `009acfe4` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009acfe8"></a> `009acfe8` | `b5 42 00 91` | add x21,x21,#0x10 | `FALL_THROUGH`
<a id="insn-009acfec"></a> `009acfec` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009acff0"></a> `009acff0` | `40 01 00 54` | b.eq 0x009ad018 | `CONDITIONAL_JUMP`
<a id="insn-009acff4"></a> `009acff4` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-009acff8"></a> `009acff8` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-009acffc"></a> `009acffc` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-009ad000"></a> `009ad000` | `a8 06 00 f9` | str x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-009ad004"></a> `009ad004` | `08 ff ff b4` | cbz x8,0x009acfe4 | `CONDITIONAL_JUMP`
<a id="insn-009ad008"></a> `009ad008` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-009ad00c"></a> `009ad00c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ad010"></a> `009ad010` | `28 9a 0a 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad014"></a> `009ad014` | `f4 ff ff 17` | b 0x009acfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad018"></a> `009ad018` | `77 5a 40 a9` | ldp x23,x22,[x19] | `FALL_THROUGH`
<a id="insn-009ad01c"></a> `009ad01c` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ad020"></a> `009ad020` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-009ad024"></a> `009ad024` | `a1 00 00 54` | b.ne 0x009ad038 | `CONDITIONAL_JUMP`
<a id="insn-009ad028"></a> `009ad028` | `12 00 00 14` | b 0x009ad070 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad02c"></a> `009ad02c` | `d6 42 00 d1` | sub x22,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009ad030"></a> `009ad030` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-009ad034"></a> `009ad034` | `c0 01 00 54` | b.eq 0x009ad06c | `CONDITIONAL_JUMP`
<a id="insn-009ad038"></a> `009ad038` | `d4 82 5f f8` | ldur x20,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad03c"></a> `009ad03c` | `94 ff ff b4` | cbz x20,0x009ad02c | `CONDITIONAL_JUMP`
<a id="insn-009ad040"></a> `009ad040` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009ad044"></a> `009ad044` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad048"></a> `009ad048` | `26 9a 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad04c"></a> `009ad04c` | `00 ff ff b5` | cbnz x0,0x009ad02c | `CONDITIONAL_JUMP`
<a id="insn-009ad050"></a> `009ad050` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009ad054"></a> `009ad054` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad058"></a> `009ad058` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad05c"></a> `009ad05c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad060"></a> `009ad060` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad064"></a> `009ad064` | `87 aa 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad068"></a> `009ad068` | `f1 ff ff 17` | b 0x009ad02c | `UNCONDITIONAL_JUMP`
<a id="insn-009ad06c"></a> `009ad06c` | `f4 13 40 f9` | ldr x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad070"></a> `009ad070` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009ad074"></a> `009ad074` | `77 06 00 f9` | str x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-009ad078"></a> `009ad078` | `9f 02 16 eb` | cmp x20,x22 | `FALL_THROUGH`
<a id="insn-009ad07c"></a> `009ad07c` | `61 01 00 54` | b.ne 0x009ad0a8 | `CONDITIONAL_JUMP`
<a id="insn-009ad080"></a> `009ad080` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad084"></a> `009ad084` | `f4 0b 00 b4` | cbz x20,0x009ad200 | `CONDITIONAL_JUMP`
<a id="insn-009ad088"></a> `009ad088` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ad08c"></a> `009ad08c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009ad090"></a> `009ad090` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-009ad094"></a> `009ad094` | `61 09 00 54` | b.ne 0x009ad1c0 | `CONDITIONAL_JUMP`
<a id="insn-009ad098"></a> `009ad098` | `58 00 00 14` | b 0x009ad1f8 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad09c"></a> `009ad09c` | `94 22 00 91` | add x20,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009ad0a0"></a> `009ad0a0` | `9f 02 16 eb` | cmp x20,x22 | `FALL_THROUGH`
<a id="insn-009ad0a4"></a> `009ad0a4` | `e0 fe ff 54` | b.eq 0x009ad080 | `CONDITIONAL_JUMP`
<a id="insn-009ad0a8"></a> `009ad0a8` | `f7 e3 40 a9` | ldp x23,x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad0ac"></a> `009ad0ac` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009ad0b0"></a> `009ad0b0` | `60 ff ff 54` | b.eq 0x009ad09c | `CONDITIONAL_JUMP`
<a id="insn-009ad0b4"></a> `009ad0b4` | `99 02 40 b9` | ldr w25,[x20] | `FALL_THROUGH`
<a id="insn-009ad0b8"></a> `009ad0b8` | `04 00 00 14` | b 0x009ad0c8 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad0bc"></a> `009ad0bc` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009ad0c0"></a> `009ad0c0` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-009ad0c4"></a> `009ad0c4` | `c0 fe ff 54` | b.eq 0x009ad09c | `CONDITIONAL_JUMP`
<a id="insn-009ad0c8"></a> `009ad0c8` | `f5 22 40 a9` | ldp x21,x8,[x23] | `FALL_THROUGH`
<a id="insn-009ad0cc"></a> `009ad0cc` | `b5 a3 3e a9` | stp x21,x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009ad0d0"></a> `009ad0d0` | `88 00 00 b4` | cbz x8,0x009ad0e0 | `CONDITIONAL_JUMP`
<a id="insn-009ad0d4"></a> `009ad0d4` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-009ad0d8"></a> `009ad0d8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ad0dc"></a> `009ad0dc` | `f5 99 0a 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad0e0"></a> `009ad0e0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad0e4"></a> `009ad0e4` | `b5 1b 00 94` | bl 0x009b3fb8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad0e8"></a> `009ad0e8` | `3f 03 00 6b` | cmp w25,w0 | `FALL_THROUGH`
<a id="insn-009ad0ec"></a> `009ad0ec` | `e1 00 00 54` | b.ne 0x009ad108 | `CONDITIONAL_JUMP`
<a id="insn-009ad0f0"></a> `009ad0f0` | `a0 83 5e f8` | ldur x0,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009ad0f4"></a> `009ad0f4` | `81 22 00 94` | bl 0x009b5af8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad0f8"></a> `009ad0f8` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-009ad0fc"></a> `009ad0fc` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-009ad100"></a> `009ad100` | `35 65 f9 97` | bl 0x008065d4 | `UNCONDITIONAL_CALL`
<a id="insn-009ad104"></a> `009ad104` | `c0 01 00 37` | tbnz w0,#0x0,0x009ad13c | `CONDITIONAL_JUMP`
<a id="insn-009ad108"></a> `009ad108` | `b5 03 5f f8` | ldur x21,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009ad10c"></a> `009ad10c` | `95 fd ff b4` | cbz x21,0x009ad0bc | `CONDITIONAL_JUMP`
<a id="insn-009ad110"></a> `009ad110` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009ad114"></a> `009ad114` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad118"></a> `009ad118` | `f2 99 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad11c"></a> `009ad11c` | `00 fd ff b5` | cbnz x0,0x009ad0bc | `CONDITIONAL_JUMP`
<a id="insn-009ad120"></a> `009ad120` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009ad124"></a> `009ad124` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad128"></a> `009ad128` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad12c"></a> `009ad12c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad130"></a> `009ad130` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad134"></a> `009ad134` | `53 aa 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad138"></a> `009ad138` | `e1 ff ff 17` | b 0x009ad0bc | `UNCONDITIONAL_JUMP`
<a id="insn-009ad13c"></a> `009ad13c` | `75 a2 40 a9` | ldp x21,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-009ad140"></a> `009ad140` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-009ad144"></a> `009ad144` | `62 01 00 54` | b.cs 0x009ad170 | `CONDITIONAL_JUMP`
<a id="insn-009ad148"></a> `009ad148` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-009ad14c"></a> `009ad14c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-009ad150"></a> `009ad150` | `a8 03 5f f8` | ldur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009ad154"></a> `009ad154` | `a8 06 00 f9` | str x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-009ad158"></a> `009ad158` | `88 00 00 b4` | cbz x8,0x009ad168 | `CONDITIONAL_JUMP`
<a id="insn-009ad15c"></a> `009ad15c` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-009ad160"></a> `009ad160` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ad164"></a> `009ad164` | `d3 99 0a 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad168"></a> `009ad168` | `a0 42 00 91` | add x0,x21,#0x10 | `FALL_THROUGH`
<a id="insn-009ad16c"></a> `009ad16c` | `04 00 00 14` | b 0x009ad17c | `UNCONDITIONAL_JUMP`
<a id="insn-009ad170"></a> `009ad170` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-009ad174"></a> `009ad174` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad178"></a> `009ad178` | `35 0e 00 94` | bl 0x009b0a4c | `UNCONDITIONAL_CALL`
<a id="insn-009ad17c"></a> `009ad17c` | `b5 03 5f f8` | ldur x21,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009ad180"></a> `009ad180` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-009ad184"></a> `009ad184` | `d5 f8 ff b4` | cbz x21,0x009ad09c | `CONDITIONAL_JUMP`
<a id="insn-009ad188"></a> `009ad188` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009ad18c"></a> `009ad18c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad190"></a> `009ad190` | `d4 99 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad194"></a> `009ad194` | `40 f8 ff b5` | cbnz x0,0x009ad09c | `CONDITIONAL_JUMP`
<a id="insn-009ad198"></a> `009ad198` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009ad19c"></a> `009ad19c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad1a0"></a> `009ad1a0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad1a4"></a> `009ad1a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad1a8"></a> `009ad1a8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ad1ac"></a> `009ad1ac` | `35 aa 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad1b0"></a> `009ad1b0` | `bb ff ff 17` | b 0x009ad09c | `UNCONDITIONAL_JUMP`
<a id="insn-009ad1b4"></a> `009ad1b4` | `b5 42 00 d1` | sub x21,x21,#0x10 | `FALL_THROUGH`
<a id="insn-009ad1b8"></a> `009ad1b8` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-009ad1bc"></a> `009ad1bc` | `c0 01 00 54` | b.eq 0x009ad1f4 | `CONDITIONAL_JUMP`
<a id="insn-009ad1c0"></a> `009ad1c0` | `b3 82 5f f8` | ldur x19,[x21, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad1c4"></a> `009ad1c4` | `93 ff ff b4` | cbz x19,0x009ad1b4 | `CONDITIONAL_JUMP`
<a id="insn-009ad1c8"></a> `009ad1c8` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-009ad1cc"></a> `009ad1cc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ad1d0"></a> `009ad1d0` | `c4 99 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad1d4"></a> `009ad1d4` | `00 ff ff b5` | cbnz x0,0x009ad1b4 | `CONDITIONAL_JUMP`
<a id="insn-009ad1d8"></a> `009ad1d8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-009ad1dc"></a> `009ad1dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad1e0"></a> `009ad1e0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ad1e4"></a> `009ad1e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ad1e8"></a> `009ad1e8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad1ec"></a> `009ad1ec` | `25 aa 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009ad1f0"></a> `009ad1f0` | `f1 ff ff 17` | b 0x009ad1b4 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad1f4"></a> `009ad1f4` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ad1f8"></a> `009ad1f8` | `f4 0b 00 f9` | str x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ad1fc"></a> `009ad1fc` | `2d aa 0a 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad200"></a> `009ad200` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad204"></a> `009ad204` | `40 00 00 b4` | cbz x0,0x009ad20c | `CONDITIONAL_JUMP`
<a id="insn-009ad208"></a> `009ad208` | `2a aa 0a 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad20c"></a> `009ad20c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad210"></a> `009ad210` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad214"></a> `009ad214` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad218"></a> `009ad218` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad21c"></a> `009ad21c` | `41 07 00 54` | b.ne 0x009ad304 | `CONDITIONAL_JUMP`
<a id="insn-009ad220"></a> `009ad220` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009ad224"></a> `009ad224` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009ad228"></a> `009ad228` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009ad22c"></a> `009ad22c` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009ad230"></a> `009ad230` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009ad234"></a> `009ad234` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009ad238"></a> `009ad238` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-009ad23c"></a> `009ad23c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009ad240"></a> `009ad240` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad244"></a> `009ad244` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad248"></a> `009ad248` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad24c"></a> `009ad24c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad250"></a> `009ad250` | `a1 05 00 54` | b.ne 0x009ad304 | `CONDITIONAL_JUMP`
<a id="insn-009ad254"></a> `009ad254` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009ad258"></a> `009ad258` | `6b 2e f4 97` | bl 0x006b8c04 | `UNCONDITIONAL_CALL`
<a id="insn-009ad25c"></a> `009ad25c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad260"></a> `009ad260` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad264"></a> `009ad264` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad268"></a> `009ad268` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad26c"></a> `009ad26c` | `c1 04 00 54` | b.ne 0x009ad304 | `CONDITIONAL_JUMP`
<a id="insn-009ad270"></a> `009ad270` | `04 4f ea 97` | bl 0x00440e80 | `CALL_TERMINATOR`
<a id="insn-009ad274"></a> `009ad274` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad278"></a> `009ad278` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad27c"></a> `009ad27c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad280"></a> `009ad280` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad284"></a> `009ad284` | `01 04 00 54` | b.ne 0x009ad304 | `CONDITIONAL_JUMP`
<a id="insn-009ad288"></a> `009ad288` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009ad28c"></a> `009ad28c` | `47 0e 00 94` | bl 0x009b0ba8 | `UNCONDITIONAL_CALL`
<a id="insn-009ad290"></a> `009ad290` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009ad294"></a> `009ad294` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-009ad298"></a> `009ad298` | `6a 12 00 94` | bl 0x009b1c40 | `UNCONDITIONAL_CALL`
<a id="insn-009ad29c"></a> `009ad29c` | `0f 00 00 14` | b 0x009ad2d8 | `UNCONDITIONAL_JUMP`
<a id="insn-009ad2d8"></a> `009ad2d8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ad2dc"></a> `009ad2dc` | `60 00 00 b4` | cbz x0,0x009ad2e8 | `CONDITIONAL_JUMP`
<a id="insn-009ad2e0"></a> `009ad2e0` | `e0 17 00 f9` | str x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009ad2e4"></a> `009ad2e4` | `f3 a9 0a 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-009ad2e8"></a> `009ad2e8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-009ad2ec"></a> `009ad2ec` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ad2f0"></a> `009ad2f0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ad2f4"></a> `009ad2f4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ad2f8"></a> `009ad2f8` | `61 00 00 54` | b.ne 0x009ad304 | `CONDITIONAL_JUMP`
<a id="insn-009ad2fc"></a> `009ad2fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ad300"></a> `009ad300` | `0f 9a 0a 94` | bl 0x00c53b3c | `CALL_TERMINATOR`
<a id="insn-009ad304"></a> `009ad304` | `f7 a9 0a 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009acdcc`](#insn-009acdcc) 範囲 `[['009acdcc', '009acdeb']]`
  - `FALL_THROUGH` [`009acde8`](#insn-009acde8) → [`009acdec`](#insn-009acdec)
- ブロック [`009acdec`](#insn-009acdec) 範囲 `[['009acdec', '009ace0f']]`
  - `FALL_THROUGH` [`009ace0c`](#insn-009ace0c) → [`009ace10`](#insn-009ace10)
- ブロック [`009ace10`](#insn-009ace10) 範囲 `[['009ace10', '009ace13']]`
  - `CONDITIONAL_JUMP` [`009ace10`](#insn-009ace10) → [`009ace2c`](#insn-009ace2c)
  - `FALL_THROUGH` [`009ace10`](#insn-009ace10) → [`009ace14`](#insn-009ace14)
- ブロック [`009ace14`](#insn-009ace14) 範囲 `[['009ace14', '009ace1f']]`
  - `UNCONDITIONAL_JUMP` [`009ace1c`](#insn-009ace1c) → [`009acf74`](#insn-009acf74)
- ブロック [`009ace20`](#insn-009ace20) 範囲 `[['009ace20', '009ace2b']]`
  - `CONDITIONAL_JUMP` [`009ace28`](#insn-009ace28) → [`009acf70`](#insn-009acf70)
  - `FALL_THROUGH` [`009ace28`](#insn-009ace28) → [`009ace2c`](#insn-009ace2c)
- ブロック [`009ace2c`](#insn-009ace2c) 範囲 `[['009ace2c', '009ace37']]`
  - `CONDITIONAL_JUMP` [`009ace34`](#insn-009ace34) → [`009ace44`](#insn-009ace44)
  - `FALL_THROUGH` [`009ace34`](#insn-009ace34) → [`009ace38`](#insn-009ace38)
- ブロック [`009ace38`](#insn-009ace38) 範囲 `[['009ace38', '009ace43']]`
  - `FALL_THROUGH` [`009ace40`](#insn-009ace40) → [`009ace44`](#insn-009ace44)
- ブロック [`009ace44`](#insn-009ace44) 範囲 `[['009ace44', '009ace53']]`
  - `CONDITIONAL_JUMP` [`009ace50`](#insn-009ace50) → [`009ace74`](#insn-009ace74)
  - `FALL_THROUGH` [`009ace50`](#insn-009ace50) → [`009ace54`](#insn-009ace54)
- ブロック [`009ace54`](#insn-009ace54) 範囲 `[['009ace54', '009ace67']]`
  - `CONDITIONAL_JUMP` [`009ace64`](#insn-009ace64) → [`009aceb0`](#insn-009aceb0)
  - `FALL_THROUGH` [`009ace64`](#insn-009ace64) → [`009ace68`](#insn-009ace68)
- ブロック [`009ace68`](#insn-009ace68) 範囲 `[['009ace68', '009ace73']]`
  - `CONDITIONAL_JUMP` [`009ace70`](#insn-009ace70) → [`009ace54`](#insn-009ace54)
  - `FALL_THROUGH` [`009ace70`](#insn-009ace70) → [`009ace74`](#insn-009ace74)
- ブロック [`009ace74`](#insn-009ace74) 範囲 `[['009ace74', '009ace7f']]`
  - `CONDITIONAL_JUMP` [`009ace7c`](#insn-009ace7c) → [`009aceb0`](#insn-009aceb0)
  - `FALL_THROUGH` [`009ace7c`](#insn-009ace7c) → [`009ace80`](#insn-009ace80)
- ブロック [`009ace80`](#insn-009ace80) 範囲 `[['009ace80', '009ace9b']]`
  - `FALL_THROUGH` [`009ace98`](#insn-009ace98) → [`009ace9c`](#insn-009ace9c)
- ブロック [`009ace9c`](#insn-009ace9c) 範囲 `[['009ace9c', '009acea7']]`
  - `CONDITIONAL_JUMP` [`009acea4`](#insn-009acea4) → [`009acee0`](#insn-009acee0)
  - `FALL_THROUGH` [`009acea4`](#insn-009acea4) → [`009acea8`](#insn-009acea8)
- ブロック [`009acea8`](#insn-009acea8) 範囲 `[['009acea8', '009aceaf']]`
  - `FALL_THROUGH` [`009aceac`](#insn-009aceac) → [`009aceb0`](#insn-009aceb0)
- ブロック [`009aceb0`](#insn-009aceb0) 範囲 `[['009aceb0', '009aceb3']]`
  - `CONDITIONAL_JUMP` [`009aceb0`](#insn-009aceb0) → [`009ace20`](#insn-009ace20)
  - `FALL_THROUGH` [`009aceb0`](#insn-009aceb0) → [`009aceb4`](#insn-009aceb4)
- ブロック [`009aceb4`](#insn-009aceb4) 範囲 `[['009aceb4', '009acec3']]`
  - `CONDITIONAL_JUMP` [`009acec0`](#insn-009acec0) → [`009ace20`](#insn-009ace20)
  - `FALL_THROUGH` [`009acec0`](#insn-009acec0) → [`009acec4`](#insn-009acec4)
- ブロック [`009acec4`](#insn-009acec4) 範囲 `[['009acec4', '009acedf']]`
  - `UNCONDITIONAL_JUMP` [`009acedc`](#insn-009acedc) → [`009ace20`](#insn-009ace20)
- ブロック [`009acee0`](#insn-009acee0) 範囲 `[['009acee0', '009acef3']]`
  - `CONDITIONAL_JUMP` [`009acef0`](#insn-009acef0) → [`009ad240`](#insn-009ad240)
  - `FALL_THROUGH` [`009acef0`](#insn-009acef0) → [`009acef4`](#insn-009acef4)
- ブロック [`009acef4`](#insn-009acef4) 範囲 `[['009acef4', '009acf17']]`
  - `CONDITIONAL_JUMP` [`009acf14`](#insn-009acf14) → [`009acf30`](#insn-009acf30)
  - `FALL_THROUGH` [`009acf14`](#insn-009acf14) → [`009acf18`](#insn-009acf18)
- ブロック [`009acf18`](#insn-009acf18) 範囲 `[['009acf18', '009acf1f']]`
  - `CONDITIONAL_JUMP` [`009acf1c`](#insn-009acf1c) → [`009ad25c`](#insn-009ad25c)
  - `FALL_THROUGH` [`009acf1c`](#insn-009acf1c) → [`009acf20`](#insn-009acf20)
- ブロック [`009acf20`](#insn-009acf20) 範囲 `[['009acf20', '009acf2f']]`
  - `UNCONDITIONAL_JUMP` [`009acf2c`](#insn-009acf2c) → [`009acf34`](#insn-009acf34)
- ブロック [`009acf30`](#insn-009acf30) 範囲 `[['009acf30', '009acf33']]`
  - `FALL_THROUGH` [`009acf30`](#insn-009acf30) → [`009acf34`](#insn-009acf34)
- ブロック [`009acf34`](#insn-009acf34) 範囲 `[['009acf34', '009acf5b']]`
  - `CONDITIONAL_JUMP` [`009acf58`](#insn-009acf58) → [`009acf64`](#insn-009acf64)
  - `FALL_THROUGH` [`009acf58`](#insn-009acf58) → [`009acf5c`](#insn-009acf5c)
- ブロック [`009acf5c`](#insn-009acf5c) 範囲 `[['009acf5c', '009acf63']]`
  - `FALL_THROUGH` [`009acf60`](#insn-009acf60) → [`009acf64`](#insn-009acf64)
- ブロック [`009acf64`](#insn-009acf64) 範囲 `[['009acf64', '009acf6b']]`
  - `CONDITIONAL_JUMP` [`009acf68`](#insn-009acf68) → [`009aceb4`](#insn-009aceb4)
  - `FALL_THROUGH` [`009acf68`](#insn-009acf68) → [`009acf6c`](#insn-009acf6c)
- ブロック [`009acf6c`](#insn-009acf6c) 範囲 `[['009acf6c', '009acf6f']]`
  - `UNCONDITIONAL_JUMP` [`009acf6c`](#insn-009acf6c) → [`009ace20`](#insn-009ace20)
- ブロック [`009acf70`](#insn-009acf70) 範囲 `[['009acf70', '009acf73']]`
  - `FALL_THROUGH` [`009acf70`](#insn-009acf70) → [`009acf74`](#insn-009acf74)
- ブロック [`009acf74`](#insn-009acf74) 範囲 `[['009acf74', '009acfc3']]`
  - `CONDITIONAL_JUMP` [`009acfc0`](#insn-009acfc0) → [`009ad070`](#insn-009ad070)
  - `FALL_THROUGH` [`009acfc0`](#insn-009acfc0) → [`009acfc4`](#insn-009acfc4)
- ブロック [`009acfc4`](#insn-009acfc4) 範囲 `[['009acfc4', '009acfc7']]`
  - `CONDITIONAL_JUMP` [`009acfc4`](#insn-009acfc4) → [`009ad274`](#insn-009ad274)
  - `FALL_THROUGH` [`009acfc4`](#insn-009acfc4) → [`009acfc8`](#insn-009acfc8)
- ブロック [`009acfc8`](#insn-009acfc8) 範囲 `[['009acfc8', '009acfe3']]`
  - `UNCONDITIONAL_JUMP` [`009acfe0`](#insn-009acfe0) → [`009acff4`](#insn-009acff4)
- ブロック [`009acfe4`](#insn-009acfe4) 範囲 `[['009acfe4', '009acff3']]`
  - `CONDITIONAL_JUMP` [`009acff0`](#insn-009acff0) → [`009ad018`](#insn-009ad018)
  - `FALL_THROUGH` [`009acff0`](#insn-009acff0) → [`009acff4`](#insn-009acff4)
- ブロック [`009acff4`](#insn-009acff4) 範囲 `[['009acff4', '009ad007']]`
  - `CONDITIONAL_JUMP` [`009ad004`](#insn-009ad004) → [`009acfe4`](#insn-009acfe4)
  - `FALL_THROUGH` [`009ad004`](#insn-009ad004) → [`009ad008`](#insn-009ad008)
- ブロック [`009ad008`](#insn-009ad008) 範囲 `[['009ad008', '009ad017']]`
  - `UNCONDITIONAL_JUMP` [`009ad014`](#insn-009ad014) → [`009acfe4`](#insn-009acfe4)
- ブロック [`009ad018`](#insn-009ad018) 範囲 `[['009ad018', '009ad027']]`
  - `CONDITIONAL_JUMP` [`009ad024`](#insn-009ad024) → [`009ad038`](#insn-009ad038)
  - `FALL_THROUGH` [`009ad024`](#insn-009ad024) → [`009ad028`](#insn-009ad028)
- ブロック [`009ad028`](#insn-009ad028) 範囲 `[['009ad028', '009ad02b']]`
  - `UNCONDITIONAL_JUMP` [`009ad028`](#insn-009ad028) → [`009ad070`](#insn-009ad070)
- ブロック [`009ad02c`](#insn-009ad02c) 範囲 `[['009ad02c', '009ad037']]`
  - `CONDITIONAL_JUMP` [`009ad034`](#insn-009ad034) → [`009ad06c`](#insn-009ad06c)
  - `FALL_THROUGH` [`009ad034`](#insn-009ad034) → [`009ad038`](#insn-009ad038)
- ブロック [`009ad038`](#insn-009ad038) 範囲 `[['009ad038', '009ad03f']]`
  - `CONDITIONAL_JUMP` [`009ad03c`](#insn-009ad03c) → [`009ad02c`](#insn-009ad02c)
  - `FALL_THROUGH` [`009ad03c`](#insn-009ad03c) → [`009ad040`](#insn-009ad040)
- ブロック [`009ad040`](#insn-009ad040) 範囲 `[['009ad040', '009ad047']]`
  - `FALL_THROUGH` [`009ad044`](#insn-009ad044) → [`009ad048`](#insn-009ad048)
- ブロック [`009ad048`](#insn-009ad048) 範囲 `[['009ad048', '009ad04f']]`
  - `CONDITIONAL_JUMP` [`009ad04c`](#insn-009ad04c) → [`009ad02c`](#insn-009ad02c)
  - `FALL_THROUGH` [`009ad04c`](#insn-009ad04c) → [`009ad050`](#insn-009ad050)
- ブロック [`009ad050`](#insn-009ad050) 範囲 `[['009ad050', '009ad06b']]`
  - `UNCONDITIONAL_JUMP` [`009ad068`](#insn-009ad068) → [`009ad02c`](#insn-009ad02c)
- ブロック [`009ad06c`](#insn-009ad06c) 範囲 `[['009ad06c', '009ad06f']]`
  - `FALL_THROUGH` [`009ad06c`](#insn-009ad06c) → [`009ad070`](#insn-009ad070)
- ブロック [`009ad070`](#insn-009ad070) 範囲 `[['009ad070', '009ad077']]`
  - `FALL_THROUGH` [`009ad074`](#insn-009ad074) → [`009ad078`](#insn-009ad078)
- ブロック [`009ad078`](#insn-009ad078) 範囲 `[['009ad078', '009ad07f']]`
  - `CONDITIONAL_JUMP` [`009ad07c`](#insn-009ad07c) → [`009ad0a8`](#insn-009ad0a8)
  - `FALL_THROUGH` [`009ad07c`](#insn-009ad07c) → [`009ad080`](#insn-009ad080)
- ブロック [`009ad080`](#insn-009ad080) 範囲 `[['009ad080', '009ad087']]`
  - `CONDITIONAL_JUMP` [`009ad084`](#insn-009ad084) → [`009ad200`](#insn-009ad200)
  - `FALL_THROUGH` [`009ad084`](#insn-009ad084) → [`009ad088`](#insn-009ad088)
- ブロック [`009ad088`](#insn-009ad088) 範囲 `[['009ad088', '009ad097']]`
  - `CONDITIONAL_JUMP` [`009ad094`](#insn-009ad094) → [`009ad1c0`](#insn-009ad1c0)
  - `FALL_THROUGH` [`009ad094`](#insn-009ad094) → [`009ad098`](#insn-009ad098)
- ブロック [`009ad098`](#insn-009ad098) 範囲 `[['009ad098', '009ad09b']]`
  - `UNCONDITIONAL_JUMP` [`009ad098`](#insn-009ad098) → [`009ad1f8`](#insn-009ad1f8)
- ブロック [`009ad09c`](#insn-009ad09c) 範囲 `[['009ad09c', '009ad0a7']]`
  - `CONDITIONAL_JUMP` [`009ad0a4`](#insn-009ad0a4) → [`009ad080`](#insn-009ad080)
  - `FALL_THROUGH` [`009ad0a4`](#insn-009ad0a4) → [`009ad0a8`](#insn-009ad0a8)
- ブロック [`009ad0a8`](#insn-009ad0a8) 範囲 `[['009ad0a8', '009ad0b3']]`
  - `CONDITIONAL_JUMP` [`009ad0b0`](#insn-009ad0b0) → [`009ad09c`](#insn-009ad09c)
  - `FALL_THROUGH` [`009ad0b0`](#insn-009ad0b0) → [`009ad0b4`](#insn-009ad0b4)
- ブロック [`009ad0b4`](#insn-009ad0b4) 範囲 `[['009ad0b4', '009ad0bb']]`
  - `UNCONDITIONAL_JUMP` [`009ad0b8`](#insn-009ad0b8) → [`009ad0c8`](#insn-009ad0c8)
- ブロック [`009ad0bc`](#insn-009ad0bc) 範囲 `[['009ad0bc', '009ad0c7']]`
  - `CONDITIONAL_JUMP` [`009ad0c4`](#insn-009ad0c4) → [`009ad09c`](#insn-009ad09c)
  - `FALL_THROUGH` [`009ad0c4`](#insn-009ad0c4) → [`009ad0c8`](#insn-009ad0c8)
- ブロック [`009ad0c8`](#insn-009ad0c8) 範囲 `[['009ad0c8', '009ad0cb']]`
  - `FALL_THROUGH` [`009ad0c8`](#insn-009ad0c8) → [`009ad0cc`](#insn-009ad0cc)
- ブロック [`009ad0cc`](#insn-009ad0cc) 範囲 `[['009ad0cc', '009ad0d3']]`
  - `CONDITIONAL_JUMP` [`009ad0d0`](#insn-009ad0d0) → [`009ad0e0`](#insn-009ad0e0)
  - `FALL_THROUGH` [`009ad0d0`](#insn-009ad0d0) → [`009ad0d4`](#insn-009ad0d4)
- ブロック [`009ad0d4`](#insn-009ad0d4) 範囲 `[['009ad0d4', '009ad0df']]`
  - `FALL_THROUGH` [`009ad0dc`](#insn-009ad0dc) → [`009ad0e0`](#insn-009ad0e0)
- ブロック [`009ad0e0`](#insn-009ad0e0) 範囲 `[['009ad0e0', '009ad0ef']]`
  - `CONDITIONAL_JUMP` [`009ad0ec`](#insn-009ad0ec) → [`009ad108`](#insn-009ad108)
  - `FALL_THROUGH` [`009ad0ec`](#insn-009ad0ec) → [`009ad0f0`](#insn-009ad0f0)
- ブロック [`009ad0f0`](#insn-009ad0f0) 範囲 `[['009ad0f0', '009ad107']]`
  - `CONDITIONAL_JUMP` [`009ad104`](#insn-009ad104) → [`009ad13c`](#insn-009ad13c)
  - `FALL_THROUGH` [`009ad104`](#insn-009ad104) → [`009ad108`](#insn-009ad108)
- ブロック [`009ad108`](#insn-009ad108) 範囲 `[['009ad108', '009ad10f']]`
  - `CONDITIONAL_JUMP` [`009ad10c`](#insn-009ad10c) → [`009ad0bc`](#insn-009ad0bc)
  - `FALL_THROUGH` [`009ad10c`](#insn-009ad10c) → [`009ad110`](#insn-009ad110)
- ブロック [`009ad110`](#insn-009ad110) 範囲 `[['009ad110', '009ad11f']]`
  - `CONDITIONAL_JUMP` [`009ad11c`](#insn-009ad11c) → [`009ad0bc`](#insn-009ad0bc)
  - `FALL_THROUGH` [`009ad11c`](#insn-009ad11c) → [`009ad120`](#insn-009ad120)
- ブロック [`009ad120`](#insn-009ad120) 範囲 `[['009ad120', '009ad13b']]`
  - `UNCONDITIONAL_JUMP` [`009ad138`](#insn-009ad138) → [`009ad0bc`](#insn-009ad0bc)
- ブロック [`009ad13c`](#insn-009ad13c) 範囲 `[['009ad13c', '009ad147']]`
  - `CONDITIONAL_JUMP` [`009ad144`](#insn-009ad144) → [`009ad170`](#insn-009ad170)
  - `FALL_THROUGH` [`009ad144`](#insn-009ad144) → [`009ad148`](#insn-009ad148)
- ブロック [`009ad148`](#insn-009ad148) 範囲 `[['009ad148', '009ad15b']]`
  - `CONDITIONAL_JUMP` [`009ad158`](#insn-009ad158) → [`009ad168`](#insn-009ad168)
  - `FALL_THROUGH` [`009ad158`](#insn-009ad158) → [`009ad15c`](#insn-009ad15c)
- ブロック [`009ad15c`](#insn-009ad15c) 範囲 `[['009ad15c', '009ad167']]`
  - `FALL_THROUGH` [`009ad164`](#insn-009ad164) → [`009ad168`](#insn-009ad168)
- ブロック [`009ad168`](#insn-009ad168) 範囲 `[['009ad168', '009ad16f']]`
  - `UNCONDITIONAL_JUMP` [`009ad16c`](#insn-009ad16c) → [`009ad17c`](#insn-009ad17c)
- ブロック [`009ad170`](#insn-009ad170) 範囲 `[['009ad170', '009ad17b']]`
  - `FALL_THROUGH` [`009ad178`](#insn-009ad178) → [`009ad17c`](#insn-009ad17c)
- ブロック [`009ad17c`](#insn-009ad17c) 範囲 `[['009ad17c', '009ad183']]`
  - `FALL_THROUGH` [`009ad180`](#insn-009ad180) → [`009ad184`](#insn-009ad184)
- ブロック [`009ad184`](#insn-009ad184) 範囲 `[['009ad184', '009ad187']]`
  - `CONDITIONAL_JUMP` [`009ad184`](#insn-009ad184) → [`009ad09c`](#insn-009ad09c)
  - `FALL_THROUGH` [`009ad184`](#insn-009ad184) → [`009ad188`](#insn-009ad188)
- ブロック [`009ad188`](#insn-009ad188) 範囲 `[['009ad188', '009ad197']]`
  - `CONDITIONAL_JUMP` [`009ad194`](#insn-009ad194) → [`009ad09c`](#insn-009ad09c)
  - `FALL_THROUGH` [`009ad194`](#insn-009ad194) → [`009ad198`](#insn-009ad198)
- ブロック [`009ad198`](#insn-009ad198) 範囲 `[['009ad198', '009ad1b3']]`
  - `UNCONDITIONAL_JUMP` [`009ad1b0`](#insn-009ad1b0) → [`009ad09c`](#insn-009ad09c)
- ブロック [`009ad1b4`](#insn-009ad1b4) 範囲 `[['009ad1b4', '009ad1bf']]`
  - `CONDITIONAL_JUMP` [`009ad1bc`](#insn-009ad1bc) → [`009ad1f4`](#insn-009ad1f4)
  - `FALL_THROUGH` [`009ad1bc`](#insn-009ad1bc) → [`009ad1c0`](#insn-009ad1c0)
- ブロック [`009ad1c0`](#insn-009ad1c0) 範囲 `[['009ad1c0', '009ad1c7']]`
  - `CONDITIONAL_JUMP` [`009ad1c4`](#insn-009ad1c4) → [`009ad1b4`](#insn-009ad1b4)
  - `FALL_THROUGH` [`009ad1c4`](#insn-009ad1c4) → [`009ad1c8`](#insn-009ad1c8)
- ブロック [`009ad1c8`](#insn-009ad1c8) 範囲 `[['009ad1c8', '009ad1d7']]`
  - `CONDITIONAL_JUMP` [`009ad1d4`](#insn-009ad1d4) → [`009ad1b4`](#insn-009ad1b4)
  - `FALL_THROUGH` [`009ad1d4`](#insn-009ad1d4) → [`009ad1d8`](#insn-009ad1d8)
- ブロック [`009ad1d8`](#insn-009ad1d8) 範囲 `[['009ad1d8', '009ad1f3']]`
  - `UNCONDITIONAL_JUMP` [`009ad1f0`](#insn-009ad1f0) → [`009ad1b4`](#insn-009ad1b4)
- ブロック [`009ad1f4`](#insn-009ad1f4) 範囲 `[['009ad1f4', '009ad1f7']]`
  - `FALL_THROUGH` [`009ad1f4`](#insn-009ad1f4) → [`009ad1f8`](#insn-009ad1f8)
- ブロック [`009ad1f8`](#insn-009ad1f8) 範囲 `[['009ad1f8', '009ad1ff']]`
  - `FALL_THROUGH` [`009ad1fc`](#insn-009ad1fc) → [`009ad200`](#insn-009ad200)
- ブロック [`009ad200`](#insn-009ad200) 範囲 `[['009ad200', '009ad207']]`
  - `CONDITIONAL_JUMP` [`009ad204`](#insn-009ad204) → [`009ad20c`](#insn-009ad20c)
  - `FALL_THROUGH` [`009ad204`](#insn-009ad204) → [`009ad208`](#insn-009ad208)
- ブロック [`009ad208`](#insn-009ad208) 範囲 `[['009ad208', '009ad20b']]`
  - `FALL_THROUGH` [`009ad208`](#insn-009ad208) → [`009ad20c`](#insn-009ad20c)
- ブロック [`009ad20c`](#insn-009ad20c) 範囲 `[['009ad20c', '009ad213']]`
  - `FALL_THROUGH` [`009ad210`](#insn-009ad210) → [`009ad214`](#insn-009ad214)
- ブロック [`009ad214`](#insn-009ad214) 範囲 `[['009ad214', '009ad21f']]`
  - `CONDITIONAL_JUMP` [`009ad21c`](#insn-009ad21c) → [`009ad304`](#insn-009ad304)
  - `FALL_THROUGH` [`009ad21c`](#insn-009ad21c) → [`009ad220`](#insn-009ad220)
- ブロック [`009ad220`](#insn-009ad220) 範囲 `[['009ad220', '009ad23f']]`
- ブロック [`009ad240`](#insn-009ad240) 範囲 `[['009ad240', '009ad253']]`
  - `CONDITIONAL_JUMP` [`009ad250`](#insn-009ad250) → [`009ad304`](#insn-009ad304)
  - `FALL_THROUGH` [`009ad250`](#insn-009ad250) → [`009ad254`](#insn-009ad254)
- ブロック [`009ad254`](#insn-009ad254) 範囲 `[['009ad254', '009ad25b']]`
  - `FALL_THROUGH` [`009ad258`](#insn-009ad258) → [`009ad25c`](#insn-009ad25c)
- ブロック [`009ad25c`](#insn-009ad25c) 範囲 `[['009ad25c', '009ad26f']]`
  - `CONDITIONAL_JUMP` [`009ad26c`](#insn-009ad26c) → [`009ad304`](#insn-009ad304)
  - `FALL_THROUGH` [`009ad26c`](#insn-009ad26c) → [`009ad270`](#insn-009ad270)
- ブロック [`009ad270`](#insn-009ad270) 範囲 `[['009ad270', '009ad273']]`
- ブロック [`009ad274`](#insn-009ad274) 範囲 `[['009ad274', '009ad287']]`
  - `CONDITIONAL_JUMP` [`009ad284`](#insn-009ad284) → [`009ad304`](#insn-009ad304)
  - `FALL_THROUGH` [`009ad284`](#insn-009ad284) → [`009ad288`](#insn-009ad288)
- ブロック [`009ad288`](#insn-009ad288) 範囲 `[['009ad288', '009ad29f']]`
  - `UNCONDITIONAL_JUMP` [`009ad29c`](#insn-009ad29c) → [`009ad2d8`](#insn-009ad2d8)
- ブロック [`009ad2d8`](#insn-009ad2d8) 範囲 `[['009ad2d8', '009ad2df']]`
  - `CONDITIONAL_JUMP` [`009ad2dc`](#insn-009ad2dc) → [`009ad2e8`](#insn-009ad2e8)
  - `FALL_THROUGH` [`009ad2dc`](#insn-009ad2dc) → [`009ad2e0`](#insn-009ad2e0)
- ブロック [`009ad2e0`](#insn-009ad2e0) 範囲 `[['009ad2e0', '009ad2e7']]`
  - `FALL_THROUGH` [`009ad2e4`](#insn-009ad2e4) → [`009ad2e8`](#insn-009ad2e8)
- ブロック [`009ad2e8`](#insn-009ad2e8) 範囲 `[['009ad2e8', '009ad2fb']]`
  - `CONDITIONAL_JUMP` [`009ad2f8`](#insn-009ad2f8) → [`009ad304`](#insn-009ad304)
  - `FALL_THROUGH` [`009ad2f8`](#insn-009ad2f8) → [`009ad2fc`](#insn-009ad2fc)
- ブロック [`009ad2fc`](#insn-009ad2fc) 範囲 `[['009ad2fc', '009ad303']]`
- ブロック [`009ad304`](#insn-009ad304) 範囲 `[['009ad304', '009ad307']]`

## 命令位置別の参照

- [`009acdd0`](#insn-009acdd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acdd4`](#insn-009acdd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acdd8`](#insn-009acdd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acddc`](#insn-009acddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acde0`](#insn-009acde0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acde4`](#insn-009acde4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acdf4`](#insn-009acdf4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acdfc`](#insn-009acdfc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace04`](#insn-009ace04) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace08`](#insn-009ace08) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace10`](#insn-009ace10) → [`009ace2c`](#insn-009ace2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace1c`](#insn-009ace1c) → [`009acf74`](#insn-009acf74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace28`](#insn-009ace28) → [`009acf70`](#insn-009acf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace30`](#insn-009ace30) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace34`](#insn-009ace34) → [`009ace44`](#insn-009ace44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace40`](#insn-009ace40) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`009ace44`](#insn-009ace44) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace50`](#insn-009ace50) → [`009ace74`](#insn-009ace74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace5c`](#insn-009ace5c) → [`009b3fb8`](../009b3/009b3fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b3fb8` · 推定シンボル `None` · 推定型 `None`
- [`009ace64`](#insn-009ace64) → [`009aceb0`](#insn-009aceb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace70`](#insn-009ace70) → [`009ace54`](#insn-009ace54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace78`](#insn-009ace78) → [`009b5b08`](../009b5/009b5b08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5b08` · 推定シンボル `None` · 推定型 `None`
- [`009ace7c`](#insn-009ace7c) → [`009aceb0`](#insn-009aceb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ace84`](#insn-009ace84) → [`009b3fb8`](../009b3/009b3fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b3fb8` · 推定シンボル `None` · 推定型 `None`
- [`009ace90`](#insn-009ace90) → [`009b5af8`](../009b5/009b5af8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5af8` · 推定シンボル `None` · 推定型 `None`
- [`009ace94`](#insn-009ace94) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acea4`](#insn-009acea4) → [`009acee0`](#insn-009acee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aceac`](#insn-009aceac) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aceb0`](#insn-009aceb0) → [`009ace20`](#insn-009ace20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acebc`](#insn-009acebc) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009acec0`](#insn-009acec0) → [`009ace20`](#insn-009ace20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aced8`](#insn-009aced8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009acedc`](#insn-009acedc) → [`009ace20`](#insn-009ace20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acef0`](#insn-009acef0) → [`009ad240`](#insn-009ad240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf14`](#insn-009acf14) → [`009acf30`](#insn-009acf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf1c`](#insn-009acf1c) → [`009ad25c`](#insn-009ad25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf24`](#insn-009acf24) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`009acf2c`](#insn-009acf2c) → [`009acf34`](#insn-009acf34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf4c`](#insn-009acf4c) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`009acf50`](#insn-009acf50) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf54`](#insn-009acf54) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf58`](#insn-009acf58) → [`009acf64`](#insn-009acf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf60`](#insn-009acf60) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`009acf64`](#insn-009acf64) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf68`](#insn-009acf68) → [`009aceb4`](#insn-009aceb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf6c`](#insn-009acf6c) → [`009ace20`](#insn-009ace20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acf70`](#insn-009acf70) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfa0`](#insn-009acfa0) → [`009b0bbc`](../009b0/009b0bbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b0bbc` · 推定シンボル `None` · 推定型 `None`
- [`009acfac`](#insn-009acfac) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfb0`](#insn-009acfb0) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfb8`](#insn-009acfb8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfbc`](#insn-009acfbc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfc0`](#insn-009acfc0) → [`009ad070`](#insn-009ad070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfc4`](#insn-009acfc4) → [`009ad274`](#insn-009ad274) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfcc`](#insn-009acfcc) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`009acfd8`](#insn-009acfd8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfdc`](#insn-009acfdc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acfe0`](#insn-009acfe0) → [`009acff4`](#insn-009acff4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009acff0`](#insn-009acff0) → [`009ad018`](#insn-009ad018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad004`](#insn-009ad004) → [`009acfe4`](#insn-009acfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad010`](#insn-009ad010) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`009ad014`](#insn-009ad014) → [`009acfe4`](#insn-009acfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad01c`](#insn-009ad01c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad024`](#insn-009ad024) → [`009ad038`](#insn-009ad038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad028`](#insn-009ad028) → [`009ad070`](#insn-009ad070) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad034`](#insn-009ad034) → [`009ad06c`](#insn-009ad06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad03c`](#insn-009ad03c) → [`009ad02c`](#insn-009ad02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad048`](#insn-009ad048) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009ad04c`](#insn-009ad04c) → [`009ad02c`](#insn-009ad02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad064`](#insn-009ad064) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009ad068`](#insn-009ad068) → [`009ad02c`](#insn-009ad02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad06c`](#insn-009ad06c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad070`](#insn-009ad070) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad07c`](#insn-009ad07c) → [`009ad0a8`](#insn-009ad0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad080`](#insn-009ad080) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad084`](#insn-009ad084) → [`009ad200`](#insn-009ad200) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad088`](#insn-009ad088) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad094`](#insn-009ad094) → [`009ad1c0`](#insn-009ad1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad098`](#insn-009ad098) → [`009ad1f8`](#insn-009ad1f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0a4`](#insn-009ad0a4) → [`009ad080`](#insn-009ad080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0a8`](#insn-009ad0a8) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0b0`](#insn-009ad0b0) → [`009ad09c`](#insn-009ad09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0b8`](#insn-009ad0b8) → [`009ad0c8`](#insn-009ad0c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0c4`](#insn-009ad0c4) → [`009ad09c`](#insn-009ad09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0cc`](#insn-009ad0cc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0d0`](#insn-009ad0d0) → [`009ad0e0`](#insn-009ad0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0dc`](#insn-009ad0dc) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`009ad0e4`](#insn-009ad0e4) → [`009b3fb8`](../009b3/009b3fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b3fb8` · 推定シンボル `None` · 推定型 `None`
- [`009ad0ec`](#insn-009ad0ec) → [`009ad108`](#insn-009ad108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0f0`](#insn-009ad0f0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad0f4`](#insn-009ad0f4) → [`009b5af8`](../009b5/009b5af8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5af8` · 推定シンボル `None` · 推定型 `None`
- [`009ad100`](#insn-009ad100) → [`008065d4`](../00806/008065d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008065d4` · 推定シンボル `None` · 推定型 `None`
- [`009ad104`](#insn-009ad104) → [`009ad13c`](#insn-009ad13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad108`](#insn-009ad108) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad10c`](#insn-009ad10c) → [`009ad0bc`](#insn-009ad0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad118`](#insn-009ad118) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009ad11c`](#insn-009ad11c) → [`009ad0bc`](#insn-009ad0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad134`](#insn-009ad134) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009ad138`](#insn-009ad138) → [`009ad0bc`](#insn-009ad0bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad144`](#insn-009ad144) → [`009ad170`](#insn-009ad170) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad148`](#insn-009ad148) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad150`](#insn-009ad150) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad158`](#insn-009ad158) → [`009ad168`](#insn-009ad168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad164`](#insn-009ad164) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`009ad16c`](#insn-009ad16c) → [`009ad17c`](#insn-009ad17c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad178`](#insn-009ad178) → [`009b0a4c`](../009b0/009b0a4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b0a4c` · 推定シンボル `None` · 推定型 `None`
- [`009ad17c`](#insn-009ad17c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad184`](#insn-009ad184) → [`009ad09c`](#insn-009ad09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad190`](#insn-009ad190) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009ad194`](#insn-009ad194) → [`009ad09c`](#insn-009ad09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1ac`](#insn-009ad1ac) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009ad1b0`](#insn-009ad1b0) → [`009ad09c`](#insn-009ad09c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1bc`](#insn-009ad1bc) → [`009ad1f4`](#insn-009ad1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1c4`](#insn-009ad1c4) → [`009ad1b4`](#insn-009ad1b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1d0`](#insn-009ad1d0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009ad1d4`](#insn-009ad1d4) → [`009ad1b4`](#insn-009ad1b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1ec`](#insn-009ad1ec) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009ad1f0`](#insn-009ad1f0) → [`009ad1b4`](#insn-009ad1b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1f4`](#insn-009ad1f4) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1f8`](#insn-009ad1f8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad1fc`](#insn-009ad1fc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`009ad200`](#insn-009ad200) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad204`](#insn-009ad204) → [`009ad20c`](#insn-009ad20c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad208`](#insn-009ad208) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`009ad20c`](#insn-009ad20c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad214`](#insn-009ad214) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad21c`](#insn-009ad21c) → [`009ad304`](#insn-009ad304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad220`](#insn-009ad220) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad224`](#insn-009ad224) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad228`](#insn-009ad228) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad22c`](#insn-009ad22c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad230`](#insn-009ad230) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad234`](#insn-009ad234) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad240`](#insn-009ad240) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad248`](#insn-009ad248) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad250`](#insn-009ad250) → [`009ad304`](#insn-009ad304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad258`](#insn-009ad258) → [`006b8c04`](../006b8/006b8c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b8c04` · 推定シンボル `None` · 推定型 `None`
- [`009ad25c`](#insn-009ad25c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad264`](#insn-009ad264) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad26c`](#insn-009ad26c) → [`009ad304`](#insn-009ad304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad270`](#insn-009ad270) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`
- [`009ad274`](#insn-009ad274) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad27c`](#insn-009ad27c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad284`](#insn-009ad284) → [`009ad304`](#insn-009ad304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad28c`](#insn-009ad28c) → [`009b0ba8`](../009b0/009b0ba8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b0ba8` · 推定シンボル `None` · 推定型 `None`
- [`009ad298`](#insn-009ad298) → [`009b1c40`](../009b1/009b1c40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b1c40` · 推定シンボル `None` · 推定型 `None`
- [`009ad29c`](#insn-009ad29c) → [`009ad2d8`](#insn-009ad2d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2d8`](#insn-009ad2d8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2dc`](#insn-009ad2dc) → [`009ad2e8`](#insn-009ad2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2e0`](#insn-009ad2e0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2e4`](#insn-009ad2e4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`009ad2e8`](#insn-009ad2e8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2f0`](#insn-009ad2f0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad2f8`](#insn-009ad2f8) → [`009ad304`](#insn-009ad304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ad300`](#insn-009ad300) → [`00c53b3c`](../00c53/00c53b3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53b3c` · 推定シンボル `None` · 推定型 `None`
- [`009ad304`](#insn-009ad304) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009acdd0`](#insn-009acdd0)

~~~json
{
  "source": "009acdd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acdd4`](#insn-009acdd4)

~~~json
{
  "source": "009acdd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acdd8`](#insn-009acdd8)

~~~json
{
  "source": "009acdd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acddc`](#insn-009acddc)

~~~json
{
  "source": "009acddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acde0`](#insn-009acde0)

~~~json
{
  "source": "009acde0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acde4`](#insn-009acde4)

~~~json
{
  "source": "009acde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acdf4`](#insn-009acdf4)

~~~json
{
  "source": "009acdf4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acdfc`](#insn-009acdfc)

~~~json
{
  "source": "009acdfc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace04`](#insn-009ace04)

~~~json
{
  "source": "009ace04",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace08`](#insn-009ace08)

~~~json
{
  "source": "009ace08",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace10`](#insn-009ace10)

~~~json
{
  "source": "009ace10",
  "target": "009ace2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace1c`](#insn-009ace1c)

~~~json
{
  "source": "009ace1c",
  "target": "009acf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace28`](#insn-009ace28)

~~~json
{
  "source": "009ace28",
  "target": "009acf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace30`](#insn-009ace30)

~~~json
{
  "source": "009ace30",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace34`](#insn-009ace34)

~~~json
{
  "source": "009ace34",
  "target": "009ace44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace40`](#insn-009ace40)

~~~json
{
  "source": "009ace40",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ace44`](#insn-009ace44)

~~~json
{
  "source": "009ace44",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace50`](#insn-009ace50)

~~~json
{
  "source": "009ace50",
  "target": "009ace74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace5c`](#insn-009ace5c)

~~~json
{
  "source": "009ace5c",
  "target": "009b3fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ace64`](#insn-009ace64)

~~~json
{
  "source": "009ace64",
  "target": "009aceb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace70`](#insn-009ace70)

~~~json
{
  "source": "009ace70",
  "target": "009ace54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace78`](#insn-009ace78)

~~~json
{
  "source": "009ace78",
  "target": "009b5b08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ace7c`](#insn-009ace7c)

~~~json
{
  "source": "009ace7c",
  "target": "009aceb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ace84`](#insn-009ace84)

~~~json
{
  "source": "009ace84",
  "target": "009b3fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ace90`](#insn-009ace90)

~~~json
{
  "source": "009ace90",
  "target": "009b5af8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ace94`](#insn-009ace94)

~~~json
{
  "source": "009ace94",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acea4`](#insn-009acea4)

~~~json
{
  "source": "009acea4",
  "target": "009acee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aceac`](#insn-009aceac)

~~~json
{
  "source": "009aceac",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aceb0`](#insn-009aceb0)

~~~json
{
  "source": "009aceb0",
  "target": "009ace20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acebc`](#insn-009acebc)

~~~json
{
  "source": "009acebc",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009acec0`](#insn-009acec0)

~~~json
{
  "source": "009acec0",
  "target": "009ace20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aced8`](#insn-009aced8)

~~~json
{
  "source": "009aced8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009acedc`](#insn-009acedc)

~~~json
{
  "source": "009acedc",
  "target": "009ace20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acef0`](#insn-009acef0)

~~~json
{
  "source": "009acef0",
  "target": "009ad240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf14`](#insn-009acf14)

~~~json
{
  "source": "009acf14",
  "target": "009acf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf1c`](#insn-009acf1c)

~~~json
{
  "source": "009acf1c",
  "target": "009ad25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf24`](#insn-009acf24)

~~~json
{
  "source": "009acf24",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009acf2c`](#insn-009acf2c)

~~~json
{
  "source": "009acf2c",
  "target": "009acf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf4c`](#insn-009acf4c)

~~~json
{
  "source": "009acf4c",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009acf50`](#insn-009acf50)

~~~json
{
  "source": "009acf50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf54`](#insn-009acf54)

~~~json
{
  "source": "009acf54",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf58`](#insn-009acf58)

~~~json
{
  "source": "009acf58",
  "target": "009acf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf60`](#insn-009acf60)

~~~json
{
  "source": "009acf60",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009acf64`](#insn-009acf64)

~~~json
{
  "source": "009acf64",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf68`](#insn-009acf68)

~~~json
{
  "source": "009acf68",
  "target": "009aceb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf6c`](#insn-009acf6c)

~~~json
{
  "source": "009acf6c",
  "target": "009ace20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acf70`](#insn-009acf70)

~~~json
{
  "source": "009acf70",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfa0`](#insn-009acfa0)

~~~json
{
  "source": "009acfa0",
  "target": "009b0bbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009acfac`](#insn-009acfac)

~~~json
{
  "source": "009acfac",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfb0`](#insn-009acfb0)

~~~json
{
  "source": "009acfb0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfb8`](#insn-009acfb8)

~~~json
{
  "source": "009acfb8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfbc`](#insn-009acfbc)

~~~json
{
  "source": "009acfbc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfc0`](#insn-009acfc0)

~~~json
{
  "source": "009acfc0",
  "target": "009ad070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfc4`](#insn-009acfc4)

~~~json
{
  "source": "009acfc4",
  "target": "009ad274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfcc`](#insn-009acfcc)

~~~json
{
  "source": "009acfcc",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009acfd8`](#insn-009acfd8)

~~~json
{
  "source": "009acfd8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfdc`](#insn-009acfdc)

~~~json
{
  "source": "009acfdc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acfe0`](#insn-009acfe0)

~~~json
{
  "source": "009acfe0",
  "target": "009acff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009acff0`](#insn-009acff0)

~~~json
{
  "source": "009acff0",
  "target": "009ad018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad004`](#insn-009ad004)

~~~json
{
  "source": "009ad004",
  "target": "009acfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad010`](#insn-009ad010)

~~~json
{
  "source": "009ad010",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad014`](#insn-009ad014)

~~~json
{
  "source": "009ad014",
  "target": "009acfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad01c`](#insn-009ad01c)

~~~json
{
  "source": "009ad01c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad024`](#insn-009ad024)

~~~json
{
  "source": "009ad024",
  "target": "009ad038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad028`](#insn-009ad028)

~~~json
{
  "source": "009ad028",
  "target": "009ad070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad034`](#insn-009ad034)

~~~json
{
  "source": "009ad034",
  "target": "009ad06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad03c`](#insn-009ad03c)

~~~json
{
  "source": "009ad03c",
  "target": "009ad02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad048`](#insn-009ad048)

~~~json
{
  "source": "009ad048",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad04c`](#insn-009ad04c)

~~~json
{
  "source": "009ad04c",
  "target": "009ad02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad064`](#insn-009ad064)

~~~json
{
  "source": "009ad064",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad068`](#insn-009ad068)

~~~json
{
  "source": "009ad068",
  "target": "009ad02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad06c`](#insn-009ad06c)

~~~json
{
  "source": "009ad06c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad070`](#insn-009ad070)

~~~json
{
  "source": "009ad070",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad07c`](#insn-009ad07c)

~~~json
{
  "source": "009ad07c",
  "target": "009ad0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad080`](#insn-009ad080)

~~~json
{
  "source": "009ad080",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad084`](#insn-009ad084)

~~~json
{
  "source": "009ad084",
  "target": "009ad200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad088`](#insn-009ad088)

~~~json
{
  "source": "009ad088",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad094`](#insn-009ad094)

~~~json
{
  "source": "009ad094",
  "target": "009ad1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad098`](#insn-009ad098)

~~~json
{
  "source": "009ad098",
  "target": "009ad1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0a4`](#insn-009ad0a4)

~~~json
{
  "source": "009ad0a4",
  "target": "009ad080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0a8`](#insn-009ad0a8)

~~~json
{
  "source": "009ad0a8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0b0`](#insn-009ad0b0)

~~~json
{
  "source": "009ad0b0",
  "target": "009ad09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0b8`](#insn-009ad0b8)

~~~json
{
  "source": "009ad0b8",
  "target": "009ad0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0c4`](#insn-009ad0c4)

~~~json
{
  "source": "009ad0c4",
  "target": "009ad09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0cc`](#insn-009ad0cc)

~~~json
{
  "source": "009ad0cc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0d0`](#insn-009ad0d0)

~~~json
{
  "source": "009ad0d0",
  "target": "009ad0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0dc`](#insn-009ad0dc)

~~~json
{
  "source": "009ad0dc",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad0e4`](#insn-009ad0e4)

~~~json
{
  "source": "009ad0e4",
  "target": "009b3fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad0ec`](#insn-009ad0ec)

~~~json
{
  "source": "009ad0ec",
  "target": "009ad108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0f0`](#insn-009ad0f0)

~~~json
{
  "source": "009ad0f0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad0f4`](#insn-009ad0f4)

~~~json
{
  "source": "009ad0f4",
  "target": "009b5af8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad100`](#insn-009ad100)

~~~json
{
  "source": "009ad100",
  "target": "008065d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad104`](#insn-009ad104)

~~~json
{
  "source": "009ad104",
  "target": "009ad13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad108`](#insn-009ad108)

~~~json
{
  "source": "009ad108",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad10c`](#insn-009ad10c)

~~~json
{
  "source": "009ad10c",
  "target": "009ad0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad118`](#insn-009ad118)

~~~json
{
  "source": "009ad118",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad11c`](#insn-009ad11c)

~~~json
{
  "source": "009ad11c",
  "target": "009ad0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad134`](#insn-009ad134)

~~~json
{
  "source": "009ad134",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad138`](#insn-009ad138)

~~~json
{
  "source": "009ad138",
  "target": "009ad0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad144`](#insn-009ad144)

~~~json
{
  "source": "009ad144",
  "target": "009ad170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad148`](#insn-009ad148)

~~~json
{
  "source": "009ad148",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad150`](#insn-009ad150)

~~~json
{
  "source": "009ad150",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad158`](#insn-009ad158)

~~~json
{
  "source": "009ad158",
  "target": "009ad168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad164`](#insn-009ad164)

~~~json
{
  "source": "009ad164",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad16c`](#insn-009ad16c)

~~~json
{
  "source": "009ad16c",
  "target": "009ad17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad178`](#insn-009ad178)

~~~json
{
  "source": "009ad178",
  "target": "009b0a4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad17c`](#insn-009ad17c)

~~~json
{
  "source": "009ad17c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad184`](#insn-009ad184)

~~~json
{
  "source": "009ad184",
  "target": "009ad09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad190`](#insn-009ad190)

~~~json
{
  "source": "009ad190",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad194`](#insn-009ad194)

~~~json
{
  "source": "009ad194",
  "target": "009ad09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1ac`](#insn-009ad1ac)

~~~json
{
  "source": "009ad1ac",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad1b0`](#insn-009ad1b0)

~~~json
{
  "source": "009ad1b0",
  "target": "009ad09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1bc`](#insn-009ad1bc)

~~~json
{
  "source": "009ad1bc",
  "target": "009ad1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1c4`](#insn-009ad1c4)

~~~json
{
  "source": "009ad1c4",
  "target": "009ad1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1d0`](#insn-009ad1d0)

~~~json
{
  "source": "009ad1d0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad1d4`](#insn-009ad1d4)

~~~json
{
  "source": "009ad1d4",
  "target": "009ad1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1ec`](#insn-009ad1ec)

~~~json
{
  "source": "009ad1ec",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad1f0`](#insn-009ad1f0)

~~~json
{
  "source": "009ad1f0",
  "target": "009ad1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1f4`](#insn-009ad1f4)

~~~json
{
  "source": "009ad1f4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1f8`](#insn-009ad1f8)

~~~json
{
  "source": "009ad1f8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad1fc`](#insn-009ad1fc)

~~~json
{
  "source": "009ad1fc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad200`](#insn-009ad200)

~~~json
{
  "source": "009ad200",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad204`](#insn-009ad204)

~~~json
{
  "source": "009ad204",
  "target": "009ad20c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad208`](#insn-009ad208)

~~~json
{
  "source": "009ad208",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad20c`](#insn-009ad20c)

~~~json
{
  "source": "009ad20c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad214`](#insn-009ad214)

~~~json
{
  "source": "009ad214",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad21c`](#insn-009ad21c)

~~~json
{
  "source": "009ad21c",
  "target": "009ad304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad220`](#insn-009ad220)

~~~json
{
  "source": "009ad220",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad224`](#insn-009ad224)

~~~json
{
  "source": "009ad224",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad228`](#insn-009ad228)

~~~json
{
  "source": "009ad228",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad22c`](#insn-009ad22c)

~~~json
{
  "source": "009ad22c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad230`](#insn-009ad230)

~~~json
{
  "source": "009ad230",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad234`](#insn-009ad234)

~~~json
{
  "source": "009ad234",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad240`](#insn-009ad240)

~~~json
{
  "source": "009ad240",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad248`](#insn-009ad248)

~~~json
{
  "source": "009ad248",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad250`](#insn-009ad250)

~~~json
{
  "source": "009ad250",
  "target": "009ad304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad258`](#insn-009ad258)

~~~json
{
  "source": "009ad258",
  "target": "006b8c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad25c`](#insn-009ad25c)

~~~json
{
  "source": "009ad25c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad264`](#insn-009ad264)

~~~json
{
  "source": "009ad264",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad26c`](#insn-009ad26c)

~~~json
{
  "source": "009ad26c",
  "target": "009ad304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad270`](#insn-009ad270)

~~~json
{
  "source": "009ad270",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad274`](#insn-009ad274)

~~~json
{
  "source": "009ad274",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad27c`](#insn-009ad27c)

~~~json
{
  "source": "009ad27c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad284`](#insn-009ad284)

~~~json
{
  "source": "009ad284",
  "target": "009ad304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad28c`](#insn-009ad28c)

~~~json
{
  "source": "009ad28c",
  "target": "009b0ba8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad298`](#insn-009ad298)

~~~json
{
  "source": "009ad298",
  "target": "009b1c40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad29c`](#insn-009ad29c)

~~~json
{
  "source": "009ad29c",
  "target": "009ad2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2d8`](#insn-009ad2d8)

~~~json
{
  "source": "009ad2d8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2dc`](#insn-009ad2dc)

~~~json
{
  "source": "009ad2dc",
  "target": "009ad2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2e0`](#insn-009ad2e0)

~~~json
{
  "source": "009ad2e0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2e4`](#insn-009ad2e4)

~~~json
{
  "source": "009ad2e4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad2e8`](#insn-009ad2e8)

~~~json
{
  "source": "009ad2e8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2f0`](#insn-009ad2f0)

~~~json
{
  "source": "009ad2f0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad2f8`](#insn-009ad2f8)

~~~json
{
  "source": "009ad2f8",
  "target": "009ad304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ad300`](#insn-009ad300)

~~~json
{
  "source": "009ad300",
  "target": "00c53b3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ad304`](#insn-009ad304)

~~~json
{
  "source": "009ad304",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
