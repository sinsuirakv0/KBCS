# 00bcaca4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc9cb0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9cb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0022.md#compare-7285e142fab2e87aea27ab403facbef8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaca4",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4d61350a42b3e78205cc862a63df01aa8e379dc739f5e37344def63a6701fd5",
  "source_text_sha256": "e4d61350a42b3e78205cc862a63df01aa8e379dc739f5e37344def63a6701fd5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcaca4",
        "00bcacaf"
      ]
    ],
    "bytes_sha256": "b140960fd00131bb194625c88c60bf8caaf7511743fca53deb9d0df44b91f2a0",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 208 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv
               (void *param_1)

{
  if (param_1 != (void *)0x0) {
    _ZdlPv(param_1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcaca4"></a> `00bcaca4` | `40 00 00 b4` | cbz x0,0x00bcacac | `CONDITIONAL_JUMP`
<a id="insn-00bcaca8"></a> `00bcaca8` | `aa 38 02 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00bcacac"></a> `00bcacac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcaca4`](#insn-00bcaca4) 範囲 `[['00bcaca4', '00bcaca7']]`
  - `CONDITIONAL_JUMP` [`00bcaca4`](#insn-00bcaca4) → [`00bcacac`](#insn-00bcacac)
  - `FALL_THROUGH` [`00bcaca4`](#insn-00bcaca4) → [`00bcaca8`](#insn-00bcaca8)
- ブロック [`00bcaca8`](#insn-00bcaca8) 範囲 `[['00bcaca8', '00bcacab']]`
- ブロック [`00bcacac`](#insn-00bcacac) 範囲 `[['00bcacac', '00bcacaf']]`

## 命令位置別の参照

- [`00bcaca4`](#insn-00bcaca4) → [`00bcacac`](#insn-00bcacac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaca8`](#insn-00bcaca8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcaca4`](#insn-00bcaca4)

~~~json
{
  "source": "00bcaca4",
  "target": "00bcacac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaca8`](#insn-00bcaca8)

~~~json
{
  "source": "00bcaca8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
