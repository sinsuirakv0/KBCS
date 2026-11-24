# 00bb8bdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb87b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-c5a48079724fbf0c43c49c394877e67d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb8c78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-29ab9791eb62cdde3f71d2ca6f5cc460)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb8bdc",
  "name": "_INIT_285",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8249224c0e645bd9b3999a8e5b43d722ba6c34fd3cfee1d93cd2af7a8e107f5",
  "source_text_sha256": "b8249224c0e645bd9b3999a8e5b43d722ba6c34fd3cfee1d93cd2af7a8e107f5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb8bdc",
        "00bb8c4b"
      ]
    ],
    "bytes_sha256": "8b5effd1f624948c47a5b3e26de0275ad3014cdc3bbce6b7c3941afbaedeec89",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e30](../00c57/00c57e30.md)
- [00c5abc0](../00c5a/00c5abc0.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 関連文字列（未確認候補）

~~~text
"messaging"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 434 bytes

~~~c

void _INIT_285(void)

{
                    /* try { // try from 00bb8be0 to 00cb8c57 has its CatchHandler @ 00bb910c */
  DAT_011261e8 = "messaging";
  DAT_011261f0 = FUN_00bb66a4;
  DAT_011261f8 = FUN_00bb66e4;
  DAT_01126200 = 0;
  _ZN8firebase11AppCallback11AddCallbackEPS0_();
  _ZN8firebase5MutexC1ENS0_4ModeE(&DAT_01126208,1);
  __cxa_atexit(PTR__ZN8firebase5MutexD1Ev_00c9b678,&DAT_01126208,&PTR_LOOP_00c62f90);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb8bdc"></a> `00bb8bdc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb8be0"></a> `00bb8be0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8be4"></a> `00bb8be4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bb8be8"></a> `00bb8be8` | `60 2b 00 d0` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bb8bec"></a> `00bb8bec` | `a8 ba ff d0` | adrp x8,0x30e000 | `FALL_THROUGH`
<a id="insn-00bb8bf0"></a> `00bb8bf0` | `e9 ff ff d0` | adrp x9,0xbb6000 | `FALL_THROUGH`
<a id="insn-00bb8bf4"></a> `00bb8bf4` | `ea ff ff d0` | adrp x10,0xbb6000 | `FALL_THROUGH`
<a id="insn-00bb8bf8"></a> `00bb8bf8` | `00 a0 07 91` | add x0,x0,#0x1e8 | `FALL_THROUGH`
<a id="insn-00bb8bfc"></a> `00bb8bfc` | `08 7d 1b 91` | add x8,x8,#0x6df | `FALL_THROUGH`
<a id="insn-00bb8c00"></a> `00bb8c00` | `29 91 1a 91` | add x9,x9,#0x6a4 | `FALL_THROUGH`
<a id="insn-00bb8c04"></a> `00bb8c04` | `4a 91 1b 91` | add x10,x10,#0x6e4 | `FALL_THROUGH`
<a id="insn-00bb8c08"></a> `00bb8c08` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bb8c0c"></a> `00bb8c0c` | `0a 08 00 f9` | str x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8c10"></a> `00bb8c10` | `1f 60 00 39` | strb wzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bb8c14"></a> `00bb8c14` | `eb 87 02 94` | bl 0x00c5abc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8c18"></a> `00bb8c18` | `73 2b 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bb8c1c"></a> `00bb8c1c` | `73 22 08 91` | add x19,x19,#0x208 | `FALL_THROUGH`
<a id="insn-00bb8c20"></a> `00bb8c20` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bb8c24"></a> `00bb8c24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb8c28"></a> `00bb8c28` | `16 88 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8c2c"></a> `00bb8c2c` | `00 07 00 f0` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bb8c30"></a> `00bb8c30` | `00 3c 43 f9` | ldr x0,[x0, #0x678] | `FALL_THROUGH`
<a id="insn-00bb8c34"></a> `00bb8c34` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8c38"></a> `00bb8c38` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bb8c3c"></a> `00bb8c3c` | `a2 1a 55 10` | adr x2,0xc62f90 | `FALL_THROUGH`
<a id="insn-00bb8c40"></a> `00bb8c40` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bb8c44"></a> `00bb8c44` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb8c48"></a> `00bb8c48` | `7a 7c 02 14` | b 0x00c57e30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb8bdc`](#insn-00bb8bdc) 範囲 `[['00bb8bdc', '00bb8bdf']]`
  - `FALL_THROUGH` [`00bb8bdc`](#insn-00bb8bdc) → [`00bb8be0`](#insn-00bb8be0)
- ブロック [`00bb8be0`](#insn-00bb8be0) 範囲 `[['00bb8be0', '00bb8c4b']]`

## 命令位置別の参照

- [`00bb8bdc`](#insn-00bb8bdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8be0`](#insn-00bb8be0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8bf8`](#insn-00bb8bf8) → `011261e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8c08`](#insn-00bb8c08) → `011261e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8c08`](#insn-00bb8c08) → `0030e6df`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bb8c08`](#insn-00bb8c08) → `011261f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8c08`](#insn-00bb8c08) → [`00bb66a4`](../00bb6/00bb66a4.md) · `DATA` · `ANALYSIS` · 関数 `00bb66a4` · 推定シンボル `None` · 推定型 `None`
- [`00bb8c0c`](#insn-00bb8c0c) → `011261f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8c0c`](#insn-00bb8c0c) → [`00bb66e4`](../00bb6/00bb66e4.md) · `DATA` · `ANALYSIS` · 関数 `00bb66e4` · 推定シンボル `None` · 推定型 `None`
- [`00bb8c10`](#insn-00bb8c10) → `01126200`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8c14`](#insn-00bb8c14) → [`00c5abc0`](../00c5a/00c5abc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abc0` · 推定シンボル `None` · 推定型 `None`
- [`00bb8c24`](#insn-00bb8c24) → `01126208`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8c28`](#insn-00bb8c28) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bb8c30`](#insn-00bb8c30) → `00c9b678`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb8c30`](#insn-00bb8c30) → [`00b65510`](../00b65/00b65510.md) · `PARAM` · `ANALYSIS` · 関数 `00b65510` · 推定シンボル `_ZN8firebase5MutexD1Ev` · 推定型 `None`
- [`00bb8c34`](#insn-00bb8c34) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8c3c`](#insn-00bb8c3c) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb8c40`](#insn-00bb8c40) → `01126208`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8c48`](#insn-00bb8c48) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb8bdc`](#insn-00bb8bdc)

~~~json
{
  "source": "00bb8bdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8be0`](#insn-00bb8be0)

~~~json
{
  "source": "00bb8be0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8bf8`](#insn-00bb8bf8)

~~~json
{
  "source": "00bb8bf8",
  "target": "011261e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8c08`](#insn-00bb8c08)

~~~json
{
  "source": "00bb8c08",
  "target": "011261e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8c08`](#insn-00bb8c08)

~~~json
{
  "source": "00bb8c08",
  "target": "0030e6df",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e6df",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "6d6573736167696e6700",
  "capture_start": "0030e6df",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb8c08`](#insn-00bb8c08)

~~~json
{
  "source": "00bb8c08",
  "target": "011261f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8c08`](#insn-00bb8c08)

~~~json
{
  "source": "00bb8c08",
  "target": "00bb66a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8c0c`](#insn-00bb8c0c)

~~~json
{
  "source": "00bb8c0c",
  "target": "011261f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8c0c`](#insn-00bb8c0c)

~~~json
{
  "source": "00bb8c0c",
  "target": "00bb66e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8c10`](#insn-00bb8c10)

~~~json
{
  "source": "00bb8c10",
  "target": "01126200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126200",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8c14`](#insn-00bb8c14)

~~~json
{
  "source": "00bb8c14",
  "target": "00c5abc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8c24`](#insn-00bb8c24)

~~~json
{
  "source": "00bb8c24",
  "target": "01126208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8c28`](#insn-00bb8c28)

~~~json
{
  "source": "00bb8c28",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8c30`](#insn-00bb8c30)

~~~json
{
  "source": "00bb8c30",
  "target": "00c9b678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b678",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb8c30`](#insn-00bb8c30)

~~~json
{
  "source": "00bb8c30",
  "target": "00b65510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8c34`](#insn-00bb8c34)

~~~json
{
  "source": "00bb8c34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8c3c`](#insn-00bb8c3c)

~~~json
{
  "source": "00bb8c3c",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb8c40`](#insn-00bb8c40)

~~~json
{
  "source": "00bb8c40",
  "target": "01126208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8c48`](#insn-00bb8c48)

~~~json
{
  "source": "00bb8c48",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
