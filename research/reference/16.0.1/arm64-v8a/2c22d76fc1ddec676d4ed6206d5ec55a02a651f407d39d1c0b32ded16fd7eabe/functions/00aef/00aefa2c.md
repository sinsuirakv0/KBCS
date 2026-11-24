# 00aefa2c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aef604`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef604.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-0987f238778de178134b0a17c78805e0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aefac8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefac8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-58be251b59c09e7b7bbcd50ec2d7b7da)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefa2c",
  "name": "FUN_00aefa2c",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f9998fc9462e708f72fbfa05e8b58d1cd546e73f16f17dffecf5d3e17e6a822",
  "source_text_sha256": "9f9998fc9462e708f72fbfa05e8b58d1cd546e73f16f17dffecf5d3e17e6a822",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefa2c",
        "00aefa5b"
      ]
    ],
    "bytes_sha256": "228f85f6d72ca1c2a07d566737f5e6695979e9903a25f6a1f0fe5a08bb45aef9",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b6a5c](../008b6/008b6a5c.md)
- [008b6f10](../008b6/008b6f10.md)
- [008b79c8](../008b7/008b79c8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 387 bytes

~~~c

void FUN_00aefa2c(long param_1)

{
  undefined8 uVar1;
  
  uVar1 = FUN_008b79c8(*(long *)(param_1 + 8) + 0x2f38,0x326);
  uVar1 = FUN_008b6f10(uVar1,1);
                    /* try { // try from 00aefa50 to 00befa57 has its CatchHandler @ 00aefdb0 */
                    /* try { // try from 00aefa58 to 00befac7 has its CatchHandler @ 00aef8e0 */
  FUN_008b6a5c(uVar1,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefa2c"></a> `00aefa2c` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00aefa30"></a> `00aefa30` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aefa34"></a> `00aefa34` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefa38"></a> `00aefa38` | `09 e7 85 52` | mov w9,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aefa3c"></a> `00aefa3c` | `c1 64 80 52` | mov w1,#0x326 | `FALL_THROUGH`
<a id="insn-00aefa40"></a> `00aefa40` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aefa44"></a> `00aefa44` | `e1 1f f7 97` | bl 0x008b79c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aefa48"></a> `00aefa48` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefa4c"></a> `00aefa4c` | `31 1d f7 97` | bl 0x008b6f10 | `UNCONDITIONAL_CALL`
<a id="insn-00aefa50"></a> `00aefa50` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefa54"></a> `00aefa54` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00aefa58"></a> `00aefa58` | `01 1c f7 17` | b 0x008b6a5c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefa2c`](#insn-00aefa2c) 範囲 `[['00aefa2c', '00aefa4f']]`
  - `FALL_THROUGH` [`00aefa4c`](#insn-00aefa4c) → [`00aefa50`](#insn-00aefa50)
- ブロック [`00aefa50`](#insn-00aefa50) 範囲 `[['00aefa50', '00aefa57']]`
  - `FALL_THROUGH` [`00aefa54`](#insn-00aefa54) → [`00aefa58`](#insn-00aefa58)
- ブロック [`00aefa58`](#insn-00aefa58) 範囲 `[['00aefa58', '00aefa5b']]`

## 命令位置別の参照

- [`00aefa2c`](#insn-00aefa2c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefa44`](#insn-00aefa44) → [`008b79c8`](../008b7/008b79c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b79c8` · 推定シンボル `None` · 推定型 `None`
- [`00aefa4c`](#insn-00aefa4c) → [`008b6f10`](../008b6/008b6f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f10` · 推定シンボル `None` · 推定型 `None`
- [`00aefa54`](#insn-00aefa54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefa58`](#insn-00aefa58) → [`008b6a5c`](../008b6/008b6a5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6a5c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefa2c`](#insn-00aefa2c)

~~~json
{
  "source": "00aefa2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefa44`](#insn-00aefa44)

~~~json
{
  "source": "00aefa44",
  "target": "008b79c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefa4c`](#insn-00aefa4c)

~~~json
{
  "source": "00aefa4c",
  "target": "008b6f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefa54`](#insn-00aefa54)

~~~json
{
  "source": "00aefa54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefa58`](#insn-00aefa58)

~~~json
{
  "source": "00aefa58",
  "target": "008b6a5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
