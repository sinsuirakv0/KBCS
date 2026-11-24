# 00afade4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afada0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afada0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-acdbb2b39beee29b069c43cb094d672d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5ab68`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ab68.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-8ee8066e3e503ad8a50acef278879f2e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afade4",
  "name": "_ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d39f10935733a974f6de213957010d2e06ff0997953d864b411f5dc06eb4b6a8",
  "source_text_sha256": "d39f10935733a974f6de213957010d2e06ff0997953d864b411f5dc06eb4b6a8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afade4",
        "00afaecb"
      ]
    ],
    "bytes_sha256": "b8f544cd7e9e05aa7bc3c030e93e0c3649565e324b62e0abe334584641ef1f6d",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde9c0](../00bde/00bde9c0.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1671 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *__src;
  void *__dest;
  ulong uVar2;
  size_t __n;
  ulong uVar3;
  
                    /* try { // try from 00afadf0 to 00bfadf7 has its CatchHandler @ 00aff548 */
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
LAB_00afae48:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* try { // try from 00afae20 to 00bfae33 has its CatchHandler @ 00aff544 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00afae5c;
    }
                    /* try { // try from 00afae44 to 00bfae4b has its CatchHandler @ 00aff540 */
    if (uVar3 >> 0x3d != 0) goto LAB_00afae48;
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00afae5c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
                    /* try { // try from 00afae74 to 00bfae87 has its CatchHandler @ 00aff53c */
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00afaea8 to 00bfaeaf has its CatchHandler @ 00aff538 */
    _ZdlPv(__src);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afade4"></a> `00afade4` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afade8"></a> `00afade8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afadec"></a> `00afadec` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afadf0"></a> `00afadf0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afadf4"></a> `00afadf4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afadf8"></a> `00afadf8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afadfc"></a> `00afadfc` | `13 20 40 a9` | ldp x19,x8,[x0] | `FALL_THROUGH`
<a id="insn-00afae00"></a> `00afae00` | `15 01 13 cb` | sub x21,x8,x19 | `FALL_THROUGH`
<a id="insn-00afae04"></a> `00afae04` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00afae08"></a> `00afae08` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00afae0c"></a> `00afae0c` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00afae10"></a> `00afae10` | `c9 01 00 b5` | cbnz x9,0x00afae48 | `CONDITIONAL_JUMP`
<a id="insn-00afae14"></a> `00afae14` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afae18"></a> `00afae18` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00afae1c"></a> `00afae1c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afae20"></a> `00afae20` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00afae24"></a> `00afae24` | `29 01 13 cb` | sub x9,x9,x19 | `FALL_THROUGH`
<a id="insn-00afae28"></a> `00afae28` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00afae2c"></a> `00afae2c` | `03 01 00 54` | b.cc 0x00afae4c | `CONDITIONAL_JUMP`
<a id="insn-00afae30"></a> `00afae30` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00afae34"></a> `00afae34` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00afae38"></a> `00afae38` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00afae3c"></a> `00afae3c` | `59 04 00 b4` | cbz x25,0x00afaec4 | `CONDITIONAL_JUMP`
<a id="insn-00afae40"></a> `00afae40` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00afae44"></a> `00afae44` | `68 00 00 b4` | cbz x8,0x00afae50 | `CONDITIONAL_JUMP`
<a id="insn-00afae48"></a> `00afae48` | `1e 8d 03 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00afae4c"></a> `00afae4c` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00afae50"></a> `00afae50` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00afae54"></a> `00afae54` | `7b 80 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00afae58"></a> `00afae58` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00afae5c"></a> `00afae5c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afae60"></a> `00afae60` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00afae64"></a> `00afae64` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00afae68"></a> `00afae68` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00afae6c"></a> `00afae6c` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00afae70"></a> `00afae70` | `ab 00 00 54` | b.lt 0x00afae84 | `CONDITIONAL_JUMP`
<a id="insn-00afae74"></a> `00afae74` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00afae78"></a> `00afae78` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00afae7c"></a> `00afae7c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00afae80"></a> `00afae80` | `cc 80 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afae84"></a> `00afae84` | `97 62 00 a9` | stp x23,x24,[x20] | `FALL_THROUGH`
<a id="insn-00afae88"></a> `00afae88` | `96 0a 00 f9` | str x22,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afae8c"></a> `00afae8c` | `13 01 00 b4` | cbz x19,0x00afaeac | `CONDITIONAL_JUMP`
<a id="insn-00afae90"></a> `00afae90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afae94"></a> `00afae94` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afae98"></a> `00afae98` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afae9c"></a> `00afae9c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaea0"></a> `00afaea0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaea4"></a> `00afaea4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afaea8"></a> `00afaea8` | `6e 80 03 14` | b 0x00bdb060 | `CALL_TERMINATOR`
<a id="insn-00afaeac"></a> `00afaeac` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afaeb0"></a> `00afaeb0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afaeb4"></a> `00afaeb4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaeb8"></a> `00afaeb8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaebc"></a> `00afaebc` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afaec0"></a> `00afaec0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afaec4"></a> `00afaec4` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00afaec8"></a> `00afaec8` | `e5 ff ff 17` | b 0x00afae5c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afade4`](#insn-00afade4) 範囲 `[['00afade4', '00afadef']]`
  - `FALL_THROUGH` [`00afadec`](#insn-00afadec) → [`00afadf0`](#insn-00afadf0)
- ブロック [`00afadf0`](#insn-00afadf0) 範囲 `[['00afadf0', '00afae13']]`
  - `CONDITIONAL_JUMP` [`00afae10`](#insn-00afae10) → [`00afae48`](#insn-00afae48)
  - `FALL_THROUGH` [`00afae10`](#insn-00afae10) → [`00afae14`](#insn-00afae14)
- ブロック [`00afae14`](#insn-00afae14) 範囲 `[['00afae14', '00afae1f']]`
  - `FALL_THROUGH` [`00afae1c`](#insn-00afae1c) → [`00afae20`](#insn-00afae20)
- ブロック [`00afae20`](#insn-00afae20) 範囲 `[['00afae20', '00afae2f']]`
  - `CONDITIONAL_JUMP` [`00afae2c`](#insn-00afae2c) → [`00afae4c`](#insn-00afae4c)
  - `FALL_THROUGH` [`00afae2c`](#insn-00afae2c) → [`00afae30`](#insn-00afae30)
- ブロック [`00afae30`](#insn-00afae30) 範囲 `[['00afae30', '00afae3f']]`
  - `CONDITIONAL_JUMP` [`00afae3c`](#insn-00afae3c) → [`00afaec4`](#insn-00afaec4)
  - `FALL_THROUGH` [`00afae3c`](#insn-00afae3c) → [`00afae40`](#insn-00afae40)
- ブロック [`00afae40`](#insn-00afae40) 範囲 `[['00afae40', '00afae43']]`
  - `FALL_THROUGH` [`00afae40`](#insn-00afae40) → [`00afae44`](#insn-00afae44)
- ブロック [`00afae44`](#insn-00afae44) 範囲 `[['00afae44', '00afae47']]`
  - `CONDITIONAL_JUMP` [`00afae44`](#insn-00afae44) → [`00afae50`](#insn-00afae50)
  - `FALL_THROUGH` [`00afae44`](#insn-00afae44) → [`00afae48`](#insn-00afae48)
- ブロック [`00afae48`](#insn-00afae48) 範囲 `[['00afae48', '00afae4b']]`
- ブロック [`00afae4c`](#insn-00afae4c) 範囲 `[['00afae4c', '00afae4f']]`
  - `FALL_THROUGH` [`00afae4c`](#insn-00afae4c) → [`00afae50`](#insn-00afae50)
- ブロック [`00afae50`](#insn-00afae50) 範囲 `[['00afae50', '00afae5b']]`
  - `FALL_THROUGH` [`00afae58`](#insn-00afae58) → [`00afae5c`](#insn-00afae5c)
- ブロック [`00afae5c`](#insn-00afae5c) 範囲 `[['00afae5c', '00afae73']]`
  - `CONDITIONAL_JUMP` [`00afae70`](#insn-00afae70) → [`00afae84`](#insn-00afae84)
  - `FALL_THROUGH` [`00afae70`](#insn-00afae70) → [`00afae74`](#insn-00afae74)
- ブロック [`00afae74`](#insn-00afae74) 範囲 `[['00afae74', '00afae83']]`
  - `FALL_THROUGH` [`00afae80`](#insn-00afae80) → [`00afae84`](#insn-00afae84)
- ブロック [`00afae84`](#insn-00afae84) 範囲 `[['00afae84', '00afae8f']]`
  - `CONDITIONAL_JUMP` [`00afae8c`](#insn-00afae8c) → [`00afaeac`](#insn-00afaeac)
  - `FALL_THROUGH` [`00afae8c`](#insn-00afae8c) → [`00afae90`](#insn-00afae90)
- ブロック [`00afae90`](#insn-00afae90) 範囲 `[['00afae90', '00afaea7']]`
  - `FALL_THROUGH` [`00afaea4`](#insn-00afaea4) → [`00afaea8`](#insn-00afaea8)
- ブロック [`00afaea8`](#insn-00afaea8) 範囲 `[['00afaea8', '00afaeab']]`
- ブロック [`00afaeac`](#insn-00afaeac) 範囲 `[['00afaeac', '00afaec3']]`
- ブロック [`00afaec4`](#insn-00afaec4) 範囲 `[['00afaec4', '00afaecb']]`
  - `UNCONDITIONAL_JUMP` [`00afaec8`](#insn-00afaec8) → [`00afae5c`](#insn-00afae5c)

## 命令位置別の参照

- [`00afade4`](#insn-00afade4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afade8`](#insn-00afade8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadec`](#insn-00afadec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadf0`](#insn-00afadf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadf4`](#insn-00afadf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae10`](#insn-00afae10) → [`00afae48`](#insn-00afae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae2c`](#insn-00afae2c) → [`00afae4c`](#insn-00afae4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae3c`](#insn-00afae3c) → [`00afaec4`](#insn-00afaec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae44`](#insn-00afae44) → [`00afae50`](#insn-00afae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae48`](#insn-00afae48) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00afae54`](#insn-00afae54) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00afae70`](#insn-00afae70) → [`00afae84`](#insn-00afae84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae80`](#insn-00afae80) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00afae8c`](#insn-00afae8c) → [`00afaeac`](#insn-00afaeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae94`](#insn-00afae94) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae98`](#insn-00afae98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae9c`](#insn-00afae9c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaea0`](#insn-00afaea0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaea8`](#insn-00afaea8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afaeac`](#insn-00afaeac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaeb0`](#insn-00afaeb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaeb4`](#insn-00afaeb4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaeb8`](#insn-00afaeb8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaec8`](#insn-00afaec8) → [`00afae5c`](#insn-00afae5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afade4`](#insn-00afade4)

~~~json
{
  "source": "00afade4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afade8`](#insn-00afade8)

~~~json
{
  "source": "00afade8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadec`](#insn-00afadec)

~~~json
{
  "source": "00afadec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadf0`](#insn-00afadf0)

~~~json
{
  "source": "00afadf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadf4`](#insn-00afadf4)

~~~json
{
  "source": "00afadf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae10`](#insn-00afae10)

~~~json
{
  "source": "00afae10",
  "target": "00afae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae2c`](#insn-00afae2c)

~~~json
{
  "source": "00afae2c",
  "target": "00afae4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae3c`](#insn-00afae3c)

~~~json
{
  "source": "00afae3c",
  "target": "00afaec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae44`](#insn-00afae44)

~~~json
{
  "source": "00afae44",
  "target": "00afae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae48`](#insn-00afae48)

~~~json
{
  "source": "00afae48",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae54`](#insn-00afae54)

~~~json
{
  "source": "00afae54",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae70`](#insn-00afae70)

~~~json
{
  "source": "00afae70",
  "target": "00afae84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae80`](#insn-00afae80)

~~~json
{
  "source": "00afae80",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae8c`](#insn-00afae8c)

~~~json
{
  "source": "00afae8c",
  "target": "00afaeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae94`](#insn-00afae94)

~~~json
{
  "source": "00afae94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae98`](#insn-00afae98)

~~~json
{
  "source": "00afae98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae9c`](#insn-00afae9c)

~~~json
{
  "source": "00afae9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaea0`](#insn-00afaea0)

~~~json
{
  "source": "00afaea0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaea8`](#insn-00afaea8)

~~~json
{
  "source": "00afaea8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaeac`](#insn-00afaeac)

~~~json
{
  "source": "00afaeac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaeb0`](#insn-00afaeb0)

~~~json
{
  "source": "00afaeb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaeb4`](#insn-00afaeb4)

~~~json
{
  "source": "00afaeb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaeb8`](#insn-00afaeb8)

~~~json
{
  "source": "00afaeb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaec8`](#insn-00afaec8)

~~~json
{
  "source": "00afaec8",
  "target": "00afae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
