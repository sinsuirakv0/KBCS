# 00c2caec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bb00a4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb00a4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-5d9bebde6804461a98901f96d3d2a771)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2cf14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0089.md#compare-5f41b4eee6dd6e20a4c4e356eb40f806)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2caec",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5d22c7149ff271b7cd0aac626b542d16846daa23afeb043d125f00283e45ee1",
  "source_text_sha256": "f5d22c7149ff271b7cd0aac626b542d16846daa23afeb043d125f00283e45ee1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2caec",
        "00c2cb53"
      ]
    ],
    "bytes_sha256": "135c32758e215be1265b5e752a702d47b37b5df704343517df3f73ac61046f4d",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c2cb6c](../00c2c/00c2cb6c.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv(void)

{
  int iVar1;
  
  if (((DAT_01127ac0 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127ac0), iVar1 != 0)) {
    FUN_00c2cb6c();
    DAT_01127ab8 = &DAT_01127d00;
    __cxa_guard_release(&DAT_01127ac0);
  }
  return DAT_01127ab8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2caec"></a> `00c2caec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c2caf0"></a> `00c2caf0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00c2caf4"></a> `00c2caf4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c2caf8"></a> `00c2caf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c2cafc"></a> `00c2cafc` | `c8 27 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb00"></a> `00c2cb00` | `08 01 2b 91` | add x8,x8,#0xac0 | `FALL_THROUGH`
<a id="insn-00c2cb04"></a> `00c2cb04` | `d3 27 00 f0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb08"></a> `00c2cb08` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00c2cb0c"></a> `00c2cb0c` | `c8 00 00 36` | tbz w8,#0x0,0x00c2cb24 | `CONDITIONAL_JUMP`
<a id="insn-00c2cb10"></a> `00c2cb10` | `60 5e 45 f9` | ldr x0,[x19, #0xab8] | `FALL_THROUGH`
<a id="insn-00c2cb14"></a> `00c2cb14` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c2cb18"></a> `00c2cb18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00c2cb1c"></a> `00c2cb1c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c2cb20"></a> `00c2cb20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c2cb24"></a> `00c2cb24` | `c0 27 00 f0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb28"></a> `00c2cb28` | `00 00 2b 91` | add x0,x0,#0xac0 | `FALL_THROUGH`
<a id="insn-00c2cb2c"></a> `00c2cb2c` | `c9 ab 00 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00c2cb30"></a> `00c2cb30` | `00 ff ff 34` | cbz w0,0x00c2cb10 | `CONDITIONAL_JUMP`
<a id="insn-00c2cb34"></a> `00c2cb34` | `0e 00 00 94` | bl 0x00c2cb6c | `UNCONDITIONAL_CALL`
<a id="insn-00c2cb38"></a> `00c2cb38` | `c8 27 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb3c"></a> `00c2cb3c` | `08 01 34 91` | add x8,x8,#0xd00 | `FALL_THROUGH`
<a id="insn-00c2cb40"></a> `00c2cb40` | `c0 27 00 f0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb44"></a> `00c2cb44` | `00 00 2b 91` | add x0,x0,#0xac0 | `FALL_THROUGH`
<a id="insn-00c2cb48"></a> `00c2cb48` | `68 5e 05 f9` | str x8,[x19, #0xab8] | `FALL_THROUGH`
<a id="insn-00c2cb4c"></a> `00c2cb4c` | `c9 ab 00 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00c2cb50"></a> `00c2cb50` | `f0 ff ff 17` | b 0x00c2cb10 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c2caec`](#insn-00c2caec) 範囲 `[['00c2caec', '00c2cb0f']]`
  - `CONDITIONAL_JUMP` [`00c2cb0c`](#insn-00c2cb0c) → [`00c2cb24`](#insn-00c2cb24)
  - `FALL_THROUGH` [`00c2cb0c`](#insn-00c2cb0c) → [`00c2cb10`](#insn-00c2cb10)
- ブロック [`00c2cb10`](#insn-00c2cb10) 範囲 `[['00c2cb10', '00c2cb23']]`
- ブロック [`00c2cb24`](#insn-00c2cb24) 範囲 `[['00c2cb24', '00c2cb33']]`
  - `CONDITIONAL_JUMP` [`00c2cb30`](#insn-00c2cb30) → [`00c2cb10`](#insn-00c2cb10)
  - `FALL_THROUGH` [`00c2cb30`](#insn-00c2cb30) → [`00c2cb34`](#insn-00c2cb34)
- ブロック [`00c2cb34`](#insn-00c2cb34) 範囲 `[['00c2cb34', '00c2cb53']]`
  - `UNCONDITIONAL_JUMP` [`00c2cb50`](#insn-00c2cb50) → [`00c2cb10`](#insn-00c2cb10)

## 命令位置別の参照

- [`00c2caf0`](#insn-00c2caf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2caf4`](#insn-00c2caf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb08`](#insn-00c2cb08) → `01127ac0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb0c`](#insn-00c2cb0c) → [`00c2cb24`](#insn-00c2cb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb10`](#insn-00c2cb10) → `01127ab8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cb10`](#insn-00c2cb10) → `01127d00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb14`](#insn-00c2cb14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb18`](#insn-00c2cb18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb28`](#insn-00c2cb28) → `01127ac0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb2c`](#insn-00c2cb2c) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb30`](#insn-00c2cb30) → [`00c2cb10`](#insn-00c2cb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb34`](#insn-00c2cb34) → [`00c2cb6c`](00c2cb6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c2cb6c` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb44`](#insn-00c2cb44) → `01127ac0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb48`](#insn-00c2cb48) → `01127ab8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cb48`](#insn-00c2cb48) → `01127d00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb4c`](#insn-00c2cb4c) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb50`](#insn-00c2cb50) → [`00c2cb10`](#insn-00c2cb10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2caf0`](#insn-00c2caf0)

~~~json
{
  "source": "00c2caf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2caf4`](#insn-00c2caf4)

~~~json
{
  "source": "00c2caf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb08`](#insn-00c2cb08)

~~~json
{
  "source": "00c2cb08",
  "target": "01127ac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ac0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb0c`](#insn-00c2cb0c)

~~~json
{
  "source": "00c2cb0c",
  "target": "00c2cb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb10`](#insn-00c2cb10)

~~~json
{
  "source": "00c2cb10",
  "target": "01127ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ab8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb10`](#insn-00c2cb10)

~~~json
{
  "source": "00c2cb10",
  "target": "01127d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127d00",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb14`](#insn-00c2cb14)

~~~json
{
  "source": "00c2cb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb18`](#insn-00c2cb18)

~~~json
{
  "source": "00c2cb18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb28`](#insn-00c2cb28)

~~~json
{
  "source": "00c2cb28",
  "target": "01127ac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ac0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb2c`](#insn-00c2cb2c)

~~~json
{
  "source": "00c2cb2c",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2cb30`](#insn-00c2cb30)

~~~json
{
  "source": "00c2cb30",
  "target": "00c2cb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb34`](#insn-00c2cb34)

~~~json
{
  "source": "00c2cb34",
  "target": "00c2cb6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2cb44`](#insn-00c2cb44)

~~~json
{
  "source": "00c2cb44",
  "target": "01127ac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ac0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb48`](#insn-00c2cb48)

~~~json
{
  "source": "00c2cb48",
  "target": "01127ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ab8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb48`](#insn-00c2cb48)

~~~json
{
  "source": "00c2cb48",
  "target": "01127d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127d00",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb4c`](#insn-00c2cb4c)

~~~json
{
  "source": "00c2cb4c",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2cb50`](#insn-00c2cb50)

~~~json
{
  "source": "00c2cb50",
  "target": "00c2cb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
