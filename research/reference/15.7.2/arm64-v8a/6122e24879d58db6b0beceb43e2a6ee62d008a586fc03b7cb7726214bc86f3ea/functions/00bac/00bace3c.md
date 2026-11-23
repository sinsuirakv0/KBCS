# 00bace3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bacf04`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bacf04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-8741a2601284e31c8d72618becddd6df)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bace3c",
  "name": "_ZNKSt6__ndk17codecvtIDiDu9mbstate_tE6do_outERS1_PKDiS5_RS5_PDuS7_RS7_",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a1dd0a0e081dd03e6553c6b5f1ecfb9f01d5158f72fbbf3ffa1acba62193a19",
  "source_text_sha256": "1a1dd0a0e081dd03e6553c6b5f1ecfb9f01d5158f72fbbf3ffa1acba62193a19",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bace3c",
        "00bacf63"
      ]
    ],
    "bytes_sha256": "8468392e62340af4eb6e393a2607e13abc7a968bf67d78c7ad8ed05232dc3bcf",
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

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2016 bytes

~~~c

undefined8
_ZNKSt6__ndk17codecvtIDiDu9mbstate_tE6do_outERS1_PKDiS5_RS5_PDuS7_RS7_
          (undefined8 param_1,undefined8 param_2,uint *param_3,uint *param_4,undefined8 *param_5,
          byte *param_6,long param_7,undefined8 *param_8)

