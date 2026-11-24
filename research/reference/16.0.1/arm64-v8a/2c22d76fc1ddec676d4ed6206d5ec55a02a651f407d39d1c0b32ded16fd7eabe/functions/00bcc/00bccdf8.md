# 00bccdf8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc9d0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc9d0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-8c56080276f183e22f787facff72cdbd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcce94`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce94.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-932ca42b82f354624283d182c2605cc0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccdf8",
  "name": "_ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edb82a29a046a645b86f55859364419ce8cd7a26505e3c7ade4f2891fd2adc2f",
  "source_text_sha256": "edb82a29a046a645b86f55859364419ce8cd7a26505e3c7ade4f2891fd2adc2f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccdf8",
        "00bcce63"
      ]
    ],
    "bytes_sha256": "9f3273b4692e5585d3f2b521c97fa96a360c9ecae25ef1a4824fc26490e3ca2e",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 497 bytes

~~~c

bool _ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126820 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126818,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126820 = iVar2 == 0;
    bVar1 = (bool)DAT_01126820;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccdf8"></a> `00bccdf8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bccdfc"></a> `00bccdfc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcce00"></a> `00bcce00` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcce04"></a> `00bcce04` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcce08"></a> `00bcce08` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcce0c"></a> `00bcce0c` | `a8 82 60 39` | ldrb w8,[x21, #0x820] | `FALL_THROUGH`
<a id="insn-00bcce10"></a> `00bcce10` | `68 00 00 34` | cbz w8,0x00bcce1c | `CONDITIONAL_JUMP`
<a id="insn-00bcce14"></a> `00bcce14` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bcce18"></a> `00bcce18` | `0f 00 00 14` | b 0x00bcce54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcce1c"></a> `00bcce1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcce20"></a> `00bcce20` | `c9 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcce24"></a> `00bcce24` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bcce28"></a> `00bcce28` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bcce2c"></a> `00bcce2c` | `21 0d 44 f9` | ldr x1,[x9, #0x818] | `FALL_THROUGH`
<a id="insn-00bcce30"></a> `00bcce30` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bcce34"></a> `00bcce34` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcce38"></a> `00bcce38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcce3c"></a> `00bcce3c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcce40"></a> `00bcce40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcce44"></a> `00bcce44` | `47 38 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcce48"></a> `00bcce48` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bcce4c"></a> `00bcce4c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bcce50"></a> `00bcce50` | `a0 82 20 39` | strb w0,[x21, #0x820] | `FALL_THROUGH`
<a id="insn-00bcce54"></a> `00bcce54` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcce58"></a> `00bcce58` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcce5c"></a> `00bcce5c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcce60"></a> `00bcce60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccdf8`](#insn-00bccdf8) 範囲 `[['00bccdf8', '00bcce13']]`
  - `CONDITIONAL_JUMP` [`00bcce10`](#insn-00bcce10) → [`00bcce1c`](#insn-00bcce1c)
  - `FALL_THROUGH` [`00bcce10`](#insn-00bcce10) → [`00bcce14`](#insn-00bcce14)
- ブロック [`00bcce14`](#insn-00bcce14) 範囲 `[['00bcce14', '00bcce1b']]`
  - `UNCONDITIONAL_JUMP` [`00bcce18`](#insn-00bcce18) → [`00bcce54`](#insn-00bcce54)
- ブロック [`00bcce1c`](#insn-00bcce1c) 範囲 `[['00bcce1c', '00bcce53']]`
  - `FALL_THROUGH` [`00bcce50`](#insn-00bcce50) → [`00bcce54`](#insn-00bcce54)
- ブロック [`00bcce54`](#insn-00bcce54) 範囲 `[['00bcce54', '00bcce63']]`

## 命令位置別の参照

- [`00bccdf8`](#insn-00bccdf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccdfc`](#insn-00bccdfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce00`](#insn-00bcce00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce0c`](#insn-00bcce0c) → `01126820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcce10`](#insn-00bcce10) → [`00bcce1c`](#insn-00bcce1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce18`](#insn-00bcce18) → [`00bcce54`](#insn-00bcce54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce2c`](#insn-00bcce2c) → `01126818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcce44`](#insn-00bcce44) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bcce50`](#insn-00bcce50) → `01126820`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcce54`](#insn-00bcce54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce58`](#insn-00bcce58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccdf8`](#insn-00bccdf8)

~~~json
{
  "source": "00bccdf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccdfc`](#insn-00bccdfc)

~~~json
{
  "source": "00bccdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce00`](#insn-00bcce00)

~~~json
{
  "source": "00bcce00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce0c`](#insn-00bcce0c)

~~~json
{
  "source": "00bcce0c",
  "target": "01126820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126820",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcce10`](#insn-00bcce10)

~~~json
{
  "source": "00bcce10",
  "target": "00bcce1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce18`](#insn-00bcce18)

~~~json
{
  "source": "00bcce18",
  "target": "00bcce54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce2c`](#insn-00bcce2c)

~~~json
{
  "source": "00bcce2c",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcce44`](#insn-00bcce44)

~~~json
{
  "source": "00bcce44",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcce50`](#insn-00bcce50)

~~~json
{
  "source": "00bcce50",
  "target": "01126820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126820",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcce54`](#insn-00bcce54)

~~~json
{
  "source": "00bcce54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce58`](#insn-00bcce58)

~~~json
{
  "source": "00bcce58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
