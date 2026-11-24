# 00badbfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00badbb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00badbb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-c901337b986a0c4a65facd4cea7c7620)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2a644`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a644.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-79b1d28907c526dc257a6f2c505dd3b1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badbfc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37837acb92e09c9e84a57dcd6c519b24eb27631f185b0fd061e2022485a11d23",
  "source_text_sha256": "37837acb92e09c9e84a57dcd6c519b24eb27631f185b0fd061e2022485a11d23",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badbfc",
        "00badcf7"
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
          goto LAB_00badcdc;
        }
                    /* catch() { ... } // from try @ 00bade98 with catch @ 00badcbc */
        if (((*(byte *)((long)param_3 + 3) & 0xfc) != 0xdc) ||
           (uVar5 = ((uint)(byte)param_3[1] | (*(byte *)((long)param_3 + 3) & 3) << 8 |
                    (uVar5 & 0x3ff) << 10) + 0x10000, uVar4 < uVar5)) goto LAB_00badce8;
        uVar2 = 4;
      }
      else {
        if (bVar1 == 0xdc) {
LAB_00badce8:
          uVar2 = 2;
          goto LAB_00badcdc;
        }
        uVar2 = 2;
        if (uVar4 < uVar5) goto LAB_00badcdc;
      }
      param_3 = (ushort *)((long)param_3 + uVar2);
      param_6 = puVar3 + 1;
      *puVar3 = uVar5;
      puVar3 = param_6;
    } while (param_3 < (ushort *)((long)param_4 + -1));
  }
  uVar2 = (ulong)(param_3 < param_4);
  puVar3 = param_6;
LAB_00badcdc:
  *param_5 = (ulong)param_3;
  *param_8 = puVar3;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badbfc"></a> `00badbfc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badc00"></a> `00badc00` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badc04"></a> `00badc04` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badc08"></a> `00badc08` | `4b 01 00 54` | b.lt 0x00badc30 | `CONDITIONAL_JUMP`
