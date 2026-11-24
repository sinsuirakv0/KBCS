# 00c0bccc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c0b8a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b8a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0042.md#compare-debd5bb9f21a6745c74af04b5090a8e6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c0bd68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-03f9d8d3c84abb3d41d38fb44151be7d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0bccc",
  "name": "FUN_00c0bccc",
  "size": 992,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f89db2358d79d5e6bd29f23b712c712079f82cdd6c6fc04007bb50ac8b09879",
  "source_text_sha256": "1f89db2358d79d5e6bd29f23b712c712079f82cdd6c6fc04007bb50ac8b09879",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c0bccc",
        "00c0c0ab"
      ]
    ],
    "bytes_sha256": "c7b3ae3a8bafc01bfa154926e13cc1fc77c438e72224291508f48ccb2e8e1c84",
    "instruction_count": 248,
    "instruction_bytes": 992,
    "body_bytes": 992,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00c0bcc4](../00c0b/00c0bcc4.md)

## 呼び出し先

- [00c363bc](../00c36/00c363bc.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5be70](../00c5b/00c5be70.md)
- [00c5e540](../00c5e/00c5e540.md)
- [00c5e590](../00c5e/00c5e590.md)
- [00c5e5a0](../00c5e/00c5e5a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6331 bytes

~~~c

long * FUN_00c0bccc(undefined8 param_1,long *param_2,long *param_3,long param_4,uint *param_5,
                   undefined2 *param_6)

{
  uint uVar1;
  ulong uVar2;
  long *plVar3;
  bool bVar4;
  undefined2 uVar5;
  int iVar6;
  ulong uVar7;
  void *pvVar8;
  ulong uVar9;
  undefined4 uVar10;
  void *pvVar11;
  undefined4 local_1bc;
  undefined4 *local_1b8;
  undefined4 auStack_1b0 [40];
  void *local_110;
  undefined8 local_108;
  ulong local_100;
  void *local_f8;
  byte local_f0 [8];
  ulong local_e8;
  void *local_e0;
  undefined1 auStack_d4 [104];
  undefined4 local_6c [3];
  
                    /* try { // try from 00c0bd00 to 00d0becf has its CatchHandler @ 00c0bd00
                       catch() { ... } // from try @ 00c0bd00 with catch @ 00c0bd00
                       catch() { ... } // from try @ 00c0beec with catch @ 00c0bd00
                       catch() { ... } // from try @ 00c0c188 with catch @ 00c0bd00 */
  uVar1 = *(uint *)(param_4 + 8) & 0x4a;
  if (uVar1 == 0) {
    uVar10 = 0;
  }
  else if (uVar1 == 0x40) {
    uVar10 = 8;
  }
  else if (uVar1 == 8) {
    uVar10 = 0x10;
  }
  else {
    uVar10 = 10;
  }
  _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw
            (local_f0,param_4,auStack_d4,local_6c);
  local_108 = 0;
  local_100 = 0;
  local_f8 = (void *)0x0;
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc(&local_108,0x16,0);
  local_1b8 = auStack_1b0;
  pvVar11 = (void *)((ulong)&local_108 | 1);
  local_1bc = 0;
  pvVar8 = local_f8;
  if ((local_108 & 1) == 0) {
    pvVar8 = (void *)((long)&local_108 + 1);
  }
  local_110 = pvVar8;
LAB_00c0bdac:
  if (param_2 == (long *)0x0) {
    bVar4 = true;
    if (param_3 != (long *)0x0) goto LAB_00c0bdf4;
LAB_00c0bdcc:
    if (bVar4 != false) goto LAB_00c0bf70;
  }
  else {
    if ((int *)param_2[3] == (int *)param_2[4]) {
      iVar6 = (**(code **)(*param_2 + 0x48))(param_2);
    }
    else {
      iVar6 = *(int *)param_2[3];
    }
    bVar4 = iVar6 == -1;
    plVar3 = (long *)0x0;
    if (!bVar4) {
      plVar3 = param_2;
    }
    param_2 = plVar3;
    if (param_3 == (long *)0x0) goto LAB_00c0bdcc;
LAB_00c0bdf4:
    if ((int *)param_3[3] == (int *)param_3[4]) {
      iVar6 = (**(code **)(*param_3 + 0x48))(param_3);
    }
    else {
      iVar6 = *(int *)param_3[3];
    }
    plVar3 = (long *)0x0;
    if (iVar6 != -1) {
      plVar3 = param_3;
    }
    param_3 = plVar3;
    if (bVar4 == (iVar6 == -1)) goto LAB_00c0bf70;
  }
  uVar7 = local_108 >> 1 & 0x7f;
  if ((local_108 & 1) != 0) {
    uVar7 = local_100;
  }
  if (local_110 == (void *)((long)pvVar8 + uVar7)) {
    if ((long)uVar7 < 1) {
      uVar9 = uVar7 * 2;
      pvVar8 = local_f8;
      uVar2 = uVar9;
      if ((local_108 & 1) == 0) {
        local_108 = CONCAT71(local_108._1_7_,(char)((int)uVar9 << 1));
        pvVar8 = pvVar11;
        uVar2 = local_100;
      }
      local_100 = uVar2;
      *(undefined1 *)((long)pvVar8 + uVar9) = 0;
    }
    else {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
                (&local_108,uVar7,0);
    }
    uVar2 = 0x16;
    if ((local_108 & 1) != 0) {
      uVar2 = (local_108 & 0xfffffffffffffffe) - 1;
    }
    uVar9 = local_108 >> 1 & 0x7f;
    if ((local_108 & 1) != 0) {
      uVar9 = local_100;
    }
    if (uVar2 < uVar9 || uVar2 - uVar9 == 0) {
      pvVar8 = local_f8;
      uVar9 = uVar2;
      if ((local_108 & 1) == 0) {
                    /* try { // try from 00c0bed0 to 00d0beeb has its CatchHandler @ 00c0c200 */
        local_108 = CONCAT71(local_108._1_7_,(char)((int)uVar2 << 1));
        pvVar8 = pvVar11;
        uVar9 = local_100;
      }
      local_100 = uVar9;
      *(undefined1 *)((long)pvVar8 + uVar2) = 0;
    }
    else {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
                (&local_108,uVar2 - uVar9,0);
    }
                    /* try { // try from 00c0beec to 00d0c097 has its CatchHandler @ 00c0bd00 */
    pvVar8 = pvVar11;
    if ((local_108 & 1) != 0) {
      pvVar8 = local_f8;
    }
    local_110 = (void *)((long)pvVar8 + uVar7);
  }
  if ((uint *)param_2[3] == (uint *)param_2[4]) {
    uVar7 = (**(code **)(*param_2 + 0x48))(param_2);
  }
  else {
    uVar7 = (ulong)*(uint *)param_2[3];
  }
  iVar6 = _ZNSt6__ndk19__num_getIwE17__stage2_int_loopEwiPcRS2_RjwRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_Pw
                    (uVar7,uVar10,pvVar8,&local_110,&local_1bc,local_6c[0],local_f0,auStack_1b0,
                     &local_1b8,auStack_d4);
  if (iVar6 != 0) goto LAB_00c0bf70;
  if (param_2[3] == param_2[4]) {
    (**(code **)(*param_2 + 0x50))(param_2);
  }
  else {
    param_2[3] = param_2[3] + 4;
  }
  goto LAB_00c0bdac;
LAB_00c0bf70:
  uVar7 = (ulong)(local_f0[0] >> 1);
  if ((local_f0[0] & 1) != 0) {
    uVar7 = local_e8;
  }
  if ((uVar7 != 0) && ((long)local_1b8 - (long)auStack_1b0 < 0xa0)) {
    *local_1b8 = local_1bc;
    local_1b8 = local_1b8 + 1;
  }
  uVar5 = FUN_00c363bc(pvVar8,local_110,param_5,uVar10);
  *param_6 = uVar5;
  _ZNSt6__ndk116__check_groupingERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjS8_Rj
            (local_f0,auStack_1b0,local_1b8,param_5);
  if (param_2 == (long *)0x0) {
    bVar4 = true;
    if (param_3 != (long *)0x0) goto LAB_00c0c024;
LAB_00c0bffc:
    if (!bVar4) goto LAB_00c0c064;
  }
  else {
    if ((int *)param_2[3] == (int *)param_2[4]) {
      iVar6 = (**(code **)(*param_2 + 0x48))(param_2);
    }
    else {
      iVar6 = *(int *)param_2[3];
    }
    bVar4 = iVar6 == -1;
    plVar3 = (long *)0x0;
    if (!bVar4) {
      plVar3 = param_2;
    }
    param_2 = plVar3;
    if (param_3 == (long *)0x0) goto LAB_00c0bffc;
LAB_00c0c024:
    if ((int *)param_3[3] == (int *)param_3[4]) {
      iVar6 = (**(code **)(*param_3 + 0x48))(param_3);
    }
    else {
      iVar6 = *(int *)param_3[3];
    }
    if (bVar4 != (iVar6 == -1)) goto LAB_00c0c064;
  }
  *param_5 = *param_5 | 2;
LAB_00c0c064:
  if ((local_108 & 1) != 0) {
    _ZdlPv(local_f8);
  }
  if ((local_f0[0] & 1) != 0) {
    _ZdlPv(local_e0);
  }
                    /* try { // try from 00c0c098 to 00d0c0a3 has its CatchHandler @ 00c0c1dc */
                    /* try { // try from 00c0c0a8 to 00d0c0bb has its CatchHandler @ 00c0c1bc */
  return param_2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c0bccc"></a> `00c0bccc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c0bcd0"></a> `00c0bcd0` | `ff 83 07 d1` | sub sp,sp,#0x1e0 | `FALL_THROUGH`
<a id="insn-00c0bcd4"></a> `00c0bcd4` | `fd 7b 18 a9` | stp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00c0bcd8"></a> `00c0bcd8` | `fc 6f 19 a9` | stp x28,x27,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00c0bcdc"></a> `00c0bcdc` | `fa 67 1a a9` | stp x26,x25,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00c0bce0"></a> `00c0bce0` | `f8 5f 1b a9` | stp x24,x23,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00c0bce4"></a> `00c0bce4` | `f6 57 1c a9` | stp x22,x21,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00c0bce8"></a> `00c0bce8` | `f4 4f 1d a9` | stp x20,x19,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00c0bcec"></a> `00c0bcec` | `fd 03 06 91` | add x29,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00c0bcf0"></a> `00c0bcf0` | `68 08 40 b9` | ldr w8,[x3, #0x8] | `FALL_THROUGH`
<a id="insn-00c0bcf4"></a> `00c0bcf4` | `49 09 80 52` | mov w9,#0x4a | `FALL_THROUGH`
<a id="insn-00c0bcf8"></a> `00c0bcf8` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00c0bcfc"></a> `00c0bcfc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00c0bd00"></a> `00c0bd00` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00c0bd04"></a> `00c0bd04` | `ba c3 02 d1` | sub x26,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-00c0bd08"></a> `00c0bd08` | `08 01 09 6a` | ands w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00c0bd0c"></a> `00c0bd0c` | `e5 0b 00 f9` | str x5,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0bd10"></a> `00c0bd10` | `20 01 00 54` | b.eq 0x00c0bd34 | `CONDITIONAL_JUMP`
<a id="insn-00c0bd14"></a> `00c0bd14` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c0bd18"></a> `00c0bd18` | `a0 00 00 54` | b.eq 0x00c0bd2c | `CONDITIONAL_JUMP`
<a id="insn-00c0bd1c"></a> `00c0bd1c` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00c0bd20"></a> `00c0bd20` | `e1 00 00 54` | b.ne 0x00c0bd3c | `CONDITIONAL_JUMP`
<a id="insn-00c0bd24"></a> `00c0bd24` | `17 02 80 52` | mov w23,#0x10 | `FALL_THROUGH`
<a id="insn-00c0bd28"></a> `00c0bd28` | `06 00 00 14` | b 0x00c0bd40 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bd2c"></a> `00c0bd2c` | `17 01 80 52` | mov w23,#0x8 | `FALL_THROUGH`
<a id="insn-00c0bd30"></a> `00c0bd30` | `04 00 00 14` | b 0x00c0bd40 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bd34"></a> `00c0bd34` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00c0bd38"></a> `00c0bd38` | `02 00 00 14` | b 0x00c0bd40 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bd3c"></a> `00c0bd3c` | `57 01 80 52` | mov w23,#0xa | `FALL_THROUGH`
<a id="insn-00c0bd40"></a> `00c0bd40` | `a8 43 02 d1` | sub x8,x29,#0x90 | `FALL_THROUGH`
<a id="insn-00c0bd44"></a> `00c0bd44` | `a1 d3 01 d1` | sub x1,x29,#0x74 | `FALL_THROUGH`
<a id="insn-00c0bd48"></a> `00c0bd48` | `a2 33 00 d1` | sub x2,x29,#0xc | `FALL_THROUGH`
<a id="insn-00c0bd4c"></a> `00c0bd4c` | `e4 0f 00 f9` | str x4,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bd50"></a> `00c0bd50` | `bb d3 01 d1` | sub x27,x29,#0x74 | `FALL_THROUGH`
<a id="insn-00c0bd54"></a> `00c0bd54` | `0f 4a 01 94` | bl 0x00c5e590 | `UNCONDITIONAL_CALL`
<a id="insn-00c0bd58"></a> `00c0bd58` | `5f ff 00 a9` | stp xzr,xzr,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00c0bd5c"></a> `00c0bd5c` | `5f 0f 00 f9` | str xzr,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bd60"></a> `00c0bd60` | `a0 a3 02 d1` | sub x0,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00c0bd64"></a> `00c0bd64` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00c0bd68"></a> `00c0bd68` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00c0bd6c"></a> `00c0bd6c` | `b3 a3 02 d1` | sub x19,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00c0bd70"></a> `00c0bd70` | `40 40 01 94` | bl 0x00c5be70 | `UNCONDITIONAL_CALL`
<a id="insn-00c0bd74"></a> `00c0bd74` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00c0bd78"></a> `00c0bd78` | `49 0f 40 f9` | ldr x9,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bd7c"></a> `00c0bd7c` | `ea c3 00 91` | add x10,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00c0bd80"></a> `00c0bd80` | `7c 02 40 b2` | orr x28,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bd84"></a> `00c0bd84` | `d6 02 80 52` | mov w22,#0x16 | `FALL_THROUGH`
<a id="insn-00c0bd88"></a> `00c0bd88` | `ea 17 00 f9` | str x10,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00c0bd8c"></a> `00c0bd8c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bd90"></a> `00c0bd90` | `ff 27 00 b9` | str wzr,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00c0bd94"></a> `00c0bd94` | `38 15 93 9a` | csinc x24,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00c0bd98"></a> `00c0bd98` | `f3 a3 00 91` | add x19,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00c0bd9c"></a> `00c0bd9c` | `58 03 00 f9` | str x24,[x26] | `FALL_THROUGH`
<a id="insn-00c0bda0"></a> `00c0bda0` | `03 00 00 14` | b 0x00c0bdac | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bda4"></a> `00c0bda4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00c0bda8"></a> `00c0bda8` | `a8 0e 00 f9` | str x8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bdac"></a> `00c0bdac` | `d5 00 00 b4` | cbz x21,0x00c0bdc4 | `CONDITIONAL_JUMP`
<a id="insn-00c0bdb0"></a> `00c0bdb0` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bdb4"></a> `00c0bdb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c0bdb8"></a> `00c0bdb8` | `e0 00 00 54` | b.eq 0x00c0bdd4 | `CONDITIONAL_JUMP`
<a id="insn-00c0bdbc"></a> `00c0bdbc` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00c0bdc0"></a> `00c0bdc0` | `09 00 00 14` | b 0x00c0bde4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bdc4"></a> `00c0bdc4` | `39 00 80 52` | mov w25,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bdc8"></a> `00c0bdc8` | `74 01 00 b5` | cbnz x20,0x00c0bdf4 | `CONDITIONAL_JUMP`
<a id="insn-00c0bdcc"></a> `00c0bdcc` | `19 03 00 36` | tbz w25,#0x0,0x00c0be2c | `CONDITIONAL_JUMP`
<a id="insn-00c0bdd0"></a> `00c0bdd0` | `68 00 00 14` | b 0x00c0bf70 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bdd4"></a> `00c0bdd4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0bdd8"></a> `00c0bdd8` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c0bddc"></a> `00c0bddc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0bde0"></a> `00c0bde0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0bde4"></a> `00c0bde4` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bde8"></a> `00c0bde8` | `f9 17 9f 1a` | cset w25,eq | `FALL_THROUGH`
<a id="insn-00c0bdec"></a> `00c0bdec` | `f5 03 95 9a` | csel x21,xzr,x21,eq | `FALL_THROUGH`
<a id="insn-00c0bdf0"></a> `00c0bdf0` | `f4 fe ff b4` | cbz x20,0x00c0bdcc | `CONDITIONAL_JUMP`
<a id="insn-00c0bdf4"></a> `00c0bdf4` | `88 a6 41 a9` | ldp x8,x9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bdf8"></a> `00c0bdf8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c0bdfc"></a> `00c0bdfc` | `60 00 00 54` | b.eq 0x00c0be08 | `CONDITIONAL_JUMP`
<a id="insn-00c0be00"></a> `00c0be00` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00c0be04"></a> `00c0be04` | `05 00 00 14` | b 0x00c0be18 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0be08"></a> `00c0be08` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c0be0c"></a> `00c0be0c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c0be10"></a> `00c0be10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c0be14"></a> `00c0be14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0be18"></a> `00c0be18` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c0be1c"></a> `00c0be1c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00c0be20"></a> `00c0be20` | `f4 03 94 9a` | csel x20,xzr,x20,eq | `FALL_THROUGH`
<a id="insn-00c0be24"></a> `00c0be24` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00c0be28"></a> `00c0be28` | `40 0a 00 54` | b.eq 0x00c0bf70 | `CONDITIONAL_JUMP`
<a id="insn-00c0be2c"></a> `00c0be2c` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00c0be30"></a> `00c0be30` | `49 0b 40 f9` | ldr x9,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00c0be34"></a> `00c0be34` | `4b 03 40 f9` | ldr x11,[x26] | `FALL_THROUGH`
<a id="insn-00c0be38"></a> `00c0be38` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0be3c"></a> `00c0be3c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0be40"></a> `00c0be40` | `59 01 89 9a` | csel x25,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c0be44"></a> `00c0be44` | `09 03 19 8b` | add x9,x24,x25 | `FALL_THROUGH`
<a id="insn-00c0be48"></a> `00c0be48` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00c0be4c"></a> `00c0be4c` | `c1 05 00 54` | b.ne 0x00c0bf04 | `CONDITIONAL_JUMP`
<a id="insn-00c0be50"></a> `00c0be50` | `3f 07 00 f1` | cmp x25,#0x1 | `FALL_THROUGH`
<a id="insn-00c0be54"></a> `00c0be54` | `cb 00 00 54` | b.lt 0x00c0be6c | `CONDITIONAL_JUMP`
<a id="insn-00c0be58"></a> `00c0be58` | `a0 a3 02 d1` | sub x0,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00c0be5c"></a> `00c0be5c` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00c0be60"></a> `00c0be60` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00c0be64"></a> `00c0be64` | `03 40 01 94` | bl 0x00c5be70 | `UNCONDITIONAL_CALL`
<a id="insn-00c0be68"></a> `00c0be68` | `0a 00 00 14` | b 0x00c0be90 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0be6c"></a> `00c0be6c` | `29 fb 7f d3` | lsl x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00c0be70"></a> `00c0be70` | `a8 00 00 37` | tbnz w8,#0x0,0x00c0be84 | `CONDITIONAL_JUMP`
<a id="insn-00c0be74"></a> `00c0be74` | `28 79 1f 53` | lsl w8,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00c0be78"></a> `00c0be78` | `a8 83 15 38` | sturb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00c0be7c"></a> `00c0be7c` | `e8 03 1c aa` | mov x8,x28 | `FALL_THROUGH`
<a id="insn-00c0be80"></a> `00c0be80` | `03 00 00 14` | b 0x00c0be8c | `UNCONDITIONAL_JUMP`
<a id="insn-00c0be84"></a> `00c0be84` | `48 0f 40 f9` | ldr x8,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00c0be88"></a> `00c0be88` | `49 0b 00 f9` | str x9,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00c0be8c"></a> `00c0be8c` | `1f 69 29 38` | strb wzr,[x8, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00c0be90"></a> `00c0be90` | `49 ab 40 a9` | ldp x9,x10,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00c0be94"></a> `00c0be94` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00c0be98"></a> `00c0be98` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0be9c"></a> `00c0be9c` | `2b f9 7f 92` | and x11,x9,#-0x2 | `FALL_THROUGH`
<a id="insn-00c0bea0"></a> `00c0bea0` | `2c 1d 41 d3` | ubfx x12,x9,#0x1,#0x7 | `FALL_THROUGH`
<a id="insn-00c0bea4"></a> `00c0bea4` | `6b 05 00 d1` | sub x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bea8"></a> `00c0bea8` | `c8 02 8b 9a` | csel x8,x22,x11,eq | `FALL_THROUGH`
<a id="insn-00c0beac"></a> `00c0beac` | `3f 01 40 f2` | tst x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c0beb0"></a> `00c0beb0` | `8a 01 8a 9a` | csel x10,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00c0beb4"></a> `00c0beb4` | `01 01 0a eb` | subs x1,x8,x10 | `FALL_THROUGH`
<a id="insn-00c0beb8"></a> `00c0beb8` | `a9 00 00 54` | b.ls 0x00c0becc | `CONDITIONAL_JUMP`
<a id="insn-00c0bebc"></a> `00c0bebc` | `a0 a3 02 d1` | sub x0,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00c0bec0"></a> `00c0bec0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00c0bec4"></a> `00c0bec4` | `eb 3f 01 94` | bl 0x00c5be70 | `UNCONDITIONAL_CALL`
<a id="insn-00c0bec8"></a> `00c0bec8` | `09 00 00 14` | b 0x00c0beec | `UNCONDITIONAL_JUMP`
<a id="insn-00c0becc"></a> `00c0becc` | `a9 00 00 37` | tbnz w9,#0x0,0x00c0bee0 | `CONDITIONAL_JUMP`
<a id="insn-00c0bed0"></a> `00c0bed0` | `09 79 1f 53` | lsl w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bed4"></a> `00c0bed4` | `a9 83 15 38` | sturb w9,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00c0bed8"></a> `00c0bed8` | `e9 03 1c aa` | mov x9,x28 | `FALL_THROUGH`
<a id="insn-00c0bedc"></a> `00c0bedc` | `03 00 00 14` | b 0x00c0bee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bee0"></a> `00c0bee0` | `49 0f 40 f9` | ldr x9,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bee4"></a> `00c0bee4` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00c0bee8"></a> `00c0bee8` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c0beec"></a> `00c0beec` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00c0bef0"></a> `00c0bef0` | `49 0f 40 f9` | ldr x9,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bef4"></a> `00c0bef4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bef8"></a> `00c0bef8` | `98 03 89 9a` | csel x24,x28,x9,eq | `FALL_THROUGH`
<a id="insn-00c0befc"></a> `00c0befc` | `08 03 19 8b` | add x8,x24,x25 | `FALL_THROUGH`
<a id="insn-00c0bf00"></a> `00c0bf00` | `48 03 00 f9` | str x8,[x26] | `FALL_THROUGH`
<a id="insn-00c0bf04"></a> `00c0bf04` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bf08"></a> `00c0bf08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c0bf0c"></a> `00c0bf0c` | `60 00 00 54` | b.eq 0x00c0bf18 | `CONDITIONAL_JUMP`
<a id="insn-00c0bf10"></a> `00c0bf10` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00c0bf14"></a> `00c0bf14` | `05 00 00 14` | b 0x00c0bf28 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bf18"></a> `00c0bf18` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0bf1c"></a> `00c0bf1c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c0bf20"></a> `00c0bf20` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0bf24"></a> `00c0bf24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0bf28"></a> `00c0bf28` | `a5 43 5f b8` | ldur w5,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00c0bf2c"></a> `00c0bf2c` | `a3 c3 02 d1` | sub x3,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-00c0bf30"></a> `00c0bf30` | `e4 93 00 91` | add x4,sp,#0x24 | `FALL_THROUGH`
<a id="insn-00c0bf34"></a> `00c0bf34` | `a6 43 02 d1` | sub x6,x29,#0x90 | `FALL_THROUGH`
<a id="insn-00c0bf38"></a> `00c0bf38` | `e7 c3 00 91` | add x7,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00c0bf3c"></a> `00c0bf3c` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00c0bf40"></a> `00c0bf40` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00c0bf44"></a> `00c0bf44` | `f3 6f 00 a9` | stp x19,x27,[sp] | `FALL_THROUGH`
<a id="insn-00c0bf48"></a> `00c0bf48` | `96 49 01 94` | bl 0x00c5e5a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0bf4c"></a> `00c0bf4c` | `20 01 00 35` | cbnz w0,0x00c0bf70 | `CONDITIONAL_JUMP`
<a id="insn-00c0bf50"></a> `00c0bf50` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bf54"></a> `00c0bf54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c0bf58"></a> `00c0bf58` | `61 f2 ff 54` | b.ne 0x00c0bda4 | `CONDITIONAL_JUMP`
<a id="insn-00c0bf5c"></a> `00c0bf5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0bf60"></a> `00c0bf60` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00c0bf64"></a> `00c0bf64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0bf68"></a> `00c0bf68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0bf6c"></a> `00c0bf6c` | `90 ff ff 17` | b 0x00c0bdac | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bf70"></a> `00c0bf70` | `a8 03 57 38` | ldurb w8,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00c0bf74"></a> `00c0bf74` | `49 17 40 f9` | ldr x9,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00c0bf78"></a> `00c0bf78` | `f6 0f 40 f9` | ldr x22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bf7c"></a> `00c0bf7c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bf80"></a> `00c0bf80` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bf84"></a> `00c0bf84` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c0bf88"></a> `00c0bf88` | `28 01 00 b4` | cbz x8,0x00c0bfac | `CONDITIONAL_JUMP`
<a id="insn-00c0bf8c"></a> `00c0bf8c` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00c0bf90"></a> `00c0bf90` | `e9 c3 00 91` | add x9,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00c0bf94"></a> `00c0bf94` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00c0bf98"></a> `00c0bf98` | `3f 7d 02 f1` | cmp x9,#0x9f | `FALL_THROUGH`
<a id="insn-00c0bf9c"></a> `00c0bf9c` | `8c 00 00 54` | b.gt 0x00c0bfac | `CONDITIONAL_JUMP`
<a id="insn-00c0bfa0"></a> `00c0bfa0` | `e9 27 40 b9` | ldr w9,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00c0bfa4"></a> `00c0bfa4` | `09 45 00 b8` | str w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00c0bfa8"></a> `00c0bfa8` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00c0bfac"></a> `00c0bfac` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00c0bfb0"></a> `00c0bfb0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00c0bfb4"></a> `00c0bfb4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00c0bfb8"></a> `00c0bfb8` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-00c0bfbc"></a> `00c0bfbc` | `00 a9 00 94` | bl 0x00c363bc | `UNCONDITIONAL_CALL`
<a id="insn-00c0bfc0"></a> `00c0bfc0` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0bfc4"></a> `00c0bfc4` | `e2 17 40 f9` | ldr x2,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00c0bfc8"></a> `00c0bfc8` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00c0bfcc"></a> `00c0bfcc` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00c0bfd0"></a> `00c0bfd0` | `00 01 00 79` | strh w0,[x8] | `FALL_THROUGH`
<a id="insn-00c0bfd4"></a> `00c0bfd4` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-00c0bfd8"></a> `00c0bfd8` | `5a 49 01 94` | bl 0x00c5e540 | `UNCONDITIONAL_CALL`
<a id="insn-00c0bfdc"></a> `00c0bfdc` | `d5 00 00 b4` | cbz x21,0x00c0bff4 | `CONDITIONAL_JUMP`
<a id="insn-00c0bfe0"></a> `00c0bfe0` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00c0bfe4"></a> `00c0bfe4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c0bfe8"></a> `00c0bfe8` | `e0 00 00 54` | b.eq 0x00c0c004 | `CONDITIONAL_JUMP`
<a id="insn-00c0bfec"></a> `00c0bfec` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00c0bff0"></a> `00c0bff0` | `09 00 00 14` | b 0x00c0c014 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0bff4"></a> `00c0bff4` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00c0bff8"></a> `00c0bff8` | `74 01 00 b5` | cbnz x20,0x00c0c024 | `CONDITIONAL_JUMP`
<a id="insn-00c0bffc"></a> `00c0bffc` | `f3 02 00 37` | tbnz w19,#0x0,0x00c0c058 | `CONDITIONAL_JUMP`
<a id="insn-00c0c000"></a> `00c0c000` | `19 00 00 14` | b 0x00c0c064 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0c004"></a> `00c0c004` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0c008"></a> `00c0c008` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c0c00c"></a> `00c0c00c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0c010"></a> `00c0c010` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0c014"></a> `00c0c014` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c0c018"></a> `00c0c018` | `f3 17 9f 1a` | cset w19,eq | `FALL_THROUGH`
<a id="insn-00c0c01c"></a> `00c0c01c` | `f5 03 95 9a` | csel x21,xzr,x21,eq | `FALL_THROUGH`
<a id="insn-00c0c020"></a> `00c0c020` | `f4 fe ff b4` | cbz x20,0x00c0bffc | `CONDITIONAL_JUMP`
<a id="insn-00c0c024"></a> `00c0c024` | `88 a6 41 a9` | ldp x8,x9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c0c028"></a> `00c0c028` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c0c02c"></a> `00c0c02c` | `60 00 00 54` | b.eq 0x00c0c038 | `CONDITIONAL_JUMP`
<a id="insn-00c0c030"></a> `00c0c030` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00c0c034"></a> `00c0c034` | `05 00 00 14` | b 0x00c0c048 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0c038"></a> `00c0c038` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c0c03c"></a> `00c0c03c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c0c040"></a> `00c0c040` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c0c044"></a> `00c0c044` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0c048"></a> `00c0c048` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c0c04c"></a> `00c0c04c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00c0c050"></a> `00c0c050` | `68 02 08 4a` | eor w8,w19,w8 | `FALL_THROUGH`
<a id="insn-00c0c054"></a> `00c0c054` | `88 00 00 37` | tbnz w8,#0x0,0x00c0c064 | `CONDITIONAL_JUMP`
<a id="insn-00c0c058"></a> `00c0c058` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00c0c05c"></a> `00c0c05c` | `08 01 1f 32` | orr w8,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00c0c060"></a> `00c0c060` | `c8 02 00 b9` | str w8,[x22] | `FALL_THROUGH`
<a id="insn-00c0c064"></a> `00c0c064` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00c0c068"></a> `00c0c068` | `68 00 00 36` | tbz w8,#0x0,0x00c0c074 | `CONDITIONAL_JUMP`
<a id="insn-00c0c06c"></a> `00c0c06c` | `40 0f 40 f9` | ldr x0,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00c0c070"></a> `00c0c070` | `90 2f 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0c074"></a> `00c0c074` | `a8 03 57 38` | ldurb w8,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00c0c078"></a> `00c0c078` | `68 00 00 36` | tbz w8,#0x0,0x00c0c084 | `CONDITIONAL_JUMP`
<a id="insn-00c0c07c"></a> `00c0c07c` | `40 1b 40 f9` | ldr x0,[x26, #0x30] | `FALL_THROUGH`
<a id="insn-00c0c080"></a> `00c0c080` | `8c 2f 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0c084"></a> `00c0c084` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0c088"></a> `00c0c088` | `f4 4f 5d a9` | ldp x20,x19,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00c0c08c"></a> `00c0c08c` | `f6 57 5c a9` | ldp x22,x21,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00c0c090"></a> `00c0c090` | `f8 5f 5b a9` | ldp x24,x23,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00c0c094"></a> `00c0c094` | `fa 67 5a a9` | ldp x26,x25,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00c0c098"></a> `00c0c098` | `fc 6f 59 a9` | ldp x28,x27,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00c0c09c"></a> `00c0c09c` | `fd 7b 58 a9` | ldp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00c0c0a0"></a> `00c0c0a0` | `ff 83 07 91` | add sp,sp,#0x1e0 | `FALL_THROUGH`
<a id="insn-00c0c0a4"></a> `00c0c0a4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c0c0a8"></a> `00c0c0a8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c0bccc`](#insn-00c0bccc) 範囲 `[['00c0bccc', '00c0bcff']]`
  - `FALL_THROUGH` [`00c0bcfc`](#insn-00c0bcfc) → [`00c0bd00`](#insn-00c0bd00)
- ブロック [`00c0bd00`](#insn-00c0bd00) 範囲 `[['00c0bd00', '00c0bd13']]`
  - `CONDITIONAL_JUMP` [`00c0bd10`](#insn-00c0bd10) → [`00c0bd34`](#insn-00c0bd34)
  - `FALL_THROUGH` [`00c0bd10`](#insn-00c0bd10) → [`00c0bd14`](#insn-00c0bd14)
- ブロック [`00c0bd14`](#insn-00c0bd14) 範囲 `[['00c0bd14', '00c0bd1b']]`
  - `CONDITIONAL_JUMP` [`00c0bd18`](#insn-00c0bd18) → [`00c0bd2c`](#insn-00c0bd2c)
  - `FALL_THROUGH` [`00c0bd18`](#insn-00c0bd18) → [`00c0bd1c`](#insn-00c0bd1c)
- ブロック [`00c0bd1c`](#insn-00c0bd1c) 範囲 `[['00c0bd1c', '00c0bd23']]`
  - `CONDITIONAL_JUMP` [`00c0bd20`](#insn-00c0bd20) → [`00c0bd3c`](#insn-00c0bd3c)
  - `FALL_THROUGH` [`00c0bd20`](#insn-00c0bd20) → [`00c0bd24`](#insn-00c0bd24)
- ブロック [`00c0bd24`](#insn-00c0bd24) 範囲 `[['00c0bd24', '00c0bd2b']]`
  - `UNCONDITIONAL_JUMP` [`00c0bd28`](#insn-00c0bd28) → [`00c0bd40`](#insn-00c0bd40)
- ブロック [`00c0bd2c`](#insn-00c0bd2c) 範囲 `[['00c0bd2c', '00c0bd33']]`
  - `UNCONDITIONAL_JUMP` [`00c0bd30`](#insn-00c0bd30) → [`00c0bd40`](#insn-00c0bd40)
- ブロック [`00c0bd34`](#insn-00c0bd34) 範囲 `[['00c0bd34', '00c0bd3b']]`
  - `UNCONDITIONAL_JUMP` [`00c0bd38`](#insn-00c0bd38) → [`00c0bd40`](#insn-00c0bd40)
- ブロック [`00c0bd3c`](#insn-00c0bd3c) 範囲 `[['00c0bd3c', '00c0bd3f']]`
  - `FALL_THROUGH` [`00c0bd3c`](#insn-00c0bd3c) → [`00c0bd40`](#insn-00c0bd40)
- ブロック [`00c0bd40`](#insn-00c0bd40) 範囲 `[['00c0bd40', '00c0bda3']]`
  - `UNCONDITIONAL_JUMP` [`00c0bda0`](#insn-00c0bda0) → [`00c0bdac`](#insn-00c0bdac)
- ブロック [`00c0bda4`](#insn-00c0bda4) 範囲 `[['00c0bda4', '00c0bdab']]`
  - `FALL_THROUGH` [`00c0bda8`](#insn-00c0bda8) → [`00c0bdac`](#insn-00c0bdac)
- ブロック [`00c0bdac`](#insn-00c0bdac) 範囲 `[['00c0bdac', '00c0bdaf']]`
  - `CONDITIONAL_JUMP` [`00c0bdac`](#insn-00c0bdac) → [`00c0bdc4`](#insn-00c0bdc4)
  - `FALL_THROUGH` [`00c0bdac`](#insn-00c0bdac) → [`00c0bdb0`](#insn-00c0bdb0)
- ブロック [`00c0bdb0`](#insn-00c0bdb0) 範囲 `[['00c0bdb0', '00c0bdbb']]`
  - `CONDITIONAL_JUMP` [`00c0bdb8`](#insn-00c0bdb8) → [`00c0bdd4`](#insn-00c0bdd4)
  - `FALL_THROUGH` [`00c0bdb8`](#insn-00c0bdb8) → [`00c0bdbc`](#insn-00c0bdbc)
- ブロック [`00c0bdbc`](#insn-00c0bdbc) 範囲 `[['00c0bdbc', '00c0bdc3']]`
  - `UNCONDITIONAL_JUMP` [`00c0bdc0`](#insn-00c0bdc0) → [`00c0bde4`](#insn-00c0bde4)
- ブロック [`00c0bdc4`](#insn-00c0bdc4) 範囲 `[['00c0bdc4', '00c0bdcb']]`
  - `CONDITIONAL_JUMP` [`00c0bdc8`](#insn-00c0bdc8) → [`00c0bdf4`](#insn-00c0bdf4)
  - `FALL_THROUGH` [`00c0bdc8`](#insn-00c0bdc8) → [`00c0bdcc`](#insn-00c0bdcc)
- ブロック [`00c0bdcc`](#insn-00c0bdcc) 範囲 `[['00c0bdcc', '00c0bdcf']]`
  - `CONDITIONAL_JUMP` [`00c0bdcc`](#insn-00c0bdcc) → [`00c0be2c`](#insn-00c0be2c)
  - `FALL_THROUGH` [`00c0bdcc`](#insn-00c0bdcc) → [`00c0bdd0`](#insn-00c0bdd0)
- ブロック [`00c0bdd0`](#insn-00c0bdd0) 範囲 `[['00c0bdd0', '00c0bdd3']]`
  - `UNCONDITIONAL_JUMP` [`00c0bdd0`](#insn-00c0bdd0) → [`00c0bf70`](#insn-00c0bf70)
- ブロック [`00c0bdd4`](#insn-00c0bdd4) 範囲 `[['00c0bdd4', '00c0bde3']]`
  - `FALL_THROUGH` [`00c0bde0`](#insn-00c0bde0) → [`00c0bde4`](#insn-00c0bde4)
- ブロック [`00c0bde4`](#insn-00c0bde4) 範囲 `[['00c0bde4', '00c0bdf3']]`
  - `CONDITIONAL_JUMP` [`00c0bdf0`](#insn-00c0bdf0) → [`00c0bdcc`](#insn-00c0bdcc)
  - `FALL_THROUGH` [`00c0bdf0`](#insn-00c0bdf0) → [`00c0bdf4`](#insn-00c0bdf4)
- ブロック [`00c0bdf4`](#insn-00c0bdf4) 範囲 `[['00c0bdf4', '00c0bdff']]`
  - `CONDITIONAL_JUMP` [`00c0bdfc`](#insn-00c0bdfc) → [`00c0be08`](#insn-00c0be08)
  - `FALL_THROUGH` [`00c0bdfc`](#insn-00c0bdfc) → [`00c0be00`](#insn-00c0be00)
- ブロック [`00c0be00`](#insn-00c0be00) 範囲 `[['00c0be00', '00c0be07']]`
  - `UNCONDITIONAL_JUMP` [`00c0be04`](#insn-00c0be04) → [`00c0be18`](#insn-00c0be18)
- ブロック [`00c0be08`](#insn-00c0be08) 範囲 `[['00c0be08', '00c0be17']]`
  - `FALL_THROUGH` [`00c0be14`](#insn-00c0be14) → [`00c0be18`](#insn-00c0be18)
- ブロック [`00c0be18`](#insn-00c0be18) 範囲 `[['00c0be18', '00c0be2b']]`
  - `CONDITIONAL_JUMP` [`00c0be28`](#insn-00c0be28) → [`00c0bf70`](#insn-00c0bf70)
  - `FALL_THROUGH` [`00c0be28`](#insn-00c0be28) → [`00c0be2c`](#insn-00c0be2c)
- ブロック [`00c0be2c`](#insn-00c0be2c) 範囲 `[['00c0be2c', '00c0be4f']]`
  - `CONDITIONAL_JUMP` [`00c0be4c`](#insn-00c0be4c) → [`00c0bf04`](#insn-00c0bf04)
  - `FALL_THROUGH` [`00c0be4c`](#insn-00c0be4c) → [`00c0be50`](#insn-00c0be50)
- ブロック [`00c0be50`](#insn-00c0be50) 範囲 `[['00c0be50', '00c0be57']]`
  - `CONDITIONAL_JUMP` [`00c0be54`](#insn-00c0be54) → [`00c0be6c`](#insn-00c0be6c)
  - `FALL_THROUGH` [`00c0be54`](#insn-00c0be54) → [`00c0be58`](#insn-00c0be58)
- ブロック [`00c0be58`](#insn-00c0be58) 範囲 `[['00c0be58', '00c0be6b']]`
  - `UNCONDITIONAL_JUMP` [`00c0be68`](#insn-00c0be68) → [`00c0be90`](#insn-00c0be90)
- ブロック [`00c0be6c`](#insn-00c0be6c) 範囲 `[['00c0be6c', '00c0be73']]`
  - `CONDITIONAL_JUMP` [`00c0be70`](#insn-00c0be70) → [`00c0be84`](#insn-00c0be84)
  - `FALL_THROUGH` [`00c0be70`](#insn-00c0be70) → [`00c0be74`](#insn-00c0be74)
- ブロック [`00c0be74`](#insn-00c0be74) 範囲 `[['00c0be74', '00c0be83']]`
  - `UNCONDITIONAL_JUMP` [`00c0be80`](#insn-00c0be80) → [`00c0be8c`](#insn-00c0be8c)
- ブロック [`00c0be84`](#insn-00c0be84) 範囲 `[['00c0be84', '00c0be8b']]`
  - `FALL_THROUGH` [`00c0be88`](#insn-00c0be88) → [`00c0be8c`](#insn-00c0be8c)
- ブロック [`00c0be8c`](#insn-00c0be8c) 範囲 `[['00c0be8c', '00c0be8f']]`
  - `FALL_THROUGH` [`00c0be8c`](#insn-00c0be8c) → [`00c0be90`](#insn-00c0be90)
- ブロック [`00c0be90`](#insn-00c0be90) 範囲 `[['00c0be90', '00c0bebb']]`
  - `CONDITIONAL_JUMP` [`00c0beb8`](#insn-00c0beb8) → [`00c0becc`](#insn-00c0becc)
  - `FALL_THROUGH` [`00c0beb8`](#insn-00c0beb8) → [`00c0bebc`](#insn-00c0bebc)
- ブロック [`00c0bebc`](#insn-00c0bebc) 範囲 `[['00c0bebc', '00c0becb']]`
  - `UNCONDITIONAL_JUMP` [`00c0bec8`](#insn-00c0bec8) → [`00c0beec`](#insn-00c0beec)
- ブロック [`00c0becc`](#insn-00c0becc) 範囲 `[['00c0becc', '00c0becf']]`
  - `CONDITIONAL_JUMP` [`00c0becc`](#insn-00c0becc) → [`00c0bee0`](#insn-00c0bee0)
  - `FALL_THROUGH` [`00c0becc`](#insn-00c0becc) → [`00c0bed0`](#insn-00c0bed0)
- ブロック [`00c0bed0`](#insn-00c0bed0) 範囲 `[['00c0bed0', '00c0bedf']]`
  - `UNCONDITIONAL_JUMP` [`00c0bedc`](#insn-00c0bedc) → [`00c0bee8`](#insn-00c0bee8)
- ブロック [`00c0bee0`](#insn-00c0bee0) 範囲 `[['00c0bee0', '00c0bee7']]`
  - `FALL_THROUGH` [`00c0bee4`](#insn-00c0bee4) → [`00c0bee8`](#insn-00c0bee8)
- ブロック [`00c0bee8`](#insn-00c0bee8) 範囲 `[['00c0bee8', '00c0beeb']]`
  - `FALL_THROUGH` [`00c0bee8`](#insn-00c0bee8) → [`00c0beec`](#insn-00c0beec)
- ブロック [`00c0beec`](#insn-00c0beec) 範囲 `[['00c0beec', '00c0bf03']]`
  - `FALL_THROUGH` [`00c0bf00`](#insn-00c0bf00) → [`00c0bf04`](#insn-00c0bf04)
- ブロック [`00c0bf04`](#insn-00c0bf04) 範囲 `[['00c0bf04', '00c0bf0f']]`
  - `CONDITIONAL_JUMP` [`00c0bf0c`](#insn-00c0bf0c) → [`00c0bf18`](#insn-00c0bf18)
  - `FALL_THROUGH` [`00c0bf0c`](#insn-00c0bf0c) → [`00c0bf10`](#insn-00c0bf10)
- ブロック [`00c0bf10`](#insn-00c0bf10) 範囲 `[['00c0bf10', '00c0bf17']]`
  - `UNCONDITIONAL_JUMP` [`00c0bf14`](#insn-00c0bf14) → [`00c0bf28`](#insn-00c0bf28)
- ブロック [`00c0bf18`](#insn-00c0bf18) 範囲 `[['00c0bf18', '00c0bf27']]`
  - `FALL_THROUGH` [`00c0bf24`](#insn-00c0bf24) → [`00c0bf28`](#insn-00c0bf28)
- ブロック [`00c0bf28`](#insn-00c0bf28) 範囲 `[['00c0bf28', '00c0bf4f']]`
  - `CONDITIONAL_JUMP` [`00c0bf4c`](#insn-00c0bf4c) → [`00c0bf70`](#insn-00c0bf70)
  - `FALL_THROUGH` [`00c0bf4c`](#insn-00c0bf4c) → [`00c0bf50`](#insn-00c0bf50)
- ブロック [`00c0bf50`](#insn-00c0bf50) 範囲 `[['00c0bf50', '00c0bf5b']]`
  - `CONDITIONAL_JUMP` [`00c0bf58`](#insn-00c0bf58) → [`00c0bda4`](#insn-00c0bda4)
  - `FALL_THROUGH` [`00c0bf58`](#insn-00c0bf58) → [`00c0bf5c`](#insn-00c0bf5c)
- ブロック [`00c0bf5c`](#insn-00c0bf5c) 範囲 `[['00c0bf5c', '00c0bf6f']]`
  - `UNCONDITIONAL_JUMP` [`00c0bf6c`](#insn-00c0bf6c) → [`00c0bdac`](#insn-00c0bdac)
- ブロック [`00c0bf70`](#insn-00c0bf70) 範囲 `[['00c0bf70', '00c0bf8b']]`
  - `CONDITIONAL_JUMP` [`00c0bf88`](#insn-00c0bf88) → [`00c0bfac`](#insn-00c0bfac)
  - `FALL_THROUGH` [`00c0bf88`](#insn-00c0bf88) → [`00c0bf8c`](#insn-00c0bf8c)
- ブロック [`00c0bf8c`](#insn-00c0bf8c) 範囲 `[['00c0bf8c', '00c0bf9f']]`
  - `CONDITIONAL_JUMP` [`00c0bf9c`](#insn-00c0bf9c) → [`00c0bfac`](#insn-00c0bfac)
  - `FALL_THROUGH` [`00c0bf9c`](#insn-00c0bf9c) → [`00c0bfa0`](#insn-00c0bfa0)
- ブロック [`00c0bfa0`](#insn-00c0bfa0) 範囲 `[['00c0bfa0', '00c0bfab']]`
  - `FALL_THROUGH` [`00c0bfa8`](#insn-00c0bfa8) → [`00c0bfac`](#insn-00c0bfac)
- ブロック [`00c0bfac`](#insn-00c0bfac) 範囲 `[['00c0bfac', '00c0bfdf']]`
  - `CONDITIONAL_JUMP` [`00c0bfdc`](#insn-00c0bfdc) → [`00c0bff4`](#insn-00c0bff4)
  - `FALL_THROUGH` [`00c0bfdc`](#insn-00c0bfdc) → [`00c0bfe0`](#insn-00c0bfe0)
- ブロック [`00c0bfe0`](#insn-00c0bfe0) 範囲 `[['00c0bfe0', '00c0bfeb']]`
  - `CONDITIONAL_JUMP` [`00c0bfe8`](#insn-00c0bfe8) → [`00c0c004`](#insn-00c0c004)
  - `FALL_THROUGH` [`00c0bfe8`](#insn-00c0bfe8) → [`00c0bfec`](#insn-00c0bfec)
- ブロック [`00c0bfec`](#insn-00c0bfec) 範囲 `[['00c0bfec', '00c0bff3']]`
  - `UNCONDITIONAL_JUMP` [`00c0bff0`](#insn-00c0bff0) → [`00c0c014`](#insn-00c0c014)
- ブロック [`00c0bff4`](#insn-00c0bff4) 範囲 `[['00c0bff4', '00c0bffb']]`
  - `CONDITIONAL_JUMP` [`00c0bff8`](#insn-00c0bff8) → [`00c0c024`](#insn-00c0c024)
  - `FALL_THROUGH` [`00c0bff8`](#insn-00c0bff8) → [`00c0bffc`](#insn-00c0bffc)
- ブロック [`00c0bffc`](#insn-00c0bffc) 範囲 `[['00c0bffc', '00c0bfff']]`
  - `CONDITIONAL_JUMP` [`00c0bffc`](#insn-00c0bffc) → [`00c0c058`](#insn-00c0c058)
  - `FALL_THROUGH` [`00c0bffc`](#insn-00c0bffc) → [`00c0c000`](#insn-00c0c000)
- ブロック [`00c0c000`](#insn-00c0c000) 範囲 `[['00c0c000', '00c0c003']]`
  - `UNCONDITIONAL_JUMP` [`00c0c000`](#insn-00c0c000) → [`00c0c064`](#insn-00c0c064)
- ブロック [`00c0c004`](#insn-00c0c004) 範囲 `[['00c0c004', '00c0c013']]`
  - `FALL_THROUGH` [`00c0c010`](#insn-00c0c010) → [`00c0c014`](#insn-00c0c014)
- ブロック [`00c0c014`](#insn-00c0c014) 範囲 `[['00c0c014', '00c0c023']]`
  - `CONDITIONAL_JUMP` [`00c0c020`](#insn-00c0c020) → [`00c0bffc`](#insn-00c0bffc)
  - `FALL_THROUGH` [`00c0c020`](#insn-00c0c020) → [`00c0c024`](#insn-00c0c024)
- ブロック [`00c0c024`](#insn-00c0c024) 範囲 `[['00c0c024', '00c0c02f']]`
  - `CONDITIONAL_JUMP` [`00c0c02c`](#insn-00c0c02c) → [`00c0c038`](#insn-00c0c038)
  - `FALL_THROUGH` [`00c0c02c`](#insn-00c0c02c) → [`00c0c030`](#insn-00c0c030)
- ブロック [`00c0c030`](#insn-00c0c030) 範囲 `[['00c0c030', '00c0c037']]`
  - `UNCONDITIONAL_JUMP` [`00c0c034`](#insn-00c0c034) → [`00c0c048`](#insn-00c0c048)
- ブロック [`00c0c038`](#insn-00c0c038) 範囲 `[['00c0c038', '00c0c047']]`
  - `FALL_THROUGH` [`00c0c044`](#insn-00c0c044) → [`00c0c048`](#insn-00c0c048)
- ブロック [`00c0c048`](#insn-00c0c048) 範囲 `[['00c0c048', '00c0c057']]`
  - `CONDITIONAL_JUMP` [`00c0c054`](#insn-00c0c054) → [`00c0c064`](#insn-00c0c064)
  - `FALL_THROUGH` [`00c0c054`](#insn-00c0c054) → [`00c0c058`](#insn-00c0c058)
- ブロック [`00c0c058`](#insn-00c0c058) 範囲 `[['00c0c058', '00c0c063']]`
  - `FALL_THROUGH` [`00c0c060`](#insn-00c0c060) → [`00c0c064`](#insn-00c0c064)
- ブロック [`00c0c064`](#insn-00c0c064) 範囲 `[['00c0c064', '00c0c06b']]`
  - `CONDITIONAL_JUMP` [`00c0c068`](#insn-00c0c068) → [`00c0c074`](#insn-00c0c074)
  - `FALL_THROUGH` [`00c0c068`](#insn-00c0c068) → [`00c0c06c`](#insn-00c0c06c)
- ブロック [`00c0c06c`](#insn-00c0c06c) 範囲 `[['00c0c06c', '00c0c073']]`
  - `FALL_THROUGH` [`00c0c070`](#insn-00c0c070) → [`00c0c074`](#insn-00c0c074)
- ブロック [`00c0c074`](#insn-00c0c074) 範囲 `[['00c0c074', '00c0c07b']]`
  - `CONDITIONAL_JUMP` [`00c0c078`](#insn-00c0c078) → [`00c0c084`](#insn-00c0c084)
  - `FALL_THROUGH` [`00c0c078`](#insn-00c0c078) → [`00c0c07c`](#insn-00c0c07c)
- ブロック [`00c0c07c`](#insn-00c0c07c) 範囲 `[['00c0c07c', '00c0c083']]`
  - `FALL_THROUGH` [`00c0c080`](#insn-00c0c080) → [`00c0c084`](#insn-00c0c084)
- ブロック [`00c0c084`](#insn-00c0c084) 範囲 `[['00c0c084', '00c0c097']]`
  - `FALL_THROUGH` [`00c0c094`](#insn-00c0c094) → [`00c0c098`](#insn-00c0c098)
- ブロック [`00c0c098`](#insn-00c0c098) 範囲 `[['00c0c098', '00c0c0a7']]`
  - `FALL_THROUGH` [`00c0c0a4`](#insn-00c0c0a4) → [`00c0c0a8`](#insn-00c0c0a8)
- ブロック [`00c0c0a8`](#insn-00c0c0a8) 範囲 `[['00c0c0a8', '00c0c0ab']]`

## 命令位置別の参照

- [`00c0bcd4`](#insn-00c0bcd4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bcd8`](#insn-00c0bcd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bcdc`](#insn-00c0bcdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bce0`](#insn-00c0bce0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bce4`](#insn-00c0bce4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bce8`](#insn-00c0bce8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd0c`](#insn-00c0bd0c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd10`](#insn-00c0bd10) → [`00c0bd34`](#insn-00c0bd34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd18`](#insn-00c0bd18) → [`00c0bd2c`](#insn-00c0bd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd20`](#insn-00c0bd20) → [`00c0bd3c`](#insn-00c0bd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd28`](#insn-00c0bd28) → [`00c0bd40`](#insn-00c0bd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd30`](#insn-00c0bd30) → [`00c0bd40`](#insn-00c0bd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd38`](#insn-00c0bd38) → [`00c0bd40`](#insn-00c0bd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd4c`](#insn-00c0bd4c) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd54`](#insn-00c0bd54) → [`00c5e590`](../00c5e/00c5e590.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e590` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd58`](#insn-00c0bd58) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd5c`](#insn-00c0bd5c) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd70`](#insn-00c0bd70) → [`00c5be70`](../00c5b/00c5be70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be70` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd74`](#insn-00c0bd74) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd78`](#insn-00c0bd78) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd88`](#insn-00c0bd88) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd90`](#insn-00c0bd90) → `Stack[-0x1bc]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bd9c`](#insn-00c0bd9c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bda0`](#insn-00c0bda0) → [`00c0bdac`](#insn-00c0bdac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdac`](#insn-00c0bdac) → [`00c0bdc4`](#insn-00c0bdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdb8`](#insn-00c0bdb8) → [`00c0bdd4`](#insn-00c0bdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdc0`](#insn-00c0bdc0) → [`00c0bde4`](#insn-00c0bde4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdc8`](#insn-00c0bdc8) → [`00c0bdf4`](#insn-00c0bdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdcc`](#insn-00c0bdcc) → [`00c0be2c`](#insn-00c0be2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdd0`](#insn-00c0bdd0) → [`00c0bf70`](#insn-00c0bf70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdf0`](#insn-00c0bdf0) → [`00c0bdcc`](#insn-00c0bdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bdfc`](#insn-00c0bdfc) → [`00c0be08`](#insn-00c0be08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be04`](#insn-00c0be04) → [`00c0be18`](#insn-00c0be18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be28`](#insn-00c0be28) → [`00c0bf70`](#insn-00c0bf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be2c`](#insn-00c0be2c) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be30`](#insn-00c0be30) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be34`](#insn-00c0be34) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be4c`](#insn-00c0be4c) → [`00c0bf04`](#insn-00c0bf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be54`](#insn-00c0be54) → [`00c0be6c`](#insn-00c0be6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be64`](#insn-00c0be64) → [`00c5be70`](../00c5b/00c5be70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be70` · 推定シンボル `None` · 推定型 `None`
- [`00c0be68`](#insn-00c0be68) → [`00c0be90`](#insn-00c0be90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be70`](#insn-00c0be70) → [`00c0be84`](#insn-00c0be84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be78`](#insn-00c0be78) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be80`](#insn-00c0be80) → [`00c0be8c`](#insn-00c0be8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be84`](#insn-00c0be84) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be88`](#insn-00c0be88) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be90`](#insn-00c0be90) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0be94`](#insn-00c0be94) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0beb8`](#insn-00c0beb8) → [`00c0becc`](#insn-00c0becc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bec4`](#insn-00c0bec4) → [`00c5be70`](../00c5b/00c5be70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be70` · 推定シンボル `None` · 推定型 `None`
- [`00c0bec8`](#insn-00c0bec8) → [`00c0beec`](#insn-00c0beec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0becc`](#insn-00c0becc) → [`00c0bee0`](#insn-00c0bee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bed4`](#insn-00c0bed4) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bedc`](#insn-00c0bedc) → [`00c0bee8`](#insn-00c0bee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bee0`](#insn-00c0bee0) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bee4`](#insn-00c0bee4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0beec`](#insn-00c0beec) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bef0`](#insn-00c0bef0) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf00`](#insn-00c0bf00) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf0c`](#insn-00c0bf0c) → [`00c0bf18`](#insn-00c0bf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf14`](#insn-00c0bf14) → [`00c0bf28`](#insn-00c0bf28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf28`](#insn-00c0bf28) → `Stack[-0x6c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf44`](#insn-00c0bf44) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf48`](#insn-00c0bf48) → [`00c5e5a0`](../00c5e/00c5e5a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e5a0` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf4c`](#insn-00c0bf4c) → [`00c0bf70`](#insn-00c0bf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf58`](#insn-00c0bf58) → [`00c0bda4`](#insn-00c0bda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf6c`](#insn-00c0bf6c) → [`00c0bdac`](#insn-00c0bdac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf70`](#insn-00c0bf70) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf74`](#insn-00c0bf74) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf78`](#insn-00c0bf78) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf88`](#insn-00c0bf88) → [`00c0bfac`](#insn-00c0bfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf8c`](#insn-00c0bf8c) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bf9c`](#insn-00c0bf9c) → [`00c0bfac`](#insn-00c0bfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfa0`](#insn-00c0bfa0) → `Stack[-0x1bc]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfa8`](#insn-00c0bfa8) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfac`](#insn-00c0bfac) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfbc`](#insn-00c0bfbc) → [`00c363bc`](../00c36/00c363bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c363bc` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfc0`](#insn-00c0bfc0) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfc4`](#insn-00c0bfc4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfd8`](#insn-00c0bfd8) → [`00c5e540`](../00c5e/00c5e540.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e540` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfdc`](#insn-00c0bfdc) → [`00c0bff4`](#insn-00c0bff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bfe8`](#insn-00c0bfe8) → [`00c0c004`](#insn-00c0c004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bff0`](#insn-00c0bff0) → [`00c0c014`](#insn-00c0c014) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bff8`](#insn-00c0bff8) → [`00c0c024`](#insn-00c0c024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0bffc`](#insn-00c0bffc) → [`00c0c058`](#insn-00c0c058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c000`](#insn-00c0c000) → [`00c0c064`](#insn-00c0c064) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c020`](#insn-00c0c020) → [`00c0bffc`](#insn-00c0bffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c02c`](#insn-00c0c02c) → [`00c0c038`](#insn-00c0c038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c034`](#insn-00c0c034) → [`00c0c048`](#insn-00c0c048) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c054`](#insn-00c0c054) → [`00c0c064`](#insn-00c0c064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c064`](#insn-00c0c064) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c068`](#insn-00c0c068) → [`00c0c074`](#insn-00c0c074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c06c`](#insn-00c0c06c) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c070`](#insn-00c0c070) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00c0c074`](#insn-00c0c074) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c078`](#insn-00c0c078) → [`00c0c084`](#insn-00c0c084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c07c`](#insn-00c0c07c) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c080`](#insn-00c0c080) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00c0c088`](#insn-00c0c088) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c08c`](#insn-00c0c08c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c090`](#insn-00c0c090) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c094`](#insn-00c0c094) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c098`](#insn-00c0c098) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0c09c`](#insn-00c0c09c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c0bcd4`](#insn-00c0bcd4)

~~~json
{
  "source": "00c0bcd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bcd8`](#insn-00c0bcd8)

~~~json
{
  "source": "00c0bcd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bcdc`](#insn-00c0bcdc)

~~~json
{
  "source": "00c0bcdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bce0`](#insn-00c0bce0)

~~~json
{
  "source": "00c0bce0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bce4`](#insn-00c0bce4)

~~~json
{
  "source": "00c0bce4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bce8`](#insn-00c0bce8)

~~~json
{
  "source": "00c0bce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd0c`](#insn-00c0bd0c)

~~~json
{
  "source": "00c0bd0c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd10`](#insn-00c0bd10)

~~~json
{
  "source": "00c0bd10",
  "target": "00c0bd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd18`](#insn-00c0bd18)

~~~json
{
  "source": "00c0bd18",
  "target": "00c0bd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd20`](#insn-00c0bd20)

~~~json
{
  "source": "00c0bd20",
  "target": "00c0bd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd28`](#insn-00c0bd28)

~~~json
{
  "source": "00c0bd28",
  "target": "00c0bd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd30`](#insn-00c0bd30)

~~~json
{
  "source": "00c0bd30",
  "target": "00c0bd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd38`](#insn-00c0bd38)

~~~json
{
  "source": "00c0bd38",
  "target": "00c0bd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd4c`](#insn-00c0bd4c)

~~~json
{
  "source": "00c0bd4c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd54`](#insn-00c0bd54)

~~~json
{
  "source": "00c0bd54",
  "target": "00c5e590",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0bd58`](#insn-00c0bd58)

~~~json
{
  "source": "00c0bd58",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd5c`](#insn-00c0bd5c)

~~~json
{
  "source": "00c0bd5c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd70`](#insn-00c0bd70)

~~~json
{
  "source": "00c0bd70",
  "target": "00c5be70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0bd74`](#insn-00c0bd74)

~~~json
{
  "source": "00c0bd74",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd78`](#insn-00c0bd78)

~~~json
{
  "source": "00c0bd78",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd88`](#insn-00c0bd88)

~~~json
{
  "source": "00c0bd88",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd90`](#insn-00c0bd90)

~~~json
{
  "source": "00c0bd90",
  "target": "Stack[-0x1bc]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bd9c`](#insn-00c0bd9c)

~~~json
{
  "source": "00c0bd9c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bda0`](#insn-00c0bda0)

~~~json
{
  "source": "00c0bda0",
  "target": "00c0bdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdac`](#insn-00c0bdac)

~~~json
{
  "source": "00c0bdac",
  "target": "00c0bdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdb8`](#insn-00c0bdb8)

~~~json
{
  "source": "00c0bdb8",
  "target": "00c0bdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdc0`](#insn-00c0bdc0)

~~~json
{
  "source": "00c0bdc0",
  "target": "00c0bde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdc8`](#insn-00c0bdc8)

~~~json
{
  "source": "00c0bdc8",
  "target": "00c0bdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdcc`](#insn-00c0bdcc)

~~~json
{
  "source": "00c0bdcc",
  "target": "00c0be2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdd0`](#insn-00c0bdd0)

~~~json
{
  "source": "00c0bdd0",
  "target": "00c0bf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdf0`](#insn-00c0bdf0)

~~~json
{
  "source": "00c0bdf0",
  "target": "00c0bdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bdfc`](#insn-00c0bdfc)

~~~json
{
  "source": "00c0bdfc",
  "target": "00c0be08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be04`](#insn-00c0be04)

~~~json
{
  "source": "00c0be04",
  "target": "00c0be18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be28`](#insn-00c0be28)

~~~json
{
  "source": "00c0be28",
  "target": "00c0bf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be2c`](#insn-00c0be2c)

~~~json
{
  "source": "00c0be2c",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be30`](#insn-00c0be30)

~~~json
{
  "source": "00c0be30",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be34`](#insn-00c0be34)

~~~json
{
  "source": "00c0be34",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be4c`](#insn-00c0be4c)

~~~json
{
  "source": "00c0be4c",
  "target": "00c0bf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be54`](#insn-00c0be54)

~~~json
{
  "source": "00c0be54",
  "target": "00c0be6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be64`](#insn-00c0be64)

~~~json
{
  "source": "00c0be64",
  "target": "00c5be70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0be68`](#insn-00c0be68)

~~~json
{
  "source": "00c0be68",
  "target": "00c0be90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be70`](#insn-00c0be70)

~~~json
{
  "source": "00c0be70",
  "target": "00c0be84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be78`](#insn-00c0be78)

~~~json
{
  "source": "00c0be78",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be80`](#insn-00c0be80)

~~~json
{
  "source": "00c0be80",
  "target": "00c0be8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be84`](#insn-00c0be84)

~~~json
{
  "source": "00c0be84",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be88`](#insn-00c0be88)

~~~json
{
  "source": "00c0be88",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be90`](#insn-00c0be90)

~~~json
{
  "source": "00c0be90",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0be94`](#insn-00c0be94)

~~~json
{
  "source": "00c0be94",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0beb8`](#insn-00c0beb8)

~~~json
{
  "source": "00c0beb8",
  "target": "00c0becc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bec4`](#insn-00c0bec4)

~~~json
{
  "source": "00c0bec4",
  "target": "00c5be70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0bec8`](#insn-00c0bec8)

~~~json
{
  "source": "00c0bec8",
  "target": "00c0beec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0becc`](#insn-00c0becc)

~~~json
{
  "source": "00c0becc",
  "target": "00c0bee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bed4`](#insn-00c0bed4)

~~~json
{
  "source": "00c0bed4",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bedc`](#insn-00c0bedc)

~~~json
{
  "source": "00c0bedc",
  "target": "00c0bee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bee0`](#insn-00c0bee0)

~~~json
{
  "source": "00c0bee0",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bee4`](#insn-00c0bee4)

~~~json
{
  "source": "00c0bee4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0beec`](#insn-00c0beec)

~~~json
{
  "source": "00c0beec",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bef0`](#insn-00c0bef0)

~~~json
{
  "source": "00c0bef0",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf00`](#insn-00c0bf00)

~~~json
{
  "source": "00c0bf00",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf0c`](#insn-00c0bf0c)

~~~json
{
  "source": "00c0bf0c",
  "target": "00c0bf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf14`](#insn-00c0bf14)

~~~json
{
  "source": "00c0bf14",
  "target": "00c0bf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf28`](#insn-00c0bf28)

~~~json
{
  "source": "00c0bf28",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf44`](#insn-00c0bf44)

~~~json
{
  "source": "00c0bf44",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf48`](#insn-00c0bf48)

~~~json
{
  "source": "00c0bf48",
  "target": "00c5e5a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0bf4c`](#insn-00c0bf4c)

~~~json
{
  "source": "00c0bf4c",
  "target": "00c0bf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf58`](#insn-00c0bf58)

~~~json
{
  "source": "00c0bf58",
  "target": "00c0bda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf6c`](#insn-00c0bf6c)

~~~json
{
  "source": "00c0bf6c",
  "target": "00c0bdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf70`](#insn-00c0bf70)

~~~json
{
  "source": "00c0bf70",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf74`](#insn-00c0bf74)

~~~json
{
  "source": "00c0bf74",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf78`](#insn-00c0bf78)

~~~json
{
  "source": "00c0bf78",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf88`](#insn-00c0bf88)

~~~json
{
  "source": "00c0bf88",
  "target": "00c0bfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf8c`](#insn-00c0bf8c)

~~~json
{
  "source": "00c0bf8c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bf9c`](#insn-00c0bf9c)

~~~json
{
  "source": "00c0bf9c",
  "target": "00c0bfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bfa0`](#insn-00c0bfa0)

~~~json
{
  "source": "00c0bfa0",
  "target": "Stack[-0x1bc]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bfa8`](#insn-00c0bfa8)

~~~json
{
  "source": "00c0bfa8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bfac`](#insn-00c0bfac)

~~~json
{
  "source": "00c0bfac",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bfbc`](#insn-00c0bfbc)

~~~json
{
  "source": "00c0bfbc",
  "target": "00c363bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0bfc0`](#insn-00c0bfc0)

~~~json
{
  "source": "00c0bfc0",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bfc4`](#insn-00c0bfc4)

~~~json
{
  "source": "00c0bfc4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bfd8`](#insn-00c0bfd8)

~~~json
{
  "source": "00c0bfd8",
  "target": "00c5e540",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0bfdc`](#insn-00c0bfdc)

~~~json
{
  "source": "00c0bfdc",
  "target": "00c0bff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bfe8`](#insn-00c0bfe8)

~~~json
{
  "source": "00c0bfe8",
  "target": "00c0c004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bff0`](#insn-00c0bff0)

~~~json
{
  "source": "00c0bff0",
  "target": "00c0c014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bff8`](#insn-00c0bff8)

~~~json
{
  "source": "00c0bff8",
  "target": "00c0c024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0bffc`](#insn-00c0bffc)

~~~json
{
  "source": "00c0bffc",
  "target": "00c0c058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c000`](#insn-00c0c000)

~~~json
{
  "source": "00c0c000",
  "target": "00c0c064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c020`](#insn-00c0c020)

~~~json
{
  "source": "00c0c020",
  "target": "00c0bffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c02c`](#insn-00c0c02c)

~~~json
{
  "source": "00c0c02c",
  "target": "00c0c038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c034`](#insn-00c0c034)

~~~json
{
  "source": "00c0c034",
  "target": "00c0c048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c054`](#insn-00c0c054)

~~~json
{
  "source": "00c0c054",
  "target": "00c0c064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c064`](#insn-00c0c064)

~~~json
{
  "source": "00c0c064",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c068`](#insn-00c0c068)

~~~json
{
  "source": "00c0c068",
  "target": "00c0c074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c06c`](#insn-00c0c06c)

~~~json
{
  "source": "00c0c06c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c070`](#insn-00c0c070)

~~~json
{
  "source": "00c0c070",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0c074`](#insn-00c0c074)

~~~json
{
  "source": "00c0c074",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c078`](#insn-00c0c078)

~~~json
{
  "source": "00c0c078",
  "target": "00c0c084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c07c`](#insn-00c0c07c)

~~~json
{
  "source": "00c0c07c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c080`](#insn-00c0c080)

~~~json
{
  "source": "00c0c080",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0c088`](#insn-00c0c088)

~~~json
{
  "source": "00c0c088",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c08c`](#insn-00c0c08c)

~~~json
{
  "source": "00c0c08c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c090`](#insn-00c0c090)

~~~json
{
  "source": "00c0c090",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c094`](#insn-00c0c094)

~~~json
{
  "source": "00c0c094",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c098`](#insn-00c0c098)

~~~json
{
  "source": "00c0c098",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0c09c`](#insn-00c0c09c)

~~~json
{
  "source": "00c0c09c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
