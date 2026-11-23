# 00b7eddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b7ed14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ed14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0043.md#compare-e40f8b61b5ae678ecb9ac9dde3c3a2d8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7ee20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ee20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0043.md#compare-ac64875ca3a4bca9836c9fb99b54f44a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7eddc",
  "name": "_ZNKSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6getlocEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b37cebe5881f12c5102417f7da44c9e1ebb868dbc485425e7b1aeca72b186c6",
  "source_text_sha256": "7b37cebe5881f12c5102417f7da44c9e1ebb868dbc485425e7b1aeca72b186c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7eddc",
        "00b7edeb"
      ]
    ],
    "bytes_sha256": "3782ff9ae7b17a88f6b87fc8b8eb715d1f96c4d728700ec285543c33381d4ff4",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd930](../00bdd/00bdd930.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 170 bytes

~~~c

void _ZNKSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6getlocEv(undefined8 param_1,long param_2)

{
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 8);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7eddc"></a> `00b7eddc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00b7ede0"></a> `00b7ede0` | `01 20 00 91` | add x1,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00b7ede4"></a> `00b7ede4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b7ede8"></a> `00b7ede8` | `d2 7a 01 14` | b 0x00bdd930 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7eddc`](#insn-00b7eddc) 範囲 `[['00b7eddc', '00b7edeb']]`

## 命令位置別の参照

- [`00b7ede8`](#insn-00b7ede8) → [`00bdd930`](../00bdd/00bdd930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd930` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7ede8`](#insn-00b7ede8)

~~~json
{
  "source": "00b7ede8",
  "target": "00bdd930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
