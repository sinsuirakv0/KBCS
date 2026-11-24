# 00bbbfd4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbbbac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbbac.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-d70111b06c4db4bf025fb6efb495eee8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbc070`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc070.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-491d46596a42e90500355fd281db9eb3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbfd4",
  "name": "_ZN8firebase9messaging27IsRegistrationOnInitEnabledEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9901f2158a0858d99b22820e4bee67bcdfcb9593c2c205c8a1fd40aa35baef45",
  "source_text_sha256": "9901f2158a0858d99b22820e4bee67bcdfcb9593c2c205c8a1fd40aa35baef45",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbfd4",
        "00bbc03f"
      ]
    ],
    "bytes_sha256": "004085af86a71f85dd6b59648bb26c295aefeb7bc16980678f53597ead227785",
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

- [00497a48](../00497/00497a48.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 539 bytes

~~~c

bool _ZN8firebase9messaging27IsRegistrationOnInitEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01126360 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    if (DAT_01126360 == 0) {
      return true;
    }
  }
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00bbc020 to 00cbc02b has its CatchHandler @ 00bbc7b8 */
  cVar1 = FUN_00497a48(uVar2,DAT_01126398,DAT_011262b8);
  return cVar1 != '\0';
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbfd4"></a> `00bbbfd4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbbfd8"></a> `00bbbfd8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbfdc"></a> `00bbbfdc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbfe0"></a> `00bbbfe0` | `53 2b 00 f0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbfe4"></a> `00bbbfe4` | `60 b2 41 f9` | ldr x0,[x19, #0x360] | `FALL_THROUGH`
<a id="insn-00bbbfe8"></a> `00bbbfe8` | `20 01 00 b5` | cbnz x0,0x00bbc00c | `CONDITIONAL_JUMP`
<a id="insn-00bbbfec"></a> `00bbbfec` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbbff0"></a> `00bbbff0` | `00 54 24 91` | add x0,x0,#0x915 | `FALL_THROUGH`
<a id="insn-00bbbff4"></a> `00bbbff4` | `2b 7b 02 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbff8"></a> `00bbbff8` | `a0 b7 ff b0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbbffc"></a> `00bbbffc` | `00 dc 1d 91` | add x0,x0,#0x777 | `FALL_THROUGH`
<a id="insn-00bbc000"></a> `00bbc000` | `00 7c 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc004"></a> `00bbc004` | `60 b2 41 f9` | ldr x0,[x19, #0x360] | `FALL_THROUGH`
<a id="insn-00bbc008"></a> `00bbc008` | `80 01 00 b4` | cbz x0,0x00bbc038 | `CONDITIONAL_JUMP`
<a id="insn-00bbc00c"></a> `00bbc00c` | `1d 7c 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc010"></a> `00bbc010` | `48 2b 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbc014"></a> `00bbc014` | `49 2b 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbc018"></a> `00bbc018` | `01 cd 41 f9` | ldr x1,[x8, #0x398] | `FALL_THROUGH`
<a id="insn-00bbc01c"></a> `00bbc01c` | `22 5d 41 f9` | ldr x2,[x9, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbc020"></a> `00bbc020` | `8a 6e e3 97` | bl 0x00497a48 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc024"></a> `00bbc024` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbc028"></a> `00bbc028` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bbc02c"></a> `00bbc02c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc030"></a> `00bbc030` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbc034"></a> `00bbc034` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbc038"></a> `00bbc038` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc03c"></a> `00bbc03c` | `fc ff ff 17` | b 0x00bbc02c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbbfd4`](#insn-00bbbfd4) 範囲 `[['00bbbfd4', '00bbbfeb']]`
  - `CONDITIONAL_JUMP` [`00bbbfe8`](#insn-00bbbfe8) → [`00bbc00c`](#insn-00bbc00c)
  - `FALL_THROUGH` [`00bbbfe8`](#insn-00bbbfe8) → [`00bbbfec`](#insn-00bbbfec)
- ブロック [`00bbbfec`](#insn-00bbbfec) 範囲 `[['00bbbfec', '00bbc00b']]`
  - `CONDITIONAL_JUMP` [`00bbc008`](#insn-00bbc008) → [`00bbc038`](#insn-00bbc038)
  - `FALL_THROUGH` [`00bbc008`](#insn-00bbc008) → [`00bbc00c`](#insn-00bbc00c)
- ブロック [`00bbc00c`](#insn-00bbc00c) 範囲 `[['00bbc00c', '00bbc01f']]`
  - `FALL_THROUGH` [`00bbc01c`](#insn-00bbc01c) → [`00bbc020`](#insn-00bbc020)
- ブロック [`00bbc020`](#insn-00bbc020) 範囲 `[['00bbc020', '00bbc02b']]`
  - `FALL_THROUGH` [`00bbc028`](#insn-00bbc028) → [`00bbc02c`](#insn-00bbc02c)
- ブロック [`00bbc02c`](#insn-00bbc02c) 範囲 `[['00bbc02c', '00bbc037']]`
- ブロック [`00bbc038`](#insn-00bbc038) 範囲 `[['00bbc038', '00bbc03f']]`
  - `UNCONDITIONAL_JUMP` [`00bbc03c`](#insn-00bbc03c) → [`00bbc02c`](#insn-00bbc02c)

## 命令位置別の参照

- [`00bbbfd4`](#insn-00bbbfd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfd8`](#insn-00bbbfd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfe4`](#insn-00bbbfe4) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbfe8`](#insn-00bbbfe8) → [`00bbc00c`](#insn-00bbc00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbff0`](#insn-00bbbff0) → `002a2915`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbff4`](#insn-00bbbff4) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbffc`](#insn-00bbbffc) → `002b0777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbc000`](#insn-00bbc000) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbc004`](#insn-00bbc004) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc008`](#insn-00bbc008) → [`00bbc038`](#insn-00bbc038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc00c`](#insn-00bbc00c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bbc018`](#insn-00bbc018) → `01126398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc01c`](#insn-00bbc01c) → `011262b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc020`](#insn-00bbc020) → [`00497a48`](../00497/00497a48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a48` · 推定シンボル `None` · 推定型 `None`
- [`00bbc02c`](#insn-00bbc02c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc03c`](#insn-00bbc03c) → [`00bbc02c`](#insn-00bbc02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbfd4`](#insn-00bbbfd4)

~~~json
{
  "source": "00bbbfd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfd8`](#insn-00bbbfd8)

~~~json
{
  "source": "00bbbfd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfe4`](#insn-00bbbfe4)

~~~json
{
  "source": "00bbbfe4",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbfe8`](#insn-00bbbfe8)

~~~json
{
  "source": "00bbbfe8",
  "target": "00bbc00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbff0`](#insn-00bbbff0)

~~~json
{
  "source": "00bbbff0",
  "target": "002a2915",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2915",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2915",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbff4`](#insn-00bbbff4)

~~~json
{
  "source": "00bbbff4",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbffc`](#insn-00bbbffc)

~~~json
{
  "source": "00bbbffc",
  "target": "002b0777",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0777",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0777",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbc000`](#insn-00bbc000)

~~~json
{
  "source": "00bbc000",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc004`](#insn-00bbc004)

~~~json
{
  "source": "00bbc004",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbc008`](#insn-00bbc008)

~~~json
{
  "source": "00bbc008",
  "target": "00bbc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc00c`](#insn-00bbc00c)

~~~json
{
  "source": "00bbc00c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc018`](#insn-00bbc018)

~~~json
{
  "source": "00bbc018",
  "target": "01126398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126398",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbc01c`](#insn-00bbc01c)

~~~json
{
  "source": "00bbc01c",
  "target": "011262b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbc020`](#insn-00bbc020)

~~~json
{
  "source": "00bbc020",
  "target": "00497a48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc02c`](#insn-00bbc02c)

~~~json
{
  "source": "00bbc02c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc03c`](#insn-00bbc03c)

~~~json
{
  "source": "00bbc03c",
  "target": "00bbc02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
