# 00a3cfac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/review-0036.md#review-f022de364b36c3bf45fb87dc41877495)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0079.md#review-f022de364b36c3bf45fb87dc41877495)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3cfac",
  "name": "FUN_00a3cfac",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "679dd1aae1894b9bc9aba650eb00637feef075764b64f04e0ac521fcde42bb6b",
  "source_text_sha256": "679dd1aae1894b9bc9aba650eb00637feef075764b64f04e0ac521fcde42bb6b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3cfac",
        "00a3cfb7"
      ]
    ],
    "bytes_sha256": "e6087f8dc0790b1c1af69a03154fcc65791296d33169e9269c3d1efca334d493",
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

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 121 bytes

~~~c

pointer_____offset_0x10___ * FUN_00a3cfac(void)

{
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c0d5a8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3cfac"></a> `00a3cfac` | `80 0e 00 b0` | adrp x0,0xc0d000 | `FALL_THROUGH`
<a id="insn-00a3cfb0"></a> `00a3cfb0` | `00 a0 16 91` | add x0,x0,#0x5a8 | `FALL_THROUGH`
<a id="insn-00a3cfb4"></a> `00a3cfb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3cfac`](#insn-00a3cfac) 範囲 `[['00a3cfac', '00a3cfb7']]`

## 命令位置別の参照

- [`00a3cfb0`](#insn-00a3cfb0) → `00c0d5a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3cfb0`](#insn-00a3cfb0)

~~~json
{
  "source": "00a3cfb0",
  "target": "00c0d5a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0d5a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
