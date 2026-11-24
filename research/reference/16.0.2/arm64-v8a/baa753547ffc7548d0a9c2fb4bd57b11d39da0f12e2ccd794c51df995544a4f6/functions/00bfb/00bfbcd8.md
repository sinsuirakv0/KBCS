# 00bfbcd8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbc3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbc3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-8d4b0483e4e8c0a5b8a7c94931f7e46d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfcccc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcccc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-c0e5070f215241102472a66c04e0049f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbcd8",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b618ca873f154b734ca720951478c68919994b2b749791c6ece2f0c31ae4f6c5",
  "source_text_sha256": "b618ca873f154b734ca720951478c68919994b2b749791c6ece2f0c31ae4f6c5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbcd8",
        "00bfbd2b"
      ]
    ],
    "bytes_sha256": "f554acbbf414b457ea7bcd41683cd64d470f767e0cb6efcd8a6e7caf3bb2fad4",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5e3b0](../00c5e/00c5e3b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  (**(code **)(*param_2 + 0x10))();
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 1);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 1,param_3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbcd8"></a> `00bfbcd8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbcdc"></a> `00bfbcdc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfbce0"></a> `00bfbce0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbce4"></a> `00bfbce4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbce8"></a> `00bfbce8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbcec"></a> `00bfbcec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfbcf0"></a> `00bfbcf0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfbcf4"></a> `00bfbcf4` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bfbcf8"></a> `00bfbcf8` | `89 86 40 f8` | ldr x9,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00bfbcfc"></a> `00bfbcfc` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbd00"></a> `00bfbd00` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bfbd04"></a> `00bfbd04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfbd08"></a> `00bfbd08` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfbd0c"></a> `00bfbd0c` | `e5 7a 01 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbd10"></a> `00bfbd10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfbd14"></a> `00bfbd14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfbd18"></a> `00bfbd18` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbd1c"></a> `00bfbd1c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbd20"></a> `00bfbd20` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfbd24"></a> `00bfbd24` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbd28"></a> `00bfbd28` | `a2 89 01 14` | b 0x00c5e3b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbcd8`](#insn-00bfbcd8) 範囲 `[['00bfbcd8', '00bfbd2b']]`

## 命令位置別の参照

- [`00bfbcdc`](#insn-00bfbcdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbce0`](#insn-00bfbce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbce4`](#insn-00bfbce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd0c`](#insn-00bfbd0c) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd18`](#insn-00bfbd18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd1c`](#insn-00bfbd1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd20`](#insn-00bfbd20) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd28`](#insn-00bfbd28) → [`00c5e3b0`](../00c5e/00c5e3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e3b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbcdc`](#insn-00bfbcdc)

~~~json
{
  "source": "00bfbcdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbce0`](#insn-00bfbce0)

~~~json
{
  "source": "00bfbce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbce4`](#insn-00bfbce4)

~~~json
{
  "source": "00bfbce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd0c`](#insn-00bfbd0c)

~~~json
{
  "source": "00bfbd0c",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbd18`](#insn-00bfbd18)

~~~json
{
  "source": "00bfbd18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd1c`](#insn-00bfbd1c)

~~~json
{
  "source": "00bfbd1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd20`](#insn-00bfbd20)

~~~json
{
  "source": "00bfbd20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd28`](#insn-00bfbd28)

~~~json
{
  "source": "00bfbd28",
  "target": "00c5e3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
