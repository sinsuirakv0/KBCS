# 00aaeea8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaede0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaede0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0026.md#compare-9ddb399c9ea595d42ff190d03f539a2d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aaeeec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaeeec.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0019.md#compare-16bcf9474cb15b1d9ed570ac29efd818)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaeea8",
  "name": "FUN_00aaeea8",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "345371b89feb41e7f2d0589e78be73d9b44fc8e61c558026e2bde8b79c74381e",
  "source_text_sha256": "345371b89feb41e7f2d0589e78be73d9b44fc8e61c558026e2bde8b79c74381e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaeea8",
        "00aaeebf"
      ]
    ],
    "bytes_sha256": "e42942a081b91fbaba26290f9efc7c307d48c72dabdd7bc9dff90c7ec2524b65",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00695904](../00695/00695904.md)
- [0081c6a0](../0081c/0081c6a0.md)
- [009a2998](../009a2/009a2998.md)
- [009bd6b8](../009bd/009bd6b8.md)
- [009eadc8](../009ea/009eadc8.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 243 bytes

~~~c

void FUN_00aaeea8(undefined8 *param_1)

{
  *(undefined1 *)((long)param_1 + 0x2c) = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  *param_1 = 0;
  *(undefined8 *)((long)param_1 + 0x1c) = 0;
  *(undefined4 *)((long)param_1 + 0x24) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaeea8"></a> `00aaeea8` | `1f b0 00 39` | strb wzr,[x0, #0x2c] | `FALL_THROUGH`
<a id="insn-00aaeeac"></a> `00aaeeac` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeeb0"></a> `00aaeeb0` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aaeeb4"></a> `00aaeeb4` | `1f c0 01 f8` | stur xzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaeeb8"></a> `00aaeeb8` | `1f 24 00 b9` | str wzr,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00aaeebc"></a> `00aaeebc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaeea8`](#insn-00aaeea8) 範囲 `[['00aaeea8', '00aaeebf']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

