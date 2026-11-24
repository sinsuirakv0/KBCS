# 00c2dfec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2df50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0089.md#compare-ef438733699d93787ca472b1cc735008)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c2efe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2efe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0089.md#compare-82c94ee279635166865e27d93e0d4377)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2dfec",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c21a09d4858c0cbd292899d7f55464b62b4b8a94f4835e269996166a18c646f3",
  "source_text_sha256": "c21a09d4858c0cbd292899d7f55464b62b4b8a94f4835e269996166a18c646f3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2dfec",
        "00c2e057"
      ]
    ],
    "bytes_sha256": "fd55826b98b015d3634fdf1ba2aa265941c979e689b9b52295898c4a8055e368",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c2e058](../00c2e/00c2e058.md)
- [00c57f20](../00c57/00c57f20.md)
- [00c57f40](../00c57/00c57f40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 404 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv(void)

{
  int iVar1;
  
  if (((DAT_01127ff0 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127ff0), iVar1 != 0)) {
    FUN_00c2e058();
                    /* try { // try from 00c2e044 to 00d2e05f has its CatchHandler @ 00c2e514 */
    DAT_01127fe8 = &DAT_011287e8;
    __cxa_guard_release(&DAT_01127ff0);
  }
  return DAT_01127fe8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2dfec"></a> `00c2dfec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c2dff0"></a> `00c2dff0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00c2dff4"></a> `00c2dff4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c2dff8"></a> `00c2dff8` | `c8 27 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2dffc"></a> `00c2dffc` | `08 c1 3f 91` | add x8,x8,#0xff0 | `FALL_THROUGH`
<a id="insn-00c2e000"></a> `00c2e000` | `09 fd df 08` | ldarb w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2e004"></a> `00c2e004` | `c8 27 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e008"></a> `00c2e008` | `a9 00 00 36` | tbz w9,#0x0,0x00c2e01c | `CONDITIONAL_JUMP`
<a id="insn-00c2e00c"></a> `00c2e00c` | `00 f5 47 f9` | ldr x0,[x8, #0xfe8] | `FALL_THROUGH`
<a id="insn-00c2e010"></a> `00c2e010` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00c2e014"></a> `00c2e014` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c2e018"></a> `00c2e018` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c2e01c"></a> `00c2e01c` | `c0 27 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e020"></a> `00c2e020` | `00 c0 3f 91` | add x0,x0,#0xff0 | `FALL_THROUGH`
<a id="insn-00c2e024"></a> `00c2e024` | `bf a7 00 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e028"></a> `00c2e028` | `c8 27 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e02c"></a> `00c2e02c` | `00 ff ff 34` | cbz w0,0x00c2e00c | `CONDITIONAL_JUMP`
<a id="insn-00c2e030"></a> `00c2e030` | `0a 00 00 94` | bl 0x00c2e058 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e034"></a> `00c2e034` | `c9 27 00 d0` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2e038"></a> `00c2e038` | `29 a1 1f 91` | add x9,x9,#0x7e8 | `FALL_THROUGH`
<a id="insn-00c2e03c"></a> `00c2e03c` | `c8 27 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e040"></a> `00c2e040` | `c0 27 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e044"></a> `00c2e044` | `00 c0 3f 91` | add x0,x0,#0xff0 | `FALL_THROUGH`
<a id="insn-00c2e048"></a> `00c2e048` | `09 f5 07 f9` | str x9,[x8, #0xfe8] | `FALL_THROUGH`
<a id="insn-00c2e04c"></a> `00c2e04c` | `bd a7 00 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e050"></a> `00c2e050` | `c8 27 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e054"></a> `00c2e054` | `ee ff ff 17` | b 0x00c2e00c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c2dfec`](#insn-00c2dfec) 範囲 `[['00c2dfec', '00c2e00b']]`
  - `CONDITIONAL_JUMP` [`00c2e008`](#insn-00c2e008) → [`00c2e01c`](#insn-00c2e01c)
  - `FALL_THROUGH` [`00c2e008`](#insn-00c2e008) → [`00c2e00c`](#insn-00c2e00c)
- ブロック [`00c2e00c`](#insn-00c2e00c) 範囲 `[['00c2e00c', '00c2e01b']]`
- ブロック [`00c2e01c`](#insn-00c2e01c) 範囲 `[['00c2e01c', '00c2e02f']]`
  - `CONDITIONAL_JUMP` [`00c2e02c`](#insn-00c2e02c) → [`00c2e00c`](#insn-00c2e00c)
  - `FALL_THROUGH` [`00c2e02c`](#insn-00c2e02c) → [`00c2e030`](#insn-00c2e030)
- ブロック [`00c2e030`](#insn-00c2e030) 範囲 `[['00c2e030', '00c2e043']]`
  - `FALL_THROUGH` [`00c2e040`](#insn-00c2e040) → [`00c2e044`](#insn-00c2e044)
- ブロック [`00c2e044`](#insn-00c2e044) 範囲 `[['00c2e044', '00c2e057']]`
  - `UNCONDITIONAL_JUMP` [`00c2e054`](#insn-00c2e054) → [`00c2e00c`](#insn-00c2e00c)

## 命令位置別の参照

- [`00c2dff0`](#insn-00c2dff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e000`](#insn-00c2e000) → `01127ff0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e008`](#insn-00c2e008) → [`00c2e01c`](#insn-00c2e01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e00c`](#insn-00c2e00c) → `01127fe8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2e00c`](#insn-00c2e00c) → `011287e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e010`](#insn-00c2e010) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e020`](#insn-00c2e020) → `01127ff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e024`](#insn-00c2e024) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`00c2e02c`](#insn-00c2e02c) → [`00c2e00c`](#insn-00c2e00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e030`](#insn-00c2e030) → [`00c2e058`](../00c2e/00c2e058.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c2e058` · 推定シンボル `None` · 推定型 `None`
- [`00c2e044`](#insn-00c2e044) → `01127ff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e048`](#insn-00c2e048) → `01127fe8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2e048`](#insn-00c2e048) → `011287e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e04c`](#insn-00c2e04c) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`00c2e054`](#insn-00c2e054) → [`00c2e00c`](#insn-00c2e00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2dff0`](#insn-00c2dff0)

~~~json
{
  "source": "00c2dff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e000`](#insn-00c2e000)

~~~json
{
  "source": "00c2e000",
  "target": "01127ff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e008`](#insn-00c2e008)

~~~json
{
  "source": "00c2e008",
  "target": "00c2e01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e00c`](#insn-00c2e00c)

~~~json
{
  "source": "00c2e00c",
  "target": "01127fe8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fe8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e00c`](#insn-00c2e00c)

~~~json
{
  "source": "00c2e00c",
  "target": "011287e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011287e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e010`](#insn-00c2e010)

~~~json
{
  "source": "00c2e010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e020`](#insn-00c2e020)

~~~json
{
  "source": "00c2e020",
  "target": "01127ff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e024`](#insn-00c2e024)

~~~json
{
  "source": "00c2e024",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e02c`](#insn-00c2e02c)

~~~json
{
  "source": "00c2e02c",
  "target": "00c2e00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e030`](#insn-00c2e030)

~~~json
{
  "source": "00c2e030",
  "target": "00c2e058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e044`](#insn-00c2e044)

~~~json
{
  "source": "00c2e044",
  "target": "01127ff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e048`](#insn-00c2e048)

~~~json
{
  "source": "00c2e048",
  "target": "01127fe8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fe8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e048`](#insn-00c2e048)

~~~json
{
  "source": "00c2e048",
  "target": "011287e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011287e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e04c`](#insn-00c2e04c)

~~~json
{
  "source": "00c2e04c",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e054`](#insn-00c2e054)

~~~json
{
  "source": "00c2e054",
  "target": "00c2e00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
