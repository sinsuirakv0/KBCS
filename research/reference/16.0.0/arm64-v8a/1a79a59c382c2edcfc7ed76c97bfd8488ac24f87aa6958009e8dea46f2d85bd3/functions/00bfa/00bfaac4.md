# 00bfaac4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e07c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0018.md#compare-442c24666e42997e0bb3aaa845c088e9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfaeec`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaeec.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-a3414344248706c62645da7b9f5fa549)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaac4",
  "name": "_ZNSt6__ndk117iostream_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc47307183cf9b19063f199a722ee44630cd2e50b5f3a46f3abd52fe6ac612e2",
  "source_text_sha256": "cc47307183cf9b19063f199a722ee44630cd2e50b5f3a46f3abd52fe6ac612e2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaac4",
        "00bfab13"
      ]
    ],
    "bytes_sha256": "f9b9f784f037bcc576b0ba94f64ed7959d54e7384fb71cc0438c25fe9d25cca5",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 243 bytes

~~~c

undefined ** _ZNSt6__ndk117iostream_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01126f90 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01126f90), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01126f90);
  }
  return &PTR_PTR_00ca4400;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaac4"></a> `00bfaac4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaac8"></a> `00bfaac8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfaacc"></a> `00bfaacc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaad0"></a> `00bfaad0` | `68 29 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bfaad4"></a> `00bfaad4` | `08 41 3e 91` | add x8,x8,#0xf90 | `FALL_THROUGH`
<a id="insn-00bfaad8"></a> `00bfaad8` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bfaadc"></a> `00bfaadc` | `c8 00 00 36` | tbz w8,#0x0,0x00bfaaf4 | `CONDITIONAL_JUMP`
<a id="insn-00bfaae0"></a> `00bfaae0` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bfaae4"></a> `00bfaae4` | `e0 c8 54 10` | adr x0,0xca4400 | `FALL_THROUGH`
<a id="insn-00bfaae8"></a> `00bfaae8` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfaaec"></a> `00bfaaec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfaaf0"></a> `00bfaaf0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfaaf4"></a> `00bfaaf4` | `60 29 00 90` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bfaaf8"></a> `00bfaaf8` | `00 40 3e 91` | add x0,x0,#0xf90 | `FALL_THROUGH`
<a id="insn-00bfaafc"></a> `00bfaafc` | `d5 73 01 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00bfab00"></a> `00bfab00` | `00 ff ff 34` | cbz w0,0x00bfaae0 | `CONDITIONAL_JUMP`
<a id="insn-00bfab04"></a> `00bfab04` | `60 29 00 90` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bfab08"></a> `00bfab08` | `00 40 3e 91` | add x0,x0,#0xf90 | `FALL_THROUGH`
<a id="insn-00bfab0c"></a> `00bfab0c` | `d9 73 01 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfab10"></a> `00bfab10` | `f4 ff ff 17` | b 0x00bfaae0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfaac4`](#insn-00bfaac4) 範囲 `[['00bfaac4', '00bfaadf']]`
  - `CONDITIONAL_JUMP` [`00bfaadc`](#insn-00bfaadc) → [`00bfaaf4`](#insn-00bfaaf4)
  - `FALL_THROUGH` [`00bfaadc`](#insn-00bfaadc) → [`00bfaae0`](#insn-00bfaae0)
- ブロック [`00bfaae0`](#insn-00bfaae0) 範囲 `[['00bfaae0', '00bfaaf3']]`
- ブロック [`00bfaaf4`](#insn-00bfaaf4) 範囲 `[['00bfaaf4', '00bfab03']]`
  - `CONDITIONAL_JUMP` [`00bfab00`](#insn-00bfab00) → [`00bfaae0`](#insn-00bfaae0)
  - `FALL_THROUGH` [`00bfab00`](#insn-00bfab00) → [`00bfab04`](#insn-00bfab04)
- ブロック [`00bfab04`](#insn-00bfab04) 範囲 `[['00bfab04', '00bfab13']]`
  - `UNCONDITIONAL_JUMP` [`00bfab10`](#insn-00bfab10) → [`00bfaae0`](#insn-00bfaae0)

## 命令位置別の参照

- [`00bfaac8`](#insn-00bfaac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaad8`](#insn-00bfaad8) → `01126f90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfaadc`](#insn-00bfaadc) → [`00bfaaf4`](#insn-00bfaaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaae4`](#insn-00bfaae4) → `00ca4400`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfaae8`](#insn-00bfaae8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaaf8`](#insn-00bfaaf8) → `01126f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfaafc`](#insn-00bfaafc) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00bfab00`](#insn-00bfab00) → [`00bfaae0`](#insn-00bfaae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab08`](#insn-00bfab08) → `01126f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfab0c`](#insn-00bfab0c) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00bfab10`](#insn-00bfab10) → [`00bfaae0`](#insn-00bfaae0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaac8`](#insn-00bfaac8)

~~~json
{
  "source": "00bfaac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaad8`](#insn-00bfaad8)

~~~json
{
  "source": "00bfaad8",
  "target": "01126f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfaadc`](#insn-00bfaadc)

~~~json
{
  "source": "00bfaadc",
  "target": "00bfaaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaae4`](#insn-00bfaae4)

~~~json
{
  "source": "00bfaae4",
  "target": "00ca4400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4400",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfaae8`](#insn-00bfaae8)

~~~json
{
  "source": "00bfaae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaaf8`](#insn-00bfaaf8)

~~~json
{
  "source": "00bfaaf8",
  "target": "01126f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfaafc`](#insn-00bfaafc)

~~~json
{
  "source": "00bfaafc",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfab00`](#insn-00bfab00)

~~~json
{
  "source": "00bfab00",
  "target": "00bfaae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab08`](#insn-00bfab08)

~~~json
{
  "source": "00bfab08",
  "target": "01126f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfab0c`](#insn-00bfab0c)

~~~json
{
  "source": "00bfab0c",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfab10`](#insn-00bfab10)

~~~json
{
  "source": "00bfab10",
  "target": "00bfaae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
