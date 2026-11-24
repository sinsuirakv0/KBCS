# 005cdeec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `005cdb3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb3c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0024.md#compare-feb6cde9bc3c76ba9722e6f9f1d413d3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cdeec",
  "name": "FUN_005cdeec",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5ebf4077e632ad724185c7f648b3fa8f78c7d7520b2f93c30417cd1e6238341",
  "source_text_sha256": "c5ebf4077e632ad724185c7f648b3fa8f78c7d7520b2f93c30417cd1e6238341",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cdeec",
        "005cdf23"
      ]
    ],
    "bytes_sha256": "348849aec02ab8c3b7c7b52070737f792edb57a73b70e68067ce8d17a90b8209",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005cda50](../005cd/005cda50.md)

## 呼び出し先

- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c5b850](../00c5b/00c5b850.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 551 bytes

~~~c

void FUN_005cdeec(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
                    /* try { // try from 005cdf08 to 006cdf0f has its CatchHandler @ 005cdf3c */
  _ZNSt6__ndk111regex_errorC1ENS_15regex_constants10error_typeE(uVar1,0x11);
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 005cdf20 to 006cdf37 has its CatchHandler @ 005cdf38 */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c9c450,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c9c458);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cdeec"></a> `005cdeec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005cdef0"></a> `005cdef0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cdef4"></a> `005cdef4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005cdef8"></a> `005cdef8` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-005cdefc"></a> `005cdefc` | `25 2c 1a 94` | bl 0x00c58f90 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf00"></a> `005cdf00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005cdf04"></a> `005cdf04` | `21 02 80 52` | mov w1,#0x11 | `FALL_THROUGH`
<a id="insn-005cdf08"></a> `005cdf08` | `52 36 1a 94` | bl 0x00c5b850 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf0c"></a> `005cdf0c` | `61 36 00 f0` | adrp x1,0xc9c000 | `FALL_THROUGH`
<a id="insn-005cdf10"></a> `005cdf10` | `62 36 00 f0` | adrp x2,0xc9c000 | `FALL_THROUGH`
<a id="insn-005cdf14"></a> `005cdf14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cdf18"></a> `005cdf18` | `21 28 42 f9` | ldr x1,[x1, #0x450] | `FALL_THROUGH`
<a id="insn-005cdf1c"></a> `005cdf1c` | `42 2c 42 f9` | ldr x2,[x2, #0x458] | `FALL_THROUGH`
<a id="insn-005cdf20"></a> `005cdf20` | `24 2c 1a 94` | bl 0x00c58fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cdeec`](#insn-005cdeec) 範囲 `[['005cdeec', '005cdf07']]`
  - `FALL_THROUGH` [`005cdf04`](#insn-005cdf04) → [`005cdf08`](#insn-005cdf08)
- ブロック [`005cdf08`](#insn-005cdf08) 範囲 `[['005cdf08', '005cdf1f']]`
  - `FALL_THROUGH` [`005cdf1c`](#insn-005cdf1c) → [`005cdf20`](#insn-005cdf20)
- ブロック [`005cdf20`](#insn-005cdf20) 範囲 `[['005cdf20', '005cdf23']]`

## 命令位置別の参照

- [`005cdeec`](#insn-005cdeec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdef0`](#insn-005cdef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdefc`](#insn-005cdefc) → [`00c58f90`](../00c58/00c58f90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f90` · 推定シンボル `None` · 推定型 `None`
- [`005cdf08`](#insn-005cdf08) → [`00c5b850`](../00c5b/00c5b850.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b850` · 推定シンボル `None` · 推定型 `None`
- [`005cdf18`](#insn-005cdf18) → `00c9c450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdf18`](#insn-005cdf18) → `00c97658`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTINSt6__ndk111regex_errorE` · 推定型 `pointer __((offset(0x10)))`
- [`005cdf1c`](#insn-005cdf1c) → `00c9c458`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdf1c`](#insn-005cdf1c) → [`00c38318`](../00c38/00c38318.md) · `PARAM` · `ANALYSIS` · 関数 `00c38318` · 推定シンボル `_ZNSt6__ndk111regex_errorD1Ev` · 推定型 `None`
- [`005cdf20`](#insn-005cdf20) → [`00c58fb0`](../00c58/00c58fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cdeec`](#insn-005cdeec)

~~~json
{
  "source": "005cdeec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdef0`](#insn-005cdef0)

~~~json
{
  "source": "005cdef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdefc`](#insn-005cdefc)

~~~json
{
  "source": "005cdefc",
  "target": "00c58f90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf08`](#insn-005cdf08)

~~~json
{
  "source": "005cdf08",
  "target": "00c5b850",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf18`](#insn-005cdf18)

~~~json
{
  "source": "005cdf18",
  "target": "00c9c450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c450",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdf18`](#insn-005cdf18)

~~~json
{
  "source": "005cdf18",
  "target": "00c97658",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c97658",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdf1c`](#insn-005cdf1c)

~~~json
{
  "source": "005cdf1c",
  "target": "00c9c458",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c458",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdf1c`](#insn-005cdf1c)

~~~json
{
  "source": "005cdf1c",
  "target": "00c38318",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf20`](#insn-005cdf20)

~~~json
{
  "source": "005cdf20",
  "target": "00c58fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
