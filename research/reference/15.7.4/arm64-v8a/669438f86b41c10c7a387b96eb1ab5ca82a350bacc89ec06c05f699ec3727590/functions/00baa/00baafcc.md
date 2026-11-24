# 00baafcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baaf88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0016.md#compare-2294eea507136f6f51529ea6f973a4bf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c27a14`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27a14.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0075.md#compare-db4ffbf404c9b5e7b8643122e9f24d95)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baafcc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d2d5f11b739a85d4fa5c635368db1415bd51266aca71637165f8618c855addd",
  "source_text_sha256": "9d2d5f11b739a85d4fa5c635368db1415bd51266aca71637165f8618c855addd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baafcc",
        "00bab027"
      ]
    ],
    "bytes_sha256": "dcec0d8cbaf4e86767b79d47d237f40ad0139f11bd8b7679ce5062694e5d3413",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1ae0](../00be1/00be1ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 638 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw
                   (long param_1,wint_t *param_2,wint_t *param_3)

{
  wint_t *pwVar1;
  wint_t wVar2;
  
  pwVar1 = param_2;
                    /* try { // try from 00baafe8 to 00cab20f has its CatchHandler @ 00baafe8
                       catch() { ... } // from try @ 00baafe8 with catch @ 00baafe8
                       catch() { ... } // from try @ 00bab21c with catch @ 00baafe8 */
  for (; param_2 != param_3; param_2 = param_2 + 1) {
    wVar2 = towupper_l(*param_2,*(__locale_t *)(param_1 + 0x10));
    *param_2 = wVar2;
    pwVar1 = param_3;
  }
  return pwVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baafcc"></a> `00baafcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baafd0"></a> `00baafd0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00baafd4"></a> `00baafd4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baafd8"></a> `00baafd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baafdc"></a> `00baafdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baafe0"></a> `00baafe0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baafe4"></a> `00baafe4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00baafe8"></a> `00baafe8` | `40 01 00 54` | b.eq 0x00bab010 | `CONDITIONAL_JUMP`
<a id="insn-00baafec"></a> `00baafec` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00baaff0"></a> `00baaff0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00baaff4"></a> `00baaff4` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-00baaff8"></a> `00baaff8` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00baaffc"></a> `00baaffc` | `b9 da 00 94` | bl 0x00be1ae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab000"></a> `00bab000` | `60 46 00 b8` | str w0,[x19], #0x4 | `FALL_THROUGH`
<a id="insn-00bab004"></a> `00bab004` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bab008"></a> `00bab008` | `61 ff ff 54` | b.ne 0x00baaff4 | `CONDITIONAL_JUMP`
<a id="insn-00bab00c"></a> `00bab00c` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00bab010"></a> `00bab010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bab014"></a> `00bab014` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab018"></a> `00bab018` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab01c"></a> `00bab01c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bab020"></a> `00bab020` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bab024"></a> `00bab024` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baafcc`](#insn-00baafcc) 範囲 `[['00baafcc', '00baafe7']]`
  - `FALL_THROUGH` [`00baafe4`](#insn-00baafe4) → [`00baafe8`](#insn-00baafe8)
- ブロック [`00baafe8`](#insn-00baafe8) 範囲 `[['00baafe8', '00baafeb']]`
  - `CONDITIONAL_JUMP` [`00baafe8`](#insn-00baafe8) → [`00bab010`](#insn-00bab010)
  - `FALL_THROUGH` [`00baafe8`](#insn-00baafe8) → [`00baafec`](#insn-00baafec)
- ブロック [`00baafec`](#insn-00baafec) 範囲 `[['00baafec', '00baaff3']]`
  - `FALL_THROUGH` [`00baaff0`](#insn-00baaff0) → [`00baaff4`](#insn-00baaff4)
- ブロック [`00baaff4`](#insn-00baaff4) 範囲 `[['00baaff4', '00bab00b']]`
  - `CONDITIONAL_JUMP` [`00bab008`](#insn-00bab008) → [`00baaff4`](#insn-00baaff4)
  - `FALL_THROUGH` [`00bab008`](#insn-00bab008) → [`00bab00c`](#insn-00bab00c)
- ブロック [`00bab00c`](#insn-00bab00c) 範囲 `[['00bab00c', '00bab00f']]`
  - `FALL_THROUGH` [`00bab00c`](#insn-00bab00c) → [`00bab010`](#insn-00bab010)
- ブロック [`00bab010`](#insn-00bab010) 範囲 `[['00bab010', '00bab027']]`

## 命令位置別の参照

- [`00baafd0`](#insn-00baafd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafd4`](#insn-00baafd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafd8`](#insn-00baafd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafe8`](#insn-00baafe8) → [`00bab010`](#insn-00bab010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaffc`](#insn-00baaffc) → [`00be1ae0`](../00be1/00be1ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ae0` · 推定シンボル `None` · 推定型 `None`
- [`00bab008`](#insn-00bab008) → [`00baaff4`](#insn-00baaff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab014`](#insn-00bab014) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab018`](#insn-00bab018) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab01c`](#insn-00bab01c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baafd0`](#insn-00baafd0)

~~~json
{
  "source": "00baafd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafd4`](#insn-00baafd4)

~~~json
{
  "source": "00baafd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafd8`](#insn-00baafd8)

~~~json
{
  "source": "00baafd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafe8`](#insn-00baafe8)

~~~json
{
  "source": "00baafe8",
  "target": "00bab010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaffc`](#insn-00baaffc)

~~~json
{
  "source": "00baaffc",
  "target": "00be1ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab008`](#insn-00bab008)

~~~json
{
  "source": "00bab008",
  "target": "00baaff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab014`](#insn-00bab014)

~~~json
{
  "source": "00bab014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab018`](#insn-00bab018)

~~~json
{
  "source": "00bab018",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab01c`](#insn-00bab01c)

~~~json
{
  "source": "00bab01c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
