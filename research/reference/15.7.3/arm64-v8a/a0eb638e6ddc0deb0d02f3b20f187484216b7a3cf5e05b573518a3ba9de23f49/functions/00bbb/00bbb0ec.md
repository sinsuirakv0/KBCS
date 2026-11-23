# 00bbb0ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbb024`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb024.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-247f8f5c79c1895110a19dceb1ef6ad8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbb130`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb130.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-5c1a6ad6df23a884679410515631728b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb0ec",
  "name": "_ZNKSt8bad_cast4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be2f333d2affad689e10c01db60548ab3f2dacabe3d6533f431347803d7f6da0",
  "source_text_sha256": "be2f333d2affad689e10c01db60548ab3f2dacabe3d6533f431347803d7f6da0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb0ec",
        "00bbb0fb"
      ]
    ],
    "bytes_sha256": "8c6f44f7c0003023f68b553510b10ea4e96073db634f4529b785aa69df99a6b4",
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

## 関連文字列（未確認候補）

~~~text
"std::bad_cast"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 69 bytes

~~~c

char * _ZNKSt8bad_cast4whatEv(void)

{
  return "std::bad_cast";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb0ec"></a> `00bbb0ec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbb0f0"></a> `00bbb0f0` | `c0 b6 ff b0` | adrp x0,0x294000 | `FALL_THROUGH`
<a id="insn-00bbb0f4"></a> `00bbb0f4` | `00 14 14 91` | add x0,x0,#0x505 | `FALL_THROUGH`
<a id="insn-00bbb0f8"></a> `00bbb0f8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb0ec`](#insn-00bbb0ec) 範囲 `[['00bbb0ec', '00bbb0fb']]`

## 命令位置別の参照

- [`00bbb0f4`](#insn-00bbb0f4) → `00294505`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb0f4`](#insn-00bbb0f4)

~~~json
{
  "source": "00bbb0f4",
  "target": "00294505",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294505",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "7374643a3a6261645f6361737400",
  "capture_start": "00294505",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
