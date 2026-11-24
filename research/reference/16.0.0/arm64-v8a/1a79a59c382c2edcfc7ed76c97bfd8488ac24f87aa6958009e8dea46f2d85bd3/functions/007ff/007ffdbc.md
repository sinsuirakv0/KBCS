# 007ffdbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0135.md#review-9d539d4a35ae9f3cc6eeee3dbe205f7d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007ffdfc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffdfc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0012.md#compare-a4ed9e82c9bf52fb3fedb65d2591d120)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ffdbc",
  "name": "FUN_007ffdbc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cf6f922c85739d71783c64bb8d583b46fac61aea83d31f25f6e2ab93d39a777",
  "source_text_sha256": "2cf6f922c85739d71783c64bb8d583b46fac61aea83d31f25f6e2ab93d39a777",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ffdbc",
        "007ffdd3"
      ]
    ],
    "bytes_sha256": "f1e3b9c574f004f85dbf6293a661480f7ee03e39c6658304bb579c0cfed858e1",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b9134](../008b9/008b9134.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_007ffdbc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  if (*param_3 == 2) {
    FUN_008b9134(*param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ffdbc"></a> `007ffdbc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007ffdc0"></a> `007ffdc0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007ffdc4"></a> `007ffdc4` | `61 00 00 54` | b.ne 0x007ffdd0 | `CONDITIONAL_JUMP`
<a id="insn-007ffdc8"></a> `007ffdc8` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-007ffdcc"></a> `007ffdcc` | `da e4 02 14` | b 0x008b9134 | `CALL_TERMINATOR`
<a id="insn-007ffdd0"></a> `007ffdd0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ffdbc`](#insn-007ffdbc) 範囲 `[['007ffdbc', '007ffdc7']]`
  - `CONDITIONAL_JUMP` [`007ffdc4`](#insn-007ffdc4) → [`007ffdd0`](#insn-007ffdd0)
  - `FALL_THROUGH` [`007ffdc4`](#insn-007ffdc4) → [`007ffdc8`](#insn-007ffdc8)
- ブロック [`007ffdc8`](#insn-007ffdc8) 範囲 `[['007ffdc8', '007ffdcf']]`
- ブロック [`007ffdd0`](#insn-007ffdd0) 範囲 `[['007ffdd0', '007ffdd3']]`

## 命令位置別の参照

- [`007ffdc4`](#insn-007ffdc4) → [`007ffdd0`](#insn-007ffdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffdcc`](#insn-007ffdcc) → [`008b9134`](../008b9/008b9134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9134` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ffdc4`](#insn-007ffdc4)

~~~json
{
  "source": "007ffdc4",
  "target": "007ffdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffdcc`](#insn-007ffdcc)

~~~json
{
  "source": "007ffdcc",
  "target": "008b9134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
