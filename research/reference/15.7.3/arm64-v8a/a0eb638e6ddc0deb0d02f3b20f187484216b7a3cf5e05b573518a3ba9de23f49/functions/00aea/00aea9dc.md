# 00aea9dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aea914`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea914.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0008.md#compare-f0f21b33cc8d1710fe7a87e8e5c56902)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeaa20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0007.md#compare-327064d98474030c915ed386e1ee2d55)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea9dc",
  "name": "_ZN8firebase4util11float_class8GetClassEv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f2c448b1185876c8ff4529f674790adfdd29207b6e476cc295d2527d54ece831",
  "source_text_sha256": "f2c448b1185876c8ff4529f674790adfdd29207b6e476cc295d2527d54ece831",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea9dc",
        "00aea9e7"
      ]
    ],
    "bytes_sha256": "682285ecbc01aa4e321745d5570f48d5ec4ccc84612316af0e363ab0e1009089",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
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

## 疑似コード / UTF-8 89 bytes

~~~c

undefined8 _ZN8firebase4util11float_class8GetClassEv(void)

{
  return DAT_010a07e8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea9dc"></a> `00aea9dc` | `a8 2d 00 d0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea9e0"></a> `00aea9e0` | `00 f5 43 f9` | ldr x0,[x8, #0x7e8] | `FALL_THROUGH`
<a id="insn-00aea9e4"></a> `00aea9e4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea9dc`](#insn-00aea9dc) 範囲 `[['00aea9dc', '00aea9e7']]`

## 命令位置別の参照

- [`00aea9e0`](#insn-00aea9e0) → `010a07e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea9e0`](#insn-00aea9e0)

~~~json
{
  "source": "00aea9e0",
  "target": "010a07e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
