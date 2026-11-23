# 00aca8fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aca834`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca834.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-524b5219ff74a36b6ee7eda6b1ab1dbe)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aca940`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca940.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-824b0c6a542a342abb748a41bb3a00c6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca8fc",
  "name": "FUN_00aca8fc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "898a89876690258f83a597cfe8012e8c2040f64411f6b0d41e939c07c9ca68e6",
  "source_text_sha256": "898a89876690258f83a597cfe8012e8c2040f64411f6b0d41e939c07c9ca68e6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aca8fc",
        "00aca90b"
      ]
    ],
    "bytes_sha256": "dfbb9acabaae329b62ed2cfb0227dd2a8cf4c57b4a5bd4ba9972f6fa2da679ca",
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

void FUN_00aca8fc(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c0f678;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aca8fc"></a> `00aca8fc` | `28 0a 00 b0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00aca900"></a> `00aca900` | `08 e1 19 91` | add x8,x8,#0x678 | `FALL_THROUGH`
<a id="insn-00aca904"></a> `00aca904` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00aca908"></a> `00aca908` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aca8fc`](#insn-00aca8fc) 範囲 `[['00aca8fc', '00aca90b']]`

## 命令位置別の参照

- [`00aca904`](#insn-00aca904) → `00c0f678`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aca904`](#insn-00aca904)

~~~json
{
  "source": "00aca904",
  "target": "00c0f678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f678",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
