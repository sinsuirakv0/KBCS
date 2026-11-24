# 00befb9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befb00`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb00.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/machine_only_observed-0022.md#compare-5171a360f7c214ddd0e15aa4b1b6f32a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf0b90`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b90.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0022.md#compare-02015b505945b3155ee6f1275ea7d33c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befb9c",
  "name": "_ZNSt13exception_ptr31__from_native_exception_pointerEPv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab94efff6e48e1cc8254530256a475c6b1ab93394096bc081b569cafc16596a6",
  "source_text_sha256": "ab94efff6e48e1cc8254530256a475c6b1ab93394096bc081b569cafc16596a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befb9c",
        "00befba7"
      ]
    ],
    "bytes_sha256": "407f9c34b5393194953a2b4cba6ccf7157e8c41916c3092afc4be16158ea2159",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58420](../00c58/00c58420.md)

## 呼び出し先

- [00c5dff0](../00c5d/00c5dff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 197 bytes

~~~c

void _ZNSt13exception_ptr31__from_native_exception_pointerEPv
               (undefined8 *param_1,undefined8 param_2)

{
  *param_1 = param_2;
  __cxa_increment_exception_refcount();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befb9c"></a> `00befb9c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00befba0"></a> `00befba0` | `00 01 00 f9` | str x0,[x8] | `FALL_THROUGH`
<a id="insn-00befba4"></a> `00befba4` | `13 b9 01 14` | b 0x00c5dff0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befb9c`](#insn-00befb9c) 範囲 `[['00befb9c', '00befba7']]`

## 命令位置別の参照

- [`00befba4`](#insn-00befba4) → [`00c5dff0`](../00c5d/00c5dff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dff0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befba4`](#insn-00befba4)

~~~json
{
  "source": "00befba4",
  "target": "00c5dff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
