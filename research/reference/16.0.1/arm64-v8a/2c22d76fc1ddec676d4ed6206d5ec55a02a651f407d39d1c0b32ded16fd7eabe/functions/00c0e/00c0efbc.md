# 00c0efbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c0eb94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eb94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-719228d5b09a0966f4d9f316549e13e0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c0f058`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f058.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0011.md#compare-4d16c10af0df272c261b932a498c3564)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0efbc",
  "name": "_ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcx",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a94af1f015c0e5ae7ec39615cd5d8325f5b9fd12c4344f5980b511183d363cf",
  "source_text_sha256": "8a94af1f015c0e5ae7ec39615cd5d8325f5b9fd12c4344f5980b511183d363cf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c0efbc",
        "00c0efcb"
      ]
    ],
    "bytes_sha256": "6ab1cf2484f4949849a37101f8ceb08752afd124442b51df94a4c41c627a631c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c0efcc](../00c0e/00c0efcc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 162 bytes

~~~c

void _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcx
               (void)

{
  FUN_00c0efcc();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c0efbc"></a> `00c0efbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c0efc0"></a> `00c0efc0` | `e5 b4 ff d0` | adrp x5,0x2ac000 | `FALL_THROUGH`
<a id="insn-00c0efc4"></a> `00c0efc4` | `a5 20 13 91` | add x5,x5,#0x4c8 | `FALL_THROUGH`
<a id="insn-00c0efc8"></a> `00c0efc8` | `01 00 00 14` | b 0x00c0efcc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c0efbc`](#insn-00c0efbc) 範囲 `[['00c0efbc', '00c0efcb']]`

## 命令位置別の参照

- [`00c0efc4`](#insn-00c0efc4) → `002ac4c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0efc8`](#insn-00c0efc8) → [`00c0efcc`](00c0efcc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c0efcc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c0efc4`](#insn-00c0efc4)

~~~json
{
  "source": "00c0efc4",
  "target": "002ac4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0efc8`](#insn-00c0efc8)

~~~json
{
  "source": "00c0efc8",
  "target": "00c0efcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