{
  uint uVar1;
  byte bVar2;
  undefined8 uVar3;
  byte *pbVar4;
  
  do {
    if (param_4 <= param_3) {
      uVar3 = 0;
                    /* catch() { ... } // from try @ 00bacd90 with catch @ 00bacf48 */
LAB_00bacf58:
                    /* catch() { ... } // from try @ 00bace28 with catch @ 00bacf58 */
      *param_5 = param_3;
      *param_8 = param_6;
      return uVar3;
    }
    uVar1 = *param_3;
    if (0x10 < uVar1 >> 0x10 || (uVar1 & 0xfffff800) == 0xd800) {
      uVar3 = 2;
      goto LAB_00bacf58;
    }
                    /* try { // try from 00bace78 to 00cad07b has its CatchHandler @ 00bacc84 */
    bVar2 = (byte)uVar1;
    if (uVar1 < 0x80) {
      if (param_7 - (long)param_6 < 1) goto LAB_00bacf54;
      pbVar4 = param_6 + 1;
      *param_6 = bVar2;
    }
    else if (uVar1 < 0x800) {
      if (param_7 - (long)param_6 < 2) goto LAB_00bacf54;
      pbVar4 = param_6 + 2;
      *param_6 = (byte)(uVar1 >> 6) | 0xc0;
      param_6[1] = bVar2 & 0x3f | 0x80;
    }
    else if (uVar1 >> 0x10 == 0) {
      if (param_7 - (long)param_6 < 3) {
LAB_00bacf54:
        uVar3 = 1;
        goto LAB_00bacf58;
      }
      pbVar4 = param_6 + 3;
      *param_6 = (byte)(uVar1 >> 0xc) | 0xe0;
      param_6[1] = (byte)(uVar1 >> 6) & 0x3f | 0x80;
      param_6[2] = bVar2 & 0x3f | 0x80;
    }
    else {
      if (param_7 - (long)param_6 < 4) goto LAB_00bacf54;
      pbVar4 = param_6 + 4;
      *param_6 = (byte)(uVar1 >> 0x12) | 0xf0;
      param_6[1] = (byte)(uVar1 >> 0xc) & 0x3f | 0x80;
      param_6[2] = (byte)(uVar1 >> 6) & 0x3f | 0x80;
      param_6[3] = bVar2 & 0x3f | 0x80;
    }
                    /* try { // try from 00bace54 to 00cace77 has its CatchHandler @ 00bacff8 */
    param_3 = param_3 + 1;
    param_6 = pbVar4;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bace3c"></a> `00bace3c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bace40"></a> `00bace40` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bace44"></a> `00bace44` | `02 08 00 54` | b.cs 0x00bacf44 | `CONDITIONAL_JUMP`
<a id="insn-00bace48"></a> `00bace48` | `08 00 9b 52` | mov w8,#0xd800 | `FALL_THROUGH`
<a id="insn-00bace4c"></a> `00bace4c` | `05 00 00 14` | b 0x00bace60 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace50"></a> `00bace50` | `e5 03 09 aa` | mov x5,x9 | `FALL_THROUGH`
<a id="insn-00bace54"></a> `00bace54` | `42 10 00 91` | add x2,x2,#0x4 | `FALL_THROUGH`
<a id="insn-00bace58"></a> `00bace58` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bace5c"></a> `00bace5c` | `42 07 00 54` | b.cs 0x00bacf44 | `CONDITIONAL_JUMP`
<a id="insn-00bace60"></a> `00bace60` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-00bace64"></a> `00bace64` | `2a 7d 10 53` | lsr w10,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00bace68"></a> `00bace68` | `2b 51 15 12` | and w11,w9,#0xfffff800 | `FALL_THROUGH`
<a id="insn-00bace6c"></a> `00bace6c` | `5f 41 00 71` | cmp w10,#0x10 | `FALL_THROUGH`
<a id="insn-00bace70"></a> `00bace70` | `64 91 48 7a` | ccmp w11,w8,#0x4,ls | `FALL_THROUGH`
<a id="insn-00bace74"></a> `00bace74` | `c0 06 00 54` | b.eq 0x00bacf4c | `CONDITIONAL_JUMP`
<a id="insn-00bace78"></a> `00bace78` | `3f fd 01 71` | cmp w9,#0x7f | `FALL_THROUGH`
<a id="insn-00bace7c"></a> `00bace7c` | `c8 00 00 54` | b.hi 0x00bace94 | `CONDITIONAL_JUMP`
<a id="insn-00bace80"></a> `00bace80` | `ca 00 05 cb` | sub x10,x6,x5 | `FALL_THROUGH`
<a id="insn-00bace84"></a> `00bace84` | `5f 05 00 f1` | cmp x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bace88"></a> `00bace88` | `6b 06 00 54` | b.lt 0x00bacf54 | `CONDITIONAL_JUMP`
<a id="insn-00bace8c"></a> `00bace8c` | `a9 14 00 38` | strb w9,[x5], #0x1 | `FALL_THROUGH`
<a id="insn-00bace90"></a> `00bace90` | `f1 ff ff 17` | b 0x00bace54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace94"></a> `00bace94` | `3f fd 1f 71` | cmp w9,#0x7ff | `FALL_THROUGH`
<a id="insn-00bace98"></a> `00bace98` | `88 01 00 54` | b.hi 0x00bacec8 | `CONDITIONAL_JUMP`
<a id="insn-00bace9c"></a> `00bace9c` | `ca 00 05 cb` | sub x10,x6,x5 | `FALL_THROUGH`
<a id="insn-00bacea0"></a> `00bacea0` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bacea4"></a> `00bacea4` | `8b 05 00 54` | b.lt 0x00bacf54 | `CONDITIONAL_JUMP`
<a id="insn-00bacea8"></a> `00bacea8` | `2a 7d 06 53` | lsr w10,w9,#0x6 | `FALL_THROUGH`
<a id="insn-00baceac"></a> `00baceac` | `0b 10 80 52` | mov w11,#0x80 | `FALL_THROUGH`
<a id="insn-00baceb0"></a> `00baceb0` | `2b 15 00 33` | bfxil w11,w9,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00baceb4"></a> `00baceb4` | `a9 08 00 91` | add x9,x5,#0x2 | `FALL_THROUGH`
<a id="insn-00baceb8"></a> `00baceb8` | `4a 05 1a 32` | orr w10,w10,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacebc"></a> `00bacebc` | `aa 00 00 39` | strb w10,[x5] | `FALL_THROUGH`
<a id="insn-00bacec0"></a> `00bacec0` | `ab 04 00 39` | strb w11,[x5, #0x1] | `FALL_THROUGH`
<a id="insn-00bacec4"></a> `00bacec4` | `e3 ff ff 17` | b 0x00bace50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacec8"></a> `00bacec8` | `cb 00 05 cb` | sub x11,x6,x5 | `FALL_THROUGH`
<a id="insn-00bacecc"></a> `00bacecc` | `ca 01 00 35` | cbnz w10,0x00bacf04 | `CONDITIONAL_JUMP`
<a id="insn-00baced0"></a> `00baced0` | `7f 0d 00 f1` | cmp x11,#0x3 | `FALL_THROUGH`
<a id="insn-00baced4"></a> `00baced4` | `0b 04 00 54` | b.lt 0x00bacf54 | `CONDITIONAL_JUMP`
<a id="insn-00baced8"></a> `00baced8` | `2a 7d 0c 53` | lsr w10,w9,#0xc | `FALL_THROUGH`
<a id="insn-00bacedc"></a> `00bacedc` | `0b 10 80 52` | mov w11,#0x80 | `FALL_THROUGH`
<a id="insn-00bacee0"></a> `00bacee0` | `0c 10 80 52` | mov w12,#0x80 | `FALL_THROUGH`
<a id="insn-00bacee4"></a> `00bacee4` | `2b 2d 06 33` | bfxil w11,w9,#0x6,#0x6 | `FALL_THROUGH`
<a id="insn-00bacee8"></a> `00bacee8` | `2c 15 00 33` | bfxil w12,w9,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00baceec"></a> `00baceec` | `a9 0c 00 91` | add x9,x5,#0x3 | `FALL_THROUGH`
<a id="insn-00bacef0"></a> `00bacef0` | `4a 09 1b 32` | orr w10,w10,#0xe0 | `FALL_THROUGH`
<a id="insn-00bacef4"></a> `00bacef4` | `aa 00 00 39` | strb w10,[x5] | `FALL_THROUGH`
<a id="insn-00bacef8"></a> `00bacef8` | `ab 04 00 39` | strb w11,[x5, #0x1] | `FALL_THROUGH`
<a id="insn-00bacefc"></a> `00bacefc` | `ac 08 00 39` | strb w12,[x5, #0x2] | `FALL_THROUGH`
<a id="insn-00bacf00"></a> `00bacf00` | `d4 ff ff 17` | b 0x00bace50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf04"></a> `00bacf04` | `7f 11 00 f1` | cmp x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bacf08"></a> `00bacf08` | `6b 02 00 54` | b.lt 0x00bacf54 | `CONDITIONAL_JUMP`
<a id="insn-00bacf0c"></a> `00bacf0c` | `2a 7d 12 53` | lsr w10,w9,#0x12 | `FALL_THROUGH`
<a id="insn-00bacf10"></a> `00bacf10` | `0b 10 80 52` | mov w11,#0x80 | `FALL_THROUGH`
<a id="insn-00bacf14"></a> `00bacf14` | `0c 10 80 52` | mov w12,#0x80 | `FALL_THROUGH`
<a id="insn-00bacf18"></a> `00bacf18` | `0d 10 80 52` | mov w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bacf1c"></a> `00bacf1c` | `2b 45 0c 33` | bfxil w11,w9,#0xc,#0x6 | `FALL_THROUGH`
<a id="insn-00bacf20"></a> `00bacf20` | `2c 2d 06 33` | bfxil w12,w9,#0x6,#0x6 | `FALL_THROUGH`
<a id="insn-00bacf24"></a> `00bacf24` | `2d 15 00 33` | bfxil w13,w9,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bacf28"></a> `00bacf28` | `4a 0d 1c 32` | orr w10,w10,#0xf0 | `FALL_THROUGH`
<a id="insn-00bacf2c"></a> `00bacf2c` | `a9 10 00 91` | add x9,x5,#0x4 | `FALL_THROUGH`
<a id="insn-00bacf30"></a> `00bacf30` | `aa 00 00 39` | strb w10,[x5] | `FALL_THROUGH`
<a id="insn-00bacf34"></a> `00bacf34` | `ab 04 00 39` | strb w11,[x5, #0x1] | `FALL_THROUGH`
<a id="insn-00bacf38"></a> `00bacf38` | `ac 08 00 39` | strb w12,[x5, #0x2] | `FALL_THROUGH`
<a id="insn-00bacf3c"></a> `00bacf3c` | `ad 0c 00 39` | strb w13,[x5, #0x3] | `FALL_THROUGH`
<a id="insn-00bacf40"></a> `00bacf40` | `c4 ff ff 17` | b 0x00bace50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf44"></a> `00bacf44` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bacf48"></a> `00bacf48` | `04 00 00 14` | b 0x00bacf58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf4c"></a> `00bacf4c` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bacf50"></a> `00bacf50` | `02 00 00 14` | b 0x00bacf58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf54"></a> `00bacf54` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf58"></a> `00bacf58` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00bacf5c"></a> `00bacf5c` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00bacf60"></a> `00bacf60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bace3c`](#insn-00bace3c) 範囲 `[['00bace3c', '00bace47']]`
  - `CONDITIONAL_JUMP` [`00bace44`](#insn-00bace44) → [`00bacf44`](#insn-00bacf44)
  - `FALL_THROUGH` [`00bace44`](#insn-00bace44) → [`00bace48`](#insn-00bace48)
- ブロック [`00bace48`](#insn-00bace48) 範囲 `[['00bace48', '00bace4f']]`
  - `UNCONDITIONAL_JUMP` [`00bace4c`](#insn-00bace4c) → [`00bace60`](#insn-00bace60)
- ブロック [`00bace50`](#insn-00bace50) 範囲 `[['00bace50', '00bace53']]`
  - `FALL_THROUGH` [`00bace50`](#insn-00bace50) → [`00bace54`](#insn-00bace54)
- ブロック [`00bace54`](#insn-00bace54) 範囲 `[['00bace54', '00bace5f']]`
  - `CONDITIONAL_JUMP` [`00bace5c`](#insn-00bace5c) → [`00bacf44`](#insn-00bacf44)
  - `FALL_THROUGH` [`00bace5c`](#insn-00bace5c) → [`00bace60`](#insn-00bace60)
- ブロック [`00bace60`](#insn-00bace60) 範囲 `[['00bace60', '00bace77']]`
  - `CONDITIONAL_JUMP` [`00bace74`](#insn-00bace74) → [`00bacf4c`](#insn-00bacf4c)
  - `FALL_THROUGH` [`00bace74`](#insn-00bace74) → [`00bace78`](#insn-00bace78)
- ブロック [`00bace78`](#insn-00bace78) 範囲 `[['00bace78', '00bace7f']]`
  - `CONDITIONAL_JUMP` [`00bace7c`](#insn-00bace7c) → [`00bace94`](#insn-00bace94)
  - `FALL_THROUGH` [`00bace7c`](#insn-00bace7c) → [`00bace80`](#insn-00bace80)
- ブロック [`00bace80`](#insn-00bace80) 範囲 `[['00bace80', '00bace8b']]`
  - `CONDITIONAL_JUMP` [`00bace88`](#insn-00bace88) → [`00bacf54`](#insn-00bacf54)
  - `FALL_THROUGH` [`00bace88`](#insn-00bace88) → [`00bace8c`](#insn-00bace8c)
- ブロック [`00bace8c`](#insn-00bace8c) 範囲 `[['00bace8c', '00bace93']]`
  - `UNCONDITIONAL_JUMP` [`00bace90`](#insn-00bace90) → [`00bace54`](#insn-00bace54)
- ブロック [`00bace94`](#insn-00bace94) 範囲 `[['00bace94', '00bace9b']]`
  - `CONDITIONAL_JUMP` [`00bace98`](#insn-00bace98) → [`00bacec8`](#insn-00bacec8)
  - `FALL_THROUGH` [`00bace98`](#insn-00bace98) → [`00bace9c`](#insn-00bace9c)
- ブロック [`00bace9c`](#insn-00bace9c) 範囲 `[['00bace9c', '00bacea7']]`
  - `CONDITIONAL_JUMP` [`00bacea4`](#insn-00bacea4) → [`00bacf54`](#insn-00bacf54)
  - `FALL_THROUGH` [`00bacea4`](#insn-00bacea4) → [`00bacea8`](#insn-00bacea8)
- ブロック [`00bacea8`](#insn-00bacea8) 範囲 `[['00bacea8', '00bacec7']]`
  - `UNCONDITIONAL_JUMP` [`00bacec4`](#insn-00bacec4) → [`00bace50`](#insn-00bace50)
- ブロック [`00bacec8`](#insn-00bacec8) 範囲 `[['00bacec8', '00bacecf']]`
  - `CONDITIONAL_JUMP` [`00bacecc`](#insn-00bacecc) → [`00bacf04`](#insn-00bacf04)
  - `FALL_THROUGH` [`00bacecc`](#insn-00bacecc) → [`00baced0`](#insn-00baced0)
- ブロック [`00baced0`](#insn-00baced0) 範囲 `[['00baced0', '00baced7']]`
  - `CONDITIONAL_JUMP` [`00baced4`](#insn-00baced4) → [`00bacf54`](#insn-00bacf54)
  - `FALL_THROUGH` [`00baced4`](#insn-00baced4) → [`00baced8`](#insn-00baced8)
- ブロック [`00baced8`](#insn-00baced8) 範囲 `[['00baced8', '00bacf03']]`
  - `UNCONDITIONAL_JUMP` [`00bacf00`](#insn-00bacf00) → [`00bace50`](#insn-00bace50)
- ブロック [`00bacf04`](#insn-00bacf04) 範囲 `[['00bacf04', '00bacf0b']]`
  - `CONDITIONAL_JUMP` [`00bacf08`](#insn-00bacf08) → [`00bacf54`](#insn-00bacf54)
  - `FALL_THROUGH` [`00bacf08`](#insn-00bacf08) → [`00bacf0c`](#insn-00bacf0c)
- ブロック [`00bacf0c`](#insn-00bacf0c) 範囲 `[['00bacf0c', '00bacf43']]`
  - `UNCONDITIONAL_JUMP` [`00bacf40`](#insn-00bacf40) → [`00bace50`](#insn-00bace50)
- ブロック [`00bacf44`](#insn-00bacf44) 範囲 `[['00bacf44', '00bacf47']]`
  - `FALL_THROUGH` [`00bacf44`](#insn-00bacf44) → [`00bacf48`](#insn-00bacf48)
- ブロック [`00bacf48`](#insn-00bacf48) 範囲 `[['00bacf48', '00bacf4b']]`
  - `UNCONDITIONAL_JUMP` [`00bacf48`](#insn-00bacf48) → [`00bacf58`](#insn-00bacf58)
- ブロック [`00bacf4c`](#insn-00bacf4c) 範囲 `[['00bacf4c', '00bacf53']]`
  - `UNCONDITIONAL_JUMP` [`00bacf50`](#insn-00bacf50) → [`00bacf58`](#insn-00bacf58)
- ブロック [`00bacf54`](#insn-00bacf54) 範囲 `[['00bacf54', '00bacf57']]`
  - `FALL_THROUGH` [`00bacf54`](#insn-00bacf54) → [`00bacf58`](#insn-00bacf58)
- ブロック [`00bacf58`](#insn-00bacf58) 範囲 `[['00bacf58', '00bacf63']]`

## 命令位置別の参照

- [`00bace44`](#insn-00bace44) → [`00bacf44`](#insn-00bacf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace4c`](#insn-00bace4c) → [`00bace60`](#insn-00bace60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace5c`](#insn-00bace5c) → [`00bacf44`](#insn-00bacf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace74`](#insn-00bace74) → [`00bacf4c`](#insn-00bacf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace7c`](#insn-00bace7c) → [`00bace94`](#insn-00bace94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace88`](#insn-00bace88) → [`00bacf54`](#insn-00bacf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace90`](#insn-00bace90) → [`00bace54`](#insn-00bace54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace98`](#insn-00bace98) → [`00bacec8`](#insn-00bacec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacea4`](#insn-00bacea4) → [`00bacf54`](#insn-00bacf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacec4`](#insn-00bacec4) → [`00bace50`](#insn-00bace50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacecc`](#insn-00bacecc) → [`00bacf04`](#insn-00bacf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baced4`](#insn-00baced4) → [`00bacf54`](#insn-00bacf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf00`](#insn-00bacf00) → [`00bace50`](#insn-00bace50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf08`](#insn-00bacf08) → [`00bacf54`](#insn-00bacf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf40`](#insn-00bacf40) → [`00bace50`](#insn-00bace50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf48`](#insn-00bacf48) → [`00bacf58`](#insn-00bacf58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf50`](#insn-00bacf50) → [`00bacf58`](#insn-00bacf58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bace44`](#insn-00bace44)

~~~json
{
  "source": "00bace44",
  "target": "00bacf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace4c`](#insn-00bace4c)

~~~json
{
  "source": "00bace4c",
  "target": "00bace60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace5c`](#insn-00bace5c)

~~~json
{
  "source": "00bace5c",
  "target": "00bacf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace74`](#insn-00bace74)

~~~json
{
  "source": "00bace74",
  "target": "00bacf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace7c`](#insn-00bace7c)

~~~json
{
  "source": "00bace7c",
  "target": "00bace94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace88`](#insn-00bace88)

~~~json
{
  "source": "00bace88",
  "target": "00bacf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace90`](#insn-00bace90)

~~~json
{
  "source": "00bace90",
  "target": "00bace54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace98`](#insn-00bace98)

~~~json
{
  "source": "00bace98",
  "target": "00bacec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacea4`](#insn-00bacea4)

~~~json
{
  "source": "00bacea4",
  "target": "00bacf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacec4`](#insn-00bacec4)

~~~json
{
  "source": "00bacec4",
  "target": "00bace50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacecc`](#insn-00bacecc)

~~~json
{
  "source": "00bacecc",
  "target": "00bacf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baced4`](#insn-00baced4)

~~~json
{
  "source": "00baced4",
  "target": "00bacf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf00`](#insn-00bacf00)

~~~json
{
  "source": "00bacf00",
  "target": "00bace50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf08`](#insn-00bacf08)

~~~json
{
  "source": "00bacf08",
  "target": "00bacf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf40`](#insn-00bacf40)

~~~json
{
  "source": "00bacf40",
  "target": "00bace50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf48`](#insn-00bacf48)

~~~json
{
  "source": "00bacf48",
  "target": "00bacf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf50`](#insn-00bacf50)

~~~json
{
  "source": "00bacf50",
  "target": "00bacf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
