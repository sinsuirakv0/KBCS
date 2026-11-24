# 00a3bfcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a3bf88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bf88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0054.md#compare-0ad44ca37b1e559eb4b22f6c53be9caf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0078.md#review-5b64cbe84b7c848c47c7c18026009fab)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3bfcc",
  "name": "FUN_00a3bfcc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a5e55a9cff5cf5dc1bbcc753eb01ac367bc1ef0205dd179b5ca5922c46939fe",
  "source_text_sha256": "8a5e55a9cff5cf5dc1bbcc753eb01ac367bc1ef0205dd179b5ca5922c46939fe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3bfcc",
        "00a3bfdb"
      ]
    ],
    "bytes_sha256": "dcbfbf49c25d5c2d33e33634e5d24cc7ed81c63fd6a069693d3dd496a531b386",
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

void FUN_00a3bfcc(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c0cf48;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3bfcc"></a> `00a3bfcc` | `88 0e 00 b0` | adrp x8,0xc0c000 | `FALL_THROUGH`
<a id="insn-00a3bfd0"></a> `00a3bfd0` | `08 21 3d 91` | add x8,x8,#0xf48 | `FALL_THROUGH`
<a id="insn-00a3bfd4"></a> `00a3bfd4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00a3bfd8"></a> `00a3bfd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3bfcc`](#insn-00a3bfcc) 範囲 `[['00a3bfcc', '00a3bfdb']]`

## 命令位置別の参照

- [`00a3bfd4`](#insn-00a3bfd4) → `00c0cf48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3bfd4`](#insn-00a3bfd4)

~~~json
{
  "source": "00a3bfd4",
  "target": "00c0cf48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0cf48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
