# 00afdbc8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-66f7c319bde961e9feed9df72dbfd0eb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afdff0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdff0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-13106f2c45222ce4189ddeb39285f72a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdbc8",
  "name": "FUN_00afdbc8",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f3cbfaca8e3bdf815fe4efeace16e500eef2685b71b65c3a888bab9b718544d3",
  "source_text_sha256": "f3cbfaca8e3bdf815fe4efeace16e500eef2685b71b65c3a888bab9b718544d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdbc8",
        "00afdc07"
      ]
    ],
    "bytes_sha256": "5cbc5e1eaef6f0481a59f9fbfed3e72c056a6fd6b6bbfd3b84ea6dd71d8c8d54",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00716d50](../00716/00716d50.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afdbc8(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c94);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afdbc8"></a> `00afdbc8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afdbcc"></a> `00afdbcc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdbd0"></a> `00afdbd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afdbd4"></a> `00afdbd4` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afdbd8"></a> `00afdbd8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afdbdc"></a> `00afdbdc` | `37 4e f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afdbe0"></a> `00afdbe0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afdbe4"></a> `00afdbe4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afdbe8"></a> `00afdbe8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afdbec"></a> `00afdbec` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afdbf0"></a> `00afdbf0` | `89 92 89 52` | mov w9,#0x4c94 | `FALL_THROUGH`
<a id="insn-00afdbf4"></a> `00afdbf4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afdbf8"></a> `00afdbf8` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afdbfc"></a> `00afdbfc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdc00"></a> `00afdc00` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afdc04"></a> `00afdc04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdbc8`](#insn-00afdbc8) 範囲 `[['00afdbc8', '00afdc07']]`

## 命令位置別の参照

- [`00afdbc8`](#insn-00afdbc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbcc`](#insn-00afdbcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbdc`](#insn-00afdbdc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afdbfc`](#insn-00afdbfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc00`](#insn-00afdc00) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdbc8`](#insn-00afdbc8)

~~~json
{
  "source": "00afdbc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbcc`](#insn-00afdbcc)

~~~json
{
  "source": "00afdbcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbdc`](#insn-00afdbdc)

~~~json
{
  "source": "00afdbdc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdbfc`](#insn-00afdbfc)

~~~json
{
  "source": "00afdbfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc00`](#insn-00afdc00)

~~~json
{
  "source": "00afdc00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