<a id="insn-00badc0c"></a> `00badc0c` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00badc10"></a> `00badc10` | `08 01 10 36` | tbz w8,#0x2,0x00badc30 | `CONDITIONAL_JUMP`
<a id="insn-00badc14"></a> `00badc14` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00badc18"></a> `00badc18` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badc1c"></a> `00badc1c` | `a1 00 00 54` | b.ne 0x00badc30 | `CONDITIONAL_JUMP`
<a id="insn-00badc20"></a> `00badc20` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badc24"></a> `00badc24` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00badc28"></a> `00badc28` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00badc2c"></a> `00badc2c` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00badc30"></a> `00badc30` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00badc34"></a> `00badc34` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badc38"></a> `00badc38` | `e2 04 00 54` | b.cs 0x00badcd4 | `CONDITIONAL_JUMP`
<a id="insn-00badc3c"></a> `00badc3c` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badc40"></a> `00badc40` | `0a 00 9b 52` | mov w10,#0xd800 | `FALL_THROUGH`
<a id="insn-00badc44"></a> `00badc44` | `0b 80 9b 52` | mov w11,#0xdc00 | `FALL_THROUGH`
<a id="insn-00badc48"></a> `00badc48` | `05 00 00 14` | b 0x00badc5c | `UNCONDITIONAL_JUMP`
<a id="insn-00badc4c"></a> `00badc4c` | `42 00 00 8b` | add x2,x2,x0 | `FALL_THROUGH`
<a id="insn-00badc50"></a> `00badc50` | `ac 44 00 b8` | str w12,[x5], #0x4 | `FALL_THROUGH`
<a id="insn-00badc54"></a> `00badc54` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badc58"></a> `00badc58` | `e2 03 00 54` | b.cs 0x00badcd4 | `CONDITIONAL_JUMP`
<a id="insn-00badc5c"></a> `00badc5c` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00badc60"></a> `00badc60` | `a2 03 00 54` | b.cs 0x00badcd4 | `CONDITIONAL_JUMP`
<a id="insn-00badc64"></a> `00badc64` | `4e 04 40 39` | ldrb w14,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badc68"></a> `00badc68` | `4c 00 40 39` | ldrb w12,[x2] | `FALL_THROUGH`
<a id="insn-00badc6c"></a> `00badc6c` | `cd 5d 18 53` | lsl w13,w14,#0x8 | `FALL_THROUGH`
<a id="insn-00badc70"></a> `00badc70` | `cc 1d 18 33` | bfm w12,w14,#0x18,#0x7 | `FALL_THROUGH`
<a id="insn-00badc74"></a> `00badc74` | `ad 15 16 12` | and w13,w13,#0xfc00 | `FALL_THROUGH`
<a id="insn-00badc78"></a> `00badc78` | `bf 01 0a 6b` | cmp w13,w10 | `FALL_THROUGH`
<a id="insn-00badc7c"></a> `00badc7c` | `e0 00 00 54` | b.eq 0x00badc98 | `CONDITIONAL_JUMP`
<a id="insn-00badc80"></a> `00badc80` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00badc84"></a> `00badc84` | `20 03 00 54` | b.eq 0x00badce8 | `CONDITIONAL_JUMP`
<a id="insn-00badc88"></a> `00badc88` | `3f 41 2c eb` | cmp x9,w12, UXTW  | `FALL_THROUGH`
<a id="insn-00badc8c"></a> `00badc8c` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badc90"></a> `00badc90` | `e2 fd ff 54` | b.cs 0x00badc4c | `CONDITIONAL_JUMP`
<a id="insn-00badc94"></a> `00badc94` | `12 00 00 14` | b 0x00badcdc | `UNCONDITIONAL_JUMP`
<a id="insn-00badc98"></a> `00badc98` | `6d 00 02 cb` | sub x13,x3,x2 | `FALL_THROUGH`
<a id="insn-00badc9c"></a> `00badc9c` | `bf 11 00 f1` | cmp x13,#0x4 | `FALL_THROUGH`
<a id="insn-00badca0"></a> `00badca0` | `8b 02 00 54` | b.lt 0x00badcf0 | `CONDITIONAL_JUMP`
<a id="insn-00badca4"></a> `00badca4` | `4d 0c 40 39` | ldrb w13,[x2, #0x3] | `FALL_THROUGH`
<a id="insn-00badca8"></a> `00badca8` | `ae 15 1e 12` | and w14,w13,#0xfc | `FALL_THROUGH`
<a id="insn-00badcac"></a> `00badcac` | `df 71 03 71` | cmp w14,#0xdc | `FALL_THROUGH`
<a id="insn-00badcb0"></a> `00badcb0` | `c1 01 00 54` | b.ne 0x00badce8 | `CONDITIONAL_JUMP`
<a id="insn-00badcb4"></a> `00badcb4` | `4e 08 40 39` | ldrb w14,[x2, #0x2] | `FALL_THROUGH`
<a id="insn-00badcb8"></a> `00badcb8` | `ae 05 18 33` | bfm w14,w13,#0x18,#0x1 | `FALL_THROUGH`
<a id="insn-00badcbc"></a> `00badcbc` | `8e 25 16 33` | bfm w14,w12,#0x16,#0x9 | `FALL_THROUGH`
<a id="insn-00badcc0"></a> `00badcc0` | `cc 41 40 11` | add w12,w14,#0x10, LSL #12 | `FALL_THROUGH`
<a id="insn-00badcc4"></a> `00badcc4` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00badcc8"></a> `00badcc8` | `03 01 00 54` | b.cc 0x00badce8 | `CONDITIONAL_JUMP`
<a id="insn-00badccc"></a> `00badccc` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00badcd0"></a> `00badcd0` | `df ff ff 17` | b 0x00badc4c | `UNCONDITIONAL_JUMP`
<a id="insn-00badcd4"></a> `00badcd4` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00badcd8"></a> `00badcd8` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00badcdc"></a> `00badcdc` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00badce0"></a> `00badce0` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00badce4"></a> `00badce4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00badce8"></a> `00badce8` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badcec"></a> `00badcec` | `fc ff ff 17` | b 0x00badcdc | `UNCONDITIONAL_JUMP`
<a id="insn-00badcf0"></a> `00badcf0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00badcf4"></a> `00badcf4` | `fa ff ff 17` | b 0x00badcdc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00badbfc`](#insn-00badbfc) 範囲 `[['00badbfc', '00badc0b']]`
  - `CONDITIONAL_JUMP` [`00badc08`](#insn-00badc08) → [`00badc30`](#insn-00badc30)
  - `FALL_THROUGH` [`00badc08`](#insn-00badc08) → [`00badc0c`](#insn-00badc0c)
- ブロック [`00badc0c`](#insn-00badc0c) 範囲 `[['00badc0c', '00badc13']]`
  - `CONDITIONAL_JUMP` [`00badc10`](#insn-00badc10) → [`00badc30`](#insn-00badc30)
  - `FALL_THROUGH` [`00badc10`](#insn-00badc10) → [`00badc14`](#insn-00badc14)
- ブロック [`00badc14`](#insn-00badc14) 範囲 `[['00badc14', '00badc1f']]`
  - `CONDITIONAL_JUMP` [`00badc1c`](#insn-00badc1c) → [`00badc30`](#insn-00badc30)
  - `FALL_THROUGH` [`00badc1c`](#insn-00badc1c) → [`00badc20`](#insn-00badc20)
- ブロック [`00badc20`](#insn-00badc20) 範囲 `[['00badc20', '00badc2f']]`
  - `FALL_THROUGH` [`00badc2c`](#insn-00badc2c) → [`00badc30`](#insn-00badc30)
- ブロック [`00badc30`](#insn-00badc30) 範囲 `[['00badc30', '00badc3b']]`
  - `CONDITIONAL_JUMP` [`00badc38`](#insn-00badc38) → [`00badcd4`](#insn-00badcd4)
  - `FALL_THROUGH` [`00badc38`](#insn-00badc38) → [`00badc3c`](#insn-00badc3c)
- ブロック [`00badc3c`](#insn-00badc3c) 範囲 `[['00badc3c', '00badc4b']]`
  - `UNCONDITIONAL_JUMP` [`00badc48`](#insn-00badc48) → [`00badc5c`](#insn-00badc5c)
- ブロック [`00badc4c`](#insn-00badc4c) 範囲 `[['00badc4c', '00badc5b']]`
  - `CONDITIONAL_JUMP` [`00badc58`](#insn-00badc58) → [`00badcd4`](#insn-00badcd4)
  - `FALL_THROUGH` [`00badc58`](#insn-00badc58) → [`00badc5c`](#insn-00badc5c)
- ブロック [`00badc5c`](#insn-00badc5c) 範囲 `[['00badc5c', '00badc63']]`
  - `CONDITIONAL_JUMP` [`00badc60`](#insn-00badc60) → [`00badcd4`](#insn-00badcd4)
  - `FALL_THROUGH` [`00badc60`](#insn-00badc60) → [`00badc64`](#insn-00badc64)
- ブロック [`00badc64`](#insn-00badc64) 範囲 `[['00badc64', '00badc7f']]`
  - `CONDITIONAL_JUMP` [`00badc7c`](#insn-00badc7c) → [`00badc98`](#insn-00badc98)
  - `FALL_THROUGH` [`00badc7c`](#insn-00badc7c) → [`00badc80`](#insn-00badc80)
- ブロック [`00badc80`](#insn-00badc80) 範囲 `[['00badc80', '00badc87']]`
  - `CONDITIONAL_JUMP` [`00badc84`](#insn-00badc84) → [`00badce8`](#insn-00badce8)
  - `FALL_THROUGH` [`00badc84`](#insn-00badc84) → [`00badc88`](#insn-00badc88)
- ブロック [`00badc88`](#insn-00badc88) 範囲 `[['00badc88', '00badc93']]`
  - `CONDITIONAL_JUMP` [`00badc90`](#insn-00badc90) → [`00badc4c`](#insn-00badc4c)
  - `FALL_THROUGH` [`00badc90`](#insn-00badc90) → [`00badc94`](#insn-00badc94)
- ブロック [`00badc94`](#insn-00badc94) 範囲 `[['00badc94', '00badc97']]`
  - `UNCONDITIONAL_JUMP` [`00badc94`](#insn-00badc94) → [`00badcdc`](#insn-00badcdc)
- ブロック [`00badc98`](#insn-00badc98) 範囲 `[['00badc98', '00badca3']]`
  - `CONDITIONAL_JUMP` [`00badca0`](#insn-00badca0) → [`00badcf0`](#insn-00badcf0)
  - `FALL_THROUGH` [`00badca0`](#insn-00badca0) → [`00badca4`](#insn-00badca4)
- ブロック [`00badca4`](#insn-00badca4) 範囲 `[['00badca4', '00badcb3']]`
  - `CONDITIONAL_JUMP` [`00badcb0`](#insn-00badcb0) → [`00badce8`](#insn-00badce8)
  - `FALL_THROUGH` [`00badcb0`](#insn-00badcb0) → [`00badcb4`](#insn-00badcb4)
- ブロック [`00badcb4`](#insn-00badcb4) 範囲 `[['00badcb4', '00badcbb']]`
  - `FALL_THROUGH` [`00badcb8`](#insn-00badcb8) → [`00badcbc`](#insn-00badcbc)
- ブロック [`00badcbc`](#insn-00badcbc) 範囲 `[['00badcbc', '00badccb']]`
  - `CONDITIONAL_JUMP` [`00badcc8`](#insn-00badcc8) → [`00badce8`](#insn-00badce8)
  - `FALL_THROUGH` [`00badcc8`](#insn-00badcc8) → [`00badccc`](#insn-00badccc)
- ブロック [`00badccc`](#insn-00badccc) 範囲 `[['00badccc', '00badcd3']]`
  - `UNCONDITIONAL_JUMP` [`00badcd0`](#insn-00badcd0) → [`00badc4c`](#insn-00badc4c)
- ブロック [`00badcd4`](#insn-00badcd4) 範囲 `[['00badcd4', '00badcdb']]`
  - `FALL_THROUGH` [`00badcd8`](#insn-00badcd8) → [`00badcdc`](#insn-00badcdc)
- ブロック [`00badcdc`](#insn-00badcdc) 範囲 `[['00badcdc', '00badce7']]`
- ブロック [`00badce8`](#insn-00badce8) 範囲 `[['00badce8', '00badcef']]`
  - `UNCONDITIONAL_JUMP` [`00badcec`](#insn-00badcec) → [`00badcdc`](#insn-00badcdc)
- ブロック [`00badcf0`](#insn-00badcf0) 範囲 `[['00badcf0', '00badcf7']]`
  - `UNCONDITIONAL_JUMP` [`00badcf4`](#insn-00badcf4) → [`00badcdc`](#insn-00badcdc)

## 命令位置別の参照

- [`00badc08`](#insn-00badc08) → [`00badc30`](#insn-00badc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc10`](#insn-00badc10) → [`00badc30`](#insn-00badc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc1c`](#insn-00badc1c) → [`00badc30`](#insn-00badc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc38`](#insn-00badc38) → [`00badcd4`](#insn-00badcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc48`](#insn-00badc48) → [`00badc5c`](#insn-00badc5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc58`](#insn-00badc58) → [`00badcd4`](#insn-00badcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc60`](#insn-00badc60) → [`00badcd4`](#insn-00badcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc7c`](#insn-00badc7c) → [`00badc98`](#insn-00badc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc84`](#insn-00badc84) → [`00badce8`](#insn-00badce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc90`](#insn-00badc90) → [`00badc4c`](#insn-00badc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc94`](#insn-00badc94) → [`00badcdc`](#insn-00badcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badca0`](#insn-00badca0) → [`00badcf0`](#insn-00badcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badcb0`](#insn-00badcb0) → [`00badce8`](#insn-00badce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badcc8`](#insn-00badcc8) → [`00badce8`](#insn-00badce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badcd0`](#insn-00badcd0) → [`00badc4c`](#insn-00badc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badcec`](#insn-00badcec) → [`00badcdc`](#insn-00badcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badcf4`](#insn-00badcf4) → [`00badcdc`](#insn-00badcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badc08`](#insn-00badc08)

~~~json
{
  "source": "00badc08",
  "target": "00badc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc10`](#insn-00badc10)

~~~json
{
  "source": "00badc10",
  "target": "00badc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc1c`](#insn-00badc1c)

~~~json
{
  "source": "00badc1c",
  "target": "00badc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc38`](#insn-00badc38)

~~~json
{
  "source": "00badc38",
  "target": "00badcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc48`](#insn-00badc48)

~~~json
{
  "source": "00badc48",
  "target": "00badc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc58`](#insn-00badc58)

~~~json
{
  "source": "00badc58",
  "target": "00badcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc60`](#insn-00badc60)

~~~json
{
  "source": "00badc60",
  "target": "00badcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc7c`](#insn-00badc7c)

~~~json
{
  "source": "00badc7c",
  "target": "00badc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc84`](#insn-00badc84)

~~~json
{
  "source": "00badc84",
  "target": "00badce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc90`](#insn-00badc90)

~~~json
{
  "source": "00badc90",
  "target": "00badc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc94`](#insn-00badc94)

~~~json
{
  "source": "00badc94",
  "target": "00badcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badca0`](#insn-00badca0)

~~~json
{
  "source": "00badca0",
  "target": "00badcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badcb0`](#insn-00badcb0)

~~~json
{
  "source": "00badcb0",
  "target": "00badce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badcc8`](#insn-00badcc8)

~~~json
{
  "source": "00badcc8",
  "target": "00badce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badcd0`](#insn-00badcd0)

~~~json
{
  "source": "00badcd0",
  "target": "00badc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badcec`](#insn-00badcec)

~~~json
{
  "source": "00badcec",
  "target": "00badcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badcf4`](#insn-00badcf4)

~~~json
{
  "source": "00badcf4",
  "target": "00badcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
