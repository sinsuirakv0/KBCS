# 005afdac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0107.md#review-3bf4fefacfde7341708a327e98bc0317)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `005afdec`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afdec.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0015.md#compare-8feedc73867189f350c82bc29c9f3956)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005afdac",
  "name": "FUN_005afdac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b626c87be87a169afa6794e450f8b168ca8106dd384550259414c3273e488ed9",
  "source_text_sha256": "b626c87be87a169afa6794e450f8b168ca8106dd384550259414c3273e488ed9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005afdac",
        "005afdc7"
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

- [00a47d08](../00a47/00a47d08.md)

## 呼び出し先

- [005afc38](../005af/005afc38.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 190 bytes

~~~c

int FUN_005afdac(void)

{
  int iVar1;
  
  iVar1 = FUN_005afc38(2);
                    /* try { // try from 005afdc0 to 006afdcf has its CatchHandler @ 005b028c */
  return iVar1 + 3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005afdac"></a> `005afdac` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-005afdb0"></a> `005afdb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005afdb4"></a> `005afdb4` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-005afdb8"></a> `005afdb8` | `a0 ff ff 97` | bl 0x005afc38 | `UNCONDITIONAL_CALL`
<a id="insn-005afdbc"></a> `005afdbc` | `00 0c 00 11` | add w0,w0,#0x3 | `FALL_THROUGH`
<a id="insn-005afdc0"></a> `005afdc0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-005afdc4"></a> `005afdc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005afdac`](#insn-005afdac) 範囲 `[['005afdac', '005afdbf']]`
  - `FALL_THROUGH` [`005afdbc`](#insn-005afdbc) → [`005afdc0`](#insn-005afdc0)
- ブロック [`005afdc0`](#insn-005afdc0) 範囲 `[['005afdc0', '005afdc7']]`

## 命令位置別の参照

- [`005afdac`](#insn-005afdac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005afdb8`](#insn-005afdb8) → [`005afc38`](005afc38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005afc38` · 推定シンボル `None` · 推定型 `None`
- [`005afdc0`](#insn-005afdc0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005afdac`](#insn-005afdac)

~~~json
{
  "source": "005afdac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005afdb8`](#insn-005afdb8)

~~~json
{
  "source": "005afdb8",
  "target": "005afc38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005afdc0`](#insn-005afdc0)

~~~json
{
  "source": "005afdc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
