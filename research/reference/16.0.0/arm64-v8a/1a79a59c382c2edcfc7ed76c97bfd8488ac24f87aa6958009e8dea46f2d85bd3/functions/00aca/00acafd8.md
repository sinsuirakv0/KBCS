# 00acafd8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6d044`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d044.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-8f005fc76ce8cf80a4914313ebbb325b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acb1d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb1d4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-f79acca8a80d0439173aa12903efffa3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acafd8",
  "name": "FUN_00acafd8",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5766b809869cd6c32aff13d345f59535a579ab23b37e5952462087990f4d67b",
  "source_text_sha256": "e5766b809869cd6c32aff13d345f59535a579ab23b37e5952462087990f4d67b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acafd8",
        "00acaffb"
      ]
    ],
    "bytes_sha256": "54b8e15b06ebad6b2daf8b648b74dbb1e7b1ac1affe2697754b0f4e99e6f901c",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 135 bytes

~~~c

void FUN_00acafd8(void)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c8d340;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acafd8"></a> `00acafd8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00acafdc"></a> `00acafdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acafe0"></a> `00acafe0` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00acafe4"></a> `00acafe4` | `ab 32 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00acafe8"></a> `00acafe8` | `08 0e 00 f0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00acafec"></a> `00acafec` | `08 01 0d 91` | add x8,x8,#0x340 | `FALL_THROUGH`
<a id="insn-00acaff0"></a> `00acaff0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00acaff4"></a> `00acaff4` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00acaff8"></a> `00acaff8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acafd8`](#insn-00acafd8) 範囲 `[['00acafd8', '00acaffb']]`

## 命令位置別の参照

- [`00acafd8`](#insn-00acafd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafe4`](#insn-00acafe4) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00acaff0`](#insn-00acaff0) → `00c8d340`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acaff4`](#insn-00acaff4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acafd8`](#insn-00acafd8)

~~~json
{
  "source": "00acafd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafe4`](#insn-00acafe4)

~~~json
{
  "source": "00acafe4",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaff0`](#insn-00acaff0)

~~~json
{
  "source": "00acaff0",
  "target": "00c8d340",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d340",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acaff4`](#insn-00acaff4)

~~~json
{
  "source": "00acaff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
