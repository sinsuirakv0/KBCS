# 00bfcccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbcd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-c0e5070f215241102472a66c04e0049f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcccc",
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
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcccc",
        "00bfcd1f"
      ]
    ],
    "bytes_sha256": "6863c7da3304db949e68d588832e8f2cf5b64d87e3f3cdb0d4e5d31461dba75d",
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

- [00c5b870](../00c5b/00c5b870.md)
- [00c5f380](../00c5f/00c5f380.md)

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
<a id="insn-00bfcccc"></a> `00bfcccc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfccd0"></a> `00bfccd0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfccd4"></a> `00bfccd4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfccd8"></a> `00bfccd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfccdc"></a> `00bfccdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfcce0"></a> `00bfcce0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfcce4"></a> `00bfcce4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfcce8"></a> `00bfcce8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bfccec"></a> `00bfccec` | `89 86 40 f8` | ldr x9,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00bfccf0"></a> `00bfccf0` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bfccf4"></a> `00bfccf4` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bfccf8"></a> `00bfccf8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfccfc"></a> `00bfccfc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfcd00"></a> `00bfcd00` | `dc 7a 01 94` | bl 0x00c5b870 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcd04"></a> `00bfcd04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfcd08"></a> `00bfcd08` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfcd0c"></a> `00bfcd0c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcd10"></a> `00bfcd10` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcd14"></a> `00bfcd14` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfcd18"></a> `00bfcd18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcd1c"></a> `00bfcd1c` | `99 89 01 14` | b 0x00c5f380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcccc`](#insn-00bfcccc) 範囲 `[['00bfcccc', '00bfcd1f']]`

## 命令位置別の参照

- [`00bfccd0`](#insn-00bfccd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfccd4`](#insn-00bfccd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfccd8`](#insn-00bfccd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd00`](#insn-00bfcd00) → [`00c5b870`](../00c5b/00c5b870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b870` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd0c`](#insn-00bfcd0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd10`](#insn-00bfcd10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd14`](#insn-00bfcd14) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd1c`](#insn-00bfcd1c) → [`00c5f380`](../00c5f/00c5f380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfccd0`](#insn-00bfccd0)

~~~json
{
  "source": "00bfccd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfccd4`](#insn-00bfccd4)

~~~json
{
  "source": "00bfccd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfccd8`](#insn-00bfccd8)

~~~json
{
  "source": "00bfccd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd00`](#insn-00bfcd00)

~~~json
{
  "source": "00bfcd00",
  "target": "00c5b870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcd0c`](#insn-00bfcd0c)

~~~json
{
  "source": "00bfcd0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd10`](#insn-00bfcd10)

~~~json
{
  "source": "00bfcd10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd14`](#insn-00bfcd14)

~~~json
{
  "source": "00bfcd14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd1c`](#insn-00bfcd1c)

~~~json
{
  "source": "00bfcd1c",
  "target": "00c5f380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
