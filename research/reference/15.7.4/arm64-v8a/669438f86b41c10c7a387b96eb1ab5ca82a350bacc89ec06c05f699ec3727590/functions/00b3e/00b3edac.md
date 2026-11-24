# 00b3edac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b3ed68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ed68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0011.md#compare-6971e4361857cd35e40a9461e6d10fe5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ba87b8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba87b8.md) · 移動量 `+0x69a0c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0063.md#compare-77944c532475812e5cd03f9abaf2a32d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3edac",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_",
  "size": 656,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e96d183da6d5f793922e0cb8c7d66e30bb5de494cf5b717c75abb3be9f466837",
  "source_text_sha256": "e96d183da6d5f793922e0cb8c7d66e30bb5de494cf5b717c75abb3be9f466837",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3edac",
        "00b3f03b"
      ]
    ],
    "bytes_sha256": "30bebe7decde6659bdf8c199cff67c0e1876953636425b1d57a251c9f0f2182f",
    "instruction_count": 164,
    "instruction_bytes": 656,
    "body_bytes": 656,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdfcf0](../00bdf/00bdfcf0.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb130](../00bdb/00bdb130.md)
- [00bdda90](../00bdd/00bdda90.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5124 bytes

~~~c

ulong * _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_
                  (ulong *param_1,undefined1 *param_2,undefined1 *param_3)

{
  byte bVar1;
  uint uVar2;
  long lVar3;
  undefined8 *puVar4;
  ulong uVar5;
  undefined1 *puVar6;
  long lVar7;
  ulong uVar8;
  undefined1 *puVar9;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  undefined1 *puVar13;
  ulong uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  undefined8 uVar17;
  ulong local_60;
  ulong local_58;
  undefined1 *local_50;
  long local_48;
  
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  bVar1 = (byte)*param_1;
  if ((bVar1 & 1) == 0) {
    uVar14 = (ulong)(bVar1 >> 1);
    lVar7 = 0x16;
    uVar8 = (ulong)bVar1;
  }
  else {
    uVar8 = *param_1;
    uVar14 = param_1[1];
    lVar7 = (uVar8 & 0xfffffffffffffffe) - 1;
  }
  uVar5 = (long)param_3 - (long)param_2;
  if (uVar5 == 0) goto LAB_00b3f008;
  if ((bVar1 & 1) == 0) {
    puVar9 = (undefined1 *)((long)param_1 + 1);
    uVar10 = (ulong)(bVar1 >> 1);
  }
  else {
    uVar10 = param_1[1];
    puVar9 = (undefined1 *)param_1[2];
  }
  if ((puVar9 <= param_2) && (param_2 < puVar9 + uVar10)) {
    local_58 = 0;
    local_50 = (undefined1 *)0x0;
    local_60 = 0;
    if (0xffffffffffffffef < uVar5) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (uVar5 < 0x17) {
      uVar2 = (int)uVar5 << 1;
      uVar8 = (ulong)uVar2;
      local_60 = (ulong)(byte)uVar2;
      puVar9 = (undefined1 *)((ulong)&local_60 | 1);
    }
    else {
      uVar8 = uVar5 + 0x10 & 0xfffffffffffffff0;
      puVar9 = (undefined1 *)_Znwm(uVar8);
      uVar8 = uVar8 | 1;
      local_60 = uVar8;
      local_50 = puVar9;
      local_58 = uVar5;
    }
    if (param_2 != param_3) {
      puVar6 = puVar9;
      if (0x1f < uVar5) {
        uVar10 = uVar5 & 0xffffffffffffffe0;
        puVar12 = (undefined8 *)(puVar9 + 0x10);
        puVar9 = puVar9 + uVar10;
        puVar11 = (undefined8 *)(param_2 + 0x10);
        uVar14 = uVar10;
        do {
          puVar4 = puVar11 + -1;
          uVar15 = puVar11[-2];
          uVar17 = puVar11[1];
          uVar16 = *puVar11;
          uVar14 = uVar14 - 0x20;
          puVar11 = puVar11 + 4;
          puVar12[-1] = *puVar4;
          puVar12[-2] = uVar15;
          puVar12[1] = uVar17;
          *puVar12 = uVar16;
          puVar12 = puVar12 + 4;
        } while (uVar14 != 0);
        puVar6 = puVar9;
        param_2 = param_2 + uVar10;
        if (uVar5 == uVar10) goto LAB_00b3efd0;
      }
      do {
        puVar13 = param_2 + 1;
        puVar9 = puVar6 + 1;
        *puVar6 = *param_2;
        puVar6 = puVar9;
        param_2 = puVar13;
      } while (param_3 != puVar13);
    }
LAB_00b3efd0:
    *puVar9 = 0;
    uVar14 = (ulong)((uint)uVar8 >> 1 & 0x7f);
    puVar9 = (undefined1 *)((ulong)&local_60 | 1);
    if ((uVar8 & 1) != 0) {
      uVar14 = local_58;
      puVar9 = local_50;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,puVar9,uVar14);
    if ((local_60 & 1) != 0) {
      _ZdlPv(local_50);
    }
    goto LAB_00b3f008;
  }
  if (lVar7 - uVar14 < uVar5) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
              (param_1,lVar7,(uVar14 + uVar5) - lVar7,uVar14,uVar14,0,0);
                    /* try { // try from 00b3eeac to 00c3efd7 has its CatchHandler @ 00b40c88 */
    uVar8 = (ulong)(byte)*param_1;
  }
  if ((uVar8 & 1) == 0) {
    uVar8 = (long)param_1 + 1;
  }
  else {
    uVar8 = param_1[2];
  }
  puVar9 = (undefined1 *)(uVar8 + uVar14);
  if (param_2 != param_3) {
    puVar6 = puVar9;
    if ((0x1f < uVar5) &&
       ((param_3 <= puVar9 || (param_3 + uVar8 + (uVar14 - (long)param_2) <= param_2)))) {
      uVar10 = uVar5 & 0xffffffffffffffe0;
      puVar12 = (undefined8 *)(param_2 + 0x10);
      puVar9 = puVar9 + uVar10;
      puVar11 = (undefined8 *)(uVar14 + uVar8 + 0x10);
      uVar8 = uVar10;
      do {
        puVar4 = puVar12 + -1;
        uVar15 = puVar12[-2];
        uVar17 = puVar12[1];
        uVar16 = *puVar12;
        puVar12 = puVar12 + 4;
        uVar8 = uVar8 - 0x20;
        puVar11[-1] = *puVar4;
        puVar11[-2] = uVar15;
        puVar11[1] = uVar17;
        *puVar11 = uVar16;
        puVar11 = puVar11 + 4;
      } while (uVar8 != 0);
      puVar6 = puVar9;
      param_2 = param_2 + uVar10;
      if (uVar5 == uVar10) goto LAB_00b3ef3c;
    }
    do {
      puVar13 = param_2 + 1;
      puVar9 = puVar6 + 1;
      *puVar6 = *param_2;
      puVar6 = puVar9;
      param_2 = puVar13;
    } while (param_3 != puVar13);
  }
LAB_00b3ef3c:
  *puVar9 = 0;
  if ((*param_1 & 1) == 0) {
    *(char *)param_1 = (char)((int)(uVar14 + uVar5) << 1);
  }
  else {
    param_1[1] = uVar14 + uVar5;
  }
LAB_00b3f008:
                    /* try { // try from 00b3f010 to 00c3f02b has its CatchHandler @ 00b40ccc */
  if (*(long *)(lVar3 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3edac"></a> `00b3edac` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b3edb0"></a> `00b3edb0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3edb4"></a> `00b3edb4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3edb8"></a> `00b3edb8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3edbc"></a> `00b3edbc` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3edc0"></a> `00b3edc0` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b3edc4"></a> `00b3edc4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b3edc8"></a> `00b3edc8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b3edcc"></a> `00b3edcc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00b3edd0"></a> `00b3edd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b3edd4"></a> `00b3edd4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00b3edd8"></a> `00b3edd8` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b3eddc"></a> `00b3eddc` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00b3ede0"></a> `00b3ede0` | `89 01 00 37` | tbnz w9,#0x0,0x00b3ee10 | `CONDITIONAL_JUMP`
<a id="insn-00b3ede4"></a> `00b3ede4` | `36 fd 41 d3` | lsr x22,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ede8"></a> `00b3ede8` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00b3edec"></a> `00b3edec` | `e8 03 09 2a` | mov w8,w9 | `FALL_THROUGH`
<a id="insn-00b3edf0"></a> `00b3edf0` | `98 02 15 eb` | subs x24,x20,x21 | `FALL_THROUGH`
<a id="insn-00b3edf4"></a> `00b3edf4` | `a0 10 00 54` | b.eq 0x00b3f008 | `CONDITIONAL_JUMP`
<a id="insn-00b3edf8"></a> `00b3edf8` | `89 01 00 37` | tbnz w9,#0x0,0x00b3ee28 | `CONDITIONAL_JUMP`
<a id="insn-00b3edfc"></a> `00b3edfc` | `6a 06 00 91` | add x10,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ee00"></a> `00b3ee00` | `29 fd 41 d3` | lsr x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ee04"></a> `00b3ee04` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00b3ee08"></a> `00b3ee08` | `69 01 00 54` | b.ls 0x00b3ee34 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee0c"></a> `00b3ee0c` | `1d 00 00 14` | b 0x00b3ee80 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ee10"></a> `00b3ee10` | `68 5a 40 a9` | ldp x8,x22,[x19] | `FALL_THROUGH`
<a id="insn-00b3ee14"></a> `00b3ee14` | `0a f9 7f 92` | and x10,x8,#-0x2 | `FALL_THROUGH`
<a id="insn-00b3ee18"></a> `00b3ee18` | `41 05 00 d1` | sub x1,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ee1c"></a> `00b3ee1c` | `98 02 15 eb` | subs x24,x20,x21 | `FALL_THROUGH`
<a id="insn-00b3ee20"></a> `00b3ee20` | `c1 fe ff 54` | b.ne 0x00b3edf8 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee24"></a> `00b3ee24` | `79 00 00 14` | b 0x00b3f008 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ee28"></a> `00b3ee28` | `69 aa 40 a9` | ldp x9,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b3ee2c"></a> `00b3ee2c` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00b3ee30"></a> `00b3ee30` | `88 02 00 54` | b.hi 0x00b3ee80 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee34"></a> `00b3ee34` | `49 01 09 8b` | add x9,x10,x9 | `FALL_THROUGH`
<a id="insn-00b3ee38"></a> `00b3ee38` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00b3ee3c"></a> `00b3ee3c` | `29 02 00 54` | b.ls 0x00b3ee80 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee40"></a> `00b3ee40` | `1f 43 00 b1` | cmn x24,#0x10 | `FALL_THROUGH`
<a id="insn-00b3ee44"></a> `00b3ee44` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3ee48"></a> `00b3ee48` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00b3ee4c"></a> `00b3ee4c` | `62 0f 00 54` | b.cs 0x00b3f038 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee50"></a> `00b3ee50` | `1f 5b 00 f1` | cmp x24,#0x16 | `FALL_THROUGH`
<a id="insn-00b3ee54"></a> `00b3ee54` | `68 08 00 54` | b.hi 0x00b3ef60 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee58"></a> `00b3ee58` | `08 7b 1f 53` | lsl w8,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ee5c"></a> `00b3ee5c` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00b3ee60"></a> `00b3ee60` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b3ee64"></a> `00b3ee64` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ee68"></a> `00b3ee68` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00b3ee6c"></a> `00b3ee6c` | `20 0b 00 54` | b.eq 0x00b3efd0 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee70"></a> `00b3ee70` | `1f 83 00 f1` | cmp x24,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ee74"></a> `00b3ee74` | `a2 08 00 54` | b.cs 0x00b3ef88 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee78"></a> `00b3ee78` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00b3ee7c"></a> `00b3ee7c` | `51 00 00 14` | b 0x00b3efc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ee80"></a> `00b3ee80` | `29 00 16 cb` | sub x9,x1,x22 | `FALL_THROUGH`
<a id="insn-00b3ee84"></a> `00b3ee84` | `3f 01 18 eb` | cmp x9,x24 | `FALL_THROUGH`
<a id="insn-00b3ee88"></a> `00b3ee88` | `42 01 00 54` | b.cs 0x00b3eeb0 | `CONDITIONAL_JUMP`
<a id="insn-00b3ee8c"></a> `00b3ee8c` | `c8 02 18 8b` | add x8,x22,x24 | `FALL_THROUGH`
<a id="insn-00b3ee90"></a> `00b3ee90` | `02 01 01 cb` | sub x2,x8,x1 | `FALL_THROUGH`
<a id="insn-00b3ee94"></a> `00b3ee94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3ee98"></a> `00b3ee98` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00b3ee9c"></a> `00b3ee9c` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00b3eea0"></a> `00b3eea0` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00b3eea4"></a> `00b3eea4` | `e6 03 1f aa` | mov x6,xzr | `FALL_THROUGH`
<a id="insn-00b3eea8"></a> `00b3eea8` | `fa 7a 02 94` | bl 0x00bdda90 | `UNCONDITIONAL_CALL`
<a id="insn-00b3eeac"></a> `00b3eeac` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b3eeb0"></a> `00b3eeb0` | `68 00 00 37` | tbnz w8,#0x0,0x00b3eebc | `CONDITIONAL_JUMP`
<a id="insn-00b3eeb4"></a> `00b3eeb4` | `69 06 00 91` | add x9,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00b3eeb8"></a> `00b3eeb8` | `02 00 00 14` | b 0x00b3eec0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3eebc"></a> `00b3eebc` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b3eec0"></a> `00b3eec0` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00b3eec4"></a> `00b3eec4` | `28 01 16 8b` | add x8,x9,x22 | `FALL_THROUGH`
<a id="insn-00b3eec8"></a> `00b3eec8` | `a0 03 00 54` | b.eq 0x00b3ef3c | `CONDITIONAL_JUMP`
<a id="insn-00b3eecc"></a> `00b3eecc` | `1f 83 00 f1` | cmp x24,#0x20 | `FALL_THROUGH`
<a id="insn-00b3eed0"></a> `00b3eed0` | `e3 02 00 54` | b.cc 0x00b3ef2c | `CONDITIONAL_JUMP`
<a id="insn-00b3eed4"></a> `00b3eed4` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00b3eed8"></a> `00b3eed8` | `c2 00 00 54` | b.cs 0x00b3eef0 | `CONDITIONAL_JUMP`
<a id="insn-00b3eedc"></a> `00b3eedc` | `ca 02 15 cb` | sub x10,x22,x21 | `FALL_THROUGH`
<a id="insn-00b3eee0"></a> `00b3eee0` | `8a 02 0a 8b` | add x10,x20,x10 | `FALL_THROUGH`
<a id="insn-00b3eee4"></a> `00b3eee4` | `2a 01 0a 8b` | add x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3eee8"></a> `00b3eee8` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00b3eeec"></a> `00b3eeec` | `08 02 00 54` | b.hi 0x00b3ef2c | `CONDITIONAL_JUMP`
<a id="insn-00b3eef0"></a> `00b3eef0` | `0a eb 7b 92` | and x10,x24,#-0x20 | `FALL_THROUGH`
<a id="insn-00b3eef4"></a> `00b3eef4` | `c9 02 09 8b` | add x9,x22,x9 | `FALL_THROUGH`
<a id="insn-00b3eef8"></a> `00b3eef8` | `ab 42 00 91` | add x11,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00b3eefc"></a> `00b3eefc` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3ef00"></a> `00b3ef00` | `b5 02 0a 8b` | add x21,x21,x10 | `FALL_THROUGH`
<a id="insn-00b3ef04"></a> `00b3ef04` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00b3ef08"></a> `00b3ef08` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00b3ef0c"></a> `00b3ef0c` | `60 85 7f ad` | ldp q0,q1,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00b3ef10"></a> `00b3ef10` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ef14"></a> `00b3ef14` | `8c 81 00 f1` | subs x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ef18"></a> `00b3ef18` | `20 85 3f ad` | stp q0,q1,[x9, #-0x10] | `FALL_THROUGH`
<a id="insn-00b3ef1c"></a> `00b3ef1c` | `29 81 00 91` | add x9,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ef20"></a> `00b3ef20` | `61 ff ff 54` | b.ne 0x00b3ef0c | `CONDITIONAL_JUMP`
<a id="insn-00b3ef24"></a> `00b3ef24` | `1f 03 0a eb` | cmp x24,x10 | `FALL_THROUGH`
<a id="insn-00b3ef28"></a> `00b3ef28` | `a0 00 00 54` | b.eq 0x00b3ef3c | `CONDITIONAL_JUMP`
<a id="insn-00b3ef2c"></a> `00b3ef2c` | `a9 16 40 38` | ldrb w9,[x21], #0x1 | `FALL_THROUGH`
<a id="insn-00b3ef30"></a> `00b3ef30` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00b3ef34"></a> `00b3ef34` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00b3ef38"></a> `00b3ef38` | `a1 ff ff 54` | b.ne 0x00b3ef2c | `CONDITIONAL_JUMP`
<a id="insn-00b3ef3c"></a> `00b3ef3c` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00b3ef40"></a> `00b3ef40` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00b3ef44"></a> `00b3ef44` | `c8 02 18 8b` | add x8,x22,x24 | `FALL_THROUGH`
<a id="insn-00b3ef48"></a> `00b3ef48` | `89 00 00 37` | tbnz w9,#0x0,0x00b3ef58 | `CONDITIONAL_JUMP`
<a id="insn-00b3ef4c"></a> `00b3ef4c` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ef50"></a> `00b3ef50` | `68 02 00 39` | strb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b3ef54"></a> `00b3ef54` | `2d 00 00 14` | b 0x00b3f008 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ef58"></a> `00b3ef58` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b3ef5c"></a> `00b3ef5c` | `2b 00 00 14` | b 0x00b3f008 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ef60"></a> `00b3ef60` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00b3ef64"></a> `00b3ef64` | `16 ed 7c 92` | and x22,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b3ef68"></a> `00b3ef68` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b3ef6c"></a> `00b3ef6c` | `35 70 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ef70"></a> `00b3ef70` | `c8 02 40 b2` | orr x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ef74"></a> `00b3ef74` | `e8 63 00 a9` | stp x8,x24,[sp] | `FALL_THROUGH`
<a id="insn-00b3ef78"></a> `00b3ef78` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3ef7c"></a> `00b3ef7c` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00b3ef80"></a> `00b3ef80` | `81 f7 ff 54` | b.ne 0x00b3ee70 | `CONDITIONAL_JUMP`
<a id="insn-00b3ef84"></a> `00b3ef84` | `13 00 00 14` | b 0x00b3efd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ef88"></a> `00b3ef88` | `0a eb 7b 92` | and x10,x24,#-0x20 | `FALL_THROUGH`
<a id="insn-00b3ef8c"></a> `00b3ef8c` | `0b 40 00 91` | add x11,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00b3ef90"></a> `00b3ef90` | `a9 02 0a 8b` | add x9,x21,x10 | `FALL_THROUGH`
<a id="insn-00b3ef94"></a> `00b3ef94` | `00 00 0a 8b` | add x0,x0,x10 | `FALL_THROUGH`
<a id="insn-00b3ef98"></a> `00b3ef98` | `ac 42 00 91` | add x12,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00b3ef9c"></a> `00b3ef9c` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00b3efa0"></a> `00b3efa0` | `80 85 7f ad` | ldp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00b3efa4"></a> `00b3efa4` | `ad 81 00 f1` | subs x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00b3efa8"></a> `00b3efa8` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00b3efac"></a> `00b3efac` | `60 85 3f ad` | stp q0,q1,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00b3efb0"></a> `00b3efb0` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00b3efb4"></a> `00b3efb4` | `61 ff ff 54` | b.ne 0x00b3efa0 | `CONDITIONAL_JUMP`
<a id="insn-00b3efb8"></a> `00b3efb8` | `1f 03 0a eb` | cmp x24,x10 | `FALL_THROUGH`
<a id="insn-00b3efbc"></a> `00b3efbc` | `a0 00 00 54` | b.eq 0x00b3efd0 | `CONDITIONAL_JUMP`
<a id="insn-00b3efc0"></a> `00b3efc0` | `2a 15 40 38` | ldrb w10,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00b3efc4"></a> `00b3efc4` | `9f 02 09 eb` | cmp x20,x9 | `FALL_THROUGH`
<a id="insn-00b3efc8"></a> `00b3efc8` | `0a 14 00 38` | strb w10,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00b3efcc"></a> `00b3efcc` | `a1 ff ff 54` | b.ne 0x00b3efc0 | `CONDITIONAL_JUMP`
<a id="insn-00b3efd0"></a> `00b3efd0` | `1f 00 00 39` | strb wzr,[x0] | `FALL_THROUGH`
<a id="insn-00b3efd4"></a> `00b3efd4` | `ec af 40 a9` | ldp x12,x11,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3efd8"></a> `00b3efd8` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00b3efdc"></a> `00b3efdc` | `0a 1d 01 53` | ubfx w10,w8,#0x1,#0x7 | `FALL_THROUGH`
<a id="insn-00b3efe0"></a> `00b3efe0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3efe4"></a> `00b3efe4` | `28 01 40 b2` | orr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3efe8"></a> `00b3efe8` | `01 01 8b 9a` | csel x1,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00b3efec"></a> `00b3efec` | `42 01 8c 9a` | csel x2,x10,x12,eq | `FALL_THROUGH`
<a id="insn-00b3eff0"></a> `00b3eff0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3eff4"></a> `00b3eff4` | `4f 70 02 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00b3eff8"></a> `00b3eff8` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b3effc"></a> `00b3effc` | `68 00 00 36` | tbz w8,#0x0,0x00b3f008 | `CONDITIONAL_JUMP`
<a id="insn-00b3f000"></a> `00b3f000` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3f004"></a> `00b3f004` | `17 70 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b3f008"></a> `00b3f008` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b3f00c"></a> `00b3f00c` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b3f010"></a> `00b3f010` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b3f014"></a> `00b3f014` | `01 01 00 54` | b.ne 0x00b3f034 | `CONDITIONAL_JUMP`
<a id="insn-00b3f018"></a> `00b3f018` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3f01c"></a> `00b3f01c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3f020"></a> `00b3f020` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3f024"></a> `00b3f024` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3f028"></a> `00b3f028` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3f02c"></a> `00b3f02c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b3f030"></a> `00b3f030` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b3f034"></a> `00b3f034` | `17 70 02 94` | bl 0x00bdb090 | `CALL_TERMINATOR`
<a id="insn-00b3f038"></a> `00b3f038` | `a2 7c 02 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3edac`](#insn-00b3edac) 範囲 `[['00b3edac', '00b3ede3']]`
  - `CONDITIONAL_JUMP` [`00b3ede0`](#insn-00b3ede0) → [`00b3ee10`](#insn-00b3ee10)
  - `FALL_THROUGH` [`00b3ede0`](#insn-00b3ede0) → [`00b3ede4`](#insn-00b3ede4)
- ブロック [`00b3ede4`](#insn-00b3ede4) 範囲 `[['00b3ede4', '00b3edf7']]`
  - `CONDITIONAL_JUMP` [`00b3edf4`](#insn-00b3edf4) → [`00b3f008`](#insn-00b3f008)
  - `FALL_THROUGH` [`00b3edf4`](#insn-00b3edf4) → [`00b3edf8`](#insn-00b3edf8)
- ブロック [`00b3edf8`](#insn-00b3edf8) 範囲 `[['00b3edf8', '00b3edfb']]`
  - `CONDITIONAL_JUMP` [`00b3edf8`](#insn-00b3edf8) → [`00b3ee28`](#insn-00b3ee28)
  - `FALL_THROUGH` [`00b3edf8`](#insn-00b3edf8) → [`00b3edfc`](#insn-00b3edfc)
- ブロック [`00b3edfc`](#insn-00b3edfc) 範囲 `[['00b3edfc', '00b3ee0b']]`
  - `CONDITIONAL_JUMP` [`00b3ee08`](#insn-00b3ee08) → [`00b3ee34`](#insn-00b3ee34)
  - `FALL_THROUGH` [`00b3ee08`](#insn-00b3ee08) → [`00b3ee0c`](#insn-00b3ee0c)
- ブロック [`00b3ee0c`](#insn-00b3ee0c) 範囲 `[['00b3ee0c', '00b3ee0f']]`
  - `UNCONDITIONAL_JUMP` [`00b3ee0c`](#insn-00b3ee0c) → [`00b3ee80`](#insn-00b3ee80)
- ブロック [`00b3ee10`](#insn-00b3ee10) 範囲 `[['00b3ee10', '00b3ee23']]`
  - `CONDITIONAL_JUMP` [`00b3ee20`](#insn-00b3ee20) → [`00b3edf8`](#insn-00b3edf8)
  - `FALL_THROUGH` [`00b3ee20`](#insn-00b3ee20) → [`00b3ee24`](#insn-00b3ee24)
- ブロック [`00b3ee24`](#insn-00b3ee24) 範囲 `[['00b3ee24', '00b3ee27']]`
  - `UNCONDITIONAL_JUMP` [`00b3ee24`](#insn-00b3ee24) → [`00b3f008`](#insn-00b3f008)
- ブロック [`00b3ee28`](#insn-00b3ee28) 範囲 `[['00b3ee28', '00b3ee33']]`
  - `CONDITIONAL_JUMP` [`00b3ee30`](#insn-00b3ee30) → [`00b3ee80`](#insn-00b3ee80)
  - `FALL_THROUGH` [`00b3ee30`](#insn-00b3ee30) → [`00b3ee34`](#insn-00b3ee34)
- ブロック [`00b3ee34`](#insn-00b3ee34) 範囲 `[['00b3ee34', '00b3ee3f']]`
  - `CONDITIONAL_JUMP` [`00b3ee3c`](#insn-00b3ee3c) → [`00b3ee80`](#insn-00b3ee80)
  - `FALL_THROUGH` [`00b3ee3c`](#insn-00b3ee3c) → [`00b3ee40`](#insn-00b3ee40)
- ブロック [`00b3ee40`](#insn-00b3ee40) 範囲 `[['00b3ee40', '00b3ee4f']]`
  - `CONDITIONAL_JUMP` [`00b3ee4c`](#insn-00b3ee4c) → [`00b3f038`](#insn-00b3f038)
  - `FALL_THROUGH` [`00b3ee4c`](#insn-00b3ee4c) → [`00b3ee50`](#insn-00b3ee50)
- ブロック [`00b3ee50`](#insn-00b3ee50) 範囲 `[['00b3ee50', '00b3ee57']]`
  - `CONDITIONAL_JUMP` [`00b3ee54`](#insn-00b3ee54) → [`00b3ef60`](#insn-00b3ef60)
  - `FALL_THROUGH` [`00b3ee54`](#insn-00b3ee54) → [`00b3ee58`](#insn-00b3ee58)
- ブロック [`00b3ee58`](#insn-00b3ee58) 範囲 `[['00b3ee58', '00b3ee6f']]`
  - `CONDITIONAL_JUMP` [`00b3ee6c`](#insn-00b3ee6c) → [`00b3efd0`](#insn-00b3efd0)
  - `FALL_THROUGH` [`00b3ee6c`](#insn-00b3ee6c) → [`00b3ee70`](#insn-00b3ee70)
- ブロック [`00b3ee70`](#insn-00b3ee70) 範囲 `[['00b3ee70', '00b3ee77']]`
  - `CONDITIONAL_JUMP` [`00b3ee74`](#insn-00b3ee74) → [`00b3ef88`](#insn-00b3ef88)
  - `FALL_THROUGH` [`00b3ee74`](#insn-00b3ee74) → [`00b3ee78`](#insn-00b3ee78)
- ブロック [`00b3ee78`](#insn-00b3ee78) 範囲 `[['00b3ee78', '00b3ee7f']]`
  - `UNCONDITIONAL_JUMP` [`00b3ee7c`](#insn-00b3ee7c) → [`00b3efc0`](#insn-00b3efc0)
- ブロック [`00b3ee80`](#insn-00b3ee80) 範囲 `[['00b3ee80', '00b3ee8b']]`
  - `CONDITIONAL_JUMP` [`00b3ee88`](#insn-00b3ee88) → [`00b3eeb0`](#insn-00b3eeb0)
  - `FALL_THROUGH` [`00b3ee88`](#insn-00b3ee88) → [`00b3ee8c`](#insn-00b3ee8c)
- ブロック [`00b3ee8c`](#insn-00b3ee8c) 範囲 `[['00b3ee8c', '00b3eeab']]`
  - `FALL_THROUGH` [`00b3eea8`](#insn-00b3eea8) → [`00b3eeac`](#insn-00b3eeac)
- ブロック [`00b3eeac`](#insn-00b3eeac) 範囲 `[['00b3eeac', '00b3eeaf']]`
  - `FALL_THROUGH` [`00b3eeac`](#insn-00b3eeac) → [`00b3eeb0`](#insn-00b3eeb0)
- ブロック [`00b3eeb0`](#insn-00b3eeb0) 範囲 `[['00b3eeb0', '00b3eeb3']]`
  - `CONDITIONAL_JUMP` [`00b3eeb0`](#insn-00b3eeb0) → [`00b3eebc`](#insn-00b3eebc)
  - `FALL_THROUGH` [`00b3eeb0`](#insn-00b3eeb0) → [`00b3eeb4`](#insn-00b3eeb4)
- ブロック [`00b3eeb4`](#insn-00b3eeb4) 範囲 `[['00b3eeb4', '00b3eebb']]`
  - `UNCONDITIONAL_JUMP` [`00b3eeb8`](#insn-00b3eeb8) → [`00b3eec0`](#insn-00b3eec0)
- ブロック [`00b3eebc`](#insn-00b3eebc) 範囲 `[['00b3eebc', '00b3eebf']]`
  - `FALL_THROUGH` [`00b3eebc`](#insn-00b3eebc) → [`00b3eec0`](#insn-00b3eec0)
- ブロック [`00b3eec0`](#insn-00b3eec0) 範囲 `[['00b3eec0', '00b3eecb']]`
  - `CONDITIONAL_JUMP` [`00b3eec8`](#insn-00b3eec8) → [`00b3ef3c`](#insn-00b3ef3c)
  - `FALL_THROUGH` [`00b3eec8`](#insn-00b3eec8) → [`00b3eecc`](#insn-00b3eecc)
- ブロック [`00b3eecc`](#insn-00b3eecc) 範囲 `[['00b3eecc', '00b3eed3']]`
  - `CONDITIONAL_JUMP` [`00b3eed0`](#insn-00b3eed0) → [`00b3ef2c`](#insn-00b3ef2c)
  - `FALL_THROUGH` [`00b3eed0`](#insn-00b3eed0) → [`00b3eed4`](#insn-00b3eed4)
- ブロック [`00b3eed4`](#insn-00b3eed4) 範囲 `[['00b3eed4', '00b3eedb']]`
  - `CONDITIONAL_JUMP` [`00b3eed8`](#insn-00b3eed8) → [`00b3eef0`](#insn-00b3eef0)
  - `FALL_THROUGH` [`00b3eed8`](#insn-00b3eed8) → [`00b3eedc`](#insn-00b3eedc)
- ブロック [`00b3eedc`](#insn-00b3eedc) 範囲 `[['00b3eedc', '00b3eeef']]`
  - `CONDITIONAL_JUMP` [`00b3eeec`](#insn-00b3eeec) → [`00b3ef2c`](#insn-00b3ef2c)
  - `FALL_THROUGH` [`00b3eeec`](#insn-00b3eeec) → [`00b3eef0`](#insn-00b3eef0)
- ブロック [`00b3eef0`](#insn-00b3eef0) 範囲 `[['00b3eef0', '00b3ef0b']]`
  - `FALL_THROUGH` [`00b3ef08`](#insn-00b3ef08) → [`00b3ef0c`](#insn-00b3ef0c)
- ブロック [`00b3ef0c`](#insn-00b3ef0c) 範囲 `[['00b3ef0c', '00b3ef23']]`
  - `CONDITIONAL_JUMP` [`00b3ef20`](#insn-00b3ef20) → [`00b3ef0c`](#insn-00b3ef0c)
  - `FALL_THROUGH` [`00b3ef20`](#insn-00b3ef20) → [`00b3ef24`](#insn-00b3ef24)
- ブロック [`00b3ef24`](#insn-00b3ef24) 範囲 `[['00b3ef24', '00b3ef2b']]`
  - `CONDITIONAL_JUMP` [`00b3ef28`](#insn-00b3ef28) → [`00b3ef3c`](#insn-00b3ef3c)
  - `FALL_THROUGH` [`00b3ef28`](#insn-00b3ef28) → [`00b3ef2c`](#insn-00b3ef2c)
- ブロック [`00b3ef2c`](#insn-00b3ef2c) 範囲 `[['00b3ef2c', '00b3ef3b']]`
  - `CONDITIONAL_JUMP` [`00b3ef38`](#insn-00b3ef38) → [`00b3ef2c`](#insn-00b3ef2c)
  - `FALL_THROUGH` [`00b3ef38`](#insn-00b3ef38) → [`00b3ef3c`](#insn-00b3ef3c)
- ブロック [`00b3ef3c`](#insn-00b3ef3c) 範囲 `[['00b3ef3c', '00b3ef4b']]`
  - `CONDITIONAL_JUMP` [`00b3ef48`](#insn-00b3ef48) → [`00b3ef58`](#insn-00b3ef58)
  - `FALL_THROUGH` [`00b3ef48`](#insn-00b3ef48) → [`00b3ef4c`](#insn-00b3ef4c)
- ブロック [`00b3ef4c`](#insn-00b3ef4c) 範囲 `[['00b3ef4c', '00b3ef57']]`
  - `UNCONDITIONAL_JUMP` [`00b3ef54`](#insn-00b3ef54) → [`00b3f008`](#insn-00b3f008)
- ブロック [`00b3ef58`](#insn-00b3ef58) 範囲 `[['00b3ef58', '00b3ef5f']]`
  - `UNCONDITIONAL_JUMP` [`00b3ef5c`](#insn-00b3ef5c) → [`00b3f008`](#insn-00b3f008)
- ブロック [`00b3ef60`](#insn-00b3ef60) 範囲 `[['00b3ef60', '00b3ef83']]`
  - `CONDITIONAL_JUMP` [`00b3ef80`](#insn-00b3ef80) → [`00b3ee70`](#insn-00b3ee70)
  - `FALL_THROUGH` [`00b3ef80`](#insn-00b3ef80) → [`00b3ef84`](#insn-00b3ef84)
- ブロック [`00b3ef84`](#insn-00b3ef84) 範囲 `[['00b3ef84', '00b3ef87']]`
  - `UNCONDITIONAL_JUMP` [`00b3ef84`](#insn-00b3ef84) → [`00b3efd0`](#insn-00b3efd0)
- ブロック [`00b3ef88`](#insn-00b3ef88) 範囲 `[['00b3ef88', '00b3ef9f']]`
  - `FALL_THROUGH` [`00b3ef9c`](#insn-00b3ef9c) → [`00b3efa0`](#insn-00b3efa0)
- ブロック [`00b3efa0`](#insn-00b3efa0) 範囲 `[['00b3efa0', '00b3efb7']]`
  - `CONDITIONAL_JUMP` [`00b3efb4`](#insn-00b3efb4) → [`00b3efa0`](#insn-00b3efa0)
  - `FALL_THROUGH` [`00b3efb4`](#insn-00b3efb4) → [`00b3efb8`](#insn-00b3efb8)
- ブロック [`00b3efb8`](#insn-00b3efb8) 範囲 `[['00b3efb8', '00b3efbf']]`
  - `CONDITIONAL_JUMP` [`00b3efbc`](#insn-00b3efbc) → [`00b3efd0`](#insn-00b3efd0)
  - `FALL_THROUGH` [`00b3efbc`](#insn-00b3efbc) → [`00b3efc0`](#insn-00b3efc0)
- ブロック [`00b3efc0`](#insn-00b3efc0) 範囲 `[['00b3efc0', '00b3efcf']]`
  - `CONDITIONAL_JUMP` [`00b3efcc`](#insn-00b3efcc) → [`00b3efc0`](#insn-00b3efc0)
  - `FALL_THROUGH` [`00b3efcc`](#insn-00b3efcc) → [`00b3efd0`](#insn-00b3efd0)
- ブロック [`00b3efd0`](#insn-00b3efd0) 範囲 `[['00b3efd0', '00b3efff']]`
  - `CONDITIONAL_JUMP` [`00b3effc`](#insn-00b3effc) → [`00b3f008`](#insn-00b3f008)
  - `FALL_THROUGH` [`00b3effc`](#insn-00b3effc) → [`00b3f000`](#insn-00b3f000)
- ブロック [`00b3f000`](#insn-00b3f000) 範囲 `[['00b3f000', '00b3f007']]`
  - `FALL_THROUGH` [`00b3f004`](#insn-00b3f004) → [`00b3f008`](#insn-00b3f008)
- ブロック [`00b3f008`](#insn-00b3f008) 範囲 `[['00b3f008', '00b3f00f']]`
  - `FALL_THROUGH` [`00b3f00c`](#insn-00b3f00c) → [`00b3f010`](#insn-00b3f010)
- ブロック [`00b3f010`](#insn-00b3f010) 範囲 `[['00b3f010', '00b3f017']]`
  - `CONDITIONAL_JUMP` [`00b3f014`](#insn-00b3f014) → [`00b3f034`](#insn-00b3f034)
  - `FALL_THROUGH` [`00b3f014`](#insn-00b3f014) → [`00b3f018`](#insn-00b3f018)
- ブロック [`00b3f018`](#insn-00b3f018) 範囲 `[['00b3f018', '00b3f033']]`
- ブロック [`00b3f034`](#insn-00b3f034) 範囲 `[['00b3f034', '00b3f037']]`
- ブロック [`00b3f038`](#insn-00b3f038) 範囲 `[['00b3f038', '00b3f03b']]`

## 命令位置別の参照

- [`00b3edb0`](#insn-00b3edb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3edb4`](#insn-00b3edb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3edb8`](#insn-00b3edb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3edbc`](#insn-00b3edbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3edd8`](#insn-00b3edd8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ede0`](#insn-00b3ede0) → [`00b3ee10`](#insn-00b3ee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3edf4`](#insn-00b3edf4) → [`00b3f008`](#insn-00b3f008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3edf8`](#insn-00b3edf8) → [`00b3ee28`](#insn-00b3ee28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee08`](#insn-00b3ee08) → [`00b3ee34`](#insn-00b3ee34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee0c`](#insn-00b3ee0c) → [`00b3ee80`](#insn-00b3ee80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee20`](#insn-00b3ee20) → [`00b3edf8`](#insn-00b3edf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee24`](#insn-00b3ee24) → [`00b3f008`](#insn-00b3f008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee30`](#insn-00b3ee30) → [`00b3ee80`](#insn-00b3ee80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee3c`](#insn-00b3ee3c) → [`00b3ee80`](#insn-00b3ee80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee44`](#insn-00b3ee44) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee48`](#insn-00b3ee48) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee4c`](#insn-00b3ee4c) → [`00b3f038`](#insn-00b3f038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee54`](#insn-00b3ee54) → [`00b3ef60`](#insn-00b3ef60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee60`](#insn-00b3ee60) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee6c`](#insn-00b3ee6c) → [`00b3efd0`](#insn-00b3efd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee74`](#insn-00b3ee74) → [`00b3ef88`](#insn-00b3ef88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee7c`](#insn-00b3ee7c) → [`00b3efc0`](#insn-00b3efc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ee88`](#insn-00b3ee88) → [`00b3eeb0`](#insn-00b3eeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3eea8`](#insn-00b3eea8) → [`00bdda90`](../00bdd/00bdda90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdda90` · 推定シンボル `None` · 推定型 `None`
- [`00b3eeb0`](#insn-00b3eeb0) → [`00b3eebc`](#insn-00b3eebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3eeb8`](#insn-00b3eeb8) → [`00b3eec0`](#insn-00b3eec0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3eec8`](#insn-00b3eec8) → [`00b3ef3c`](#insn-00b3ef3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3eed0`](#insn-00b3eed0) → [`00b3ef2c`](#insn-00b3ef2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3eed8`](#insn-00b3eed8) → [`00b3eef0`](#insn-00b3eef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3eeec`](#insn-00b3eeec) → [`00b3ef2c`](#insn-00b3ef2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef20`](#insn-00b3ef20) → [`00b3ef0c`](#insn-00b3ef0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef28`](#insn-00b3ef28) → [`00b3ef3c`](#insn-00b3ef3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef38`](#insn-00b3ef38) → [`00b3ef2c`](#insn-00b3ef2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef48`](#insn-00b3ef48) → [`00b3ef58`](#insn-00b3ef58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef54`](#insn-00b3ef54) → [`00b3f008`](#insn-00b3f008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef5c`](#insn-00b3ef5c) → [`00b3f008`](#insn-00b3f008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef6c`](#insn-00b3ef6c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef74`](#insn-00b3ef74) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef78`](#insn-00b3ef78) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef80`](#insn-00b3ef80) → [`00b3ee70`](#insn-00b3ee70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ef84`](#insn-00b3ef84) → [`00b3efd0`](#insn-00b3efd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3efb4`](#insn-00b3efb4) → [`00b3efa0`](#insn-00b3efa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3efbc`](#insn-00b3efbc) → [`00b3efd0`](#insn-00b3efd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3efcc`](#insn-00b3efcc) → [`00b3efc0`](#insn-00b3efc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3efd4`](#insn-00b3efd4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3eff4`](#insn-00b3eff4) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00b3eff8`](#insn-00b3eff8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3effc`](#insn-00b3effc) → [`00b3f008`](#insn-00b3f008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f000`](#insn-00b3f000) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f004`](#insn-00b3f004) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b3f00c`](#insn-00b3f00c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f014`](#insn-00b3f014) → [`00b3f034`](#insn-00b3f034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f01c`](#insn-00b3f01c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f020`](#insn-00b3f020) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f024`](#insn-00b3f024) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f028`](#insn-00b3f028) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3f034`](#insn-00b3f034) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b3f038`](#insn-00b3f038) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3edb0`](#insn-00b3edb0)

~~~json
{
  "source": "00b3edb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3edb4`](#insn-00b3edb4)

~~~json
{
  "source": "00b3edb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3edb8`](#insn-00b3edb8)

~~~json
{
  "source": "00b3edb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3edbc`](#insn-00b3edbc)

~~~json
{
  "source": "00b3edbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3edd8`](#insn-00b3edd8)

~~~json
{
  "source": "00b3edd8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ede0`](#insn-00b3ede0)

~~~json
{
  "source": "00b3ede0",
  "target": "00b3ee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3edf4`](#insn-00b3edf4)

~~~json
{
  "source": "00b3edf4",
  "target": "00b3f008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3edf8`](#insn-00b3edf8)

~~~json
{
  "source": "00b3edf8",
  "target": "00b3ee28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee08`](#insn-00b3ee08)

~~~json
{
  "source": "00b3ee08",
  "target": "00b3ee34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee0c`](#insn-00b3ee0c)

~~~json
{
  "source": "00b3ee0c",
  "target": "00b3ee80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee20`](#insn-00b3ee20)

~~~json
{
  "source": "00b3ee20",
  "target": "00b3edf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee24`](#insn-00b3ee24)

~~~json
{
  "source": "00b3ee24",
  "target": "00b3f008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee30`](#insn-00b3ee30)

~~~json
{
  "source": "00b3ee30",
  "target": "00b3ee80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee3c`](#insn-00b3ee3c)

~~~json
{
  "source": "00b3ee3c",
  "target": "00b3ee80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee44`](#insn-00b3ee44)

~~~json
{
  "source": "00b3ee44",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee48`](#insn-00b3ee48)

~~~json
{
  "source": "00b3ee48",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee4c`](#insn-00b3ee4c)

~~~json
{
  "source": "00b3ee4c",
  "target": "00b3f038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee54`](#insn-00b3ee54)

~~~json
{
  "source": "00b3ee54",
  "target": "00b3ef60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee60`](#insn-00b3ee60)

~~~json
{
  "source": "00b3ee60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee6c`](#insn-00b3ee6c)

~~~json
{
  "source": "00b3ee6c",
  "target": "00b3efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee74`](#insn-00b3ee74)

~~~json
{
  "source": "00b3ee74",
  "target": "00b3ef88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee7c`](#insn-00b3ee7c)

~~~json
{
  "source": "00b3ee7c",
  "target": "00b3efc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ee88`](#insn-00b3ee88)

~~~json
{
  "source": "00b3ee88",
  "target": "00b3eeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3eea8`](#insn-00b3eea8)

~~~json
{
  "source": "00b3eea8",
  "target": "00bdda90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3eeb0`](#insn-00b3eeb0)

~~~json
{
  "source": "00b3eeb0",
  "target": "00b3eebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3eeb8`](#insn-00b3eeb8)

~~~json
{
  "source": "00b3eeb8",
  "target": "00b3eec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3eec8`](#insn-00b3eec8)

~~~json
{
  "source": "00b3eec8",
  "target": "00b3ef3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3eed0`](#insn-00b3eed0)

~~~json
{
  "source": "00b3eed0",
  "target": "00b3ef2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3eed8`](#insn-00b3eed8)

~~~json
{
  "source": "00b3eed8",
  "target": "00b3eef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3eeec`](#insn-00b3eeec)

~~~json
{
  "source": "00b3eeec",
  "target": "00b3ef2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef20`](#insn-00b3ef20)

~~~json
{
  "source": "00b3ef20",
  "target": "00b3ef0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef28`](#insn-00b3ef28)

~~~json
{
  "source": "00b3ef28",
  "target": "00b3ef3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef38`](#insn-00b3ef38)

~~~json
{
  "source": "00b3ef38",
  "target": "00b3ef2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef48`](#insn-00b3ef48)

~~~json
{
  "source": "00b3ef48",
  "target": "00b3ef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef54`](#insn-00b3ef54)

~~~json
{
  "source": "00b3ef54",
  "target": "00b3f008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef5c`](#insn-00b3ef5c)

~~~json
{
  "source": "00b3ef5c",
  "target": "00b3f008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef6c`](#insn-00b3ef6c)

~~~json
{
  "source": "00b3ef6c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ef74`](#insn-00b3ef74)

~~~json
{
  "source": "00b3ef74",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef78`](#insn-00b3ef78)

~~~json
{
  "source": "00b3ef78",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef80`](#insn-00b3ef80)

~~~json
{
  "source": "00b3ef80",
  "target": "00b3ee70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ef84`](#insn-00b3ef84)

~~~json
{
  "source": "00b3ef84",
  "target": "00b3efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3efb4`](#insn-00b3efb4)

~~~json
{
  "source": "00b3efb4",
  "target": "00b3efa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3efbc`](#insn-00b3efbc)

~~~json
{
  "source": "00b3efbc",
  "target": "00b3efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3efcc`](#insn-00b3efcc)

~~~json
{
  "source": "00b3efcc",
  "target": "00b3efc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3efd4`](#insn-00b3efd4)

~~~json
{
  "source": "00b3efd4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3eff4`](#insn-00b3eff4)

~~~json
{
  "source": "00b3eff4",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3eff8`](#insn-00b3eff8)

~~~json
{
  "source": "00b3eff8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3effc`](#insn-00b3effc)

~~~json
{
  "source": "00b3effc",
  "target": "00b3f008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f000`](#insn-00b3f000)

~~~json
{
  "source": "00b3f000",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f004`](#insn-00b3f004)

~~~json
{
  "source": "00b3f004",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3f00c`](#insn-00b3f00c)

~~~json
{
  "source": "00b3f00c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f014`](#insn-00b3f014)

~~~json
{
  "source": "00b3f014",
  "target": "00b3f034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f01c`](#insn-00b3f01c)

~~~json
{
  "source": "00b3f01c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f020`](#insn-00b3f020)

~~~json
{
  "source": "00b3f020",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f024`](#insn-00b3f024)

~~~json
{
  "source": "00b3f024",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f028`](#insn-00b3f028)

~~~json
{
  "source": "00b3f028",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3f034`](#insn-00b3f034)

~~~json
{
  "source": "00b3f034",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3f038`](#insn-00b3f038)

~~~json
{
  "source": "00b3f038",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
