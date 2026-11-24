# 005afdec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005afdac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0015.md#compare-8feedc73867189f350c82bc29c9f3956)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `005afe2c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afe2c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0015.md#compare-0ea259739ac147b244095895a3e20915)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005afdec",
  "name": "FUN_005afdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb90ce07b03258c02c1003fd5fb0d3e8f527eda4e069f18f284966c44101f007",
  "source_text_sha256": "bb90ce07b03258c02c1003fd5fb0d3e8f527eda4e069f18f284966c44101f007",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005afdec",
        "005afe07"
      ]
    ],
    "bytes_sha256": "fc4d2d229a5b920378618e6054d8b57409868e2e7fd2ef3430829fc93cef0606",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a47f00](../00a47/00a47f00.md)

## 呼び出し先

- [005afc78](../005af/005afc78.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 190 bytes

~~~c

int FUN_005afdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005afc78(2);
                    /* try { // try from 005afe00 to 006afe0f has its CatchHandler @ 005b02cc */
  return iVar1 + 3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005afdec"></a> `005afdec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-005afdf0"></a> `005afdf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005afdf4"></a> `005afdf4` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-005afdf8"></a> `005afdf8` | `a0 ff ff 97` | bl 0x005afc78 | `UNCONDITIONAL_CALL`
<a id="insn-005afdfc"></a> `005afdfc` | `00 0c 00 11` | add w0,w0,#0x3 | `FALL_THROUGH`
<a id="insn-005afe00"></a> `005afe00` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-005afe04"></a> `005afe04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005afdec`](#insn-005afdec) 範囲 `[['005afdec', '005afdff']]`
  - `FALL_THROUGH` [`005afdfc`](#insn-005afdfc) → [`005afe00`](#insn-005afe00)
- ブロック [`005afe00`](#insn-005afe00) 範囲 `[['005afe00', '005afe07']]`

## 命令位置別の参照

- [`005afdec`](#insn-005afdec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005afdf8`](#insn-005afdf8) → [`005afc78`](005afc78.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005afc78` · 推定シンボル `None` · 推定型 `None`
- [`005afe00`](#insn-005afe00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005afdec`](#insn-005afdec)

~~~json
{
  "source": "005afdec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005afdf8`](#insn-005afdf8)

~~~json
{
  "source": "005afdf8",
  "target": "005afc78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005afe00`](#insn-005afe00)

~~~json
{
  "source": "005afe00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
