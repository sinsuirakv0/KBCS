# 00bbaff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb0b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0b8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0044.md#compare-8c2bf5355701f441d1c48f9bf8636cc2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaff0",
  "name": "_ZNSt8bad_castD1Ev",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90aefd0e796e8803278559c7823991a0e3f222bd5807330272b7699e80813997",
  "source_text_sha256": "90aefd0e796e8803278559c7823991a0e3f222bd5807330272b7699e80813997",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaff0",
        "00bbaff7"
      ]
    ],
    "bytes_sha256": "0c167fd35208d2d25ccd4c212137a2f15945e7da1f2e3d9910f37357d3f99457",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1390](../00be1/00be1390.md)

## 呼び出し先

- [00bdb390](../00bdb/00bdb390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 84 bytes

~~~c

void _ZNSt8bad_castD1Ev(void)

{
  _ZNSt20bad_array_new_lengthD1Ev();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaff0"></a> `00bbaff0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbaff4"></a> `00bbaff4` | `e7 80 00 14` | b 0x00bdb390 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaff0`](#insn-00bbaff0) 範囲 `[['00bbaff0', '00bbaff7']]`

## 命令位置別の参照

- [`00bbaff4`](#insn-00bbaff4) → [`00bdb390`](../00bdb/00bdb390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb390` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaff4`](#insn-00bbaff4)

~~~json
{
  "source": "00bbaff4",
  "target": "00bdb390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
