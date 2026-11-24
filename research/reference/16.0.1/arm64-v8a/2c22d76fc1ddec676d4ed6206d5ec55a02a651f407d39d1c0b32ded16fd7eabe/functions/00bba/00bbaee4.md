# 00bbaee4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbaabc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbaabc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-170594141238bfbe7ca3816f0c508d18)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbaf80`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-1beacfd6972405f21dfef01d6239337b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaee4",
  "name": "_ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43432ae0afb702394557486a437feca42f4539493446b7bc29a88be43ba84053",
  "source_text_sha256": "43432ae0afb702394557486a437feca42f4539493446b7bc29a88be43ba84053",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaee4",
        "00bbaf4f"
      ]
    ],
    "bytes_sha256": "b2be817292168963c2ee1777918aabdae0dc1a89bf69b1446852e3e7d6d877bf",
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

## 疑似コード / UTF-8 447 bytes

~~~c

bool _ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv(void)

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
  cVar1 = FUN_00497a48(uVar2,DAT_01126398,DAT_011262b8);
  return cVar1 != '\0';
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaee4"></a> `00bbaee4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbaee8"></a> `00bbaee8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaeec"></a> `00bbaeec` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbaef0"></a> `00bbaef0` | `73 2b 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbaef4"></a> `00bbaef4` | `60 b2 41 f9` | ldr x0,[x19, #0x360] | `FALL_THROUGH`
<a id="insn-00bbaef8"></a> `00bbaef8` | `20 01 00 b5` | cbnz x0,0x00bbaf1c | `CONDITIONAL_JUMP`
<a id="insn-00bbaefc"></a> `00bbaefc` | `40 b7 ff 90` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbaf00"></a> `00bbaf00` | `00 54 24 91` | add x0,x0,#0x915 | `FALL_THROUGH`
<a id="insn-00bbaf04"></a> `00bbaf04` | `67 7f 02 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf08"></a> `00bbaf08` | `a0 b7 ff d0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbaf0c"></a> `00bbaf0c` | `00 dc 1d 91` | add x0,x0,#0x777 | `FALL_THROUGH`
<a id="insn-00bbaf10"></a> `00bbaf10` | `3c 80 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf14"></a> `00bbaf14` | `60 b2 41 f9` | ldr x0,[x19, #0x360] | `FALL_THROUGH`
<a id="insn-00bbaf18"></a> `00bbaf18` | `80 01 00 b4` | cbz x0,0x00bbaf48 | `CONDITIONAL_JUMP`
<a id="insn-00bbaf1c"></a> `00bbaf1c` | `59 80 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf20"></a> `00bbaf20` | `68 2b 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbaf24"></a> `00bbaf24` | `69 2b 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbaf28"></a> `00bbaf28` | `01 cd 41 f9` | ldr x1,[x8, #0x398] | `FALL_THROUGH`
<a id="insn-00bbaf2c"></a> `00bbaf2c` | `22 5d 41 f9` | ldr x2,[x9, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbaf30"></a> `00bbaf30` | `c6 72 e3 97` | bl 0x00497a48 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf34"></a> `00bbaf34` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbaf38"></a> `00bbaf38` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bbaf3c"></a> `00bbaf3c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaf40"></a> `00bbaf40` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbaf44"></a> `00bbaf44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbaf48"></a> `00bbaf48` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbaf4c"></a> `00bbaf4c` | `fc ff ff 17` | b 0x00bbaf3c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbaee4`](#insn-00bbaee4) 範囲 `[['00bbaee4', '00bbaefb']]`
  - `CONDITIONAL_JUMP` [`00bbaef8`](#insn-00bbaef8) → [`00bbaf1c`](#insn-00bbaf1c)
  - `FALL_THROUGH` [`00bbaef8`](#insn-00bbaef8) → [`00bbaefc`](#insn-00bbaefc)
- ブロック [`00bbaefc`](#insn-00bbaefc) 範囲 `[['00bbaefc', '00bbaf1b']]`
  - `CONDITIONAL_JUMP` [`00bbaf18`](#insn-00bbaf18) → [`00bbaf48`](#insn-00bbaf48)
  - `FALL_THROUGH` [`00bbaf18`](#insn-00bbaf18) → [`00bbaf1c`](#insn-00bbaf1c)
- ブロック [`00bbaf1c`](#insn-00bbaf1c) 範囲 `[['00bbaf1c', '00bbaf3b']]`
  - `FALL_THROUGH` [`00bbaf38`](#insn-00bbaf38) → [`00bbaf3c`](#insn-00bbaf3c)
- ブロック [`00bbaf3c`](#insn-00bbaf3c) 範囲 `[['00bbaf3c', '00bbaf47']]`
- ブロック [`00bbaf48`](#insn-00bbaf48) 範囲 `[['00bbaf48', '00bbaf4f']]`
  - `UNCONDITIONAL_JUMP` [`00bbaf4c`](#insn-00bbaf4c) → [`00bbaf3c`](#insn-00bbaf3c)

## 命令位置別の参照

- [`00bbaee4`](#insn-00bbaee4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee8`](#insn-00bbaee8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaef4`](#insn-00bbaef4) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaef8`](#insn-00bbaef8) → [`00bbaf1c`](#insn-00bbaf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf00`](#insn-00bbaf00) → `002a2915`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbaf04`](#insn-00bbaf04) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf0c`](#insn-00bbaf0c) → `002b0777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbaf10`](#insn-00bbaf10) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf14`](#insn-00bbaf14) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaf18`](#insn-00bbaf18) → [`00bbaf48`](#insn-00bbaf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf1c`](#insn-00bbaf1c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf28`](#insn-00bbaf28) → `01126398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaf2c`](#insn-00bbaf2c) → `011262b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaf30`](#insn-00bbaf30) → [`00497a48`](../00497/00497a48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a48` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf3c`](#insn-00bbaf3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf4c`](#insn-00bbaf4c) → [`00bbaf3c`](#insn-00bbaf3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaee4`](#insn-00bbaee4)

~~~json
{
  "source": "00bbaee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaee8`](#insn-00bbaee8)

~~~json
{
  "source": "00bbaee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaef4`](#insn-00bbaef4)

~~~json
{
  "source": "00bbaef4",
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
- 参照命令 [`00bbaef8`](#insn-00bbaef8)

~~~json
{
  "source": "00bbaef8",
  "target": "00bbaf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf00`](#insn-00bbaf00)

~~~json
{
  "source": "00bbaf00",
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
- 参照命令 [`00bbaf04`](#insn-00bbaf04)

~~~json
{
  "source": "00bbaf04",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf0c`](#insn-00bbaf0c)

~~~json
{
  "source": "00bbaf0c",
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
- 参照命令 [`00bbaf10`](#insn-00bbaf10)

~~~json
{
  "source": "00bbaf10",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf14`](#insn-00bbaf14)

~~~json
{
  "source": "00bbaf14",
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
- 参照命令 [`00bbaf18`](#insn-00bbaf18)

~~~json
{
  "source": "00bbaf18",
  "target": "00bbaf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf1c`](#insn-00bbaf1c)

~~~json
{
  "source": "00bbaf1c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf28`](#insn-00bbaf28)

~~~json
{
  "source": "00bbaf28",
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
- 参照命令 [`00bbaf2c`](#insn-00bbaf2c)

~~~json
{
  "source": "00bbaf2c",
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
- 参照命令 [`00bbaf30`](#insn-00bbaf30)

~~~json
{
  "source": "00bbaf30",
  "target": "00497a48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf3c`](#insn-00bbaf3c)

~~~json
{
  "source": "00bbaf3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf4c`](#insn-00bbaf4c)

~~~json
{
  "source": "00bbaf4c",
  "target": "00bbaf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
