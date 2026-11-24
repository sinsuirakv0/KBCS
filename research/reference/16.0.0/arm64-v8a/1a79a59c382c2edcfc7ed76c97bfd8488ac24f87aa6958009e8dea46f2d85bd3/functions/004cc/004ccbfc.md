# 004ccbfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0100.md#review-d4d35536c65c3bd83d8806c93650381d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0008.md#review-d4d35536c65c3bd83d8806c93650381d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ccbfc",
  "name": "FUN_004ccbfc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8b386ad60c7f7546b5eb0182565aa8c7da7dcb4f1e5358965cb4772a0bae476",
  "source_text_sha256": "b8b386ad60c7f7546b5eb0182565aa8c7da7dcb4f1e5358965cb4772a0bae476",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ccbfc",
        "004ccc0b"
      ]
    ],
    "bytes_sha256": "e93c5e177d1d7b4d08b8d122145a539e70d5621b85decd2e5853133161deaaad",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 263 bytes

~~~c

void FUN_004ccbfc(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x004ccc08. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)**(undefined8 **)(param_1 + 0x10))();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ccbfc"></a> `004ccbfc` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004ccc00"></a> `004ccc00` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004ccc04"></a> `004ccc04` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-004ccc08"></a> `004ccc08` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`004ccbfc`](#insn-004ccbfc) 範囲 `[['004ccbfc', '004ccc0b']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

