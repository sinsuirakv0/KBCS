# 008daafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008d9b50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9b50.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0009.md#compare-298a2901ecb0e0acd878299c57903e4e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008daafc",
  "name": "FUN_008daafc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9dfaf0c989cdd542d559a047b3a40a9ca767d987821b79c732d83ca189091189",
  "source_text_sha256": "9dfaf0c989cdd542d559a047b3a40a9ca767d987821b79c732d83ca189091189",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008daafc",
        "008dab13"
      ]
    ],
    "bytes_sha256": "99567c5ffdde2baae607654c9f1600781e13cdf0d32e50a30b6005e5022194b3",
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

- [008ba17c](../008ba/008ba17c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_008daafc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  if (*param_3 == 2) {
    FUN_008ba17c(*param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008daafc"></a> `008daafc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-008dab00"></a> `008dab00` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-008dab04"></a> `008dab04` | `61 00 00 54` | b.ne 0x008dab10 | `CONDITIONAL_JUMP`
<a id="insn-008dab08"></a> `008dab08` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-008dab0c"></a> `008dab0c` | `9c 7d ff 17` | b 0x008ba17c | `CALL_TERMINATOR`
<a id="insn-008dab10"></a> `008dab10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008daafc`](#insn-008daafc) 範囲 `[['008daafc', '008dab07']]`
  - `CONDITIONAL_JUMP` [`008dab04`](#insn-008dab04) → [`008dab10`](#insn-008dab10)
  - `FALL_THROUGH` [`008dab04`](#insn-008dab04) → [`008dab08`](#insn-008dab08)
- ブロック [`008dab08`](#insn-008dab08) 範囲 `[['008dab08', '008dab0f']]`
- ブロック [`008dab10`](#insn-008dab10) 範囲 `[['008dab10', '008dab13']]`

## 命令位置別の参照

- [`008dab04`](#insn-008dab04) → [`008dab10`](#insn-008dab10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dab0c`](#insn-008dab0c) → [`008ba17c`](../008ba/008ba17c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba17c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008dab04`](#insn-008dab04)

~~~json
{
  "source": "008dab04",
  "target": "008dab10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dab0c`](#insn-008dab0c)

~~~json
{
  "source": "008dab0c",
  "target": "008ba17c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
