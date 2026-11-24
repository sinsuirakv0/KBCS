# 00bbcd2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4e8dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e8dc.md) · 移動量 `+0x6e450`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0017.md#compare-cd8597fd41889ba3bc7d3d4b022b2bdb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbd154`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd154.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0022.md#compare-06a3f5794942ab486e1620d88b523f86)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcd2c",
  "name": "_ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "763bb6eb5c3bbed0a8f01f732ea91ee4a8412fd6dd8b8462aedc99163dbdab3e",
  "source_text_sha256": "763bb6eb5c3bbed0a8f01f732ea91ee4a8412fd6dd8b8462aedc99163dbdab3e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcd2c",
        "00bbcd2f"
      ]
    ],
    "bytes_sha256": "12dd6c4cd72243817fa082773686b0f82274c92ec2e061c062be1a514db7d691",
    "instruction_count": 1,
    "instruction_bytes": 4,
    "body_bytes": 4,
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

## 疑似コード / UTF-8 185 bytes

~~~c

void _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE(void)

{
  (*(code *)PTR__ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE_00c9e590)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcd2c"></a> `00bbcd2c` | `9d 80 02 14` | b 0x00c5cfa0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbcd2c`](#insn-00bbcd2c) 範囲 `[['00bbcd2c', '00bbcd2f']]`
  - `UNCONDITIONAL_JUMP` [`00bbcd2c`](#insn-00bbcd2c) → [`00c5cfa0`](../00c5c/00c5cfa0.md)

## 命令位置別の参照

- [`00bbcd2c`](#insn-00bbcd2c) → [`00c5cfa0`](../00c5c/00c5cfa0.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00c5cfa0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcd2c`](#insn-00bbcd2c)

~~~json
{
  "source": "00bbcd2c",
  "target": "00c5cfa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
