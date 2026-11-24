# 007ccbbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007ccbbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccbbc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0011.md#compare-42b6a14eb343c427e0a25aea71262e17)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0056.md#review-d677e4616bf1aeb48323f564342838ef)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ccbbc",
  "name": "FUN_007ccbbc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "799e737b3821d954548e2d836c8df8d7401bd0c2384f7b5575ebc4633fbdfe74",
  "source_text_sha256": "799e737b3821d954548e2d836c8df8d7401bd0c2384f7b5575ebc4633fbdfe74",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ccbbc",
        "007ccbd3"
      ]
    ],
    "bytes_sha256": "8af565495190711ad728a15577432de8baa4dbf9cdf6f7cf1d1748a870872b24",
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

- [00885f80](../00885/00885f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 252 bytes

~~~c

void FUN_007ccbbc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  if (*param_3 == 2) {
    FUN_00885f80(*param_2);
    return;
  }
                    /* try { // try from 007ccbd0 to 008ccc0b has its CatchHandler @ 007c86d0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ccbbc"></a> `007ccbbc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007ccbc0"></a> `007ccbc0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007ccbc4"></a> `007ccbc4` | `61 00 00 54` | b.ne 0x007ccbd0 | `CONDITIONAL_JUMP`
<a id="insn-007ccbc8"></a> `007ccbc8` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-007ccbcc"></a> `007ccbcc` | `ed e4 02 14` | b 0x00885f80 | `CALL_TERMINATOR`
<a id="insn-007ccbd0"></a> `007ccbd0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ccbbc`](#insn-007ccbbc) 範囲 `[['007ccbbc', '007ccbc7']]`
  - `CONDITIONAL_JUMP` [`007ccbc4`](#insn-007ccbc4) → [`007ccbd0`](#insn-007ccbd0)
  - `FALL_THROUGH` [`007ccbc4`](#insn-007ccbc4) → [`007ccbc8`](#insn-007ccbc8)
- ブロック [`007ccbc8`](#insn-007ccbc8) 範囲 `[['007ccbc8', '007ccbcf']]`
- ブロック [`007ccbd0`](#insn-007ccbd0) 範囲 `[['007ccbd0', '007ccbd3']]`

## 命令位置別の参照

- [`007ccbc4`](#insn-007ccbc4) → [`007ccbd0`](#insn-007ccbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccbcc`](#insn-007ccbcc) → [`00885f80`](../00885/00885f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00885f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ccbc4`](#insn-007ccbc4)

~~~json
{
  "source": "007ccbc4",
  "target": "007ccbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccbcc`](#insn-007ccbcc)

~~~json
{
  "source": "007ccbcc",
  "target": "00885f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
