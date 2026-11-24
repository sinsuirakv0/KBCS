# 007fccfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007fccbc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fccbc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-2b7d16f4b9f8a370ccb9e2267b2800d9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fcd54`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcd54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0042.md#compare-58b64749a0a3f1bc0a3e1da1fb007e84)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fccfc",
  "name": "FUN_007fccfc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b03e2cade6807fbe4882b29309d8f83b7e90745851ef85ea13bb96f1354c1193",
  "source_text_sha256": "b03e2cade6807fbe4882b29309d8f83b7e90745851ef85ea13bb96f1354c1193",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fccfc",
        "007fcd33"
      ]
    ],
    "bytes_sha256": "b9a1229aaa2c064b2b95d55fa6cf289b76310f30835740a17ba3a704fd6be76a",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
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

## 疑似コード / UTF-8 242 bytes

~~~c

void FUN_007fccfc(long param_1)

{
  undefined4 uVar1;
  undefined8 *puVar2;
  
  puVar2 = (undefined8 *)_Znwm(0x10);
  uVar1 = *(undefined4 *)(param_1 + 8);
  *puVar2 = &PTR_FUN_00c7d730;
  *(undefined4 *)(puVar2 + 1) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fccfc"></a> `007fccfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fcd00"></a> `007fcd00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcd04"></a> `007fcd04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fcd08"></a> `007fcd08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007fcd0c"></a> `007fcd0c` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-007fcd10"></a> `007fcd10` | `60 6c 11 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-007fcd14"></a> `007fcd14` | `69 0a 40 b9` | ldr w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007fcd18"></a> `007fcd18` | `08 24 00 b0` | adrp x8,0xc7d000 | `FALL_THROUGH`
<a id="insn-007fcd1c"></a> `007fcd1c` | `08 c1 1c 91` | add x8,x8,#0x730 | `FALL_THROUGH`
<a id="insn-007fcd20"></a> `007fcd20` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007fcd24"></a> `007fcd24` | `09 08 00 b9` | str w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007fcd28"></a> `007fcd28` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcd2c"></a> `007fcd2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fcd30"></a> `007fcd30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fccfc`](#insn-007fccfc) 範囲 `[['007fccfc', '007fcd33']]`

## 命令位置別の参照

- [`007fccfc`](#insn-007fccfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcd00`](#insn-007fcd00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcd10`](#insn-007fcd10) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`007fcd20`](#insn-007fcd20) → `00c7d730`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007fcd28`](#insn-007fcd28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcd2c`](#insn-007fcd2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fccfc`](#insn-007fccfc)

~~~json
{
  "source": "007fccfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcd00`](#insn-007fcd00)

~~~json
{
  "source": "007fcd00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcd10`](#insn-007fcd10)

~~~json
{
  "source": "007fcd10",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcd20`](#insn-007fcd20)

~~~json
{
  "source": "007fcd20",
  "target": "00c7d730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7d730",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007fcd28`](#insn-007fcd28)

~~~json
{
  "source": "007fcd28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcd2c`](#insn-007fcd2c)

~~~json
{
  "source": "007fcd2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
