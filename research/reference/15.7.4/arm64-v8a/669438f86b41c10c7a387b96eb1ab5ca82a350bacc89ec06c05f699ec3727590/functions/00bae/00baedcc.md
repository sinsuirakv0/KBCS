# 00baedcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baed88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baed88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-5b115b9c51284306633b021e1976e593)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2b814`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b814.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/detail_skipped-0006.md#compare-3c682a17927a989a5ba7f5e2cfe103cb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baedcc",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "648425ebde57b171d7b0314a27c526308c75a3ab9c39cc4b461d2c78f0bcd6df",
  "source_text_sha256": "648425ebde57b171d7b0314a27c526308c75a3ab9c39cc4b461d2c78f0bcd6df",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baedcc",
        "00baedeb"
      ]
    ],
    "bytes_sha256": "22814a76afbdb542d86f24aa28db928a37a08ba9a078f2af4af1f3ccef7b86fe",
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

- [00bac408](../00bac/00bac408.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 334 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00bac408(param_3,param_4,param_5,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baedcc"></a> `00baedcc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baedd0"></a> `00baedd0` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baedd4"></a> `00baedd4` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baedd8"></a> `00baedd8` | `03 08 40 f9` | ldr x3,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baeddc"></a> `00baeddc` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00baede0"></a> `00baede0` | `e2 03 04 aa` | mov x2,x4 | `FALL_THROUGH`
<a id="insn-00baede4"></a> `00baede4` | `e4 03 08 2a` | mov w4,w8 | `FALL_THROUGH`
<a id="insn-00baede8"></a> `00baede8` | `88 f5 ff 17` | b 0x00bac408 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baedcc`](#insn-00baedcc) 範囲 `[['00baedcc', '00baedeb']]`

## 命令位置別の参照

- [`00baede8`](#insn-00baede8) → [`00bac408`](../00bac/00bac408.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac408` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baede8`](#insn-00baede8)

~~~json
{
  "source": "00baede8",
  "target": "00bac408",
  "target_space": "ram",
  "resolution": "function"
}
~~~
