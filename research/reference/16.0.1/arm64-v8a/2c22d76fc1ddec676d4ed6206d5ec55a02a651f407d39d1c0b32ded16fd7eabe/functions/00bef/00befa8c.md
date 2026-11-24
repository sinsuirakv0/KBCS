# 00befa8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef664`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef664.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0022.md#compare-c04ed83f486ab6ebeed6643549958e12)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00befb28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befb28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/machine_only_observed-0022.md#compare-9dae612cad0f89154a1f7f108ce02ad7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befa8c",
  "name": "_ZNSt13exception_ptrD1Ev",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a0b858b86959e82f35387494de7c7962a8fd4ea76780b9a84cc227380241865",
  "source_text_sha256": "3a0b858b86959e82f35387494de7c7962a8fd4ea76780b9a84cc227380241865",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befa8c",
        "00befa97"
      ]
    ],
    "bytes_sha256": "ef6271d9cd16e45cddd9e86a3d9a2835b64df3ae0ce48632b2c0f80f16bed85e",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c582f0](../00c58/00c582f0.md)

## 呼び出し先

- [00c5df10](../00c5d/00c5df10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 116 bytes

~~~c

void _ZNSt13exception_ptrD1Ev(undefined8 *param_1)

{
  __cxa_decrement_exception_refcount(*param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befa8c"></a> `00befa8c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00befa90"></a> `00befa90` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00befa94"></a> `00befa94` | `1f b9 01 14` | b 0x00c5df10 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befa8c`](#insn-00befa8c) 範囲 `[['00befa8c', '00befa97']]`

## 命令位置別の参照

- [`00befa94`](#insn-00befa94) → [`00c5df10`](../00c5d/00c5df10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5df10` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befa94`](#insn-00befa94)

~~~json
{
  "source": "00befa94",
  "target": "00c5df10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
