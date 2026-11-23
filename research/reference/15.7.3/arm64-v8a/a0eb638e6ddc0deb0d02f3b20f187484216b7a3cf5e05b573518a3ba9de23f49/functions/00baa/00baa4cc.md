# 00baa4cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baa404`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa404.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-eeecd47d092fcd402c50673ca718023f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baa510`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa510.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0022.md#compare-3f4422afce8ac7728c2651dd9252a849)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baa4cc",
  "name": "_ZNKSt6__ndk112ctype_bynameIcE10do_toupperEc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a596d79d4ad0d3131aa2d854781da41d82b6241e066f296238dae2d505a5f028",
  "source_text_sha256": "a596d79d4ad0d3131aa2d854781da41d82b6241e066f296238dae2d505a5f028",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baa4cc",
        "00baa4e7"
      ]
    ],
    "bytes_sha256": "e511dfcd0ff3dddf2e5c87c473a474fad8078c0896dec7592e63126cef545176",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
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

## 疑似コード / UTF-8 214 bytes

~~~c

uint _ZNKSt6__ndk112ctype_bynameIcE10do_toupperEc(undefined8 param_1,uint param_2)

{
  uint uVar1;
  
  uVar1 = param_2 ^ 0x20;
  if (0x19 < (param_2 & 0xff) - 0x61) {
    uVar1 = param_2;
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baa4cc"></a> `00baa4cc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baa4d0"></a> `00baa4d0` | `28 1c 00 12` | and w8,w1,#0xff | `FALL_THROUGH`
<a id="insn-00baa4d4"></a> `00baa4d4` | `29 00 1b 52` | eor w9,w1,#0x20 | `FALL_THROUGH`
<a id="insn-00baa4d8"></a> `00baa4d8` | `08 85 01 51` | sub w8,w8,#0x61 | `FALL_THROUGH`
<a id="insn-00baa4dc"></a> `00baa4dc` | `1f 69 00 71` | cmp w8,#0x1a | `FALL_THROUGH`
<a id="insn-00baa4e0"></a> `00baa4e0` | `20 31 81 1a` | csel w0,w9,w1,cc | `FALL_THROUGH`
<a id="insn-00baa4e4"></a> `00baa4e4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baa4cc`](#insn-00baa4cc) 範囲 `[['00baa4cc', '00baa4e7']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

