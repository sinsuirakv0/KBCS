# 009fcbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0156.md#review-3b9ff62747331b4a814672260310c948)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009fcd88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0058.md#compare-e647a836bb2dbcaf8c1e46bb543871d9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009fcbec",
  "name": "FUN_009fcbec",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4cb2efe8a7bef2312aeba372a99be47dbcc76bb5d350830baf3d083bed68668",
  "source_text_sha256": "a4cb2efe8a7bef2312aeba372a99be47dbcc76bb5d350830baf3d083bed68668",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009fcbec",
        "009fcc5b"
      ]
    ],
    "bytes_sha256": "f986ff8571273fe2c91fee6f4c0bbf80ff189414e52c13f540e5b1ecb569b3d4",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 527 bytes

~~~c

void FUN_009fcbec(undefined8 *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  undefined8 *__ptr;
  
  __ptr = (undefined8 *)*param_1;
  *param_1 = 0;
  if (__ptr == (undefined8 *)0x0) {
    return;
  }
  plVar1 = (long *)__ptr[10];
  plVar2 = __ptr + 6;
  *__ptr = &PTR_FUN_00c8a080;
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_009fcc4c;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_009fcc4c:
  _ZdlPv(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009fcbec"></a> `009fcbec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-009fcbf0"></a> `009fcbf0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009fcbf4"></a> `009fcbf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009fcbf8"></a> `009fcbf8` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-009fcbfc"></a> `009fcbfc` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-009fcc00"></a> `009fcc00` | `73 01 00 b4` | cbz x19,0x009fcc2c | `CONDITIONAL_JUMP`
<a id="insn-009fcc04"></a> `009fcc04` | `60 2a 40 f9` | ldr x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-009fcc08"></a> `009fcc08` | `69 c2 00 91` | add x9,x19,#0x30 | `FALL_THROUGH`
<a id="insn-009fcc0c"></a> `009fcc0c` | `68 14 00 d0` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fcc10"></a> `009fcc10` | `08 01 02 91` | add x8,x8,#0x80 | `FALL_THROUGH`
<a id="insn-009fcc14"></a> `009fcc14` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-009fcc18"></a> `009fcc18` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-009fcc1c"></a> `009fcc1c` | `e0 00 00 54` | b.eq 0x009fcc38 | `CONDITIONAL_JUMP`
<a id="insn-009fcc20"></a> `009fcc20` | `60 01 00 b4` | cbz x0,0x009fcc4c | `CONDITIONAL_JUMP`
<a id="insn-009fcc24"></a> `009fcc24` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fcc28"></a> `009fcc28` | `06 00 00 14` | b 0x009fcc40 | `UNCONDITIONAL_JUMP`
<a id="insn-009fcc2c"></a> `009fcc2c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009fcc30"></a> `009fcc30` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009fcc34"></a> `009fcc34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009fcc38"></a> `009fcc38` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fcc3c"></a> `009fcc3c` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-009fcc40"></a> `009fcc40` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fcc44"></a> `009fcc44` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fcc48"></a> `009fcc48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fcc4c"></a> `009fcc4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fcc50"></a> `009fcc50` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009fcc54"></a> `009fcc54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009fcc58"></a> `009fcc58` | `96 6b 09 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009fcbec`](#insn-009fcbec) 範囲 `[['009fcbec', '009fcc03']]`
  - `CONDITIONAL_JUMP` [`009fcc00`](#insn-009fcc00) → [`009fcc2c`](#insn-009fcc2c)
  - `FALL_THROUGH` [`009fcc00`](#insn-009fcc00) → [`009fcc04`](#insn-009fcc04)
- ブロック [`009fcc04`](#insn-009fcc04) 範囲 `[['009fcc04', '009fcc1f']]`
  - `CONDITIONAL_JUMP` [`009fcc1c`](#insn-009fcc1c) → [`009fcc38`](#insn-009fcc38)
  - `FALL_THROUGH` [`009fcc1c`](#insn-009fcc1c) → [`009fcc20`](#insn-009fcc20)
- ブロック [`009fcc20`](#insn-009fcc20) 範囲 `[['009fcc20', '009fcc23']]`
  - `CONDITIONAL_JUMP` [`009fcc20`](#insn-009fcc20) → [`009fcc4c`](#insn-009fcc4c)
  - `FALL_THROUGH` [`009fcc20`](#insn-009fcc20) → [`009fcc24`](#insn-009fcc24)
- ブロック [`009fcc24`](#insn-009fcc24) 範囲 `[['009fcc24', '009fcc2b']]`
  - `UNCONDITIONAL_JUMP` [`009fcc28`](#insn-009fcc28) → [`009fcc40`](#insn-009fcc40)
- ブロック [`009fcc2c`](#insn-009fcc2c) 範囲 `[['009fcc2c', '009fcc37']]`
- ブロック [`009fcc38`](#insn-009fcc38) 範囲 `[['009fcc38', '009fcc3f']]`
  - `FALL_THROUGH` [`009fcc3c`](#insn-009fcc3c) → [`009fcc40`](#insn-009fcc40)
- ブロック [`009fcc40`](#insn-009fcc40) 範囲 `[['009fcc40', '009fcc4b']]`
  - `FALL_THROUGH` [`009fcc48`](#insn-009fcc48) → [`009fcc4c`](#insn-009fcc4c)
- ブロック [`009fcc4c`](#insn-009fcc4c) 範囲 `[['009fcc4c', '009fcc5b']]`

## 命令位置別の参照

- [`009fcbec`](#insn-009fcbec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcbf0`](#insn-009fcbf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc00`](#insn-009fcc00) → [`009fcc2c`](#insn-009fcc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc18`](#insn-009fcc18) → `00c8a080`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fcc1c`](#insn-009fcc1c) → [`009fcc38`](#insn-009fcc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc20`](#insn-009fcc20) → [`009fcc4c`](#insn-009fcc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc28`](#insn-009fcc28) → [`009fcc40`](#insn-009fcc40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc2c`](#insn-009fcc2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc30`](#insn-009fcc30) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc50`](#insn-009fcc50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc54`](#insn-009fcc54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcc58`](#insn-009fcc58) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fcbec`](#insn-009fcbec)

~~~json
{
  "source": "009fcbec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcbf0`](#insn-009fcbf0)

~~~json
{
  "source": "009fcbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc00`](#insn-009fcc00)

~~~json
{
  "source": "009fcc00",
  "target": "009fcc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc18`](#insn-009fcc18)

~~~json
{
  "source": "009fcc18",
  "target": "00c8a080",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8a080",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fcc1c`](#insn-009fcc1c)

~~~json
{
  "source": "009fcc1c",
  "target": "009fcc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc20`](#insn-009fcc20)

~~~json
{
  "source": "009fcc20",
  "target": "009fcc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc28`](#insn-009fcc28)

~~~json
{
  "source": "009fcc28",
  "target": "009fcc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc2c`](#insn-009fcc2c)

~~~json
{
  "source": "009fcc2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc30`](#insn-009fcc30)

~~~json
{
  "source": "009fcc30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc50`](#insn-009fcc50)

~~~json
{
  "source": "009fcc50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc54`](#insn-009fcc54)

~~~json
{
  "source": "009fcc54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcc58`](#insn-009fcc58)

~~~json
{
  "source": "009fcc58",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
