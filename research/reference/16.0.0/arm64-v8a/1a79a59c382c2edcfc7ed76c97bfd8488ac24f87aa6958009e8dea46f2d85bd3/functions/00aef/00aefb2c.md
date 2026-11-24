# 00aefb2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0163.md#review-976f6437848b3de874c8ccb45113af5f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0043.md#review-976f6437848b3de874c8ccb45113af5f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefb2c",
  "name": "FUN_00aefb2c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "054ab7f1d90526a8a8b431445220863fef3944bad231536b26bfc7110b2ecb16",
  "source_text_sha256": "054ab7f1d90526a8a8b431445220863fef3944bad231536b26bfc7110b2ecb16",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefb2c",
        "00aefb47"
      ]
    ],
    "bytes_sha256": "3b16efc7f811295d8369ff73cc967e3244bf727c08d789c8e4f4b046f2d71358",
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

## 疑似コード / UTF-8 259 bytes

~~~c

long FUN_00aefb2c(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_5clEP9NewButton20NewButtonChangeStateEUlS2_S3_E_"
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
<a id="insn-00aefb2c"></a> `00aefb2c` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aefb30"></a> `00aefb30` | `c9 c0 ff d0` | adrp x9,0x309000 | `FALL_THROUGH`
<a id="insn-00aefb34"></a> `00aefb34` | `29 35 04 91` | add x9,x9,#0x10d | `FALL_THROUGH`
<a id="insn-00aefb38"></a> `00aefb38` | `0a 20 00 91` | add x10,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00aefb3c"></a> `00aefb3c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aefb40"></a> `00aefb40` | `40 01 9f 9a` | csel x0,x10,xzr,eq | `FALL_THROUGH`
<a id="insn-00aefb44"></a> `00aefb44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefb2c`](#insn-00aefb2c) 範囲 `[['00aefb2c', '00aefb47']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

