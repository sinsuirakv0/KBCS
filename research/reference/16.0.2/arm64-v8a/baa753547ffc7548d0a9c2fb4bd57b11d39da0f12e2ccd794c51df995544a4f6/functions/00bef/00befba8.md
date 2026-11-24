# 00befba8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befb0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb0c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-67f9ab61d2706e7551f5fd7903552f69)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf0b9c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b9c.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-2c590e6a652c0aed0ee04744fa3868a6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befba8",
  "name": "_ZNSt16nested_exceptionC2Ev",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "762871103ed4cbad8766aba52887d09315247ab583332febff26de4595e0cce4",
  "source_text_sha256": "762871103ed4cbad8766aba52887d09315247ab583332febff26de4595e0cce4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befba8",
        "00befbe3"
      ]
    ],
    "bytes_sha256": "e308ddf36627635916ae1ba3140cf0fda849e6284cf74a01ee089470d1c6f27b",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e010](../00c5e/00c5e010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 216 bytes

~~~c

void _ZNSt16nested_exceptionC2Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVSt16nested_exception_00c9bb40 + 0x10);
  lVar1 = __cxa_current_primary_exception();
  param_1[1] = lVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befba8"></a> `00befba8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befbac"></a> `00befbac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00befbb0"></a> `00befbb0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befbb4"></a> `00befbb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befbb8"></a> `00befbb8` | `68 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00befbbc"></a> `00befbbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00befbc0"></a> `00befbc0` | `08 a1 45 f9` | ldr x8,[x8, #0xb40] | `FALL_THROUGH`
<a id="insn-00befbc4"></a> `00befbc4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00befbc8"></a> `00befbc8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00befbcc"></a> `00befbcc` | `11 b9 01 94` | bl 0x00c5e010 | `UNCONDITIONAL_CALL`
<a id="insn-00befbd0"></a> `00befbd0` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00befbd4"></a> `00befbd4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befbd8"></a> `00befbd8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00befbdc"></a> `00befbdc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befbe0"></a> `00befbe0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befba8`](#insn-00befba8) 範囲 `[['00befba8', '00befbe3']]`

## 命令位置別の参照

- [`00befbac`](#insn-00befbac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbb0`](#insn-00befbb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbc0`](#insn-00befbc0) → `00c9bb40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00befbc8`](#insn-00befbc8) → `00c92aa8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[32]`
- [`00befbcc`](#insn-00befbcc) → [`00c5e010`](../00c5e/00c5e010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e010` · 推定シンボル `None` · 推定型 `None`
- [`00befbd4`](#insn-00befbd4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbd8`](#insn-00befbd8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befbac`](#insn-00befbac)

~~~json
{
  "source": "00befbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbb0`](#insn-00befbb0)

~~~json
{
  "source": "00befbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbc0`](#insn-00befbc0)

~~~json
{
  "source": "00befbc0",
  "target": "00c9bb40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bb40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00befbc8`](#insn-00befbc8)

~~~json
{
  "source": "00befbc8",
  "target": "00c92aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92a98",
  "offset": 16,
  "size": 32,
  "datatype": "undefined1[32]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00befbcc`](#insn-00befbcc)

~~~json
{
  "source": "00befbcc",
  "target": "00c5e010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befbd4`](#insn-00befbd4)

~~~json
{
  "source": "00befbd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbd8`](#insn-00befbd8)

~~~json
{
  "source": "00befbd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
