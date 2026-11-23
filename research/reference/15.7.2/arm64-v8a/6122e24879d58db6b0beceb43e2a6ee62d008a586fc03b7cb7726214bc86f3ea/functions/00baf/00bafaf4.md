# 00bafaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bafbbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-3443b2096fbdb04f33987723463bd0bb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafaf4",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "975907a8ae54983651d58d8323847def352da2816f62eb4662a67826a74c835d",
  "source_text_sha256": "975907a8ae54983651d58d8323847def352da2816f62eb4662a67826a74c835d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafaf4",
        "00bafb5f"
      ]
    ],
    "bytes_sha256": "8a5c2523c870d95bb582b32a2e119fbaaca088484ecb4ca589ee48e0131eba31",
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

- [00bafb60](../00baf/00bafb60.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 404 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv(void)

{
  int iVar1;
  
  if (((DAT_010a2aa8 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_010a2aa8), iVar1 != 0)) {
    FUN_00bafb60();
    DAT_010a2aa0 = &DAT_010a2ba0;
    __cxa_guard_release(&DAT_010a2aa8);
                    /* try { // try from 00bafb5c to 00cafbab has its CatchHandler @ 00bb0d00 */
  }
  return DAT_010a2aa0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafaf4"></a> `00bafaf4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bafaf8"></a> `00bafaf8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bafafc"></a> `00bafafc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bafb00"></a> `00bafb00` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb04"></a> `00bafb04` | `08 a1 2a 91` | add x8,x8,#0xaa8 | `FALL_THROUGH`
<a id="insn-00bafb08"></a> `00bafb08` | `09 fd df 08` | ldarb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bafb0c"></a> `00bafb0c` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb10"></a> `00bafb10` | `a9 00 00 36` | tbz w9,#0x0,0x00bafb24 | `CONDITIONAL_JUMP`
<a id="insn-00bafb14"></a> `00bafb14` | `00 51 45 f9` | ldr x0,[x8, #0xaa0] | `FALL_THROUGH`
<a id="insn-00bafb18"></a> `00bafb18` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bafb1c"></a> `00bafb1c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bafb20"></a> `00bafb20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafb24"></a> `00bafb24` | `80 27 00 f0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb28"></a> `00bafb28` | `00 a0 2a 91` | add x0,x0,#0xaa8 | `FALL_THROUGH`
<a id="insn-00bafb2c"></a> `00bafb2c` | `f5 ac 00 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00bafb30"></a> `00bafb30` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb34"></a> `00bafb34` | `00 ff ff 34` | cbz w0,0x00bafb14 | `CONDITIONAL_JUMP`
<a id="insn-00bafb38"></a> `00bafb38` | `0a 00 00 94` | bl 0x00bafb60 | `UNCONDITIONAL_CALL`
<a id="insn-00bafb3c"></a> `00bafb3c` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb40"></a> `00bafb40` | `29 81 2e 91` | add x9,x9,#0xba0 | `FALL_THROUGH`
<a id="insn-00bafb44"></a> `00bafb44` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb48"></a> `00bafb48` | `80 27 00 f0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb4c"></a> `00bafb4c` | `00 a0 2a 91` | add x0,x0,#0xaa8 | `FALL_THROUGH`
<a id="insn-00bafb50"></a> `00bafb50` | `09 51 05 f9` | str x9,[x8, #0xaa0] | `FALL_THROUGH`
<a id="insn-00bafb54"></a> `00bafb54` | `f3 ac 00 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00bafb58"></a> `00bafb58` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafb5c"></a> `00bafb5c` | `ee ff ff 17` | b 0x00bafb14 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bafaf4`](#insn-00bafaf4) 範囲 `[['00bafaf4', '00bafb13']]`
  - `CONDITIONAL_JUMP` [`00bafb10`](#insn-00bafb10) → [`00bafb24`](#insn-00bafb24)
  - `FALL_THROUGH` [`00bafb10`](#insn-00bafb10) → [`00bafb14`](#insn-00bafb14)
- ブロック [`00bafb14`](#insn-00bafb14) 範囲 `[['00bafb14', '00bafb23']]`
- ブロック [`00bafb24`](#insn-00bafb24) 範囲 `[['00bafb24', '00bafb37']]`
  - `CONDITIONAL_JUMP` [`00bafb34`](#insn-00bafb34) → [`00bafb14`](#insn-00bafb14)
  - `FALL_THROUGH` [`00bafb34`](#insn-00bafb34) → [`00bafb38`](#insn-00bafb38)
- ブロック [`00bafb38`](#insn-00bafb38) 範囲 `[['00bafb38', '00bafb5b']]`
  - `FALL_THROUGH` [`00bafb58`](#insn-00bafb58) → [`00bafb5c`](#insn-00bafb5c)
- ブロック [`00bafb5c`](#insn-00bafb5c) 範囲 `[['00bafb5c', '00bafb5f']]`
  - `UNCONDITIONAL_JUMP` [`00bafb5c`](#insn-00bafb5c) → [`00bafb14`](#insn-00bafb14)

## 命令位置別の参照

- [`00bafaf8`](#insn-00bafaf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb08`](#insn-00bafb08) → `010a2aa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafb10`](#insn-00bafb10) → [`00bafb24`](#insn-00bafb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb14`](#insn-00bafb14) → `010a2aa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafb14`](#insn-00bafb14) → `010a2ba0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafb18`](#insn-00bafb18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb28`](#insn-00bafb28) → `010a2aa8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafb2c`](#insn-00bafb2c) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00bafb34`](#insn-00bafb34) → [`00bafb14`](#insn-00bafb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb38`](#insn-00bafb38) → [`00bafb60`](00bafb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bafb60` · 推定シンボル `None` · 推定型 `None`
- [`00bafb4c`](#insn-00bafb4c) → `010a2aa8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafb50`](#insn-00bafb50) → `010a2aa0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafb50`](#insn-00bafb50) → `010a2ba0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafb54`](#insn-00bafb54) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00bafb5c`](#insn-00bafb5c) → [`00bafb14`](#insn-00bafb14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafaf8`](#insn-00bafaf8)

~~~json
{
  "source": "00bafaf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb08`](#insn-00bafb08)

~~~json
{
  "source": "00bafb08",
  "target": "010a2aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2aa8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafb10`](#insn-00bafb10)

~~~json
{
  "source": "00bafb10",
  "target": "00bafb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb14`](#insn-00bafb14)

~~~json
{
  "source": "00bafb14",
  "target": "010a2aa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2aa0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafb14`](#insn-00bafb14)

~~~json
{
  "source": "00bafb14",
  "target": "010a2ba0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ba0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafb18`](#insn-00bafb18)

~~~json
{
  "source": "00bafb18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb28`](#insn-00bafb28)

~~~json
{
  "source": "00bafb28",
  "target": "010a2aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2aa8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafb2c`](#insn-00bafb2c)

~~~json
{
  "source": "00bafb2c",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafb34`](#insn-00bafb34)

~~~json
{
  "source": "00bafb34",
  "target": "00bafb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb38`](#insn-00bafb38)

~~~json
{
  "source": "00bafb38",
  "target": "00bafb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafb4c`](#insn-00bafb4c)

~~~json
{
  "source": "00bafb4c",
  "target": "010a2aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2aa8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafb50`](#insn-00bafb50)

~~~json
{
  "source": "00bafb50",
  "target": "010a2aa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2aa0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafb50`](#insn-00bafb50)

~~~json
{
  "source": "00bafb50",
  "target": "010a2ba0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ba0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafb54`](#insn-00bafb54)

~~~json
{
  "source": "00bafb54",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafb5c`](#insn-00bafb5c)

~~~json
{
  "source": "00bafb5c",
  "target": "00bafb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
