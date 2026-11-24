# 009fcfec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009fd188`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd188.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0058.md#compare-2acc4cdc19779185eeabe3b62164fa9a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009fcfec",
  "name": "FUN_009fcfec",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2931df64c526ea8b1d4ae4c9b8aeb6a1ff31258c15190d350327b8c97fb65b17",
  "source_text_sha256": "2931df64c526ea8b1d4ae4c9b8aeb6a1ff31258c15190d350327b8c97fb65b17",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009fcfec",
        "009fd00f"
      ]
    ],
    "bytes_sha256": "3ea6e167193e77dff0372194c392f80e8dd427373084c64e931bdbcc09c28a48",
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

void FUN_009fcfec(void)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c8a120;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009fcfec"></a> `009fcfec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-009fcff0"></a> `009fcff0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009fcff4"></a> `009fcff4` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-009fcff8"></a> `009fcff8` | `a6 6a 09 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-009fcffc"></a> `009fcffc` | `68 14 00 d0` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fd000"></a> `009fd000` | `08 81 04 91` | add x8,x8,#0x120 | `FALL_THROUGH`
<a id="insn-009fd004"></a> `009fd004` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-009fd008"></a> `009fd008` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-009fd00c"></a> `009fd00c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009fcfec`](#insn-009fcfec) 範囲 `[['009fcfec', '009fd00f']]`

## 命令位置別の参照

- [`009fcfec`](#insn-009fcfec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcff8`](#insn-009fcff8) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`009fd004`](#insn-009fd004) → `00c8a120`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fd008`](#insn-009fd008) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fcfec`](#insn-009fcfec)

~~~json
{
  "source": "009fcfec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcff8`](#insn-009fcff8)

~~~json
{
  "source": "009fcff8",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fd004`](#insn-009fd004)

~~~json
{
  "source": "009fd004",
  "target": "00c8a120",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8a120",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fd008`](#insn-009fd008)

~~~json
{
  "source": "009fd008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
