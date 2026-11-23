# 008ffafc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `008ffafc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffafc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0017.md#compare-b178dc4d3c499e789b2b39ff52bc7209)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `008ffafc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0017.md#compare-601381634770192cad9536ad4ac8b022)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008ffafc",
  "name": "FUN_008ffafc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c4c99ffa69ec1a06912d6d8671fc00c281dbeff03944646b7e4e6beb1eb91463",
  "source_text_sha256": "c4c99ffa69ec1a06912d6d8671fc00c281dbeff03944646b7e4e6beb1eb91463",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008ffafc",
        "008ffb17"
      ]
    ],
    "bytes_sha256": "4625b0a9eeddaf90b14b6206ca7acaaa1505a560d04828a2a92d48e4ab5d82e4",
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

## 疑似コード / UTF-8 312 bytes

~~~c

long FUN_008ffafc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN16GameOptionWindow4initERKNSt6__ndk110shared_ptrI8aTextureEEENK3$_4clEP9NewButton20NewButtonChangeStateEUlP9NewDialog20NewDialogChangeStateiE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008ffafc"></a> `008ffafc` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-008ffb00"></a> `008ffb00` | `49 cf ff f0` | adrp x9,0x2ea000 | `FALL_THROUGH`
<a id="insn-008ffb04"></a> `008ffb04` | `29 99 2c 91` | add x9,x9,#0xb26 | `FALL_THROUGH`
<a id="insn-008ffb08"></a> `008ffb08` | `0a 20 00 91` | add x10,x0,#0x8 | `FALL_THROUGH`
<a id="insn-008ffb0c"></a> `008ffb0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008ffb10"></a> `008ffb10` | `40 01 9f 9a` | csel x0,x10,xzr,eq | `FALL_THROUGH`
<a id="insn-008ffb14"></a> `008ffb14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008ffafc`](#insn-008ffafc) 範囲 `[['008ffafc', '008ffb17']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

