# 00a6accc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a6ac88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6ac88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0002.md#compare-26ee11d5154deb64abde03f304d7a7e0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac8c60`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c60.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-dd401640a4ef3aa39dd46fe97c475d74)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6accc",
  "name": "FUN_00a6accc",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b213e49280e4a176fbdcecba4dbbe50cd0a91b36bb520ccb58d1adf037769904",
  "source_text_sha256": "b213e49280e4a176fbdcecba4dbbe50cd0a91b36bb520ccb58d1adf037769904",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6accc",
        "00a6adef"
      ]
    ],
    "bytes_sha256": "e7daa51f74aa962df56d5464971a60d635064284712d6f7c5cf20f63cb6a6861",
    "instruction_count": 73,
    "instruction_bytes": 292,
    "body_bytes": 292,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00632468](../00632/00632468.md)
- [00664710](../00664/00664710.md)
- [006aad48](../006aa/006aad48.md)
- [006d6364](../006d6/006d6364.md)
- [0073fa38](../0073f/0073fa38.md)
- [00803d90](../00803/00803d90.md)
- [0088d060](../0088d/0088d060.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)
- [00827b94](../00827/00827b94.md)
- [008292ec](../00829/008292ec.md)
- [008292f4](../00829/008292f4.md)
- [00829328](../00829/00829328.md)
- [00a6adf0](../00a6a/00a6adf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1520 bytes

~~~c

undefined8 FUN_00a6accc(long param_1)

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
  FUN_0081f580();
  uVar2 = FUN_00827b94();
  if ((uVar2 & 1) == 0) {
    FUN_0081f580();
    uVar2 = FUN_00829328();
    if (((uVar2 & 1) == 0) && (lVar3 = FUN_0081f580(), *(char *)(lVar3 + 0x347d) == '\0'))
    goto LAB_00a6ad8c;
  }
  FUN_0081f580();
  uVar2 = FUN_00829328();
  if ((uVar2 & 1) != 0) {
    *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
    return 1;
  }
  uVar2 = FUN_00a6adf0(param_1);
  if ((uVar2 & 1) != 0) {
    fVar4 = *(float *)(param_1 + 0x1d8);
    iVar1 = *(int *)(param_1 + 0x284);
    fVar5 = (fVar4 * *(float *)(param_1 + 0x1e0)) / *(float *)(param_1 + 0x1dc);
    if (fVar5 <= 14.0) {
      fVar5 = 14.0;
    }
    FUN_0081f580();
    if (iVar1 == 0) {
      iVar1 = FUN_008292ec();
      fVar6 = *(float *)(param_1 + 0x1e4);
    }
    else {
      iVar1 = FUN_008292f4();
      fVar6 = *(float *)(param_1 + 0x1e8);
    }
    fVar4 = (float)NEON_fminnm((((float)iVar1 - fVar6) + -fVar5 * 0.5) / (float)(int)(fVar4 - fVar5)
                               ,0x3f800000);
    if (fVar4 <= 0.0) {
      fVar4 = 0.0;
    }
    *(float *)(param_1 + 0x1f0) = fVar4;
    return 1;
  }
LAB_00a6ad8c:
  *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
                    /* try { // try from 00a6addc to 00b6ae0b has its CatchHandler @ 00a6b6a4 */
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6accc"></a> `00a6accc` | `08 50 47 39` | ldrb w8,[x0, #0x1d4] | `FALL_THROUGH`
<a id="insn-00a6acd0"></a> `00a6acd0` | `08 03 00 34` | cbz w8,0x00a6ad30 | `CONDITIONAL_JUMP`
<a id="insn-00a6acd4"></a> `00a6acd4` | `e8 0f 1d fc` | str d8,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a6acd8"></a> `00a6acd8` | `fd fb 00 a9` | stp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6acdc"></a> `00a6acdc` | `f5 0f 00 f9` | str x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a6ace0"></a> `00a6ace0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6ace4"></a> `00a6ace4` | `fd 23 00 91` | add x29,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a6ace8"></a> `00a6ace8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a6acec"></a> `00a6acec` | `25 d2 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6acf0"></a> `00a6acf0` | `a9 f3 f6 97` | bl 0x00827b94 | `UNCONDITIONAL_CALL`
<a id="insn-00a6acf4"></a> `00a6acf4` | `00 01 00 37` | tbnz w0,#0x0,0x00a6ad14 | `CONDITIONAL_JUMP`
<a id="insn-00a6acf8"></a> `00a6acf8` | `22 d2 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6acfc"></a> `00a6acfc` | `8b f9 f6 97` | bl 0x00829328 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad00"></a> `00a6ad00` | `a0 00 00 37` | tbnz w0,#0x0,0x00a6ad14 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad04"></a> `00a6ad04` | `1f d2 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad08"></a> `00a6ad08` | `a8 8f 86 52` | mov w8,#0x347d | `FALL_THROUGH`
<a id="insn-00a6ad0c"></a> `00a6ad0c` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a6ad10"></a> `00a6ad10` | `e8 03 00 34` | cbz w8,0x00a6ad8c | `CONDITIONAL_JUMP`
<a id="insn-00a6ad14"></a> `00a6ad14` | `1b d2 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad18"></a> `00a6ad18` | `84 f9 f6 97` | bl 0x00829328 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad1c"></a> `00a6ad1c` | `e0 00 00 36` | tbz w0,#0x0,0x00a6ad38 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad20"></a> `00a6ad20` | `60 f2 41 bd` | ldr s0,[x19, #0x1f0] | `FALL_THROUGH`
<a id="insn-00a6ad24"></a> `00a6ad24` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a6ad28"></a> `00a6ad28` | `60 f6 01 bd` | str s0,[x19, #0x1f4] | `FALL_THROUGH`
<a id="insn-00a6ad2c"></a> `00a6ad2c` | `2c 00 00 14` | b 0x00a6addc | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ad30"></a> `00a6ad30` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a6ad34"></a> `00a6ad34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6ad38"></a> `00a6ad38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6ad3c"></a> `00a6ad3c` | `2d 00 00 94` | bl 0x00a6adf0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad40"></a> `00a6ad40` | `60 02 00 36` | tbz w0,#0x0,0x00a6ad8c | `CONDITIONAL_JUMP`
<a id="insn-00a6ad44"></a> `00a6ad44` | `60 da 41 bd` | ldr s0,[x19, #0x1d8] | `FALL_THROUGH`
<a id="insn-00a6ad48"></a> `00a6ad48` | `61 e2 41 bd` | ldr s1,[x19, #0x1e0] | `FALL_THROUGH`
<a id="insn-00a6ad4c"></a> `00a6ad4c` | `62 de 41 bd` | ldr s2,[x19, #0x1dc] | `FALL_THROUGH`
<a id="insn-00a6ad50"></a> `00a6ad50` | `75 86 42 b9` | ldr w21,[x19, #0x284] | `FALL_THROUGH`
<a id="insn-00a6ad54"></a> `00a6ad54` | `01 08 21 1e` | fmul s1,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6ad58"></a> `00a6ad58` | `21 18 22 1e` | fdiv s1,s1,s2 | `FALL_THROUGH`
<a id="insn-00a6ad5c"></a> `00a6ad5c` | `02 90 25 1e` | fmov s2,0x41600000 | `FALL_THROUGH`
<a id="insn-00a6ad60"></a> `00a6ad60` | `28 68 22 1e` | fmaxnm s8,s1,s2 | `FALL_THROUGH`
<a id="insn-00a6ad64"></a> `00a6ad64` | `00 38 28 1e` | fsub s0,s0,s8 | `FALL_THROUGH`
<a id="insn-00a6ad68"></a> `00a6ad68` | `14 00 38 1e` | fcvtzs w20,s0 | `FALL_THROUGH`
<a id="insn-00a6ad6c"></a> `00a6ad6c` | `05 d2 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad70"></a> `00a6ad70` | `00 c1 22 1e` | fcvt d0,s8 | `FALL_THROUGH`
<a id="insn-00a6ad74"></a> `00a6ad74` | `08 40 61 1e` | fneg d8,d0 | `FALL_THROUGH`
<a id="insn-00a6ad78"></a> `00a6ad78` | `35 01 00 34` | cbz w21,0x00a6ad9c | `CONDITIONAL_JUMP`
<a id="insn-00a6ad7c"></a> `00a6ad7c` | `5e f9 f6 97` | bl 0x008292f4 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad80"></a> `00a6ad80` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00a6ad84"></a> `00a6ad84` | `61 ea 41 bd` | ldr s1,[x19, #0x1e8] | `FALL_THROUGH`
<a id="insn-00a6ad88"></a> `00a6ad88` | `08 00 00 14` | b 0x00a6ada8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ad8c"></a> `00a6ad8c` | `60 f2 41 bd` | ldr s0,[x19, #0x1f0] | `FALL_THROUGH`
<a id="insn-00a6ad90"></a> `00a6ad90` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a6ad94"></a> `00a6ad94` | `60 f6 01 bd` | str s0,[x19, #0x1f4] | `FALL_THROUGH`
<a id="insn-00a6ad98"></a> `00a6ad98` | `11 00 00 14` | b 0x00a6addc | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ad9c"></a> `00a6ad9c` | `54 f9 f6 97` | bl 0x008292ec | `UNCONDITIONAL_CALL`
<a id="insn-00a6ada0"></a> `00a6ada0` | `61 e6 41 bd` | ldr s1,[x19, #0x1e4] | `FALL_THROUGH`
<a id="insn-00a6ada4"></a> `00a6ada4` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00a6ada8"></a> `00a6ada8` | `00 38 21 1e` | fsub s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6adac"></a> `00a6adac` | `01 10 6c 1e` | fmov d1,0x3fe0000000000000 | `FALL_THROUGH`
<a id="insn-00a6adb0"></a> `00a6adb0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a6adb4"></a> `00a6adb4` | `00 c0 22 1e` | fcvt d0,s0 | `FALL_THROUGH`
<a id="insn-00a6adb8"></a> `00a6adb8` | `00 01 41 1f` | fmadd d0,d8,d1,d0 | `FALL_THROUGH`
<a id="insn-00a6adbc"></a> `00a6adbc` | `81 02 22 1e` | scvtf s1,w20 | `FALL_THROUGH`
<a id="insn-00a6adc0"></a> `00a6adc0` | `00 40 62 1e` | fcvt s0,d0 | `FALL_THROUGH`
<a id="insn-00a6adc4"></a> `00a6adc4` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6adc8"></a> `00a6adc8` | `01 10 2e 1e` | fmov s1,0x3f800000 | `FALL_THROUGH`
<a id="insn-00a6adcc"></a> `00a6adcc` | `00 78 21 1e` | fminnm s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6add0"></a> `00a6add0` | `01 e4 00 2f` | movi d1,#0x0 | `FALL_THROUGH`
<a id="insn-00a6add4"></a> `00a6add4` | `00 68 21 1e` | fmaxnm s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6add8"></a> `00a6add8` | `60 f2 01 bd` | str s0,[x19, #0x1f0] | `FALL_THROUGH`
<a id="insn-00a6addc"></a> `00a6addc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6ade0"></a> `00a6ade0` | `f5 0f 40 f9` | ldr x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a6ade4"></a> `00a6ade4` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6ade8"></a> `00a6ade8` | `e8 07 43 fc` | ldr d8,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a6adec"></a> `00a6adec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6accc`](#insn-00a6accc) 範囲 `[['00a6accc', '00a6acd3']]`
  - `CONDITIONAL_JUMP` [`00a6acd0`](#insn-00a6acd0) → [`00a6ad30`](#insn-00a6ad30)
  - `FALL_THROUGH` [`00a6acd0`](#insn-00a6acd0) → [`00a6acd4`](#insn-00a6acd4)
- ブロック [`00a6acd4`](#insn-00a6acd4) 範囲 `[['00a6acd4', '00a6acf7']]`
  - `CONDITIONAL_JUMP` [`00a6acf4`](#insn-00a6acf4) → [`00a6ad14`](#insn-00a6ad14)
  - `FALL_THROUGH` [`00a6acf4`](#insn-00a6acf4) → [`00a6acf8`](#insn-00a6acf8)
- ブロック [`00a6acf8`](#insn-00a6acf8) 範囲 `[['00a6acf8', '00a6ad03']]`
  - `CONDITIONAL_JUMP` [`00a6ad00`](#insn-00a6ad00) → [`00a6ad14`](#insn-00a6ad14)
  - `FALL_THROUGH` [`00a6ad00`](#insn-00a6ad00) → [`00a6ad04`](#insn-00a6ad04)
- ブロック [`00a6ad04`](#insn-00a6ad04) 範囲 `[['00a6ad04', '00a6ad13']]`
  - `CONDITIONAL_JUMP` [`00a6ad10`](#insn-00a6ad10) → [`00a6ad8c`](#insn-00a6ad8c)
  - `FALL_THROUGH` [`00a6ad10`](#insn-00a6ad10) → [`00a6ad14`](#insn-00a6ad14)
- ブロック [`00a6ad14`](#insn-00a6ad14) 範囲 `[['00a6ad14', '00a6ad1f']]`
  - `CONDITIONAL_JUMP` [`00a6ad1c`](#insn-00a6ad1c) → [`00a6ad38`](#insn-00a6ad38)
  - `FALL_THROUGH` [`00a6ad1c`](#insn-00a6ad1c) → [`00a6ad20`](#insn-00a6ad20)
- ブロック [`00a6ad20`](#insn-00a6ad20) 範囲 `[['00a6ad20', '00a6ad2f']]`
  - `UNCONDITIONAL_JUMP` [`00a6ad2c`](#insn-00a6ad2c) → [`00a6addc`](#insn-00a6addc)
- ブロック [`00a6ad30`](#insn-00a6ad30) 範囲 `[['00a6ad30', '00a6ad37']]`
- ブロック [`00a6ad38`](#insn-00a6ad38) 範囲 `[['00a6ad38', '00a6ad43']]`
  - `CONDITIONAL_JUMP` [`00a6ad40`](#insn-00a6ad40) → [`00a6ad8c`](#insn-00a6ad8c)
  - `FALL_THROUGH` [`00a6ad40`](#insn-00a6ad40) → [`00a6ad44`](#insn-00a6ad44)
- ブロック [`00a6ad44`](#insn-00a6ad44) 範囲 `[['00a6ad44', '00a6ad7b']]`
  - `CONDITIONAL_JUMP` [`00a6ad78`](#insn-00a6ad78) → [`00a6ad9c`](#insn-00a6ad9c)
  - `FALL_THROUGH` [`00a6ad78`](#insn-00a6ad78) → [`00a6ad7c`](#insn-00a6ad7c)
- ブロック [`00a6ad7c`](#insn-00a6ad7c) 範囲 `[['00a6ad7c', '00a6ad8b']]`
  - `UNCONDITIONAL_JUMP` [`00a6ad88`](#insn-00a6ad88) → [`00a6ada8`](#insn-00a6ada8)
- ブロック [`00a6ad8c`](#insn-00a6ad8c) 範囲 `[['00a6ad8c', '00a6ad9b']]`
  - `UNCONDITIONAL_JUMP` [`00a6ad98`](#insn-00a6ad98) → [`00a6addc`](#insn-00a6addc)
- ブロック [`00a6ad9c`](#insn-00a6ad9c) 範囲 `[['00a6ad9c', '00a6ada7']]`
  - `FALL_THROUGH` [`00a6ada4`](#insn-00a6ada4) → [`00a6ada8`](#insn-00a6ada8)
- ブロック [`00a6ada8`](#insn-00a6ada8) 範囲 `[['00a6ada8', '00a6addb']]`
  - `FALL_THROUGH` [`00a6add8`](#insn-00a6add8) → [`00a6addc`](#insn-00a6addc)
- ブロック [`00a6addc`](#insn-00a6addc) 範囲 `[['00a6addc', '00a6adef']]`

## 命令位置別の参照

- [`00a6acd0`](#insn-00a6acd0) → [`00a6ad30`](#insn-00a6ad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acd4`](#insn-00a6acd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acd8`](#insn-00a6acd8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acdc`](#insn-00a6acdc) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ace0`](#insn-00a6ace0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acec`](#insn-00a6acec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6acf0`](#insn-00a6acf0) → [`00827b94`](../00827/00827b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00827b94` · 推定シンボル `None` · 推定型 `None`
- [`00a6acf4`](#insn-00a6acf4) → [`00a6ad14`](#insn-00a6ad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acf8`](#insn-00a6acf8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6acfc`](#insn-00a6acfc) → [`00829328`](../00829/00829328.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00829328` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad00`](#insn-00a6ad00) → [`00a6ad14`](#insn-00a6ad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad04`](#insn-00a6ad04) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad10`](#insn-00a6ad10) → [`00a6ad8c`](#insn-00a6ad8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad14`](#insn-00a6ad14) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad18`](#insn-00a6ad18) → [`00829328`](../00829/00829328.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00829328` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad1c`](#insn-00a6ad1c) → [`00a6ad38`](#insn-00a6ad38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad2c`](#insn-00a6ad2c) → [`00a6addc`](#insn-00a6addc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad3c`](#insn-00a6ad3c) → [`00a6adf0`](00a6adf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6adf0` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad40`](#insn-00a6ad40) → [`00a6ad8c`](#insn-00a6ad8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad6c`](#insn-00a6ad6c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad78`](#insn-00a6ad78) → [`00a6ad9c`](#insn-00a6ad9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad7c`](#insn-00a6ad7c) → [`008292f4`](../00829/008292f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008292f4` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad88`](#insn-00a6ad88) → [`00a6ada8`](#insn-00a6ada8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad98`](#insn-00a6ad98) → [`00a6addc`](#insn-00a6addc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad9c`](#insn-00a6ad9c) → [`008292ec`](../00829/008292ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008292ec` · 推定シンボル `None` · 推定型 `None`
- [`00a6addc`](#insn-00a6addc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ade0`](#insn-00a6ade0) → `Stack[-0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ade4`](#insn-00a6ade4) → `Stack[-0x28]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6acd0`](#insn-00a6acd0)

~~~json
{
  "source": "00a6acd0",
  "target": "00a6ad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acd4`](#insn-00a6acd4)

~~~json
{
  "source": "00a6acd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acd8`](#insn-00a6acd8)

~~~json
{
  "source": "00a6acd8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acdc`](#insn-00a6acdc)

~~~json
{
  "source": "00a6acdc",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ace0`](#insn-00a6ace0)

~~~json
{
  "source": "00a6ace0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acec`](#insn-00a6acec)

~~~json
{
  "source": "00a6acec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6acf0`](#insn-00a6acf0)

~~~json
{
  "source": "00a6acf0",
  "target": "00827b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6acf4`](#insn-00a6acf4)

~~~json
{
  "source": "00a6acf4",
  "target": "00a6ad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acf8`](#insn-00a6acf8)

~~~json
{
  "source": "00a6acf8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6acfc`](#insn-00a6acfc)

~~~json
{
  "source": "00a6acfc",
  "target": "00829328",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad00`](#insn-00a6ad00)

~~~json
{
  "source": "00a6ad00",
  "target": "00a6ad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad04`](#insn-00a6ad04)

~~~json
{
  "source": "00a6ad04",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad10`](#insn-00a6ad10)

~~~json
{
  "source": "00a6ad10",
  "target": "00a6ad8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad14`](#insn-00a6ad14)

~~~json
{
  "source": "00a6ad14",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad18`](#insn-00a6ad18)

~~~json
{
  "source": "00a6ad18",
  "target": "00829328",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad1c`](#insn-00a6ad1c)

~~~json
{
  "source": "00a6ad1c",
  "target": "00a6ad38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad2c`](#insn-00a6ad2c)

~~~json
{
  "source": "00a6ad2c",
  "target": "00a6addc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad3c`](#insn-00a6ad3c)

~~~json
{
  "source": "00a6ad3c",
  "target": "00a6adf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad40`](#insn-00a6ad40)

~~~json
{
  "source": "00a6ad40",
  "target": "00a6ad8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad6c`](#insn-00a6ad6c)

~~~json
{
  "source": "00a6ad6c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad78`](#insn-00a6ad78)

~~~json
{
  "source": "00a6ad78",
  "target": "00a6ad9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad7c`](#insn-00a6ad7c)

~~~json
{
  "source": "00a6ad7c",
  "target": "008292f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad88`](#insn-00a6ad88)

~~~json
{
  "source": "00a6ad88",
  "target": "00a6ada8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad98`](#insn-00a6ad98)

~~~json
{
  "source": "00a6ad98",
  "target": "00a6addc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad9c`](#insn-00a6ad9c)

~~~json
{
  "source": "00a6ad9c",
  "target": "008292ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6addc`](#insn-00a6addc)

~~~json
{
  "source": "00a6addc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ade0`](#insn-00a6ade0)

~~~json
{
  "source": "00a6ade0",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ade4`](#insn-00a6ade4)

~~~json
{
  "source": "00a6ade4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
