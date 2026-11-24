# 009abafc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0153.md#review-3922267b08b11a13529e85b1c3ba6194)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0037.md#review-3922267b08b11a13529e85b1c3ba6194)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009abafc",
  "name": "FUN_009abafc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d12a6ad084c10b5618f702b0cb284312a77bc4fd2a5ce59faf58a527863a99a5",
  "source_text_sha256": "d12a6ad084c10b5618f702b0cb284312a77bc4fd2a5ce59faf58a527863a99a5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009abafc",
        "009abb17"
      ]
    ],
    "bytes_sha256": "0411abb22636d0ca7b52ca343b56d8eb86236d330e6be672dea6d4ec635903cd",
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

## 疑似コード / UTF-8 264 bytes

~~~c

long FUN_009abafc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN7Ranking10updateRankERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEE3$_1"
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
<a id="insn-009abafc"></a> `009abafc` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-009abb00"></a> `009abb00` | `a9 ca ff 90` | adrp x9,0x2ff000 | `FALL_THROUGH`
<a id="insn-009abb04"></a> `009abb04` | `29 bd 38 91` | add x9,x9,#0xe2f | `FALL_THROUGH`
<a id="insn-009abb08"></a> `009abb08` | `0a 20 00 91` | add x10,x0,#0x8 | `FALL_THROUGH`
<a id="insn-009abb0c"></a> `009abb0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009abb10"></a> `009abb10` | `40 01 9f 9a` | csel x0,x10,xzr,eq | `FALL_THROUGH`
<a id="insn-009abb14"></a> `009abb14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009abafc`](#insn-009abafc) 範囲 `[['009abafc', '009abb17']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

