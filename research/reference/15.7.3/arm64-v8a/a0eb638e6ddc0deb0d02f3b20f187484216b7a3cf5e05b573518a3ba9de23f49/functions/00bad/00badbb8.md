# 00badbb8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00badaf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00badaf0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-97511b69e4ae7d856b5b18d9b679c0c3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00badbfc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badbfc.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-c901337b986a0c4a65facd4cea7c7620)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badbb8",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db188caf9805f6a585c4ed45b09928bb8cd4cf7f04393b327a7da688d8c9601f",
  "source_text_sha256": "db188caf9805f6a585c4ed45b09928bb8cd4cf7f04393b327a7da688d8c9601f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badbb8",
        "00badcb3"
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
          goto LAB_00badc98;
        }
                    /* catch() { ... } // from try @ 00bade54 with catch @ 00badc78 */
        if (((*(byte *)((long)param_3 + 3) & 0xfc) != 0xdc) ||
           (uVar5 = ((uint)(byte)param_3[1] | (*(byte *)((long)param_3 + 3) & 3) << 8 |
                    (uVar5 & 0x3ff) << 10) + 0x10000, uVar4 < uVar5)) goto LAB_00badca4;
        uVar2 = 4;
      }
      else {
        if (bVar1 == 0xdc) {
LAB_00badca4:
          uVar2 = 2;
          goto LAB_00badc98;
        }
        uVar2 = 2;
        if (uVar4 < uVar5) goto LAB_00badc98;
      }
      param_3 = (ushort *)((long)param_3 + uVar2);
      param_6 = puVar3 + 1;
      *puVar3 = uVar5;
      puVar3 = param_6;
    } while (param_3 < (ushort *)((long)param_4 + -1));
  }
  uVar2 = (ulong)(param_3 < param_4);
  puVar3 = param_6;
LAB_00badc98:
  *param_5 = (ulong)param_3;
  *param_8 = puVar3;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badbb8"></a> `00badbb8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badbbc"></a> `00badbbc` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badbc0"></a> `00badbc0` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badbc4"></a> `00badbc4` | `4b 01 00 54` | b.lt 0x00badbec | `CONDITIONAL_JUMP`
