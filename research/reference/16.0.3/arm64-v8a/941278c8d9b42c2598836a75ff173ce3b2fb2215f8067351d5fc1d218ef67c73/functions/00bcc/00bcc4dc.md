# 00bcc4dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcb4e8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb4e8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-90f407e762065ecdf25ffa4ac368a90a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc4dc",
  "name": "_ZN8firebase4auth17AuthStateListenerD1Ev",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37a1a37d3122edbfbac7945a5cb688c03aa46fce1ea67a95304a277bd3ce695e",
  "source_text_sha256": "37a1a37d3122edbfbac7945a5cb688c03aa46fce1ea67a95304a277bd3ce695e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc4dc",
        "00bcc53b"
      ]
    ],
    "bytes_sha256": "5a7d3f4afb4d8bafffcaef79a04b2736d2031463c4288c33806725b63a6a75ca",
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

- [00c58f50](../00c58/00c58f50.md)
- [00c5eb10](../00c5e/00c5eb10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 490 bytes

~~~c

void _ZN8firebase4auth17AuthStateListenerD1Ev(long *param_1)

{
  undefined8 *__ptr;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17AuthStateListenerE_00c9ca58 + 0x10);
  while( true ) {
    __ptr = (undefined8 *)param_1[1];
    if (__ptr == (undefined8 *)param_1[2]) break;
    _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE(*__ptr,param_1);
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
<a id="insn-00bcc4dc"></a> `00bcc4dc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcc4e0"></a> `00bcc4e0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc4e4"></a> `00bcc4e4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcc4e8"></a> `00bcc4e8` | `88 06 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bcc4ec"></a> `00bcc4ec` | `08 2d 45 f9` | ldr x8,[x8, #0xa58] | `FALL_THROUGH`
<a id="insn-00bcc4f0"></a> `00bcc4f0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcc4f4"></a> `00bcc4f4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcc4f8"></a> `00bcc4f8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcc4fc"></a> `00bcc4fc` | `88 86 00 f8` | str x8,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00bcc500"></a> `00bcc500` | `60 a2 40 a9` | ldp x0,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcc504"></a> `00bcc504` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bcc508"></a> `00bcc508` | `a0 00 00 54` | b.eq 0x00bcc51c | `CONDITIONAL_JUMP`
<a id="insn-00bcc50c"></a> `00bcc50c` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bcc510"></a> `00bcc510` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcc514"></a> `00bcc514` | `7f 49 02 94` | bl 0x00c5eb10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc518"></a> `00bcc518` | `fa ff ff 17` | b 0x00bcc500 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcc51c"></a> `00bcc51c` | `a0 00 00 b4` | cbz x0,0x00bcc530 | `CONDITIONAL_JUMP`
<a id="insn-00bcc520"></a> `00bcc520` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc524"></a> `00bcc524` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc528"></a> `00bcc528` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcc52c"></a> `00bcc52c` | `89 32 02 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00bcc530"></a> `00bcc530` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc534"></a> `00bcc534` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcc538"></a> `00bcc538` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc4dc`](#insn-00bcc4dc) 範囲 `[['00bcc4dc', '00bcc4ff']]`
  - `FALL_THROUGH` [`00bcc4fc`](#insn-00bcc4fc) → [`00bcc500`](#insn-00bcc500)
- ブロック [`00bcc500`](#insn-00bcc500) 範囲 `[['00bcc500', '00bcc50b']]`
  - `CONDITIONAL_JUMP` [`00bcc508`](#insn-00bcc508) → [`00bcc51c`](#insn-00bcc51c)
  - `FALL_THROUGH` [`00bcc508`](#insn-00bcc508) → [`00bcc50c`](#insn-00bcc50c)
- ブロック [`00bcc50c`](#insn-00bcc50c) 範囲 `[['00bcc50c', '00bcc51b']]`
  - `UNCONDITIONAL_JUMP` [`00bcc518`](#insn-00bcc518) → [`00bcc500`](#insn-00bcc500)
- ブロック [`00bcc51c`](#insn-00bcc51c) 範囲 `[['00bcc51c', '00bcc51f']]`
  - `CONDITIONAL_JUMP` [`00bcc51c`](#insn-00bcc51c) → [`00bcc530`](#insn-00bcc530)
  - `FALL_THROUGH` [`00bcc51c`](#insn-00bcc51c) → [`00bcc520`](#insn-00bcc520)
- ブロック [`00bcc520`](#insn-00bcc520) 範囲 `[['00bcc520', '00bcc52f']]`
- ブロック [`00bcc530`](#insn-00bcc530) 範囲 `[['00bcc530', '00bcc53b']]`

## 命令位置別の参照

- [`00bcc4dc`](#insn-00bcc4dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc4e0`](#insn-00bcc4e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc4ec`](#insn-00bcc4ec) → `00c9ca58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcc4fc`](#insn-00bcc4fc) → `00c92978`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bcc508`](#insn-00bcc508) → [`00bcc51c`](#insn-00bcc51c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc514`](#insn-00bcc514) → [`00c5eb10`](../00c5e/00c5eb10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eb10` · 推定シンボル `None` · 推定型 `None`
- [`00bcc518`](#insn-00bcc518) → [`00bcc500`](#insn-00bcc500) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc51c`](#insn-00bcc51c) → [`00bcc530`](#insn-00bcc530) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc524`](#insn-00bcc524) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc52c`](#insn-00bcc52c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bcc530`](#insn-00bcc530) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc4dc`](#insn-00bcc4dc)

~~~json
{
  "source": "00bcc4dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc4e0`](#insn-00bcc4e0)

~~~json
{
  "source": "00bcc4e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc4ec`](#insn-00bcc4ec)

~~~json
{
  "source": "00bcc4ec",
  "target": "00c9ca58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcc4fc`](#insn-00bcc4fc)

~~~json
{
  "source": "00bcc4fc",
  "target": "00c92978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92968",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bcc508`](#insn-00bcc508)

~~~json
{
  "source": "00bcc508",
  "target": "00bcc51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc514`](#insn-00bcc514)

~~~json
{
  "source": "00bcc514",
  "target": "00c5eb10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc518`](#insn-00bcc518)

~~~json
{
  "source": "00bcc518",
  "target": "00bcc500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc51c`](#insn-00bcc51c)

~~~json
{
  "source": "00bcc51c",
  "target": "00bcc530",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc524`](#insn-00bcc524)

~~~json
{
  "source": "00bcc524",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc52c`](#insn-00bcc52c)

~~~json
{
  "source": "00bcc52c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc530`](#insn-00bcc530)

~~~json
{
  "source": "00bcc530",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
