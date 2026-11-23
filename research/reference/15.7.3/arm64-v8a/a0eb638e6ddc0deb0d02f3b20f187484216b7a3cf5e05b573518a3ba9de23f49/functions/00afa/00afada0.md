# 00afada0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afacd8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afacd8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-498d48ba861e874d8c0d572ea0d4ea4e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afade4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afade4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-acdbb2b39beee29b069c43cb094d672d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afada0",
  "name": "_ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03b61cd3c8c0321e848bf6cf48449bce4150e5eb3a52ce31668952c2453e97fc",
  "source_text_sha256": "03b61cd3c8c0321e848bf6cf48449bce4150e5eb3a52ce31668952c2453e97fc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afada0",
        "00afae87"
      ]
    ],
    "bytes_sha256": "47cc52a5d1b46d952fa61a8d410f6dfad43b656de7375be274c5beb9656c9133",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde970](../00bde/00bde970.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde270](../00bde/00bde270.md)

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
  
                    /* try { // try from 00afadac to 00bfadb3 has its CatchHandler @ 00aff504 */
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
LAB_00afae04:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* try { // try from 00afaddc to 00bfadef has its CatchHandler @ 00aff500 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00afae18;
    }
                    /* try { // try from 00afae00 to 00bfae07 has its CatchHandler @ 00aff4fc */
    if (uVar3 >> 0x3d != 0) goto LAB_00afae04;
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00afae18:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
                    /* try { // try from 00afae30 to 00bfae43 has its CatchHandler @ 00aff4f8 */
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00afae64 to 00bfae6b has its CatchHandler @ 00aff4f4 */
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
<a id="insn-00afada0"></a> `00afada0` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afada4"></a> `00afada4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afada8"></a> `00afada8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afadac"></a> `00afadac` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afadb0"></a> `00afadb0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afadb4"></a> `00afadb4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afadb8"></a> `00afadb8` | `13 20 40 a9` | ldp x19,x8,[x0] | `FALL_THROUGH`
<a id="insn-00afadbc"></a> `00afadbc` | `15 01 13 cb` | sub x21,x8,x19 | `FALL_THROUGH`
<a id="insn-00afadc0"></a> `00afadc0` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00afadc4"></a> `00afadc4` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00afadc8"></a> `00afadc8` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00afadcc"></a> `00afadcc` | `c9 01 00 b5` | cbnz x9,0x00afae04 | `CONDITIONAL_JUMP`
<a id="insn-00afadd0"></a> `00afadd0` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afadd4"></a> `00afadd4` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00afadd8"></a> `00afadd8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afaddc"></a> `00afaddc` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00afade0"></a> `00afade0` | `29 01 13 cb` | sub x9,x9,x19 | `FALL_THROUGH`
<a id="insn-00afade4"></a> `00afade4` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00afade8"></a> `00afade8` | `03 01 00 54` | b.cc 0x00afae08 | `CONDITIONAL_JUMP`
<a id="insn-00afadec"></a> `00afadec` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00afadf0"></a> `00afadf0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00afadf4"></a> `00afadf4` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00afadf8"></a> `00afadf8` | `59 04 00 b4` | cbz x25,0x00afae80 | `CONDITIONAL_JUMP`
<a id="insn-00afadfc"></a> `00afadfc` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00afae00"></a> `00afae00` | `68 00 00 b4` | cbz x8,0x00afae0c | `CONDITIONAL_JUMP`
<a id="insn-00afae04"></a> `00afae04` | `1b 8d 03 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00afae08"></a> `00afae08` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00afae0c"></a> `00afae0c` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00afae10"></a> `00afae10` | `78 80 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afae14"></a> `00afae14` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00afae18"></a> `00afae18` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afae1c"></a> `00afae1c` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00afae20"></a> `00afae20` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00afae24"></a> `00afae24` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00afae28"></a> `00afae28` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00afae2c"></a> `00afae2c` | `ab 00 00 54` | b.lt 0x00afae40 | `CONDITIONAL_JUMP`
<a id="insn-00afae30"></a> `00afae30` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00afae34"></a> `00afae34` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00afae38"></a> `00afae38` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00afae3c"></a> `00afae3c` | `c9 80 03 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00afae40"></a> `00afae40` | `97 62 00 a9` | stp x23,x24,[x20] | `FALL_THROUGH`
<a id="insn-00afae44"></a> `00afae44` | `96 0a 00 f9` | str x22,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afae48"></a> `00afae48` | `13 01 00 b4` | cbz x19,0x00afae68 | `CONDITIONAL_JUMP`
<a id="insn-00afae4c"></a> `00afae4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afae50"></a> `00afae50` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afae54"></a> `00afae54` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afae58"></a> `00afae58` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afae5c"></a> `00afae5c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afae60"></a> `00afae60` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afae64"></a> `00afae64` | `6b 80 03 14` | b 0x00bdb010 | `CALL_TERMINATOR`
<a id="insn-00afae68"></a> `00afae68` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afae6c"></a> `00afae6c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afae70"></a> `00afae70` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afae74"></a> `00afae74` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afae78"></a> `00afae78` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afae7c"></a> `00afae7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afae80"></a> `00afae80` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00afae84"></a> `00afae84` | `e5 ff ff 17` | b 0x00afae18 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afada0`](#insn-00afada0) 範囲 `[['00afada0', '00afadab']]`
  - `FALL_THROUGH` [`00afada8`](#insn-00afada8) → [`00afadac`](#insn-00afadac)
- ブロック [`00afadac`](#insn-00afadac) 範囲 `[['00afadac', '00afadcf']]`
  - `CONDITIONAL_JUMP` [`00afadcc`](#insn-00afadcc) → [`00afae04`](#insn-00afae04)
  - `FALL_THROUGH` [`00afadcc`](#insn-00afadcc) → [`00afadd0`](#insn-00afadd0)
- ブロック [`00afadd0`](#insn-00afadd0) 範囲 `[['00afadd0', '00afaddb']]`
  - `FALL_THROUGH` [`00afadd8`](#insn-00afadd8) → [`00afaddc`](#insn-00afaddc)
- ブロック [`00afaddc`](#insn-00afaddc) 範囲 `[['00afaddc', '00afadeb']]`
  - `CONDITIONAL_JUMP` [`00afade8`](#insn-00afade8) → [`00afae08`](#insn-00afae08)
  - `FALL_THROUGH` [`00afade8`](#insn-00afade8) → [`00afadec`](#insn-00afadec)
- ブロック [`00afadec`](#insn-00afadec) 範囲 `[['00afadec', '00afadfb']]`
  - `CONDITIONAL_JUMP` [`00afadf8`](#insn-00afadf8) → [`00afae80`](#insn-00afae80)
  - `FALL_THROUGH` [`00afadf8`](#insn-00afadf8) → [`00afadfc`](#insn-00afadfc)
- ブロック [`00afadfc`](#insn-00afadfc) 範囲 `[['00afadfc', '00afadff']]`
  - `FALL_THROUGH` [`00afadfc`](#insn-00afadfc) → [`00afae00`](#insn-00afae00)
- ブロック [`00afae00`](#insn-00afae00) 範囲 `[['00afae00', '00afae03']]`
  - `CONDITIONAL_JUMP` [`00afae00`](#insn-00afae00) → [`00afae0c`](#insn-00afae0c)
  - `FALL_THROUGH` [`00afae00`](#insn-00afae00) → [`00afae04`](#insn-00afae04)
- ブロック [`00afae04`](#insn-00afae04) 範囲 `[['00afae04', '00afae07']]`
- ブロック [`00afae08`](#insn-00afae08) 範囲 `[['00afae08', '00afae0b']]`
  - `FALL_THROUGH` [`00afae08`](#insn-00afae08) → [`00afae0c`](#insn-00afae0c)
- ブロック [`00afae0c`](#insn-00afae0c) 範囲 `[['00afae0c', '00afae17']]`
  - `FALL_THROUGH` [`00afae14`](#insn-00afae14) → [`00afae18`](#insn-00afae18)
- ブロック [`00afae18`](#insn-00afae18) 範囲 `[['00afae18', '00afae2f']]`
  - `CONDITIONAL_JUMP` [`00afae2c`](#insn-00afae2c) → [`00afae40`](#insn-00afae40)
  - `FALL_THROUGH` [`00afae2c`](#insn-00afae2c) → [`00afae30`](#insn-00afae30)
- ブロック [`00afae30`](#insn-00afae30) 範囲 `[['00afae30', '00afae3f']]`
  - `FALL_THROUGH` [`00afae3c`](#insn-00afae3c) → [`00afae40`](#insn-00afae40)
- ブロック [`00afae40`](#insn-00afae40) 範囲 `[['00afae40', '00afae4b']]`
  - `CONDITIONAL_JUMP` [`00afae48`](#insn-00afae48) → [`00afae68`](#insn-00afae68)
  - `FALL_THROUGH` [`00afae48`](#insn-00afae48) → [`00afae4c`](#insn-00afae4c)
- ブロック [`00afae4c`](#insn-00afae4c) 範囲 `[['00afae4c', '00afae63']]`
  - `FALL_THROUGH` [`00afae60`](#insn-00afae60) → [`00afae64`](#insn-00afae64)
- ブロック [`00afae64`](#insn-00afae64) 範囲 `[['00afae64', '00afae67']]`
- ブロック [`00afae68`](#insn-00afae68) 範囲 `[['00afae68', '00afae7f']]`
- ブロック [`00afae80`](#insn-00afae80) 範囲 `[['00afae80', '00afae87']]`
  - `UNCONDITIONAL_JUMP` [`00afae84`](#insn-00afae84) → [`00afae18`](#insn-00afae18)

## 命令位置別の参照

- [`00afada0`](#insn-00afada0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afada4`](#insn-00afada4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afada8`](#insn-00afada8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadac`](#insn-00afadac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadb0`](#insn-00afadb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadcc`](#insn-00afadcc) → [`00afae04`](#insn-00afae04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afade8`](#insn-00afade8) → [`00afae08`](#insn-00afae08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadf8`](#insn-00afadf8) → [`00afae80`](#insn-00afae80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae00`](#insn-00afae00) → [`00afae0c`](#insn-00afae0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae04`](#insn-00afae04) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00afae10`](#insn-00afae10) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afae2c`](#insn-00afae2c) → [`00afae40`](#insn-00afae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae3c`](#insn-00afae3c) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00afae48`](#insn-00afae48) → [`00afae68`](#insn-00afae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae50`](#insn-00afae50) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae54`](#insn-00afae54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae58`](#insn-00afae58) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae5c`](#insn-00afae5c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae64`](#insn-00afae64) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afae68`](#insn-00afae68) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae6c`](#insn-00afae6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae70`](#insn-00afae70) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae74`](#insn-00afae74) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae84`](#insn-00afae84) → [`00afae18`](#insn-00afae18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afada0`](#insn-00afada0)

~~~json
{
  "source": "00afada0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afada4`](#insn-00afada4)

~~~json
{
  "source": "00afada4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afada8`](#insn-00afada8)

~~~json
{
  "source": "00afada8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadac`](#insn-00afadac)

~~~json
{
  "source": "00afadac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadb0`](#insn-00afadb0)

~~~json
{
  "source": "00afadb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadcc`](#insn-00afadcc)

~~~json
{
  "source": "00afadcc",
  "target": "00afae04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afade8`](#insn-00afade8)

~~~json
{
  "source": "00afade8",
  "target": "00afae08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadf8`](#insn-00afadf8)

~~~json
{
  "source": "00afadf8",
  "target": "00afae80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae00`](#insn-00afae00)

~~~json
{
  "source": "00afae00",
  "target": "00afae0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae04`](#insn-00afae04)

~~~json
{
  "source": "00afae04",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae10`](#insn-00afae10)

~~~json
{
  "source": "00afae10",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae2c`](#insn-00afae2c)

~~~json
{
  "source": "00afae2c",
  "target": "00afae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae3c`](#insn-00afae3c)

~~~json
{
  "source": "00afae3c",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae48`](#insn-00afae48)

~~~json
{
  "source": "00afae48",
  "target": "00afae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae50`](#insn-00afae50)

~~~json
{
  "source": "00afae50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae54`](#insn-00afae54)

~~~json
{
  "source": "00afae54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae58`](#insn-00afae58)

~~~json
{
  "source": "00afae58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae5c`](#insn-00afae5c)

~~~json
{
  "source": "00afae5c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae64`](#insn-00afae64)

~~~json
{
  "source": "00afae64",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae68`](#insn-00afae68)

~~~json
{
  "source": "00afae68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae6c`](#insn-00afae6c)

~~~json
{
  "source": "00afae6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae70`](#insn-00afae70)

~~~json
{
  "source": "00afae70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae74`](#insn-00afae74)

~~~json
{
  "source": "00afae74",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae84`](#insn-00afae84)

~~~json
{
  "source": "00afae84",
  "target": "00afae18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
