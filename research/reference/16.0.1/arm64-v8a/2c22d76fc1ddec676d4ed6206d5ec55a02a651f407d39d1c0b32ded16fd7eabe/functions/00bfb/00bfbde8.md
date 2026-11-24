# 00bfbde8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb9c0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb9c0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/reference_unresolved-0001.md#compare-f100b4989ebbd67bb3ec0a32988c1508)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbe84`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbe84.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-177cffdb2bc2ee05c3902a17026dae9c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbde8",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE9sputbackcEc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b5916ec98df9f97dfe66b702a878748a4f7ea8e8a308519450e58bc0235e4656",
  "source_text_sha256": "b5916ec98df9f97dfe66b702a878748a4f7ea8e8a308519450e58bc0235e4656",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbde8",
        "00bfbe1f"
      ]
    ],
    "bytes_sha256": "ff892c6c239a0db06dcc9a6ece496745e2dfea150dd00c73416598374c7e226b",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 535 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE9sputbackcEc(long *param_1,byte param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((param_1[2] != param_1[3]) && (pbVar2 = (byte *)(param_1[3] + -1), *pbVar2 == param_2)) {
    param_1[3] = (long)pbVar2;
    return (ulong)*pbVar2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbe1c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x58))(param_1,param_2);
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbde8"></a> `00bfbde8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbdec"></a> `00bfbdec` | `09 20 41 a9` | ldp x9,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbdf0"></a> `00bfbdf0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfbdf4"></a> `00bfbdf4` | `e0 00 00 54` | b.eq 0x00bfbe10 | `CONDITIONAL_JUMP`
<a id="insn-00bfbdf8"></a> `00bfbdf8` | `09 fd 5f 38` | ldrb w9,[x8, #-0x1]! | `FALL_THROUGH`
<a id="insn-00bfbdfc"></a> `00bfbdfc` | `3f 01 21 6b` | cmp w9,w1, UXTB  | `FALL_THROUGH`
<a id="insn-00bfbe00"></a> `00bfbe00` | `81 00 00 54` | b.ne 0x00bfbe10 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe04"></a> `00bfbe04` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbe08"></a> `00bfbe08` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfbe0c"></a> `00bfbe0c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbe10"></a> `00bfbe10` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfbe14"></a> `00bfbe14` | `21 1c 00 12` | and w1,w1,#0xff | `FALL_THROUGH`
<a id="insn-00bfbe18"></a> `00bfbe18` | `10 2d 40 f9` | ldr x16,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bfbe1c"></a> `00bfbe1c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfbde8`](#insn-00bfbde8) 範囲 `[['00bfbde8', '00bfbdf7']]`
  - `CONDITIONAL_JUMP` [`00bfbdf4`](#insn-00bfbdf4) → [`00bfbe10`](#insn-00bfbe10)
  - `FALL_THROUGH` [`00bfbdf4`](#insn-00bfbdf4) → [`00bfbdf8`](#insn-00bfbdf8)
- ブロック [`00bfbdf8`](#insn-00bfbdf8) 範囲 `[['00bfbdf8', '00bfbe03']]`
  - `CONDITIONAL_JUMP` [`00bfbe00`](#insn-00bfbe00) → [`00bfbe10`](#insn-00bfbe10)
  - `FALL_THROUGH` [`00bfbe00`](#insn-00bfbe00) → [`00bfbe04`](#insn-00bfbe04)
- ブロック [`00bfbe04`](#insn-00bfbe04) 範囲 `[['00bfbe04', '00bfbe0f']]`
- ブロック [`00bfbe10`](#insn-00bfbe10) 範囲 `[['00bfbe10', '00bfbe1f']]`

## 命令位置別の参照

- [`00bfbdf4`](#insn-00bfbdf4) → [`00bfbe10`](#insn-00bfbe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe00`](#insn-00bfbe00) → [`00bfbe10`](#insn-00bfbe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbdf4`](#insn-00bfbdf4)

~~~json
{
  "source": "00bfbdf4",
  "target": "00bfbe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe00`](#insn-00bfbe00)

~~~json
{
  "source": "00bfbe00",
  "target": "00bfbe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
