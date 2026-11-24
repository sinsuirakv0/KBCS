# 00af0eac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0164.md#review-9e2f0b29bcc20013c70f332e67090ff4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af12d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af12d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0021.md#compare-3474a843b3aa5527c5e3a28c4b8f8cae)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af0eac",
  "name": "_ZdlPv",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "581af68db4fb4f3584fa721cd4857b87bee003b569c87f194078b7d61ba03aa0",
  "source_text_sha256": "581af68db4fb4f3584fa721cd4857b87bee003b569c87f194078b7d61ba03aa0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af0eac",
        "00af0eaf"
      ]
    ],
    "bytes_sha256": "dd7ad7a0dc8e735b1ab30a7492f02928a8c0f56ddc431461310367f216ee2cbf",
    "instruction_count": 1,
    "instruction_bytes": 4,
    "body_bytes": 4,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad6d50](../00ad6/00ad6d50.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 243 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
                    /* catch() { ... } // from try @ 00af1004 with catch @ 00af0eac */
  (*(code *)PTR__ZdlPv_00c9bb18)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af0eac"></a> `00af0eac` | `01 9b 05 14` | b 0x00c57ab0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00af0eac`](#insn-00af0eac) 範囲 `[['00af0eac', '00af0eaf']]`
  - `UNCONDITIONAL_JUMP` [`00af0eac`](#insn-00af0eac) → [`00c57ab0`](../00c57/00c57ab0.md)

## 命令位置別の参照

- [`00af0eac`](#insn-00af0eac) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af0eac`](#insn-00af0eac)

~~~json
{
  "source": "00af0eac",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
