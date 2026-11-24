# 00bbb0fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb0b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0043.md#compare-15615b210453d24c8366a7a78321ce42)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37b44`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b44.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0018.md#compare-cb78ff841754fb4b6793415a73d542b4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb0fc",
  "name": "_ZNSt8bad_castD1Ev",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90aefd0e796e8803278559c7823991a0e3f222bd5807330272b7699e80813997",
  "source_text_sha256": "90aefd0e796e8803278559c7823991a0e3f222bd5807330272b7699e80813997",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb0fc",
        "00bbb103"
      ]
    ],
    "bytes_sha256": "e8e2b3b8afa478ade49290345f5bb35c565c0574b16eae5e75c77fe341430a51",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1490](../00be1/00be1490.md)

## 呼び出し先

- [00bdb490](../00bdb/00bdb490.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 84 bytes

~~~c

void _ZNSt8bad_castD1Ev(void)

{
  _ZNSt20bad_array_new_lengthD1Ev();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb0fc"></a> `00bbb0fc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbb100"></a> `00bbb100` | `e4 80 00 14` | b 0x00bdb490 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb0fc`](#insn-00bbb0fc) 範囲 `[['00bbb0fc', '00bbb103']]`

## 命令位置別の参照

- [`00bbb100`](#insn-00bbb100) → [`00bdb490`](../00bdb/00bdb490.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb490` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb100`](#insn-00bbb100)

~~~json
{
  "source": "00bbb100",
  "target": "00bdb490",
  "target_space": "ram",
  "resolution": "function"
}
~~~
