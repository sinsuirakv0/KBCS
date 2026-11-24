# 00c1afec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c1abc4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1abc4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0043.md#compare-2aa385e055230e2d5ed499c24a75a89d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c1b088`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b088.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0043.md#compare-f273a5a0873f105646ae2686d5d662b9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c1afec",
  "name": "FUN_00c1afec",
  "size": 800,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3cbd0d3b3dd63b8a10086e1dd2a708c951d9d269ca740eeff67babd77df8523f",
  "source_text_sha256": "3cbd0d3b3dd63b8a10086e1dd2a708c951d9d269ca740eeff67babd77df8523f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c1afec",
        "00c1b30b"
      ]
    ],
    "bytes_sha256": "59c42b62570714d953e8f5ea60cb23e206b34df6af9c71d87505489b534a64c4",
    "instruction_count": 200,
    "instruction_bytes": 800,
    "body_bytes": 800,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c1acc0](../00c1a/00c1acc0.md)

## 呼び出し先

- [006d76a0](../006d7/006d76a0.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c58000](../00c58/00c58000.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5dff0](../00c5d/00c5dff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5681 bytes

~~~c

ulong * FUN_00c1afec(ulong *param_1,undefined4 *param_2,undefined4 *param_3)

{
  size_t __n;
  ulong uVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  undefined8 *puVar5;
  bool bVar6;
  undefined8 uVar7;
  uint uVar8;
  undefined4 *puVar9;
  undefined4 *puVar10;
  ulong uVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  ulong uVar14;
  void *pvVar15;
  byte bVar16;
  ulong uVar17;
  ulong uVar18;
  undefined4 *puVar19;
  long lVar20;
  undefined8 uVar21;
  undefined8 uVar22;
  ulong local_78;
  ulong local_70;
  void *local_68;
  
  uVar4 = *param_1;
  uVar14 = param_1[1];
                    /* try { // try from 00c1b020 to 00d1b02b has its CatchHandler @ 00c1b738 */
  bVar6 = ((byte)*param_1 & 1) != 0;
  lVar20 = (uVar4 & 0xfffffffffffffffe) - 1;
  uVar2 = (ulong)(byte)((byte)*param_1 >> 1);
                    /* try { // try from 00c1b02c to 00d1b0d7 has its CatchHandler @ 00c1b79c */
  if (bVar6) {
    uVar2 = uVar14;
  }
  lVar3 = 4;
  if (bVar6) {
    lVar3 = lVar20;
  }
  uVar11 = (long)param_3 - (long)param_2;
  if (uVar11 == 0) {
    return param_1;
  }
  puVar19 = (undefined4 *)param_1[2];
  uVar8 = (uint)uVar4;
  puVar10 = (undefined4 *)((long)param_1 + 4);
  uVar18 = uVar4 >> 1 & 0x7f;
  uVar17 = (long)uVar11 >> 2;
  uVar1 = uVar18;
  puVar9 = puVar10;
  if ((uVar4 & 1) != 0) {
    uVar1 = uVar14;
    puVar9 = puVar19;
  }
  if ((puVar9 <= param_2) && (param_2 < puVar9 + uVar1 + 1)) {
    if (0x3ffffffffffffff7 < uVar17) {
      uVar7 = FUN_006d76a0(&local_78);
      if ((local_78 & 1) != 0) {
        _ZdlPv(local_68);
      }
                    /* WARNING: Subroutine does not return */
      FUN_00c53f5c(uVar7);
    }
    if (uVar17 < 5) {
      pvVar15 = (void *)((ulong)&local_78 | 4);
      local_78 = CONCAT71(local_78._1_7_,(char)(uVar11 >> 1)) & 0xfffffffffffffffe;
    }
    else {
                    /* try { // try from 00c1b134 to 00d1b13f has its CatchHandler @ 00c1b734 */
                    /* try { // try from 00c1b140 to 00d1b14f has its CatchHandler @ 00c1b720 */
      uVar2 = (uVar17 & 0x3ffffffffffffffe) + 2;
      if ((uVar17 | 1) != 5) {
        uVar2 = uVar17 | 1;
      }
                    /* try { // try from 00c1b150 to 00d1b163 has its CatchHandler @ 00c1b708 */
      pvVar15 = (void *)_Znwm((uVar2 + 1) * 4);
      local_78 = uVar2 + 1 | 1;
      local_70 = uVar17;
      local_68 = pvVar15;
    }
    __n = (uVar11 - 4 & 0xfffffffffffffffc) + 4;
    memcpy(pvVar15,param_2,__n);
    *(undefined4 *)((long)pvVar15 + __n) = 0;
    bVar16 = (byte)local_78 & 1;
    uVar2 = (ulong)((byte)local_78 >> 1);
    pvVar15 = (void *)((ulong)&local_78 | 4);
    if ((local_78 & 1) != 0) {
      uVar2 = local_70;
      pvVar15 = local_68;
    }
    lVar3 = 4;
    if ((uVar4 & 1) != 0) {
      lVar3 = lVar20;
    }
                    /* try { // try from 00c1b1c4 to 00d1b1cf has its CatchHandler @ 00c1b7bc */
    if ((uVar4 & 1) != 0) {
      uVar18 = uVar14;
    }
                    /* try { // try from 00c1b1d0 to 00d1b1df has its CatchHandler @ 00c1b7c0 */
    if (lVar3 - uVar18 < uVar2) {
      _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw
                (param_1,lVar3,(uVar2 - lVar3) + uVar18,uVar18,uVar18,0);
                    /* try { // try from 00c1b1f4 to 00d1b1fb has its CatchHandler @ 00c1b7a0 */
      bVar16 = (byte)local_78 & 1;
    }
    else if (uVar2 != 0) {
      if ((uVar4 & 1) != 0) {
        puVar10 = puVar19;
      }
      memmove(puVar10 + uVar18,pvVar15,uVar2 << 2);
      uVar18 = uVar18 + uVar2;
      if ((*param_1 & 1) == 0) {
        *(char *)param_1 = (char)((int)uVar18 << 1);
                    /* try { // try from 00c1b230 to 00d1b23b has its CatchHandler @ 00c1b704 */
      }
      else {
        param_1[1] = uVar18;
      }
      puVar10[uVar18] = 0;
    }
    if (bVar16 == 0) {
      return param_1;
    }
    _ZdlPv(local_68);
    return param_1;
  }
  if (lVar3 - uVar2 < uVar17) {
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm
              (param_1,lVar3,(uVar2 + uVar17) - lVar3,uVar2,uVar2,0,0);
    puVar19 = (undefined4 *)param_1[2];
    param_1[1] = uVar2;
    uVar8 = (uint)(byte)*param_1;
  }
                    /* try { // try from 00c1b0fc to 00d1b103 has its CatchHandler @ 00c1b7a0 */
  if ((uVar8 & 1) != 0) {
    puVar10 = puVar19;
  }
  puVar9 = puVar10 + uVar2;
  if ((0x1b < uVar11 - 4) && (0x1f < (long)puVar10 + (uVar2 * 4 - (long)param_2))) {
    puVar12 = (undefined8 *)(puVar10 + uVar2 + 4);
                    /* try { // try from 00c1b23c to 00d1b24b has its CatchHandler @ 00c1b6f0 */
    uVar4 = (uVar11 - 4 >> 2) + 1;
    uVar11 = uVar4 & 0x7ffffffffffffff8;
                    /* try { // try from 00c1b24c to 00d1b25f has its CatchHandler @ 00c1b6d8 */
    puVar9 = puVar9 + uVar11;
    puVar13 = (undefined8 *)(param_2 + 4);
    uVar14 = uVar11;
    do {
      puVar5 = puVar13 + -1;
      uVar7 = puVar13[-2];
      uVar22 = puVar13[1];
      uVar21 = *puVar13;
      uVar14 = uVar14 - 8;
      puVar13 = puVar13 + 4;
      puVar12[-1] = *puVar5;
      puVar12[-2] = uVar7;
      puVar12[1] = uVar22;
      *puVar12 = uVar21;
      puVar12 = puVar12 + 4;
    } while (uVar14 != 0);
    param_2 = param_2 + uVar11;
    if (uVar4 == uVar11) goto LAB_00c1b288;
  }
  do {
    puVar19 = param_2 + 1;
    puVar10 = puVar9 + 1;
    *puVar9 = *param_2;
    puVar9 = puVar10;
    param_2 = puVar19;
  } while (puVar19 != param_3);
LAB_00c1b288:
  *puVar9 = 0;
  if ((*param_1 & 1) == 0) {
    *(char *)param_1 = (char)((int)(uVar2 + uVar17) << 1);
  }
  else {
    param_1[1] = uVar2 + uVar17;
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c1afec"></a> `00c1afec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c1aff0"></a> `00c1aff0` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00c1aff4"></a> `00c1aff4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1aff8"></a> `00c1aff8` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1affc"></a> `00c1affc` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c1b000"></a> `00c1b000` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00c1b004"></a> `00c1b004` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00c1b008"></a> `00c1b008` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00c1b00c"></a> `00c1b00c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00c1b010"></a> `00c1b010` | `18 68 40 a9` | ldp x24,x26,[x0] | `FALL_THROUGH`
<a id="insn-00c1b014"></a> `00c1b014` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c1b018"></a> `00c1b018` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00c1b01c"></a> `00c1b01c` | `09 fd 41 d3` | lsr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b020"></a> `00c1b020` | `0a fb 7f 92` | and x10,x24,#-0x2 | `FALL_THROUGH`
<a id="insn-00c1b024"></a> `00c1b024` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b028"></a> `00c1b028` | `5b 05 00 d1` | sub x27,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b02c"></a> `00c1b02c` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b030"></a> `00c1b030` | `34 01 9a 9a` | csel x20,x9,x26,eq | `FALL_THROUGH`
<a id="insn-00c1b034"></a> `00c1b034` | `08 01 9b 9a` | csel x8,x8,x27,eq | `FALL_THROUGH`
<a id="insn-00c1b038"></a> `00c1b038` | `59 00 01 eb` | subs x25,x2,x1 | `FALL_THROUGH`
<a id="insn-00c1b03c"></a> `00c1b03c` | `20 14 00 54` | b.eq 0x00c1b2c0 | `CONDITIONAL_JUMP`
<a id="insn-00c1b040"></a> `00c1b040` | `77 0a 40 f9` | ldr x23,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c1b044"></a> `00c1b044` | `0b 03 00 72` | ands w11,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b048"></a> `00c1b048` | `7c 12 00 91` | add x28,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b04c"></a> `00c1b04c` | `16 1f 41 d3` | ubfx x22,x24,#0x1,#0x7 | `FALL_THROUGH`
<a id="insn-00c1b050"></a> `00c1b050` | `35 ff 42 93` | asr x21,x25,#0x2 | `FALL_THROUGH`
<a id="insn-00c1b054"></a> `00c1b054` | `89 03 97 9a` | csel x9,x28,x23,eq | `FALL_THROUGH`
<a id="insn-00c1b058"></a> `00c1b058` | `ca 02 9a 9a` | csel x10,x22,x26,eq | `FALL_THROUGH`
<a id="insn-00c1b05c"></a> `00c1b05c` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00c1b060"></a> `00c1b060` | `28 02 00 54` | b.hi 0x00c1b0a4 | `CONDITIONAL_JUMP`
<a id="insn-00c1b064"></a> `00c1b064` | `29 09 0a 8b` | add x9,x9,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00c1b068"></a> `00c1b068` | `29 11 00 91` | add x9,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b06c"></a> `00c1b06c` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00c1b070"></a> `00c1b070` | `a9 01 00 54` | b.ls 0x00c1b0a4 | `CONDITIONAL_JUMP`
<a id="insn-00c1b074"></a> `00c1b074` | `e8 eb 7d b2` | orr x8,xzr,#0x3ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00c1b078"></a> `00c1b078` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00c1b07c"></a> `00c1b07c` | `62 13 00 54` | b.cs 0x00c1b2e8 | `CONDITIONAL_JUMP`
<a id="insn-00c1b080"></a> `00c1b080` | `bf 12 00 f1` | cmp x21,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b084"></a> `00c1b084` | `eb 17 00 b9` | str w11,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00c1b088"></a> `00c1b088` | `68 05 00 54` | b.hi 0x00c1b134 | `CONDITIONAL_JUMP`
<a id="insn-00c1b08c"></a> `00c1b08c` | `28 7f 41 d3` | ubfx x8,x25,#0x1,#0x1f | `FALL_THROUGH`
<a id="insn-00c1b090"></a> `00c1b090` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00c1b094"></a> `00c1b094` | `34 01 7e b2` | orr x20,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b098"></a> `00c1b098` | `08 19 1f 12` | and w8,w8,#0xfe | `FALL_THROUGH`
<a id="insn-00c1b09c"></a> `00c1b09c` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c1b0a0"></a> `00c1b0a0` | `35 00 00 14` | b 0x00c1b174 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1b0a4"></a> `00c1b0a4` | `09 01 14 cb` | sub x9,x8,x20 | `FALL_THROUGH`
<a id="insn-00c1b0a8"></a> `00c1b0a8` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00c1b0ac"></a> `00c1b0ac` | `62 02 00 54` | b.cs 0x00c1b0f8 | `CONDITIONAL_JUMP`
<a id="insn-00c1b0b0"></a> `00c1b0b0` | `89 02 15 8b` | add x9,x20,x21 | `FALL_THROUGH`
<a id="insn-00c1b0b4"></a> `00c1b0b4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c1b0b8"></a> `00c1b0b8` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00c1b0bc"></a> `00c1b0bc` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00c1b0c0"></a> `00c1b0c0` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00c1b0c4"></a> `00c1b0c4` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00c1b0c8"></a> `00c1b0c8` | `e2 03 09 aa` | mov x2,x9 | `FALL_THROUGH`
<a id="insn-00c1b0cc"></a> `00c1b0cc` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00c1b0d0"></a> `00c1b0d0` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00c1b0d4"></a> `00c1b0d4` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00c1b0d8"></a> `00c1b0d8` | `e6 03 1f aa` | mov x6,xzr | `FALL_THROUGH`
<a id="insn-00c1b0dc"></a> `00c1b0dc` | `f1 fd 00 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b0e0"></a> `00c1b0e0` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00c1b0e4"></a> `00c1b0e4` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00c1b0e8"></a> `00c1b0e8` | `77 0a 40 f9` | ldr x23,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c1b0ec"></a> `00c1b0ec` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00c1b0f0"></a> `00c1b0f0` | `74 06 00 f9` | str x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c1b0f4"></a> `00c1b0f4` | `0b 01 00 12` | and w11,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b0f8"></a> `00c1b0f8` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-00c1b0fc"></a> `00c1b0fc` | `29 13 00 d1` | sub x9,x25,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b100"></a> `00c1b100` | `8a 03 97 9a` | csel x10,x28,x23,eq | `FALL_THROUGH`
<a id="insn-00c1b104"></a> `00c1b104` | `3f 71 00 f1` | cmp x9,#0x1c | `FALL_THROUGH`
<a id="insn-00c1b108"></a> `00c1b108` | `48 09 14 8b` | add x8,x10,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00c1b10c"></a> `00c1b10c` | `62 00 00 54` | b.cs 0x00c1b118 | `CONDITIONAL_JUMP`
<a id="insn-00c1b110"></a> `00c1b110` | `e9 03 01 aa` | mov x9,x1 | `FALL_THROUGH`
<a id="insn-00c1b114"></a> `00c1b114` | `59 00 00 14` | b 0x00c1b278 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1b118"></a> `00c1b118` | `8b f6 7e d3` | lsl x11,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00c1b11c"></a> `00c1b11c` | `6c 01 0a 8b` | add x12,x11,x10 | `FALL_THROUGH`
<a id="insn-00c1b120"></a> `00c1b120` | `8a 01 01 cb` | sub x10,x12,x1 | `FALL_THROUGH`
<a id="insn-00c1b124"></a> `00c1b124` | `5f 81 00 f1` | cmp x10,#0x20 | `FALL_THROUGH`
<a id="insn-00c1b128"></a> `00c1b128` | `62 08 00 54` | b.cs 0x00c1b234 | `CONDITIONAL_JUMP`
<a id="insn-00c1b12c"></a> `00c1b12c` | `e9 03 01 aa` | mov x9,x1 | `FALL_THROUGH`
<a id="insn-00c1b130"></a> `00c1b130` | `52 00 00 14` | b 0x00c1b278 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1b134"></a> `00c1b134` | `a8 f2 7f 92` | and x8,x21,#0x3ffffffffffffffe | `FALL_THROUGH`
<a id="insn-00c1b138"></a> `00c1b138` | `a9 02 40 b2` | orr x9,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b13c"></a> `00c1b13c` | `fc 07 00 f9` | str x28,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c1b140"></a> `00c1b140` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c1b144"></a> `00c1b144` | `3f 15 00 f1` | cmp x9,#0x5 | `FALL_THROUGH`
<a id="insn-00c1b148"></a> `00c1b148` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00c1b14c"></a> `00c1b14c` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00c1b150"></a> `00c1b150` | `1c 05 00 91` | add x28,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b154"></a> `00c1b154` | `80 f7 7e d3` | lsl x0,x28,#0x2 | `FALL_THROUGH`
<a id="insn-00c1b158"></a> `00c1b158` | `4e f3 00 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b15c"></a> `00c1b15c` | `88 03 40 b2` | orr x8,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b160"></a> `00c1b160` | `fc 07 40 f9` | ldr x28,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c1b164"></a> `00c1b164` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00c1b168"></a> `00c1b168` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c1b16c"></a> `00c1b16c` | `f5 03 02 a9` | stp x21,x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1b170"></a> `00c1b170` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c1b174"></a> `00c1b174` | `28 13 00 d1` | sub x8,x25,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b178"></a> `00c1b178` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c1b17c"></a> `00c1b17c` | `08 f5 7e 92` | and x8,x8,#-0x4 | `FALL_THROUGH`
<a id="insn-00c1b180"></a> `00c1b180` | `15 11 00 91` | add x21,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b184"></a> `00c1b184` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00c1b188"></a> `00c1b188` | `9e f3 00 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b18c"></a> `00c1b18c` | `9f 6a 35 b8` | str wzr,[x20, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00c1b190"></a> `00c1b190` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00c1b194"></a> `00c1b194` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c1b198"></a> `00c1b198` | `eb 2b 42 a9` | ldp x11,x10,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1b19c"></a> `00c1b19c` | `29 01 7e b2` | orr x9,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b1a0"></a> `00c1b1a0` | `15 01 00 72` | ands w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b1a4"></a> `00c1b1a4` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b1a8"></a> `00c1b1a8` | `27 01 8a 9a` | csel x7,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00c1b1ac"></a> `00c1b1ac` | `06 01 8b 9a` | csel x6,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00c1b1b0"></a> `00c1b1b0` | `e8 17 40 b9` | ldr w8,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00c1b1b4"></a> `00c1b1b4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00c1b1b8"></a> `00c1b1b8` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00c1b1bc"></a> `00c1b1bc` | `01 01 9b 9a` | csel x1,x8,x27,eq | `FALL_THROUGH`
<a id="insn-00c1b1c0"></a> `00c1b1c0` | `1f 03 40 f2` | tst x24,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b1c4"></a> `00c1b1c4` | `d4 02 9a 9a` | csel x20,x22,x26,eq | `FALL_THROUGH`
<a id="insn-00c1b1c8"></a> `00c1b1c8` | `28 00 14 cb` | sub x8,x1,x20 | `FALL_THROUGH`
<a id="insn-00c1b1cc"></a> `00c1b1cc` | `1f 01 06 eb` | cmp x8,x6 | `FALL_THROUGH`
<a id="insn-00c1b1d0"></a> `00c1b1d0` | `62 01 00 54` | b.cs 0x00c1b1fc | `CONDITIONAL_JUMP`
<a id="insn-00c1b1d4"></a> `00c1b1d4` | `c8 00 01 cb` | sub x8,x6,x1 | `FALL_THROUGH`
<a id="insn-00c1b1d8"></a> `00c1b1d8` | `02 01 14 8b` | add x2,x8,x20 | `FALL_THROUGH`
<a id="insn-00c1b1dc"></a> `00c1b1dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c1b1e0"></a> `00c1b1e0` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00c1b1e4"></a> `00c1b1e4` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00c1b1e8"></a> `00c1b1e8` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00c1b1ec"></a> `00c1b1ec` | `81 0b 01 94` | bl 0x00c5dff0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b1f0"></a> `00c1b1f0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c1b1f4"></a> `00c1b1f4` | `15 01 00 12` | and w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b1f8"></a> `00c1b1f8` | `2f 00 00 14` | b 0x00c1b2b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1b1fc"></a> `00c1b1fc` | `c6 05 00 b4` | cbz x6,0x00c1b2b4 | `CONDITIONAL_JUMP`
<a id="insn-00c1b200"></a> `00c1b200` | `1f 03 40 f2` | tst x24,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b204"></a> `00c1b204` | `c2 f4 7e d3` | lsl x2,x6,#0x2 | `FALL_THROUGH`
<a id="insn-00c1b208"></a> `00c1b208` | `e1 03 07 aa` | mov x1,x7 | `FALL_THROUGH`
<a id="insn-00c1b20c"></a> `00c1b20c` | `96 03 97 9a` | csel x22,x28,x23,eq | `FALL_THROUGH`
<a id="insn-00c1b210"></a> `00c1b210` | `f7 03 06 aa` | mov x23,x6 | `FALL_THROUGH`
<a id="insn-00c1b214"></a> `00c1b214` | `c0 0a 14 8b` | add x0,x22,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00c1b218"></a> `00c1b218` | `4a f3 00 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b21c"></a> `00c1b21c` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00c1b220"></a> `00c1b220` | `88 02 17 8b` | add x8,x20,x23 | `FALL_THROUGH`
<a id="insn-00c1b224"></a> `00c1b224` | `49 04 00 37` | tbnz w9,#0x0,0x00c1b2ac | `CONDITIONAL_JUMP`
<a id="insn-00c1b228"></a> `00c1b228` | `09 79 1f 53` | lsl w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b22c"></a> `00c1b22c` | `69 02 00 39` | strb w9,[x19] | `FALL_THROUGH`
<a id="insn-00c1b230"></a> `00c1b230` | `20 00 00 14` | b 0x00c1b2b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1b234"></a> `00c1b234` | `29 fd 42 d3` | lsr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00c1b238"></a> `00c1b238` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00c1b23c"></a> `00c1b23c` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b240"></a> `00c1b240` | `4b ed 7d 92` | and x11,x10,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00c1b244"></a> `00c1b244` | `6d f5 7e d3` | lsl x13,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00c1b248"></a> `00c1b248` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00c1b24c"></a> `00c1b24c` | `29 00 0d 8b` | add x9,x1,x13 | `FALL_THROUGH`
<a id="insn-00c1b250"></a> `00c1b250` | `08 01 0d 8b` | add x8,x8,x13 | `FALL_THROUGH`
<a id="insn-00c1b254"></a> `00c1b254` | `2d 40 00 91` | add x13,x1,#0x10 | `FALL_THROUGH`
<a id="insn-00c1b258"></a> `00c1b258` | `a0 85 7f ad` | ldp q0,q1,[x13, #-0x10] | `FALL_THROUGH`
<a id="insn-00c1b25c"></a> `00c1b25c` | `ce 21 00 f1` | subs x14,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00c1b260"></a> `00c1b260` | `ad 81 00 91` | add x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00c1b264"></a> `00c1b264` | `80 85 3f ad` | stp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00c1b268"></a> `00c1b268` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00c1b26c"></a> `00c1b26c` | `61 ff ff 54` | b.ne 0x00c1b258 | `CONDITIONAL_JUMP`
<a id="insn-00c1b270"></a> `00c1b270` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00c1b274"></a> `00c1b274` | `a0 00 00 54` | b.eq 0x00c1b288 | `CONDITIONAL_JUMP`
<a id="insn-00c1b278"></a> `00c1b278` | `2a 45 40 b8` | ldr w10,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00c1b27c"></a> `00c1b27c` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00c1b280"></a> `00c1b280` | `0a 45 00 b8` | str w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00c1b284"></a> `00c1b284` | `a1 ff ff 54` | b.ne 0x00c1b278 | `CONDITIONAL_JUMP`
<a id="insn-00c1b288"></a> `00c1b288` | `1f 01 00 b9` | str wzr,[x8] | `FALL_THROUGH`
<a id="insn-00c1b28c"></a> `00c1b28c` | `88 02 15 8b` | add x8,x20,x21 | `FALL_THROUGH`
<a id="insn-00c1b290"></a> `00c1b290` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00c1b294"></a> `00c1b294` | `89 00 00 37` | tbnz w9,#0x0,0x00c1b2a4 | `CONDITIONAL_JUMP`
<a id="insn-00c1b298"></a> `00c1b298` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1b29c"></a> `00c1b29c` | `68 02 00 39` | strb w8,[x19] | `FALL_THROUGH`
<a id="insn-00c1b2a0"></a> `00c1b2a0` | `08 00 00 14` | b 0x00c1b2c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1b2a4"></a> `00c1b2a4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c1b2a8"></a> `00c1b2a8` | `06 00 00 14` | b 0x00c1b2c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1b2ac"></a> `00c1b2ac` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c1b2b0"></a> `00c1b2b0` | `df 7a 28 b8` | str wzr,[x22, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00c1b2b4"></a> `00c1b2b4` | `75 00 00 34` | cbz w21,0x00c1b2c0 | `CONDITIONAL_JUMP`
<a id="insn-00c1b2b8"></a> `00c1b2b8` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00c1b2bc"></a> `00c1b2bc` | `fd f2 00 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b2c0"></a> `00c1b2c0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c1b2c4"></a> `00c1b2c4` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00c1b2c8"></a> `00c1b2c8` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00c1b2cc"></a> `00c1b2cc` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00c1b2d0"></a> `00c1b2d0` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c1b2d4"></a> `00c1b2d4` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1b2d8"></a> `00c1b2d8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1b2dc"></a> `00c1b2dc` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00c1b2e0"></a> `00c1b2e0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c1b2e4"></a> `00c1b2e4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c1b2e8"></a> `00c1b2e8` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00c1b2ec"></a> `00c1b2ec` | `ed f0 ea 97` | bl 0x006d76a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b2f0"></a> `00c1b2f0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c1b2f4"></a> `00c1b2f4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c1b2f8"></a> `00c1b2f8` | `68 00 00 36` | tbz w8,#0x0,0x00c1b304 | `CONDITIONAL_JUMP`
<a id="insn-00c1b2fc"></a> `00c1b2fc` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00c1b300"></a> `00c1b300` | `ec f2 00 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1b304"></a> `00c1b304` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c1b308"></a> `00c1b308` | `15 e3 00 94` | bl 0x00c53f5c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c1afec`](#insn-00c1afec) 範囲 `[['00c1afec', '00c1b01f']]`
  - `FALL_THROUGH` [`00c1b01c`](#insn-00c1b01c) → [`00c1b020`](#insn-00c1b020)
- ブロック [`00c1b020`](#insn-00c1b020) 範囲 `[['00c1b020', '00c1b02b']]`
  - `FALL_THROUGH` [`00c1b028`](#insn-00c1b028) → [`00c1b02c`](#insn-00c1b02c)
- ブロック [`00c1b02c`](#insn-00c1b02c) 範囲 `[['00c1b02c', '00c1b03f']]`
  - `CONDITIONAL_JUMP` [`00c1b03c`](#insn-00c1b03c) → [`00c1b2c0`](#insn-00c1b2c0)
  - `FALL_THROUGH` [`00c1b03c`](#insn-00c1b03c) → [`00c1b040`](#insn-00c1b040)
- ブロック [`00c1b040`](#insn-00c1b040) 範囲 `[['00c1b040', '00c1b063']]`
  - `CONDITIONAL_JUMP` [`00c1b060`](#insn-00c1b060) → [`00c1b0a4`](#insn-00c1b0a4)
  - `FALL_THROUGH` [`00c1b060`](#insn-00c1b060) → [`00c1b064`](#insn-00c1b064)
- ブロック [`00c1b064`](#insn-00c1b064) 範囲 `[['00c1b064', '00c1b073']]`
  - `CONDITIONAL_JUMP` [`00c1b070`](#insn-00c1b070) → [`00c1b0a4`](#insn-00c1b0a4)
  - `FALL_THROUGH` [`00c1b070`](#insn-00c1b070) → [`00c1b074`](#insn-00c1b074)
- ブロック [`00c1b074`](#insn-00c1b074) 範囲 `[['00c1b074', '00c1b07f']]`
  - `CONDITIONAL_JUMP` [`00c1b07c`](#insn-00c1b07c) → [`00c1b2e8`](#insn-00c1b2e8)
  - `FALL_THROUGH` [`00c1b07c`](#insn-00c1b07c) → [`00c1b080`](#insn-00c1b080)
- ブロック [`00c1b080`](#insn-00c1b080) 範囲 `[['00c1b080', '00c1b08b']]`
  - `CONDITIONAL_JUMP` [`00c1b088`](#insn-00c1b088) → [`00c1b134`](#insn-00c1b134)
  - `FALL_THROUGH` [`00c1b088`](#insn-00c1b088) → [`00c1b08c`](#insn-00c1b08c)
- ブロック [`00c1b08c`](#insn-00c1b08c) 範囲 `[['00c1b08c', '00c1b0a3']]`
  - `UNCONDITIONAL_JUMP` [`00c1b0a0`](#insn-00c1b0a0) → [`00c1b174`](#insn-00c1b174)
- ブロック [`00c1b0a4`](#insn-00c1b0a4) 範囲 `[['00c1b0a4', '00c1b0af']]`
  - `CONDITIONAL_JUMP` [`00c1b0ac`](#insn-00c1b0ac) → [`00c1b0f8`](#insn-00c1b0f8)
  - `FALL_THROUGH` [`00c1b0ac`](#insn-00c1b0ac) → [`00c1b0b0`](#insn-00c1b0b0)
- ブロック [`00c1b0b0`](#insn-00c1b0b0) 範囲 `[['00c1b0b0', '00c1b0f7']]`
  - `FALL_THROUGH` [`00c1b0f4`](#insn-00c1b0f4) → [`00c1b0f8`](#insn-00c1b0f8)
- ブロック [`00c1b0f8`](#insn-00c1b0f8) 範囲 `[['00c1b0f8', '00c1b0fb']]`
  - `FALL_THROUGH` [`00c1b0f8`](#insn-00c1b0f8) → [`00c1b0fc`](#insn-00c1b0fc)
- ブロック [`00c1b0fc`](#insn-00c1b0fc) 範囲 `[['00c1b0fc', '00c1b10f']]`
  - `CONDITIONAL_JUMP` [`00c1b10c`](#insn-00c1b10c) → [`00c1b118`](#insn-00c1b118)
  - `FALL_THROUGH` [`00c1b10c`](#insn-00c1b10c) → [`00c1b110`](#insn-00c1b110)
- ブロック [`00c1b110`](#insn-00c1b110) 範囲 `[['00c1b110', '00c1b117']]`
  - `UNCONDITIONAL_JUMP` [`00c1b114`](#insn-00c1b114) → [`00c1b278`](#insn-00c1b278)
- ブロック [`00c1b118`](#insn-00c1b118) 範囲 `[['00c1b118', '00c1b12b']]`
  - `CONDITIONAL_JUMP` [`00c1b128`](#insn-00c1b128) → [`00c1b234`](#insn-00c1b234)
  - `FALL_THROUGH` [`00c1b128`](#insn-00c1b128) → [`00c1b12c`](#insn-00c1b12c)
- ブロック [`00c1b12c`](#insn-00c1b12c) 範囲 `[['00c1b12c', '00c1b133']]`
  - `UNCONDITIONAL_JUMP` [`00c1b130`](#insn-00c1b130) → [`00c1b278`](#insn-00c1b278)
- ブロック [`00c1b134`](#insn-00c1b134) 範囲 `[['00c1b134', '00c1b13f']]`
  - `FALL_THROUGH` [`00c1b13c`](#insn-00c1b13c) → [`00c1b140`](#insn-00c1b140)
- ブロック [`00c1b140`](#insn-00c1b140) 範囲 `[['00c1b140', '00c1b14f']]`
  - `FALL_THROUGH` [`00c1b14c`](#insn-00c1b14c) → [`00c1b150`](#insn-00c1b150)
- ブロック [`00c1b150`](#insn-00c1b150) 範囲 `[['00c1b150', '00c1b173']]`
  - `FALL_THROUGH` [`00c1b170`](#insn-00c1b170) → [`00c1b174`](#insn-00c1b174)
- ブロック [`00c1b174`](#insn-00c1b174) 範囲 `[['00c1b174', '00c1b1c3']]`
  - `FALL_THROUGH` [`00c1b1c0`](#insn-00c1b1c0) → [`00c1b1c4`](#insn-00c1b1c4)
- ブロック [`00c1b1c4`](#insn-00c1b1c4) 範囲 `[['00c1b1c4', '00c1b1cf']]`
  - `FALL_THROUGH` [`00c1b1cc`](#insn-00c1b1cc) → [`00c1b1d0`](#insn-00c1b1d0)
- ブロック [`00c1b1d0`](#insn-00c1b1d0) 範囲 `[['00c1b1d0', '00c1b1d3']]`
  - `CONDITIONAL_JUMP` [`00c1b1d0`](#insn-00c1b1d0) → [`00c1b1fc`](#insn-00c1b1fc)
  - `FALL_THROUGH` [`00c1b1d0`](#insn-00c1b1d0) → [`00c1b1d4`](#insn-00c1b1d4)
- ブロック [`00c1b1d4`](#insn-00c1b1d4) 範囲 `[['00c1b1d4', '00c1b1f3']]`
  - `FALL_THROUGH` [`00c1b1f0`](#insn-00c1b1f0) → [`00c1b1f4`](#insn-00c1b1f4)
- ブロック [`00c1b1f4`](#insn-00c1b1f4) 範囲 `[['00c1b1f4', '00c1b1fb']]`
  - `UNCONDITIONAL_JUMP` [`00c1b1f8`](#insn-00c1b1f8) → [`00c1b2b4`](#insn-00c1b2b4)
- ブロック [`00c1b1fc`](#insn-00c1b1fc) 範囲 `[['00c1b1fc', '00c1b1ff']]`
  - `CONDITIONAL_JUMP` [`00c1b1fc`](#insn-00c1b1fc) → [`00c1b2b4`](#insn-00c1b2b4)
  - `FALL_THROUGH` [`00c1b1fc`](#insn-00c1b1fc) → [`00c1b200`](#insn-00c1b200)
- ブロック [`00c1b200`](#insn-00c1b200) 範囲 `[['00c1b200', '00c1b227']]`
  - `CONDITIONAL_JUMP` [`00c1b224`](#insn-00c1b224) → [`00c1b2ac`](#insn-00c1b2ac)
  - `FALL_THROUGH` [`00c1b224`](#insn-00c1b224) → [`00c1b228`](#insn-00c1b228)
- ブロック [`00c1b228`](#insn-00c1b228) 範囲 `[['00c1b228', '00c1b22f']]`
  - `FALL_THROUGH` [`00c1b22c`](#insn-00c1b22c) → [`00c1b230`](#insn-00c1b230)
- ブロック [`00c1b230`](#insn-00c1b230) 範囲 `[['00c1b230', '00c1b233']]`
  - `UNCONDITIONAL_JUMP` [`00c1b230`](#insn-00c1b230) → [`00c1b2b0`](#insn-00c1b2b0)
- ブロック [`00c1b234`](#insn-00c1b234) 範囲 `[['00c1b234', '00c1b23b']]`
  - `FALL_THROUGH` [`00c1b238`](#insn-00c1b238) → [`00c1b23c`](#insn-00c1b23c)
- ブロック [`00c1b23c`](#insn-00c1b23c) 範囲 `[['00c1b23c', '00c1b24b']]`
  - `FALL_THROUGH` [`00c1b248`](#insn-00c1b248) → [`00c1b24c`](#insn-00c1b24c)
- ブロック [`00c1b24c`](#insn-00c1b24c) 範囲 `[['00c1b24c', '00c1b257']]`
  - `FALL_THROUGH` [`00c1b254`](#insn-00c1b254) → [`00c1b258`](#insn-00c1b258)
- ブロック [`00c1b258`](#insn-00c1b258) 範囲 `[['00c1b258', '00c1b26f']]`
  - `CONDITIONAL_JUMP` [`00c1b26c`](#insn-00c1b26c) → [`00c1b258`](#insn-00c1b258)
  - `FALL_THROUGH` [`00c1b26c`](#insn-00c1b26c) → [`00c1b270`](#insn-00c1b270)
- ブロック [`00c1b270`](#insn-00c1b270) 範囲 `[['00c1b270', '00c1b277']]`
  - `CONDITIONAL_JUMP` [`00c1b274`](#insn-00c1b274) → [`00c1b288`](#insn-00c1b288)
  - `FALL_THROUGH` [`00c1b274`](#insn-00c1b274) → [`00c1b278`](#insn-00c1b278)
- ブロック [`00c1b278`](#insn-00c1b278) 範囲 `[['00c1b278', '00c1b287']]`
  - `CONDITIONAL_JUMP` [`00c1b284`](#insn-00c1b284) → [`00c1b278`](#insn-00c1b278)
  - `FALL_THROUGH` [`00c1b284`](#insn-00c1b284) → [`00c1b288`](#insn-00c1b288)
- ブロック [`00c1b288`](#insn-00c1b288) 範囲 `[['00c1b288', '00c1b297']]`
  - `CONDITIONAL_JUMP` [`00c1b294`](#insn-00c1b294) → [`00c1b2a4`](#insn-00c1b2a4)
  - `FALL_THROUGH` [`00c1b294`](#insn-00c1b294) → [`00c1b298`](#insn-00c1b298)
- ブロック [`00c1b298`](#insn-00c1b298) 範囲 `[['00c1b298', '00c1b2a3']]`
  - `UNCONDITIONAL_JUMP` [`00c1b2a0`](#insn-00c1b2a0) → [`00c1b2c0`](#insn-00c1b2c0)
- ブロック [`00c1b2a4`](#insn-00c1b2a4) 範囲 `[['00c1b2a4', '00c1b2ab']]`
  - `UNCONDITIONAL_JUMP` [`00c1b2a8`](#insn-00c1b2a8) → [`00c1b2c0`](#insn-00c1b2c0)
- ブロック [`00c1b2ac`](#insn-00c1b2ac) 範囲 `[['00c1b2ac', '00c1b2af']]`
  - `FALL_THROUGH` [`00c1b2ac`](#insn-00c1b2ac) → [`00c1b2b0`](#insn-00c1b2b0)
- ブロック [`00c1b2b0`](#insn-00c1b2b0) 範囲 `[['00c1b2b0', '00c1b2b3']]`
  - `FALL_THROUGH` [`00c1b2b0`](#insn-00c1b2b0) → [`00c1b2b4`](#insn-00c1b2b4)
- ブロック [`00c1b2b4`](#insn-00c1b2b4) 範囲 `[['00c1b2b4', '00c1b2b7']]`
  - `CONDITIONAL_JUMP` [`00c1b2b4`](#insn-00c1b2b4) → [`00c1b2c0`](#insn-00c1b2c0)
  - `FALL_THROUGH` [`00c1b2b4`](#insn-00c1b2b4) → [`00c1b2b8`](#insn-00c1b2b8)
- ブロック [`00c1b2b8`](#insn-00c1b2b8) 範囲 `[['00c1b2b8', '00c1b2bf']]`
  - `FALL_THROUGH` [`00c1b2bc`](#insn-00c1b2bc) → [`00c1b2c0`](#insn-00c1b2c0)
- ブロック [`00c1b2c0`](#insn-00c1b2c0) 範囲 `[['00c1b2c0', '00c1b2e7']]`
- ブロック [`00c1b2e8`](#insn-00c1b2e8) 範囲 `[['00c1b2e8', '00c1b2fb']]`
  - `CONDITIONAL_JUMP` [`00c1b2f8`](#insn-00c1b2f8) → [`00c1b304`](#insn-00c1b304)
  - `FALL_THROUGH` [`00c1b2f8`](#insn-00c1b2f8) → [`00c1b2fc`](#insn-00c1b2fc)
- ブロック [`00c1b2fc`](#insn-00c1b2fc) 範囲 `[['00c1b2fc', '00c1b303']]`
  - `FALL_THROUGH` [`00c1b300`](#insn-00c1b300) → [`00c1b304`](#insn-00c1b304)
- ブロック [`00c1b304`](#insn-00c1b304) 範囲 `[['00c1b304', '00c1b30b']]`

## 命令位置別の参照

- [`00c1aff4`](#insn-00c1aff4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1aff8`](#insn-00c1aff8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1affc`](#insn-00c1affc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b000`](#insn-00c1b000) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b004`](#insn-00c1b004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b008`](#insn-00c1b008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b03c`](#insn-00c1b03c) → [`00c1b2c0`](#insn-00c1b2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b060`](#insn-00c1b060) → [`00c1b0a4`](#insn-00c1b0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b070`](#insn-00c1b070) → [`00c1b0a4`](#insn-00c1b0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b07c`](#insn-00c1b07c) → [`00c1b2e8`](#insn-00c1b2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b084`](#insn-00c1b084) → `Stack[-0x7c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b088`](#insn-00c1b088) → [`00c1b134`](#insn-00c1b134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b09c`](#insn-00c1b09c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b0a0`](#insn-00c1b0a0) → [`00c1b174`](#insn-00c1b174) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b0ac`](#insn-00c1b0ac) → [`00c1b0f8`](#insn-00c1b0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b0dc`](#insn-00c1b0dc) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00c1b10c`](#insn-00c1b10c) → [`00c1b118`](#insn-00c1b118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b114`](#insn-00c1b114) → [`00c1b278`](#insn-00c1b278) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b128`](#insn-00c1b128) → [`00c1b234`](#insn-00c1b234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b130`](#insn-00c1b130) → [`00c1b278`](#insn-00c1b278) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b13c`](#insn-00c1b13c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b158`](#insn-00c1b158) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00c1b160`](#insn-00c1b160) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b16c`](#insn-00c1b16c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b170`](#insn-00c1b170) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b188`](#insn-00c1b188) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00c1b194`](#insn-00c1b194) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b198`](#insn-00c1b198) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b1b0`](#insn-00c1b1b0) → `Stack[-0x7c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b1d0`](#insn-00c1b1d0) → [`00c1b1fc`](#insn-00c1b1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b1ec`](#insn-00c1b1ec) → [`00c5dff0`](../00c5d/00c5dff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dff0` · 推定シンボル `None` · 推定型 `None`
- [`00c1b1f0`](#insn-00c1b1f0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b1f8`](#insn-00c1b1f8) → [`00c1b2b4`](#insn-00c1b2b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b1fc`](#insn-00c1b1fc) → [`00c1b2b4`](#insn-00c1b2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b218`](#insn-00c1b218) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`00c1b224`](#insn-00c1b224) → [`00c1b2ac`](#insn-00c1b2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b230`](#insn-00c1b230) → [`00c1b2b0`](#insn-00c1b2b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b26c`](#insn-00c1b26c) → [`00c1b258`](#insn-00c1b258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b274`](#insn-00c1b274) → [`00c1b288`](#insn-00c1b288) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b284`](#insn-00c1b284) → [`00c1b278`](#insn-00c1b278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b294`](#insn-00c1b294) → [`00c1b2a4`](#insn-00c1b2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2a0`](#insn-00c1b2a0) → [`00c1b2c0`](#insn-00c1b2c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2a8`](#insn-00c1b2a8) → [`00c1b2c0`](#insn-00c1b2c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2b4`](#insn-00c1b2b4) → [`00c1b2c0`](#insn-00c1b2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2b8`](#insn-00c1b2b8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2bc`](#insn-00c1b2bc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2c4`](#insn-00c1b2c4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2c8`](#insn-00c1b2c8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2cc`](#insn-00c1b2cc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2d0`](#insn-00c1b2d0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2d4`](#insn-00c1b2d4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2d8`](#insn-00c1b2d8) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2ec`](#insn-00c1b2ec) → [`006d76a0`](../006d7/006d76a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d76a0` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2f0`](#insn-00c1b2f0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2f8`](#insn-00c1b2f8) → [`00c1b304`](#insn-00c1b304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b2fc`](#insn-00c1b2fc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1b300`](#insn-00c1b300) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00c1b308`](#insn-00c1b308) → [`00c53f5c`](../00c53/00c53f5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53f5c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c1aff4`](#insn-00c1aff4)

~~~json
{
  "source": "00c1aff4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1aff8`](#insn-00c1aff8)

~~~json
{
  "source": "00c1aff8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1affc`](#insn-00c1affc)

~~~json
{
  "source": "00c1affc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b000`](#insn-00c1b000)

~~~json
{
  "source": "00c1b000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b004`](#insn-00c1b004)

~~~json
{
  "source": "00c1b004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b008`](#insn-00c1b008)

~~~json
{
  "source": "00c1b008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b03c`](#insn-00c1b03c)

~~~json
{
  "source": "00c1b03c",
  "target": "00c1b2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b060`](#insn-00c1b060)

~~~json
{
  "source": "00c1b060",
  "target": "00c1b0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b070`](#insn-00c1b070)

~~~json
{
  "source": "00c1b070",
  "target": "00c1b0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b07c`](#insn-00c1b07c)

~~~json
{
  "source": "00c1b07c",
  "target": "00c1b2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b084`](#insn-00c1b084)

~~~json
{
  "source": "00c1b084",
  "target": "Stack[-0x7c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b088`](#insn-00c1b088)

~~~json
{
  "source": "00c1b088",
  "target": "00c1b134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b09c`](#insn-00c1b09c)

~~~json
{
  "source": "00c1b09c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b0a0`](#insn-00c1b0a0)

~~~json
{
  "source": "00c1b0a0",
  "target": "00c1b174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b0ac`](#insn-00c1b0ac)

~~~json
{
  "source": "00c1b0ac",
  "target": "00c1b0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b0dc`](#insn-00c1b0dc)

~~~json
{
  "source": "00c1b0dc",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b10c`](#insn-00c1b10c)

~~~json
{
  "source": "00c1b10c",
  "target": "00c1b118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b114`](#insn-00c1b114)

~~~json
{
  "source": "00c1b114",
  "target": "00c1b278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b128`](#insn-00c1b128)

~~~json
{
  "source": "00c1b128",
  "target": "00c1b234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b130`](#insn-00c1b130)

~~~json
{
  "source": "00c1b130",
  "target": "00c1b278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b13c`](#insn-00c1b13c)

~~~json
{
  "source": "00c1b13c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b158`](#insn-00c1b158)

~~~json
{
  "source": "00c1b158",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b160`](#insn-00c1b160)

~~~json
{
  "source": "00c1b160",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b16c`](#insn-00c1b16c)

~~~json
{
  "source": "00c1b16c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b170`](#insn-00c1b170)

~~~json
{
  "source": "00c1b170",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b188`](#insn-00c1b188)

~~~json
{
  "source": "00c1b188",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b194`](#insn-00c1b194)

~~~json
{
  "source": "00c1b194",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b198`](#insn-00c1b198)

~~~json
{
  "source": "00c1b198",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b1b0`](#insn-00c1b1b0)

~~~json
{
  "source": "00c1b1b0",
  "target": "Stack[-0x7c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b1d0`](#insn-00c1b1d0)

~~~json
{
  "source": "00c1b1d0",
  "target": "00c1b1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b1ec`](#insn-00c1b1ec)

~~~json
{
  "source": "00c1b1ec",
  "target": "00c5dff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b1f0`](#insn-00c1b1f0)

~~~json
{
  "source": "00c1b1f0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b1f8`](#insn-00c1b1f8)

~~~json
{
  "source": "00c1b1f8",
  "target": "00c1b2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b1fc`](#insn-00c1b1fc)

~~~json
{
  "source": "00c1b1fc",
  "target": "00c1b2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b218`](#insn-00c1b218)

~~~json
{
  "source": "00c1b218",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b224`](#insn-00c1b224)

~~~json
{
  "source": "00c1b224",
  "target": "00c1b2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b230`](#insn-00c1b230)

~~~json
{
  "source": "00c1b230",
  "target": "00c1b2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b26c`](#insn-00c1b26c)

~~~json
{
  "source": "00c1b26c",
  "target": "00c1b258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b274`](#insn-00c1b274)

~~~json
{
  "source": "00c1b274",
  "target": "00c1b288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b284`](#insn-00c1b284)

~~~json
{
  "source": "00c1b284",
  "target": "00c1b278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b294`](#insn-00c1b294)

~~~json
{
  "source": "00c1b294",
  "target": "00c1b2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2a0`](#insn-00c1b2a0)

~~~json
{
  "source": "00c1b2a0",
  "target": "00c1b2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2a8`](#insn-00c1b2a8)

~~~json
{
  "source": "00c1b2a8",
  "target": "00c1b2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2b4`](#insn-00c1b2b4)

~~~json
{
  "source": "00c1b2b4",
  "target": "00c1b2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2b8`](#insn-00c1b2b8)

~~~json
{
  "source": "00c1b2b8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2bc`](#insn-00c1b2bc)

~~~json
{
  "source": "00c1b2bc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b2c4`](#insn-00c1b2c4)

~~~json
{
  "source": "00c1b2c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2c8`](#insn-00c1b2c8)

~~~json
{
  "source": "00c1b2c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2cc`](#insn-00c1b2cc)

~~~json
{
  "source": "00c1b2cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2d0`](#insn-00c1b2d0)

~~~json
{
  "source": "00c1b2d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2d4`](#insn-00c1b2d4)

~~~json
{
  "source": "00c1b2d4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2d8`](#insn-00c1b2d8)

~~~json
{
  "source": "00c1b2d8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2ec`](#insn-00c1b2ec)

~~~json
{
  "source": "00c1b2ec",
  "target": "006d76a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b2f0`](#insn-00c1b2f0)

~~~json
{
  "source": "00c1b2f0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2f8`](#insn-00c1b2f8)

~~~json
{
  "source": "00c1b2f8",
  "target": "00c1b304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b2fc`](#insn-00c1b2fc)

~~~json
{
  "source": "00c1b2fc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1b300`](#insn-00c1b300)

~~~json
{
  "source": "00c1b300",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1b308`](#insn-00c1b308)

~~~json
{
  "source": "00c1b308",
  "target": "00c53f5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
