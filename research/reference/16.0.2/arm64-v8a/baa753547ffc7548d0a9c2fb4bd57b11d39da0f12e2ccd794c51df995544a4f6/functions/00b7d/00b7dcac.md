# 00b7dcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b7dc10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dc10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-ae289cbdcc937823ffa19f50b78a1ffa)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b7eca0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eca0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0033.md#compare-4b6f2e996c5404f6b42d10004e37fb92)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7dcac",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81f44ac56998c5297aaea3df53421b1da72a53fcdf0fcd45d5a454c71044343b",
  "source_text_sha256": "81f44ac56998c5297aaea3df53421b1da72a53fcdf0fcd45d5a454c71044343b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7dcac",
        "00b7ddbf"
      ]
    ],
    "bytes_sha256": "9e37b1fc0e84c29e70c3bb0b25a7b6acb34f4c402140e784150c889c2dacf745",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c2d0](../00c5c/00c5c2d0.md)

## 呼び出し先

- [00c5c270](../00c5c/00c5c270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1741 bytes

~~~c

void _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_
               (long param_1,uint param_2,undefined2 param_3)

{
  int iVar1;
  uint uVar2;
  ulong *puVar3;
  long lVar4;
  ulong uVar5;
  
  if (*(ulong *)(param_1 + 0x68) < 2) {
    *(undefined8 *)(param_1 + 0x68) = 2;
  }
  uVar2 = *(uint *)(param_1 + 0x30);
  uVar5 = (ulong)uVar2 & 1;
  if ((int)uVar5 != 0) {
    lVar4 = *(long *)(param_1 + 0x40);
    if ((uint)((int)lVar4 - *(int *)(param_1 + 0x48)) < uVar5) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar5);
      lVar4 = *(long *)(param_1 + 0x40);
      uVar2 = *(uint *)(param_1 + 0x30);
    }
    *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar4 - uVar5);
    *(uint *)(param_1 + 0x30) = uVar2 + (int)uVar5;
    *(undefined1 *)(lVar4 - uVar5) = 0;
  }
  lVar4 = *(long *)(param_1 + 0x40);
  puVar3 = *(ulong **)(param_1 + 0x48);
  if (((int)lVar4 - (int)puVar3 & 0xfffffffeU) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,2);
    lVar4 = *(long *)(param_1 + 0x40);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *(long *)(param_1 + 0x40) = lVar4 + -2;
  iVar1 = *(int *)(param_1 + 0x30) + 2;
  *(int *)(param_1 + 0x30) = iVar1;
  *(undefined2 *)(lVar4 + -2) = param_3;
  if (((int)(lVar4 + -2) - (int)puVar3 & 0xfffffff8U) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,8);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *puVar3 = CONCAT44(param_2,iVar1) & 0xffffffffffff;
  *(long *)(param_1 + 0x48) = *(long *)(param_1 + 0x48) + 8;
  *(int *)(param_1 + 0x50) = *(int *)(param_1 + 0x50) + 1;
  if ((uint)*(ushort *)(param_1 + 0x54) < (param_2 & 0xffff)) {
    *(short *)(param_1 + 0x54) = (short)param_2;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7dcac"></a> `00b7dcac` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b7dcb0"></a> `00b7dcb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7dcb4"></a> `00b7dcb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7dcb8"></a> `00b7dcb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b7dcbc"></a> `00b7dcbc` | `08 34 40 f9` | ldr x8,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00b7dcc0"></a> `00b7dcc0` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00b7dcc4"></a> `00b7dcc4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b7dcc8"></a> `00b7dcc8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00b7dccc"></a> `00b7dccc` | `1f 05 00 f1` | cmp x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7dcd0"></a> `00b7dcd0` | `68 00 00 54` | b.hi 0x00b7dcdc | `CONDITIONAL_JUMP`
<a id="insn-00b7dcd4"></a> `00b7dcd4` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00b7dcd8"></a> `00b7dcd8` | `68 36 00 f9` | str x8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b7dcdc"></a> `00b7dcdc` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7dce0"></a> `00b7dce0` | `16 01 40 92` | and x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7dce4"></a> `00b7dce4` | `16 02 00 34` | cbz w22,0x00b7dd24 | `CONDITIONAL_JUMP`
<a id="insn-00b7dce8"></a> `00b7dce8` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7dcec"></a> `00b7dcec` | `6a 4a 40 b9` | ldr w10,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7dcf0"></a> `00b7dcf0` | `2a 01 0a 4b` | sub w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00b7dcf4"></a> `00b7dcf4` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00b7dcf8"></a> `00b7dcf8` | `c2 00 00 54` | b.cs 0x00b7dd10 | `CONDITIONAL_JUMP`
<a id="insn-00b7dcfc"></a> `00b7dcfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7dd00"></a> `00b7dd00` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b7dd04"></a> `00b7dd04` | `5b 79 03 94` | bl 0x00c5c270 | `UNCONDITIONAL_CALL`
<a id="insn-00b7dd08"></a> `00b7dd08` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7dd0c"></a> `00b7dd0c` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7dd10"></a> `00b7dd10` | `29 01 16 cb` | sub x9,x9,x22 | `FALL_THROUGH`
<a id="insn-00b7dd14"></a> `00b7dd14` | `08 01 16 0b` | add w8,w8,w22 | `FALL_THROUGH`
<a id="insn-00b7dd18"></a> `00b7dd18` | `69 22 00 f9` | str x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7dd1c"></a> `00b7dd1c` | `68 32 00 b9` | str w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7dd20"></a> `00b7dd20` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00b7dd24"></a> `00b7dd24` | `69 22 44 a9` | ldp x9,x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7dd28"></a> `00b7dd28` | `2a 01 08 4b` | sub w10,w9,w8 | `FALL_THROUGH`
<a id="insn-00b7dd2c"></a> `00b7dd2c` | `5f 79 7f f2` | tst x10,#0xfffffffe | `FALL_THROUGH`
<a id="insn-00b7dd30"></a> `00b7dd30` | `a1 00 00 54` | b.ne 0x00b7dd44 | `CONDITIONAL_JUMP`
<a id="insn-00b7dd34"></a> `00b7dd34` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00b7dd38"></a> `00b7dd38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7dd3c"></a> `00b7dd3c` | `4d 79 03 94` | bl 0x00c5c270 | `UNCONDITIONAL_CALL`
<a id="insn-00b7dd40"></a> `00b7dd40` | `69 22 44 a9` | ldp x9,x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7dd44"></a> `00b7dd44` | `6b 32 40 b9` | ldr w11,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7dd48"></a> `00b7dd48` | `2a 09 00 d1` | sub x10,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00b7dd4c"></a> `00b7dd4c` | `6a 22 00 f9` | str x10,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7dd50"></a> `00b7dd50` | `4a 01 08 4b` | sub w10,w10,w8 | `FALL_THROUGH`
<a id="insn-00b7dd54"></a> `00b7dd54` | `5f 71 7d f2` | tst x10,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00b7dd58"></a> `00b7dd58` | `76 09 00 11` | add w22,w11,#0x2 | `FALL_THROUGH`
<a id="insn-00b7dd5c"></a> `00b7dd5c` | `76 32 00 b9` | str w22,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7dd60"></a> `00b7dd60` | `35 e1 1f 78` | sturh w21,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-00b7dd64"></a> `00b7dd64` | `a1 00 00 54` | b.ne 0x00b7dd78 | `CONDITIONAL_JUMP`
<a id="insn-00b7dd68"></a> `00b7dd68` | `01 01 80 52` | mov w1,#0x8 | `FALL_THROUGH`
<a id="insn-00b7dd6c"></a> `00b7dd6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7dd70"></a> `00b7dd70` | `40 79 03 94` | bl 0x00c5c270 | `UNCONDITIONAL_CALL`
<a id="insn-00b7dd74"></a> `00b7dd74` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7dd78"></a> `00b7dd78` | `89 3e 00 12` | and w9,w20,#0xffff | `FALL_THROUGH`
<a id="insn-00b7dd7c"></a> `00b7dd7c` | `ea 03 16 2a` | mov w10,w22 | `FALL_THROUGH`
<a id="insn-00b7dd80"></a> `00b7dd80` | `2a 3d 60 b3` | bfm x10,x9,#0x20,#0xf | `FALL_THROUGH`
<a id="insn-00b7dd84"></a> `00b7dd84` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00b7dd88"></a> `00b7dd88` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7dd8c"></a> `00b7dd8c` | `6a 52 40 b9` | ldr w10,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00b7dd90"></a> `00b7dd90` | `6b aa 40 79` | ldrh w11,[x19, #0x54] | `FALL_THROUGH`
<a id="insn-00b7dd94"></a> `00b7dd94` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00b7dd98"></a> `00b7dd98` | `4a 05 00 11` | add w10,w10,#0x1 | `FALL_THROUGH`
<a id="insn-00b7dd9c"></a> `00b7dd9c` | `7f 01 09 6b` | cmp w11,w9 | `FALL_THROUGH`
<a id="insn-00b7dda0"></a> `00b7dda0` | `68 26 00 f9` | str x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7dda4"></a> `00b7dda4` | `6a 52 00 b9` | str w10,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00b7dda8"></a> `00b7dda8` | `42 00 00 54` | b.cs 0x00b7ddb0 | `CONDITIONAL_JUMP`
<a id="insn-00b7ddac"></a> `00b7ddac` | `74 aa 00 79` | strh w20,[x19, #0x54] | `FALL_THROUGH`
<a id="insn-00b7ddb0"></a> `00b7ddb0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7ddb4"></a> `00b7ddb4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7ddb8"></a> `00b7ddb8` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b7ddbc"></a> `00b7ddbc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7dcac`](#insn-00b7dcac) 範囲 `[['00b7dcac', '00b7dcd3']]`
  - `CONDITIONAL_JUMP` [`00b7dcd0`](#insn-00b7dcd0) → [`00b7dcdc`](#insn-00b7dcdc)
  - `FALL_THROUGH` [`00b7dcd0`](#insn-00b7dcd0) → [`00b7dcd4`](#insn-00b7dcd4)
- ブロック [`00b7dcd4`](#insn-00b7dcd4) 範囲 `[['00b7dcd4', '00b7dcdb']]`
  - `FALL_THROUGH` [`00b7dcd8`](#insn-00b7dcd8) → [`00b7dcdc`](#insn-00b7dcdc)
- ブロック [`00b7dcdc`](#insn-00b7dcdc) 範囲 `[['00b7dcdc', '00b7dce7']]`
  - `CONDITIONAL_JUMP` [`00b7dce4`](#insn-00b7dce4) → [`00b7dd24`](#insn-00b7dd24)
  - `FALL_THROUGH` [`00b7dce4`](#insn-00b7dce4) → [`00b7dce8`](#insn-00b7dce8)
- ブロック [`00b7dce8`](#insn-00b7dce8) 範囲 `[['00b7dce8', '00b7dcfb']]`
  - `CONDITIONAL_JUMP` [`00b7dcf8`](#insn-00b7dcf8) → [`00b7dd10`](#insn-00b7dd10)
  - `FALL_THROUGH` [`00b7dcf8`](#insn-00b7dcf8) → [`00b7dcfc`](#insn-00b7dcfc)
- ブロック [`00b7dcfc`](#insn-00b7dcfc) 範囲 `[['00b7dcfc', '00b7dd0f']]`
  - `FALL_THROUGH` [`00b7dd0c`](#insn-00b7dd0c) → [`00b7dd10`](#insn-00b7dd10)
- ブロック [`00b7dd10`](#insn-00b7dd10) 範囲 `[['00b7dd10', '00b7dd23']]`
  - `FALL_THROUGH` [`00b7dd20`](#insn-00b7dd20) → [`00b7dd24`](#insn-00b7dd24)
- ブロック [`00b7dd24`](#insn-00b7dd24) 範囲 `[['00b7dd24', '00b7dd33']]`
  - `CONDITIONAL_JUMP` [`00b7dd30`](#insn-00b7dd30) → [`00b7dd44`](#insn-00b7dd44)
  - `FALL_THROUGH` [`00b7dd30`](#insn-00b7dd30) → [`00b7dd34`](#insn-00b7dd34)
- ブロック [`00b7dd34`](#insn-00b7dd34) 範囲 `[['00b7dd34', '00b7dd43']]`
  - `FALL_THROUGH` [`00b7dd40`](#insn-00b7dd40) → [`00b7dd44`](#insn-00b7dd44)
- ブロック [`00b7dd44`](#insn-00b7dd44) 範囲 `[['00b7dd44', '00b7dd67']]`
  - `CONDITIONAL_JUMP` [`00b7dd64`](#insn-00b7dd64) → [`00b7dd78`](#insn-00b7dd78)
  - `FALL_THROUGH` [`00b7dd64`](#insn-00b7dd64) → [`00b7dd68`](#insn-00b7dd68)
- ブロック [`00b7dd68`](#insn-00b7dd68) 範囲 `[['00b7dd68', '00b7dd77']]`
  - `FALL_THROUGH` [`00b7dd74`](#insn-00b7dd74) → [`00b7dd78`](#insn-00b7dd78)
- ブロック [`00b7dd78`](#insn-00b7dd78) 範囲 `[['00b7dd78', '00b7ddab']]`
  - `CONDITIONAL_JUMP` [`00b7dda8`](#insn-00b7dda8) → [`00b7ddb0`](#insn-00b7ddb0)
  - `FALL_THROUGH` [`00b7dda8`](#insn-00b7dda8) → [`00b7ddac`](#insn-00b7ddac)
- ブロック [`00b7ddac`](#insn-00b7ddac) 範囲 `[['00b7ddac', '00b7ddaf']]`
  - `FALL_THROUGH` [`00b7ddac`](#insn-00b7ddac) → [`00b7ddb0`](#insn-00b7ddb0)
- ブロック [`00b7ddb0`](#insn-00b7ddb0) 範囲 `[['00b7ddb0', '00b7ddbf']]`

## 命令位置別の参照

- [`00b7dcac`](#insn-00b7dcac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dcb0`](#insn-00b7dcb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dcb4`](#insn-00b7dcb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dcd0`](#insn-00b7dcd0) → [`00b7dcdc`](#insn-00b7dcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dce4`](#insn-00b7dce4) → [`00b7dd24`](#insn-00b7dd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dcf8`](#insn-00b7dcf8) → [`00b7dd10`](#insn-00b7dd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dd04`](#insn-00b7dd04) → [`00c5c270`](../00c5c/00c5c270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c270` · 推定シンボル `None` · 推定型 `None`
- [`00b7dd30`](#insn-00b7dd30) → [`00b7dd44`](#insn-00b7dd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dd3c`](#insn-00b7dd3c) → [`00c5c270`](../00c5c/00c5c270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c270` · 推定シンボル `None` · 推定型 `None`
- [`00b7dd64`](#insn-00b7dd64) → [`00b7dd78`](#insn-00b7dd78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dd70`](#insn-00b7dd70) → [`00c5c270`](../00c5c/00c5c270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c270` · 推定シンボル `None` · 推定型 `None`
- [`00b7dda8`](#insn-00b7dda8) → [`00b7ddb0`](#insn-00b7ddb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ddb0`](#insn-00b7ddb0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ddb4`](#insn-00b7ddb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7dcac`](#insn-00b7dcac)

~~~json
{
  "source": "00b7dcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dcb0`](#insn-00b7dcb0)

~~~json
{
  "source": "00b7dcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dcb4`](#insn-00b7dcb4)

~~~json
{
  "source": "00b7dcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dcd0`](#insn-00b7dcd0)

~~~json
{
  "source": "00b7dcd0",
  "target": "00b7dcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dce4`](#insn-00b7dce4)

~~~json
{
  "source": "00b7dce4",
  "target": "00b7dd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dcf8`](#insn-00b7dcf8)

~~~json
{
  "source": "00b7dcf8",
  "target": "00b7dd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dd04`](#insn-00b7dd04)

~~~json
{
  "source": "00b7dd04",
  "target": "00c5c270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7dd30`](#insn-00b7dd30)

~~~json
{
  "source": "00b7dd30",
  "target": "00b7dd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dd3c`](#insn-00b7dd3c)

~~~json
{
  "source": "00b7dd3c",
  "target": "00c5c270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7dd64`](#insn-00b7dd64)

~~~json
{
  "source": "00b7dd64",
  "target": "00b7dd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dd70`](#insn-00b7dd70)

~~~json
{
  "source": "00b7dd70",
  "target": "00c5c270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7dda8`](#insn-00b7dda8)

~~~json
{
  "source": "00b7dda8",
  "target": "00b7ddb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ddb0`](#insn-00b7ddb0)

~~~json
{
  "source": "00b7ddb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ddb4`](#insn-00b7ddb4)

~~~json
{
  "source": "00b7ddb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
