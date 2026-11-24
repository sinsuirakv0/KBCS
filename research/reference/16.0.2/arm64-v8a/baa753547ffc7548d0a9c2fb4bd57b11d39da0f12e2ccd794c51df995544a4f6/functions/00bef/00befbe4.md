# 00befbe4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befb48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-fc5f5b7da94b026f94334df4c324ffc8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf0bd8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0bd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-2e8e47427953bcdcc9daa19b90610ad5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befbe4",
  "name": "_ZSt17current_exceptionv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f8728db7cc57237c9b622542ef4abd517fbc75dabce2a85fce939f597b014453",
  "source_text_sha256": "f8728db7cc57237c9b622542ef4abd517fbc75dabce2a85fce939f597b014453",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befbe4",
        "00befc0f"
      ]
    ],
    "bytes_sha256": "274e779b8fd9c369c66145590826bee4e05efaa6995568cc375d651585e403c6",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58630](../00c58/00c58630.md)

## 呼び出し先

- [00c5e010](../00c5e/00c5e010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 156 bytes

~~~c

void _ZSt17current_exceptionv(undefined8 *param_1)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_current_primary_exception();
  *param_1 = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befbe4"></a> `00befbe4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befbe8"></a> `00befbe8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00befbec"></a> `00befbec` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befbf0"></a> `00befbf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befbf4"></a> `00befbf4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00befbf8"></a> `00befbf8` | `06 b9 01 94` | bl 0x00c5e010 | `UNCONDITIONAL_CALL`
<a id="insn-00befbfc"></a> `00befbfc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00befc00"></a> `00befc00` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befc04"></a> `00befc04` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00befc08"></a> `00befc08` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befc0c"></a> `00befc0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befbe4`](#insn-00befbe4) 範囲 `[['00befbe4', '00befc0f']]`

## 命令位置別の参照

- [`00befbe8`](#insn-00befbe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbec`](#insn-00befbec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbf8`](#insn-00befbf8) → [`00c5e010`](../00c5e/00c5e010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e010` · 推定シンボル `None` · 推定型 `None`
- [`00befc00`](#insn-00befc00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc04`](#insn-00befc04) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befbe8`](#insn-00befbe8)

~~~json
{
  "source": "00befbe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbec`](#insn-00befbec)

~~~json
{
  "source": "00befbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbf8`](#insn-00befbf8)

~~~json
{
  "source": "00befbf8",
  "target": "00c5e010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befc00`](#insn-00befc00)

~~~json
{
  "source": "00befc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc04`](#insn-00befc04)

~~~json
{
  "source": "00befc04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
