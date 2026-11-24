# 00ac8ecc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ac8e5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8e5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0005.md#compare-49f41a06f9faa3f19b0bdec2d34253dc)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00ac9ec0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9ec0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-ed6afae7413f5c50b4838845d2dbeeeb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8ecc",
  "name": "FUN_00ac8ecc",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83026b603df259e896eab1b8f1abdf14fc30595c656444b6510032f78ab52cc3",
  "source_text_sha256": "83026b603df259e896eab1b8f1abdf14fc30595c656444b6510032f78ab52cc3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac8ecc",
        "00ac8fef"
      ]
    ],
    "bytes_sha256": "37d7c9c78252c34aaadb296b69ddc0ecf7f9cfa180480770945d31107a9173c8",
    "instruction_count": 73,
    "instruction_bytes": 292,
    "body_bytes": 292,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00657fcc](../00657/00657fcc.md)
- [0068aae0](../0068a/0068aae0.md)
- [006d3e94](../006d3/006d3e94.md)
- [007001b0](../00700/007001b0.md)
- [00769ddc](../00769/00769ddc.md)
- [00835794](../00835/00835794.md)
- [008c038c](../008c0/008c038c.md)
- [00a01544](../00a01/00a01544.md)

## 呼び出し先

- [00851550](../00851/00851550.md)
- [00859ba4](../00859/00859ba4.md)
- [0085b2fc](../0085b/0085b2fc.md)
- [0085b304](../0085b/0085b304.md)
- [0085b338](../0085b/0085b338.md)
- [00ac8ff0](../00ac8/00ac8ff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2005 bytes

~~~c

undefined8 FUN_00ac8ecc(long param_1)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  float fVar4;
  float fVar5;
  float fVar6;
  
  if (*(char *)(param_1 + 0x1d4) == '\0') {
    return 0;
  }
  FUN_00851550();
  uVar2 = FUN_00859ba4();
  if ((uVar2 & 1) == 0) {
    FUN_00851550();
    uVar2 = FUN_0085b338();
    if (((uVar2 & 1) == 0) && (lVar3 = FUN_00851550(), *(char *)(lVar3 + 0x3575) == '\0'))
    goto LAB_00ac8f8c;
  }
  FUN_00851550();
  uVar2 = FUN_0085b338();
  if ((uVar2 & 1) != 0) {
                    /* try { // try from 00ac8f20 to 00bc8f2b has its CatchHandler @ 00ac9384 */
    *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
    return 1;
  }
                    /* try { // try from 00ac8f3c to 00bc8f4b has its CatchHandler @ 00ac935c */
  uVar2 = FUN_00ac8ff0(param_1);
  if ((uVar2 & 1) != 0) {
    fVar4 = *(float *)(param_1 + 0x1d8);
                    /* try { // try from 00ac8f4c to 00bc8f5b has its CatchHandler @ 00ac9358 */
    iVar1 = *(int *)(param_1 + 0x284);
    fVar5 = (fVar4 * *(float *)(param_1 + 0x1e0)) / *(float *)(param_1 + 0x1dc);
    if (fVar5 <= 14.0) {
      fVar5 = 14.0;
    }
    FUN_00851550();
    if (iVar1 == 0) {
      iVar1 = FUN_0085b2fc();
      fVar6 = *(float *)(param_1 + 0x1e4);
    }
    else {
      iVar1 = FUN_0085b304();
      fVar6 = *(float *)(param_1 + 0x1e8);
                    /* try { // try from 00ac8f88 to 00bc8f9b has its CatchHandler @ 00ac9350 */
    }
                    /* try { // try from 00ac8fbc to 00bc8fcf has its CatchHandler @ 00ac9370 */
    fVar4 = (float)NEON_fminnm((((float)iVar1 - fVar6) + -fVar5 * 0.5) / (float)(int)(fVar4 - fVar5)
                               ,0x3f800000);
                    /* try { // try from 00ac8fd4 to 00bc900b has its CatchHandler @ 00ac9390 */
    if (fVar4 <= 0.0) {
      fVar4 = 0.0;
    }
    *(float *)(param_1 + 0x1f0) = fVar4;
    return 1;
  }
LAB_00ac8f8c:
  *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac8ecc"></a> `00ac8ecc` | `08 50 47 39` | ldrb w8,[x0, #0x1d4] | `FALL_THROUGH`
<a id="insn-00ac8ed0"></a> `00ac8ed0` | `08 03 00 34` | cbz w8,0x00ac8f30 | `CONDITIONAL_JUMP`
<a id="insn-00ac8ed4"></a> `00ac8ed4` | `e8 0f 1d fc` | str d8,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ac8ed8"></a> `00ac8ed8` | `fd fb 00 a9` | stp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac8edc"></a> `00ac8edc` | `f5 0f 00 f9` | str x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ac8ee0"></a> `00ac8ee0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac8ee4"></a> `00ac8ee4` | `fd 23 00 91` | add x29,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ac8ee8"></a> `00ac8ee8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac8eec"></a> `00ac8eec` | `99 21 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ef0"></a> `00ac8ef0` | `2d 43 f6 97` | bl 0x00859ba4 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8ef4"></a> `00ac8ef4` | `00 01 00 37` | tbnz w0,#0x0,0x00ac8f14 | `CONDITIONAL_JUMP`
<a id="insn-00ac8ef8"></a> `00ac8ef8` | `96 21 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8efc"></a> `00ac8efc` | `0f 49 f6 97` | bl 0x0085b338 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f00"></a> `00ac8f00` | `a0 00 00 37` | tbnz w0,#0x0,0x00ac8f14 | `CONDITIONAL_JUMP`
<a id="insn-00ac8f04"></a> `00ac8f04` | `93 21 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f08"></a> `00ac8f08` | `a8 ae 86 52` | mov w8,#0x3575 | `FALL_THROUGH`
<a id="insn-00ac8f0c"></a> `00ac8f0c` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac8f10"></a> `00ac8f10` | `e8 03 00 34` | cbz w8,0x00ac8f8c | `CONDITIONAL_JUMP`
<a id="insn-00ac8f14"></a> `00ac8f14` | `8f 21 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f18"></a> `00ac8f18` | `08 49 f6 97` | bl 0x0085b338 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f1c"></a> `00ac8f1c` | `e0 00 00 36` | tbz w0,#0x0,0x00ac8f38 | `CONDITIONAL_JUMP`
<a id="insn-00ac8f20"></a> `00ac8f20` | `60 f2 41 bd` | ldr s0,[x19, #0x1f0] | `FALL_THROUGH`
<a id="insn-00ac8f24"></a> `00ac8f24` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8f28"></a> `00ac8f28` | `60 f6 01 bd` | str s0,[x19, #0x1f4] | `FALL_THROUGH`
<a id="insn-00ac8f2c"></a> `00ac8f2c` | `2c 00 00 14` | b 0x00ac8fdc | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8f30"></a> `00ac8f30` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ac8f34"></a> `00ac8f34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac8f38"></a> `00ac8f38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac8f3c"></a> `00ac8f3c` | `2d 00 00 94` | bl 0x00ac8ff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f40"></a> `00ac8f40` | `60 02 00 36` | tbz w0,#0x0,0x00ac8f8c | `CONDITIONAL_JUMP`
<a id="insn-00ac8f44"></a> `00ac8f44` | `60 da 41 bd` | ldr s0,[x19, #0x1d8] | `FALL_THROUGH`
<a id="insn-00ac8f48"></a> `00ac8f48` | `61 e2 41 bd` | ldr s1,[x19, #0x1e0] | `FALL_THROUGH`
<a id="insn-00ac8f4c"></a> `00ac8f4c` | `62 de 41 bd` | ldr s2,[x19, #0x1dc] | `FALL_THROUGH`
<a id="insn-00ac8f50"></a> `00ac8f50` | `75 86 42 b9` | ldr w21,[x19, #0x284] | `FALL_THROUGH`
<a id="insn-00ac8f54"></a> `00ac8f54` | `01 08 21 1e` | fmul s1,s0,s1 | `FALL_THROUGH`
<a id="insn-00ac8f58"></a> `00ac8f58` | `21 18 22 1e` | fdiv s1,s1,s2 | `FALL_THROUGH`
<a id="insn-00ac8f5c"></a> `00ac8f5c` | `02 90 25 1e` | fmov s2,0x41600000 | `FALL_THROUGH`
<a id="insn-00ac8f60"></a> `00ac8f60` | `28 68 22 1e` | fmaxnm s8,s1,s2 | `FALL_THROUGH`
<a id="insn-00ac8f64"></a> `00ac8f64` | `00 38 28 1e` | fsub s0,s0,s8 | `FALL_THROUGH`
<a id="insn-00ac8f68"></a> `00ac8f68` | `14 00 38 1e` | fcvtzs w20,s0 | `FALL_THROUGH`
<a id="insn-00ac8f6c"></a> `00ac8f6c` | `79 21 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f70"></a> `00ac8f70` | `00 c1 22 1e` | fcvt d0,s8 | `FALL_THROUGH`
<a id="insn-00ac8f74"></a> `00ac8f74` | `08 40 61 1e` | fneg d8,d0 | `FALL_THROUGH`
<a id="insn-00ac8f78"></a> `00ac8f78` | `35 01 00 34` | cbz w21,0x00ac8f9c | `CONDITIONAL_JUMP`
<a id="insn-00ac8f7c"></a> `00ac8f7c` | `e2 48 f6 97` | bl 0x0085b304 | `UNCONDITIONAL_CALL`
<a id="insn-00ac8f80"></a> `00ac8f80` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00ac8f84"></a> `00ac8f84` | `61 ea 41 bd` | ldr s1,[x19, #0x1e8] | `FALL_THROUGH`
<a id="insn-00ac8f88"></a> `00ac8f88` | `08 00 00 14` | b 0x00ac8fa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8f8c"></a> `00ac8f8c` | `60 f2 41 bd` | ldr s0,[x19, #0x1f0] | `FALL_THROUGH`
<a id="insn-00ac8f90"></a> `00ac8f90` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ac8f94"></a> `00ac8f94` | `60 f6 01 bd` | str s0,[x19, #0x1f4] | `FALL_THROUGH`
<a id="insn-00ac8f98"></a> `00ac8f98` | `11 00 00 14` | b 0x00ac8fdc | `UNCONDITIONAL_JUMP`
<a id="insn-00ac8f9c"></a> `00ac8f9c` | `d8 48 f6 97` | bl 0x0085b2fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac8fa0"></a> `00ac8fa0` | `61 e6 41 bd` | ldr s1,[x19, #0x1e4] | `FALL_THROUGH`
<a id="insn-00ac8fa4"></a> `00ac8fa4` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00ac8fa8"></a> `00ac8fa8` | `00 38 21 1e` | fsub s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00ac8fac"></a> `00ac8fac` | `01 10 6c 1e` | fmov d1,0x3fe0000000000000 | `FALL_THROUGH`
<a id="insn-00ac8fb0"></a> `00ac8fb0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8fb4"></a> `00ac8fb4` | `00 c0 22 1e` | fcvt d0,s0 | `FALL_THROUGH`
<a id="insn-00ac8fb8"></a> `00ac8fb8` | `00 01 41 1f` | fmadd d0,d8,d1,d0 | `FALL_THROUGH`
<a id="insn-00ac8fbc"></a> `00ac8fbc` | `81 02 22 1e` | scvtf s1,w20 | `FALL_THROUGH`
<a id="insn-00ac8fc0"></a> `00ac8fc0` | `00 40 62 1e` | fcvt s0,d0 | `FALL_THROUGH`
<a id="insn-00ac8fc4"></a> `00ac8fc4` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00ac8fc8"></a> `00ac8fc8` | `01 10 2e 1e` | fmov s1,0x3f800000 | `FALL_THROUGH`
<a id="insn-00ac8fcc"></a> `00ac8fcc` | `00 78 21 1e` | fminnm s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00ac8fd0"></a> `00ac8fd0` | `01 e4 00 2f` | movi d1,#0x0 | `FALL_THROUGH`
<a id="insn-00ac8fd4"></a> `00ac8fd4` | `00 68 21 1e` | fmaxnm s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00ac8fd8"></a> `00ac8fd8` | `60 f2 01 bd` | str s0,[x19, #0x1f0] | `FALL_THROUGH`
<a id="insn-00ac8fdc"></a> `00ac8fdc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac8fe0"></a> `00ac8fe0` | `f5 0f 40 f9` | ldr x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ac8fe4"></a> `00ac8fe4` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac8fe8"></a> `00ac8fe8` | `e8 07 43 fc` | ldr d8,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ac8fec"></a> `00ac8fec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac8ecc`](#insn-00ac8ecc) 範囲 `[['00ac8ecc', '00ac8ed3']]`
  - `CONDITIONAL_JUMP` [`00ac8ed0`](#insn-00ac8ed0) → [`00ac8f30`](#insn-00ac8f30)
  - `FALL_THROUGH` [`00ac8ed0`](#insn-00ac8ed0) → [`00ac8ed4`](#insn-00ac8ed4)
- ブロック [`00ac8ed4`](#insn-00ac8ed4) 範囲 `[['00ac8ed4', '00ac8ef7']]`
  - `CONDITIONAL_JUMP` [`00ac8ef4`](#insn-00ac8ef4) → [`00ac8f14`](#insn-00ac8f14)
  - `FALL_THROUGH` [`00ac8ef4`](#insn-00ac8ef4) → [`00ac8ef8`](#insn-00ac8ef8)
- ブロック [`00ac8ef8`](#insn-00ac8ef8) 範囲 `[['00ac8ef8', '00ac8f03']]`
  - `CONDITIONAL_JUMP` [`00ac8f00`](#insn-00ac8f00) → [`00ac8f14`](#insn-00ac8f14)
  - `FALL_THROUGH` [`00ac8f00`](#insn-00ac8f00) → [`00ac8f04`](#insn-00ac8f04)
- ブロック [`00ac8f04`](#insn-00ac8f04) 範囲 `[['00ac8f04', '00ac8f13']]`
  - `CONDITIONAL_JUMP` [`00ac8f10`](#insn-00ac8f10) → [`00ac8f8c`](#insn-00ac8f8c)
  - `FALL_THROUGH` [`00ac8f10`](#insn-00ac8f10) → [`00ac8f14`](#insn-00ac8f14)
- ブロック [`00ac8f14`](#insn-00ac8f14) 範囲 `[['00ac8f14', '00ac8f1f']]`
  - `CONDITIONAL_JUMP` [`00ac8f1c`](#insn-00ac8f1c) → [`00ac8f38`](#insn-00ac8f38)
  - `FALL_THROUGH` [`00ac8f1c`](#insn-00ac8f1c) → [`00ac8f20`](#insn-00ac8f20)
- ブロック [`00ac8f20`](#insn-00ac8f20) 範囲 `[['00ac8f20', '00ac8f2f']]`
  - `UNCONDITIONAL_JUMP` [`00ac8f2c`](#insn-00ac8f2c) → [`00ac8fdc`](#insn-00ac8fdc)
- ブロック [`00ac8f30`](#insn-00ac8f30) 範囲 `[['00ac8f30', '00ac8f37']]`
- ブロック [`00ac8f38`](#insn-00ac8f38) 範囲 `[['00ac8f38', '00ac8f3b']]`
  - `FALL_THROUGH` [`00ac8f38`](#insn-00ac8f38) → [`00ac8f3c`](#insn-00ac8f3c)
- ブロック [`00ac8f3c`](#insn-00ac8f3c) 範囲 `[['00ac8f3c', '00ac8f43']]`
  - `CONDITIONAL_JUMP` [`00ac8f40`](#insn-00ac8f40) → [`00ac8f8c`](#insn-00ac8f8c)
  - `FALL_THROUGH` [`00ac8f40`](#insn-00ac8f40) → [`00ac8f44`](#insn-00ac8f44)
- ブロック [`00ac8f44`](#insn-00ac8f44) 範囲 `[['00ac8f44', '00ac8f4b']]`
  - `FALL_THROUGH` [`00ac8f48`](#insn-00ac8f48) → [`00ac8f4c`](#insn-00ac8f4c)
- ブロック [`00ac8f4c`](#insn-00ac8f4c) 範囲 `[['00ac8f4c', '00ac8f7b']]`
  - `CONDITIONAL_JUMP` [`00ac8f78`](#insn-00ac8f78) → [`00ac8f9c`](#insn-00ac8f9c)
  - `FALL_THROUGH` [`00ac8f78`](#insn-00ac8f78) → [`00ac8f7c`](#insn-00ac8f7c)
- ブロック [`00ac8f7c`](#insn-00ac8f7c) 範囲 `[['00ac8f7c', '00ac8f87']]`
  - `FALL_THROUGH` [`00ac8f84`](#insn-00ac8f84) → [`00ac8f88`](#insn-00ac8f88)
- ブロック [`00ac8f88`](#insn-00ac8f88) 範囲 `[['00ac8f88', '00ac8f8b']]`
  - `UNCONDITIONAL_JUMP` [`00ac8f88`](#insn-00ac8f88) → [`00ac8fa8`](#insn-00ac8fa8)
- ブロック [`00ac8f8c`](#insn-00ac8f8c) 範囲 `[['00ac8f8c', '00ac8f9b']]`
  - `UNCONDITIONAL_JUMP` [`00ac8f98`](#insn-00ac8f98) → [`00ac8fdc`](#insn-00ac8fdc)
- ブロック [`00ac8f9c`](#insn-00ac8f9c) 範囲 `[['00ac8f9c', '00ac8fa7']]`
  - `FALL_THROUGH` [`00ac8fa4`](#insn-00ac8fa4) → [`00ac8fa8`](#insn-00ac8fa8)
- ブロック [`00ac8fa8`](#insn-00ac8fa8) 範囲 `[['00ac8fa8', '00ac8fbb']]`
  - `FALL_THROUGH` [`00ac8fb8`](#insn-00ac8fb8) → [`00ac8fbc`](#insn-00ac8fbc)
- ブロック [`00ac8fbc`](#insn-00ac8fbc) 範囲 `[['00ac8fbc', '00ac8fd3']]`
  - `FALL_THROUGH` [`00ac8fd0`](#insn-00ac8fd0) → [`00ac8fd4`](#insn-00ac8fd4)
- ブロック [`00ac8fd4`](#insn-00ac8fd4) 範囲 `[['00ac8fd4', '00ac8fdb']]`
  - `FALL_THROUGH` [`00ac8fd8`](#insn-00ac8fd8) → [`00ac8fdc`](#insn-00ac8fdc)
- ブロック [`00ac8fdc`](#insn-00ac8fdc) 範囲 `[['00ac8fdc', '00ac8fef']]`

## 命令位置別の参照

- [`00ac8ed0`](#insn-00ac8ed0) → [`00ac8f30`](#insn-00ac8f30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ed4`](#insn-00ac8ed4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ed8`](#insn-00ac8ed8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8edc`](#insn-00ac8edc) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ee0`](#insn-00ac8ee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8eec`](#insn-00ac8eec) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ef0`](#insn-00ac8ef0) → [`00859ba4`](../00859/00859ba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00859ba4` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ef4`](#insn-00ac8ef4) → [`00ac8f14`](#insn-00ac8f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8ef8`](#insn-00ac8ef8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00ac8efc`](#insn-00ac8efc) → [`0085b338`](../0085b/0085b338.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b338` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f00`](#insn-00ac8f00) → [`00ac8f14`](#insn-00ac8f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f04`](#insn-00ac8f04) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f10`](#insn-00ac8f10) → [`00ac8f8c`](#insn-00ac8f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f14`](#insn-00ac8f14) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f18`](#insn-00ac8f18) → [`0085b338`](../0085b/0085b338.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b338` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f1c`](#insn-00ac8f1c) → [`00ac8f38`](#insn-00ac8f38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f2c`](#insn-00ac8f2c) → [`00ac8fdc`](#insn-00ac8fdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f3c`](#insn-00ac8f3c) → [`00ac8ff0`](00ac8ff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac8ff0` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f40`](#insn-00ac8f40) → [`00ac8f8c`](#insn-00ac8f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f6c`](#insn-00ac8f6c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f78`](#insn-00ac8f78) → [`00ac8f9c`](#insn-00ac8f9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f7c`](#insn-00ac8f7c) → [`0085b304`](../0085b/0085b304.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b304` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f88`](#insn-00ac8f88) → [`00ac8fa8`](#insn-00ac8fa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f98`](#insn-00ac8f98) → [`00ac8fdc`](#insn-00ac8fdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8f9c`](#insn-00ac8f9c) → [`0085b2fc`](../0085b/0085b2fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fdc`](#insn-00ac8fdc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fe0`](#insn-00ac8fe0) → `Stack[-0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8fe4`](#insn-00ac8fe4) → `Stack[-0x28]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac8ed0`](#insn-00ac8ed0)

~~~json
{
  "source": "00ac8ed0",
  "target": "00ac8f30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8ed4`](#insn-00ac8ed4)

~~~json
{
  "source": "00ac8ed4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8ed8`](#insn-00ac8ed8)

~~~json
{
  "source": "00ac8ed8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8edc`](#insn-00ac8edc)

~~~json
{
  "source": "00ac8edc",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8ee0`](#insn-00ac8ee0)

~~~json
{
  "source": "00ac8ee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8eec`](#insn-00ac8eec)

~~~json
{
  "source": "00ac8eec",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ef0`](#insn-00ac8ef0)

~~~json
{
  "source": "00ac8ef0",
  "target": "00859ba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8ef4`](#insn-00ac8ef4)

~~~json
{
  "source": "00ac8ef4",
  "target": "00ac8f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8ef8`](#insn-00ac8ef8)

~~~json
{
  "source": "00ac8ef8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8efc`](#insn-00ac8efc)

~~~json
{
  "source": "00ac8efc",
  "target": "0085b338",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f00`](#insn-00ac8f00)

~~~json
{
  "source": "00ac8f00",
  "target": "00ac8f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f04`](#insn-00ac8f04)

~~~json
{
  "source": "00ac8f04",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f10`](#insn-00ac8f10)

~~~json
{
  "source": "00ac8f10",
  "target": "00ac8f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f14`](#insn-00ac8f14)

~~~json
{
  "source": "00ac8f14",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f18`](#insn-00ac8f18)

~~~json
{
  "source": "00ac8f18",
  "target": "0085b338",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f1c`](#insn-00ac8f1c)

~~~json
{
  "source": "00ac8f1c",
  "target": "00ac8f38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f2c`](#insn-00ac8f2c)

~~~json
{
  "source": "00ac8f2c",
  "target": "00ac8fdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f3c`](#insn-00ac8f3c)

~~~json
{
  "source": "00ac8f3c",
  "target": "00ac8ff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f40`](#insn-00ac8f40)

~~~json
{
  "source": "00ac8f40",
  "target": "00ac8f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f6c`](#insn-00ac8f6c)

~~~json
{
  "source": "00ac8f6c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f78`](#insn-00ac8f78)

~~~json
{
  "source": "00ac8f78",
  "target": "00ac8f9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f7c`](#insn-00ac8f7c)

~~~json
{
  "source": "00ac8f7c",
  "target": "0085b304",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8f88`](#insn-00ac8f88)

~~~json
{
  "source": "00ac8f88",
  "target": "00ac8fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f98`](#insn-00ac8f98)

~~~json
{
  "source": "00ac8f98",
  "target": "00ac8fdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8f9c`](#insn-00ac8f9c)

~~~json
{
  "source": "00ac8f9c",
  "target": "0085b2fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac8fdc`](#insn-00ac8fdc)

~~~json
{
  "source": "00ac8fdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fe0`](#insn-00ac8fe0)

~~~json
{
  "source": "00ac8fe0",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8fe4`](#insn-00ac8fe4)

~~~json
{
  "source": "00ac8fe4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
