# 007ffdfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007ffdbc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffdbc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0012.md#compare-a4ed9e82c9bf52fb3fedb65d2591d120)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007ffe54`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ff/007ffe54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0008.md#compare-14fde0837b72ba779e92235f4c99360c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ffdfc",
  "name": "FUN_007ffdfc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c622e1721c13c34615b7e13377d3b9e69f99b5a01e4f8cf01f4cd1298463ba48",
  "source_text_sha256": "c622e1721c13c34615b7e13377d3b9e69f99b5a01e4f8cf01f4cd1298463ba48",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ffdfc",
        "007ffe13"
      ]
    ],
    "bytes_sha256": "cdf81e864a1bfb00fb55d910409e13408375fdc8db1350af90287964da9fdfd0",
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

- [008b9178](../008b9/008b9178.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_007ffdfc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  if (*param_3 == 2) {
    FUN_008b9178(*param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ffdfc"></a> `007ffdfc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007ffe00"></a> `007ffe00` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007ffe04"></a> `007ffe04` | `61 00 00 54` | b.ne 0x007ffe10 | `CONDITIONAL_JUMP`
<a id="insn-007ffe08"></a> `007ffe08` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-007ffe0c"></a> `007ffe0c` | `db e4 02 14` | b 0x008b9178 | `CALL_TERMINATOR`
<a id="insn-007ffe10"></a> `007ffe10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ffdfc`](#insn-007ffdfc) 範囲 `[['007ffdfc', '007ffe07']]`
  - `CONDITIONAL_JUMP` [`007ffe04`](#insn-007ffe04) → [`007ffe10`](#insn-007ffe10)
  - `FALL_THROUGH` [`007ffe04`](#insn-007ffe04) → [`007ffe08`](#insn-007ffe08)
- ブロック [`007ffe08`](#insn-007ffe08) 範囲 `[['007ffe08', '007ffe0f']]`
- ブロック [`007ffe10`](#insn-007ffe10) 範囲 `[['007ffe10', '007ffe13']]`

## 命令位置別の参照

- [`007ffe04`](#insn-007ffe04) → [`007ffe10`](#insn-007ffe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe0c`](#insn-007ffe0c) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ffe04`](#insn-007ffe04)

~~~json
{
  "source": "007ffe04",
  "target": "007ffe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe0c`](#insn-007ffe0c)

~~~json
{
  "source": "007ffe0c",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
