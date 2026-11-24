# 00b8faec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b8faa8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0016.md#compare-93f6c71540fc73168ea5d3a11af561ae)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c0c534`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c534.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0073.md#compare-185efac55c31f5382849005da060816e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b8faec",
  "name": "FUN_00b8faec",
  "size": 992,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "add2024fa89e33f4eb2804ee8bce8633fa615af76c6b5ff8cce7adb3f7545168",
  "source_text_sha256": "add2024fa89e33f4eb2804ee8bce8633fa615af76c6b5ff8cce7adb3f7545168",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b8faec",
        "00b8fecb"
      ]
    ],
    "bytes_sha256": "1efe65322d20f96142f225bdc2fdab8473574424a1dc3875b8d893a83a581c38",
    "instruction_count": 248,
    "instruction_bytes": 992,
    "body_bytes": 992,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00b8fae4](../00b8f/00b8fae4.md)

## 呼び出し先

- [00bb9940](../00bb9/00bb9940.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdefc0](../00bde/00bdefc0.md)
- [00be1540](../00be1/00be1540.md)
- [00be15a0](../00be1/00be15a0.md)
- [00be15b0](../00be1/00be15b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6879 bytes

~~~c

long * FUN_00b8faec(undefined8 param_1,long *param_2,long *param_3,long param_4,uint *param_5,
                   undefined8 *param_6)

{
  uint uVar1;
  ulong uVar2;
  long *plVar3;
  bool bVar4;
  int iVar5;
  ulong uVar6;
  undefined8 uVar7;
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
LAB_00b8fbcc:
  if (param_2 == (long *)0x0) {
    bVar4 = true;
    if (param_3 != (long *)0x0) goto LAB_00b8fc14;
LAB_00b8fbec:
    if (bVar4 != false) goto LAB_00b8fd90;
  }
  else {
    if ((int *)param_2[3] == (int *)param_2[4]) {
      iVar5 = (**(code **)(*param_2 + 0x48))(param_2);
    }
    else {
      iVar5 = *(int *)param_2[3];
    }
    bVar4 = iVar5 == -1;
    plVar3 = (long *)0x0;
    if (!bVar4) {
      plVar3 = param_2;
    }
    param_2 = plVar3;
    if (param_3 == (long *)0x0) goto LAB_00b8fbec;
LAB_00b8fc14:
    if ((int *)param_3[3] == (int *)param_3[4]) {
                    /* try { // try from 00b8fc34 to 00c8fc3b has its CatchHandler @ 00b8feb8 */
      iVar5 = (**(code **)(*param_3 + 0x48))(param_3);
    }
    else {
      iVar5 = *(int *)param_3[3];
    }
    plVar3 = (long *)0x0;
    if (iVar5 != -1) {
      plVar3 = param_3;
    }
    param_3 = plVar3;
                    /* try { // try from 00b8fc48 to 00c8fc93 has its CatchHandler @ 00b8fec0 */
    if (bVar4 == (iVar5 == -1)) goto LAB_00b8fd90;
  }
  uVar6 = local_108 >> 1 & 0x7f;
  if ((local_108 & 1) != 0) {
    uVar6 = local_100;
  }
  if (local_110 == (void *)((long)pvVar8 + uVar6)) {
    if ((long)uVar6 < 1) {
      uVar9 = uVar6 * 2;
      pvVar8 = local_f8;
      uVar2 = uVar9;
      if ((local_108 & 1) == 0) {
        local_108 = CONCAT71(local_108._1_7_,(char)((int)uVar9 << 1));
        pvVar8 = pvVar11;
        uVar2 = local_100;
                    /* try { // try from 00b8fca0 to 00c8fcbb has its CatchHandler @ 00b8fea0 */
      }
      local_100 = uVar2;
      *(undefined1 *)((long)pvVar8 + uVar9) = 0;
    }
    else {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
                (&local_108,uVar6,0);
    }
                    /* try { // try from 00b8fcbc to 00c8fd4b has its CatchHandler @ 00b8f8f8 */
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
    pvVar8 = pvVar11;
    if ((local_108 & 1) != 0) {
      pvVar8 = local_f8;
    }
    local_110 = (void *)((long)pvVar8 + uVar6);
  }
  if ((uint *)param_2[3] == (uint *)param_2[4]) {
    uVar6 = (**(code **)(*param_2 + 0x48))(param_2);
  }
  else {
    uVar6 = (ulong)*(uint *)param_2[3];
  }
                    /* try { // try from 00b8fd4c to 00c8fd4f has its CatchHandler @ 00b8feb8 */
  iVar5 = _ZNSt6__ndk19__num_getIwE17__stage2_int_loopEwiPcRS2_RjwRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_Pw
                    (uVar6,uVar10,pvVar8,&local_110,&local_1bc,local_6c[0],local_f0,auStack_1b0,
                     &local_1b8,auStack_d4);
  if (iVar5 != 0) goto LAB_00b8fd90;
                    /* try { // try from 00b8fd78 to 00c8fda7 has its CatchHandler @ 00b8fed0 */
  if (param_2[3] == param_2[4]) {
    (**(code **)(*param_2 + 0x50))(param_2);
  }
  else {
    param_2[3] = param_2[3] + 4;
  }
  goto LAB_00b8fbcc;
LAB_00b8fd90:
  uVar6 = (ulong)(local_f0[0] >> 1);
  if ((local_f0[0] & 1) != 0) {
    uVar6 = local_e8;
  }
                    /* try { // try from 00b8fda8 to 00c8fffb has its CatchHandler @ 00b8f8f8 */
  if ((uVar6 != 0) && ((long)local_1b8 - (long)auStack_1b0 < 0xa0)) {
    *local_1b8 = local_1bc;
    local_1b8 = local_1b8 + 1;
  }
  uVar7 = FUN_00bb9940(pvVar8,local_110,param_5,uVar10);
  *param_6 = uVar7;
  _ZNSt6__ndk116__check_groupingERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjS8_Rj
            (local_f0,auStack_1b0,local_1b8,param_5);
  if (param_2 == (long *)0x0) {
    bVar4 = true;
    if (param_3 != (long *)0x0) goto LAB_00b8fe44;
LAB_00b8fe1c:
    if (!bVar4) goto LAB_00b8fe84;
  }
  else {
    if ((int *)param_2[3] == (int *)param_2[4]) {
      iVar5 = (**(code **)(*param_2 + 0x48))(param_2);
    }
    else {
      iVar5 = *(int *)param_2[3];
    }
    bVar4 = iVar5 == -1;
    plVar3 = (long *)0x0;
    if (!bVar4) {
      plVar3 = param_2;
    }
    param_2 = plVar3;
    if (param_3 == (long *)0x0) goto LAB_00b8fe1c;
LAB_00b8fe44:
    if ((int *)param_3[3] == (int *)param_3[4]) {
      iVar5 = (**(code **)(*param_3 + 0x48))(param_3);
    }
    else {
      iVar5 = *(int *)param_3[3];
    }
    if (bVar4 != (iVar5 == -1)) goto LAB_00b8fe84;
  }
  *param_5 = *param_5 | 2;
LAB_00b8fe84:
                    /* catch() { ... } // from try @ 00b8fa4c with catch @ 00b8fe88 */
  if ((local_108 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b8f9f0 with catch @ 00b8fe90 */
    _ZdlPv(local_f8);
  }
  if ((local_f0[0] & 1) != 0) {
                    /* catch() { ... } // from try @ 00b8fca0 with catch @ 00b8fea0 */
    _ZdlPv(local_e0);
  }
                    /* catch() { ... } // from try @ 00b8fc34 with catch @ 00b8feb8
                       catch() { ... } // from try @ 00b8fd4c with catch @ 00b8feb8 */
                    /* catch() { ... } // from try @ 00b8fc48 with catch @ 00b8fec0 */
                    /* catch() { ... } // from try @ 00b8fa14 with catch @ 00b8fec8 */
  return param_2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b8faec"></a> `00b8faec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b8faf0"></a> `00b8faf0` | `ff 83 07 d1` | sub sp,sp,#0x1e0 | `FALL_THROUGH`
<a id="insn-00b8faf4"></a> `00b8faf4` | `fd 7b 18 a9` | stp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00b8faf8"></a> `00b8faf8` | `fc 6f 19 a9` | stp x28,x27,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00b8fafc"></a> `00b8fafc` | `fa 67 1a a9` | stp x26,x25,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00b8fb00"></a> `00b8fb00` | `f8 5f 1b a9` | stp x24,x23,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00b8fb04"></a> `00b8fb04` | `f6 57 1c a9` | stp x22,x21,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00b8fb08"></a> `00b8fb08` | `f4 4f 1d a9` | stp x20,x19,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00b8fb0c"></a> `00b8fb0c` | `fd 03 06 91` | add x29,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b8fb10"></a> `00b8fb10` | `68 08 40 b9` | ldr w8,[x3, #0x8] | `FALL_THROUGH`
<a id="insn-00b8fb14"></a> `00b8fb14` | `49 09 80 52` | mov w9,#0x4a | `FALL_THROUGH`
<a id="insn-00b8fb18"></a> `00b8fb18` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00b8fb1c"></a> `00b8fb1c` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00b8fb20"></a> `00b8fb20` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00b8fb24"></a> `00b8fb24` | `ba c3 02 d1` | sub x26,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-00b8fb28"></a> `00b8fb28` | `08 01 09 6a` | ands w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00b8fb2c"></a> `00b8fb2c` | `e5 0b 00 f9` | str x5,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b8fb30"></a> `00b8fb30` | `20 01 00 54` | b.eq 0x00b8fb54 | `CONDITIONAL_JUMP`
<a id="insn-00b8fb34"></a> `00b8fb34` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00b8fb38"></a> `00b8fb38` | `a0 00 00 54` | b.eq 0x00b8fb4c | `CONDITIONAL_JUMP`
<a id="insn-00b8fb3c"></a> `00b8fb3c` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00b8fb40"></a> `00b8fb40` | `e1 00 00 54` | b.ne 0x00b8fb5c | `CONDITIONAL_JUMP`
<a id="insn-00b8fb44"></a> `00b8fb44` | `17 02 80 52` | mov w23,#0x10 | `FALL_THROUGH`
<a id="insn-00b8fb48"></a> `00b8fb48` | `06 00 00 14` | b 0x00b8fb60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fb4c"></a> `00b8fb4c` | `17 01 80 52` | mov w23,#0x8 | `FALL_THROUGH`
<a id="insn-00b8fb50"></a> `00b8fb50` | `04 00 00 14` | b 0x00b8fb60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fb54"></a> `00b8fb54` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00b8fb58"></a> `00b8fb58` | `02 00 00 14` | b 0x00b8fb60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fb5c"></a> `00b8fb5c` | `57 01 80 52` | mov w23,#0xa | `FALL_THROUGH`
<a id="insn-00b8fb60"></a> `00b8fb60` | `a8 43 02 d1` | sub x8,x29,#0x90 | `FALL_THROUGH`
<a id="insn-00b8fb64"></a> `00b8fb64` | `a1 d3 01 d1` | sub x1,x29,#0x74 | `FALL_THROUGH`
<a id="insn-00b8fb68"></a> `00b8fb68` | `a2 33 00 d1` | sub x2,x29,#0xc | `FALL_THROUGH`
<a id="insn-00b8fb6c"></a> `00b8fb6c` | `e4 0f 00 f9` | str x4,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fb70"></a> `00b8fb70` | `bb d3 01 d1` | sub x27,x29,#0x74 | `FALL_THROUGH`
<a id="insn-00b8fb74"></a> `00b8fb74` | `8b 46 01 94` | bl 0x00be15a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fb78"></a> `00b8fb78` | `5f ff 00 a9` | stp xzr,xzr,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00b8fb7c"></a> `00b8fb7c` | `5f 0f 00 f9` | str xzr,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fb80"></a> `00b8fb80` | `a0 a3 02 d1` | sub x0,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00b8fb84"></a> `00b8fb84` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00b8fb88"></a> `00b8fb88` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b8fb8c"></a> `00b8fb8c` | `b3 a3 02 d1` | sub x19,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00b8fb90"></a> `00b8fb90` | `0c 3d 01 94` | bl 0x00bdefc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fb94"></a> `00b8fb94` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00b8fb98"></a> `00b8fb98` | `49 0f 40 f9` | ldr x9,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fb9c"></a> `00b8fb9c` | `ea c3 00 91` | add x10,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b8fba0"></a> `00b8fba0` | `7c 02 40 b2` | orr x28,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fba4"></a> `00b8fba4` | `d6 02 80 52` | mov w22,#0x16 | `FALL_THROUGH`
<a id="insn-00b8fba8"></a> `00b8fba8` | `ea 17 00 f9` | str x10,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b8fbac"></a> `00b8fbac` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fbb0"></a> `00b8fbb0` | `ff 27 00 b9` | str wzr,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00b8fbb4"></a> `00b8fbb4` | `38 15 93 9a` | csinc x24,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00b8fbb8"></a> `00b8fbb8` | `f3 a3 00 91` | add x19,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00b8fbbc"></a> `00b8fbbc` | `58 03 00 f9` | str x24,[x26] | `FALL_THROUGH`
<a id="insn-00b8fbc0"></a> `00b8fbc0` | `03 00 00 14` | b 0x00b8fbcc | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fbc4"></a> `00b8fbc4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b8fbc8"></a> `00b8fbc8` | `a8 0e 00 f9` | str x8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fbcc"></a> `00b8fbcc` | `d5 00 00 b4` | cbz x21,0x00b8fbe4 | `CONDITIONAL_JUMP`
<a id="insn-00b8fbd0"></a> `00b8fbd0` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fbd4"></a> `00b8fbd4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fbd8"></a> `00b8fbd8` | `e0 00 00 54` | b.eq 0x00b8fbf4 | `CONDITIONAL_JUMP`
<a id="insn-00b8fbdc"></a> `00b8fbdc` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00b8fbe0"></a> `00b8fbe0` | `09 00 00 14` | b 0x00b8fc04 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fbe4"></a> `00b8fbe4` | `39 00 80 52` | mov w25,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fbe8"></a> `00b8fbe8` | `74 01 00 b5` | cbnz x20,0x00b8fc14 | `CONDITIONAL_JUMP`
<a id="insn-00b8fbec"></a> `00b8fbec` | `19 03 00 36` | tbz w25,#0x0,0x00b8fc4c | `CONDITIONAL_JUMP`
<a id="insn-00b8fbf0"></a> `00b8fbf0` | `68 00 00 14` | b 0x00b8fd90 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fbf4"></a> `00b8fbf4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b8fbf8"></a> `00b8fbf8` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00b8fbfc"></a> `00b8fbfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b8fc00"></a> `00b8fc00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b8fc04"></a> `00b8fc04` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fc08"></a> `00b8fc08` | `f9 17 9f 1a` | cset w25,eq | `FALL_THROUGH`
<a id="insn-00b8fc0c"></a> `00b8fc0c` | `f5 03 95 9a` | csel x21,xzr,x21,eq | `FALL_THROUGH`
<a id="insn-00b8fc10"></a> `00b8fc10` | `f4 fe ff b4` | cbz x20,0x00b8fbec | `CONDITIONAL_JUMP`
<a id="insn-00b8fc14"></a> `00b8fc14` | `88 a6 41 a9` | ldp x8,x9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fc18"></a> `00b8fc18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fc1c"></a> `00b8fc1c` | `60 00 00 54` | b.eq 0x00b8fc28 | `CONDITIONAL_JUMP`
<a id="insn-00b8fc20"></a> `00b8fc20` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00b8fc24"></a> `00b8fc24` | `05 00 00 14` | b 0x00b8fc38 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fc28"></a> `00b8fc28` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b8fc2c"></a> `00b8fc2c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00b8fc30"></a> `00b8fc30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b8fc34"></a> `00b8fc34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b8fc38"></a> `00b8fc38` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fc3c"></a> `00b8fc3c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00b8fc40"></a> `00b8fc40` | `f4 03 94 9a` | csel x20,xzr,x20,eq | `FALL_THROUGH`
<a id="insn-00b8fc44"></a> `00b8fc44` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00b8fc48"></a> `00b8fc48` | `40 0a 00 54` | b.eq 0x00b8fd90 | `CONDITIONAL_JUMP`
<a id="insn-00b8fc4c"></a> `00b8fc4c` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00b8fc50"></a> `00b8fc50` | `49 0b 40 f9` | ldr x9,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00b8fc54"></a> `00b8fc54` | `4b 03 40 f9` | ldr x11,[x26] | `FALL_THROUGH`
<a id="insn-00b8fc58"></a> `00b8fc58` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fc5c"></a> `00b8fc5c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fc60"></a> `00b8fc60` | `59 01 89 9a` | csel x25,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00b8fc64"></a> `00b8fc64` | `09 03 19 8b` | add x9,x24,x25 | `FALL_THROUGH`
<a id="insn-00b8fc68"></a> `00b8fc68` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00b8fc6c"></a> `00b8fc6c` | `c1 05 00 54` | b.ne 0x00b8fd24 | `CONDITIONAL_JUMP`
<a id="insn-00b8fc70"></a> `00b8fc70` | `3f 07 00 f1` | cmp x25,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fc74"></a> `00b8fc74` | `cb 00 00 54` | b.lt 0x00b8fc8c | `CONDITIONAL_JUMP`
<a id="insn-00b8fc78"></a> `00b8fc78` | `a0 a3 02 d1` | sub x0,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00b8fc7c"></a> `00b8fc7c` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00b8fc80"></a> `00b8fc80` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b8fc84"></a> `00b8fc84` | `cf 3c 01 94` | bl 0x00bdefc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fc88"></a> `00b8fc88` | `0a 00 00 14` | b 0x00b8fcb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fc8c"></a> `00b8fc8c` | `29 fb 7f d3` | lsl x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fc90"></a> `00b8fc90` | `a8 00 00 37` | tbnz w8,#0x0,0x00b8fca4 | `CONDITIONAL_JUMP`
<a id="insn-00b8fc94"></a> `00b8fc94` | `28 79 1f 53` | lsl w8,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fc98"></a> `00b8fc98` | `a8 83 15 38` | sturb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00b8fc9c"></a> `00b8fc9c` | `e8 03 1c aa` | mov x8,x28 | `FALL_THROUGH`
<a id="insn-00b8fca0"></a> `00b8fca0` | `03 00 00 14` | b 0x00b8fcac | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fca4"></a> `00b8fca4` | `48 0f 40 f9` | ldr x8,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fca8"></a> `00b8fca8` | `49 0b 00 f9` | str x9,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00b8fcac"></a> `00b8fcac` | `1f 69 29 38` | strb wzr,[x8, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00b8fcb0"></a> `00b8fcb0` | `49 ab 40 a9` | ldp x9,x10,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00b8fcb4"></a> `00b8fcb4` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00b8fcb8"></a> `00b8fcb8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fcbc"></a> `00b8fcbc` | `2b f9 7f 92` | and x11,x9,#-0x2 | `FALL_THROUGH`
<a id="insn-00b8fcc0"></a> `00b8fcc0` | `2c 1d 41 d3` | ubfx x12,x9,#0x1,#0x7 | `FALL_THROUGH`
<a id="insn-00b8fcc4"></a> `00b8fcc4` | `6b 05 00 d1` | sub x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fcc8"></a> `00b8fcc8` | `c8 02 8b 9a` | csel x8,x22,x11,eq | `FALL_THROUGH`
<a id="insn-00b8fccc"></a> `00b8fccc` | `3f 01 40 f2` | tst x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fcd0"></a> `00b8fcd0` | `8a 01 8a 9a` | csel x10,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00b8fcd4"></a> `00b8fcd4` | `01 01 0a eb` | subs x1,x8,x10 | `FALL_THROUGH`
<a id="insn-00b8fcd8"></a> `00b8fcd8` | `a9 00 00 54` | b.ls 0x00b8fcec | `CONDITIONAL_JUMP`
<a id="insn-00b8fcdc"></a> `00b8fcdc` | `a0 a3 02 d1` | sub x0,x29,#0xa8 | `FALL_THROUGH`
<a id="insn-00b8fce0"></a> `00b8fce0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b8fce4"></a> `00b8fce4` | `b7 3c 01 94` | bl 0x00bdefc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fce8"></a> `00b8fce8` | `09 00 00 14` | b 0x00b8fd0c | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fcec"></a> `00b8fcec` | `a9 00 00 37` | tbnz w9,#0x0,0x00b8fd00 | `CONDITIONAL_JUMP`
<a id="insn-00b8fcf0"></a> `00b8fcf0` | `09 79 1f 53` | lsl w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fcf4"></a> `00b8fcf4` | `a9 83 15 38` | sturb w9,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00b8fcf8"></a> `00b8fcf8` | `e9 03 1c aa` | mov x9,x28 | `FALL_THROUGH`
<a id="insn-00b8fcfc"></a> `00b8fcfc` | `03 00 00 14` | b 0x00b8fd08 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fd00"></a> `00b8fd00` | `49 0f 40 f9` | ldr x9,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fd04"></a> `00b8fd04` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00b8fd08"></a> `00b8fd08` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b8fd0c"></a> `00b8fd0c` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00b8fd10"></a> `00b8fd10` | `49 0f 40 f9` | ldr x9,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fd14"></a> `00b8fd14` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fd18"></a> `00b8fd18` | `98 03 89 9a` | csel x24,x28,x9,eq | `FALL_THROUGH`
<a id="insn-00b8fd1c"></a> `00b8fd1c` | `08 03 19 8b` | add x8,x24,x25 | `FALL_THROUGH`
<a id="insn-00b8fd20"></a> `00b8fd20` | `48 03 00 f9` | str x8,[x26] | `FALL_THROUGH`
<a id="insn-00b8fd24"></a> `00b8fd24` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fd28"></a> `00b8fd28` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fd2c"></a> `00b8fd2c` | `60 00 00 54` | b.eq 0x00b8fd38 | `CONDITIONAL_JUMP`
<a id="insn-00b8fd30"></a> `00b8fd30` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00b8fd34"></a> `00b8fd34` | `05 00 00 14` | b 0x00b8fd48 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fd38"></a> `00b8fd38` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b8fd3c"></a> `00b8fd3c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00b8fd40"></a> `00b8fd40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b8fd44"></a> `00b8fd44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b8fd48"></a> `00b8fd48` | `a5 43 5f b8` | ldur w5,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00b8fd4c"></a> `00b8fd4c` | `a3 c3 02 d1` | sub x3,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-00b8fd50"></a> `00b8fd50` | `e4 93 00 91` | add x4,sp,#0x24 | `FALL_THROUGH`
<a id="insn-00b8fd54"></a> `00b8fd54` | `a6 43 02 d1` | sub x6,x29,#0x90 | `FALL_THROUGH`
<a id="insn-00b8fd58"></a> `00b8fd58` | `e7 c3 00 91` | add x7,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b8fd5c"></a> `00b8fd5c` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00b8fd60"></a> `00b8fd60` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00b8fd64"></a> `00b8fd64` | `f3 6f 00 a9` | stp x19,x27,[sp] | `FALL_THROUGH`
<a id="insn-00b8fd68"></a> `00b8fd68` | `12 46 01 94` | bl 0x00be15b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fd6c"></a> `00b8fd6c` | `20 01 00 35` | cbnz w0,0x00b8fd90 | `CONDITIONAL_JUMP`
<a id="insn-00b8fd70"></a> `00b8fd70` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fd74"></a> `00b8fd74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fd78"></a> `00b8fd78` | `61 f2 ff 54` | b.ne 0x00b8fbc4 | `CONDITIONAL_JUMP`
<a id="insn-00b8fd7c"></a> `00b8fd7c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b8fd80"></a> `00b8fd80` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00b8fd84"></a> `00b8fd84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b8fd88"></a> `00b8fd88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b8fd8c"></a> `00b8fd8c` | `90 ff ff 17` | b 0x00b8fbcc | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fd90"></a> `00b8fd90` | `a8 03 57 38` | ldurb w8,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00b8fd94"></a> `00b8fd94` | `49 17 40 f9` | ldr x9,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00b8fd98"></a> `00b8fd98` | `f6 0f 40 f9` | ldr x22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fd9c"></a> `00b8fd9c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fda0"></a> `00b8fda0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fda4"></a> `00b8fda4` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00b8fda8"></a> `00b8fda8` | `28 01 00 b4` | cbz x8,0x00b8fdcc | `CONDITIONAL_JUMP`
<a id="insn-00b8fdac"></a> `00b8fdac` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b8fdb0"></a> `00b8fdb0` | `e9 c3 00 91` | add x9,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b8fdb4"></a> `00b8fdb4` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fdb8"></a> `00b8fdb8` | `3f 7d 02 f1` | cmp x9,#0x9f | `FALL_THROUGH`
<a id="insn-00b8fdbc"></a> `00b8fdbc` | `8c 00 00 54` | b.gt 0x00b8fdcc | `CONDITIONAL_JUMP`
<a id="insn-00b8fdc0"></a> `00b8fdc0` | `e9 27 40 b9` | ldr w9,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00b8fdc4"></a> `00b8fdc4` | `09 45 00 b8` | str w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00b8fdc8"></a> `00b8fdc8` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b8fdcc"></a> `00b8fdcc` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00b8fdd0"></a> `00b8fdd0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b8fdd4"></a> `00b8fdd4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b8fdd8"></a> `00b8fdd8` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-00b8fddc"></a> `00b8fddc` | `d9 a6 00 94` | bl 0x00bb9940 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fde0"></a> `00b8fde0` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b8fde4"></a> `00b8fde4` | `e2 17 40 f9` | ldr x2,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b8fde8"></a> `00b8fde8` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b8fdec"></a> `00b8fdec` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00b8fdf0"></a> `00b8fdf0` | `00 01 00 f9` | str x0,[x8] | `FALL_THROUGH`
<a id="insn-00b8fdf4"></a> `00b8fdf4` | `a0 43 02 d1` | sub x0,x29,#0x90 | `FALL_THROUGH`
<a id="insn-00b8fdf8"></a> `00b8fdf8` | `d2 45 01 94` | bl 0x00be1540 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fdfc"></a> `00b8fdfc` | `d5 00 00 b4` | cbz x21,0x00b8fe14 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe00"></a> `00b8fe00` | `a8 a6 41 a9` | ldp x8,x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fe04"></a> `00b8fe04` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fe08"></a> `00b8fe08` | `e0 00 00 54` | b.eq 0x00b8fe24 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe0c"></a> `00b8fe0c` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00b8fe10"></a> `00b8fe10` | `09 00 00 14` | b 0x00b8fe34 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fe14"></a> `00b8fe14` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fe18"></a> `00b8fe18` | `74 01 00 b5` | cbnz x20,0x00b8fe44 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe1c"></a> `00b8fe1c` | `f3 02 00 37` | tbnz w19,#0x0,0x00b8fe78 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe20"></a> `00b8fe20` | `19 00 00 14` | b 0x00b8fe84 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fe24"></a> `00b8fe24` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b8fe28"></a> `00b8fe28` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00b8fe2c"></a> `00b8fe2c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b8fe30"></a> `00b8fe30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b8fe34"></a> `00b8fe34` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fe38"></a> `00b8fe38` | `f3 17 9f 1a` | cset w19,eq | `FALL_THROUGH`
<a id="insn-00b8fe3c"></a> `00b8fe3c` | `f5 03 95 9a` | csel x21,xzr,x21,eq | `FALL_THROUGH`
<a id="insn-00b8fe40"></a> `00b8fe40` | `f4 fe ff b4` | cbz x20,0x00b8fe1c | `CONDITIONAL_JUMP`
<a id="insn-00b8fe44"></a> `00b8fe44` | `88 a6 41 a9` | ldp x8,x9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fe48"></a> `00b8fe48` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fe4c"></a> `00b8fe4c` | `60 00 00 54` | b.eq 0x00b8fe58 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe50"></a> `00b8fe50` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00b8fe54"></a> `00b8fe54` | `05 00 00 14` | b 0x00b8fe68 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fe58"></a> `00b8fe58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b8fe5c"></a> `00b8fe5c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00b8fe60"></a> `00b8fe60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b8fe64"></a> `00b8fe64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b8fe68"></a> `00b8fe68` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fe6c"></a> `00b8fe6c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00b8fe70"></a> `00b8fe70` | `68 02 08 4a` | eor w8,w19,w8 | `FALL_THROUGH`
<a id="insn-00b8fe74"></a> `00b8fe74` | `88 00 00 37` | tbnz w8,#0x0,0x00b8fe84 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe78"></a> `00b8fe78` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00b8fe7c"></a> `00b8fe7c` | `08 01 1f 32` | orr w8,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00b8fe80"></a> `00b8fe80` | `c8 02 00 b9` | str w8,[x22] | `FALL_THROUGH`
<a id="insn-00b8fe84"></a> `00b8fe84` | `a8 83 55 38` | ldurb w8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00b8fe88"></a> `00b8fe88` | `68 00 00 36` | tbz w8,#0x0,0x00b8fe94 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe8c"></a> `00b8fe8c` | `40 0f 40 f9` | ldr x0,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00b8fe90"></a> `00b8fe90` | `74 2c 01 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fe94"></a> `00b8fe94` | `a8 03 57 38` | ldurb w8,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00b8fe98"></a> `00b8fe98` | `68 00 00 36` | tbz w8,#0x0,0x00b8fea4 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe9c"></a> `00b8fe9c` | `40 1b 40 f9` | ldr x0,[x26, #0x30] | `FALL_THROUGH`
<a id="insn-00b8fea0"></a> `00b8fea0` | `70 2c 01 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fea4"></a> `00b8fea4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b8fea8"></a> `00b8fea8` | `f4 4f 5d a9` | ldp x20,x19,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00b8feac"></a> `00b8feac` | `f6 57 5c a9` | ldp x22,x21,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00b8feb0"></a> `00b8feb0` | `f8 5f 5b a9` | ldp x24,x23,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00b8feb4"></a> `00b8feb4` | `fa 67 5a a9` | ldp x26,x25,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00b8feb8"></a> `00b8feb8` | `fc 6f 59 a9` | ldp x28,x27,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00b8febc"></a> `00b8febc` | `fd 7b 58 a9` | ldp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00b8fec0"></a> `00b8fec0` | `ff 83 07 91` | add sp,sp,#0x1e0 | `FALL_THROUGH`
<a id="insn-00b8fec4"></a> `00b8fec4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b8fec8"></a> `00b8fec8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b8faec`](#insn-00b8faec) 範囲 `[['00b8faec', '00b8fb33']]`
  - `CONDITIONAL_JUMP` [`00b8fb30`](#insn-00b8fb30) → [`00b8fb54`](#insn-00b8fb54)
  - `FALL_THROUGH` [`00b8fb30`](#insn-00b8fb30) → [`00b8fb34`](#insn-00b8fb34)
- ブロック [`00b8fb34`](#insn-00b8fb34) 範囲 `[['00b8fb34', '00b8fb3b']]`
  - `CONDITIONAL_JUMP` [`00b8fb38`](#insn-00b8fb38) → [`00b8fb4c`](#insn-00b8fb4c)
  - `FALL_THROUGH` [`00b8fb38`](#insn-00b8fb38) → [`00b8fb3c`](#insn-00b8fb3c)
- ブロック [`00b8fb3c`](#insn-00b8fb3c) 範囲 `[['00b8fb3c', '00b8fb43']]`
  - `CONDITIONAL_JUMP` [`00b8fb40`](#insn-00b8fb40) → [`00b8fb5c`](#insn-00b8fb5c)
  - `FALL_THROUGH` [`00b8fb40`](#insn-00b8fb40) → [`00b8fb44`](#insn-00b8fb44)
- ブロック [`00b8fb44`](#insn-00b8fb44) 範囲 `[['00b8fb44', '00b8fb4b']]`
  - `UNCONDITIONAL_JUMP` [`00b8fb48`](#insn-00b8fb48) → [`00b8fb60`](#insn-00b8fb60)
- ブロック [`00b8fb4c`](#insn-00b8fb4c) 範囲 `[['00b8fb4c', '00b8fb53']]`
  - `UNCONDITIONAL_JUMP` [`00b8fb50`](#insn-00b8fb50) → [`00b8fb60`](#insn-00b8fb60)
- ブロック [`00b8fb54`](#insn-00b8fb54) 範囲 `[['00b8fb54', '00b8fb5b']]`
  - `UNCONDITIONAL_JUMP` [`00b8fb58`](#insn-00b8fb58) → [`00b8fb60`](#insn-00b8fb60)
- ブロック [`00b8fb5c`](#insn-00b8fb5c) 範囲 `[['00b8fb5c', '00b8fb5f']]`
  - `FALL_THROUGH` [`00b8fb5c`](#insn-00b8fb5c) → [`00b8fb60`](#insn-00b8fb60)
- ブロック [`00b8fb60`](#insn-00b8fb60) 範囲 `[['00b8fb60', '00b8fbc3']]`
  - `UNCONDITIONAL_JUMP` [`00b8fbc0`](#insn-00b8fbc0) → [`00b8fbcc`](#insn-00b8fbcc)
- ブロック [`00b8fbc4`](#insn-00b8fbc4) 範囲 `[['00b8fbc4', '00b8fbcb']]`
  - `FALL_THROUGH` [`00b8fbc8`](#insn-00b8fbc8) → [`00b8fbcc`](#insn-00b8fbcc)
- ブロック [`00b8fbcc`](#insn-00b8fbcc) 範囲 `[['00b8fbcc', '00b8fbcf']]`
  - `CONDITIONAL_JUMP` [`00b8fbcc`](#insn-00b8fbcc) → [`00b8fbe4`](#insn-00b8fbe4)
  - `FALL_THROUGH` [`00b8fbcc`](#insn-00b8fbcc) → [`00b8fbd0`](#insn-00b8fbd0)
- ブロック [`00b8fbd0`](#insn-00b8fbd0) 範囲 `[['00b8fbd0', '00b8fbdb']]`
  - `CONDITIONAL_JUMP` [`00b8fbd8`](#insn-00b8fbd8) → [`00b8fbf4`](#insn-00b8fbf4)
  - `FALL_THROUGH` [`00b8fbd8`](#insn-00b8fbd8) → [`00b8fbdc`](#insn-00b8fbdc)
- ブロック [`00b8fbdc`](#insn-00b8fbdc) 範囲 `[['00b8fbdc', '00b8fbe3']]`
  - `UNCONDITIONAL_JUMP` [`00b8fbe0`](#insn-00b8fbe0) → [`00b8fc04`](#insn-00b8fc04)
- ブロック [`00b8fbe4`](#insn-00b8fbe4) 範囲 `[['00b8fbe4', '00b8fbeb']]`
  - `CONDITIONAL_JUMP` [`00b8fbe8`](#insn-00b8fbe8) → [`00b8fc14`](#insn-00b8fc14)
  - `FALL_THROUGH` [`00b8fbe8`](#insn-00b8fbe8) → [`00b8fbec`](#insn-00b8fbec)
- ブロック [`00b8fbec`](#insn-00b8fbec) 範囲 `[['00b8fbec', '00b8fbef']]`
  - `CONDITIONAL_JUMP` [`00b8fbec`](#insn-00b8fbec) → [`00b8fc4c`](#insn-00b8fc4c)
  - `FALL_THROUGH` [`00b8fbec`](#insn-00b8fbec) → [`00b8fbf0`](#insn-00b8fbf0)
- ブロック [`00b8fbf0`](#insn-00b8fbf0) 範囲 `[['00b8fbf0', '00b8fbf3']]`
  - `UNCONDITIONAL_JUMP` [`00b8fbf0`](#insn-00b8fbf0) → [`00b8fd90`](#insn-00b8fd90)
- ブロック [`00b8fbf4`](#insn-00b8fbf4) 範囲 `[['00b8fbf4', '00b8fc03']]`
  - `FALL_THROUGH` [`00b8fc00`](#insn-00b8fc00) → [`00b8fc04`](#insn-00b8fc04)
- ブロック [`00b8fc04`](#insn-00b8fc04) 範囲 `[['00b8fc04', '00b8fc13']]`
  - `CONDITIONAL_JUMP` [`00b8fc10`](#insn-00b8fc10) → [`00b8fbec`](#insn-00b8fbec)
  - `FALL_THROUGH` [`00b8fc10`](#insn-00b8fc10) → [`00b8fc14`](#insn-00b8fc14)
- ブロック [`00b8fc14`](#insn-00b8fc14) 範囲 `[['00b8fc14', '00b8fc1f']]`
  - `CONDITIONAL_JUMP` [`00b8fc1c`](#insn-00b8fc1c) → [`00b8fc28`](#insn-00b8fc28)
  - `FALL_THROUGH` [`00b8fc1c`](#insn-00b8fc1c) → [`00b8fc20`](#insn-00b8fc20)
- ブロック [`00b8fc20`](#insn-00b8fc20) 範囲 `[['00b8fc20', '00b8fc27']]`
  - `UNCONDITIONAL_JUMP` [`00b8fc24`](#insn-00b8fc24) → [`00b8fc38`](#insn-00b8fc38)
- ブロック [`00b8fc28`](#insn-00b8fc28) 範囲 `[['00b8fc28', '00b8fc33']]`
  - `FALL_THROUGH` [`00b8fc30`](#insn-00b8fc30) → [`00b8fc34`](#insn-00b8fc34)
- ブロック [`00b8fc34`](#insn-00b8fc34) 範囲 `[['00b8fc34', '00b8fc37']]`
  - `FALL_THROUGH` [`00b8fc34`](#insn-00b8fc34) → [`00b8fc38`](#insn-00b8fc38)
- ブロック [`00b8fc38`](#insn-00b8fc38) 範囲 `[['00b8fc38', '00b8fc47']]`
  - `FALL_THROUGH` [`00b8fc44`](#insn-00b8fc44) → [`00b8fc48`](#insn-00b8fc48)
- ブロック [`00b8fc48`](#insn-00b8fc48) 範囲 `[['00b8fc48', '00b8fc4b']]`
  - `CONDITIONAL_JUMP` [`00b8fc48`](#insn-00b8fc48) → [`00b8fd90`](#insn-00b8fd90)
  - `FALL_THROUGH` [`00b8fc48`](#insn-00b8fc48) → [`00b8fc4c`](#insn-00b8fc4c)
- ブロック [`00b8fc4c`](#insn-00b8fc4c) 範囲 `[['00b8fc4c', '00b8fc6f']]`
  - `CONDITIONAL_JUMP` [`00b8fc6c`](#insn-00b8fc6c) → [`00b8fd24`](#insn-00b8fd24)
  - `FALL_THROUGH` [`00b8fc6c`](#insn-00b8fc6c) → [`00b8fc70`](#insn-00b8fc70)
- ブロック [`00b8fc70`](#insn-00b8fc70) 範囲 `[['00b8fc70', '00b8fc77']]`
  - `CONDITIONAL_JUMP` [`00b8fc74`](#insn-00b8fc74) → [`00b8fc8c`](#insn-00b8fc8c)
  - `FALL_THROUGH` [`00b8fc74`](#insn-00b8fc74) → [`00b8fc78`](#insn-00b8fc78)
- ブロック [`00b8fc78`](#insn-00b8fc78) 範囲 `[['00b8fc78', '00b8fc8b']]`
  - `UNCONDITIONAL_JUMP` [`00b8fc88`](#insn-00b8fc88) → [`00b8fcb0`](#insn-00b8fcb0)
- ブロック [`00b8fc8c`](#insn-00b8fc8c) 範囲 `[['00b8fc8c', '00b8fc93']]`
  - `CONDITIONAL_JUMP` [`00b8fc90`](#insn-00b8fc90) → [`00b8fca4`](#insn-00b8fca4)
  - `FALL_THROUGH` [`00b8fc90`](#insn-00b8fc90) → [`00b8fc94`](#insn-00b8fc94)
- ブロック [`00b8fc94`](#insn-00b8fc94) 範囲 `[['00b8fc94', '00b8fc9f']]`
  - `FALL_THROUGH` [`00b8fc9c`](#insn-00b8fc9c) → [`00b8fca0`](#insn-00b8fca0)
- ブロック [`00b8fca0`](#insn-00b8fca0) 範囲 `[['00b8fca0', '00b8fca3']]`
  - `UNCONDITIONAL_JUMP` [`00b8fca0`](#insn-00b8fca0) → [`00b8fcac`](#insn-00b8fcac)
- ブロック [`00b8fca4`](#insn-00b8fca4) 範囲 `[['00b8fca4', '00b8fcab']]`
  - `FALL_THROUGH` [`00b8fca8`](#insn-00b8fca8) → [`00b8fcac`](#insn-00b8fcac)
- ブロック [`00b8fcac`](#insn-00b8fcac) 範囲 `[['00b8fcac', '00b8fcaf']]`
  - `FALL_THROUGH` [`00b8fcac`](#insn-00b8fcac) → [`00b8fcb0`](#insn-00b8fcb0)
- ブロック [`00b8fcb0`](#insn-00b8fcb0) 範囲 `[['00b8fcb0', '00b8fcbb']]`
  - `FALL_THROUGH` [`00b8fcb8`](#insn-00b8fcb8) → [`00b8fcbc`](#insn-00b8fcbc)
- ブロック [`00b8fcbc`](#insn-00b8fcbc) 範囲 `[['00b8fcbc', '00b8fcdb']]`
  - `CONDITIONAL_JUMP` [`00b8fcd8`](#insn-00b8fcd8) → [`00b8fcec`](#insn-00b8fcec)
  - `FALL_THROUGH` [`00b8fcd8`](#insn-00b8fcd8) → [`00b8fcdc`](#insn-00b8fcdc)
- ブロック [`00b8fcdc`](#insn-00b8fcdc) 範囲 `[['00b8fcdc', '00b8fceb']]`
  - `UNCONDITIONAL_JUMP` [`00b8fce8`](#insn-00b8fce8) → [`00b8fd0c`](#insn-00b8fd0c)
- ブロック [`00b8fcec`](#insn-00b8fcec) 範囲 `[['00b8fcec', '00b8fcef']]`
  - `CONDITIONAL_JUMP` [`00b8fcec`](#insn-00b8fcec) → [`00b8fd00`](#insn-00b8fd00)
  - `FALL_THROUGH` [`00b8fcec`](#insn-00b8fcec) → [`00b8fcf0`](#insn-00b8fcf0)
- ブロック [`00b8fcf0`](#insn-00b8fcf0) 範囲 `[['00b8fcf0', '00b8fcff']]`
  - `UNCONDITIONAL_JUMP` [`00b8fcfc`](#insn-00b8fcfc) → [`00b8fd08`](#insn-00b8fd08)
- ブロック [`00b8fd00`](#insn-00b8fd00) 範囲 `[['00b8fd00', '00b8fd07']]`
  - `FALL_THROUGH` [`00b8fd04`](#insn-00b8fd04) → [`00b8fd08`](#insn-00b8fd08)
- ブロック [`00b8fd08`](#insn-00b8fd08) 範囲 `[['00b8fd08', '00b8fd0b']]`
  - `FALL_THROUGH` [`00b8fd08`](#insn-00b8fd08) → [`00b8fd0c`](#insn-00b8fd0c)
- ブロック [`00b8fd0c`](#insn-00b8fd0c) 範囲 `[['00b8fd0c', '00b8fd23']]`
  - `FALL_THROUGH` [`00b8fd20`](#insn-00b8fd20) → [`00b8fd24`](#insn-00b8fd24)
- ブロック [`00b8fd24`](#insn-00b8fd24) 範囲 `[['00b8fd24', '00b8fd2f']]`
  - `CONDITIONAL_JUMP` [`00b8fd2c`](#insn-00b8fd2c) → [`00b8fd38`](#insn-00b8fd38)
  - `FALL_THROUGH` [`00b8fd2c`](#insn-00b8fd2c) → [`00b8fd30`](#insn-00b8fd30)
- ブロック [`00b8fd30`](#insn-00b8fd30) 範囲 `[['00b8fd30', '00b8fd37']]`
  - `UNCONDITIONAL_JUMP` [`00b8fd34`](#insn-00b8fd34) → [`00b8fd48`](#insn-00b8fd48)
- ブロック [`00b8fd38`](#insn-00b8fd38) 範囲 `[['00b8fd38', '00b8fd47']]`
  - `FALL_THROUGH` [`00b8fd44`](#insn-00b8fd44) → [`00b8fd48`](#insn-00b8fd48)
- ブロック [`00b8fd48`](#insn-00b8fd48) 範囲 `[['00b8fd48', '00b8fd4b']]`
  - `FALL_THROUGH` [`00b8fd48`](#insn-00b8fd48) → [`00b8fd4c`](#insn-00b8fd4c)
- ブロック [`00b8fd4c`](#insn-00b8fd4c) 範囲 `[['00b8fd4c', '00b8fd6f']]`
  - `CONDITIONAL_JUMP` [`00b8fd6c`](#insn-00b8fd6c) → [`00b8fd90`](#insn-00b8fd90)
  - `FALL_THROUGH` [`00b8fd6c`](#insn-00b8fd6c) → [`00b8fd70`](#insn-00b8fd70)
- ブロック [`00b8fd70`](#insn-00b8fd70) 範囲 `[['00b8fd70', '00b8fd77']]`
  - `FALL_THROUGH` [`00b8fd74`](#insn-00b8fd74) → [`00b8fd78`](#insn-00b8fd78)
- ブロック [`00b8fd78`](#insn-00b8fd78) 範囲 `[['00b8fd78', '00b8fd7b']]`
  - `CONDITIONAL_JUMP` [`00b8fd78`](#insn-00b8fd78) → [`00b8fbc4`](#insn-00b8fbc4)
  - `FALL_THROUGH` [`00b8fd78`](#insn-00b8fd78) → [`00b8fd7c`](#insn-00b8fd7c)
- ブロック [`00b8fd7c`](#insn-00b8fd7c) 範囲 `[['00b8fd7c', '00b8fd8f']]`
  - `UNCONDITIONAL_JUMP` [`00b8fd8c`](#insn-00b8fd8c) → [`00b8fbcc`](#insn-00b8fbcc)
- ブロック [`00b8fd90`](#insn-00b8fd90) 範囲 `[['00b8fd90', '00b8fda7']]`
  - `FALL_THROUGH` [`00b8fda4`](#insn-00b8fda4) → [`00b8fda8`](#insn-00b8fda8)
- ブロック [`00b8fda8`](#insn-00b8fda8) 範囲 `[['00b8fda8', '00b8fdab']]`
  - `CONDITIONAL_JUMP` [`00b8fda8`](#insn-00b8fda8) → [`00b8fdcc`](#insn-00b8fdcc)
  - `FALL_THROUGH` [`00b8fda8`](#insn-00b8fda8) → [`00b8fdac`](#insn-00b8fdac)
- ブロック [`00b8fdac`](#insn-00b8fdac) 範囲 `[['00b8fdac', '00b8fdbf']]`
  - `CONDITIONAL_JUMP` [`00b8fdbc`](#insn-00b8fdbc) → [`00b8fdcc`](#insn-00b8fdcc)
  - `FALL_THROUGH` [`00b8fdbc`](#insn-00b8fdbc) → [`00b8fdc0`](#insn-00b8fdc0)
- ブロック [`00b8fdc0`](#insn-00b8fdc0) 範囲 `[['00b8fdc0', '00b8fdcb']]`
  - `FALL_THROUGH` [`00b8fdc8`](#insn-00b8fdc8) → [`00b8fdcc`](#insn-00b8fdcc)
- ブロック [`00b8fdcc`](#insn-00b8fdcc) 範囲 `[['00b8fdcc', '00b8fdff']]`
  - `CONDITIONAL_JUMP` [`00b8fdfc`](#insn-00b8fdfc) → [`00b8fe14`](#insn-00b8fe14)
  - `FALL_THROUGH` [`00b8fdfc`](#insn-00b8fdfc) → [`00b8fe00`](#insn-00b8fe00)
- ブロック [`00b8fe00`](#insn-00b8fe00) 範囲 `[['00b8fe00', '00b8fe0b']]`
  - `CONDITIONAL_JUMP` [`00b8fe08`](#insn-00b8fe08) → [`00b8fe24`](#insn-00b8fe24)
  - `FALL_THROUGH` [`00b8fe08`](#insn-00b8fe08) → [`00b8fe0c`](#insn-00b8fe0c)
- ブロック [`00b8fe0c`](#insn-00b8fe0c) 範囲 `[['00b8fe0c', '00b8fe13']]`
  - `UNCONDITIONAL_JUMP` [`00b8fe10`](#insn-00b8fe10) → [`00b8fe34`](#insn-00b8fe34)
- ブロック [`00b8fe14`](#insn-00b8fe14) 範囲 `[['00b8fe14', '00b8fe1b']]`
  - `CONDITIONAL_JUMP` [`00b8fe18`](#insn-00b8fe18) → [`00b8fe44`](#insn-00b8fe44)
  - `FALL_THROUGH` [`00b8fe18`](#insn-00b8fe18) → [`00b8fe1c`](#insn-00b8fe1c)
- ブロック [`00b8fe1c`](#insn-00b8fe1c) 範囲 `[['00b8fe1c', '00b8fe1f']]`
  - `CONDITIONAL_JUMP` [`00b8fe1c`](#insn-00b8fe1c) → [`00b8fe78`](#insn-00b8fe78)
  - `FALL_THROUGH` [`00b8fe1c`](#insn-00b8fe1c) → [`00b8fe20`](#insn-00b8fe20)
- ブロック [`00b8fe20`](#insn-00b8fe20) 範囲 `[['00b8fe20', '00b8fe23']]`
  - `UNCONDITIONAL_JUMP` [`00b8fe20`](#insn-00b8fe20) → [`00b8fe84`](#insn-00b8fe84)
- ブロック [`00b8fe24`](#insn-00b8fe24) 範囲 `[['00b8fe24', '00b8fe33']]`
  - `FALL_THROUGH` [`00b8fe30`](#insn-00b8fe30) → [`00b8fe34`](#insn-00b8fe34)
- ブロック [`00b8fe34`](#insn-00b8fe34) 範囲 `[['00b8fe34', '00b8fe43']]`
  - `CONDITIONAL_JUMP` [`00b8fe40`](#insn-00b8fe40) → [`00b8fe1c`](#insn-00b8fe1c)
  - `FALL_THROUGH` [`00b8fe40`](#insn-00b8fe40) → [`00b8fe44`](#insn-00b8fe44)
- ブロック [`00b8fe44`](#insn-00b8fe44) 範囲 `[['00b8fe44', '00b8fe4f']]`
  - `CONDITIONAL_JUMP` [`00b8fe4c`](#insn-00b8fe4c) → [`00b8fe58`](#insn-00b8fe58)
  - `FALL_THROUGH` [`00b8fe4c`](#insn-00b8fe4c) → [`00b8fe50`](#insn-00b8fe50)
- ブロック [`00b8fe50`](#insn-00b8fe50) 範囲 `[['00b8fe50', '00b8fe57']]`
  - `UNCONDITIONAL_JUMP` [`00b8fe54`](#insn-00b8fe54) → [`00b8fe68`](#insn-00b8fe68)
- ブロック [`00b8fe58`](#insn-00b8fe58) 範囲 `[['00b8fe58', '00b8fe67']]`
  - `FALL_THROUGH` [`00b8fe64`](#insn-00b8fe64) → [`00b8fe68`](#insn-00b8fe68)
- ブロック [`00b8fe68`](#insn-00b8fe68) 範囲 `[['00b8fe68', '00b8fe77']]`
  - `CONDITIONAL_JUMP` [`00b8fe74`](#insn-00b8fe74) → [`00b8fe84`](#insn-00b8fe84)
  - `FALL_THROUGH` [`00b8fe74`](#insn-00b8fe74) → [`00b8fe78`](#insn-00b8fe78)
- ブロック [`00b8fe78`](#insn-00b8fe78) 範囲 `[['00b8fe78', '00b8fe83']]`
  - `FALL_THROUGH` [`00b8fe80`](#insn-00b8fe80) → [`00b8fe84`](#insn-00b8fe84)
- ブロック [`00b8fe84`](#insn-00b8fe84) 範囲 `[['00b8fe84', '00b8fe87']]`
  - `FALL_THROUGH` [`00b8fe84`](#insn-00b8fe84) → [`00b8fe88`](#insn-00b8fe88)
- ブロック [`00b8fe88`](#insn-00b8fe88) 範囲 `[['00b8fe88', '00b8fe8b']]`
  - `CONDITIONAL_JUMP` [`00b8fe88`](#insn-00b8fe88) → [`00b8fe94`](#insn-00b8fe94)
  - `FALL_THROUGH` [`00b8fe88`](#insn-00b8fe88) → [`00b8fe8c`](#insn-00b8fe8c)
- ブロック [`00b8fe8c`](#insn-00b8fe8c) 範囲 `[['00b8fe8c', '00b8fe8f']]`
  - `FALL_THROUGH` [`00b8fe8c`](#insn-00b8fe8c) → [`00b8fe90`](#insn-00b8fe90)
- ブロック [`00b8fe90`](#insn-00b8fe90) 範囲 `[['00b8fe90', '00b8fe93']]`
  - `FALL_THROUGH` [`00b8fe90`](#insn-00b8fe90) → [`00b8fe94`](#insn-00b8fe94)
- ブロック [`00b8fe94`](#insn-00b8fe94) 範囲 `[['00b8fe94', '00b8fe9b']]`
  - `CONDITIONAL_JUMP` [`00b8fe98`](#insn-00b8fe98) → [`00b8fea4`](#insn-00b8fea4)
  - `FALL_THROUGH` [`00b8fe98`](#insn-00b8fe98) → [`00b8fe9c`](#insn-00b8fe9c)
- ブロック [`00b8fe9c`](#insn-00b8fe9c) 範囲 `[['00b8fe9c', '00b8fe9f']]`
  - `FALL_THROUGH` [`00b8fe9c`](#insn-00b8fe9c) → [`00b8fea0`](#insn-00b8fea0)
- ブロック [`00b8fea0`](#insn-00b8fea0) 範囲 `[['00b8fea0', '00b8fea3']]`
  - `FALL_THROUGH` [`00b8fea0`](#insn-00b8fea0) → [`00b8fea4`](#insn-00b8fea4)
- ブロック [`00b8fea4`](#insn-00b8fea4) 範囲 `[['00b8fea4', '00b8feb7']]`
  - `FALL_THROUGH` [`00b8feb4`](#insn-00b8feb4) → [`00b8feb8`](#insn-00b8feb8)
- ブロック [`00b8feb8`](#insn-00b8feb8) 範囲 `[['00b8feb8', '00b8febf']]`
  - `FALL_THROUGH` [`00b8febc`](#insn-00b8febc) → [`00b8fec0`](#insn-00b8fec0)
- ブロック [`00b8fec0`](#insn-00b8fec0) 範囲 `[['00b8fec0', '00b8fec7']]`
  - `FALL_THROUGH` [`00b8fec4`](#insn-00b8fec4) → [`00b8fec8`](#insn-00b8fec8)
- ブロック [`00b8fec8`](#insn-00b8fec8) 範囲 `[['00b8fec8', '00b8fecb']]`

## 命令位置別の参照

- [`00b8faf4`](#insn-00b8faf4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8faf8`](#insn-00b8faf8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fafc`](#insn-00b8fafc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb00`](#insn-00b8fb00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb04`](#insn-00b8fb04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb08`](#insn-00b8fb08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb2c`](#insn-00b8fb2c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb30`](#insn-00b8fb30) → [`00b8fb54`](#insn-00b8fb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb38`](#insn-00b8fb38) → [`00b8fb4c`](#insn-00b8fb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb40`](#insn-00b8fb40) → [`00b8fb5c`](#insn-00b8fb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb48`](#insn-00b8fb48) → [`00b8fb60`](#insn-00b8fb60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb50`](#insn-00b8fb50) → [`00b8fb60`](#insn-00b8fb60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb58`](#insn-00b8fb58) → [`00b8fb60`](#insn-00b8fb60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb6c`](#insn-00b8fb6c) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb74`](#insn-00b8fb74) → [`00be15a0`](../00be1/00be15a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be15a0` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb78`](#insn-00b8fb78) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb7c`](#insn-00b8fb7c) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb90`](#insn-00b8fb90) → [`00bdefc0`](../00bde/00bdefc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdefc0` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb94`](#insn-00b8fb94) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fb98`](#insn-00b8fb98) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fba8`](#insn-00b8fba8) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbb0`](#insn-00b8fbb0) → `Stack[-0x1bc]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbbc`](#insn-00b8fbbc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbc0`](#insn-00b8fbc0) → [`00b8fbcc`](#insn-00b8fbcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbcc`](#insn-00b8fbcc) → [`00b8fbe4`](#insn-00b8fbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbd8`](#insn-00b8fbd8) → [`00b8fbf4`](#insn-00b8fbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbe0`](#insn-00b8fbe0) → [`00b8fc04`](#insn-00b8fc04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbe8`](#insn-00b8fbe8) → [`00b8fc14`](#insn-00b8fc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbec`](#insn-00b8fbec) → [`00b8fc4c`](#insn-00b8fc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fbf0`](#insn-00b8fbf0) → [`00b8fd90`](#insn-00b8fd90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc10`](#insn-00b8fc10) → [`00b8fbec`](#insn-00b8fbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc1c`](#insn-00b8fc1c) → [`00b8fc28`](#insn-00b8fc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc24`](#insn-00b8fc24) → [`00b8fc38`](#insn-00b8fc38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc48`](#insn-00b8fc48) → [`00b8fd90`](#insn-00b8fd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc4c`](#insn-00b8fc4c) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc50`](#insn-00b8fc50) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc54`](#insn-00b8fc54) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc6c`](#insn-00b8fc6c) → [`00b8fd24`](#insn-00b8fd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc74`](#insn-00b8fc74) → [`00b8fc8c`](#insn-00b8fc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc84`](#insn-00b8fc84) → [`00bdefc0`](../00bde/00bdefc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdefc0` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc88`](#insn-00b8fc88) → [`00b8fcb0`](#insn-00b8fcb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc90`](#insn-00b8fc90) → [`00b8fca4`](#insn-00b8fca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fc98`](#insn-00b8fc98) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fca0`](#insn-00b8fca0) → [`00b8fcac`](#insn-00b8fcac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fca4`](#insn-00b8fca4) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fca8`](#insn-00b8fca8) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fcb0`](#insn-00b8fcb0) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fcb4`](#insn-00b8fcb4) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fcd8`](#insn-00b8fcd8) → [`00b8fcec`](#insn-00b8fcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fce4`](#insn-00b8fce4) → [`00bdefc0`](../00bde/00bdefc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdefc0` · 推定シンボル `None` · 推定型 `None`
- [`00b8fce8`](#insn-00b8fce8) → [`00b8fd0c`](#insn-00b8fd0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fcec`](#insn-00b8fcec) → [`00b8fd00`](#insn-00b8fd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fcf4`](#insn-00b8fcf4) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fcfc`](#insn-00b8fcfc) → [`00b8fd08`](#insn-00b8fd08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd00`](#insn-00b8fd00) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd04`](#insn-00b8fd04) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd0c`](#insn-00b8fd0c) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd10`](#insn-00b8fd10) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd20`](#insn-00b8fd20) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd2c`](#insn-00b8fd2c) → [`00b8fd38`](#insn-00b8fd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd34`](#insn-00b8fd34) → [`00b8fd48`](#insn-00b8fd48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd48`](#insn-00b8fd48) → `Stack[-0x6c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd64`](#insn-00b8fd64) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd68`](#insn-00b8fd68) → [`00be15b0`](../00be1/00be15b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be15b0` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd6c`](#insn-00b8fd6c) → [`00b8fd90`](#insn-00b8fd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd78`](#insn-00b8fd78) → [`00b8fbc4`](#insn-00b8fbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd8c`](#insn-00b8fd8c) → [`00b8fbcc`](#insn-00b8fbcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd90`](#insn-00b8fd90) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd94`](#insn-00b8fd94) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fd98`](#insn-00b8fd98) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fda8`](#insn-00b8fda8) → [`00b8fdcc`](#insn-00b8fdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdac`](#insn-00b8fdac) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdbc`](#insn-00b8fdbc) → [`00b8fdcc`](#insn-00b8fdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdc0`](#insn-00b8fdc0) → `Stack[-0x1bc]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdc8`](#insn-00b8fdc8) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdcc`](#insn-00b8fdcc) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fddc`](#insn-00b8fddc) → [`00bb9940`](../00bb9/00bb9940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb9940` · 推定シンボル `None` · 推定型 `None`
- [`00b8fde0`](#insn-00b8fde0) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fde4`](#insn-00b8fde4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdf8`](#insn-00b8fdf8) → [`00be1540`](../00be1/00be1540.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1540` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdfc`](#insn-00b8fdfc) → [`00b8fe14`](#insn-00b8fe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe08`](#insn-00b8fe08) → [`00b8fe24`](#insn-00b8fe24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe10`](#insn-00b8fe10) → [`00b8fe34`](#insn-00b8fe34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe18`](#insn-00b8fe18) → [`00b8fe44`](#insn-00b8fe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe1c`](#insn-00b8fe1c) → [`00b8fe78`](#insn-00b8fe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe20`](#insn-00b8fe20) → [`00b8fe84`](#insn-00b8fe84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe40`](#insn-00b8fe40) → [`00b8fe1c`](#insn-00b8fe1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe4c`](#insn-00b8fe4c) → [`00b8fe58`](#insn-00b8fe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe54`](#insn-00b8fe54) → [`00b8fe68`](#insn-00b8fe68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe74`](#insn-00b8fe74) → [`00b8fe84`](#insn-00b8fe84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe84`](#insn-00b8fe84) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe88`](#insn-00b8fe88) → [`00b8fe94`](#insn-00b8fe94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe8c`](#insn-00b8fe8c) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe90`](#insn-00b8fe90) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe94`](#insn-00b8fe94) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe98`](#insn-00b8fe98) → [`00b8fea4`](#insn-00b8fea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe9c`](#insn-00b8fe9c) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fea0`](#insn-00b8fea0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b8fea8`](#insn-00b8fea8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8feac`](#insn-00b8feac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8feb0`](#insn-00b8feb0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8feb4`](#insn-00b8feb4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8feb8`](#insn-00b8feb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8febc`](#insn-00b8febc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b8faf4`](#insn-00b8faf4)

~~~json
{
  "source": "00b8faf4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8faf8`](#insn-00b8faf8)

~~~json
{
  "source": "00b8faf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fafc`](#insn-00b8fafc)

~~~json
{
  "source": "00b8fafc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb00`](#insn-00b8fb00)

~~~json
{
  "source": "00b8fb00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb04`](#insn-00b8fb04)

~~~json
{
  "source": "00b8fb04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb08`](#insn-00b8fb08)

~~~json
{
  "source": "00b8fb08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb2c`](#insn-00b8fb2c)

~~~json
{
  "source": "00b8fb2c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb30`](#insn-00b8fb30)

~~~json
{
  "source": "00b8fb30",
  "target": "00b8fb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb38`](#insn-00b8fb38)

~~~json
{
  "source": "00b8fb38",
  "target": "00b8fb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb40`](#insn-00b8fb40)

~~~json
{
  "source": "00b8fb40",
  "target": "00b8fb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb48`](#insn-00b8fb48)

~~~json
{
  "source": "00b8fb48",
  "target": "00b8fb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb50`](#insn-00b8fb50)

~~~json
{
  "source": "00b8fb50",
  "target": "00b8fb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb58`](#insn-00b8fb58)

~~~json
{
  "source": "00b8fb58",
  "target": "00b8fb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb6c`](#insn-00b8fb6c)

~~~json
{
  "source": "00b8fb6c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb74`](#insn-00b8fb74)

~~~json
{
  "source": "00b8fb74",
  "target": "00be15a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fb78`](#insn-00b8fb78)

~~~json
{
  "source": "00b8fb78",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb7c`](#insn-00b8fb7c)

~~~json
{
  "source": "00b8fb7c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb90`](#insn-00b8fb90)

~~~json
{
  "source": "00b8fb90",
  "target": "00bdefc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fb94`](#insn-00b8fb94)

~~~json
{
  "source": "00b8fb94",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fb98`](#insn-00b8fb98)

~~~json
{
  "source": "00b8fb98",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fba8`](#insn-00b8fba8)

~~~json
{
  "source": "00b8fba8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbb0`](#insn-00b8fbb0)

~~~json
{
  "source": "00b8fbb0",
  "target": "Stack[-0x1bc]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbbc`](#insn-00b8fbbc)

~~~json
{
  "source": "00b8fbbc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbc0`](#insn-00b8fbc0)

~~~json
{
  "source": "00b8fbc0",
  "target": "00b8fbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbcc`](#insn-00b8fbcc)

~~~json
{
  "source": "00b8fbcc",
  "target": "00b8fbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbd8`](#insn-00b8fbd8)

~~~json
{
  "source": "00b8fbd8",
  "target": "00b8fbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbe0`](#insn-00b8fbe0)

~~~json
{
  "source": "00b8fbe0",
  "target": "00b8fc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbe8`](#insn-00b8fbe8)

~~~json
{
  "source": "00b8fbe8",
  "target": "00b8fc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbec`](#insn-00b8fbec)

~~~json
{
  "source": "00b8fbec",
  "target": "00b8fc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fbf0`](#insn-00b8fbf0)

~~~json
{
  "source": "00b8fbf0",
  "target": "00b8fd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc10`](#insn-00b8fc10)

~~~json
{
  "source": "00b8fc10",
  "target": "00b8fbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc1c`](#insn-00b8fc1c)

~~~json
{
  "source": "00b8fc1c",
  "target": "00b8fc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc24`](#insn-00b8fc24)

~~~json
{
  "source": "00b8fc24",
  "target": "00b8fc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc48`](#insn-00b8fc48)

~~~json
{
  "source": "00b8fc48",
  "target": "00b8fd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc4c`](#insn-00b8fc4c)

~~~json
{
  "source": "00b8fc4c",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc50`](#insn-00b8fc50)

~~~json
{
  "source": "00b8fc50",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc54`](#insn-00b8fc54)

~~~json
{
  "source": "00b8fc54",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc6c`](#insn-00b8fc6c)

~~~json
{
  "source": "00b8fc6c",
  "target": "00b8fd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc74`](#insn-00b8fc74)

~~~json
{
  "source": "00b8fc74",
  "target": "00b8fc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc84`](#insn-00b8fc84)

~~~json
{
  "source": "00b8fc84",
  "target": "00bdefc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fc88`](#insn-00b8fc88)

~~~json
{
  "source": "00b8fc88",
  "target": "00b8fcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc90`](#insn-00b8fc90)

~~~json
{
  "source": "00b8fc90",
  "target": "00b8fca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fc98`](#insn-00b8fc98)

~~~json
{
  "source": "00b8fc98",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fca0`](#insn-00b8fca0)

~~~json
{
  "source": "00b8fca0",
  "target": "00b8fcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fca4`](#insn-00b8fca4)

~~~json
{
  "source": "00b8fca4",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fca8`](#insn-00b8fca8)

~~~json
{
  "source": "00b8fca8",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fcb0`](#insn-00b8fcb0)

~~~json
{
  "source": "00b8fcb0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fcb4`](#insn-00b8fcb4)

~~~json
{
  "source": "00b8fcb4",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fcd8`](#insn-00b8fcd8)

~~~json
{
  "source": "00b8fcd8",
  "target": "00b8fcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fce4`](#insn-00b8fce4)

~~~json
{
  "source": "00b8fce4",
  "target": "00bdefc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fce8`](#insn-00b8fce8)

~~~json
{
  "source": "00b8fce8",
  "target": "00b8fd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fcec`](#insn-00b8fcec)

~~~json
{
  "source": "00b8fcec",
  "target": "00b8fd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fcf4`](#insn-00b8fcf4)

~~~json
{
  "source": "00b8fcf4",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fcfc`](#insn-00b8fcfc)

~~~json
{
  "source": "00b8fcfc",
  "target": "00b8fd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd00`](#insn-00b8fd00)

~~~json
{
  "source": "00b8fd00",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd04`](#insn-00b8fd04)

~~~json
{
  "source": "00b8fd04",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd0c`](#insn-00b8fd0c)

~~~json
{
  "source": "00b8fd0c",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd10`](#insn-00b8fd10)

~~~json
{
  "source": "00b8fd10",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd20`](#insn-00b8fd20)

~~~json
{
  "source": "00b8fd20",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd2c`](#insn-00b8fd2c)

~~~json
{
  "source": "00b8fd2c",
  "target": "00b8fd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd34`](#insn-00b8fd34)

~~~json
{
  "source": "00b8fd34",
  "target": "00b8fd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd48`](#insn-00b8fd48)

~~~json
{
  "source": "00b8fd48",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd64`](#insn-00b8fd64)

~~~json
{
  "source": "00b8fd64",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd68`](#insn-00b8fd68)

~~~json
{
  "source": "00b8fd68",
  "target": "00be15b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fd6c`](#insn-00b8fd6c)

~~~json
{
  "source": "00b8fd6c",
  "target": "00b8fd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd78`](#insn-00b8fd78)

~~~json
{
  "source": "00b8fd78",
  "target": "00b8fbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd8c`](#insn-00b8fd8c)

~~~json
{
  "source": "00b8fd8c",
  "target": "00b8fbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd90`](#insn-00b8fd90)

~~~json
{
  "source": "00b8fd90",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd94`](#insn-00b8fd94)

~~~json
{
  "source": "00b8fd94",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fd98`](#insn-00b8fd98)

~~~json
{
  "source": "00b8fd98",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fda8`](#insn-00b8fda8)

~~~json
{
  "source": "00b8fda8",
  "target": "00b8fdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdac`](#insn-00b8fdac)

~~~json
{
  "source": "00b8fdac",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdbc`](#insn-00b8fdbc)

~~~json
{
  "source": "00b8fdbc",
  "target": "00b8fdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdc0`](#insn-00b8fdc0)

~~~json
{
  "source": "00b8fdc0",
  "target": "Stack[-0x1bc]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdc8`](#insn-00b8fdc8)

~~~json
{
  "source": "00b8fdc8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdcc`](#insn-00b8fdcc)

~~~json
{
  "source": "00b8fdcc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fddc`](#insn-00b8fddc)

~~~json
{
  "source": "00b8fddc",
  "target": "00bb9940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fde0`](#insn-00b8fde0)

~~~json
{
  "source": "00b8fde0",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fde4`](#insn-00b8fde4)

~~~json
{
  "source": "00b8fde4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdf8`](#insn-00b8fdf8)

~~~json
{
  "source": "00b8fdf8",
  "target": "00be1540",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fdfc`](#insn-00b8fdfc)

~~~json
{
  "source": "00b8fdfc",
  "target": "00b8fe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe08`](#insn-00b8fe08)

~~~json
{
  "source": "00b8fe08",
  "target": "00b8fe24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe10`](#insn-00b8fe10)

~~~json
{
  "source": "00b8fe10",
  "target": "00b8fe34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe18`](#insn-00b8fe18)

~~~json
{
  "source": "00b8fe18",
  "target": "00b8fe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe1c`](#insn-00b8fe1c)

~~~json
{
  "source": "00b8fe1c",
  "target": "00b8fe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe20`](#insn-00b8fe20)

~~~json
{
  "source": "00b8fe20",
  "target": "00b8fe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe40`](#insn-00b8fe40)

~~~json
{
  "source": "00b8fe40",
  "target": "00b8fe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe4c`](#insn-00b8fe4c)

~~~json
{
  "source": "00b8fe4c",
  "target": "00b8fe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe54`](#insn-00b8fe54)

~~~json
{
  "source": "00b8fe54",
  "target": "00b8fe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe74`](#insn-00b8fe74)

~~~json
{
  "source": "00b8fe74",
  "target": "00b8fe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe84`](#insn-00b8fe84)

~~~json
{
  "source": "00b8fe84",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe88`](#insn-00b8fe88)

~~~json
{
  "source": "00b8fe88",
  "target": "00b8fe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe8c`](#insn-00b8fe8c)

~~~json
{
  "source": "00b8fe8c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe90`](#insn-00b8fe90)

~~~json
{
  "source": "00b8fe90",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fe94`](#insn-00b8fe94)

~~~json
{
  "source": "00b8fe94",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe98`](#insn-00b8fe98)

~~~json
{
  "source": "00b8fe98",
  "target": "00b8fea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe9c`](#insn-00b8fe9c)

~~~json
{
  "source": "00b8fe9c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fea0`](#insn-00b8fea0)

~~~json
{
  "source": "00b8fea0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fea8`](#insn-00b8fea8)

~~~json
{
  "source": "00b8fea8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8feac`](#insn-00b8feac)

~~~json
{
  "source": "00b8feac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8feb0`](#insn-00b8feb0)

~~~json
{
  "source": "00b8feb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8feb4`](#insn-00b8feb4)

~~~json
{
  "source": "00b8feb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8feb8`](#insn-00b8feb8)

~~~json
{
  "source": "00b8feb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8febc`](#insn-00b8febc)

~~~json
{
  "source": "00b8febc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
