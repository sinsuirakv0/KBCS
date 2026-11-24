# 008fceac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `008fceac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fceac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0048.md#compare-0daaab16f2554aa3b0ade5759c298bff)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0070.md#review-058ee09a1cdc4f6ac5eee028e7222967)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fceac",
  "name": "FUN_008fceac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "223821dec0da68ecd8304468ee48e8eb2d86ffa652c0ec5243af7faf3e9f1dee",
  "source_text_sha256": "223821dec0da68ecd8304468ee48e8eb2d86ffa652c0ec5243af7faf3e9f1dee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008fceac",
        "008fcebb"
      ]
    ],
    "bytes_sha256": "a8b3a06a5ea18e6647e96ba8fef48595732390044deb0f008ae995c74c0bcfaf",
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

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_008fceac(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c08a60;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008fceac"></a> `008fceac` | `68 18 00 90` | adrp x8,0xc08000 | `FALL_THROUGH`
<a id="insn-008fceb0"></a> `008fceb0` | `08 81 29 91` | add x8,x8,#0xa60 | `FALL_THROUGH`
<a id="insn-008fceb4"></a> `008fceb4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008fceb8"></a> `008fceb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008fceac`](#insn-008fceac) 範囲 `[['008fceac', '008fcebb']]`

## 命令位置別の参照

- [`008fceb4`](#insn-008fceb4) → `00c08a60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008fceb4`](#insn-008fceb4)

~~~json
{
  "source": "008fceb4",
  "target": "00c08a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c08a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
