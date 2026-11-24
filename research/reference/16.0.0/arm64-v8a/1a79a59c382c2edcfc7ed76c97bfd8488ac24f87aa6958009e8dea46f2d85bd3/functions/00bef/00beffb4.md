# 00beffb4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b733ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733ac.md) · 移動量 `+0x7cc08`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0018.md#compare-efd8a2ec2846b7224ebd3bf3a84408f9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf03dc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf03dc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-54592de73b3bba428c3b66bcac085a30)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beffb4",
  "name": "_ZNSt6__ndk112bad_weak_ptrD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b61dccad7ab163de2d3dc60bbf4bccabaff1d67e9eb0b6bca32fe292b450fe06",
  "source_text_sha256": "b61dccad7ab163de2d3dc60bbf4bccabaff1d67e9eb0b6bca32fe292b450fe06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beffb4",
        "00beffdf"
      ]
    ],
    "bytes_sha256": "31d77deb07d67d34a6805ae368fd81b4ca95fec7f1ac06b61a9bb154095344d2",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5a390](../00c5a/00c5a390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 317 bytes

~~~c

void _ZNSt6__ndk112bad_weak_ptrD0Ev(void *param_1)

{
                    /* try { // try from 00beffb8 to 00ceffdb has its CatchHandler @ 00bf006c */
  _ZNSt6__ndk112bad_weak_ptrD2Ev();
                    /* try { // try from 00beffdc to 00cf016b has its CatchHandler @ 00befce0 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beffb4"></a> `00beffb4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beffb8"></a> `00beffb8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00beffbc"></a> `00beffbc` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beffc0"></a> `00beffc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00beffc4"></a> `00beffc4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00beffc8"></a> `00beffc8` | `f2 a8 01 94` | bl 0x00c5a390 | `UNCONDITIONAL_CALL`
<a id="insn-00beffcc"></a> `00beffcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00beffd0"></a> `00beffd0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beffd4"></a> `00beffd4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00beffd8"></a> `00beffd8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00beffdc"></a> `00beffdc` | `b5 9e 01 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beffb4`](#insn-00beffb4) 範囲 `[['00beffb4', '00beffb7']]`
  - `FALL_THROUGH` [`00beffb4`](#insn-00beffb4) → [`00beffb8`](#insn-00beffb8)
- ブロック [`00beffb8`](#insn-00beffb8) 範囲 `[['00beffb8', '00beffdb']]`
  - `FALL_THROUGH` [`00beffd8`](#insn-00beffd8) → [`00beffdc`](#insn-00beffdc)
- ブロック [`00beffdc`](#insn-00beffdc) 範囲 `[['00beffdc', '00beffdf']]`

## 命令位置別の参照

- [`00beffb8`](#insn-00beffb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffbc`](#insn-00beffbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffc8`](#insn-00beffc8) → [`00c5a390`](../00c5a/00c5a390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a390` · 推定シンボル `None` · 推定型 `None`
- [`00beffd0`](#insn-00beffd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffd4`](#insn-00beffd4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffdc`](#insn-00beffdc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beffb8`](#insn-00beffb8)

~~~json
{
  "source": "00beffb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffbc`](#insn-00beffbc)

~~~json
{
  "source": "00beffbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffc8`](#insn-00beffc8)

~~~json
{
  "source": "00beffc8",
  "target": "00c5a390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beffd0`](#insn-00beffd0)

~~~json
{
  "source": "00beffd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffd4`](#insn-00beffd4)

~~~json
{
  "source": "00beffd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffdc`](#insn-00beffdc)

~~~json
{
  "source": "00beffdc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
