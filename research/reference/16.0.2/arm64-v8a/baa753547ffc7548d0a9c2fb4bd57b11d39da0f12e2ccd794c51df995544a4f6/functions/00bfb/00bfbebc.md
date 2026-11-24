# 00bfbebc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbe20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbe20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-d71390970528241181284d15b05e0b88)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfceb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfceb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-88f70b1c421e23eef85a1e157c02de52)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbebc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ccfd6d5436c691b2e9519442ddfd98d0e12000f38f1e017c2eb7a81f341a854",
  "source_text_sha256": "9ccfd6d5436c691b2e9519442ddfd98d0e12000f38f1e017c2eb7a81f341a854",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbebc",
        "00bfbeeb"
      ]
    ],
    "bytes_sha256": "cc050d2778023f8b1da4c0feec16c763dfa99ef97c0cdc70fabafe181290faf2",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
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

## 疑似コード / UTF-8 488 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv(long *param_1)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = param_1[3];
  if (param_1[2] != lVar1) {
    param_1[3] = lVar1 + -1;
    return (ulong)*(byte *)(lVar1 + -1);
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbee8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x58))(param_1,0xffffffff);
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbebc"></a> `00bfbebc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbec0"></a> `00bfbec0` | `09 20 41 a9` | ldp x9,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbec4"></a> `00bfbec4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfbec8"></a> `00bfbec8` | `a0 00 00 54` | b.eq 0x00bfbedc | `CONDITIONAL_JUMP`
<a id="insn-00bfbecc"></a> `00bfbecc` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbed0"></a> `00bfbed0` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbed4"></a> `00bfbed4` | `00 f1 5f 38` | ldurb w0,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00bfbed8"></a> `00bfbed8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbedc"></a> `00bfbedc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfbee0"></a> `00bfbee0` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bfbee4"></a> `00bfbee4` | `10 2d 40 f9` | ldr x16,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bfbee8"></a> `00bfbee8` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfbebc`](#insn-00bfbebc) 範囲 `[['00bfbebc', '00bfbecb']]`
  - `CONDITIONAL_JUMP` [`00bfbec8`](#insn-00bfbec8) → [`00bfbedc`](#insn-00bfbedc)
  - `FALL_THROUGH` [`00bfbec8`](#insn-00bfbec8) → [`00bfbecc`](#insn-00bfbecc)
- ブロック [`00bfbecc`](#insn-00bfbecc) 範囲 `[['00bfbecc', '00bfbedb']]`
- ブロック [`00bfbedc`](#insn-00bfbedc) 範囲 `[['00bfbedc', '00bfbeeb']]`

## 命令位置別の参照

- [`00bfbec8`](#insn-00bfbec8) → [`00bfbedc`](#insn-00bfbedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbec8`](#insn-00bfbec8)

~~~json
{
  "source": "00bfbec8",
  "target": "00bfbedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
