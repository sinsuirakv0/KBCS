# 007fefec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007fefac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-35d2dfc2504ad784719f9ffecb3943cf)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007ff044`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ff/007ff044.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0043.md#compare-c1cac87803692184acae1d704fcb583b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fefec",
  "name": "FUN_007fefec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c1f60cc41966e8ce690e8dff879c3e869f8d88faa36e94497380e3ca3eb320b",
  "source_text_sha256": "7c1f60cc41966e8ce690e8dff879c3e869f8d88faa36e94497380e3ca3eb320b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fefec",
        "007ff02b"
      ]
    ],
    "bytes_sha256": "0d66067b1b10768cc9029cc04e7e1c4221bf90af8f15be1e0e3202d56fc9a31a",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 232 bytes

~~~c

void FUN_007fefec(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[2];
  *param_1 = &PTR_FUN_00c7e030;
  if (__ptr != (void *)0x0) {
    param_1[3] = __ptr;
    _ZdlPv(__ptr);
  }
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fefec"></a> `007fefec` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007feff0"></a> `007feff0` | `09 24 00 90` | adrp x9,0xc7e000 | `FALL_THROUGH`
<a id="insn-007feff4"></a> `007feff4` | `29 c1 00 91` | add x9,x9,#0x30 | `FALL_THROUGH`
<a id="insn-007feff8"></a> `007feff8` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-007feffc"></a> `007feffc` | `68 01 00 b4` | cbz x8,0x007ff028 | `CONDITIONAL_JUMP`
<a id="insn-007ff000"></a> `007ff000` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007ff004"></a> `007ff004` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ff008"></a> `007ff008` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007ff00c"></a> `007ff00c` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-007ff010"></a> `007ff010` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007ff014"></a> `007ff014` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-007ff018"></a> `007ff018` | `a6 63 11 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007ff01c"></a> `007ff01c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ff020"></a> `007ff020` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ff024"></a> `007ff024` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007ff028"></a> `007ff028` | `a2 63 11 14` | b 0x00c57eb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fefec`](#insn-007fefec) 範囲 `[['007fefec', '007fefff']]`
  - `CONDITIONAL_JUMP` [`007feffc`](#insn-007feffc) → [`007ff028`](#insn-007ff028)
  - `FALL_THROUGH` [`007feffc`](#insn-007feffc) → [`007ff000`](#insn-007ff000)
- ブロック [`007ff000`](#insn-007ff000) 範囲 `[['007ff000', '007ff027']]`
  - `FALL_THROUGH` [`007ff024`](#insn-007ff024) → [`007ff028`](#insn-007ff028)
- ブロック [`007ff028`](#insn-007ff028) 範囲 `[['007ff028', '007ff02b']]`

## 命令位置別の参照

- [`007feff8`](#insn-007feff8) → `00c7e030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007feffc`](#insn-007feffc) → [`007ff028`](#insn-007ff028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff000`](#insn-007ff000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff004`](#insn-007ff004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff018`](#insn-007ff018) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007ff020`](#insn-007ff020) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff024`](#insn-007ff024) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff028`](#insn-007ff028) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007feff8`](#insn-007feff8)

~~~json
{
  "source": "007feff8",
  "target": "00c7e030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7e030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007feffc`](#insn-007feffc)

~~~json
{
  "source": "007feffc",
  "target": "007ff028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff000`](#insn-007ff000)

~~~json
{
  "source": "007ff000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff004`](#insn-007ff004)

~~~json
{
  "source": "007ff004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff018`](#insn-007ff018)

~~~json
{
  "source": "007ff018",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ff020`](#insn-007ff020)

~~~json
{
  "source": "007ff020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff024`](#insn-007ff024)

~~~json
{
  "source": "007ff024",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff028`](#insn-007ff028)

~~~json
{
  "source": "007ff028",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
