# 005cfcbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `005aaff0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md) · 移動量 `+0x24ccc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0023.md#compare-2aa1828ab4e725c77ae5aaf8ebc35caa)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `005cfcfc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfcfc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0024.md#compare-32d5ba2f69340c09d2d6752ba824e462)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cfcbc",
  "name": "FUN_005cfcbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa079ad4230c72a53c8731464e5d1774b78447b212e75e792e716dd69314442d",
  "source_text_sha256": "aa079ad4230c72a53c8731464e5d1774b78447b212e75e792e716dd69314442d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cfcbc",
        "005cfccf"
      ]
    ],
    "bytes_sha256": "c3490373f2d0e03c99594d87987e4b34cf6b0dd5079bc2d56e43d8a5d1a348c6",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005cfaf4](../005cf/005cfaf4.md)
- [005cfd60](../005cf/005cfd60.md)
- [005d0344](../005d0/005d0344.md)
- [005d804c](../005d8/005d804c.md)

## 呼び出し先

- [0043b738](../0043b/0043b738.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_005cfcbc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_0043b738("vector");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cfcbc"></a> `005cfcbc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-005cfcc0"></a> `005cfcc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005cfcc4"></a> `005cfcc4` | `40 e7 ff 90` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-005cfcc8"></a> `005cfcc8` | `00 30 3c 91` | add x0,x0,#0xf0c | `FALL_THROUGH`
<a id="insn-005cfccc"></a> `005cfccc` | `9b ae f9 97` | bl 0x0043b738 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cfcbc`](#insn-005cfcbc) 範囲 `[['005cfcbc', '005cfccf']]`

## 命令位置別の参照

- [`005cfcbc`](#insn-005cfcbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cfcc8`](#insn-005cfcc8) → `002b7f0c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cfccc`](#insn-005cfccc) → [`0043b738`](../0043b/0043b738.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b738` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cfcbc`](#insn-005cfcbc)

~~~json
{
  "source": "005cfcbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cfcc8`](#insn-005cfcc8)

~~~json
{
  "source": "005cfcc8",
  "target": "002b7f0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f0c",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "766563746f7200",
  "capture_start": "002b7f0c",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005cfccc`](#insn-005cfccc)

~~~json
{
  "source": "005cfccc",
  "target": "0043b738",
  "target_space": "ram",
  "resolution": "function"
}
~~~
