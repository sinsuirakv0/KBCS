# 00ad8ffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad90c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0021.md#compare-218acf694d5e53f04add0c8e42a1d8e9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad8ffc",
  "name": "FUN_00ad8ffc",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8a547b3e8d0b5a35523059cf181e00686e452911e4c530dd12428d2f3d5c482",
  "source_text_sha256": "e8a547b3e8d0b5a35523059cf181e00686e452911e4c530dd12428d2f3d5c482",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad8ffc",
        "00ad9003"
      ]
    ],
    "bytes_sha256": "f489d98981356334b3b1be4113d26d8ccdd7844574d6c98a374246ac21c7fa17",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00adb010](../00adb/00adb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 103 bytes

~~~c

void FUN_00ad8ffc(long param_1)

{
  FUN_00adb010(param_1,*(undefined8 *)(param_1 + 8));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad8ffc"></a> `00ad8ffc` | `01 04 40 f9` | ldr x1,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00ad9000"></a> `00ad9000` | `04 08 00 14` | b 0x00adb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad8ffc`](#insn-00ad8ffc) 範囲 `[['00ad8ffc', '00ad9003']]`

## 命令位置別の参照

- [`00ad9000`](#insn-00ad9000) → [`00adb010`](../00adb/00adb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad9000`](#insn-00ad9000)

~~~json
{
  "source": "00ad9000",
  "target": "00adb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
