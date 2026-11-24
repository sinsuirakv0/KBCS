# 00bffa9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff674`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff674.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-e52bb78123c35d02284021faddd3eba8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bffb38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb38.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-930d82f9f14d214c4d75bfd379a24ed7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffa9c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ffa2f4192e6e6f2c9d5fca00554f8c7023612d6c406120e64f29e1130c471f21",
  "source_text_sha256": "ffa2f4192e6e6f2c9d5fca00554f8c7023612d6c406120e64f29e1130c471f21",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffa9c",
        "00bffaef"
      ]
    ],
    "bytes_sha256": "6495fc6e3567476ca9e9bfc3a3666efa640597a150d94f5a488bd797d8610a1e",
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

- [00c5a7d0](../00c5a/00c5a7d0.md)
- [00c5e2e0](../00c5e/00c5e2e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE
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
<a id="insn-00bffa9c"></a> `00bffa9c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffaa0"></a> `00bffaa0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bffaa4"></a> `00bffaa4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffaa8"></a> `00bffaa8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffaac"></a> `00bffaac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bffab0"></a> `00bffab0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bffab4"></a> `00bffab4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bffab8"></a> `00bffab8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bffabc"></a> `00bffabc` | `89 86 40 f8` | ldr x9,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00bffac0"></a> `00bffac0` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bffac4"></a> `00bffac4` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bffac8"></a> `00bffac8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bffacc"></a> `00bffacc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bffad0"></a> `00bffad0` | `40 6b 01 94` | bl 0x00c5a7d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffad4"></a> `00bffad4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bffad8"></a> `00bffad8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bffadc"></a> `00bffadc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffae0"></a> `00bffae0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffae4"></a> `00bffae4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bffae8"></a> `00bffae8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffaec"></a> `00bffaec` | `fd 79 01 14` | b 0x00c5e2e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffa9c`](#insn-00bffa9c) 範囲 `[['00bffa9c', '00bffaef']]`

## 命令位置別の参照

- [`00bffaa0`](#insn-00bffaa0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffaa4`](#insn-00bffaa4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffaa8`](#insn-00bffaa8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffad0`](#insn-00bffad0) → [`00c5a7d0`](../00c5a/00c5a7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7d0` · 推定シンボル `None` · 推定型 `None`
- [`00bffadc`](#insn-00bffadc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffae0`](#insn-00bffae0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffae4`](#insn-00bffae4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffaec`](#insn-00bffaec) → [`00c5e2e0`](../00c5e/00c5e2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffaa0`](#insn-00bffaa0)

~~~json
{
  "source": "00bffaa0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffaa4`](#insn-00bffaa4)

~~~json
{
  "source": "00bffaa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffaa8`](#insn-00bffaa8)

~~~json
{
  "source": "00bffaa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffad0`](#insn-00bffad0)

~~~json
{
  "source": "00bffad0",
  "target": "00c5a7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffadc`](#insn-00bffadc)

~~~json
{
  "source": "00bffadc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffae0`](#insn-00bffae0)

~~~json
{
  "source": "00bffae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffae4`](#insn-00bffae4)

~~~json
{
  "source": "00bffae4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffaec`](#insn-00bffaec)

~~~json
{
  "source": "00bffaec",
  "target": "00c5e2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
