# 00badaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00badbb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00badbb8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-97511b69e4ae7d856b5b18d9b679c0c3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badaf0",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07c9a509ff11e6028c3b377785da9f01b7af1ffd09a0c87e5a012ac2f1d15125",
  "source_text_sha256": "07c9a509ff11e6028c3b377785da9f01b7af1ffd09a0c87e5a012ac2f1d15125",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badaf0",
        "00badbeb"
      ]
    ],
    "bytes_sha256": "c71536c685fba74ad6ca476233b6e24f3433c2e1c07664b692a79821fc3472d2",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
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

## 疑似コード / UTF-8 1783 bytes

~~~c

ulong _ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_
                (long param_1,undefined8 param_2,ushort *param_3,ushort *param_4,ulong *param_5,
                uint *param_6,uint *param_7,undefined8 *param_8)

{
  byte bVar1;
  ulong uVar2;
  uint *puVar3;
  ulong uVar4;
  uint uVar5;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x20) >> 2 & 1) != 0)) &&
     ((char)*param_3 == -1)) {
    param_3 = param_3 + (*(char *)((long)param_3 + 1) == -2);
  }
  if (param_3 < (ushort *)((long)param_4 + -1)) {
    uVar4 = *(ulong *)(param_1 + 0x18);
    puVar3 = param_6;
    do {
      param_6 = puVar3;
      if (param_7 <= puVar3) break;
      uVar5 = (uint)*param_3;
      bVar1 = *(byte *)((long)param_3 + 1) & 0xfc;
      if (bVar1 == 0xd8) {
        if ((long)param_4 - (long)param_3 < 4) {
          uVar2 = 1;
          goto LAB_00badbd0;
        }
                    /* catch() { ... } // from try @ 00badd8c with catch @ 00badbb0 */
        if (((*(byte *)((long)param_3 + 3) & 0xfc) != 0xdc) ||
           (uVar5 = ((uint)(byte)param_3[1] | (*(byte *)((long)param_3 + 3) & 3) << 8 |
                    (uVar5 & 0x3ff) << 10) + 0x10000, uVar4 < uVar5)) goto LAB_00badbdc;
        uVar2 = 4;
      }
      else {
        if (bVar1 == 0xdc) {
LAB_00badbdc:
          uVar2 = 2;
          goto LAB_00badbd0;
        }
        uVar2 = 2;
        if (uVar4 < uVar5) goto LAB_00badbd0;
      }
      param_3 = (ushort *)((long)param_3 + uVar2);
      param_6 = puVar3 + 1;
      *puVar3 = uVar5;
      puVar3 = param_6;
    } while (param_3 < (ushort *)((long)param_4 + -1));
  }
  uVar2 = (ulong)(param_3 < param_4);
  puVar3 = param_6;
LAB_00badbd0:
  *param_5 = (ulong)param_3;
  *param_8 = puVar3;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badaf0"></a> `00badaf0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badaf4"></a> `00badaf4` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badaf8"></a> `00badaf8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badafc"></a> `00badafc` | `4b 01 00 54` | b.lt 0x00badb24 | `CONDITIONAL_JUMP`
