# 00bfa0cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf90d8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf90d8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-a931de955192f680bfa2cc75231349f9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa0cc",
  "name": "_ZNSt6__ndk112system_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd422ff0037ee70d846014d93427837c9fdce786e1149570a7d38e9ca537c047",
  "source_text_sha256": "bd422ff0037ee70d846014d93427837c9fdce786e1149570a7d38e9ca537c047",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa0cc",
        "00bfa0f7"
      ]
    ],
    "bytes_sha256": "a27bd71a3c4b6d05186c150e76ad1c7bc4296e2ab7d5713a286883a6b6e8dca4",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c5f220](../00c5f/00c5f220.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZNSt6__ndk112system_errorD0Ev(void *param_1)

{
  _ZNSt6__ndk112system_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa0cc"></a> `00bfa0cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa0d0"></a> `00bfa0d0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfa0d4"></a> `00bfa0d4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa0d8"></a> `00bfa0d8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa0dc"></a> `00bfa0dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfa0e0"></a> `00bfa0e0` | `50 94 01 94` | bl 0x00c5f220 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa0e4"></a> `00bfa0e4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfa0e8"></a> `00bfa0e8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa0ec"></a> `00bfa0ec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfa0f0"></a> `00bfa0f0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa0f4"></a> `00bfa0f4` | `97 7b 01 14` | b 0x00c58f50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa0cc`](#insn-00bfa0cc) 範囲 `[['00bfa0cc', '00bfa0f7']]`

## 命令位置別の参照

- [`00bfa0d0`](#insn-00bfa0d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0d4`](#insn-00bfa0d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0e0`](#insn-00bfa0e0) → [`00c5f220`](../00c5f/00c5f220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f220` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0e8`](#insn-00bfa0e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0ec`](#insn-00bfa0ec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0f4`](#insn-00bfa0f4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa0d0`](#insn-00bfa0d0)

~~~json
{
  "source": "00bfa0d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0d4`](#insn-00bfa0d4)

~~~json
{
  "source": "00bfa0d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0e0`](#insn-00bfa0e0)

~~~json
{
  "source": "00bfa0e0",
  "target": "00c5f220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa0e8`](#insn-00bfa0e8)

~~~json
{
  "source": "00bfa0e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0ec`](#insn-00bfa0ec)

~~~json
{
  "source": "00bfa0ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0f4`](#insn-00bfa0f4)

~~~json
{
  "source": "00bfa0f4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
