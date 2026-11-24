# 00bffa4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bff9b0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9b0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-f5970bc3afa86b84d839a99274a846a5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00a40`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00a40.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-b617a5a41dc5b323d62120f907b4b6ab)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffa4c",
  "name": "_ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4aee3d14543e4a4d45e9b14947de920c5466d852c65455162211cebab0403a02",
  "source_text_sha256": "4aee3d14543e4a4d45e9b14947de920c5466d852c65455162211cebab0403a02",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffa4c",
        "00bffa77"
      ]
    ],
    "bytes_sha256": "d171aaeea8e58c6b9e3191f1b8de09d31730564d53e2f98b7bbd98de1a380b02",
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
- [00c5e480](../00c5e/00c5e480.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 161 bytes

~~~c

void _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev(void *param_1)

{
  _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffa4c"></a> `00bffa4c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffa50"></a> `00bffa50` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bffa54"></a> `00bffa54` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa58"></a> `00bffa58` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bffa5c"></a> `00bffa5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bffa60"></a> `00bffa60` | `88 7a 01 94` | bl 0x00c5e480 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa64"></a> `00bffa64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffa68"></a> `00bffa68` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa6c"></a> `00bffa6c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bffa70"></a> `00bffa70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffa74"></a> `00bffa74` | `43 61 01 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffa4c`](#insn-00bffa4c) 範囲 `[['00bffa4c', '00bffa77']]`

## 命令位置別の参照

- [`00bffa50`](#insn-00bffa50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffa54`](#insn-00bffa54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffa60`](#insn-00bffa60) → [`00c5e480`](../00c5e/00c5e480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e480` · 推定シンボル `None` · 推定型 `None`
- [`00bffa68`](#insn-00bffa68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffa6c`](#insn-00bffa6c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffa74`](#insn-00bffa74) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffa50`](#insn-00bffa50)

~~~json
{
  "source": "00bffa50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffa54`](#insn-00bffa54)

~~~json
{
  "source": "00bffa54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffa60`](#insn-00bffa60)

~~~json
{
  "source": "00bffa60",
  "target": "00c5e480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa68`](#insn-00bffa68)

~~~json
{
  "source": "00bffa68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffa6c`](#insn-00bffa6c)

~~~json
{
  "source": "00bffa6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffa74`](#insn-00bffa74)

~~~json
{
  "source": "00bffa74",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
