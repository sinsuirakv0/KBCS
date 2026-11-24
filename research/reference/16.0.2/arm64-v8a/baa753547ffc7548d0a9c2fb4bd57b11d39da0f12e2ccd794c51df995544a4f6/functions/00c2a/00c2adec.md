# 00c2adec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2ad50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2ad50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0009.md#compare-256c4b1c093a41565af1b2d171e3c649)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c2bde0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2b/00c2bde0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/detail_skipped-0009.md#compare-44ed9c047765351be409c267684b39b7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2adec",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d77bfa624d821a71994479c7025ea29c0469df005771d99bc12a7936de86213",
  "source_text_sha256": "5d77bfa624d821a71994479c7025ea29c0469df005771d99bc12a7936de86213",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2adec",
        "00c2ae7f"
      ]
    ],
    "bytes_sha256": "b3a7ca12fc2fe93be1a2845088b697c23a965f353ad87eeaf08c86309dd99fe1",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
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

## 疑似コード / UTF-8 1397 bytes

~~~c

undefined1
_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_
          (long param_1,undefined8 param_2,byte *param_3,byte *param_4,ulong *param_5,
          ushort *param_6,ushort *param_7,undefined8 *param_8)

{
  ushort uVar1;
  undefined1 uVar2;
  ushort *puVar3;
  ulong uVar4;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == 0xfe)) {
    param_3 = param_3 + (ulong)(param_3[1] == 0xff) * 2;
  }
  if (param_3 < param_4 + -1) {
    uVar4 = *(ulong *)(param_1 + 0x10);
    uVar2 = 2;
    puVar3 = param_6;
    while (param_6 = puVar3, puVar3 < param_7) {
                    /* catch() { ... } // from try @ 00c2ad50 with catch @ 00c2ae50 */
      if (((*param_3 & 0xf8) == 0xd8) || (uVar1 = CONCAT11(*param_3,param_3[1]), uVar4 < uVar1))
      goto LAB_00c2ae74;
      param_3 = param_3 + 2;
      param_6 = puVar3 + 1;
      *puVar3 = uVar1;
      puVar3 = param_6;
      if (param_4 + -1 <= param_3) break;
    }
  }
  uVar2 = param_3 < param_4;
LAB_00c2ae74:
  *param_5 = (ulong)param_3;
                    /* try { // try from 00c2ae78 to 00d2af27 has its CatchHandler @ 00c2ae78
                       catch() { ... } // from try @ 00c2ae78 with catch @ 00c2ae78
                       catch() { ... } // from try @ 00c2af3c with catch @ 00c2ae78 */
  *param_8 = param_6;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2adec"></a> `00c2adec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c2adf0"></a> `00c2adf0` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00c2adf4"></a> `00c2adf4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c2adf8"></a> `00c2adf8` | `4b 01 00 54` | b.lt 0x00c2ae20 | `CONDITIONAL_JUMP`
