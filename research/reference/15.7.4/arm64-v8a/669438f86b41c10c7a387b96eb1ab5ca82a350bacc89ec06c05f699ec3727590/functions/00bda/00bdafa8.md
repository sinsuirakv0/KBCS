# 00bdafa8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdaf58`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf58.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0024.md#compare-9a72fe8089dafdb5c8c5addebb9b7ecf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c579f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c579f0.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0019.md#compare-605a16a083b3c29e1e80d55f901b2071)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafa8",
  "name": "_ZnamSt11align_val_t",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2b00da2d42b48e594a9c1b5ae3e23e29113eb1a9f3fbeece28090b5ee7e52d5",
  "source_text_sha256": "a2b00da2d42b48e594a9c1b5ae3e23e29113eb1a9f3fbeece28090b5ee7e52d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdafa8",
        "00bdafaf"
      ]
    ],
    "bytes_sha256": "fe2d20252832a4e6539c397c46775ec75b8610db8e2d8750c1dd06184d22a433",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1f20](../00be1/00be1f20.md)

## 呼び出し先

- [00be1f00](../00be1/00be1f00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 75 bytes

~~~c

void _ZnamSt11align_val_t(void)

{
  _ZnwmSt11align_val_t();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdafa8"></a> `00bdafa8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bdafac"></a> `00bdafac` | `d5 1b 00 14` | b 0x00be1f00 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdafa8`](#insn-00bdafa8) 範囲 `[['00bdafa8', '00bdafaf']]`

## 命令位置別の参照

- [`00bdafac`](#insn-00bdafac) → [`00be1f00`](../00be1/00be1f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f00` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdafac`](#insn-00bdafac)

~~~json
{
  "source": "00bdafac",
  "target": "00be1f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
