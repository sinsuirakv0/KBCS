# 00bffb0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffa70`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa70.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-75ae7d52c521e2d3f95164e6d1c51820)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00b00`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00b00.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0039.md#compare-243c2492d9eeda408d696eea544254b0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffb0c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac317ab8a7097e5a3b4341ec91f1407d827f9b02f055aa340a7083fe49651ae9",
  "source_text_sha256": "ac317ab8a7097e5a3b4341ec91f1407d827f9b02f055aa340a7083fe49651ae9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffb0c",
        "00bffb37"
      ]
    ],
    "bytes_sha256": "e29d7174f31759f76dd18f625cd113d2fefe5d019db83c1ca693c8c91a38ea14",
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

- [00c57f80](../00c57/00c57f80.md)
- [00c5e4a0](../00c5e/00c5e4a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 175 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev(void *param_1)

{
  _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffb0c"></a> `00bffb0c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffb10"></a> `00bffb10` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bffb14"></a> `00bffb14` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffb18"></a> `00bffb18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bffb1c"></a> `00bffb1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bffb20"></a> `00bffb20` | `60 7a 01 94` | bl 0x00c5e4a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffb24"></a> `00bffb24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffb28"></a> `00bffb28` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffb2c"></a> `00bffb2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bffb30"></a> `00bffb30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffb34"></a> `00bffb34` | `13 61 01 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffb0c`](#insn-00bffb0c) 範囲 `[['00bffb0c', '00bffb37']]`

## 命令位置別の参照

- [`00bffb10`](#insn-00bffb10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffb14`](#insn-00bffb14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffb20`](#insn-00bffb20) → [`00c5e4a0`](../00c5e/00c5e4a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e4a0` · 推定シンボル `None` · 推定型 `None`
- [`00bffb28`](#insn-00bffb28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffb2c`](#insn-00bffb2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffb34`](#insn-00bffb34) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffb10`](#insn-00bffb10)

~~~json
{
  "source": "00bffb10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffb14`](#insn-00bffb14)

~~~json
{
  "source": "00bffb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffb20`](#insn-00bffb20)

~~~json
{
  "source": "00bffb20",
  "target": "00c5e4a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffb28`](#insn-00bffb28)

~~~json
{
  "source": "00bffb28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffb2c`](#insn-00bffb2c)

~~~json
{
  "source": "00bffb2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffb34`](#insn-00bffb34)

~~~json
{
  "source": "00bffb34",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
