# 00a7bdfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a7bc04`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc04.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-3bff48bcb136f50df60666f20ad667bf)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a7be6c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7be6c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0004.md#compare-ec4f1459c243a7d1afd1eafb225d5b41)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7bdfc",
  "name": "FUN_00a7bdfc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04bafd3ed871f6a7c4cc6190ed40ba2cb153bcffea61bbaf11354a0e1d6675d6",
  "source_text_sha256": "04bafd3ed871f6a7c4cc6190ed40ba2cb153bcffea61bbaf11354a0e1d6675d6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7bdfc",
        "00a7be1f"
      ]
    ],
    "bytes_sha256": "1cccb8efb9e0b426b605df2283707a3afce8bbe3d8b9ef054ecb72f3fa34f2ea",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 135 bytes

~~~c

void FUN_00a7bdfc(void)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c8ba70;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7bdfc"></a> `00a7bdfc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00a7be00"></a> `00a7be00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a7be04"></a> `00a7be04` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00a7be08"></a> `00a7be08` | `22 70 07 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00a7be0c"></a> `00a7be0c` | `88 10 00 90` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a7be10"></a> `00a7be10` | `08 c1 29 91` | add x8,x8,#0xa70 | `FALL_THROUGH`
<a id="insn-00a7be14"></a> `00a7be14` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00a7be18"></a> `00a7be18` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00a7be1c"></a> `00a7be1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7bdfc`](#insn-00a7bdfc) 範囲 `[['00a7bdfc', '00a7be1f']]`

## 命令位置別の参照

- [`00a7bdfc`](#insn-00a7bdfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7be08`](#insn-00a7be08) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00a7be14`](#insn-00a7be14) → `00c8ba70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a7be18`](#insn-00a7be18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7bdfc`](#insn-00a7bdfc)

~~~json
{
  "source": "00a7bdfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7be08`](#insn-00a7be08)

~~~json
{
  "source": "00a7be08",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7be14`](#insn-00a7be14)

~~~json
{
  "source": "00a7be14",
  "target": "00c8ba70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ba70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7be18`](#insn-00a7be18)

~~~json
{
  "source": "00a7be18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