<a id="insn-00badbc8"></a> `00badbc8` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00badbcc"></a> `00badbcc` | `08 01 10 36` | tbz w8,#0x2,0x00badbec | `CONDITIONAL_JUMP`
<a id="insn-00badbd0"></a> `00badbd0` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00badbd4"></a> `00badbd4` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badbd8"></a> `00badbd8` | `a1 00 00 54` | b.ne 0x00badbec | `CONDITIONAL_JUMP`
<a id="insn-00badbdc"></a> `00badbdc` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badbe0"></a> `00badbe0` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00badbe4"></a> `00badbe4` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00badbe8"></a> `00badbe8` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00badbec"></a> `00badbec` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00badbf0"></a> `00badbf0` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badbf4"></a> `00badbf4` | `e2 04 00 54` | b.cs 0x00badc90 | `CONDITIONAL_JUMP`
<a id="insn-00badbf8"></a> `00badbf8` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badbfc"></a> `00badbfc` | `0a 00 9b 52` | mov w10,#0xd800 | `FALL_THROUGH`
<a id="insn-00badc00"></a> `00badc00` | `0b 80 9b 52` | mov w11,#0xdc00 | `FALL_THROUGH`
<a id="insn-00badc04"></a> `00badc04` | `05 00 00 14` | b 0x00badc18 | `UNCONDITIONAL_JUMP`
<a id="insn-00badc08"></a> `00badc08` | `42 00 00 8b` | add x2,x2,x0 | `FALL_THROUGH`
<a id="insn-00badc0c"></a> `00badc0c` | `ac 44 00 b8` | str w12,[x5], #0x4 | `FALL_THROUGH`
<a id="insn-00badc10"></a> `00badc10` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badc14"></a> `00badc14` | `e2 03 00 54` | b.cs 0x00badc90 | `CONDITIONAL_JUMP`
<a id="insn-00badc18"></a> `00badc18` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00badc1c"></a> `00badc1c` | `a2 03 00 54` | b.cs 0x00badc90 | `CONDITIONAL_JUMP`
<a id="insn-00badc20"></a> `00badc20` | `4e 04 40 39` | ldrb w14,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badc24"></a> `00badc24` | `4c 00 40 39` | ldrb w12,[x2] | `FALL_THROUGH`
<a id="insn-00badc28"></a> `00badc28` | `cd 5d 18 53` | lsl w13,w14,#0x8 | `FALL_THROUGH`
<a id="insn-00badc2c"></a> `00badc2c` | `cc 1d 18 33` | bfm w12,w14,#0x18,#0x7 | `FALL_THROUGH`
<a id="insn-00badc30"></a> `00badc30` | `ad 15 16 12` | and w13,w13,#0xfc00 | `FALL_THROUGH`
<a id="insn-00badc34"></a> `00badc34` | `bf 01 0a 6b` | cmp w13,w10 | `FALL_THROUGH`
<a id="insn-00badc38"></a> `00badc38` | `e0 00 00 54` | b.eq 0x00badc54 | `CONDITIONAL_JUMP`
<a id="insn-00badc3c"></a> `00badc3c` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00badc40"></a> `00badc40` | `20 03 00 54` | b.eq 0x00badca4 | `CONDITIONAL_JUMP`
<a id="insn-00badc44"></a> `00badc44` | `3f 41 2c eb` | cmp x9,w12, UXTW  | `FALL_THROUGH`
<a id="insn-00badc48"></a> `00badc48` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badc4c"></a> `00badc4c` | `e2 fd ff 54` | b.cs 0x00badc08 | `CONDITIONAL_JUMP`
<a id="insn-00badc50"></a> `00badc50` | `12 00 00 14` | b 0x00badc98 | `UNCONDITIONAL_JUMP`
<a id="insn-00badc54"></a> `00badc54` | `6d 00 02 cb` | sub x13,x3,x2 | `FALL_THROUGH`
<a id="insn-00badc58"></a> `00badc58` | `bf 11 00 f1` | cmp x13,#0x4 | `FALL_THROUGH`
<a id="insn-00badc5c"></a> `00badc5c` | `8b 02 00 54` | b.lt 0x00badcac | `CONDITIONAL_JUMP`
<a id="insn-00badc60"></a> `00badc60` | `4d 0c 40 39` | ldrb w13,[x2, #0x3] | `FALL_THROUGH`
<a id="insn-00badc64"></a> `00badc64` | `ae 15 1e 12` | and w14,w13,#0xfc | `FALL_THROUGH`
<a id="insn-00badc68"></a> `00badc68` | `df 71 03 71` | cmp w14,#0xdc | `FALL_THROUGH`
<a id="insn-00badc6c"></a> `00badc6c` | `c1 01 00 54` | b.ne 0x00badca4 | `CONDITIONAL_JUMP`
<a id="insn-00badc70"></a> `00badc70` | `4e 08 40 39` | ldrb w14,[x2, #0x2] | `FALL_THROUGH`
<a id="insn-00badc74"></a> `00badc74` | `ae 05 18 33` | bfm w14,w13,#0x18,#0x1 | `FALL_THROUGH`
<a id="insn-00badc78"></a> `00badc78` | `8e 25 16 33` | bfm w14,w12,#0x16,#0x9 | `FALL_THROUGH`
<a id="insn-00badc7c"></a> `00badc7c` | `cc 41 40 11` | add w12,w14,#0x10, LSL #12 | `FALL_THROUGH`
<a id="insn-00badc80"></a> `00badc80` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00badc84"></a> `00badc84` | `03 01 00 54` | b.cc 0x00badca4 | `CONDITIONAL_JUMP`
<a id="insn-00badc88"></a> `00badc88` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00badc8c"></a> `00badc8c` | `df ff ff 17` | b 0x00badc08 | `UNCONDITIONAL_JUMP`
<a id="insn-00badc90"></a> `00badc90` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00badc94"></a> `00badc94` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00badc98"></a> `00badc98` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00badc9c"></a> `00badc9c` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00badca0"></a> `00badca0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00badca4"></a> `00badca4` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badca8"></a> `00badca8` | `fc ff ff 17` | b 0x00badc98 | `UNCONDITIONAL_JUMP`
<a id="insn-00badcac"></a> `00badcac` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00badcb0"></a> `00badcb0` | `fa ff ff 17` | b 0x00badc98 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00badbb8`](#insn-00badbb8) 範囲 `[['00badbb8', '00badbc7']]`
  - `CONDITIONAL_JUMP` [`00badbc4`](#insn-00badbc4) → [`00badbec`](#insn-00badbec)
  - `FALL_THROUGH` [`00badbc4`](#insn-00badbc4) → [`00badbc8`](#insn-00badbc8)
- ブロック [`00badbc8`](#insn-00badbc8) 範囲 `[['00badbc8', '00badbcf']]`
  - `CONDITIONAL_JUMP` [`00badbcc`](#insn-00badbcc) → [`00badbec`](#insn-00badbec)
  - `FALL_THROUGH` [`00badbcc`](#insn-00badbcc) → [`00badbd0`](#insn-00badbd0)
- ブロック [`00badbd0`](#insn-00badbd0) 範囲 `[['00badbd0', '00badbdb']]`
  - `CONDITIONAL_JUMP` [`00badbd8`](#insn-00badbd8) → [`00badbec`](#insn-00badbec)
  - `FALL_THROUGH` [`00badbd8`](#insn-00badbd8) → [`00badbdc`](#insn-00badbdc)
- ブロック [`00badbdc`](#insn-00badbdc) 範囲 `[['00badbdc', '00badbeb']]`
  - `FALL_THROUGH` [`00badbe8`](#insn-00badbe8) → [`00badbec`](#insn-00badbec)
- ブロック [`00badbec`](#insn-00badbec) 範囲 `[['00badbec', '00badbf7']]`
  - `CONDITIONAL_JUMP` [`00badbf4`](#insn-00badbf4) → [`00badc90`](#insn-00badc90)
  - `FALL_THROUGH` [`00badbf4`](#insn-00badbf4) → [`00badbf8`](#insn-00badbf8)
- ブロック [`00badbf8`](#insn-00badbf8) 範囲 `[['00badbf8', '00badc07']]`
  - `UNCONDITIONAL_JUMP` [`00badc04`](#insn-00badc04) → [`00badc18`](#insn-00badc18)
- ブロック [`00badc08`](#insn-00badc08) 範囲 `[['00badc08', '00badc17']]`
  - `CONDITIONAL_JUMP` [`00badc14`](#insn-00badc14) → [`00badc90`](#insn-00badc90)
  - `FALL_THROUGH` [`00badc14`](#insn-00badc14) → [`00badc18`](#insn-00badc18)
- ブロック [`00badc18`](#insn-00badc18) 範囲 `[['00badc18', '00badc1f']]`
  - `CONDITIONAL_JUMP` [`00badc1c`](#insn-00badc1c) → [`00badc90`](#insn-00badc90)
  - `FALL_THROUGH` [`00badc1c`](#insn-00badc1c) → [`00badc20`](#insn-00badc20)
- ブロック [`00badc20`](#insn-00badc20) 範囲 `[['00badc20', '00badc3b']]`
  - `CONDITIONAL_JUMP` [`00badc38`](#insn-00badc38) → [`00badc54`](#insn-00badc54)
  - `FALL_THROUGH` [`00badc38`](#insn-00badc38) → [`00badc3c`](#insn-00badc3c)
- ブロック [`00badc3c`](#insn-00badc3c) 範囲 `[['00badc3c', '00badc43']]`
  - `CONDITIONAL_JUMP` [`00badc40`](#insn-00badc40) → [`00badca4`](#insn-00badca4)
  - `FALL_THROUGH` [`00badc40`](#insn-00badc40) → [`00badc44`](#insn-00badc44)
- ブロック [`00badc44`](#insn-00badc44) 範囲 `[['00badc44', '00badc4f']]`
  - `CONDITIONAL_JUMP` [`00badc4c`](#insn-00badc4c) → [`00badc08`](#insn-00badc08)
  - `FALL_THROUGH` [`00badc4c`](#insn-00badc4c) → [`00badc50`](#insn-00badc50)
- ブロック [`00badc50`](#insn-00badc50) 範囲 `[['00badc50', '00badc53']]`
  - `UNCONDITIONAL_JUMP` [`00badc50`](#insn-00badc50) → [`00badc98`](#insn-00badc98)
- ブロック [`00badc54`](#insn-00badc54) 範囲 `[['00badc54', '00badc5f']]`
  - `CONDITIONAL_JUMP` [`00badc5c`](#insn-00badc5c) → [`00badcac`](#insn-00badcac)
  - `FALL_THROUGH` [`00badc5c`](#insn-00badc5c) → [`00badc60`](#insn-00badc60)
- ブロック [`00badc60`](#insn-00badc60) 範囲 `[['00badc60', '00badc6f']]`
  - `CONDITIONAL_JUMP` [`00badc6c`](#insn-00badc6c) → [`00badca4`](#insn-00badca4)
  - `FALL_THROUGH` [`00badc6c`](#insn-00badc6c) → [`00badc70`](#insn-00badc70)
- ブロック [`00badc70`](#insn-00badc70) 範囲 `[['00badc70', '00badc77']]`
  - `FALL_THROUGH` [`00badc74`](#insn-00badc74) → [`00badc78`](#insn-00badc78)
- ブロック [`00badc78`](#insn-00badc78) 範囲 `[['00badc78', '00badc87']]`
  - `CONDITIONAL_JUMP` [`00badc84`](#insn-00badc84) → [`00badca4`](#insn-00badca4)
  - `FALL_THROUGH` [`00badc84`](#insn-00badc84) → [`00badc88`](#insn-00badc88)
- ブロック [`00badc88`](#insn-00badc88) 範囲 `[['00badc88', '00badc8f']]`
  - `UNCONDITIONAL_JUMP` [`00badc8c`](#insn-00badc8c) → [`00badc08`](#insn-00badc08)
- ブロック [`00badc90`](#insn-00badc90) 範囲 `[['00badc90', '00badc97']]`
  - `FALL_THROUGH` [`00badc94`](#insn-00badc94) → [`00badc98`](#insn-00badc98)
- ブロック [`00badc98`](#insn-00badc98) 範囲 `[['00badc98', '00badca3']]`
- ブロック [`00badca4`](#insn-00badca4) 範囲 `[['00badca4', '00badcab']]`
  - `UNCONDITIONAL_JUMP` [`00badca8`](#insn-00badca8) → [`00badc98`](#insn-00badc98)
- ブロック [`00badcac`](#insn-00badcac) 範囲 `[['00badcac', '00badcb3']]`
  - `UNCONDITIONAL_JUMP` [`00badcb0`](#insn-00badcb0) → [`00badc98`](#insn-00badc98)

## 命令位置別の参照

- [`00badbc4`](#insn-00badbc4) → [`00badbec`](#insn-00badbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badbcc`](#insn-00badbcc) → [`00badbec`](#insn-00badbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badbd8`](#insn-00badbd8) → [`00badbec`](#insn-00badbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badbf4`](#insn-00badbf4) → [`00badc90`](#insn-00badc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc04`](#insn-00badc04) → [`00badc18`](#insn-00badc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc14`](#insn-00badc14) → [`00badc90`](#insn-00badc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc1c`](#insn-00badc1c) → [`00badc90`](#insn-00badc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc38`](#insn-00badc38) → [`00badc54`](#insn-00badc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc40`](#insn-00badc40) → [`00badca4`](#insn-00badca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc4c`](#insn-00badc4c) → [`00badc08`](#insn-00badc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc50`](#insn-00badc50) → [`00badc98`](#insn-00badc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc5c`](#insn-00badc5c) → [`00badcac`](#insn-00badcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc6c`](#insn-00badc6c) → [`00badca4`](#insn-00badca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc84`](#insn-00badc84) → [`00badca4`](#insn-00badca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc8c`](#insn-00badc8c) → [`00badc08`](#insn-00badc08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badca8`](#insn-00badca8) → [`00badc98`](#insn-00badc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badcb0`](#insn-00badcb0) → [`00badc98`](#insn-00badc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badbc4`](#insn-00badbc4)

~~~json
{
  "source": "00badbc4",
  "target": "00badbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badbcc`](#insn-00badbcc)

~~~json
{
  "source": "00badbcc",
  "target": "00badbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badbd8`](#insn-00badbd8)

~~~json
{
  "source": "00badbd8",
  "target": "00badbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badbf4`](#insn-00badbf4)

~~~json
{
  "source": "00badbf4",
  "target": "00badc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc04`](#insn-00badc04)

~~~json
{
  "source": "00badc04",
  "target": "00badc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc14`](#insn-00badc14)

~~~json
{
  "source": "00badc14",
  "target": "00badc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc1c`](#insn-00badc1c)

~~~json
{
  "source": "00badc1c",
  "target": "00badc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc38`](#insn-00badc38)

~~~json
{
  "source": "00badc38",
  "target": "00badc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc40`](#insn-00badc40)

~~~json
{
  "source": "00badc40",
  "target": "00badca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc4c`](#insn-00badc4c)

~~~json
{
  "source": "00badc4c",
  "target": "00badc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc50`](#insn-00badc50)

~~~json
{
  "source": "00badc50",
  "target": "00badc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc5c`](#insn-00badc5c)

~~~json
{
  "source": "00badc5c",
  "target": "00badcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc6c`](#insn-00badc6c)

~~~json
{
  "source": "00badc6c",
  "target": "00badca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc84`](#insn-00badc84)

~~~json
{
  "source": "00badc84",
  "target": "00badca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc8c`](#insn-00badc8c)

~~~json
{
  "source": "00badc8c",
  "target": "00badc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badca8`](#insn-00badca8)

~~~json
{
  "source": "00badca8",
  "target": "00badc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badcb0`](#insn-00badcb0)

~~~json
{
  "source": "00badcb0",
  "target": "00badc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
