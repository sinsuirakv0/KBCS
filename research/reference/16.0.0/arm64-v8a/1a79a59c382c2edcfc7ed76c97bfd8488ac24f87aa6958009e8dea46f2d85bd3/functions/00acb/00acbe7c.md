# 00acbe7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6dee8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dee8.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-e0c99f67cc80cb14c82fa0c19097556d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acc078`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc078.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-26b58fc90d49ab3a741ac25329b6994d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbe7c",
  "name": "FUN_00acbe7c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ec548f80c2b98a6f35f9d2ad5a9c3f952246a5c0938f7fecd3f9ada677a267a",
  "source_text_sha256": "9ec548f80c2b98a6f35f9d2ad5a9c3f952246a5c0938f7fecd3f9ada677a267a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbe7c",
        "00acbeb3"
      ]
    ],
    "bytes_sha256": "5dc8b717196a63cd81a4cfe46064e489b956e8252313c6bace7077a853e3aa00",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00acbb50](../00acb/00acbb50.md)

## 呼び出し先

- [00acb88c](../00acb/00acb88c.md)
- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 195 bytes

~~~c

void FUN_00acbe7c(long param_1)

{
  void *__ptr;
  
  __ptr = *(void **)(param_1 + 0x18);
  if (__ptr != (void *)0x0) {
    FUN_00acb88c(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbe7c"></a> `00acbe7c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acbe80"></a> `00acbe80` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe84"></a> `00acbe84` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acbe88"></a> `00acbe88` | `13 0c 40 f9` | ldr x19,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00acbe8c"></a> `00acbe8c` | `f3 00 00 b4` | cbz x19,0x00acbea8 | `CONDITIONAL_JUMP`
<a id="insn-00acbe90"></a> `00acbe90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe94"></a> `00acbe94` | `7e fe ff 97` | bl 0x00acb88c | `UNCONDITIONAL_CALL`
<a id="insn-00acbe98"></a> `00acbe98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe9c"></a> `00acbe9c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbea0"></a> `00acbea0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acbea4"></a> `00acbea4` | `03 2f 06 14` | b 0x00c57ab0 | `CALL_TERMINATOR`
<a id="insn-00acbea8"></a> `00acbea8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbeac"></a> `00acbeac` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acbeb0"></a> `00acbeb0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbe7c`](#insn-00acbe7c) 範囲 `[['00acbe7c', '00acbe8f']]`
  - `CONDITIONAL_JUMP` [`00acbe8c`](#insn-00acbe8c) → [`00acbea8`](#insn-00acbea8)
  - `FALL_THROUGH` [`00acbe8c`](#insn-00acbe8c) → [`00acbe90`](#insn-00acbe90)
- ブロック [`00acbe90`](#insn-00acbe90) 範囲 `[['00acbe90', '00acbea7']]`
- ブロック [`00acbea8`](#insn-00acbea8) 範囲 `[['00acbea8', '00acbeb3']]`

## 命令位置別の参照

- [`00acbe7c`](#insn-00acbe7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe80`](#insn-00acbe80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe8c`](#insn-00acbe8c) → [`00acbea8`](#insn-00acbea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe94`](#insn-00acbe94) → [`00acb88c`](00acb88c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acb88c` · 推定シンボル `None` · 推定型 `None`
- [`00acbe9c`](#insn-00acbe9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbea0`](#insn-00acbea0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbea4`](#insn-00acbea4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acbea8`](#insn-00acbea8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbeac`](#insn-00acbeac) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbe7c`](#insn-00acbe7c)

~~~json
{
  "source": "00acbe7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe80`](#insn-00acbe80)

~~~json
{
  "source": "00acbe80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe8c`](#insn-00acbe8c)

~~~json
{
  "source": "00acbe8c",
  "target": "00acbea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe94`](#insn-00acbe94)

~~~json
{
  "source": "00acbe94",
  "target": "00acb88c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe9c`](#insn-00acbe9c)

~~~json
{
  "source": "00acbe9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbea0`](#insn-00acbea0)

~~~json
{
  "source": "00acbea0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbea4`](#insn-00acbea4)

~~~json
{
  "source": "00acbea4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbea8`](#insn-00acbea8)

~~~json
{
  "source": "00acbea8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbeac`](#insn-00acbeac)

~~~json
{
  "source": "00acbeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
