# 00b6acec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6ac24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-373a0d71ae47290e750a11d0a6e3aca6)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6ad30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0074.md#compare-660704537c4c3438d83796db01eff3da)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6acec",
  "name": "_ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e74028d8f05ef886ce86e4855f3c4b524b9cdc0e06a3acc4a2ac3e0758f7362",
  "source_text_sha256": "0e74028d8f05ef886ce86e4855f3c4b524b9cdc0e06a3acc4a2ac3e0758f7362",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6acec",
        "00b6ad0b"
      ]
    ],
    "bytes_sha256": "6484806deab40248b65d1ec0b8a4afdda6ad7cffa299d210d1cdfecd5fd2cdb5",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"is_gamecenter_available_on_android"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 172 bytes

~~~c

undefined8 _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv(void)

{
  _ZN8firebase9LogAssertEPKcz("is_gamecenter_available_on_android");
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6acec"></a> `00b6acec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00b6acf0"></a> `00b6acf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b6acf4"></a> `00b6acf4` | `c0 b9 ff b0` | adrp x0,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b6acf8"></a> `00b6acf8` | `00 bc 3f 91` | add x0,x0,#0xfef | `FALL_THROUGH`
<a id="insn-00b6acfc"></a> `00b6acfc` | `0d cd 01 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ad00"></a> `00b6ad00` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b6ad04"></a> `00b6ad04` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00b6ad08"></a> `00b6ad08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6acec`](#insn-00b6acec) 範囲 `[['00b6acec', '00b6ad0b']]`

## 命令位置別の参照

- [`00b6acec`](#insn-00b6acec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6acf8`](#insn-00b6acf8) → `002a3fef`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6acfc`](#insn-00b6acfc) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b6ad04`](#insn-00b6ad04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6acec`](#insn-00b6acec)

~~~json
{
  "source": "00b6acec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6acf8`](#insn-00b6acf8)

~~~json
{
  "source": "00b6acf8",
  "target": "002a3fef",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3fef",
  "offset": 0,
  "size": 35,
  "datatype": "string",
  "bytes": "69735f67616d6563656e7465725f617661696c61626c655f6f6e5f616e64726f",
  "capture_start": "002a3fef",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b6acfc`](#insn-00b6acfc)

~~~json
{
  "source": "00b6acfc",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ad04`](#insn-00b6ad04)

~~~json
{
  "source": "00b6ad04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
