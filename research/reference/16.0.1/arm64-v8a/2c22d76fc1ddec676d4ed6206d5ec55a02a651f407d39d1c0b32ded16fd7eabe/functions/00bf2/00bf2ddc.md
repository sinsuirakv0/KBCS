# 00bf2ddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf29b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0040.md#compare-ab89c3ba027524b5dd468519cab6bf84)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf2e78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-edfd897adbfc7e188d4c1f1c3c55819c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf2ddc",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cfb153b1c9f98f08f519228e35ec66de1d15667b60983b89517357811478409",
  "source_text_sha256": "2cfb153b1c9f98f08f519228e35ec66de1d15667b60983b89517357811478409",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf2ddc",
        "00bf2f33"
      ]
    ],
    "bytes_sha256": "54e7a5f68699c9c1e483e8f4259204d5937bdc0611da6cc675e9e7c9043b2ee5",
    "instruction_count": 86,
    "instruction_bytes": 344,
    "body_bytes": 344,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e010](../00c5e/00c5e010.md)

## 呼び出し先

- [00bf28d8](../00bf2/00bf28d8.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2166 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw
               (ulong *param_1,ulong param_2,ulong param_3,undefined4 param_4)

{
  ulong uVar1;
  long lVar2;
  byte bVar3;
  byte *pbVar4;
  ulong uVar5;
  ulong uVar6;
  byte *pbVar7;
  ulong uVar8;
  byte *pbVar9;
  
  bVar3 = (byte)*param_1;
  uVar1 = (ulong)(bVar3 >> 1);
  if ((bVar3 & 1) != 0) {
    uVar1 = param_1[1];
  }
  if (uVar1 < param_2) {
                    /* WARNING: Subroutine does not return */
    FUN_00bf28d8();
  }
  if (param_3 == 0) {
    return;
  }
  lVar2 = 4;
  if ((bVar3 & 1) != 0) {
    lVar2 = (*param_1 & 0xfffffffffffffffe) - 1;
  }
  if (lVar2 - uVar1 < param_3) {
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm
              (param_1,lVar2,(uVar1 + param_3) - lVar2,uVar1,param_2,0,param_3);
    pbVar9 = (byte *)param_1[2];
    param_1[1] = uVar1 + param_3;
  }
  else {
    pbVar9 = (byte *)((long)param_1 + 4);
    if ((*param_1 & 1) != 0) {
      pbVar9 = (byte *)param_1[2];
    }
    if (uVar1 - param_2 != 0) {
      memmove(pbVar9 + param_2 * 4 + param_3 * 4,pbVar9 + param_2 * 4,(uVar1 - param_2) * 4);
    }
  }
  pbVar4 = pbVar9 + param_2 * 4;
  uVar5 = param_3;
  if (7 < param_3) {
    uVar6 = param_3 & 0xfffffffffffffff8;
    uVar5 = param_3 & 7;
    pbVar7 = pbVar4 + 0x10;
    uVar8 = uVar6;
    do {
      uVar8 = uVar8 - 8;
      *(ulong *)(pbVar7 + -8) = CONCAT44(param_4,param_4);
      *(ulong *)(pbVar7 + -0x10) = CONCAT44(param_4,param_4);
      *(ulong *)(pbVar7 + 8) = CONCAT44(param_4,param_4);
      *(ulong *)pbVar7 = CONCAT44(param_4,param_4);
      pbVar7 = pbVar7 + 0x20;
    } while (uVar8 != 0);
    pbVar4 = pbVar4 + uVar6 * 4;
    if (uVar6 == param_3) goto LAB_00bf2ef8;
  }
  do {
    uVar5 = uVar5 - 1;
    *(undefined4 *)pbVar4 = param_4;
    pbVar4 = pbVar4 + 4;
  } while (uVar5 != 0);
LAB_00bf2ef8:
  uVar1 = uVar1 + param_3;
  if ((*param_1 & 1) == 0) {
    *(byte *)param_1 = (byte)((int)uVar1 << 1);
  }
  else {
    param_1[1] = uVar1;
  }
  pbVar9 = pbVar9 + uVar1 * 4;
  pbVar9[0] = 0;
  pbVar9[1] = 0;
  pbVar9[2] = 0;
  pbVar9[3] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf2ddc"></a> `00bf2ddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf2de0"></a> `00bf2de0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bf2de4"></a> `00bf2de4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2de8"></a> `00bf2de8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf2dec"></a> `00bf2dec` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf2df0"></a> `00bf2df0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf2df4"></a> `00bf2df4` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bf2df8"></a> `00bf2df8` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bf2dfc"></a> `00bf2dfc` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2e00"></a> `00bf2e00` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2e04"></a> `00bf2e04` | `54 01 89 9a` | csel x20,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bf2e08"></a> `00bf2e08` | `9f 02 01 eb` | cmp x20,x1 | `FALL_THROUGH`
<a id="insn-00bf2e0c"></a> `00bf2e0c` | `23 09 00 54` | b.cc 0x00bf2f30 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e10"></a> `00bf2e10` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bf2e14"></a> `00bf2e14` | `22 08 00 b4` | cbz x2,0x00bf2f18 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e18"></a> `00bf2e18` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bf2e1c"></a> `00bf2e1c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2e20"></a> `00bf2e20` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bf2e24"></a> `00bf2e24` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bf2e28"></a> `00bf2e28` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00bf2e2c"></a> `00bf2e2c` | `2a f9 7f 92` | and x10,x9,#-0x2 | `FALL_THROUGH`
<a id="insn-00bf2e30"></a> `00bf2e30` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2e34"></a> `00bf2e34` | `01 01 8a 9a` | csel x1,x8,x10,eq | `FALL_THROUGH`
<a id="insn-00bf2e38"></a> `00bf2e38` | `28 00 14 cb` | sub x8,x1,x20 | `FALL_THROUGH`
<a id="insn-00bf2e3c"></a> `00bf2e3c` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bf2e40"></a> `00bf2e40` | `a2 01 00 54` | b.cs 0x00bf2e74 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e44"></a> `00bf2e44` | `98 02 15 8b` | add x24,x20,x21 | `FALL_THROUGH`
<a id="insn-00bf2e48"></a> `00bf2e48` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bf2e4c"></a> `00bf2e4c` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00bf2e50"></a> `00bf2e50` | `02 03 01 cb` | sub x2,x24,x1 | `FALL_THROUGH`
<a id="insn-00bf2e54"></a> `00bf2e54` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00bf2e58"></a> `00bf2e58` | `e6 03 15 aa` | mov x6,x21 | `FALL_THROUGH`
<a id="insn-00bf2e5c"></a> `00bf2e5c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bf2e60"></a> `00bf2e60` | `90 9e 01 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf2e64"></a> `00bf2e64` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bf2e68"></a> `00bf2e68` | `f7 0a 40 f9` | ldr x23,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2e6c"></a> `00bf2e6c` | `18 04 00 f9` | str x24,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bf2e70"></a> `00bf2e70` | `0e 00 00 14` | b 0x00bf2ea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf2e74"></a> `00bf2e74` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2e78"></a> `00bf2e78` | `0a 10 00 91` | add x10,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bf2e7c"></a> `00bf2e7c` | `3f 01 40 f2` | tst x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2e80"></a> `00bf2e80` | `57 01 88 9a` | csel x23,x10,x8,eq | `FALL_THROUGH`
<a id="insn-00bf2e84"></a> `00bf2e84` | `89 02 16 eb` | subs x9,x20,x22 | `FALL_THROUGH`
<a id="insn-00bf2e88"></a> `00bf2e88` | `00 01 00 54` | b.eq 0x00bf2ea8 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e8c"></a> `00bf2e8c` | `e1 0a 16 8b` | add x1,x23,x22, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf2e90"></a> `00bf2e90` | `22 f5 7e d3` | lsl x2,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bf2e94"></a> `00bf2e94` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bf2e98"></a> `00bf2e98` | `28 08 15 8b` | add x8,x1,x21, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf2e9c"></a> `00bf2e9c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bf2ea0"></a> `00bf2ea0` | `28 94 01 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-00bf2ea4"></a> `00bf2ea4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bf2ea8"></a> `00bf2ea8` | `eb 0a 16 8b` | add x11,x23,x22, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf2eac"></a> `00bf2eac` | `bf 22 00 f1` | cmp x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bf2eb0"></a> `00bf2eb0` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bf2eb4"></a> `00bf2eb4` | `e8 03 0b aa` | mov x8,x11 | `FALL_THROUGH`
<a id="insn-00bf2eb8"></a> `00bf2eb8` | `a3 01 00 54` | b.cc 0x00bf2eec | `CONDITIONAL_JUMP`
<a id="insn-00bf2ebc"></a> `00bf2ebc` | `aa f2 7d 92` | and x10,x21,#-0x8 | `FALL_THROUGH`
<a id="insn-00bf2ec0"></a> `00bf2ec0` | `60 0e 04 4e` | dup v0.4S,w19 | `FALL_THROUGH`
<a id="insn-00bf2ec4"></a> `00bf2ec4` | `a9 0a 40 92` | and x9,x21,#0x7 | `FALL_THROUGH`
<a id="insn-00bf2ec8"></a> `00bf2ec8` | `68 09 0a 8b` | add x8,x11,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf2ecc"></a> `00bf2ecc` | `6b 41 00 91` | add x11,x11,#0x10 | `FALL_THROUGH`
<a id="insn-00bf2ed0"></a> `00bf2ed0` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00bf2ed4"></a> `00bf2ed4` | `8c 21 00 f1` | subs x12,x12,#0x8 | `FALL_THROUGH`
<a id="insn-00bf2ed8"></a> `00bf2ed8` | `60 81 3f ad` | stp q0,q0,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf2edc"></a> `00bf2edc` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00bf2ee0"></a> `00bf2ee0` | `a1 ff ff 54` | b.ne 0x00bf2ed4 | `CONDITIONAL_JUMP`
<a id="insn-00bf2ee4"></a> `00bf2ee4` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00bf2ee8"></a> `00bf2ee8` | `80 00 00 54` | b.eq 0x00bf2ef8 | `CONDITIONAL_JUMP`
<a id="insn-00bf2eec"></a> `00bf2eec` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2ef0"></a> `00bf2ef0` | `13 45 00 b8` | str w19,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bf2ef4"></a> `00bf2ef4` | `c1 ff ff 54` | b.ne 0x00bf2eec | `CONDITIONAL_JUMP`
<a id="insn-00bf2ef8"></a> `00bf2ef8` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bf2efc"></a> `00bf2efc` | `88 02 15 8b` | add x8,x20,x21 | `FALL_THROUGH`
<a id="insn-00bf2f00"></a> `00bf2f00` | `89 00 00 37` | tbnz w9,#0x0,0x00bf2f10 | `CONDITIONAL_JUMP`
<a id="insn-00bf2f04"></a> `00bf2f04` | `09 79 1f 53` | lsl w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2f08"></a> `00bf2f08` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bf2f0c"></a> `00bf2f0c` | `02 00 00 14` | b 0x00bf2f14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf2f10"></a> `00bf2f10` | `08 04 00 f9` | str x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bf2f14"></a> `00bf2f14` | `ff 7a 28 b8` | str wzr,[x23, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00bf2f18"></a> `00bf2f18` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf2f1c"></a> `00bf2f1c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf2f20"></a> `00bf2f20` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2f24"></a> `00bf2f24` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bf2f28"></a> `00bf2f28` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf2f2c"></a> `00bf2f2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf2f30"></a> `00bf2f30` | `6a fe ff 97` | bl 0x00bf28d8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf2ddc`](#insn-00bf2ddc) 範囲 `[['00bf2ddc', '00bf2e0f']]`
  - `CONDITIONAL_JUMP` [`00bf2e0c`](#insn-00bf2e0c) → [`00bf2f30`](#insn-00bf2f30)
  - `FALL_THROUGH` [`00bf2e0c`](#insn-00bf2e0c) → [`00bf2e10`](#insn-00bf2e10)
- ブロック [`00bf2e10`](#insn-00bf2e10) 範囲 `[['00bf2e10', '00bf2e17']]`
  - `CONDITIONAL_JUMP` [`00bf2e14`](#insn-00bf2e14) → [`00bf2f18`](#insn-00bf2f18)
  - `FALL_THROUGH` [`00bf2e14`](#insn-00bf2e14) → [`00bf2e18`](#insn-00bf2e18)
- ブロック [`00bf2e18`](#insn-00bf2e18) 範囲 `[['00bf2e18', '00bf2e43']]`
  - `CONDITIONAL_JUMP` [`00bf2e40`](#insn-00bf2e40) → [`00bf2e74`](#insn-00bf2e74)
  - `FALL_THROUGH` [`00bf2e40`](#insn-00bf2e40) → [`00bf2e44`](#insn-00bf2e44)
- ブロック [`00bf2e44`](#insn-00bf2e44) 範囲 `[['00bf2e44', '00bf2e73']]`
  - `UNCONDITIONAL_JUMP` [`00bf2e70`](#insn-00bf2e70) → [`00bf2ea8`](#insn-00bf2ea8)
- ブロック [`00bf2e74`](#insn-00bf2e74) 範囲 `[['00bf2e74', '00bf2e8b']]`
  - `CONDITIONAL_JUMP` [`00bf2e88`](#insn-00bf2e88) → [`00bf2ea8`](#insn-00bf2ea8)
  - `FALL_THROUGH` [`00bf2e88`](#insn-00bf2e88) → [`00bf2e8c`](#insn-00bf2e8c)
- ブロック [`00bf2e8c`](#insn-00bf2e8c) 範囲 `[['00bf2e8c', '00bf2ea7']]`
  - `FALL_THROUGH` [`00bf2ea4`](#insn-00bf2ea4) → [`00bf2ea8`](#insn-00bf2ea8)
- ブロック [`00bf2ea8`](#insn-00bf2ea8) 範囲 `[['00bf2ea8', '00bf2ebb']]`
  - `CONDITIONAL_JUMP` [`00bf2eb8`](#insn-00bf2eb8) → [`00bf2eec`](#insn-00bf2eec)
  - `FALL_THROUGH` [`00bf2eb8`](#insn-00bf2eb8) → [`00bf2ebc`](#insn-00bf2ebc)
- ブロック [`00bf2ebc`](#insn-00bf2ebc) 範囲 `[['00bf2ebc', '00bf2ed3']]`
  - `FALL_THROUGH` [`00bf2ed0`](#insn-00bf2ed0) → [`00bf2ed4`](#insn-00bf2ed4)
- ブロック [`00bf2ed4`](#insn-00bf2ed4) 範囲 `[['00bf2ed4', '00bf2ee3']]`
  - `CONDITIONAL_JUMP` [`00bf2ee0`](#insn-00bf2ee0) → [`00bf2ed4`](#insn-00bf2ed4)
  - `FALL_THROUGH` [`00bf2ee0`](#insn-00bf2ee0) → [`00bf2ee4`](#insn-00bf2ee4)
- ブロック [`00bf2ee4`](#insn-00bf2ee4) 範囲 `[['00bf2ee4', '00bf2eeb']]`
  - `CONDITIONAL_JUMP` [`00bf2ee8`](#insn-00bf2ee8) → [`00bf2ef8`](#insn-00bf2ef8)
  - `FALL_THROUGH` [`00bf2ee8`](#insn-00bf2ee8) → [`00bf2eec`](#insn-00bf2eec)
- ブロック [`00bf2eec`](#insn-00bf2eec) 範囲 `[['00bf2eec', '00bf2ef7']]`
  - `CONDITIONAL_JUMP` [`00bf2ef4`](#insn-00bf2ef4) → [`00bf2eec`](#insn-00bf2eec)
  - `FALL_THROUGH` [`00bf2ef4`](#insn-00bf2ef4) → [`00bf2ef8`](#insn-00bf2ef8)
- ブロック [`00bf2ef8`](#insn-00bf2ef8) 範囲 `[['00bf2ef8', '00bf2f03']]`
  - `CONDITIONAL_JUMP` [`00bf2f00`](#insn-00bf2f00) → [`00bf2f10`](#insn-00bf2f10)
  - `FALL_THROUGH` [`00bf2f00`](#insn-00bf2f00) → [`00bf2f04`](#insn-00bf2f04)
- ブロック [`00bf2f04`](#insn-00bf2f04) 範囲 `[['00bf2f04', '00bf2f0f']]`
  - `UNCONDITIONAL_JUMP` [`00bf2f0c`](#insn-00bf2f0c) → [`00bf2f14`](#insn-00bf2f14)
- ブロック [`00bf2f10`](#insn-00bf2f10) 範囲 `[['00bf2f10', '00bf2f13']]`
  - `FALL_THROUGH` [`00bf2f10`](#insn-00bf2f10) → [`00bf2f14`](#insn-00bf2f14)
- ブロック [`00bf2f14`](#insn-00bf2f14) 範囲 `[['00bf2f14', '00bf2f17']]`
  - `FALL_THROUGH` [`00bf2f14`](#insn-00bf2f14) → [`00bf2f18`](#insn-00bf2f18)
- ブロック [`00bf2f18`](#insn-00bf2f18) 範囲 `[['00bf2f18', '00bf2f2f']]`
- ブロック [`00bf2f30`](#insn-00bf2f30) 範囲 `[['00bf2f30', '00bf2f33']]`

## 命令位置別の参照

- [`00bf2de0`](#insn-00bf2de0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2de4`](#insn-00bf2de4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2de8`](#insn-00bf2de8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2dec`](#insn-00bf2dec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e0c`](#insn-00bf2e0c) → [`00bf2f30`](#insn-00bf2f30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e14`](#insn-00bf2e14) → [`00bf2f18`](#insn-00bf2f18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e40`](#insn-00bf2e40) → [`00bf2e74`](#insn-00bf2e74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e60`](#insn-00bf2e60) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e70`](#insn-00bf2e70) → [`00bf2ea8`](#insn-00bf2ea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e88`](#insn-00bf2e88) → [`00bf2ea8`](#insn-00bf2ea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2ea0`](#insn-00bf2ea0) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`00bf2eb8`](#insn-00bf2eb8) → [`00bf2eec`](#insn-00bf2eec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2ee0`](#insn-00bf2ee0) → [`00bf2ed4`](#insn-00bf2ed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2ee8`](#insn-00bf2ee8) → [`00bf2ef8`](#insn-00bf2ef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2ef4`](#insn-00bf2ef4) → [`00bf2eec`](#insn-00bf2eec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2f00`](#insn-00bf2f00) → [`00bf2f10`](#insn-00bf2f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2f0c`](#insn-00bf2f0c) → [`00bf2f14`](#insn-00bf2f14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2f18`](#insn-00bf2f18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2f1c`](#insn-00bf2f1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2f20`](#insn-00bf2f20) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2f24`](#insn-00bf2f24) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2f30`](#insn-00bf2f30) → [`00bf28d8`](00bf28d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf28d8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf2de0`](#insn-00bf2de0)

~~~json
{
  "source": "00bf2de0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2de4`](#insn-00bf2de4)

~~~json
{
  "source": "00bf2de4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2de8`](#insn-00bf2de8)

~~~json
{
  "source": "00bf2de8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2dec`](#insn-00bf2dec)

~~~json
{
  "source": "00bf2dec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e0c`](#insn-00bf2e0c)

~~~json
{
  "source": "00bf2e0c",
  "target": "00bf2f30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e14`](#insn-00bf2e14)

~~~json
{
  "source": "00bf2e14",
  "target": "00bf2f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e40`](#insn-00bf2e40)

~~~json
{
  "source": "00bf2e40",
  "target": "00bf2e74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e60`](#insn-00bf2e60)

~~~json
{
  "source": "00bf2e60",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf2e70`](#insn-00bf2e70)

~~~json
{
  "source": "00bf2e70",
  "target": "00bf2ea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e88`](#insn-00bf2e88)

~~~json
{
  "source": "00bf2e88",
  "target": "00bf2ea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2ea0`](#insn-00bf2ea0)

~~~json
{
  "source": "00bf2ea0",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf2eb8`](#insn-00bf2eb8)

~~~json
{
  "source": "00bf2eb8",
  "target": "00bf2eec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2ee0`](#insn-00bf2ee0)

~~~json
{
  "source": "00bf2ee0",
  "target": "00bf2ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2ee8`](#insn-00bf2ee8)

~~~json
{
  "source": "00bf2ee8",
  "target": "00bf2ef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2ef4`](#insn-00bf2ef4)

~~~json
{
  "source": "00bf2ef4",
  "target": "00bf2eec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2f00`](#insn-00bf2f00)

~~~json
{
  "source": "00bf2f00",
  "target": "00bf2f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2f0c`](#insn-00bf2f0c)

~~~json
{
  "source": "00bf2f0c",
  "target": "00bf2f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2f18`](#insn-00bf2f18)

~~~json
{
  "source": "00bf2f18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2f1c`](#insn-00bf2f1c)

~~~json
{
  "source": "00bf2f1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2f20`](#insn-00bf2f20)

~~~json
{
  "source": "00bf2f20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2f24`](#insn-00bf2f24)

~~~json
{
  "source": "00bf2f24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2f30`](#insn-00bf2f30)

~~~json
{
  "source": "00bf2f30",
  "target": "00bf28d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
