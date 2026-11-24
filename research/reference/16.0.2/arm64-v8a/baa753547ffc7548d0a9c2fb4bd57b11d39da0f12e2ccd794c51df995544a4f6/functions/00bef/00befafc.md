# 00befafc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befa60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-ce92a923dbf54a3923ef26c7e1f04239)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf0af0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0af0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-cf6cb1f34b0b7acafbbbf9f5ffccbd36)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befafc",
  "name": "_ZSt18uncaught_exceptionv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "408c32ff3f2a9d43bdea5bc67a0634c1f0706226fe222aba20bfa3acd33b0c75",
  "source_text_sha256": "408c32ff3f2a9d43bdea5bc67a0634c1f0706226fe222aba20bfa3acd33b0c75",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befafc",
        "00befb1f"
      ]
    ],
    "bytes_sha256": "d4e5755b12cef27acdcda7775528f99642d29234af6619b439334932b1763bce",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d1c0](../00c5d/00c5d1c0.md)

## 呼び出し先

- [00c5dfd0](../00c5d/00c5dfd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

bool _ZSt18uncaught_exceptionv(void)

{
  int iVar1;
  
  iVar1 = __cxa_uncaught_exceptions();
  return 0 < iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befafc"></a> `00befafc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befb00"></a> `00befb00` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00befb04"></a> `00befb04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befb08"></a> `00befb08` | `32 b9 01 94` | bl 0x00c5dfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00befb0c"></a> `00befb0c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00befb10"></a> `00befb10` | `e0 d7 9f 1a` | cset w0,gt | `FALL_THROUGH`
<a id="insn-00befb14"></a> `00befb14` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00befb18"></a> `00befb18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befb1c"></a> `00befb1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befafc`](#insn-00befafc) 範囲 `[['00befafc', '00befb1f']]`

## 命令位置別の参照

- [`00befb00`](#insn-00befb00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb08`](#insn-00befb08) → [`00c5dfd0`](../00c5d/00c5dfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dfd0` · 推定シンボル `None` · 推定型 `None`
- [`00befb14`](#insn-00befb14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befb00`](#insn-00befb00)

~~~json
{
  "source": "00befb00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb08`](#insn-00befb08)

~~~json
{
  "source": "00befb08",
  "target": "00c5dfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befb14`](#insn-00befb14)

~~~json
{
  "source": "00befb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
