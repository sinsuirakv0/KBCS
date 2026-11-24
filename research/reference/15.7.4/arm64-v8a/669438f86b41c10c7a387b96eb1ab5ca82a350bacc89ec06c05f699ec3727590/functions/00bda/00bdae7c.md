# 00bdae7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdae3c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae3c.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0044.md#compare-cf6892722ed23093bfcf396da705e7e3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0093.md#review-fbeb6883ebd0a43641426d6f8835fea7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdae7c",
  "name": "FUN_00bdae7c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc544322f07c36a87b2571b48848c85f0dba70fcd82b93516dac3f27cf135d06",
  "source_text_sha256": "dc544322f07c36a87b2571b48848c85f0dba70fcd82b93516dac3f27cf135d06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdae7c",
        "00bdae83"
      ]
    ],
    "bytes_sha256": "89d94763eb0a9e387f0982dff02e8195d5cae090c35fd7325248cf64b6521317",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008d40c0](../008d4/008d40c0.md)

## 呼び出し先

- [008d5008](../008d5/008d5008.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 133 bytes

~~~c

void FUN_00bdae7c(undefined1 param_1 [16])

{
  long in_x9;
  
  FUN_008d5008(param_1,*(undefined8 *)(in_x9 + 0xe10));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdae7c"></a> `00bdae7c` | `21 85 c3 3d` | ldr q1,[x9, #0xe10] | `FALL_THROUGH`
<a id="insn-00bdae80"></a> `00bdae80` | `62 e8 f3 17` | b 0x008d5008 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdae7c`](#insn-00bdae7c) 範囲 `[['00bdae7c', '00bdae83']]`

## 命令位置別の参照

- [`00bdae80`](#insn-00bdae80) → [`008d5008`](../008d5/008d5008.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008d5008` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdae80`](#insn-00bdae80)

~~~json
{
  "source": "00bdae80",
  "target": "008d5008",
  "target_space": "ram",
  "resolution": "function"
}
~~~
