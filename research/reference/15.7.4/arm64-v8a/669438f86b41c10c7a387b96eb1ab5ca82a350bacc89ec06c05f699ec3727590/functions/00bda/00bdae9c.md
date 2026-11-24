# 00bdae9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 対応未確定
  - [v15.7.3 → v15.7.4 版の比較一覧](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/README.md)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0093.md#review-9660f8349055a59d9f7c31c688359827)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdae9c",
  "name": "FUN_00bdae9c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d378de2315dae509f9da866b4583f3081a7ffcbf99acd629b8c63db1a06e998d",
  "source_text_sha256": "d378de2315dae509f9da866b4583f3081a7ffcbf99acd629b8c63db1a06e998d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdae9c",
        "00bdaea3"
      ]
    ],
    "bytes_sha256": "134f7e9ee48f50b6db997c9e9cec85f5602b3269313f02dd9192b8964d1aaa19",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b07fc8](../00b07/00b07fc8.md)

## 呼び出し先

- [00b08008](../00b08/00b08008.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_00bdae9c(undefined8 param_1,undefined8 param_2)

{
  long in_x9;
  
  FUN_00b08008(param_1,param_2,*(undefined8 *)(in_x9 + 0xea8));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdae9c"></a> `00bdae9c` | `22 55 47 f9` | ldr x2,[x9, #0xea8] | `FALL_THROUGH`
<a id="insn-00bdaea0"></a> `00bdaea0` | `5a b4 fc 17` | b 0x00b08008 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdae9c`](#insn-00bdae9c) 範囲 `[['00bdae9c', '00bdaea3']]`

## 命令位置別の参照

- [`00bdaea0`](#insn-00bdaea0) → [`00b08008`](../00b08/00b08008.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b08008` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaea0`](#insn-00bdaea0)

~~~json
{
  "source": "00bdaea0",
  "target": "00b08008",
  "target_space": "ram",
  "resolution": "function"
}
~~~
