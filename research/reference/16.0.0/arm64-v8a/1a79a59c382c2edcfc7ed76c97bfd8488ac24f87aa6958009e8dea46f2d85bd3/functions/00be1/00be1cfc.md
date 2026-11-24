# 00be1cfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b727fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b727fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-45fc3192f9992ffa931ca0b6dbb9a0e2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00be2124`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2124.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-00e0829caf4190bffaa3ba833882cc62)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00be1cfc",
  "name": "_ZN8firebase4auth17UserInfoInterfaceD2Ev",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94843f119f6eba4cbf94e4badf54b64940161807c39c6338456ff5e6ecbe1f7f",
  "source_text_sha256": "94843f119f6eba4cbf94e4badf54b64940161807c39c6338456ff5e6ecbe1f7f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00be1cfc",
        "00be1db7"
      ]
    ],
    "bytes_sha256": "e6f3c6b936fed240531faa22d0416683450c7fc8edbc0b8d92ef9342dbf3e2c5",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d770](../00c5d/00c5d770.md)
- [00c5d780](../00c5d/00c5d780.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1019 bytes

~~~c

void _ZN8firebase4auth17UserInfoInterfaceD2Ev(long *param_1)

{
  byte bVar1;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17UserInfoInterfaceE_00c9b5c8 + 0x10);
  if ((*(byte *)(param_1 + 0x10) & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0xd);
  }
  else {
    _ZdlPv((void *)param_1[0x12]);
    bVar1 = *(byte *)(param_1 + 0xd);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 10);
  }
  else {
    _ZdlPv((void *)param_1[0xf]);
    bVar1 = *(byte *)(param_1 + 10);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 7);
  }
  else {
    _ZdlPv((void *)param_1[0xc]);
    bVar1 = *(byte *)(param_1 + 7);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 4);
  }
  else {
    _ZdlPv((void *)param_1[9]);
    bVar1 = *(byte *)(param_1 + 4);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 1);
  }
  else {
    _ZdlPv((void *)param_1[6]);
    bVar1 = *(byte *)(param_1 + 1);
  }
  if ((bVar1 & 1) != 0) {
    _ZdlPv((void *)param_1[3]);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00be1cfc"></a> `00be1cfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00be1d00"></a> `00be1d00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00be1d04"></a> `00be1d04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00be1d08"></a> `00be1d08` | `c9 05 00 d0` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-00be1d0c"></a> `00be1d0c` | `08 00 42 39` | ldrb w8,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00be1d10"></a> `00be1d10` | `29 e5 42 f9` | ldr x9,[x9, #0x5c8] | `FALL_THROUGH`
<a id="insn-00be1d14"></a> `00be1d14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00be1d18"></a> `00be1d18` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00be1d1c"></a> `00be1d1c` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00be1d20"></a> `00be1d20` | `c8 01 00 37` | tbnz w8,#0x0,0x00be1d58 | `CONDITIONAL_JUMP`
<a id="insn-00be1d24"></a> `00be1d24` | `68 a2 41 39` | ldrb w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00be1d28"></a> `00be1d28` | `08 02 00 37` | tbnz w8,#0x0,0x00be1d68 | `CONDITIONAL_JUMP`
<a id="insn-00be1d2c"></a> `00be1d2c` | `68 42 41 39` | ldrb w8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00be1d30"></a> `00be1d30` | `48 02 00 37` | tbnz w8,#0x0,0x00be1d78 | `CONDITIONAL_JUMP`
<a id="insn-00be1d34"></a> `00be1d34` | `68 e2 40 39` | ldrb w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00be1d38"></a> `00be1d38` | `88 02 00 37` | tbnz w8,#0x0,0x00be1d88 | `CONDITIONAL_JUMP`
<a id="insn-00be1d3c"></a> `00be1d3c` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00be1d40"></a> `00be1d40` | `c8 02 00 37` | tbnz w8,#0x0,0x00be1d98 | `CONDITIONAL_JUMP`
<a id="insn-00be1d44"></a> `00be1d44` | `68 22 40 39` | ldrb w8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00be1d48"></a> `00be1d48` | `08 03 00 37` | tbnz w8,#0x0,0x00be1da8 | `CONDITIONAL_JUMP`
<a id="insn-00be1d4c"></a> `00be1d4c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00be1d50"></a> `00be1d50` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00be1d54"></a> `00be1d54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00be1d58"></a> `00be1d58` | `60 4a 40 f9` | ldr x0,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00be1d5c"></a> `00be1d5c` | `55 d7 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00be1d60"></a> `00be1d60` | `68 a2 41 39` | ldrb w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00be1d64"></a> `00be1d64` | `48 fe 07 36` | tbz w8,#0x0,0x00be1d2c | `CONDITIONAL_JUMP`
<a id="insn-00be1d68"></a> `00be1d68` | `60 3e 40 f9` | ldr x0,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00be1d6c"></a> `00be1d6c` | `51 d7 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00be1d70"></a> `00be1d70` | `68 42 41 39` | ldrb w8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00be1d74"></a> `00be1d74` | `08 fe 07 36` | tbz w8,#0x0,0x00be1d34 | `CONDITIONAL_JUMP`
<a id="insn-00be1d78"></a> `00be1d78` | `60 32 40 f9` | ldr x0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00be1d7c"></a> `00be1d7c` | `4d d7 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00be1d80"></a> `00be1d80` | `68 e2 40 39` | ldrb w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00be1d84"></a> `00be1d84` | `c8 fd 07 36` | tbz w8,#0x0,0x00be1d3c | `CONDITIONAL_JUMP`
<a id="insn-00be1d88"></a> `00be1d88` | `60 26 40 f9` | ldr x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00be1d8c"></a> `00be1d8c` | `49 d7 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00be1d90"></a> `00be1d90` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00be1d94"></a> `00be1d94` | `88 fd 07 36` | tbz w8,#0x0,0x00be1d44 | `CONDITIONAL_JUMP`
<a id="insn-00be1d98"></a> `00be1d98` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00be1d9c"></a> `00be1d9c` | `45 d7 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00be1da0"></a> `00be1da0` | `68 22 40 39` | ldrb w8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00be1da4"></a> `00be1da4` | `48 fd 07 36` | tbz w8,#0x0,0x00be1d4c | `CONDITIONAL_JUMP`
<a id="insn-00be1da8"></a> `00be1da8` | `60 0e 40 f9` | ldr x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00be1dac"></a> `00be1dac` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00be1db0"></a> `00be1db0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00be1db4"></a> `00be1db4` | `3f d7 01 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00be1cfc`](#insn-00be1cfc) 範囲 `[['00be1cfc', '00be1d23']]`
  - `CONDITIONAL_JUMP` [`00be1d20`](#insn-00be1d20) → [`00be1d58`](#insn-00be1d58)
  - `FALL_THROUGH` [`00be1d20`](#insn-00be1d20) → [`00be1d24`](#insn-00be1d24)
- ブロック [`00be1d24`](#insn-00be1d24) 範囲 `[['00be1d24', '00be1d2b']]`
  - `CONDITIONAL_JUMP` [`00be1d28`](#insn-00be1d28) → [`00be1d68`](#insn-00be1d68)
  - `FALL_THROUGH` [`00be1d28`](#insn-00be1d28) → [`00be1d2c`](#insn-00be1d2c)
- ブロック [`00be1d2c`](#insn-00be1d2c) 範囲 `[['00be1d2c', '00be1d33']]`
  - `CONDITIONAL_JUMP` [`00be1d30`](#insn-00be1d30) → [`00be1d78`](#insn-00be1d78)
  - `FALL_THROUGH` [`00be1d30`](#insn-00be1d30) → [`00be1d34`](#insn-00be1d34)
- ブロック [`00be1d34`](#insn-00be1d34) 範囲 `[['00be1d34', '00be1d3b']]`
  - `CONDITIONAL_JUMP` [`00be1d38`](#insn-00be1d38) → [`00be1d88`](#insn-00be1d88)
  - `FALL_THROUGH` [`00be1d38`](#insn-00be1d38) → [`00be1d3c`](#insn-00be1d3c)
- ブロック [`00be1d3c`](#insn-00be1d3c) 範囲 `[['00be1d3c', '00be1d43']]`
  - `CONDITIONAL_JUMP` [`00be1d40`](#insn-00be1d40) → [`00be1d98`](#insn-00be1d98)
  - `FALL_THROUGH` [`00be1d40`](#insn-00be1d40) → [`00be1d44`](#insn-00be1d44)
- ブロック [`00be1d44`](#insn-00be1d44) 範囲 `[['00be1d44', '00be1d4b']]`
  - `CONDITIONAL_JUMP` [`00be1d48`](#insn-00be1d48) → [`00be1da8`](#insn-00be1da8)
  - `FALL_THROUGH` [`00be1d48`](#insn-00be1d48) → [`00be1d4c`](#insn-00be1d4c)
- ブロック [`00be1d4c`](#insn-00be1d4c) 範囲 `[['00be1d4c', '00be1d57']]`
- ブロック [`00be1d58`](#insn-00be1d58) 範囲 `[['00be1d58', '00be1d67']]`
  - `CONDITIONAL_JUMP` [`00be1d64`](#insn-00be1d64) → [`00be1d2c`](#insn-00be1d2c)
  - `FALL_THROUGH` [`00be1d64`](#insn-00be1d64) → [`00be1d68`](#insn-00be1d68)
- ブロック [`00be1d68`](#insn-00be1d68) 範囲 `[['00be1d68', '00be1d77']]`
  - `CONDITIONAL_JUMP` [`00be1d74`](#insn-00be1d74) → [`00be1d34`](#insn-00be1d34)
  - `FALL_THROUGH` [`00be1d74`](#insn-00be1d74) → [`00be1d78`](#insn-00be1d78)
- ブロック [`00be1d78`](#insn-00be1d78) 範囲 `[['00be1d78', '00be1d87']]`
  - `CONDITIONAL_JUMP` [`00be1d84`](#insn-00be1d84) → [`00be1d3c`](#insn-00be1d3c)
  - `FALL_THROUGH` [`00be1d84`](#insn-00be1d84) → [`00be1d88`](#insn-00be1d88)
- ブロック [`00be1d88`](#insn-00be1d88) 範囲 `[['00be1d88', '00be1d97']]`
  - `CONDITIONAL_JUMP` [`00be1d94`](#insn-00be1d94) → [`00be1d44`](#insn-00be1d44)
  - `FALL_THROUGH` [`00be1d94`](#insn-00be1d94) → [`00be1d98`](#insn-00be1d98)
- ブロック [`00be1d98`](#insn-00be1d98) 範囲 `[['00be1d98', '00be1da7']]`
  - `CONDITIONAL_JUMP` [`00be1da4`](#insn-00be1da4) → [`00be1d4c`](#insn-00be1d4c)
  - `FALL_THROUGH` [`00be1da4`](#insn-00be1da4) → [`00be1da8`](#insn-00be1da8)
- ブロック [`00be1da8`](#insn-00be1da8) 範囲 `[['00be1da8', '00be1db7']]`

## 命令位置別の参照

- [`00be1cfc`](#insn-00be1cfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d00`](#insn-00be1d00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d10`](#insn-00be1d10) → `00c9b5c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00be1d1c`](#insn-00be1d1c) → `00c92578`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00be1d20`](#insn-00be1d20) → [`00be1d58`](#insn-00be1d58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d28`](#insn-00be1d28) → [`00be1d68`](#insn-00be1d68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d30`](#insn-00be1d30) → [`00be1d78`](#insn-00be1d78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d38`](#insn-00be1d38) → [`00be1d88`](#insn-00be1d88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d40`](#insn-00be1d40) → [`00be1d98`](#insn-00be1d98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d48`](#insn-00be1d48) → [`00be1da8`](#insn-00be1da8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d4c`](#insn-00be1d4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d5c`](#insn-00be1d5c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00be1d64`](#insn-00be1d64) → [`00be1d2c`](#insn-00be1d2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d6c`](#insn-00be1d6c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00be1d74`](#insn-00be1d74) → [`00be1d34`](#insn-00be1d34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d7c`](#insn-00be1d7c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00be1d84`](#insn-00be1d84) → [`00be1d3c`](#insn-00be1d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d8c`](#insn-00be1d8c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00be1d94`](#insn-00be1d94) → [`00be1d44`](#insn-00be1d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1d9c`](#insn-00be1d9c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00be1da4`](#insn-00be1da4) → [`00be1d4c`](#insn-00be1d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1dac`](#insn-00be1dac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1db4`](#insn-00be1db4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00be1cfc`](#insn-00be1cfc)

~~~json
{
  "source": "00be1cfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d00`](#insn-00be1d00)

~~~json
{
  "source": "00be1d00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d10`](#insn-00be1d10)

~~~json
{
  "source": "00be1d10",
  "target": "00c9b5c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5c8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00be1d1c`](#insn-00be1d1c)

~~~json
{
  "source": "00be1d1c",
  "target": "00c92578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92568",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00be1d20`](#insn-00be1d20)

~~~json
{
  "source": "00be1d20",
  "target": "00be1d58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d28`](#insn-00be1d28)

~~~json
{
  "source": "00be1d28",
  "target": "00be1d68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d30`](#insn-00be1d30)

~~~json
{
  "source": "00be1d30",
  "target": "00be1d78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d38`](#insn-00be1d38)

~~~json
{
  "source": "00be1d38",
  "target": "00be1d88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d40`](#insn-00be1d40)

~~~json
{
  "source": "00be1d40",
  "target": "00be1d98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d48`](#insn-00be1d48)

~~~json
{
  "source": "00be1d48",
  "target": "00be1da8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d4c`](#insn-00be1d4c)

~~~json
{
  "source": "00be1d4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d5c`](#insn-00be1d5c)

~~~json
{
  "source": "00be1d5c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1d64`](#insn-00be1d64)

~~~json
{
  "source": "00be1d64",
  "target": "00be1d2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d6c`](#insn-00be1d6c)

~~~json
{
  "source": "00be1d6c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1d74`](#insn-00be1d74)

~~~json
{
  "source": "00be1d74",
  "target": "00be1d34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d7c`](#insn-00be1d7c)

~~~json
{
  "source": "00be1d7c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1d84`](#insn-00be1d84)

~~~json
{
  "source": "00be1d84",
  "target": "00be1d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d8c`](#insn-00be1d8c)

~~~json
{
  "source": "00be1d8c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1d94`](#insn-00be1d94)

~~~json
{
  "source": "00be1d94",
  "target": "00be1d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1d9c`](#insn-00be1d9c)

~~~json
{
  "source": "00be1d9c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1da4`](#insn-00be1da4)

~~~json
{
  "source": "00be1da4",
  "target": "00be1d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1dac`](#insn-00be1dac)

~~~json
{
  "source": "00be1dac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1db4`](#insn-00be1db4)

~~~json
{
  "source": "00be1db4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
