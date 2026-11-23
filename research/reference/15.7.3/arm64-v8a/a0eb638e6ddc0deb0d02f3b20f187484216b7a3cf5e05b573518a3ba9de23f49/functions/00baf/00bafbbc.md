# 00bafbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bafaf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafaf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-3443b2096fbdb04f33987723463bd0bb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bafc00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-ab7cf24a33bec817e1fd2f1e4b4c39ee)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafbbc",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0a70d9c0e8d33346251f1a55172e67db7ae130e612c7f1d5a1fef0c5f8093ef",
  "source_text_sha256": "b0a70d9c0e8d33346251f1a55172e67db7ae130e612c7f1d5a1fef0c5f8093ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafbbc",
        "00bafc27"
      ]
    ],
    "bytes_sha256": "f4e73ae84f2ae3b6a857abe5fca76325e48065c40c31c78b39e9a424a81518b9",
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

- [00bafc28](../00baf/00bafc28.md)
- [00bdafb0](../00bda/00bdafb0.md)
- [00bdafd0](../00bda/00bdafd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 404 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv(void)

{
  int iVar1;
  
  if (((DAT_010a2b68 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_010a2b68), iVar1 != 0)) {
    FUN_00bafc28();
    DAT_010a2b60 = &DAT_010a2c60;
    __cxa_guard_release(&DAT_010a2b68);
                    /* try { // try from 00bafc24 to 00cafc73 has its CatchHandler @ 00bb0dc8 */
  }
  return DAT_010a2b60;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafbbc"></a> `00bafbbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bafbc0"></a> `00bafbc0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bafbc4"></a> `00bafbc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bafbc8"></a> `00bafbc8` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafbcc"></a> `00bafbcc` | `08 a1 2d 91` | add x8,x8,#0xb68 | `FALL_THROUGH`
<a id="insn-00bafbd0"></a> `00bafbd0` | `09 fd df 08` | ldarb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bafbd4"></a> `00bafbd4` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafbd8"></a> `00bafbd8` | `a9 00 00 36` | tbz w9,#0x0,0x00bafbec | `CONDITIONAL_JUMP`
<a id="insn-00bafbdc"></a> `00bafbdc` | `00 b1 45 f9` | ldr x0,[x8, #0xb60] | `FALL_THROUGH`
<a id="insn-00bafbe0"></a> `00bafbe0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bafbe4"></a> `00bafbe4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bafbe8"></a> `00bafbe8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafbec"></a> `00bafbec` | `80 27 00 f0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafbf0"></a> `00bafbf0` | `00 a0 2d 91` | add x0,x0,#0xb68 | `FALL_THROUGH`
<a id="insn-00bafbf4"></a> `00bafbf4` | `ef ac 00 94` | bl 0x00bdafb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bafbf8"></a> `00bafbf8` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafbfc"></a> `00bafbfc` | `00 ff ff 34` | cbz w0,0x00bafbdc | `CONDITIONAL_JUMP`
<a id="insn-00bafc00"></a> `00bafc00` | `0a 00 00 94` | bl 0x00bafc28 | `UNCONDITIONAL_CALL`
<a id="insn-00bafc04"></a> `00bafc04` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafc08"></a> `00bafc08` | `29 81 31 91` | add x9,x9,#0xc60 | `FALL_THROUGH`
<a id="insn-00bafc0c"></a> `00bafc0c` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafc10"></a> `00bafc10` | `80 27 00 f0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafc14"></a> `00bafc14` | `00 a0 2d 91` | add x0,x0,#0xb68 | `FALL_THROUGH`
<a id="insn-00bafc18"></a> `00bafc18` | `09 b1 05 f9` | str x9,[x8, #0xb60] | `FALL_THROUGH`
<a id="insn-00bafc1c"></a> `00bafc1c` | `ed ac 00 94` | bl 0x00bdafd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bafc20"></a> `00bafc20` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafc24"></a> `00bafc24` | `ee ff ff 17` | b 0x00bafbdc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bafbbc`](#insn-00bafbbc) 範囲 `[['00bafbbc', '00bafbdb']]`
  - `CONDITIONAL_JUMP` [`00bafbd8`](#insn-00bafbd8) → [`00bafbec`](#insn-00bafbec)
  - `FALL_THROUGH` [`00bafbd8`](#insn-00bafbd8) → [`00bafbdc`](#insn-00bafbdc)
- ブロック [`00bafbdc`](#insn-00bafbdc) 範囲 `[['00bafbdc', '00bafbeb']]`
- ブロック [`00bafbec`](#insn-00bafbec) 範囲 `[['00bafbec', '00bafbff']]`
  - `CONDITIONAL_JUMP` [`00bafbfc`](#insn-00bafbfc) → [`00bafbdc`](#insn-00bafbdc)
  - `FALL_THROUGH` [`00bafbfc`](#insn-00bafbfc) → [`00bafc00`](#insn-00bafc00)
- ブロック [`00bafc00`](#insn-00bafc00) 範囲 `[['00bafc00', '00bafc23']]`
  - `FALL_THROUGH` [`00bafc20`](#insn-00bafc20) → [`00bafc24`](#insn-00bafc24)
- ブロック [`00bafc24`](#insn-00bafc24) 範囲 `[['00bafc24', '00bafc27']]`
  - `UNCONDITIONAL_JUMP` [`00bafc24`](#insn-00bafc24) → [`00bafbdc`](#insn-00bafbdc)

## 命令位置別の参照

- [`00bafbc0`](#insn-00bafbc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbd0`](#insn-00bafbd0) → `010a2b68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafbd8`](#insn-00bafbd8) → [`00bafbec`](#insn-00bafbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbdc`](#insn-00bafbdc) → `010a2b60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafbdc`](#insn-00bafbdc) → `010a2c60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafbe0`](#insn-00bafbe0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbf0`](#insn-00bafbf0) → `010a2b68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafbf4`](#insn-00bafbf4) → [`00bdafb0`](../00bda/00bdafb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafb0` · 推定シンボル `None` · 推定型 `None`
- [`00bafbfc`](#insn-00bafbfc) → [`00bafbdc`](#insn-00bafbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc00`](#insn-00bafc00) → [`00bafc28`](00bafc28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bafc28` · 推定シンボル `None` · 推定型 `None`
- [`00bafc14`](#insn-00bafc14) → `010a2b68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafc18`](#insn-00bafc18) → `010a2b60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafc18`](#insn-00bafc18) → `010a2c60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafc1c`](#insn-00bafc1c) → [`00bdafd0`](../00bda/00bdafd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafd0` · 推定シンボル `None` · 推定型 `None`
- [`00bafc24`](#insn-00bafc24) → [`00bafbdc`](#insn-00bafbdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafbc0`](#insn-00bafbc0)

~~~json
{
  "source": "00bafbc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbd0`](#insn-00bafbd0)

~~~json
{
  "source": "00bafbd0",
  "target": "010a2b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2b68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafbd8`](#insn-00bafbd8)

~~~json
{
  "source": "00bafbd8",
  "target": "00bafbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbdc`](#insn-00bafbdc)

~~~json
{
  "source": "00bafbdc",
  "target": "010a2b60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2b60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafbdc`](#insn-00bafbdc)

~~~json
{
  "source": "00bafbdc",
  "target": "010a2c60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2c60",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafbe0`](#insn-00bafbe0)

~~~json
{
  "source": "00bafbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbf0`](#insn-00bafbf0)

~~~json
{
  "source": "00bafbf0",
  "target": "010a2b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2b68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafbf4`](#insn-00bafbf4)

~~~json
{
  "source": "00bafbf4",
  "target": "00bdafb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafbfc`](#insn-00bafbfc)

~~~json
{
  "source": "00bafbfc",
  "target": "00bafbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc00`](#insn-00bafc00)

~~~json
{
  "source": "00bafc00",
  "target": "00bafc28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafc14`](#insn-00bafc14)

~~~json
{
  "source": "00bafc14",
  "target": "010a2b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2b68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafc18`](#insn-00bafc18)

~~~json
{
  "source": "00bafc18",
  "target": "010a2b60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2b60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafc18`](#insn-00bafc18)

~~~json
{
  "source": "00bafc18",
  "target": "010a2c60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2c60",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafc1c`](#insn-00bafc1c)

~~~json
{
  "source": "00bafc1c",
  "target": "00bdafd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafc24`](#insn-00bafc24)

~~~json
{
  "source": "00bafc24",
  "target": "00bafbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
