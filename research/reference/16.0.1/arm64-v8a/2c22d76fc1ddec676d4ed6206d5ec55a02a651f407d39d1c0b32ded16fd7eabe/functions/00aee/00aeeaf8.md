# 00aeeaf8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aee6d0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee6d0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0004.md#compare-6ce5d3985313db0956895c00ecb1bf74)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeeb94`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeb94.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-57e196885d2ae2b9c8743381a49cb4d4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeeaf8",
  "name": "FUN_00aeeaf8",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9947526cece1c92dd2d851ebb176084458bf520ed56d690cd04a1be30c3fd8be",
  "source_text_sha256": "9947526cece1c92dd2d851ebb176084458bf520ed56d690cd04a1be30c3fd8be",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeeaf8",
        "00aeeb1b"
      ]
    ],
    "bytes_sha256": "03f7fa1d7c0e72899abfd6feda02fb5517f37af697bb64ea9d2529227db6c876",
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

void FUN_00aeeaf8(void)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c8ddd8;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeeaf8"></a> `00aeeaf8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00aeeafc"></a> `00aeeafc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aeeb00"></a> `00aeeb00` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00aeeb04"></a> `00aeeb04` | `e3 a4 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb08"></a> `00aeeb08` | `e8 0c 00 f0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeeb0c"></a> `00aeeb0c` | `08 61 37 91` | add x8,x8,#0xdd8 | `FALL_THROUGH`
<a id="insn-00aeeb10"></a> `00aeeb10` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00aeeb14"></a> `00aeeb14` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00aeeb18"></a> `00aeeb18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeeaf8`](#insn-00aeeaf8) 範囲 `[['00aeeaf8', '00aeeb1b']]`

## 命令位置別の参照

- [`00aeeaf8`](#insn-00aeeaf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb04`](#insn-00aeeb04) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb10`](#insn-00aeeb10) → `00c8ddd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeeb14`](#insn-00aeeb14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeeaf8`](#insn-00aeeaf8)

~~~json
{
  "source": "00aeeaf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb04`](#insn-00aeeb04)

~~~json
{
  "source": "00aeeb04",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb10`](#insn-00aeeb10)

~~~json
{
  "source": "00aeeb10",
  "target": "00c8ddd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ddd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeeb14`](#insn-00aeeb14)

~~~json
{
  "source": "00aeeb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
