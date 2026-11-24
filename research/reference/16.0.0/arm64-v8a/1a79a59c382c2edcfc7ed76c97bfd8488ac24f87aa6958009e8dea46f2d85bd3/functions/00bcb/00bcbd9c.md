# 00bcbd9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c89c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c89c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-1a29c80400822fb41b3653c30d315c60)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc1c4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0009.md#compare-cef0778ca28b90d4f17970599e8d40df)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbd9c",
  "name": "_ZN8firebase4auth27CleanupCredentialFutureImplEv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "baf9cfdea0eee5739c8a17e4959f3f5cec3872258f343bfc5f1edd567d1d0d41",
  "source_text_sha256": "baf9cfdea0eee5739c8a17e4959f3f5cec3872258f343bfc5f1edd567d1d0d41",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbd9c",
        "00bcbda7"
      ]
    ],
    "bytes_sha256": "a44371f3d5a8e48809c6e8232f7df4bc2e7af83be038b08b286c0a5658e2d21e",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d620](../00c5d/00c5d620.md)

## 呼び出し先

- [00c5b940](../00c5b/00c5b940.md)

## 関連文字列（未確認候補）

~~~text
"Auth-Credentials"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 260 bytes

~~~c

void _ZN8firebase4auth27CleanupCredentialFutureImplEv(void)

{
                    /* try { // try from 00bcbd9c to 00ccbe1b has its CatchHandler @ 00bcbd30 */
  _ZN8firebase16StaticFutureData26CleanupFutureDataForModuleEPKv("Auth-Credentials");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbd9c"></a> `00bcbd9c` | `20 ba ff 90` | adrp x0,0x30f000 | `FALL_THROUGH`
<a id="insn-00bcbda0"></a> `00bcbda0` | `00 8c 00 91` | add x0,x0,#0x23 | `FALL_THROUGH`
<a id="insn-00bcbda4"></a> `00bcbda4` | `e7 3e 02 14` | b 0x00c5b940 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbd9c`](#insn-00bcbd9c) 範囲 `[['00bcbd9c', '00bcbda7']]`

## 命令位置別の参照

- [`00bcbda0`](#insn-00bcbda0) → `0030f023`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbda4`](#insn-00bcbda4) → [`00c5b940`](../00c5b/00c5b940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b940` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbda0`](#insn-00bcbda0)

~~~json
{
  "source": "00bcbda0",
  "target": "0030f023",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030f023",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "417574682d43726564656e7469616c7300",
  "capture_start": "0030f023",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbda4`](#insn-00bcbda4)

~~~json
{
  "source": "00bcbda4",
  "target": "00c5b940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
