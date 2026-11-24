# 00afb8cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-0e21548a498b1b07d0427ad701e077fb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afbcf4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afbcf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0036.md#compare-5f68b38a88c518164b207ee1010e5098)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb8cc",
  "name": "FUN_00afb8cc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53ded58fb6c464d38411efd77bbb7a236fc9aac1bc645d7b62f1d98881f8ec80",
  "source_text_sha256": "53ded58fb6c464d38411efd77bbb7a236fc9aac1bc645d7b62f1d98881f8ec80",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb8cc",
        "00afb917"
      ]
    ],
    "bytes_sha256": "62a3dc9c2dba06f1850695db7c257b73b56680b084d61be31cec2bfe0a4adfbd",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afb8cc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849d4) = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb8cc"></a> `00afb8cc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afb8d0"></a> `00afb8d0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb8d4"></a> `00afb8d4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb8d8"></a> `00afb8d8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afb8dc"></a> `00afb8dc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afb8e0"></a> `00afb8e0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afb8e4"></a> `00afb8e4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afb8e8"></a> `00afb8e8` | `f4 56 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb8ec"></a> `00afb8ec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb8f0"></a> `00afb8f0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb8f4"></a> `00afb8f4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb8f8"></a> `00afb8f8` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb8fc"></a> `00afb8fc` | `89 3a 89 52` | mov w9,#0x49d4 | `FALL_THROUGH`
<a id="insn-00afb900"></a> `00afb900` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb904"></a> `00afb904` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb908"></a> `00afb908` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb90c"></a> `00afb90c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb910"></a> `00afb910` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afb914"></a> `00afb914` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb8cc`](#insn-00afb8cc) 範囲 `[['00afb8cc', '00afb917']]`

## 命令位置別の参照

- [`00afb8cc`](#insn-00afb8cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb8d0`](#insn-00afb8d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb8d4`](#insn-00afb8d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb8e8`](#insn-00afb8e8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afb908`](#insn-00afb908) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb90c`](#insn-00afb90c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb910`](#insn-00afb910) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb8cc`](#insn-00afb8cc)

~~~json
{
  "source": "00afb8cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb8d0`](#insn-00afb8d0)

~~~json
{
  "source": "00afb8d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb8d4`](#insn-00afb8d4)

~~~json
{
  "source": "00afb8d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb8e8`](#insn-00afb8e8)

~~~json
{
  "source": "00afb8e8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb908`](#insn-00afb908)

~~~json
{
  "source": "00afb908",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb90c`](#insn-00afb90c)

~~~json
{
  "source": "00afb90c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb910`](#insn-00afb910)

~~~json
{
  "source": "00afb910",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
