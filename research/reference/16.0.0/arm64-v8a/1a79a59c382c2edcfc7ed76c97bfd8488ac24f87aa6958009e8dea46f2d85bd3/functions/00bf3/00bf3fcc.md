# 00bf3fcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b77584`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77584.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-5d3c567d8116ad9134cbac8b75fbdaf5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf43f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0040.md#compare-93ea53ff2b23c979d8b998972cbfcf3d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf3fcc",
  "name": "FUN_00bf3fcc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc0a66bb4e5c7940a94dc44d63c144f2622f62b16de045a618ecc2d5e9667bd9",
  "source_text_sha256": "fc0a66bb4e5c7940a94dc44d63c144f2622f62b16de045a618ecc2d5e9667bd9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf3fcc",
        "00bf4007"
      ]
    ],
    "bytes_sha256": "78878b75016cd547e2cefb6f9675f261c1a07569e85ba94dc19c8e1e8e6dcc30",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bf3fc4](../00bf3/00bf3fc4.md)

## 呼び出し先

- [00bf2f78](../00bf2/00bf2f78.md)
- [00c5dc00](../00c5d/00c5dc00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 157 bytes

~~~c

void FUN_00bf3fcc(undefined8 param_1,wchar_t *param_2)

{
  size_t sVar1;
  
  sVar1 = wcslen(param_2);
  FUN_00bf2f78(param_1,param_2,sVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf3fcc"></a> `00bf3fcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf3fd0"></a> `00bf3fd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bf3fd4"></a> `00bf3fd4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3fd8"></a> `00bf3fd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf3fdc"></a> `00bf3fdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bf3fe0"></a> `00bf3fe0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bf3fe4"></a> `00bf3fe4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bf3fe8"></a> `00bf3fe8` | `06 a7 01 94` | bl 0x00c5dc00 | `UNCONDITIONAL_CALL`
<a id="insn-00bf3fec"></a> `00bf3fec` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bf3ff0"></a> `00bf3ff0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf3ff4"></a> `00bf3ff4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bf3ff8"></a> `00bf3ff8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3ffc"></a> `00bf3ffc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bf4000"></a> `00bf4000` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf4004"></a> `00bf4004` | `dd fb ff 17` | b 0x00bf2f78 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf3fcc`](#insn-00bf3fcc) 範囲 `[['00bf3fcc', '00bf4007']]`

## 命令位置別の参照

- [`00bf3fd0`](#insn-00bf3fd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3fd4`](#insn-00bf3fd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3fe8`](#insn-00bf3fe8) → [`00c5dc00`](../00c5d/00c5dc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc00` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ff8`](#insn-00bf3ff8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3ffc`](#insn-00bf3ffc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4004`](#insn-00bf4004) → [`00bf2f78`](../00bf2/00bf2f78.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf2f78` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf3fd0`](#insn-00bf3fd0)

~~~json
{
  "source": "00bf3fd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3fd4`](#insn-00bf3fd4)

~~~json
{
  "source": "00bf3fd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3fe8`](#insn-00bf3fe8)

~~~json
{
  "source": "00bf3fe8",
  "target": "00c5dc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf3ff8`](#insn-00bf3ff8)

~~~json
{
  "source": "00bf3ff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3ffc`](#insn-00bf3ffc)

~~~json
{
  "source": "00bf3ffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4004`](#insn-00bf4004)

~~~json
{
  "source": "00bf4004",
  "target": "00bf2f78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
