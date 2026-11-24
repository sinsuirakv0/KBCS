# 00acbe1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6de88`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6de88.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-851cb12d642b8958945865c7e02aa1c5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acc018`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc018.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-c153922739d257f2edbdef0ee74b4559)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbe1c",
  "name": "FUN_00acbe1c",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f95dbbb153ab12f99834fb51016d4ea4c0e621d24b2f166773324971c4eb105",
  "source_text_sha256": "2f95dbbb153ab12f99834fb51016d4ea4c0e621d24b2f166773324971c4eb105",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbe1c",
        "00acbe57"
      ]
    ],
    "bytes_sha256": "299b36e3ce8058a77513379dd82de3c574ce547e26c39ca0401b15cb12e492fb",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00acb88c](../00acb/00acb88c.md)
- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 208 bytes

~~~c

void FUN_00acbe1c(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  *param_1 = 0;
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
<a id="insn-00acbe1c"></a> `00acbe1c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acbe20"></a> `00acbe20` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe24"></a> `00acbe24` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acbe28"></a> `00acbe28` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00acbe2c"></a> `00acbe2c` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00acbe30"></a> `00acbe30` | `f3 00 00 b4` | cbz x19,0x00acbe4c | `CONDITIONAL_JUMP`
<a id="insn-00acbe34"></a> `00acbe34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe38"></a> `00acbe38` | `95 fe ff 97` | bl 0x00acb88c | `UNCONDITIONAL_CALL`
<a id="insn-00acbe3c"></a> `00acbe3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe40"></a> `00acbe40` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe44"></a> `00acbe44` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acbe48"></a> `00acbe48` | `1a 2f 06 14` | b 0x00c57ab0 | `CALL_TERMINATOR`
<a id="insn-00acbe4c"></a> `00acbe4c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe50"></a> `00acbe50` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acbe54"></a> `00acbe54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbe1c`](#insn-00acbe1c) 範囲 `[['00acbe1c', '00acbe33']]`
  - `CONDITIONAL_JUMP` [`00acbe30`](#insn-00acbe30) → [`00acbe4c`](#insn-00acbe4c)
  - `FALL_THROUGH` [`00acbe30`](#insn-00acbe30) → [`00acbe34`](#insn-00acbe34)
- ブロック [`00acbe34`](#insn-00acbe34) 範囲 `[['00acbe34', '00acbe4b']]`
- ブロック [`00acbe4c`](#insn-00acbe4c) 範囲 `[['00acbe4c', '00acbe57']]`

## 命令位置別の参照

- [`00acbe1c`](#insn-00acbe1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe20`](#insn-00acbe20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe30`](#insn-00acbe30) → [`00acbe4c`](#insn-00acbe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe38`](#insn-00acbe38) → [`00acb88c`](00acb88c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acb88c` · 推定シンボル `None` · 推定型 `None`
- [`00acbe40`](#insn-00acbe40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe44`](#insn-00acbe44) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe48`](#insn-00acbe48) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acbe4c`](#insn-00acbe4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe50`](#insn-00acbe50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbe1c`](#insn-00acbe1c)

~~~json
{
  "source": "00acbe1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe20`](#insn-00acbe20)

~~~json
{
  "source": "00acbe20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe30`](#insn-00acbe30)

~~~json
{
  "source": "00acbe30",
  "target": "00acbe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe38`](#insn-00acbe38)

~~~json
{
  "source": "00acbe38",
  "target": "00acb88c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe40`](#insn-00acbe40)

~~~json
{
  "source": "00acbe40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe44`](#insn-00acbe44)

~~~json
{
  "source": "00acbe44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe48`](#insn-00acbe48)

~~~json
{
  "source": "00acbe48",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe4c`](#insn-00acbe4c)

~~~json
{
  "source": "00acbe4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe50`](#insn-00acbe50)

~~~json
{
  "source": "00acbe50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
