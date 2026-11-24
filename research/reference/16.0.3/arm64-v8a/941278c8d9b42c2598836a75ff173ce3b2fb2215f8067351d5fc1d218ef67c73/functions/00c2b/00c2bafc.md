# 00c2bafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c2ab08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2ab08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/detail_skipped-0009.md#compare-50e02d1a19f2f624359f509157c5faad)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2bafc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a6b932162450eb9c19ad68df1794bd31134ee4b8f0146350d9d6dc12a93aaef9",
  "source_text_sha256": "a6b932162450eb9c19ad68df1794bd31134ee4b8f0146350d9d6dc12a93aaef9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2bafc",
        "00c2bbf7"
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

## 疑似コード / UTF-8 1696 bytes

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
          goto LAB_00c2bbdc;
        }
        if (((*(byte *)((long)param_3 + 3) & 0xfc) != 0xdc) ||
           (uVar5 = ((uint)(byte)param_3[1] | (*(byte *)((long)param_3 + 3) & 3) << 8 |
                    (uVar5 & 0x3ff) << 10) + 0x10000, uVar4 < uVar5)) goto LAB_00c2bbe8;
        uVar2 = 4;
      }
      else {
        if (bVar1 == 0xdc) {
LAB_00c2bbe8:
          uVar2 = 2;
          goto LAB_00c2bbdc;
        }
        uVar2 = 2;
        if (uVar4 < uVar5) goto LAB_00c2bbdc;
      }
      param_3 = (ushort *)((long)param_3 + uVar2);
      param_6 = puVar3 + 1;
      *puVar3 = uVar5;
      puVar3 = param_6;
    } while (param_3 < (ushort *)((long)param_4 + -1));
  }
  uVar2 = (ulong)(param_3 < param_4);
  puVar3 = param_6;
LAB_00c2bbdc:
  *param_5 = (ulong)param_3;
  *param_8 = puVar3;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2bafc"></a> `00c2bafc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c2bb00"></a> `00c2bb00` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00c2bb04"></a> `00c2bb04` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c2bb08"></a> `00c2bb08` | `4b 01 00 54` | b.lt 0x00c2bb30 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb0c"></a> `00c2bb0c` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00c2bb10"></a> `00c2bb10` | `08 01 10 36` | tbz w8,#0x2,0x00c2bb30 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb14"></a> `00c2bb14` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00c2bb18"></a> `00c2bb18` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00c2bb1c"></a> `00c2bb1c` | `a1 00 00 54` | b.ne 0x00c2bb30 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb20"></a> `00c2bb20` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00c2bb24"></a> `00c2bb24` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00c2bb28"></a> `00c2bb28` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00c2bb2c"></a> `00c2bb2c` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00c2bb30"></a> `00c2bb30` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00c2bb34"></a> `00c2bb34` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00c2bb38"></a> `00c2bb38` | `e2 04 00 54` | b.cs 0x00c2bbd4 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb3c"></a> `00c2bb3c` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c2bb40"></a> `00c2bb40` | `0a 00 9b 52` | mov w10,#0xd800 | `FALL_THROUGH`
