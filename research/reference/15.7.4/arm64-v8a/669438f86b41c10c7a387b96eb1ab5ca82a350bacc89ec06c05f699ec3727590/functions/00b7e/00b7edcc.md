# 00b7edcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7ed88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0014.md#compare-159b6ced24ade15b38d0d423f3ad43e1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb814`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb814.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0020.md#compare-623bf948f5c53912a54bd4f8f2068097)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7edcc",
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
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7edcc",
        "00b7ee1f"
      ]
    ],
    "bytes_sha256": "291cdb606d076261cf1ca17078c530e4e71a20f2ada3df71c42dec64294c3129",
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

- [00bdd980](../00bdd/00bdd980.md)
- [00be12e0](../00be1/00be12e0.md)

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
<a id="insn-00b7edcc"></a> `00b7edcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7edd0"></a> `00b7edd0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b7edd4"></a> `00b7edd4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7edd8"></a> `00b7edd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7eddc"></a> `00b7eddc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b7ede0"></a> `00b7ede0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b7ede4"></a> `00b7ede4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b7ede8"></a> `00b7ede8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00b7edec"></a> `00b7edec` | `89 86 40 f8` | ldr x9,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00b7edf0"></a> `00b7edf0` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b7edf4"></a> `00b7edf4` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b7edf8"></a> `00b7edf8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b7edfc"></a> `00b7edfc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b7ee00"></a> `00b7ee00` | `e0 7a 01 94` | bl 0x00bdd980 | `UNCONDITIONAL_CALL`
<a id="insn-00b7ee04"></a> `00b7ee04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b7ee08"></a> `00b7ee08` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b7ee0c"></a> `00b7ee0c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7ee10"></a> `00b7ee10` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7ee14"></a> `00b7ee14` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b7ee18"></a> `00b7ee18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7ee1c"></a> `00b7ee1c` | `31 89 01 14` | b 0x00be12e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7edcc`](#insn-00b7edcc) 範囲 `[['00b7edcc', '00b7ee1f']]`

## 命令位置別の参照

- [`00b7edd0`](#insn-00b7edd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7edd4`](#insn-00b7edd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7edd8`](#insn-00b7edd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ee00`](#insn-00b7ee00) → [`00bdd980`](../00bdd/00bdd980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd980` · 推定シンボル `None` · 推定型 `None`
- [`00b7ee0c`](#insn-00b7ee0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ee10`](#insn-00b7ee10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ee14`](#insn-00b7ee14) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ee1c`](#insn-00b7ee1c) → [`00be12e0`](../00be1/00be12e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be12e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7edd0`](#insn-00b7edd0)

~~~json
{
  "source": "00b7edd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7edd4`](#insn-00b7edd4)

~~~json
{
  "source": "00b7edd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7edd8`](#insn-00b7edd8)

~~~json
{
  "source": "00b7edd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ee00`](#insn-00b7ee00)

~~~json
{
  "source": "00b7ee00",
  "target": "00bdd980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7ee0c`](#insn-00b7ee0c)

~~~json
{
  "source": "00b7ee0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ee10`](#insn-00b7ee10)

~~~json
{
  "source": "00b7ee10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ee14`](#insn-00b7ee14)

~~~json
{
  "source": "00b7ee14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ee1c`](#insn-00b7ee1c)

~~~json
{
  "source": "00b7ee1c",
  "target": "00be12e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