<a id="insn-00c2adfc"></a> `00c2adfc` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c2ae00"></a> `00c2ae00` | `08 01 10 36` | tbz w8,#0x2,0x00c2ae20 | `CONDITIONAL_JUMP`
<a id="insn-00c2ae04"></a> `00c2ae04` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00c2ae08"></a> `00c2ae08` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00c2ae0c"></a> `00c2ae0c` | `a1 00 00 54` | b.ne 0x00c2ae20 | `CONDITIONAL_JUMP`
<a id="insn-00c2ae10"></a> `00c2ae10` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00c2ae14"></a> `00c2ae14` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00c2ae18"></a> `00c2ae18` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00c2ae1c"></a> `00c2ae1c` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00c2ae20"></a> `00c2ae20` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00c2ae24"></a> `00c2ae24` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00c2ae28"></a> `00c2ae28` | `22 02 00 54` | b.cs 0x00c2ae6c | `CONDITIONAL_JUMP`
<a id="insn-00c2ae2c"></a> `00c2ae2c` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c2ae30"></a> `00c2ae30` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00c2ae34"></a> `00c2ae34` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00c2ae38"></a> `00c2ae38` | `a2 01 00 54` | b.cs 0x00c2ae6c | `CONDITIONAL_JUMP`
<a id="insn-00c2ae3c"></a> `00c2ae3c` | `4a 00 40 39` | ldrb w10,[x2] | `FALL_THROUGH`
<a id="insn-00c2ae40"></a> `00c2ae40` | `4b 11 1d 12` | and w11,w10,#0xf8 | `FALL_THROUGH`
<a id="insn-00c2ae44"></a> `00c2ae44` | `7f 61 03 71` | cmp w11,#0xd8 | `FALL_THROUGH`
<a id="insn-00c2ae48"></a> `00c2ae48` | `60 01 00 54` | b.eq 0x00c2ae74 | `CONDITIONAL_JUMP`
<a id="insn-00c2ae4c"></a> `00c2ae4c` | `4b 04 40 39` | ldrb w11,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00c2ae50"></a> `00c2ae50` | `6a 21 0a 2a` | orr w10,w11,w10, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00c2ae54"></a> `00c2ae54` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c2ae58"></a> `00c2ae58` | `e3 00 00 54` | b.cc 0x00c2ae74 | `CONDITIONAL_JUMP`
<a id="insn-00c2ae5c"></a> `00c2ae5c` | `42 08 00 91` | add x2,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00c2ae60"></a> `00c2ae60` | `aa 24 00 78` | strh w10,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00c2ae64"></a> `00c2ae64` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00c2ae68"></a> `00c2ae68` | `63 fe ff 54` | b.cc 0x00c2ae34 | `CONDITIONAL_JUMP`
<a id="insn-00c2ae6c"></a> `00c2ae6c` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00c2ae70"></a> `00c2ae70` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00c2ae74"></a> `00c2ae74` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00c2ae78"></a> `00c2ae78` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00c2ae7c"></a> `00c2ae7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c2adec`](#insn-00c2adec) 範囲 `[['00c2adec', '00c2adfb']]`
  - `CONDITIONAL_JUMP` [`00c2adf8`](#insn-00c2adf8) → [`00c2ae20`](#insn-00c2ae20)
  - `FALL_THROUGH` [`00c2adf8`](#insn-00c2adf8) → [`00c2adfc`](#insn-00c2adfc)
- ブロック [`00c2adfc`](#insn-00c2adfc) 範囲 `[['00c2adfc', '00c2ae03']]`
  - `CONDITIONAL_JUMP` [`00c2ae00`](#insn-00c2ae00) → [`00c2ae20`](#insn-00c2ae20)
  - `FALL_THROUGH` [`00c2ae00`](#insn-00c2ae00) → [`00c2ae04`](#insn-00c2ae04)
- ブロック [`00c2ae04`](#insn-00c2ae04) 範囲 `[['00c2ae04', '00c2ae0f']]`
  - `CONDITIONAL_JUMP` [`00c2ae0c`](#insn-00c2ae0c) → [`00c2ae20`](#insn-00c2ae20)
  - `FALL_THROUGH` [`00c2ae0c`](#insn-00c2ae0c) → [`00c2ae10`](#insn-00c2ae10)
- ブロック [`00c2ae10`](#insn-00c2ae10) 範囲 `[['00c2ae10', '00c2ae1f']]`
  - `FALL_THROUGH` [`00c2ae1c`](#insn-00c2ae1c) → [`00c2ae20`](#insn-00c2ae20)
- ブロック [`00c2ae20`](#insn-00c2ae20) 範囲 `[['00c2ae20', '00c2ae2b']]`
  - `CONDITIONAL_JUMP` [`00c2ae28`](#insn-00c2ae28) → [`00c2ae6c`](#insn-00c2ae6c)
  - `FALL_THROUGH` [`00c2ae28`](#insn-00c2ae28) → [`00c2ae2c`](#insn-00c2ae2c)
- ブロック [`00c2ae2c`](#insn-00c2ae2c) 範囲 `[['00c2ae2c', '00c2ae33']]`
  - `FALL_THROUGH` [`00c2ae30`](#insn-00c2ae30) → [`00c2ae34`](#insn-00c2ae34)
- ブロック [`00c2ae34`](#insn-00c2ae34) 範囲 `[['00c2ae34', '00c2ae3b']]`
  - `CONDITIONAL_JUMP` [`00c2ae38`](#insn-00c2ae38) → [`00c2ae6c`](#insn-00c2ae6c)
  - `FALL_THROUGH` [`00c2ae38`](#insn-00c2ae38) → [`00c2ae3c`](#insn-00c2ae3c)
- ブロック [`00c2ae3c`](#insn-00c2ae3c) 範囲 `[['00c2ae3c', '00c2ae4b']]`
  - `CONDITIONAL_JUMP` [`00c2ae48`](#insn-00c2ae48) → [`00c2ae74`](#insn-00c2ae74)
  - `FALL_THROUGH` [`00c2ae48`](#insn-00c2ae48) → [`00c2ae4c`](#insn-00c2ae4c)
- ブロック [`00c2ae4c`](#insn-00c2ae4c) 範囲 `[['00c2ae4c', '00c2ae4f']]`
  - `FALL_THROUGH` [`00c2ae4c`](#insn-00c2ae4c) → [`00c2ae50`](#insn-00c2ae50)
- ブロック [`00c2ae50`](#insn-00c2ae50) 範囲 `[['00c2ae50', '00c2ae5b']]`
  - `CONDITIONAL_JUMP` [`00c2ae58`](#insn-00c2ae58) → [`00c2ae74`](#insn-00c2ae74)
  - `FALL_THROUGH` [`00c2ae58`](#insn-00c2ae58) → [`00c2ae5c`](#insn-00c2ae5c)
- ブロック [`00c2ae5c`](#insn-00c2ae5c) 範囲 `[['00c2ae5c', '00c2ae6b']]`
  - `CONDITIONAL_JUMP` [`00c2ae68`](#insn-00c2ae68) → [`00c2ae34`](#insn-00c2ae34)
  - `FALL_THROUGH` [`00c2ae68`](#insn-00c2ae68) → [`00c2ae6c`](#insn-00c2ae6c)
- ブロック [`00c2ae6c`](#insn-00c2ae6c) 範囲 `[['00c2ae6c', '00c2ae73']]`
  - `FALL_THROUGH` [`00c2ae70`](#insn-00c2ae70) → [`00c2ae74`](#insn-00c2ae74)
- ブロック [`00c2ae74`](#insn-00c2ae74) 範囲 `[['00c2ae74', '00c2ae77']]`
  - `FALL_THROUGH` [`00c2ae74`](#insn-00c2ae74) → [`00c2ae78`](#insn-00c2ae78)
- ブロック [`00c2ae78`](#insn-00c2ae78) 範囲 `[['00c2ae78', '00c2ae7f']]`

## 命令位置別の参照

- [`00c2adf8`](#insn-00c2adf8) → [`00c2ae20`](#insn-00c2ae20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ae00`](#insn-00c2ae00) → [`00c2ae20`](#insn-00c2ae20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ae0c`](#insn-00c2ae0c) → [`00c2ae20`](#insn-00c2ae20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ae28`](#insn-00c2ae28) → [`00c2ae6c`](#insn-00c2ae6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ae38`](#insn-00c2ae38) → [`00c2ae6c`](#insn-00c2ae6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ae48`](#insn-00c2ae48) → [`00c2ae74`](#insn-00c2ae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ae58`](#insn-00c2ae58) → [`00c2ae74`](#insn-00c2ae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ae68`](#insn-00c2ae68) → [`00c2ae34`](#insn-00c2ae34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2adf8`](#insn-00c2adf8)

~~~json
{
  "source": "00c2adf8",
  "target": "00c2ae20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ae00`](#insn-00c2ae00)

~~~json
{
  "source": "00c2ae00",
  "target": "00c2ae20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ae0c`](#insn-00c2ae0c)

~~~json
{
  "source": "00c2ae0c",
  "target": "00c2ae20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ae28`](#insn-00c2ae28)

~~~json
{
  "source": "00c2ae28",
  "target": "00c2ae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ae38`](#insn-00c2ae38)

~~~json
{
  "source": "00c2ae38",
  "target": "00c2ae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ae48`](#insn-00c2ae48)

~~~json
{
  "source": "00c2ae48",
  "target": "00c2ae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ae58`](#insn-00c2ae58)

~~~json
{
  "source": "00c2ae58",
  "target": "00c2ae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ae68`](#insn-00c2ae68)

~~~json
{
  "source": "00c2ae68",
  "target": "00c2ae34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
