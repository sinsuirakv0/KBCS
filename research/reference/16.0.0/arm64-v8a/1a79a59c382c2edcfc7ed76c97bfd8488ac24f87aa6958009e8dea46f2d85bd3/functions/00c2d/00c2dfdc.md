# 00c2dfdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bb1594`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1594.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-6917196673fd12182b7447de626e0b43)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2e404`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0089.md#compare-fb5b718078a3a481a4f90037a5bcb434)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2dfdc",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE3__cEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afef491d8d40edb7d987125c8bbbe1b20d89fc82d1aeb1d93a7a8f723db869df",
  "source_text_sha256": "afef491d8d40edb7d987125c8bbbe1b20d89fc82d1aeb1d93a7a8f723db869df",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2dfdc",
        "00c2e047"
      ]
    ],
    "bytes_sha256": "4d855b967a6104f15f8585f2c0dfdba8c16988bbb12c9a14ea666e12d2a7fc77",
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

- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

## 関連文字列（未確認候補）

~~~text
"(%a %b %d %H:%M:%S %Y"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 784 bytes

~~~c

char * _ZNKSt6__ndk120__time_get_c_storageIcE3__cEv(void)

{
  int iVar1;
  
  if (((DAT_01127b58 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127b58), iVar1 != 0)) {
    __cxa_atexit(PTR__ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev_00c9a7f8
                 ,s___a__b__d__H__M__S__Y_00ca4440,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00c2db08 with catch @ 00c2e038 */
                    /* catch() { ... } // from try @ 00c2da80 with catch @ 00c2e03c */
                    /* catch() { ... } // from try @ 00c2d9f8 with catch @ 00c2e040 */
    __cxa_guard_release(&DAT_01127b58);
                    /* catch() { ... } // from try @ 00c2d968 with catch @ 00c2e044 */
  }
  return s___a__b__d__H__M__S__Y_00ca4440;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2dfdc"></a> `00c2dfdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c2dfe0"></a> `00c2dfe0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00c2dfe4"></a> `00c2dfe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c2dfe8"></a> `00c2dfe8` | `c8 27 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2dfec"></a> `00c2dfec` | `08 61 2d 91` | add x8,x8,#0xb58 | `FALL_THROUGH`
<a id="insn-00c2dff0"></a> `00c2dff0` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00c2dff4"></a> `00c2dff4` | `c8 00 00 36` | tbz w8,#0x0,0x00c2e00c | `CONDITIONAL_JUMP`
<a id="insn-00c2dff8"></a> `00c2dff8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c2dffc"></a> `00c2dffc` | `20 22 3b 10` | adr x0,0xca4440 | `FALL_THROUGH`
<a id="insn-00c2e000"></a> `00c2e000` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00c2e004"></a> `00c2e004` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c2e008"></a> `00c2e008` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c2e00c"></a> `00c2e00c` | `c0 27 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e010"></a> `00c2e010` | `00 60 2d 91` | add x0,x0,#0xb58 | `FALL_THROUGH`
<a id="insn-00c2e014"></a> `00c2e014` | `8f a6 00 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e018"></a> `00c2e018` | `00 ff ff 34` | cbz w0,0x00c2dff8 | `CONDITIONAL_JUMP`
<a id="insn-00c2e01c"></a> `00c2e01c` | `60 03 00 90` | adrp x0,0xc9a000 | `FALL_THROUGH`
<a id="insn-00c2e020"></a> `00c2e020` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c2e024"></a> `00c2e024` | `e1 20 3b 10` | adr x1,0xca4440 | `FALL_THROUGH`
<a id="insn-00c2e028"></a> `00c2e028` | `00 fc 43 f9` | ldr x0,[x0, #0x7f8] | `FALL_THROUGH`
<a id="insn-00c2e02c"></a> `00c2e02c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c2e030"></a> `00c2e030` | `02 5b 1a 10` | adr x2,0xc62b90 | `FALL_THROUGH`
<a id="insn-00c2e034"></a> `00c2e034` | `7f a6 00 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e038"></a> `00c2e038` | `c0 27 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2e03c"></a> `00c2e03c` | `00 60 2d 91` | add x0,x0,#0xb58 | `FALL_THROUGH`
<a id="insn-00c2e040"></a> `00c2e040` | `8c a6 00 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e044"></a> `00c2e044` | `ed ff ff 17` | b 0x00c2dff8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c2dfdc`](#insn-00c2dfdc) 範囲 `[['00c2dfdc', '00c2dff7']]`
  - `CONDITIONAL_JUMP` [`00c2dff4`](#insn-00c2dff4) → [`00c2e00c`](#insn-00c2e00c)
  - `FALL_THROUGH` [`00c2dff4`](#insn-00c2dff4) → [`00c2dff8`](#insn-00c2dff8)
- ブロック [`00c2dff8`](#insn-00c2dff8) 範囲 `[['00c2dff8', '00c2e00b']]`
- ブロック [`00c2e00c`](#insn-00c2e00c) 範囲 `[['00c2e00c', '00c2e01b']]`
  - `CONDITIONAL_JUMP` [`00c2e018`](#insn-00c2e018) → [`00c2dff8`](#insn-00c2dff8)
  - `FALL_THROUGH` [`00c2e018`](#insn-00c2e018) → [`00c2e01c`](#insn-00c2e01c)
- ブロック [`00c2e01c`](#insn-00c2e01c) 範囲 `[['00c2e01c', '00c2e037']]`
  - `FALL_THROUGH` [`00c2e034`](#insn-00c2e034) → [`00c2e038`](#insn-00c2e038)
- ブロック [`00c2e038`](#insn-00c2e038) 範囲 `[['00c2e038', '00c2e03b']]`
  - `FALL_THROUGH` [`00c2e038`](#insn-00c2e038) → [`00c2e03c`](#insn-00c2e03c)
- ブロック [`00c2e03c`](#insn-00c2e03c) 範囲 `[['00c2e03c', '00c2e03f']]`
  - `FALL_THROUGH` [`00c2e03c`](#insn-00c2e03c) → [`00c2e040`](#insn-00c2e040)
- ブロック [`00c2e040`](#insn-00c2e040) 範囲 `[['00c2e040', '00c2e043']]`
  - `FALL_THROUGH` [`00c2e040`](#insn-00c2e040) → [`00c2e044`](#insn-00c2e044)
- ブロック [`00c2e044`](#insn-00c2e044) 範囲 `[['00c2e044', '00c2e047']]`
  - `UNCONDITIONAL_JUMP` [`00c2e044`](#insn-00c2e044) → [`00c2dff8`](#insn-00c2dff8)

## 命令位置別の参照

- [`00c2dfe0`](#insn-00c2dfe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2dff0`](#insn-00c2dff0) → `01127b58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2dff4`](#insn-00c2dff4) → [`00c2e00c`](#insn-00c2e00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2dffc`](#insn-00c2dffc) → `00ca4440`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c2e000`](#insn-00c2e000) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e010`](#insn-00c2e010) → `01127b58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e014`](#insn-00c2e014) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00c2e018`](#insn-00c2e018) → [`00c2dff8`](#insn-00c2dff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e024`](#insn-00c2e024) → `00ca4440`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c2e028`](#insn-00c2e028) → `00c9a7f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c2e028`](#insn-00c2e028) → [`00bc43c8`](../00bc4/00bc43c8.md) · `PARAM` · `ANALYSIS` · 関数 `00bc43c8` · 推定シンボル `_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev` · 推定型 `None`
- [`00c2e030`](#insn-00c2e030) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c2e034`](#insn-00c2e034) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00c2e03c`](#insn-00c2e03c) → `01127b58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e040`](#insn-00c2e040) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00c2e044`](#insn-00c2e044) → [`00c2dff8`](#insn-00c2dff8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2dfe0`](#insn-00c2dfe0)

~~~json
{
  "source": "00c2dfe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2dff0`](#insn-00c2dff0)

~~~json
{
  "source": "00c2dff0",
  "target": "01127b58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b58",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2dff4`](#insn-00c2dff4)

~~~json
{
  "source": "00c2dff4",
  "target": "00c2e00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2dffc`](#insn-00c2dffc)

~~~json
{
  "source": "00c2dffc",
  "target": "00ca4440",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4440",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e000`](#insn-00c2e000)

~~~json
{
  "source": "00c2e000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e010`](#insn-00c2e010)

~~~json
{
  "source": "00c2e010",
  "target": "01127b58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b58",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e014`](#insn-00c2e014)

~~~json
{
  "source": "00c2e014",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e018`](#insn-00c2e018)

~~~json
{
  "source": "00c2e018",
  "target": "00c2dff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e024`](#insn-00c2e024)

~~~json
{
  "source": "00c2e024",
  "target": "00ca4440",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4440",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e028`](#insn-00c2e028)

~~~json
{
  "source": "00c2e028",
  "target": "00c9a7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a7f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c2e028`](#insn-00c2e028)

~~~json
{
  "source": "00c2e028",
  "target": "00bc43c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e030`](#insn-00c2e030)

~~~json
{
  "source": "00c2e030",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c2e034`](#insn-00c2e034)

~~~json
{
  "source": "00c2e034",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e03c`](#insn-00c2e03c)

~~~json
{
  "source": "00c2e03c",
  "target": "01127b58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b58",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e040`](#insn-00c2e040)

~~~json
{
  "source": "00c2e040",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e044`](#insn-00c2e044)

~~~json
{
  "source": "00c2e044",
  "target": "00c2dff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
