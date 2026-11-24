# 00bf3adc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf3a40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-87936134184b2efe6a81a8b03c91fa47)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf4ad0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4ad0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-d65c488b5bb2255de96b95407c251c02)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf3adc",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dcf6df050c2fae4bed68da48a7eb029d70e6d9c8936d387acc153f5a900e90db",
  "source_text_sha256": "dcf6df050c2fae4bed68da48a7eb029d70e6d9c8936d387acc153f5a900e90db",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf3adc",
        "00bf3b27"
      ]
    ],
    "bytes_sha256": "c1f67b8833e686793aa1cee4db9373eda30a0ef25d7450aa997e732c3c4919f3",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e0d0](../00c5e/00c5e0d0.md)
- [00c5e0f0](../00c5e/00c5e0f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 346 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw
               (undefined8 param_1,undefined8 param_2,wchar_t *param_3)

{
  size_t sVar1;
  
  sVar1 = wcslen(param_3);
  _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm
            (param_1,param_2,param_3,sVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf3adc"></a> `00bf3adc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf3ae0"></a> `00bf3ae0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bf3ae4"></a> `00bf3ae4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3ae8"></a> `00bf3ae8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf3aec"></a> `00bf3aec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf3af0"></a> `00bf3af0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bf3af4"></a> `00bf3af4` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bf3af8"></a> `00bf3af8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bf3afc"></a> `00bf3afc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bf3b00"></a> `00bf3b00` | `74 a9 01 94` | bl 0x00c5e0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf3b04"></a> `00bf3b04` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bf3b08"></a> `00bf3b08` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bf3b0c"></a> `00bf3b0c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bf3b10"></a> `00bf3b10` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bf3b14"></a> `00bf3b14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf3b18"></a> `00bf3b18` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3b1c"></a> `00bf3b1c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bf3b20"></a> `00bf3b20` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf3b24"></a> `00bf3b24` | `73 a9 01 14` | b 0x00c5e0f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf3adc`](#insn-00bf3adc) 範囲 `[['00bf3adc', '00bf3b27']]`

## 命令位置別の参照

- [`00bf3ae0`](#insn-00bf3ae0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ae4`](#insn-00bf3ae4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ae8`](#insn-00bf3ae8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3b00`](#insn-00bf3b00) → [`00c5e0d0`](../00c5e/00c5e0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bf3b14`](#insn-00bf3b14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3b18`](#insn-00bf3b18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3b1c`](#insn-00bf3b1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3b24`](#insn-00bf3b24) → [`00c5e0f0`](../00c5e/00c5e0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e0f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf3ae0`](#insn-00bf3ae0)

~~~json
{
  "source": "00bf3ae0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3ae4`](#insn-00bf3ae4)

~~~json
{
  "source": "00bf3ae4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3ae8`](#insn-00bf3ae8)

~~~json
{
  "source": "00bf3ae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3b00`](#insn-00bf3b00)

~~~json
{
  "source": "00bf3b00",
  "target": "00c5e0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf3b14`](#insn-00bf3b14)

~~~json
{
  "source": "00bf3b14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3b18`](#insn-00bf3b18)

~~~json
{
  "source": "00bf3b18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3b1c`](#insn-00bf3b1c)

~~~json
{
  "source": "00bf3b1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3b24`](#insn-00bf3b24)

~~~json
{
  "source": "00bf3b24",
  "target": "00c5e0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
