# 00bccb1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc6f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc6f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-ff846be4bd572ad3eb11cb0a0d9b59a3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccbb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccbb8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-6843d3a05a28c490c93fd379d3356331)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccb1c",
  "name": "_ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f85bb97ffd9868033fcc3d54220bc664ccc7e1bcfc6cb8f21fa0b642429667bb",
  "source_text_sha256": "f85bb97ffd9868033fcc3d54220bc664ccc7e1bcfc6cb8f21fa0b642429667bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccb1c",
        "00bccb8b"
      ]
    ],
    "bytes_sha256": "e1e3b6c8629e1efff9ec8c92d022ab1e58893f5611b199add7ef637bab6137f3",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 386 bytes

~~~c

void _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011267f0 != 0) {
    if (DAT_011267f8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011267f8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011267f0);
    DAT_011267f0 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccb1c"></a> `00bccb1c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bccb20"></a> `00bccb20` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb24"></a> `00bccb24` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccb28"></a> `00bccb28` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bccb2c"></a> `00bccb2c` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccb30"></a> `00bccb30` | `81 fa 43 f9` | ldr x1,[x20, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bccb34"></a> `00bccb34` | `41 02 00 b4` | cbz x1,0x00bccb7c | `CONDITIONAL_JUMP`
<a id="insn-00bccb38"></a> `00bccb38` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccb3c"></a> `00bccb3c` | `a8 e2 5f 39` | ldrb w8,[x21, #0x7f8] | `FALL_THROUGH`
<a id="insn-00bccb40"></a> `00bccb40` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccb44"></a> `00bccb44` | `c8 00 00 34` | cbz w8,0x00bccb5c | `CONDITIONAL_JUMP`
<a id="insn-00bccb48"></a> `00bccb48` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bccb4c"></a> `00bccb4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccb50"></a> `00bccb50` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bccb54"></a> `00bccb54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccb58"></a> `00bccb58` | `bf e2 1f 39` | strb wzr,[x21, #0x7f8] | `FALL_THROUGH`
<a id="insn-00bccb5c"></a> `00bccb5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccb60"></a> `00bccb60` | `00 39 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bccb64"></a> `00bccb64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bccb68"></a> `00bccb68` | `81 fa 43 f9` | ldr x1,[x20, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bccb6c"></a> `00bccb6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccb70"></a> `00bccb70` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bccb74"></a> `00bccb74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccb78"></a> `00bccb78` | `9f fa 03 f9` | str xzr,[x20, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bccb7c"></a> `00bccb7c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccb80"></a> `00bccb80` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb84"></a> `00bccb84` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bccb88"></a> `00bccb88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccb1c`](#insn-00bccb1c) 範囲 `[['00bccb1c', '00bccb37']]`
  - `CONDITIONAL_JUMP` [`00bccb34`](#insn-00bccb34) → [`00bccb7c`](#insn-00bccb7c)
  - `FALL_THROUGH` [`00bccb34`](#insn-00bccb34) → [`00bccb38`](#insn-00bccb38)
- ブロック [`00bccb38`](#insn-00bccb38) 範囲 `[['00bccb38', '00bccb47']]`
  - `CONDITIONAL_JUMP` [`00bccb44`](#insn-00bccb44) → [`00bccb5c`](#insn-00bccb5c)
  - `FALL_THROUGH` [`00bccb44`](#insn-00bccb44) → [`00bccb48`](#insn-00bccb48)
- ブロック [`00bccb48`](#insn-00bccb48) 範囲 `[['00bccb48', '00bccb5b']]`
  - `FALL_THROUGH` [`00bccb58`](#insn-00bccb58) → [`00bccb5c`](#insn-00bccb5c)
- ブロック [`00bccb5c`](#insn-00bccb5c) 範囲 `[['00bccb5c', '00bccb7b']]`
  - `FALL_THROUGH` [`00bccb78`](#insn-00bccb78) → [`00bccb7c`](#insn-00bccb7c)
- ブロック [`00bccb7c`](#insn-00bccb7c) 範囲 `[['00bccb7c', '00bccb8b']]`

## 命令位置別の参照

- [`00bccb1c`](#insn-00bccb1c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb20`](#insn-00bccb20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb24`](#insn-00bccb24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb30`](#insn-00bccb30) → `011267f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb34`](#insn-00bccb34) → [`00bccb7c`](#insn-00bccb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb3c`](#insn-00bccb3c) → `011267f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccb44`](#insn-00bccb44) → [`00bccb5c`](#insn-00bccb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb58`](#insn-00bccb58) → `011267f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccb60`](#insn-00bccb60) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bccb68`](#insn-00bccb68) → `011267f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb78`](#insn-00bccb78) → `011267f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb7c`](#insn-00bccb7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb80`](#insn-00bccb80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccb1c`](#insn-00bccb1c)

~~~json
{
  "source": "00bccb1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb20`](#insn-00bccb20)

~~~json
{
  "source": "00bccb20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb24`](#insn-00bccb24)

~~~json
{
  "source": "00bccb24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb30`](#insn-00bccb30)

~~~json
{
  "source": "00bccb30",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb34`](#insn-00bccb34)

~~~json
{
  "source": "00bccb34",
  "target": "00bccb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb3c`](#insn-00bccb3c)

~~~json
{
  "source": "00bccb3c",
  "target": "011267f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb44`](#insn-00bccb44)

~~~json
{
  "source": "00bccb44",
  "target": "00bccb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb58`](#insn-00bccb58)

~~~json
{
  "source": "00bccb58",
  "target": "011267f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb60`](#insn-00bccb60)

~~~json
{
  "source": "00bccb60",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccb68`](#insn-00bccb68)

~~~json
{
  "source": "00bccb68",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb78`](#insn-00bccb78)

~~~json
{
  "source": "00bccb78",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb7c`](#insn-00bccb7c)

~~~json
{
  "source": "00bccb7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb80`](#insn-00bccb80)

~~~json
{
  "source": "00bccb80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
