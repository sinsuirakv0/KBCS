# 007fceec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `007fce94`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce94.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0042.md#compare-74785836169d6e916cf51bb1e0aa089f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `007fde50`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fd/007fde50.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0042.md#compare-2e3df6c2f4a059f3f3dc1b7ec4df829e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fceec",
  "name": "FUN_007fceec",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb975d18f710d8179b5aa6e2a4aa05c9e8d092608c2e54a2bd1230cba6c0995b",
  "source_text_sha256": "eb975d18f710d8179b5aa6e2a4aa05c9e8d092608c2e54a2bd1230cba6c0995b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fceec",
        "007fcf23"
      ]
    ],
    "bytes_sha256": "6bbea17077be75c76e803d4443c245b5c79d902c05dd532d38e8766ab38d748a",
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

- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_007fceec(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c7d900;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fceec"></a> `007fceec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fcef0"></a> `007fcef0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcef4"></a> `007fcef4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fcef8"></a> `007fcef8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007fcefc"></a> `007fcefc` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-007fcf00"></a> `007fcf00` | `18 6c 11 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-007fcf04"></a> `007fcf04` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007fcf08"></a> `007fcf08` | `08 24 00 b0` | adrp x8,0xc7d000 | `FALL_THROUGH`
<a id="insn-007fcf0c"></a> `007fcf0c` | `08 01 24 91` | add x8,x8,#0x900 | `FALL_THROUGH`
<a id="insn-007fcf10"></a> `007fcf10` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007fcf14"></a> `007fcf14` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007fcf18"></a> `007fcf18` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcf1c"></a> `007fcf1c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fcf20"></a> `007fcf20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fceec`](#insn-007fceec) 範囲 `[['007fceec', '007fcf23']]`

## 命令位置別の参照

- [`007fceec`](#insn-007fceec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcef0`](#insn-007fcef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf00`](#insn-007fcf00) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`007fcf10`](#insn-007fcf10) → `00c7d900`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007fcf18`](#insn-007fcf18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf1c`](#insn-007fcf1c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fceec`](#insn-007fceec)

~~~json
{
  "source": "007fceec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcef0`](#insn-007fcef0)

~~~json
{
  "source": "007fcef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf00`](#insn-007fcf00)

~~~json
{
  "source": "007fcf00",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcf10`](#insn-007fcf10)

~~~json
{
  "source": "007fcf10",
  "target": "00c7d900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7d900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007fcf18`](#insn-007fcf18)

~~~json
{
  "source": "007fcf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf1c`](#insn-007fcf1c)

~~~json
{
  "source": "007fcf1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
