# 00baaec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baaf88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf88.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-26201fa1bb3c4f5702f66aa8b54a0875)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaec0",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6c2cae7208b07b6eb0af53db6d0f78dff85246cf304637afe61772b385f6acb0",
  "source_text_sha256": "6c2cae7208b07b6eb0af53db6d0f78dff85246cf304637afe61772b385f6acb0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaec0",
        "00baaf1b"
      ]
    ],
    "bytes_sha256": "5ca3607ea4e0a9d8c783cb682cd9ca16da0bea19cd02ea01c3a0c5548a88a586",
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

- [00be19e0](../00be1/00be19e0.md)

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
                    /* try { // try from 00baaedc to 00cab103 has its CatchHandler @ 00baaedc
                       catch() { ... } // from try @ 00baaedc with catch @ 00baaedc
                       catch() { ... } // from try @ 00bab110 with catch @ 00baaedc */
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
<a id="insn-00baaec0"></a> `00baaec0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baaec4"></a> `00baaec4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00baaec8"></a> `00baaec8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaecc"></a> `00baaecc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaed0"></a> `00baaed0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baaed4"></a> `00baaed4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baaed8"></a> `00baaed8` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00baaedc"></a> `00baaedc` | `40 01 00 54` | b.eq 0x00baaf04 | `CONDITIONAL_JUMP`
<a id="insn-00baaee0"></a> `00baaee0` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00baaee4"></a> `00baaee4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00baaee8"></a> `00baaee8` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-00baaeec"></a> `00baaeec` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00baaef0"></a> `00baaef0` | `bc da 00 94` | bl 0x00be19e0 | `UNCONDITIONAL_CALL`
<a id="insn-00baaef4"></a> `00baaef4` | `60 46 00 b8` | str w0,[x19], #0x4 | `FALL_THROUGH`
<a id="insn-00baaef8"></a> `00baaef8` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00baaefc"></a> `00baaefc` | `61 ff ff 54` | b.ne 0x00baaee8 | `CONDITIONAL_JUMP`
<a id="insn-00baaf00"></a> `00baaf00` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00baaf04"></a> `00baaf04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baaf08"></a> `00baaf08` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaf0c"></a> `00baaf0c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaf10"></a> `00baaf10` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00baaf14"></a> `00baaf14` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baaf18"></a> `00baaf18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaec0`](#insn-00baaec0) 範囲 `[['00baaec0', '00baaedb']]`
  - `FALL_THROUGH` [`00baaed8`](#insn-00baaed8) → [`00baaedc`](#insn-00baaedc)
- ブロック [`00baaedc`](#insn-00baaedc) 範囲 `[['00baaedc', '00baaedf']]`
  - `CONDITIONAL_JUMP` [`00baaedc`](#insn-00baaedc) → [`00baaf04`](#insn-00baaf04)
  - `FALL_THROUGH` [`00baaedc`](#insn-00baaedc) → [`00baaee0`](#insn-00baaee0)
- ブロック [`00baaee0`](#insn-00baaee0) 範囲 `[['00baaee0', '00baaee7']]`
  - `FALL_THROUGH` [`00baaee4`](#insn-00baaee4) → [`00baaee8`](#insn-00baaee8)
- ブロック [`00baaee8`](#insn-00baaee8) 範囲 `[['00baaee8', '00baaeff']]`
  - `CONDITIONAL_JUMP` [`00baaefc`](#insn-00baaefc) → [`00baaee8`](#insn-00baaee8)
  - `FALL_THROUGH` [`00baaefc`](#insn-00baaefc) → [`00baaf00`](#insn-00baaf00)
- ブロック [`00baaf00`](#insn-00baaf00) 範囲 `[['00baaf00', '00baaf03']]`
  - `FALL_THROUGH` [`00baaf00`](#insn-00baaf00) → [`00baaf04`](#insn-00baaf04)
- ブロック [`00baaf04`](#insn-00baaf04) 範囲 `[['00baaf04', '00baaf1b']]`

## 命令位置別の参照

- [`00baaec4`](#insn-00baaec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaec8`](#insn-00baaec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaecc`](#insn-00baaecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaedc`](#insn-00baaedc) → [`00baaf04`](#insn-00baaf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaef0`](#insn-00baaef0) → [`00be19e0`](../00be1/00be19e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19e0` · 推定シンボル `None` · 推定型 `None`
- [`00baaefc`](#insn-00baaefc) → [`00baaee8`](#insn-00baaee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf08`](#insn-00baaf08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf0c`](#insn-00baaf0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf10`](#insn-00baaf10) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaec4`](#insn-00baaec4)

~~~json
{
  "source": "00baaec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaec8`](#insn-00baaec8)

~~~json
{
  "source": "00baaec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaecc`](#insn-00baaecc)

~~~json
{
  "source": "00baaecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaedc`](#insn-00baaedc)

~~~json
{
  "source": "00baaedc",
  "target": "00baaf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaef0`](#insn-00baaef0)

~~~json
{
  "source": "00baaef0",
  "target": "00be19e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaefc`](#insn-00baaefc)

~~~json
{
  "source": "00baaefc",
  "target": "00baaee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf08`](#insn-00baaf08)

~~~json
{
  "source": "00baaf08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf0c`](#insn-00baaf0c)

~~~json
{
  "source": "00baaf0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf10`](#insn-00baaf10)

~~~json
{
  "source": "00baaf10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
