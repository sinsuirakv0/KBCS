# 00afed1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afecd8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afecd8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-aa2bdc18d2e40c20a96a4f9cb323a6ea)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5eaa0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5eaa0.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-6381b74285f3eac8943ec05144bb6211)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afed1c",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD0Ev",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a9ad010502a1a246bb61a9dca977afaf76f1e1f31c463b98debf1a03cd224ada",
  "source_text_sha256": "a9ad010502a1a246bb61a9dca977afaf76f1e1f31c463b98debf1a03cd224ada",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afed1c",
        "00afed3f"
      ]
    ],
    "bytes_sha256": "b4bfe68997508eb82364ed5f7fb92fbe7141e4b70447cefff79db4ee057291e4",
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

- [00bdb060](../00bdb/00bdb060.md)
- [00bdee20](../00bde/00bdee20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 325 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00afdb74 with catch @ 00afed1c */
                    /* catch() { ... } // from try @ 00af6ff4 with catch @ 00afed20 */
  _ZN8firebase26ReferenceCountedFutureImplD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afed1c"></a> `00afed1c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afed20"></a> `00afed20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afed24"></a> `00afed24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afed28"></a> `00afed28` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afed2c"></a> `00afed2c` | `3d 80 03 94` | bl 0x00bdee20 | `UNCONDITIONAL_CALL`
<a id="insn-00afed30"></a> `00afed30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afed34"></a> `00afed34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afed38"></a> `00afed38` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afed3c"></a> `00afed3c` | `c9 70 03 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afed1c`](#insn-00afed1c) 範囲 `[['00afed1c', '00afed1f']]`
  - `FALL_THROUGH` [`00afed1c`](#insn-00afed1c) → [`00afed20`](#insn-00afed20)
- ブロック [`00afed20`](#insn-00afed20) 範囲 `[['00afed20', '00afed3f']]`

## 命令位置別の参照

- [`00afed1c`](#insn-00afed1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed20`](#insn-00afed20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed2c`](#insn-00afed2c) → [`00bdee20`](../00bde/00bdee20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdee20` · 推定シンボル `None` · 推定型 `None`
- [`00afed30`](#insn-00afed30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed3c`](#insn-00afed3c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afed1c`](#insn-00afed1c)

~~~json
{
  "source": "00afed1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed20`](#insn-00afed20)

~~~json
{
  "source": "00afed20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed2c`](#insn-00afed2c)

~~~json
{
  "source": "00afed2c",
  "target": "00bdee20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afed30`](#insn-00afed30)

~~~json
{
  "source": "00afed30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed3c`](#insn-00afed3c)

~~~json
{
  "source": "00afed3c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
