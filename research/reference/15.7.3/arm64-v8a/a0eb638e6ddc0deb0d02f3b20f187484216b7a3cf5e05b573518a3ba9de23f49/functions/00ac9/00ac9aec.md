# 00ac9aec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ac9a24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9a24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-5d9cd7e52cd478c2bb9822cab57e83b5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ac9b30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9b30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-b64f884be1f919ecf18ec8016ba57a6c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9aec",
  "name": "FUN_00ac9aec",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4e18ff19212e7d2d653ec3efb7228fe23179963dc05487e66b309671bdd8266",
  "source_text_sha256": "a4e18ff19212e7d2d653ec3efb7228fe23179963dc05487e66b309671bdd8266",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9aec",
        "00ac9c17"
      ]
    ],
    "bytes_sha256": "30d1cfd4ff40aac4f302a9900c876c92142d6dfd4be1c3267618f21aa87e7530",
    "instruction_count": 75,
    "instruction_bytes": 300,
    "body_bytes": 300,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ab3400](../00ab3/00ab3400.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00729118](../00729/00729118.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb1f0](../00bdb/00bdb1f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1421 bytes

~~~c

void FUN_00ac9aec(undefined8 *param_1,ulong param_2)

{
  ulong uVar1;
  void *__s;
  void *__dest;
  ulong uVar2;
  ulong uVar3;
  void *__src;
  void *__s_00;
  long lVar4;
  
  __s_00 = (void *)param_1[1];
  if ((ulong)(param_1[2] - (long)__s_00 >> 4) < param_2) {
    __src = (void *)*param_1;
    lVar4 = (long)__s_00 - (long)__src >> 4;
    uVar1 = lVar4 + param_2;
    if (uVar1 >> 0x3c != 0) {
      FUN_00729118(param_1);
LAB_00ac9c14:
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
    uVar2 = param_1[2] - (long)__src;
    uVar3 = (long)uVar2 >> 3;
    if (uVar3 <= uVar1) {
      uVar3 = uVar1;
    }
    if (0x7fffffffffffffef < uVar2) {
      uVar3 = 0xfffffffffffffff;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
    }
    else {
      if (uVar3 >> 0x3c != 0) goto LAB_00ac9c14;
      __dest = (void *)_Znwm(uVar3 << 4);
    }
    __s = (void *)((long)__dest + lVar4 * 0x10);
    memset(__s,0,param_2 * 0x10);
    memcpy(__dest,__src,(long)__s_00 - (long)__src);
    *param_1 = __dest;
    param_1[1] = (void *)((long)__s + param_2 * 0x10);
    param_1[2] = (void *)((long)__dest + uVar3 * 0x10);
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
      return;
    }
  }
  else {
    if (param_2 != 0) {
      memset(__s_00,0,param_2 * 0x10);
      __s_00 = (void *)((long)__s_00 + param_2 * 0x10);
    }
    param_1[1] = __s_00;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac9aec"></a> `00ac9aec` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00ac9af0"></a> `00ac9af0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9af4"></a> `00ac9af4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9af8"></a> `00ac9af8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9afc"></a> `00ac9afc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9b00"></a> `00ac9b00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ac9b04"></a> `00ac9b04` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9b08"></a> `00ac9b08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac9b0c"></a> `00ac9b0c` | `09 01 15 cb` | sub x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00ac9b10"></a> `00ac9b10` | `3f 10 89 eb` | cmp x1,x9, ASR #0x4 | `FALL_THROUGH`
<a id="insn-00ac9b14"></a> `00ac9b14` | `09 03 00 54` | b.ls 0x00ac9b74 | `CONDITIONAL_JUMP`
<a id="insn-00ac9b18"></a> `00ac9b18` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00ac9b1c"></a> `00ac9b1c` | `b5 02 14 cb` | sub x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00ac9b20"></a> `00ac9b20` | `b7 fe 44 93` | asr x23,x21,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9b24"></a> `00ac9b24` | `e9 02 01 8b` | add x9,x23,x1 | `FALL_THROUGH`
<a id="insn-00ac9b28"></a> `00ac9b28` | `2a fd 7c d3` | lsr x10,x9,#0x3c | `FALL_THROUGH`
<a id="insn-00ac9b2c"></a> `00ac9b2c` | `0a 07 00 b5` | cbnz x10,0x00ac9c0c | `CONDITIONAL_JUMP`
<a id="insn-00ac9b30"></a> `00ac9b30` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00ac9b34"></a> `00ac9b34` | `eb eb 7c b2` | orr x11,xzr,#0x7ffffffffffffff0 | `FALL_THROUGH`
<a id="insn-00ac9b38"></a> `00ac9b38` | `0a fd 43 93` | asr x10,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00ac9b3c"></a> `00ac9b3c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00ac9b40"></a> `00ac9b40` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00ac9b44"></a> `00ac9b44` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-00ac9b48"></a> `00ac9b48` | `08 00 fe 92` | mov x8,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-00ac9b4c"></a> `00ac9b4c` | `38 31 88 9a` | csel x24,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00ac9b50"></a> `00ac9b50` | `58 02 00 b4` | cbz x24,0x00ac9b98 | `CONDITIONAL_JUMP`
<a id="insn-00ac9b54"></a> `00ac9b54` | `08 ff 7c d3` | lsr x8,x24,#0x3c | `FALL_THROUGH`
<a id="insn-00ac9b58"></a> `00ac9b58` | `e8 05 00 b5` | cbnz x8,0x00ac9c14 | `CONDITIONAL_JUMP`
<a id="insn-00ac9b5c"></a> `00ac9b5c` | `00 ef 7c d3` | lsl x0,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9b60"></a> `00ac9b60` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00ac9b64"></a> `00ac9b64` | `23 45 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9b68"></a> `00ac9b68` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ac9b6c"></a> `00ac9b6c` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00ac9b70"></a> `00ac9b70` | `0b 00 00 14` | b 0x00ac9b9c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9b74"></a> `00ac9b74` | `e1 00 00 b4` | cbz x1,0x00ac9b90 | `CONDITIONAL_JUMP`
<a id="insn-00ac9b78"></a> `00ac9b78` | `34 ec 7c d3` | lsl x20,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9b7c"></a> `00ac9b7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9b80"></a> `00ac9b80` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9b84"></a> `00ac9b84` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ac9b88"></a> `00ac9b88` | `9a 45 04 94` | bl 0x00bdb1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9b8c"></a> `00ac9b8c` | `b5 02 14 8b` | add x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00ac9b90"></a> `00ac9b90` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9b94"></a> `00ac9b94` | `18 00 00 14` | b 0x00ac9bf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9b98"></a> `00ac9b98` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00ac9b9c"></a> `00ac9b9c` | `d7 12 17 8b` | add x23,x22,x23, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00ac9ba0"></a> `00ac9ba0` | `d9 12 18 8b` | add x25,x22,x24, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00ac9ba4"></a> `00ac9ba4` | `38 ec 7c d3` | lsl x24,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9ba8"></a> `00ac9ba8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9bac"></a> `00ac9bac` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ac9bb0"></a> `00ac9bb0` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00ac9bb4"></a> `00ac9bb4` | `8f 45 04 94` | bl 0x00bdb1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9bb8"></a> `00ac9bb8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ac9bbc"></a> `00ac9bbc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ac9bc0"></a> `00ac9bc0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ac9bc4"></a> `00ac9bc4` | `f7 02 18 8b` | add x23,x23,x24 | `FALL_THROUGH`
<a id="insn-00ac9bc8"></a> `00ac9bc8` | `66 45 04 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9bcc"></a> `00ac9bcc` | `76 5e 00 a9` | stp x22,x23,[x19] | `FALL_THROUGH`
<a id="insn-00ac9bd0"></a> `00ac9bd0` | `79 0a 00 f9` | str x25,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9bd4"></a> `00ac9bd4` | `14 01 00 b4` | cbz x20,0x00ac9bf4 | `CONDITIONAL_JUMP`
<a id="insn-00ac9bd8"></a> `00ac9bd8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9bdc"></a> `00ac9bdc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9be0"></a> `00ac9be0` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9be4"></a> `00ac9be4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9be8"></a> `00ac9be8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9bec"></a> `00ac9bec` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9bf0"></a> `00ac9bf0` | `08 45 04 14` | b 0x00bdb010 | `CALL_TERMINATOR`
<a id="insn-00ac9bf4"></a> `00ac9bf4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9bf8"></a> `00ac9bf8` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9bfc"></a> `00ac9bfc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9c00"></a> `00ac9c00` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9c04"></a> `00ac9c04` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9c08"></a> `00ac9c08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac9c0c"></a> `00ac9c0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac9c10"></a> `00ac9c10` | `42 7d f1 97` | bl 0x00729118 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c14"></a> `00ac9c14` | `db 51 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9aec`](#insn-00ac9aec) 範囲 `[['00ac9aec', '00ac9b17']]`
  - `CONDITIONAL_JUMP` [`00ac9b14`](#insn-00ac9b14) → [`00ac9b74`](#insn-00ac9b74)
  - `FALL_THROUGH` [`00ac9b14`](#insn-00ac9b14) → [`00ac9b18`](#insn-00ac9b18)
- ブロック [`00ac9b18`](#insn-00ac9b18) 範囲 `[['00ac9b18', '00ac9b2f']]`
  - `CONDITIONAL_JUMP` [`00ac9b2c`](#insn-00ac9b2c) → [`00ac9c0c`](#insn-00ac9c0c)
  - `FALL_THROUGH` [`00ac9b2c`](#insn-00ac9b2c) → [`00ac9b30`](#insn-00ac9b30)
- ブロック [`00ac9b30`](#insn-00ac9b30) 範囲 `[['00ac9b30', '00ac9b53']]`
  - `CONDITIONAL_JUMP` [`00ac9b50`](#insn-00ac9b50) → [`00ac9b98`](#insn-00ac9b98)
  - `FALL_THROUGH` [`00ac9b50`](#insn-00ac9b50) → [`00ac9b54`](#insn-00ac9b54)
- ブロック [`00ac9b54`](#insn-00ac9b54) 範囲 `[['00ac9b54', '00ac9b5b']]`
  - `CONDITIONAL_JUMP` [`00ac9b58`](#insn-00ac9b58) → [`00ac9c14`](#insn-00ac9c14)
  - `FALL_THROUGH` [`00ac9b58`](#insn-00ac9b58) → [`00ac9b5c`](#insn-00ac9b5c)
- ブロック [`00ac9b5c`](#insn-00ac9b5c) 範囲 `[['00ac9b5c', '00ac9b73']]`
  - `UNCONDITIONAL_JUMP` [`00ac9b70`](#insn-00ac9b70) → [`00ac9b9c`](#insn-00ac9b9c)
- ブロック [`00ac9b74`](#insn-00ac9b74) 範囲 `[['00ac9b74', '00ac9b77']]`
  - `CONDITIONAL_JUMP` [`00ac9b74`](#insn-00ac9b74) → [`00ac9b90`](#insn-00ac9b90)
  - `FALL_THROUGH` [`00ac9b74`](#insn-00ac9b74) → [`00ac9b78`](#insn-00ac9b78)
- ブロック [`00ac9b78`](#insn-00ac9b78) 範囲 `[['00ac9b78', '00ac9b8f']]`
  - `FALL_THROUGH` [`00ac9b8c`](#insn-00ac9b8c) → [`00ac9b90`](#insn-00ac9b90)
- ブロック [`00ac9b90`](#insn-00ac9b90) 範囲 `[['00ac9b90', '00ac9b97']]`
  - `UNCONDITIONAL_JUMP` [`00ac9b94`](#insn-00ac9b94) → [`00ac9bf4`](#insn-00ac9bf4)
- ブロック [`00ac9b98`](#insn-00ac9b98) 範囲 `[['00ac9b98', '00ac9b9b']]`
  - `FALL_THROUGH` [`00ac9b98`](#insn-00ac9b98) → [`00ac9b9c`](#insn-00ac9b9c)
- ブロック [`00ac9b9c`](#insn-00ac9b9c) 範囲 `[['00ac9b9c', '00ac9bd7']]`
  - `CONDITIONAL_JUMP` [`00ac9bd4`](#insn-00ac9bd4) → [`00ac9bf4`](#insn-00ac9bf4)
  - `FALL_THROUGH` [`00ac9bd4`](#insn-00ac9bd4) → [`00ac9bd8`](#insn-00ac9bd8)
- ブロック [`00ac9bd8`](#insn-00ac9bd8) 範囲 `[['00ac9bd8', '00ac9bf3']]`
- ブロック [`00ac9bf4`](#insn-00ac9bf4) 範囲 `[['00ac9bf4', '00ac9c0b']]`
- ブロック [`00ac9c0c`](#insn-00ac9c0c) 範囲 `[['00ac9c0c', '00ac9c13']]`
  - `FALL_THROUGH` [`00ac9c10`](#insn-00ac9c10) → [`00ac9c14`](#insn-00ac9c14)
- ブロック [`00ac9c14`](#insn-00ac9c14) 範囲 `[['00ac9c14', '00ac9c17']]`

## 命令位置別の参照

- [`00ac9aec`](#insn-00ac9aec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9af0`](#insn-00ac9af0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9af4`](#insn-00ac9af4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9af8`](#insn-00ac9af8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9afc`](#insn-00ac9afc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b14`](#insn-00ac9b14) → [`00ac9b74`](#insn-00ac9b74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b2c`](#insn-00ac9b2c) → [`00ac9c0c`](#insn-00ac9c0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b50`](#insn-00ac9b50) → [`00ac9b98`](#insn-00ac9b98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b58`](#insn-00ac9b58) → [`00ac9c14`](#insn-00ac9c14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b64`](#insn-00ac9b64) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b70`](#insn-00ac9b70) → [`00ac9b9c`](#insn-00ac9b9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b74`](#insn-00ac9b74) → [`00ac9b90`](#insn-00ac9b90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b88`](#insn-00ac9b88) → [`00bdb1f0`](../00bdb/00bdb1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1f0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b94`](#insn-00ac9b94) → [`00ac9bf4`](#insn-00ac9bf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bb4`](#insn-00ac9bb4) → [`00bdb1f0`](../00bdb/00bdb1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1f0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bc8`](#insn-00ac9bc8) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bd4`](#insn-00ac9bd4) → [`00ac9bf4`](#insn-00ac9bf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bdc`](#insn-00ac9bdc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9be0`](#insn-00ac9be0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9be4`](#insn-00ac9be4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9be8`](#insn-00ac9be8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bec`](#insn-00ac9bec) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bf0`](#insn-00ac9bf0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bf4`](#insn-00ac9bf4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bf8`](#insn-00ac9bf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bfc`](#insn-00ac9bfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c00`](#insn-00ac9c00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c04`](#insn-00ac9c04) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c10`](#insn-00ac9c10) → [`00729118`](../00729/00729118.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00729118` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c14`](#insn-00ac9c14) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac9aec`](#insn-00ac9aec)

~~~json
{
  "source": "00ac9aec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9af0`](#insn-00ac9af0)

~~~json
{
  "source": "00ac9af0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9af4`](#insn-00ac9af4)

~~~json
{
  "source": "00ac9af4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9af8`](#insn-00ac9af8)

~~~json
{
  "source": "00ac9af8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9afc`](#insn-00ac9afc)

~~~json
{
  "source": "00ac9afc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b14`](#insn-00ac9b14)

~~~json
{
  "source": "00ac9b14",
  "target": "00ac9b74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b2c`](#insn-00ac9b2c)

~~~json
{
  "source": "00ac9b2c",
  "target": "00ac9c0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b50`](#insn-00ac9b50)

~~~json
{
  "source": "00ac9b50",
  "target": "00ac9b98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b58`](#insn-00ac9b58)

~~~json
{
  "source": "00ac9b58",
  "target": "00ac9c14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b64`](#insn-00ac9b64)

~~~json
{
  "source": "00ac9b64",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9b70`](#insn-00ac9b70)

~~~json
{
  "source": "00ac9b70",
  "target": "00ac9b9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b74`](#insn-00ac9b74)

~~~json
{
  "source": "00ac9b74",
  "target": "00ac9b90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b88`](#insn-00ac9b88)

~~~json
{
  "source": "00ac9b88",
  "target": "00bdb1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9b94`](#insn-00ac9b94)

~~~json
{
  "source": "00ac9b94",
  "target": "00ac9bf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bb4`](#insn-00ac9bb4)

~~~json
{
  "source": "00ac9bb4",
  "target": "00bdb1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9bc8`](#insn-00ac9bc8)

~~~json
{
  "source": "00ac9bc8",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9bd4`](#insn-00ac9bd4)

~~~json
{
  "source": "00ac9bd4",
  "target": "00ac9bf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bdc`](#insn-00ac9bdc)

~~~json
{
  "source": "00ac9bdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9be0`](#insn-00ac9be0)

~~~json
{
  "source": "00ac9be0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9be4`](#insn-00ac9be4)

~~~json
{
  "source": "00ac9be4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9be8`](#insn-00ac9be8)

~~~json
{
  "source": "00ac9be8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bec`](#insn-00ac9bec)

~~~json
{
  "source": "00ac9bec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bf0`](#insn-00ac9bf0)

~~~json
{
  "source": "00ac9bf0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9bf4`](#insn-00ac9bf4)

~~~json
{
  "source": "00ac9bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bf8`](#insn-00ac9bf8)

~~~json
{
  "source": "00ac9bf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bfc`](#insn-00ac9bfc)

~~~json
{
  "source": "00ac9bfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c00`](#insn-00ac9c00)

~~~json
{
  "source": "00ac9c00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c04`](#insn-00ac9c04)

~~~json
{
  "source": "00ac9c04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c10`](#insn-00ac9c10)

~~~json
{
  "source": "00ac9c10",
  "target": "00729118",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c14`](#insn-00ac9c14)

~~~json
{
  "source": "00ac9c14",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
