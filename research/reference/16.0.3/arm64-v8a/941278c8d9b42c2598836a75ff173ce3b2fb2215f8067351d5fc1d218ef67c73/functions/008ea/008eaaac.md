# 008eaaac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008e9b00`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b00.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0054.md#compare-4d69fdc66594d40179e5a3d21957cdcd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008eaaac",
  "name": "FUN_008eaaac",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1ed58ea63529aa7722e79c9f50a5a3d2bb0ef7b01725257509eabce84a7dccdf",
  "source_text_sha256": "1ed58ea63529aa7722e79c9f50a5a3d2bb0ef7b01725257509eabce84a7dccdf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008eaaac",
        "008eaae3"
      ]
    ],
    "bytes_sha256": "db54d7ba2a01d665367edb7708ab5e249cfe9e90aa83add9d2804f227a18cfff",
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

- [00c58f30](../00c58/00c58f30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_008eaaac(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c862f0;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008eaaac"></a> `008eaaac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008eaab0"></a> `008eaab0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008eaab4"></a> `008eaab4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008eaab8"></a> `008eaab8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008eaabc"></a> `008eaabc` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-008eaac0"></a> `008eaac0` | `1c b9 0d 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-008eaac4"></a> `008eaac4` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-008eaac8"></a> `008eaac8` | `e8 1c 00 90` | adrp x8,0xc86000 | `FALL_THROUGH`
<a id="insn-008eaacc"></a> `008eaacc` | `08 c1 0b 91` | add x8,x8,#0x2f0 | `FALL_THROUGH`
<a id="insn-008eaad0"></a> `008eaad0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-008eaad4"></a> `008eaad4` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008eaad8"></a> `008eaad8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008eaadc"></a> `008eaadc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008eaae0"></a> `008eaae0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008eaaac`](#insn-008eaaac) 範囲 `[['008eaaac', '008eaae3']]`

## 命令位置別の参照

- [`008eaaac`](#insn-008eaaac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eaab0`](#insn-008eaab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eaac0`](#insn-008eaac0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`008eaad0`](#insn-008eaad0) → `00c862f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008eaad8`](#insn-008eaad8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008eaadc`](#insn-008eaadc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008eaaac`](#insn-008eaaac)

~~~json
{
  "source": "008eaaac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eaab0`](#insn-008eaab0)

~~~json
{
  "source": "008eaab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eaac0`](#insn-008eaac0)

~~~json
{
  "source": "008eaac0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008eaad0`](#insn-008eaad0)

~~~json
{
  "source": "008eaad0",
  "target": "00c862f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c862f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008eaad8`](#insn-008eaad8)

~~~json
{
  "source": "008eaad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008eaadc`](#insn-008eaadc)

~~~json
{
  "source": "008eaadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
