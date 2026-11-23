# 00afacd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afada0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afada0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-498d48ba861e874d8c0d572ea0d4ea4e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afacd8",
  "name": "_ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e12a6bcddbcd7407504aadc17f491c3437d566b904cc37e9cf974260c6b311c0",
  "source_text_sha256": "e12a6bcddbcd7407504aadc17f491c3437d566b904cc37e9cf974260c6b311c0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afacd8",
        "00afadbf"
      ]
    ],
    "bytes_sha256": "f62deb6e769d50beefc535b7969566b4ea19066ec7b3ee75d1b8819334a3e4d2",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde8c0](../00bde/00bde8c0.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde1c0](../00bde/00bde1c0.md)

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
  
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
LAB_00afad3c:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* try { // try from 00afad10 to 00bfad23 has its CatchHandler @ 00aff510 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00afad50;
    }
                    /* try { // try from 00afad34 to 00bfad3b has its CatchHandler @ 00aff50c */
    if (uVar3 >> 0x3d != 0) goto LAB_00afad3c;
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00afad50:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
                    /* try { // try from 00afad64 to 00bfad77 has its CatchHandler @ 00aff508 */
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00afad88 to 00bfadab has its CatchHandler @ 00b0037c */
    _ZdlPv(__src);
    return;
  }
                    /* try { // try from 00afadac to 00bfadb3 has its CatchHandler @ 00aff504 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afacd8"></a> `00afacd8` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afacdc"></a> `00afacdc` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aface0"></a> `00aface0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aface4"></a> `00aface4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aface8"></a> `00aface8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afacec"></a> `00afacec` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afacf0"></a> `00afacf0` | `13 20 40 a9` | ldp x19,x8,[x0] | `FALL_THROUGH`
<a id="insn-00afacf4"></a> `00afacf4` | `15 01 13 cb` | sub x21,x8,x19 | `FALL_THROUGH`
<a id="insn-00afacf8"></a> `00afacf8` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00afacfc"></a> `00afacfc` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00afad00"></a> `00afad00` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00afad04"></a> `00afad04` | `c9 01 00 b5` | cbnz x9,0x00afad3c | `CONDITIONAL_JUMP`
<a id="insn-00afad08"></a> `00afad08` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afad0c"></a> `00afad0c` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00afad10"></a> `00afad10` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afad14"></a> `00afad14` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00afad18"></a> `00afad18` | `29 01 13 cb` | sub x9,x9,x19 | `FALL_THROUGH`
<a id="insn-00afad1c"></a> `00afad1c` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00afad20"></a> `00afad20` | `03 01 00 54` | b.cc 0x00afad40 | `CONDITIONAL_JUMP`
<a id="insn-00afad24"></a> `00afad24` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00afad28"></a> `00afad28` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00afad2c"></a> `00afad2c` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00afad30"></a> `00afad30` | `59 04 00 b4` | cbz x25,0x00afadb8 | `CONDITIONAL_JUMP`
<a id="insn-00afad34"></a> `00afad34` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00afad38"></a> `00afad38` | `68 00 00 b4` | cbz x8,0x00afad44 | `CONDITIONAL_JUMP`
<a id="insn-00afad3c"></a> `00afad3c` | `21 8d 03 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00afad40"></a> `00afad40` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00afad44"></a> `00afad44` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00afad48"></a> `00afad48` | `7e 80 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00afad4c"></a> `00afad4c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00afad50"></a> `00afad50` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afad54"></a> `00afad54` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00afad58"></a> `00afad58` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00afad5c"></a> `00afad5c` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00afad60"></a> `00afad60` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00afad64"></a> `00afad64` | `ab 00 00 54` | b.lt 0x00afad78 | `CONDITIONAL_JUMP`
<a id="insn-00afad68"></a> `00afad68` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00afad6c"></a> `00afad6c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00afad70"></a> `00afad70` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00afad74"></a> `00afad74` | `cf 80 03 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afad78"></a> `00afad78` | `97 62 00 a9` | stp x23,x24,[x20] | `FALL_THROUGH`
<a id="insn-00afad7c"></a> `00afad7c` | `96 0a 00 f9` | str x22,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afad80"></a> `00afad80` | `13 01 00 b4` | cbz x19,0x00afada0 | `CONDITIONAL_JUMP`
<a id="insn-00afad84"></a> `00afad84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afad88"></a> `00afad88` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afad8c"></a> `00afad8c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afad90"></a> `00afad90` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afad94"></a> `00afad94` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad98"></a> `00afad98` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afad9c"></a> `00afad9c` | `71 80 03 14` | b 0x00bdaf60 | `CALL_TERMINATOR`
<a id="insn-00afada0"></a> `00afada0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afada4"></a> `00afada4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afada8"></a> `00afada8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afadac"></a> `00afadac` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afadb0"></a> `00afadb0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afadb4"></a> `00afadb4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afadb8"></a> `00afadb8` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00afadbc"></a> `00afadbc` | `e5 ff ff 17` | b 0x00afad50 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afacd8`](#insn-00afacd8) 範囲 `[['00afacd8', '00afad07']]`
  - `CONDITIONAL_JUMP` [`00afad04`](#insn-00afad04) → [`00afad3c`](#insn-00afad3c)
  - `FALL_THROUGH` [`00afad04`](#insn-00afad04) → [`00afad08`](#insn-00afad08)
- ブロック [`00afad08`](#insn-00afad08) 範囲 `[['00afad08', '00afad0f']]`
  - `FALL_THROUGH` [`00afad0c`](#insn-00afad0c) → [`00afad10`](#insn-00afad10)
- ブロック [`00afad10`](#insn-00afad10) 範囲 `[['00afad10', '00afad23']]`
  - `CONDITIONAL_JUMP` [`00afad20`](#insn-00afad20) → [`00afad40`](#insn-00afad40)
  - `FALL_THROUGH` [`00afad20`](#insn-00afad20) → [`00afad24`](#insn-00afad24)
- ブロック [`00afad24`](#insn-00afad24) 範囲 `[['00afad24', '00afad33']]`
  - `CONDITIONAL_JUMP` [`00afad30`](#insn-00afad30) → [`00afadb8`](#insn-00afadb8)
  - `FALL_THROUGH` [`00afad30`](#insn-00afad30) → [`00afad34`](#insn-00afad34)
- ブロック [`00afad34`](#insn-00afad34) 範囲 `[['00afad34', '00afad3b']]`
  - `CONDITIONAL_JUMP` [`00afad38`](#insn-00afad38) → [`00afad44`](#insn-00afad44)
  - `FALL_THROUGH` [`00afad38`](#insn-00afad38) → [`00afad3c`](#insn-00afad3c)
- ブロック [`00afad3c`](#insn-00afad3c) 範囲 `[['00afad3c', '00afad3f']]`
- ブロック [`00afad40`](#insn-00afad40) 範囲 `[['00afad40', '00afad43']]`
  - `FALL_THROUGH` [`00afad40`](#insn-00afad40) → [`00afad44`](#insn-00afad44)
- ブロック [`00afad44`](#insn-00afad44) 範囲 `[['00afad44', '00afad4f']]`
  - `FALL_THROUGH` [`00afad4c`](#insn-00afad4c) → [`00afad50`](#insn-00afad50)
- ブロック [`00afad50`](#insn-00afad50) 範囲 `[['00afad50', '00afad63']]`
  - `FALL_THROUGH` [`00afad60`](#insn-00afad60) → [`00afad64`](#insn-00afad64)
- ブロック [`00afad64`](#insn-00afad64) 範囲 `[['00afad64', '00afad67']]`
  - `CONDITIONAL_JUMP` [`00afad64`](#insn-00afad64) → [`00afad78`](#insn-00afad78)
  - `FALL_THROUGH` [`00afad64`](#insn-00afad64) → [`00afad68`](#insn-00afad68)
- ブロック [`00afad68`](#insn-00afad68) 範囲 `[['00afad68', '00afad77']]`
  - `FALL_THROUGH` [`00afad74`](#insn-00afad74) → [`00afad78`](#insn-00afad78)
- ブロック [`00afad78`](#insn-00afad78) 範囲 `[['00afad78', '00afad83']]`
  - `CONDITIONAL_JUMP` [`00afad80`](#insn-00afad80) → [`00afada0`](#insn-00afada0)
  - `FALL_THROUGH` [`00afad80`](#insn-00afad80) → [`00afad84`](#insn-00afad84)
- ブロック [`00afad84`](#insn-00afad84) 範囲 `[['00afad84', '00afad87']]`
  - `FALL_THROUGH` [`00afad84`](#insn-00afad84) → [`00afad88`](#insn-00afad88)
- ブロック [`00afad88`](#insn-00afad88) 範囲 `[['00afad88', '00afad9f']]`
- ブロック [`00afada0`](#insn-00afada0) 範囲 `[['00afada0', '00afadab']]`
  - `FALL_THROUGH` [`00afada8`](#insn-00afada8) → [`00afadac`](#insn-00afadac)
- ブロック [`00afadac`](#insn-00afadac) 範囲 `[['00afadac', '00afadb7']]`
- ブロック [`00afadb8`](#insn-00afadb8) 範囲 `[['00afadb8', '00afadbf']]`
  - `UNCONDITIONAL_JUMP` [`00afadbc`](#insn-00afadbc) → [`00afad50`](#insn-00afad50)

## 命令位置別の参照

- [`00afacd8`](#insn-00afacd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacdc`](#insn-00afacdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aface0`](#insn-00aface0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aface4`](#insn-00aface4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aface8`](#insn-00aface8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad04`](#insn-00afad04) → [`00afad3c`](#insn-00afad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad20`](#insn-00afad20) → [`00afad40`](#insn-00afad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad30`](#insn-00afad30) → [`00afadb8`](#insn-00afadb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad38`](#insn-00afad38) → [`00afad44`](#insn-00afad44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad3c`](#insn-00afad3c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00afad48`](#insn-00afad48) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00afad64`](#insn-00afad64) → [`00afad78`](#insn-00afad78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad74`](#insn-00afad74) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00afad80`](#insn-00afad80) → [`00afada0`](#insn-00afada0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad88`](#insn-00afad88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad8c`](#insn-00afad8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad90`](#insn-00afad90) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad94`](#insn-00afad94) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad9c`](#insn-00afad9c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afada0`](#insn-00afada0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afada4`](#insn-00afada4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afada8`](#insn-00afada8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadac`](#insn-00afadac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadbc`](#insn-00afadbc) → [`00afad50`](#insn-00afad50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afacd8`](#insn-00afacd8)

~~~json
{
  "source": "00afacd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacdc`](#insn-00afacdc)

~~~json
{
  "source": "00afacdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aface0`](#insn-00aface0)

~~~json
{
  "source": "00aface0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aface4`](#insn-00aface4)

~~~json
{
  "source": "00aface4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aface8`](#insn-00aface8)

~~~json
{
  "source": "00aface8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad04`](#insn-00afad04)

~~~json
{
  "source": "00afad04",
  "target": "00afad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad20`](#insn-00afad20)

~~~json
{
  "source": "00afad20",
  "target": "00afad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad30`](#insn-00afad30)

~~~json
{
  "source": "00afad30",
  "target": "00afadb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad38`](#insn-00afad38)

~~~json
{
  "source": "00afad38",
  "target": "00afad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad3c`](#insn-00afad3c)

~~~json
{
  "source": "00afad3c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad48`](#insn-00afad48)

~~~json
{
  "source": "00afad48",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad64`](#insn-00afad64)

~~~json
{
  "source": "00afad64",
  "target": "00afad78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad74`](#insn-00afad74)

~~~json
{
  "source": "00afad74",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad80`](#insn-00afad80)

~~~json
{
  "source": "00afad80",
  "target": "00afada0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad88`](#insn-00afad88)

~~~json
{
  "source": "00afad88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad8c`](#insn-00afad8c)

~~~json
{
  "source": "00afad8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad90`](#insn-00afad90)

~~~json
{
  "source": "00afad90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad94`](#insn-00afad94)

~~~json
{
  "source": "00afad94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad9c`](#insn-00afad9c)

~~~json
{
  "source": "00afad9c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afada0`](#insn-00afada0)

~~~json
{
  "source": "00afada0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afada4`](#insn-00afada4)

~~~json
{
  "source": "00afada4",
  "target": "Stack[-0x20]",
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
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadbc`](#insn-00afadbc)

~~~json
{
  "source": "00afadbc",
  "target": "00afad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
