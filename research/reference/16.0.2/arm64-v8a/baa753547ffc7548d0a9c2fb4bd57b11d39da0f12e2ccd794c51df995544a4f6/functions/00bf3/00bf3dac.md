# 00bf3dac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf3d10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3d10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-2b677be4b990d765d7980068f5cbe919)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf4da0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4da0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-0eb224c774bbc9175ab57c7c06355e18)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf3dac",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "11730acc14636afabbcf386d14aa0081dad217902ba7a7c660816b7c85cfd5e6",
  "source_text_sha256": "11730acc14636afabbcf386d14aa0081dad217902ba7a7c660816b7c85cfd5e6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf3dac",
        "00bf3ed3"
      ]
    ],
    "bytes_sha256": "c88079cf58311dbbea6c81d64cddcaef2c2e78ed90cbdd485301a3d9f02228b9",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a970](../00c5a/00c5a970.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1770 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw
               (ulong *param_1,ulong param_2,undefined4 param_3)

{
  ulong uVar1;
  long lVar2;
  ulong uVar3;
  uint uVar4;
  undefined4 *puVar5;
  ulong uVar6;
  ulong uVar7;
  undefined8 *puVar8;
  ulong uVar9;
  
  if (param_2 == 0) {
    return;
  }
  uVar3 = *param_1;
  lVar2 = 4;
  if ((*param_1 & 1) != 0) {
    lVar2 = (uVar3 & 0xfffffffffffffffe) - 1;
  }
  uVar4 = (uint)uVar3;
  uVar1 = uVar3 >> 1 & 0x7f;
  if ((uVar3 & 1) != 0) {
    uVar1 = param_1[1];
  }
  if (lVar2 - uVar1 < param_2) {
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm
              (param_1,lVar2,(param_2 - lVar2) + uVar1,uVar1,uVar1,0,0);
    param_1[1] = uVar1;
    uVar4 = (uint)(byte)*param_1;
  }
  uVar3 = (long)param_1 + 4;
  if ((uVar4 & 1) != 0) {
    uVar3 = param_1[2];
  }
  puVar5 = (undefined4 *)(uVar3 + uVar1 * 4);
  uVar6 = param_2;
  if (7 < param_2) {
    uVar7 = param_2 & 0xfffffffffffffff8;
    uVar6 = param_2 & 7;
    puVar8 = (undefined8 *)(puVar5 + 4);
    uVar9 = uVar7;
    do {
      uVar9 = uVar9 - 8;
      puVar8[-1] = CONCAT44(param_3,param_3);
      puVar8[-2] = CONCAT44(param_3,param_3);
      puVar8[1] = CONCAT44(param_3,param_3);
      *puVar8 = CONCAT44(param_3,param_3);
      puVar8 = puVar8 + 4;
    } while (uVar9 != 0);
    puVar5 = puVar5 + uVar7;
    if (uVar7 == param_2) goto LAB_00bf3ea0;
  }
  do {
    uVar6 = uVar6 - 1;
    *puVar5 = param_3;
    puVar5 = puVar5 + 1;
  } while (uVar6 != 0);
LAB_00bf3ea0:
  uVar1 = uVar1 + param_2;
  if ((*param_1 & 1) == 0) {
    *(char *)param_1 = (char)((int)uVar1 << 1);
  }
  else {
    param_1[1] = uVar1;
  }
  *(undefined4 *)(uVar3 + uVar1 * 4) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf3dac"></a> `00bf3dac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bf3db0"></a> `00bf3db0` | `01 09 00 b4` | cbz x1,0x00bf3ed0 | `CONDITIONAL_JUMP`
<a id="insn-00bf3db4"></a> `00bf3db4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf3db8"></a> `00bf3db8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bf3dbc"></a> `00bf3dbc` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3dc0"></a> `00bf3dc0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf3dc4"></a> `00bf3dc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf3dc8"></a> `00bf3dc8` | `09 28 40 a9` | ldp x9,x10,[x0] | `FALL_THROUGH`
<a id="insn-00bf3dcc"></a> `00bf3dcc` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bf3dd0"></a> `00bf3dd0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf3dd4"></a> `00bf3dd4` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bf3dd8"></a> `00bf3dd8` | `2b f9 7f 92` | and x11,x9,#-0x2 | `FALL_THROUGH`
<a id="insn-00bf3ddc"></a> `00bf3ddc` | `2c 1d 41 d3` | ubfx x12,x9,#0x1,#0x7 | `FALL_THROUGH`
<a id="insn-00bf3de0"></a> `00bf3de0` | `6b 05 00 d1` | sub x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bf3de4"></a> `00bf3de4` | `08 01 8b 9a` | csel x8,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00bf3de8"></a> `00bf3de8` | `29 01 00 72` | ands w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf3dec"></a> `00bf3dec` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bf3df0"></a> `00bf3df0` | `0a 01 13 cb` | sub x10,x8,x19 | `FALL_THROUGH`
<a id="insn-00bf3df4"></a> `00bf3df4` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-00bf3df8"></a> `00bf3df8` | `42 02 00 54` | b.cs 0x00bf3e40 | `CONDITIONAL_JUMP`
<a id="insn-00bf3dfc"></a> `00bf3dfc` | `29 00 08 cb` | sub x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00bf3e00"></a> `00bf3e00` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bf3e04"></a> `00bf3e04` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bf3e08"></a> `00bf3e08` | `22 01 13 8b` | add x2,x9,x19 | `FALL_THROUGH`
<a id="insn-00bf3e0c"></a> `00bf3e0c` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bf3e10"></a> `00bf3e10` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bf3e14"></a> `00bf3e14` | `e4 03 13 aa` | mov x4,x19 | `FALL_THROUGH`
<a id="insn-00bf3e18"></a> `00bf3e18` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00bf3e1c"></a> `00bf3e1c` | `e6 03 1f aa` | mov x6,xzr | `FALL_THROUGH`
<a id="insn-00bf3e20"></a> `00bf3e20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bf3e24"></a> `00bf3e24` | `d3 9a 01 94` | bl 0x00c5a970 | `UNCONDITIONAL_CALL`
<a id="insn-00bf3e28"></a> `00bf3e28` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00bf3e2c"></a> `00bf3e2c` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bf3e30"></a> `00bf3e30` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bf3e34"></a> `00bf3e34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf3e38"></a> `00bf3e38` | `93 06 00 f9` | str x19,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bf3e3c"></a> `00bf3e3c` | `09 01 00 12` | and w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf3e40"></a> `00bf3e40` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3e44"></a> `00bf3e44` | `0a 10 00 91` | add x10,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bf3e48"></a> `00bf3e48` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00bf3e4c"></a> `00bf3e4c` | `48 01 88 9a` | csel x8,x10,x8,eq | `FALL_THROUGH`
<a id="insn-00bf3e50"></a> `00bf3e50` | `3f 20 00 f1` | cmp x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bf3e54"></a> `00bf3e54` | `ea 03 01 aa` | mov x10,x1 | `FALL_THROUGH`
<a id="insn-00bf3e58"></a> `00bf3e58` | `0c 09 13 8b` | add x12,x8,x19, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf3e5c"></a> `00bf3e5c` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bf3e60"></a> `00bf3e60` | `a3 01 00 54` | b.cc 0x00bf3e94 | `CONDITIONAL_JUMP`
<a id="insn-00bf3e64"></a> `00bf3e64` | `2b f0 7d 92` | and x11,x1,#-0x8 | `FALL_THROUGH`
<a id="insn-00bf3e68"></a> `00bf3e68` | `40 0c 04 4e` | dup v0.4S,w2 | `FALL_THROUGH`
<a id="insn-00bf3e6c"></a> `00bf3e6c` | `2a 08 40 92` | and x10,x1,#0x7 | `FALL_THROUGH`
<a id="insn-00bf3e70"></a> `00bf3e70` | `89 09 0b 8b` | add x9,x12,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf3e74"></a> `00bf3e74` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00bf3e78"></a> `00bf3e78` | `ed 03 0b aa` | mov x13,x11 | `FALL_THROUGH`
<a id="insn-00bf3e7c"></a> `00bf3e7c` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00bf3e80"></a> `00bf3e80` | `80 81 3f ad` | stp q0,q0,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf3e84"></a> `00bf3e84` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00bf3e88"></a> `00bf3e88` | `a1 ff ff 54` | b.ne 0x00bf3e7c | `CONDITIONAL_JUMP`
<a id="insn-00bf3e8c"></a> `00bf3e8c` | `7f 01 01 eb` | cmp x11,x1 | `FALL_THROUGH`
<a id="insn-00bf3e90"></a> `00bf3e90` | `80 00 00 54` | b.eq 0x00bf3ea0 | `CONDITIONAL_JUMP`
<a id="insn-00bf3e94"></a> `00bf3e94` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bf3e98"></a> `00bf3e98` | `22 45 00 b8` | str w2,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00bf3e9c"></a> `00bf3e9c` | `c1 ff ff 54` | b.ne 0x00bf3e94 | `CONDITIONAL_JUMP`
<a id="insn-00bf3ea0"></a> `00bf3ea0` | `0a 00 40 39` | ldrb w10,[x0] | `FALL_THROUGH`
<a id="insn-00bf3ea4"></a> `00bf3ea4` | `69 02 01 8b` | add x9,x19,x1 | `FALL_THROUGH`
<a id="insn-00bf3ea8"></a> `00bf3ea8` | `8a 00 00 37` | tbnz w10,#0x0,0x00bf3eb8 | `CONDITIONAL_JUMP`
<a id="insn-00bf3eac"></a> `00bf3eac` | `2a 79 1f 53` | lsl w10,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf3eb0"></a> `00bf3eb0` | `0a 00 00 39` | strb w10,[x0] | `FALL_THROUGH`
<a id="insn-00bf3eb4"></a> `00bf3eb4` | `02 00 00 14` | b 0x00bf3ebc | `UNCONDITIONAL_JUMP`
<a id="insn-00bf3eb8"></a> `00bf3eb8` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bf3ebc"></a> `00bf3ebc` | `1f 79 29 b8` | str wzr,[x8, x9, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00bf3ec0"></a> `00bf3ec0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf3ec4"></a> `00bf3ec4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3ec8"></a> `00bf3ec8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bf3ecc"></a> `00bf3ecc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf3ed0"></a> `00bf3ed0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf3dac`](#insn-00bf3dac) 範囲 `[['00bf3dac', '00bf3db3']]`
  - `CONDITIONAL_JUMP` [`00bf3db0`](#insn-00bf3db0) → [`00bf3ed0`](#insn-00bf3ed0)
  - `FALL_THROUGH` [`00bf3db0`](#insn-00bf3db0) → [`00bf3db4`](#insn-00bf3db4)
- ブロック [`00bf3db4`](#insn-00bf3db4) 範囲 `[['00bf3db4', '00bf3dfb']]`
  - `CONDITIONAL_JUMP` [`00bf3df8`](#insn-00bf3df8) → [`00bf3e40`](#insn-00bf3e40)
  - `FALL_THROUGH` [`00bf3df8`](#insn-00bf3df8) → [`00bf3dfc`](#insn-00bf3dfc)
- ブロック [`00bf3dfc`](#insn-00bf3dfc) 範囲 `[['00bf3dfc', '00bf3e3f']]`
  - `FALL_THROUGH` [`00bf3e3c`](#insn-00bf3e3c) → [`00bf3e40`](#insn-00bf3e40)
- ブロック [`00bf3e40`](#insn-00bf3e40) 範囲 `[['00bf3e40', '00bf3e63']]`
  - `CONDITIONAL_JUMP` [`00bf3e60`](#insn-00bf3e60) → [`00bf3e94`](#insn-00bf3e94)
  - `FALL_THROUGH` [`00bf3e60`](#insn-00bf3e60) → [`00bf3e64`](#insn-00bf3e64)
- ブロック [`00bf3e64`](#insn-00bf3e64) 範囲 `[['00bf3e64', '00bf3e7b']]`
  - `FALL_THROUGH` [`00bf3e78`](#insn-00bf3e78) → [`00bf3e7c`](#insn-00bf3e7c)
- ブロック [`00bf3e7c`](#insn-00bf3e7c) 範囲 `[['00bf3e7c', '00bf3e8b']]`
  - `CONDITIONAL_JUMP` [`00bf3e88`](#insn-00bf3e88) → [`00bf3e7c`](#insn-00bf3e7c)
  - `FALL_THROUGH` [`00bf3e88`](#insn-00bf3e88) → [`00bf3e8c`](#insn-00bf3e8c)
- ブロック [`00bf3e8c`](#insn-00bf3e8c) 範囲 `[['00bf3e8c', '00bf3e93']]`
  - `CONDITIONAL_JUMP` [`00bf3e90`](#insn-00bf3e90) → [`00bf3ea0`](#insn-00bf3ea0)
  - `FALL_THROUGH` [`00bf3e90`](#insn-00bf3e90) → [`00bf3e94`](#insn-00bf3e94)
- ブロック [`00bf3e94`](#insn-00bf3e94) 範囲 `[['00bf3e94', '00bf3e9f']]`
  - `CONDITIONAL_JUMP` [`00bf3e9c`](#insn-00bf3e9c) → [`00bf3e94`](#insn-00bf3e94)
  - `FALL_THROUGH` [`00bf3e9c`](#insn-00bf3e9c) → [`00bf3ea0`](#insn-00bf3ea0)
- ブロック [`00bf3ea0`](#insn-00bf3ea0) 範囲 `[['00bf3ea0', '00bf3eab']]`
  - `CONDITIONAL_JUMP` [`00bf3ea8`](#insn-00bf3ea8) → [`00bf3eb8`](#insn-00bf3eb8)
  - `FALL_THROUGH` [`00bf3ea8`](#insn-00bf3ea8) → [`00bf3eac`](#insn-00bf3eac)
- ブロック [`00bf3eac`](#insn-00bf3eac) 範囲 `[['00bf3eac', '00bf3eb7']]`
  - `UNCONDITIONAL_JUMP` [`00bf3eb4`](#insn-00bf3eb4) → [`00bf3ebc`](#insn-00bf3ebc)
- ブロック [`00bf3eb8`](#insn-00bf3eb8) 範囲 `[['00bf3eb8', '00bf3ebb']]`
  - `FALL_THROUGH` [`00bf3eb8`](#insn-00bf3eb8) → [`00bf3ebc`](#insn-00bf3ebc)
- ブロック [`00bf3ebc`](#insn-00bf3ebc) 範囲 `[['00bf3ebc', '00bf3ecf']]`
  - `FALL_THROUGH` [`00bf3ecc`](#insn-00bf3ecc) → [`00bf3ed0`](#insn-00bf3ed0)
- ブロック [`00bf3ed0`](#insn-00bf3ed0) 範囲 `[['00bf3ed0', '00bf3ed3']]`

## 命令位置別の参照

- [`00bf3db0`](#insn-00bf3db0) → [`00bf3ed0`](#insn-00bf3ed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3db8`](#insn-00bf3db8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3dbc`](#insn-00bf3dbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3dc0`](#insn-00bf3dc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3df8`](#insn-00bf3df8) → [`00bf3e40`](#insn-00bf3e40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3e24`](#insn-00bf3e24) → [`00c5a970`](../00c5a/00c5a970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a970` · 推定シンボル `None` · 推定型 `None`
- [`00bf3e60`](#insn-00bf3e60) → [`00bf3e94`](#insn-00bf3e94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3e88`](#insn-00bf3e88) → [`00bf3e7c`](#insn-00bf3e7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3e90`](#insn-00bf3e90) → [`00bf3ea0`](#insn-00bf3ea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3e9c`](#insn-00bf3e9c) → [`00bf3e94`](#insn-00bf3e94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ea8`](#insn-00bf3ea8) → [`00bf3eb8`](#insn-00bf3eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3eb4`](#insn-00bf3eb4) → [`00bf3ebc`](#insn-00bf3ebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ec0`](#insn-00bf3ec0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ec4`](#insn-00bf3ec4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ec8`](#insn-00bf3ec8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf3db0`](#insn-00bf3db0)

~~~json
{
  "source": "00bf3db0",
  "target": "00bf3ed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3db8`](#insn-00bf3db8)

~~~json
{
  "source": "00bf3db8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3dbc`](#insn-00bf3dbc)

~~~json
{
  "source": "00bf3dbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3dc0`](#insn-00bf3dc0)

~~~json
{
  "source": "00bf3dc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3df8`](#insn-00bf3df8)

~~~json
{
  "source": "00bf3df8",
  "target": "00bf3e40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3e24`](#insn-00bf3e24)

~~~json
{
  "source": "00bf3e24",
  "target": "00c5a970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf3e60`](#insn-00bf3e60)

~~~json
{
  "source": "00bf3e60",
  "target": "00bf3e94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3e88`](#insn-00bf3e88)

~~~json
{
  "source": "00bf3e88",
  "target": "00bf3e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3e90`](#insn-00bf3e90)

~~~json
{
  "source": "00bf3e90",
  "target": "00bf3ea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3e9c`](#insn-00bf3e9c)

~~~json
{
  "source": "00bf3e9c",
  "target": "00bf3e94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3ea8`](#insn-00bf3ea8)

~~~json
{
  "source": "00bf3ea8",
  "target": "00bf3eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3eb4`](#insn-00bf3eb4)

~~~json
{
  "source": "00bf3eb4",
  "target": "00bf3ebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3ec0`](#insn-00bf3ec0)

~~~json
{
  "source": "00bf3ec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3ec4`](#insn-00bf3ec4)

~~~json
{
  "source": "00bf3ec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3ec8`](#insn-00bf3ec8)

~~~json
{
  "source": "00bf3ec8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
