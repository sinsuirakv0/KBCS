# 00be7fbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00be7f20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0013.md#compare-038d799ce7cc5f9e5c5c1bc7d2fe6e09)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00be8fb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0013.md#compare-1bb66207aef8c68d8bae795a1c173b7b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00be7fbc",
  "name": "_ZNSt6__ndk16__sortIRNS_6__lessIddEEPdEEvT0_S5_T_",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4984c030c9297870f51407e635b5c60fefd026a6e5a6b76573cd9a4834bbc70",
  "source_text_sha256": "e4984c030c9297870f51407e635b5c60fefd026a6e5a6b76573cd9a4834bbc70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00be7fbc",
        "00be7fdb"
      ]
    ],
    "bytes_sha256": "94826312a48c9ec8a7c2121a3f46bf227c9db47286c97cc5371c070349930627",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be7fdc](../00be7/00be7fdc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 96 bytes

~~~c

void _ZNSt6__ndk16__sortIRNS_6__lessIddEEPdEEvT0_S5_T_(void)

{
  FUN_00be7fdc();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00be7fbc"></a> `00be7fbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00be7fc0"></a> `00be7fc0` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00be7fc4"></a> `00be7fc4` | `c8 0f 80 52` | mov w8,#0x7e | `FALL_THROUGH`
<a id="insn-00be7fc8"></a> `00be7fc8` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00be7fcc"></a> `00be7fcc` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00be7fd0"></a> `00be7fd0` | `29 11 c0 da` | clz x9,x9 | `FALL_THROUGH`
<a id="insn-00be7fd4"></a> `00be7fd4` | `03 05 09 cb` | sub x3,x8,x9, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00be7fd8"></a> `00be7fd8` | `01 00 00 14` | b 0x00be7fdc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00be7fbc`](#insn-00be7fbc) 範囲 `[['00be7fbc', '00be7fdb']]`

## 命令位置別の参照

- [`00be7fd8`](#insn-00be7fd8) → [`00be7fdc`](00be7fdc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be7fdc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00be7fd8`](#insn-00be7fd8)

~~~json
{
  "source": "00be7fd8",
  "target": "00be7fdc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
