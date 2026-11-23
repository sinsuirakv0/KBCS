# 00bad3fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bad4c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad4c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-3c3f410548c571cae109352fc6b904ac)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bad3fc",
  "name": "_ZNKSt6__ndk114__codecvt_utf8IDsE10do_unshiftER9mbstate_tPcS4_RS4_",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b5d2aa8bbd16cc2a492a2d15b74278d2892a8882718728eaf89caab2551f2df3",
  "source_text_sha256": "b5d2aa8bbd16cc2a492a2d15b74278d2892a8882718728eaf89caab2551f2df3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bad3fc",
        "00bad40b"
      ]
    ],
    "bytes_sha256": "3f910fcd47da1d8c275765ab9a5b7122f893992e5d87a2ac14556495e9ac3ef1",
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

## 疑似コード / UTF-8 238 bytes

~~~c

undefined8
_ZNKSt6__ndk114__codecvt_utf8IDsE10do_unshiftER9mbstate_tPcS4_RS4_
          (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
          undefined8 *param_5)

{
  *param_5 = param_3;
  return 3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bad3fc"></a> `00bad3fc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bad400"></a> `00bad400` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00bad404"></a> `00bad404` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00bad408"></a> `00bad408` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bad3fc`](#insn-00bad3fc) 範囲 `[['00bad3fc', '00bad40b']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

