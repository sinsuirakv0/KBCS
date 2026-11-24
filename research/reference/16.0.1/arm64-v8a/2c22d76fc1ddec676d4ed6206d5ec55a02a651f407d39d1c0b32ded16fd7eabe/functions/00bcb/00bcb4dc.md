# 00bcb4dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcb0b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-3fd5c0c8c0c7fb84a13e6aea2f2885c4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcb578`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb578.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0010.md#compare-0172adcd874eea3f49df1b8c92fa7d7a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb4dc",
  "name": "_ZN8firebase4auth15IdTokenListenerD1Ev",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "479ab731a25513e2927709e59d19ae7d772d32c14fb9112be1109f1554be815e",
  "source_text_sha256": "479ab731a25513e2927709e59d19ae7d772d32c14fb9112be1109f1554be815e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb4dc",
        "00bcb53b"
      ]
    ],
    "bytes_sha256": "102f2ebdbfa5fc93bfdb6ac6b5203da8820edfc04e25fda179c9eba877350e34",
    "instruction_count": 24,
    "instruction_bytes": 96,
    "body_bytes": 96,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5da60](../00c5d/00c5da60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 482 bytes

~~~c

void _ZN8firebase4auth15IdTokenListenerD1Ev(long *param_1)

{
  undefined8 *__ptr;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth15IdTokenListenerE_00c9b9b0 + 0x10);
  while( true ) {
    __ptr = (undefined8 *)param_1[1];
    if (__ptr == (undefined8 *)param_1[2]) break;
    _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE(*__ptr,param_1);
  }
  if (__ptr != (undefined8 *)0x0) {
    param_1[2] = (long)__ptr;
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb4dc"></a> `00bcb4dc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcb4e0"></a> `00bcb4e0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb4e4"></a> `00bcb4e4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcb4e8"></a> `00bcb4e8` | `88 06 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcb4ec"></a> `00bcb4ec` | `08 d9 44 f9` | ldr x8,[x8, #0x9b0] | `FALL_THROUGH`
<a id="insn-00bcb4f0"></a> `00bcb4f0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcb4f4"></a> `00bcb4f4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcb4f8"></a> `00bcb4f8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcb4fc"></a> `00bcb4fc` | `88 86 00 f8` | str x8,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00bcb500"></a> `00bcb500` | `60 a2 40 a9` | ldp x0,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb504"></a> `00bcb504` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bcb508"></a> `00bcb508` | `a0 00 00 54` | b.eq 0x00bcb51c | `CONDITIONAL_JUMP`
<a id="insn-00bcb50c"></a> `00bcb50c` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bcb510"></a> `00bcb510` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcb514"></a> `00bcb514` | `53 49 02 94` | bl 0x00c5da60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb518"></a> `00bcb518` | `fa ff ff 17` | b 0x00bcb500 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcb51c"></a> `00bcb51c` | `a0 00 00 b4` | cbz x0,0x00bcb530 | `CONDITIONAL_JUMP`
<a id="insn-00bcb520"></a> `00bcb520` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb524"></a> `00bcb524` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb528"></a> `00bcb528` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcb52c"></a> `00bcb52c` | `61 32 02 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bcb530"></a> `00bcb530` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb534"></a> `00bcb534` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcb538"></a> `00bcb538` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb4dc`](#insn-00bcb4dc) 範囲 `[['00bcb4dc', '00bcb4ff']]`
  - `FALL_THROUGH` [`00bcb4fc`](#insn-00bcb4fc) → [`00bcb500`](#insn-00bcb500)
- ブロック [`00bcb500`](#insn-00bcb500) 範囲 `[['00bcb500', '00bcb50b']]`
  - `CONDITIONAL_JUMP` [`00bcb508`](#insn-00bcb508) → [`00bcb51c`](#insn-00bcb51c)
  - `FALL_THROUGH` [`00bcb508`](#insn-00bcb508) → [`00bcb50c`](#insn-00bcb50c)
- ブロック [`00bcb50c`](#insn-00bcb50c) 範囲 `[['00bcb50c', '00bcb51b']]`
  - `UNCONDITIONAL_JUMP` [`00bcb518`](#insn-00bcb518) → [`00bcb500`](#insn-00bcb500)
- ブロック [`00bcb51c`](#insn-00bcb51c) 範囲 `[['00bcb51c', '00bcb51f']]`
  - `CONDITIONAL_JUMP` [`00bcb51c`](#insn-00bcb51c) → [`00bcb530`](#insn-00bcb530)
  - `FALL_THROUGH` [`00bcb51c`](#insn-00bcb51c) → [`00bcb520`](#insn-00bcb520)
- ブロック [`00bcb520`](#insn-00bcb520) 範囲 `[['00bcb520', '00bcb52f']]`
- ブロック [`00bcb530`](#insn-00bcb530) 範囲 `[['00bcb530', '00bcb53b']]`

## 命令位置別の参照

- [`00bcb4dc`](#insn-00bcb4dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb4e0`](#insn-00bcb4e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb4ec`](#insn-00bcb4ec) → `00c9b9b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcb4fc`](#insn-00bcb4fc) → `00c91900`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bcb508`](#insn-00bcb508) → [`00bcb51c`](#insn-00bcb51c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb514`](#insn-00bcb514) → [`00c5da60`](../00c5d/00c5da60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da60` · 推定シンボル `None` · 推定型 `None`
- [`00bcb518`](#insn-00bcb518) → [`00bcb500`](#insn-00bcb500) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb51c`](#insn-00bcb51c) → [`00bcb530`](#insn-00bcb530) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb524`](#insn-00bcb524) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb52c`](#insn-00bcb52c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb530`](#insn-00bcb530) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb4dc`](#insn-00bcb4dc)

~~~json
{
  "source": "00bcb4dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb4e0`](#insn-00bcb4e0)

~~~json
{
  "source": "00bcb4e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb4ec`](#insn-00bcb4ec)

~~~json
{
  "source": "00bcb4ec",
  "target": "00c9b9b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcb4fc`](#insn-00bcb4fc)

~~~json
{
  "source": "00bcb4fc",
  "target": "00c91900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c918f0",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bcb508`](#insn-00bcb508)

~~~json
{
  "source": "00bcb508",
  "target": "00bcb51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb514`](#insn-00bcb514)

~~~json
{
  "source": "00bcb514",
  "target": "00c5da60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb518`](#insn-00bcb518)

~~~json
{
  "source": "00bcb518",
  "target": "00bcb500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb51c`](#insn-00bcb51c)

~~~json
{
  "source": "00bcb51c",
  "target": "00bcb530",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb524`](#insn-00bcb524)

~~~json
{
  "source": "00bcb524",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb52c`](#insn-00bcb52c)

~~~json
{
  "source": "00bcb52c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb530`](#insn-00bcb530)

~~~json
{
  "source": "00bcb530",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