<a id="insn-00c2bb44"></a> `00c2bb44` | `0b 80 9b 52` | mov w11,#0xdc00 | `FALL_THROUGH`
<a id="insn-00c2bb48"></a> `00c2bb48` | `05 00 00 14` | b 0x00c2bb5c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2bb4c"></a> `00c2bb4c` | `42 00 00 8b` | add x2,x2,x0 | `FALL_THROUGH`
<a id="insn-00c2bb50"></a> `00c2bb50` | `ac 44 00 b8` | str w12,[x5], #0x4 | `FALL_THROUGH`
<a id="insn-00c2bb54"></a> `00c2bb54` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00c2bb58"></a> `00c2bb58` | `e2 03 00 54` | b.cs 0x00c2bbd4 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb5c"></a> `00c2bb5c` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00c2bb60"></a> `00c2bb60` | `a2 03 00 54` | b.cs 0x00c2bbd4 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb64"></a> `00c2bb64` | `4e 04 40 39` | ldrb w14,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00c2bb68"></a> `00c2bb68` | `4c 00 40 39` | ldrb w12,[x2] | `FALL_THROUGH`
<a id="insn-00c2bb6c"></a> `00c2bb6c` | `cd 5d 18 53` | lsl w13,w14,#0x8 | `FALL_THROUGH`
<a id="insn-00c2bb70"></a> `00c2bb70` | `cc 1d 18 33` | bfm w12,w14,#0x18,#0x7 | `FALL_THROUGH`
<a id="insn-00c2bb74"></a> `00c2bb74` | `ad 15 16 12` | and w13,w13,#0xfc00 | `FALL_THROUGH`
<a id="insn-00c2bb78"></a> `00c2bb78` | `bf 01 0a 6b` | cmp w13,w10 | `FALL_THROUGH`
<a id="insn-00c2bb7c"></a> `00c2bb7c` | `e0 00 00 54` | b.eq 0x00c2bb98 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb80"></a> `00c2bb80` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00c2bb84"></a> `00c2bb84` | `20 03 00 54` | b.eq 0x00c2bbe8 | `CONDITIONAL_JUMP`
<a id="insn-00c2bb88"></a> `00c2bb88` | `3f 41 2c eb` | cmp x9,w12, UXTW  | `FALL_THROUGH`
<a id="insn-00c2bb8c"></a> `00c2bb8c` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00c2bb90"></a> `00c2bb90` | `e2 fd ff 54` | b.cs 0x00c2bb4c | `CONDITIONAL_JUMP`
<a id="insn-00c2bb94"></a> `00c2bb94` | `12 00 00 14` | b 0x00c2bbdc | `UNCONDITIONAL_JUMP`
<a id="insn-00c2bb98"></a> `00c2bb98` | `6d 00 02 cb` | sub x13,x3,x2 | `FALL_THROUGH`
<a id="insn-00c2bb9c"></a> `00c2bb9c` | `bf 11 00 f1` | cmp x13,#0x4 | `FALL_THROUGH`
<a id="insn-00c2bba0"></a> `00c2bba0` | `8b 02 00 54` | b.lt 0x00c2bbf0 | `CONDITIONAL_JUMP`
<a id="insn-00c2bba4"></a> `00c2bba4` | `4d 0c 40 39` | ldrb w13,[x2, #0x3] | `FALL_THROUGH`
<a id="insn-00c2bba8"></a> `00c2bba8` | `ae 15 1e 12` | and w14,w13,#0xfc | `FALL_THROUGH`
<a id="insn-00c2bbac"></a> `00c2bbac` | `df 71 03 71` | cmp w14,#0xdc | `FALL_THROUGH`
<a id="insn-00c2bbb0"></a> `00c2bbb0` | `c1 01 00 54` | b.ne 0x00c2bbe8 | `CONDITIONAL_JUMP`
<a id="insn-00c2bbb4"></a> `00c2bbb4` | `4e 08 40 39` | ldrb w14,[x2, #0x2] | `FALL_THROUGH`
<a id="insn-00c2bbb8"></a> `00c2bbb8` | `ae 05 18 33` | bfm w14,w13,#0x18,#0x1 | `FALL_THROUGH`
<a id="insn-00c2bbbc"></a> `00c2bbbc` | `8e 25 16 33` | bfm w14,w12,#0x16,#0x9 | `FALL_THROUGH`
<a id="insn-00c2bbc0"></a> `00c2bbc0` | `cc 41 40 11` | add w12,w14,#0x10, LSL #12 | `FALL_THROUGH`
<a id="insn-00c2bbc4"></a> `00c2bbc4` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00c2bbc8"></a> `00c2bbc8` | `03 01 00 54` | b.cc 0x00c2bbe8 | `CONDITIONAL_JUMP`
<a id="insn-00c2bbcc"></a> `00c2bbcc` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00c2bbd0"></a> `00c2bbd0` | `df ff ff 17` | b 0x00c2bb4c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2bbd4"></a> `00c2bbd4` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00c2bbd8"></a> `00c2bbd8` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00c2bbdc"></a> `00c2bbdc` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00c2bbe0"></a> `00c2bbe0` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00c2bbe4"></a> `00c2bbe4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c2bbe8"></a> `00c2bbe8` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00c2bbec"></a> `00c2bbec` | `fc ff ff 17` | b 0x00c2bbdc | `UNCONDITIONAL_JUMP`
<a id="insn-00c2bbf0"></a> `00c2bbf0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c2bbf4"></a> `00c2bbf4` | `fa ff ff 17` | b 0x00c2bbdc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c2bafc`](#insn-00c2bafc) 範囲 `[['00c2bafc', '00c2bb0b']]`
  - `CONDITIONAL_JUMP` [`00c2bb08`](#insn-00c2bb08) → [`00c2bb30`](#insn-00c2bb30)
  - `FALL_THROUGH` [`00c2bb08`](#insn-00c2bb08) → [`00c2bb0c`](#insn-00c2bb0c)
- ブロック [`00c2bb0c`](#insn-00c2bb0c) 範囲 `[['00c2bb0c', '00c2bb13']]`
  - `CONDITIONAL_JUMP` [`00c2bb10`](#insn-00c2bb10) → [`00c2bb30`](#insn-00c2bb30)
  - `FALL_THROUGH` [`00c2bb10`](#insn-00c2bb10) → [`00c2bb14`](#insn-00c2bb14)
- ブロック [`00c2bb14`](#insn-00c2bb14) 範囲 `[['00c2bb14', '00c2bb1f']]`
  - `CONDITIONAL_JUMP` [`00c2bb1c`](#insn-00c2bb1c) → [`00c2bb30`](#insn-00c2bb30)
  - `FALL_THROUGH` [`00c2bb1c`](#insn-00c2bb1c) → [`00c2bb20`](#insn-00c2bb20)
- ブロック [`00c2bb20`](#insn-00c2bb20) 範囲 `[['00c2bb20', '00c2bb2f']]`
  - `FALL_THROUGH` [`00c2bb2c`](#insn-00c2bb2c) → [`00c2bb30`](#insn-00c2bb30)
- ブロック [`00c2bb30`](#insn-00c2bb30) 範囲 `[['00c2bb30', '00c2bb3b']]`
  - `CONDITIONAL_JUMP` [`00c2bb38`](#insn-00c2bb38) → [`00c2bbd4`](#insn-00c2bbd4)
  - `FALL_THROUGH` [`00c2bb38`](#insn-00c2bb38) → [`00c2bb3c`](#insn-00c2bb3c)
- ブロック [`00c2bb3c`](#insn-00c2bb3c) 範囲 `[['00c2bb3c', '00c2bb4b']]`
  - `UNCONDITIONAL_JUMP` [`00c2bb48`](#insn-00c2bb48) → [`00c2bb5c`](#insn-00c2bb5c)
- ブロック [`00c2bb4c`](#insn-00c2bb4c) 範囲 `[['00c2bb4c', '00c2bb5b']]`
  - `CONDITIONAL_JUMP` [`00c2bb58`](#insn-00c2bb58) → [`00c2bbd4`](#insn-00c2bbd4)
  - `FALL_THROUGH` [`00c2bb58`](#insn-00c2bb58) → [`00c2bb5c`](#insn-00c2bb5c)
- ブロック [`00c2bb5c`](#insn-00c2bb5c) 範囲 `[['00c2bb5c', '00c2bb63']]`
  - `CONDITIONAL_JUMP` [`00c2bb60`](#insn-00c2bb60) → [`00c2bbd4`](#insn-00c2bbd4)
  - `FALL_THROUGH` [`00c2bb60`](#insn-00c2bb60) → [`00c2bb64`](#insn-00c2bb64)
- ブロック [`00c2bb64`](#insn-00c2bb64) 範囲 `[['00c2bb64', '00c2bb7f']]`
  - `CONDITIONAL_JUMP` [`00c2bb7c`](#insn-00c2bb7c) → [`00c2bb98`](#insn-00c2bb98)
  - `FALL_THROUGH` [`00c2bb7c`](#insn-00c2bb7c) → [`00c2bb80`](#insn-00c2bb80)
- ブロック [`00c2bb80`](#insn-00c2bb80) 範囲 `[['00c2bb80', '00c2bb87']]`
  - `CONDITIONAL_JUMP` [`00c2bb84`](#insn-00c2bb84) → [`00c2bbe8`](#insn-00c2bbe8)
  - `FALL_THROUGH` [`00c2bb84`](#insn-00c2bb84) → [`00c2bb88`](#insn-00c2bb88)
- ブロック [`00c2bb88`](#insn-00c2bb88) 範囲 `[['00c2bb88', '00c2bb93']]`
  - `CONDITIONAL_JUMP` [`00c2bb90`](#insn-00c2bb90) → [`00c2bb4c`](#insn-00c2bb4c)
  - `FALL_THROUGH` [`00c2bb90`](#insn-00c2bb90) → [`00c2bb94`](#insn-00c2bb94)
- ブロック [`00c2bb94`](#insn-00c2bb94) 範囲 `[['00c2bb94', '00c2bb97']]`
  - `UNCONDITIONAL_JUMP` [`00c2bb94`](#insn-00c2bb94) → [`00c2bbdc`](#insn-00c2bbdc)
- ブロック [`00c2bb98`](#insn-00c2bb98) 範囲 `[['00c2bb98', '00c2bba3']]`
  - `CONDITIONAL_JUMP` [`00c2bba0`](#insn-00c2bba0) → [`00c2bbf0`](#insn-00c2bbf0)
  - `FALL_THROUGH` [`00c2bba0`](#insn-00c2bba0) → [`00c2bba4`](#insn-00c2bba4)
- ブロック [`00c2bba4`](#insn-00c2bba4) 範囲 `[['00c2bba4', '00c2bbb3']]`
  - `CONDITIONAL_JUMP` [`00c2bbb0`](#insn-00c2bbb0) → [`00c2bbe8`](#insn-00c2bbe8)
  - `FALL_THROUGH` [`00c2bbb0`](#insn-00c2bbb0) → [`00c2bbb4`](#insn-00c2bbb4)
- ブロック [`00c2bbb4`](#insn-00c2bbb4) 範囲 `[['00c2bbb4', '00c2bbcb']]`
  - `CONDITIONAL_JUMP` [`00c2bbc8`](#insn-00c2bbc8) → [`00c2bbe8`](#insn-00c2bbe8)
  - `FALL_THROUGH` [`00c2bbc8`](#insn-00c2bbc8) → [`00c2bbcc`](#insn-00c2bbcc)
- ブロック [`00c2bbcc`](#insn-00c2bbcc) 範囲 `[['00c2bbcc', '00c2bbd3']]`
  - `UNCONDITIONAL_JUMP` [`00c2bbd0`](#insn-00c2bbd0) → [`00c2bb4c`](#insn-00c2bb4c)
- ブロック [`00c2bbd4`](#insn-00c2bbd4) 範囲 `[['00c2bbd4', '00c2bbdb']]`
  - `FALL_THROUGH` [`00c2bbd8`](#insn-00c2bbd8) → [`00c2bbdc`](#insn-00c2bbdc)
- ブロック [`00c2bbdc`](#insn-00c2bbdc) 範囲 `[['00c2bbdc', '00c2bbe7']]`
- ブロック [`00c2bbe8`](#insn-00c2bbe8) 範囲 `[['00c2bbe8', '00c2bbef']]`
  - `UNCONDITIONAL_JUMP` [`00c2bbec`](#insn-00c2bbec) → [`00c2bbdc`](#insn-00c2bbdc)
- ブロック [`00c2bbf0`](#insn-00c2bbf0) 範囲 `[['00c2bbf0', '00c2bbf7']]`
  - `UNCONDITIONAL_JUMP` [`00c2bbf4`](#insn-00c2bbf4) → [`00c2bbdc`](#insn-00c2bbdc)

## 命令位置別の参照

- [`00c2bb08`](#insn-00c2bb08) → [`00c2bb30`](#insn-00c2bb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb10`](#insn-00c2bb10) → [`00c2bb30`](#insn-00c2bb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb1c`](#insn-00c2bb1c) → [`00c2bb30`](#insn-00c2bb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb38`](#insn-00c2bb38) → [`00c2bbd4`](#insn-00c2bbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb48`](#insn-00c2bb48) → [`00c2bb5c`](#insn-00c2bb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb58`](#insn-00c2bb58) → [`00c2bbd4`](#insn-00c2bbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb60`](#insn-00c2bb60) → [`00c2bbd4`](#insn-00c2bbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb7c`](#insn-00c2bb7c) → [`00c2bb98`](#insn-00c2bb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb84`](#insn-00c2bb84) → [`00c2bbe8`](#insn-00c2bbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb90`](#insn-00c2bb90) → [`00c2bb4c`](#insn-00c2bb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bb94`](#insn-00c2bb94) → [`00c2bbdc`](#insn-00c2bbdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bba0`](#insn-00c2bba0) → [`00c2bbf0`](#insn-00c2bbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bbb0`](#insn-00c2bbb0) → [`00c2bbe8`](#insn-00c2bbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bbc8`](#insn-00c2bbc8) → [`00c2bbe8`](#insn-00c2bbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bbd0`](#insn-00c2bbd0) → [`00c2bb4c`](#insn-00c2bb4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bbec`](#insn-00c2bbec) → [`00c2bbdc`](#insn-00c2bbdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2bbf4`](#insn-00c2bbf4) → [`00c2bbdc`](#insn-00c2bbdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2bb08`](#insn-00c2bb08)

~~~json
{
  "source": "00c2bb08",
  "target": "00c2bb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb10`](#insn-00c2bb10)

~~~json
{
  "source": "00c2bb10",
  "target": "00c2bb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb1c`](#insn-00c2bb1c)

~~~json
{
  "source": "00c2bb1c",
  "target": "00c2bb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb38`](#insn-00c2bb38)

~~~json
{
  "source": "00c2bb38",
  "target": "00c2bbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb48`](#insn-00c2bb48)

~~~json
{
  "source": "00c2bb48",
  "target": "00c2bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb58`](#insn-00c2bb58)

~~~json
{
  "source": "00c2bb58",
  "target": "00c2bbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb60`](#insn-00c2bb60)

~~~json
{
  "source": "00c2bb60",
  "target": "00c2bbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb7c`](#insn-00c2bb7c)

~~~json
{
  "source": "00c2bb7c",
  "target": "00c2bb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb84`](#insn-00c2bb84)

~~~json
{
  "source": "00c2bb84",
  "target": "00c2bbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb90`](#insn-00c2bb90)

~~~json
{
  "source": "00c2bb90",
  "target": "00c2bb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bb94`](#insn-00c2bb94)

~~~json
{
  "source": "00c2bb94",
  "target": "00c2bbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bba0`](#insn-00c2bba0)

~~~json
{
  "source": "00c2bba0",
  "target": "00c2bbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bbb0`](#insn-00c2bbb0)

~~~json
{
  "source": "00c2bbb0",
  "target": "00c2bbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bbc8`](#insn-00c2bbc8)

~~~json
{
  "source": "00c2bbc8",
  "target": "00c2bbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bbd0`](#insn-00c2bbd0)

~~~json
{
  "source": "00c2bbd0",
  "target": "00c2bb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bbec`](#insn-00c2bbec)

~~~json
{
  "source": "00c2bbec",
  "target": "00c2bbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2bbf4`](#insn-00c2bbf4)

~~~json
{
  "source": "00c2bbf4",
  "target": "00c2bbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
