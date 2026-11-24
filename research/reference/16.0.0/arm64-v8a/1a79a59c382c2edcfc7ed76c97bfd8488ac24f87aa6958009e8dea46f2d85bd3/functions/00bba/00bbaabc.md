# 00bbaabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4cd80`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cd80.md) · 移動量 `+0x6dd3c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-01c2f093fad25e1f18712a6c1e75cacd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbaee4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaee4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-170594141238bfbe7ca3816f0c508d18)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaabc",
  "name": "_ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6dc11f8fa20b7cbe578099ef06f22658152c193cd5ead47334cfb2b281900779",
  "source_text_sha256": "6dc11f8fa20b7cbe578099ef06f22658152c193cd5ead47334cfb2b281900779",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaabc",
        "00bbab27"
      ]
    ],
    "bytes_sha256": "9b1ef1a506f0c2edb710e05ccb3dcb6eb7202717505bfab4ada53e83b4c34200",
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

- [00497a08](../00497/00497a08.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)

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
  
  if (DAT_01125f60 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    if (DAT_01125f60 == 0) {
      return true;
    }
  }
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
  cVar1 = FUN_00497a08(uVar2,DAT_01125f98,DAT_01125eb8);
  return cVar1 != '\0';
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaabc"></a> `00bbaabc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbaac0"></a> `00bbaac0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaac4"></a> `00bbaac4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbaac8"></a> `00bbaac8` | `53 2b 00 f0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbaacc"></a> `00bbaacc` | `60 b2 47 f9` | ldr x0,[x19, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbaad0"></a> `00bbaad0` | `20 01 00 b5` | cbnz x0,0x00bbaaf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbaad4"></a> `00bbaad4` | `40 b7 ff 90` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbaad8"></a> `00bbaad8` | `00 20 21 91` | add x0,x0,#0x848 | `FALL_THROUGH`
<a id="insn-00bbaadc"></a> `00bbaadc` | `71 7f 02 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaae0"></a> `00bbaae0` | `a0 b7 ff d0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbaae4"></a> `00bbaae4` | `00 dc 1c 91` | add x0,x0,#0x737 | `FALL_THROUGH`
<a id="insn-00bbaae8"></a> `00bbaae8` | `46 80 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaaec"></a> `00bbaaec` | `60 b2 47 f9` | ldr x0,[x19, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbaaf0"></a> `00bbaaf0` | `80 01 00 b4` | cbz x0,0x00bbab20 | `CONDITIONAL_JUMP`
<a id="insn-00bbaaf4"></a> `00bbaaf4` | `63 80 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaaf8"></a> `00bbaaf8` | `48 2b 00 f0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbaafc"></a> `00bbaafc` | `49 2b 00 f0` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbab00"></a> `00bbab00` | `01 cd 47 f9` | ldr x1,[x8, #0xf98] | `FALL_THROUGH`
<a id="insn-00bbab04"></a> `00bbab04` | `22 5d 47 f9` | ldr x2,[x9, #0xeb8] | `FALL_THROUGH`
<a id="insn-00bbab08"></a> `00bbab08` | `c0 73 e3 97` | bl 0x00497a08 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab0c"></a> `00bbab0c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbab10"></a> `00bbab10` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bbab14"></a> `00bbab14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbab18"></a> `00bbab18` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbab1c"></a> `00bbab1c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbab20"></a> `00bbab20` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbab24"></a> `00bbab24` | `fc ff ff 17` | b 0x00bbab14 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbaabc`](#insn-00bbaabc) 範囲 `[['00bbaabc', '00bbaad3']]`
  - `CONDITIONAL_JUMP` [`00bbaad0`](#insn-00bbaad0) → [`00bbaaf4`](#insn-00bbaaf4)
  - `FALL_THROUGH` [`00bbaad0`](#insn-00bbaad0) → [`00bbaad4`](#insn-00bbaad4)
- ブロック [`00bbaad4`](#insn-00bbaad4) 範囲 `[['00bbaad4', '00bbaaf3']]`
  - `CONDITIONAL_JUMP` [`00bbaaf0`](#insn-00bbaaf0) → [`00bbab20`](#insn-00bbab20)
  - `FALL_THROUGH` [`00bbaaf0`](#insn-00bbaaf0) → [`00bbaaf4`](#insn-00bbaaf4)
- ブロック [`00bbaaf4`](#insn-00bbaaf4) 範囲 `[['00bbaaf4', '00bbab13']]`
  - `FALL_THROUGH` [`00bbab10`](#insn-00bbab10) → [`00bbab14`](#insn-00bbab14)
- ブロック [`00bbab14`](#insn-00bbab14) 範囲 `[['00bbab14', '00bbab1f']]`
- ブロック [`00bbab20`](#insn-00bbab20) 範囲 `[['00bbab20', '00bbab27']]`
  - `UNCONDITIONAL_JUMP` [`00bbab24`](#insn-00bbab24) → [`00bbab14`](#insn-00bbab14)

## 命令位置別の参照

- [`00bbaabc`](#insn-00bbaabc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaac0`](#insn-00bbaac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaacc`](#insn-00bbaacc) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaad0`](#insn-00bbaad0) → [`00bbaaf4`](#insn-00bbaaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaad8`](#insn-00bbaad8) → `002a2848`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbaadc`](#insn-00bbaadc) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbaae4`](#insn-00bbaae4) → `002b0737`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbaae8`](#insn-00bbaae8) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bbaaec`](#insn-00bbaaec) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaaf0`](#insn-00bbaaf0) → [`00bbab20`](#insn-00bbab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaaf4`](#insn-00bbaaf4) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bbab00`](#insn-00bbab00) → `01125f98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbab04`](#insn-00bbab04) → `01125eb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbab08`](#insn-00bbab08) → [`00497a08`](../00497/00497a08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a08` · 推定シンボル `None` · 推定型 `None`
- [`00bbab14`](#insn-00bbab14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab24`](#insn-00bbab24) → [`00bbab14`](#insn-00bbab14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaabc`](#insn-00bbaabc)

~~~json
{
  "source": "00bbaabc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaac0`](#insn-00bbaac0)

~~~json
{
  "source": "00bbaac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaacc`](#insn-00bbaacc)

~~~json
{
  "source": "00bbaacc",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbaad0`](#insn-00bbaad0)

~~~json
{
  "source": "00bbaad0",
  "target": "00bbaaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaad8`](#insn-00bbaad8)

~~~json
{
  "source": "00bbaad8",
  "target": "002a2848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2848",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2848",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbaadc`](#insn-00bbaadc)

~~~json
{
  "source": "00bbaadc",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaae4`](#insn-00bbaae4)

~~~json
{
  "source": "00bbaae4",
  "target": "002b0737",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0737",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0737",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbaae8`](#insn-00bbaae8)

~~~json
{
  "source": "00bbaae8",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaaec`](#insn-00bbaaec)

~~~json
{
  "source": "00bbaaec",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbaaf0`](#insn-00bbaaf0)

~~~json
{
  "source": "00bbaaf0",
  "target": "00bbab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaaf4`](#insn-00bbaaf4)

~~~json
{
  "source": "00bbaaf4",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab00`](#insn-00bbab00)

~~~json
{
  "source": "00bbab00",
  "target": "01125f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbab04`](#insn-00bbab04)

~~~json
{
  "source": "00bbab04",
  "target": "01125eb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125eb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbab08`](#insn-00bbab08)

~~~json
{
  "source": "00bbab08",
  "target": "00497a08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab14`](#insn-00bbab14)

~~~json
{
  "source": "00bbab14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab24`](#insn-00bbab24)

~~~json
{
  "source": "00bbab24",
  "target": "00bbab14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
