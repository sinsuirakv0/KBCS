# 00aaede0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaeea8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeea8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0026.md#compare-9ddb399c9ea595d42ff190d03f539a2d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaede0",
  "name": "FUN_00aaede0",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bbe945ff31a8be7ce2466e0782e490f244b4bb40f4a109d7e77089a45d50e64d",
  "source_text_sha256": "bbe945ff31a8be7ce2466e0782e490f244b4bb40f4a109d7e77089a45d50e64d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaede0",
        "00aaedf7"
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

void FUN_00aaede0(undefined8 *param_1)

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
<a id="insn-00aaede0"></a> `00aaede0` | `1f b0 00 39` | strb wzr,[x0, #0x2c] | `FALL_THROUGH`
<a id="insn-00aaede4"></a> `00aaede4` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aaede8"></a> `00aaede8` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aaedec"></a> `00aaedec` | `1f c0 01 f8` | stur xzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaedf0"></a> `00aaedf0` | `1f 24 00 b9` | str wzr,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00aaedf4"></a> `00aaedf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaede0`](#insn-00aaede0) 範囲 `[['00aaede0', '00aaedf7']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

