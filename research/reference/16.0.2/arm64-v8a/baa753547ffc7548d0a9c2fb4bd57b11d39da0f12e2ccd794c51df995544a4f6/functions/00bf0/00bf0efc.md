# 00bf0efc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf0e60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0e60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-40e5195eb95cb345c388eb7e2754b475)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf1ef0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ef0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-b7c607aeae73245a385bef0048bb970e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf0efc",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d7bee42d8c1ef082d4482e3bfe38637abab28ec5812a87431775ab140a7ae030",
  "source_text_sha256": "d7bee42d8c1ef082d4482e3bfe38637abab28ec5812a87431775ab140a7ae030",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf0efc",
        "00bf0f4f"
      ]
    ],
    "bytes_sha256": "2695e5776f0dd76f8e5a6f65c5328d85c6bb89d66fc8bbeddf8977edb6389c39",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58150](../00c58/00c58150.md)

## 呼び出し先

- [00c580b0](../00c58/00c580b0.md)
- [00c58140](../00c58/00c58140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 374 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,char *param_4)

{
  size_t sVar1;
  
  sVar1 = strlen(param_4);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm
            (param_1,param_2,param_3,param_4,sVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf0efc"></a> `00bf0efc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf0f00"></a> `00bf0f00` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bf0f04"></a> `00bf0f04` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0f08"></a> `00bf0f08` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf0f0c"></a> `00bf0f0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf0f10"></a> `00bf0f10` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bf0f14"></a> `00bf0f14` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00bf0f18"></a> `00bf0f18` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bf0f1c"></a> `00bf0f1c` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bf0f20"></a> `00bf0f20` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bf0f24"></a> `00bf0f24` | `63 9c 01 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0f28"></a> `00bf0f28` | `e4 03 00 aa` | mov x4,x0 | `FALL_THROUGH`
<a id="insn-00bf0f2c"></a> `00bf0f2c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bf0f30"></a> `00bf0f30` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bf0f34"></a> `00bf0f34` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bf0f38"></a> `00bf0f38` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bf0f3c"></a> `00bf0f3c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf0f40"></a> `00bf0f40` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0f44"></a> `00bf0f44` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bf0f48"></a> `00bf0f48` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf0f4c"></a> `00bf0f4c` | `7d 9c 01 14` | b 0x00c58140 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf0efc`](#insn-00bf0efc) 範囲 `[['00bf0efc', '00bf0f4f']]`

## 命令位置別の参照

- [`00bf0f00`](#insn-00bf0f00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0f04`](#insn-00bf0f04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0f08`](#insn-00bf0f08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0f24`](#insn-00bf0f24) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bf0f3c`](#insn-00bf0f3c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0f40`](#insn-00bf0f40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0f44`](#insn-00bf0f44) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0f4c`](#insn-00bf0f4c) → [`00c58140`](../00c58/00c58140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58140` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf0f00`](#insn-00bf0f00)

~~~json
{
  "source": "00bf0f00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0f04`](#insn-00bf0f04)

~~~json
{
  "source": "00bf0f04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0f08`](#insn-00bf0f08)

~~~json
{
  "source": "00bf0f08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0f24`](#insn-00bf0f24)

~~~json
{
  "source": "00bf0f24",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0f3c`](#insn-00bf0f3c)

~~~json
{
  "source": "00bf0f3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0f40`](#insn-00bf0f40)

~~~json
{
  "source": "00bf0f40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0f44`](#insn-00bf0f44)

~~~json
{
  "source": "00bf0f44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0f4c`](#insn-00bf0f4c)

~~~json
{
  "source": "00bf0f4c",
  "target": "00c58140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