<a id="insn-00badb00"></a> `00badb00` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00badb04"></a> `00badb04` | `08 01 10 36` | tbz w8,#0x2,0x00badb24 | `CONDITIONAL_JUMP`
<a id="insn-00badb08"></a> `00badb08` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00badb0c"></a> `00badb0c` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badb10"></a> `00badb10` | `a1 00 00 54` | b.ne 0x00badb24 | `CONDITIONAL_JUMP`
<a id="insn-00badb14"></a> `00badb14` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badb18"></a> `00badb18` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00badb1c"></a> `00badb1c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00badb20"></a> `00badb20` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00badb24"></a> `00badb24` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00badb28"></a> `00badb28` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badb2c"></a> `00badb2c` | `e2 04 00 54` | b.cs 0x00badbc8 | `CONDITIONAL_JUMP`
<a id="insn-00badb30"></a> `00badb30` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badb34"></a> `00badb34` | `0a 00 9b 52` | mov w10,#0xd800 | `FALL_THROUGH`
<a id="insn-00badb38"></a> `00badb38` | `0b 80 9b 52` | mov w11,#0xdc00 | `FALL_THROUGH`
<a id="insn-00badb3c"></a> `00badb3c` | `05 00 00 14` | b 0x00badb50 | `UNCONDITIONAL_JUMP`
<a id="insn-00badb40"></a> `00badb40` | `42 00 00 8b` | add x2,x2,x0 | `FALL_THROUGH`
<a id="insn-00badb44"></a> `00badb44` | `ac 44 00 b8` | str w12,[x5], #0x4 | `FALL_THROUGH`
<a id="insn-00badb48"></a> `00badb48` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badb4c"></a> `00badb4c` | `e2 03 00 54` | b.cs 0x00badbc8 | `CONDITIONAL_JUMP`
<a id="insn-00badb50"></a> `00badb50` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00badb54"></a> `00badb54` | `a2 03 00 54` | b.cs 0x00badbc8 | `CONDITIONAL_JUMP`
<a id="insn-00badb58"></a> `00badb58` | `4e 04 40 39` | ldrb w14,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badb5c"></a> `00badb5c` | `4c 00 40 39` | ldrb w12,[x2] | `FALL_THROUGH`
<a id="insn-00badb60"></a> `00badb60` | `cd 5d 18 53` | lsl w13,w14,#0x8 | `FALL_THROUGH`
<a id="insn-00badb64"></a> `00badb64` | `cc 1d 18 33` | bfm w12,w14,#0x18,#0x7 | `FALL_THROUGH`
<a id="insn-00badb68"></a> `00badb68` | `ad 15 16 12` | and w13,w13,#0xfc00 | `FALL_THROUGH`
<a id="insn-00badb6c"></a> `00badb6c` | `bf 01 0a 6b` | cmp w13,w10 | `FALL_THROUGH`
<a id="insn-00badb70"></a> `00badb70` | `e0 00 00 54` | b.eq 0x00badb8c | `CONDITIONAL_JUMP`
<a id="insn-00badb74"></a> `00badb74` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00badb78"></a> `00badb78` | `20 03 00 54` | b.eq 0x00badbdc | `CONDITIONAL_JUMP`
<a id="insn-00badb7c"></a> `00badb7c` | `3f 41 2c eb` | cmp x9,w12, UXTW  | `FALL_THROUGH`
<a id="insn-00badb80"></a> `00badb80` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badb84"></a> `00badb84` | `e2 fd ff 54` | b.cs 0x00badb40 | `CONDITIONAL_JUMP`
<a id="insn-00badb88"></a> `00badb88` | `12 00 00 14` | b 0x00badbd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00badb8c"></a> `00badb8c` | `6d 00 02 cb` | sub x13,x3,x2 | `FALL_THROUGH`
<a id="insn-00badb90"></a> `00badb90` | `bf 11 00 f1` | cmp x13,#0x4 | `FALL_THROUGH`
<a id="insn-00badb94"></a> `00badb94` | `8b 02 00 54` | b.lt 0x00badbe4 | `CONDITIONAL_JUMP`
<a id="insn-00badb98"></a> `00badb98` | `4d 0c 40 39` | ldrb w13,[x2, #0x3] | `FALL_THROUGH`
<a id="insn-00badb9c"></a> `00badb9c` | `ae 15 1e 12` | and w14,w13,#0xfc | `FALL_THROUGH`
<a id="insn-00badba0"></a> `00badba0` | `df 71 03 71` | cmp w14,#0xdc | `FALL_THROUGH`
<a id="insn-00badba4"></a> `00badba4` | `c1 01 00 54` | b.ne 0x00badbdc | `CONDITIONAL_JUMP`
<a id="insn-00badba8"></a> `00badba8` | `4e 08 40 39` | ldrb w14,[x2, #0x2] | `FALL_THROUGH`
<a id="insn-00badbac"></a> `00badbac` | `ae 05 18 33` | bfm w14,w13,#0x18,#0x1 | `FALL_THROUGH`
<a id="insn-00badbb0"></a> `00badbb0` | `8e 25 16 33` | bfm w14,w12,#0x16,#0x9 | `FALL_THROUGH`
<a id="insn-00badbb4"></a> `00badbb4` | `cc 41 40 11` | add w12,w14,#0x10, LSL #12 | `FALL_THROUGH`
<a id="insn-00badbb8"></a> `00badbb8` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00badbbc"></a> `00badbbc` | `03 01 00 54` | b.cc 0x00badbdc | `CONDITIONAL_JUMP`
<a id="insn-00badbc0"></a> `00badbc0` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00badbc4"></a> `00badbc4` | `df ff ff 17` | b 0x00badb40 | `UNCONDITIONAL_JUMP`
<a id="insn-00badbc8"></a> `00badbc8` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00badbcc"></a> `00badbcc` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00badbd0"></a> `00badbd0` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00badbd4"></a> `00badbd4` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00badbd8"></a> `00badbd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00badbdc"></a> `00badbdc` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badbe0"></a> `00badbe0` | `fc ff ff 17` | b 0x00badbd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00badbe4"></a> `00badbe4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00badbe8"></a> `00badbe8` | `fa ff ff 17` | b 0x00badbd0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00badaf0`](#insn-00badaf0) 範囲 `[['00badaf0', '00badaff']]`
  - `CONDITIONAL_JUMP` [`00badafc`](#insn-00badafc) → [`00badb24`](#insn-00badb24)
  - `FALL_THROUGH` [`00badafc`](#insn-00badafc) → [`00badb00`](#insn-00badb00)
- ブロック [`00badb00`](#insn-00badb00) 範囲 `[['00badb00', '00badb07']]`
  - `CONDITIONAL_JUMP` [`00badb04`](#insn-00badb04) → [`00badb24`](#insn-00badb24)
  - `FALL_THROUGH` [`00badb04`](#insn-00badb04) → [`00badb08`](#insn-00badb08)
- ブロック [`00badb08`](#insn-00badb08) 範囲 `[['00badb08', '00badb13']]`
  - `CONDITIONAL_JUMP` [`00badb10`](#insn-00badb10) → [`00badb24`](#insn-00badb24)
  - `FALL_THROUGH` [`00badb10`](#insn-00badb10) → [`00badb14`](#insn-00badb14)
- ブロック [`00badb14`](#insn-00badb14) 範囲 `[['00badb14', '00badb23']]`
  - `FALL_THROUGH` [`00badb20`](#insn-00badb20) → [`00badb24`](#insn-00badb24)
- ブロック [`00badb24`](#insn-00badb24) 範囲 `[['00badb24', '00badb2f']]`
  - `CONDITIONAL_JUMP` [`00badb2c`](#insn-00badb2c) → [`00badbc8`](#insn-00badbc8)
  - `FALL_THROUGH` [`00badb2c`](#insn-00badb2c) → [`00badb30`](#insn-00badb30)
- ブロック [`00badb30`](#insn-00badb30) 範囲 `[['00badb30', '00badb3f']]`
  - `UNCONDITIONAL_JUMP` [`00badb3c`](#insn-00badb3c) → [`00badb50`](#insn-00badb50)
- ブロック [`00badb40`](#insn-00badb40) 範囲 `[['00badb40', '00badb4f']]`
  - `CONDITIONAL_JUMP` [`00badb4c`](#insn-00badb4c) → [`00badbc8`](#insn-00badbc8)
  - `FALL_THROUGH` [`00badb4c`](#insn-00badb4c) → [`00badb50`](#insn-00badb50)
- ブロック [`00badb50`](#insn-00badb50) 範囲 `[['00badb50', '00badb57']]`
  - `CONDITIONAL_JUMP` [`00badb54`](#insn-00badb54) → [`00badbc8`](#insn-00badbc8)
  - `FALL_THROUGH` [`00badb54`](#insn-00badb54) → [`00badb58`](#insn-00badb58)
- ブロック [`00badb58`](#insn-00badb58) 範囲 `[['00badb58', '00badb73']]`
  - `CONDITIONAL_JUMP` [`00badb70`](#insn-00badb70) → [`00badb8c`](#insn-00badb8c)
  - `FALL_THROUGH` [`00badb70`](#insn-00badb70) → [`00badb74`](#insn-00badb74)
- ブロック [`00badb74`](#insn-00badb74) 範囲 `[['00badb74', '00badb7b']]`
  - `CONDITIONAL_JUMP` [`00badb78`](#insn-00badb78) → [`00badbdc`](#insn-00badbdc)
  - `FALL_THROUGH` [`00badb78`](#insn-00badb78) → [`00badb7c`](#insn-00badb7c)
- ブロック [`00badb7c`](#insn-00badb7c) 範囲 `[['00badb7c', '00badb87']]`
  - `CONDITIONAL_JUMP` [`00badb84`](#insn-00badb84) → [`00badb40`](#insn-00badb40)
  - `FALL_THROUGH` [`00badb84`](#insn-00badb84) → [`00badb88`](#insn-00badb88)
- ブロック [`00badb88`](#insn-00badb88) 範囲 `[['00badb88', '00badb8b']]`
  - `UNCONDITIONAL_JUMP` [`00badb88`](#insn-00badb88) → [`00badbd0`](#insn-00badbd0)
- ブロック [`00badb8c`](#insn-00badb8c) 範囲 `[['00badb8c', '00badb97']]`
  - `CONDITIONAL_JUMP` [`00badb94`](#insn-00badb94) → [`00badbe4`](#insn-00badbe4)
  - `FALL_THROUGH` [`00badb94`](#insn-00badb94) → [`00badb98`](#insn-00badb98)
- ブロック [`00badb98`](#insn-00badb98) 範囲 `[['00badb98', '00badba7']]`
  - `CONDITIONAL_JUMP` [`00badba4`](#insn-00badba4) → [`00badbdc`](#insn-00badbdc)
  - `FALL_THROUGH` [`00badba4`](#insn-00badba4) → [`00badba8`](#insn-00badba8)
- ブロック [`00badba8`](#insn-00badba8) 範囲 `[['00badba8', '00badbaf']]`
  - `FALL_THROUGH` [`00badbac`](#insn-00badbac) → [`00badbb0`](#insn-00badbb0)
- ブロック [`00badbb0`](#insn-00badbb0) 範囲 `[['00badbb0', '00badbbf']]`
  - `CONDITIONAL_JUMP` [`00badbbc`](#insn-00badbbc) → [`00badbdc`](#insn-00badbdc)
  - `FALL_THROUGH` [`00badbbc`](#insn-00badbbc) → [`00badbc0`](#insn-00badbc0)
- ブロック [`00badbc0`](#insn-00badbc0) 範囲 `[['00badbc0', '00badbc7']]`
  - `UNCONDITIONAL_JUMP` [`00badbc4`](#insn-00badbc4) → [`00badb40`](#insn-00badb40)
- ブロック [`00badbc8`](#insn-00badbc8) 範囲 `[['00badbc8', '00badbcf']]`
  - `FALL_THROUGH` [`00badbcc`](#insn-00badbcc) → [`00badbd0`](#insn-00badbd0)
- ブロック [`00badbd0`](#insn-00badbd0) 範囲 `[['00badbd0', '00badbdb']]`
- ブロック [`00badbdc`](#insn-00badbdc) 範囲 `[['00badbdc', '00badbe3']]`
  - `UNCONDITIONAL_JUMP` [`00badbe0`](#insn-00badbe0) → [`00badbd0`](#insn-00badbd0)
- ブロック [`00badbe4`](#insn-00badbe4) 範囲 `[['00badbe4', '00badbeb']]`
  - `UNCONDITIONAL_JUMP` [`00badbe8`](#insn-00badbe8) → [`00badbd0`](#insn-00badbd0)

## 命令位置別の参照

- [`00badafc`](#insn-00badafc) → [`00badb24`](#insn-00badb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb04`](#insn-00badb04) → [`00badb24`](#insn-00badb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb10`](#insn-00badb10) → [`00badb24`](#insn-00badb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb2c`](#insn-00badb2c) → [`00badbc8`](#insn-00badbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb3c`](#insn-00badb3c) → [`00badb50`](#insn-00badb50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb4c`](#insn-00badb4c) → [`00badbc8`](#insn-00badbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb54`](#insn-00badb54) → [`00badbc8`](#insn-00badbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb70`](#insn-00badb70) → [`00badb8c`](#insn-00badb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb78`](#insn-00badb78) → [`00badbdc`](#insn-00badbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb84`](#insn-00badb84) → [`00badb40`](#insn-00badb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb88`](#insn-00badb88) → [`00badbd0`](#insn-00badbd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb94`](#insn-00badb94) → [`00badbe4`](#insn-00badbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badba4`](#insn-00badba4) → [`00badbdc`](#insn-00badbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badbbc`](#insn-00badbbc) → [`00badbdc`](#insn-00badbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badbc4`](#insn-00badbc4) → [`00badb40`](#insn-00badb40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badbe0`](#insn-00badbe0) → [`00badbd0`](#insn-00badbd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badbe8`](#insn-00badbe8) → [`00badbd0`](#insn-00badbd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badafc`](#insn-00badafc)

~~~json
{
  "source": "00badafc",
  "target": "00badb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb04`](#insn-00badb04)

~~~json
{
  "source": "00badb04",
  "target": "00badb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb10`](#insn-00badb10)

~~~json
{
  "source": "00badb10",
  "target": "00badb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb2c`](#insn-00badb2c)

~~~json
{
  "source": "00badb2c",
  "target": "00badbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb3c`](#insn-00badb3c)

~~~json
{
  "source": "00badb3c",
  "target": "00badb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb4c`](#insn-00badb4c)

~~~json
{
  "source": "00badb4c",
  "target": "00badbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb54`](#insn-00badb54)

~~~json
{
  "source": "00badb54",
  "target": "00badbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb70`](#insn-00badb70)

~~~json
{
  "source": "00badb70",
  "target": "00badb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb78`](#insn-00badb78)

~~~json
{
  "source": "00badb78",
  "target": "00badbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb84`](#insn-00badb84)

~~~json
{
  "source": "00badb84",
  "target": "00badb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb88`](#insn-00badb88)

~~~json
{
  "source": "00badb88",
  "target": "00badbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb94`](#insn-00badb94)

~~~json
{
  "source": "00badb94",
  "target": "00badbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badba4`](#insn-00badba4)

~~~json
{
  "source": "00badba4",
  "target": "00badbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badbbc`](#insn-00badbbc)

~~~json
{
  "source": "00badbbc",
  "target": "00badbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badbc4`](#insn-00badbc4)

~~~json
{
  "source": "00badbc4",
  "target": "00badb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badbe0`](#insn-00badbe0)

~~~json
{
  "source": "00badbe0",
  "target": "00badbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badbe8`](#insn-00badbe8)

~~~json
{
  "source": "00badbe8",
  "target": "00badbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
