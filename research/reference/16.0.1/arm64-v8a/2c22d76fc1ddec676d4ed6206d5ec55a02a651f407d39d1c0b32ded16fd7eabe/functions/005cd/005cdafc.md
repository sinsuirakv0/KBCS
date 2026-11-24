# 005cdafc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005cdabc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdabc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0024.md#compare-4234c4562d07c7c0e35facd15f9ce3eb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `005cdb3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb3c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0024.md#compare-4ca71246ba95219292d4b1fe553e6877)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cdafc",
  "name": "FUN_005cdafc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e2230905d70f21febf609a8a17d50bc088d4a682ec81c95fdee0ac8ffafbc73",
  "source_text_sha256": "9e2230905d70f21febf609a8a17d50bc088d4a682ec81c95fdee0ac8ffafbc73",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cdafc",
        "005cdb33"
      ]
    ],
    "bytes_sha256": "9858582cbc33c7eaf6fcc7397fd98d762a1adb1fd9457d498c9934b1980d2911",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005cd660](../005cd/005cd660.md)

## 呼び出し先

- [00c57ef0](../00c57/00c57ef0.md)
- [00c57f10](../00c57/00c57f10.md)
- [00c5a7b0](../00c5a/00c5a7b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 357 bytes

~~~c

void FUN_005cdafc(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
  _ZNSt6__ndk111regex_errorC1ENS_15regex_constants10error_typeE(uVar1,0x11);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c9b3b0,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c9b3b8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cdafc"></a> `005cdafc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005cdb00"></a> `005cdb00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cdb04"></a> `005cdb04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005cdb08"></a> `005cdb08` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-005cdb0c"></a> `005cdb0c` | `f9 28 1a 94` | bl 0x00c57ef0 | `UNCONDITIONAL_CALL`
<a id="insn-005cdb10"></a> `005cdb10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005cdb14"></a> `005cdb14` | `21 02 80 52` | mov w1,#0x11 | `FALL_THROUGH`
<a id="insn-005cdb18"></a> `005cdb18` | `26 33 1a 94` | bl 0x00c5a7b0 | `UNCONDITIONAL_CALL`
<a id="insn-005cdb1c"></a> `005cdb1c` | `61 36 00 d0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-005cdb20"></a> `005cdb20` | `62 36 00 d0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-005cdb24"></a> `005cdb24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cdb28"></a> `005cdb28` | `21 d8 41 f9` | ldr x1,[x1, #0x3b0] | `FALL_THROUGH`
<a id="insn-005cdb2c"></a> `005cdb2c` | `42 dc 41 f9` | ldr x2,[x2, #0x3b8] | `FALL_THROUGH`
<a id="insn-005cdb30"></a> `005cdb30` | `f8 28 1a 94` | bl 0x00c57f10 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cdafc`](#insn-005cdafc) 範囲 `[['005cdafc', '005cdb33']]`

## 命令位置別の参照

- [`005cdafc`](#insn-005cdafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdb00`](#insn-005cdb00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdb0c`](#insn-005cdb0c) → [`00c57ef0`](../00c57/00c57ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ef0` · 推定シンボル `None` · 推定型 `None`
- [`005cdb18`](#insn-005cdb18) → [`00c5a7b0`](../00c5a/00c5a7b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7b0` · 推定シンボル `None` · 推定型 `None`
- [`005cdb28`](#insn-005cdb28) → `00c9b3b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdb28`](#insn-005cdb28) → `00c965b8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTINSt6__ndk111regex_errorE` · 推定型 `pointer __((offset(0x10)))`
- [`005cdb2c`](#insn-005cdb2c) → `00c9b3b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdb2c`](#insn-005cdb2c) → [`00c37288`](../00c37/00c37288.md) · `PARAM` · `ANALYSIS` · 関数 `00c37288` · 推定シンボル `_ZNSt6__ndk111regex_errorD1Ev` · 推定型 `None`
- [`005cdb30`](#insn-005cdb30) → [`00c57f10`](../00c57/00c57f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f10` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cdafc`](#insn-005cdafc)

~~~json
{
  "source": "005cdafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdb00`](#insn-005cdb00)

~~~json
{
  "source": "005cdb00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdb0c`](#insn-005cdb0c)

~~~json
{
  "source": "005cdb0c",
  "target": "00c57ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdb18`](#insn-005cdb18)

~~~json
{
  "source": "005cdb18",
  "target": "00c5a7b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdb28`](#insn-005cdb28)

~~~json
{
  "source": "005cdb28",
  "target": "00c9b3b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b3b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdb28`](#insn-005cdb28)

~~~json
{
  "source": "005cdb28",
  "target": "00c965b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c965b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdb2c`](#insn-005cdb2c)

~~~json
{
  "source": "005cdb2c",
  "target": "00c9b3b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b3b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdb2c`](#insn-005cdb2c)

~~~json
{
  "source": "005cdb2c",
  "target": "00c37288",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdb30`](#insn-005cdb30)

~~~json
{
  "source": "005cdb30",
  "target": "00c57f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
