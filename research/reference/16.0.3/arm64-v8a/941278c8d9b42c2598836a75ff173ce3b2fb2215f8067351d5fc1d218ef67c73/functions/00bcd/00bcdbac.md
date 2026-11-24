# 00bcdbac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccbb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccbb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-cb07fb265f339b00de924ced4b0594ff)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdbac",
  "name": "_ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea0da8c9284cd3253bf16edc590eca583992d10a9d432b0a3dfb3b7634f49433",
  "source_text_sha256": "ea0da8c9284cd3253bf16edc590eca583992d10a9d432b0a3dfb3b7634f49433",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdbac",
        "00bcdc1b"
      ]
    ],
    "bytes_sha256": "5b494b55486eb0ab0ad1aa822afa7dd28c3633eb465b4487e7e53cfb92a701d6",
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

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 386 bytes

~~~c

void _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011278b0 != 0) {
    if (DAT_011278b8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278b8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278b0);
    DAT_011278b0 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdbac"></a> `00bcdbac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcdbb0"></a> `00bcdbb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdbb4"></a> `00bcdbb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdbb8"></a> `00bcdbb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdbbc"></a> `00bcdbbc` | `d4 2a 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdbc0"></a> `00bcdbc0` | `81 5a 44 f9` | ldr x1,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdbc4"></a> `00bcdbc4` | `41 02 00 b4` | cbz x1,0x00bcdc0c | `CONDITIONAL_JUMP`
<a id="insn-00bcdbc8"></a> `00bcdbc8` | `d5 2a 00 d0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdbcc"></a> `00bcdbcc` | `a8 e2 62 39` | ldrb w8,[x21, #0x8b8] | `FALL_THROUGH`
<a id="insn-00bcdbd0"></a> `00bcdbd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcdbd4"></a> `00bcdbd4` | `c8 00 00 34` | cbz w8,0x00bcdbec | `CONDITIONAL_JUMP`
<a id="insn-00bcdbd8"></a> `00bcdbd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcdbdc"></a> `00bcdbdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdbe0"></a> `00bcdbe0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bcdbe4"></a> `00bcdbe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdbe8"></a> `00bcdbe8` | `bf e2 22 39` | strb wzr,[x21, #0x8b8] | `FALL_THROUGH`
<a id="insn-00bcdbec"></a> `00bcdbec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdbf0"></a> `00bcdbf0` | `04 39 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdbf4"></a> `00bcdbf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcdbf8"></a> `00bcdbf8` | `81 5a 44 f9` | ldr x1,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdbfc"></a> `00bcdbfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdc00"></a> `00bcdc00` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bcdc04"></a> `00bcdc04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdc08"></a> `00bcdc08` | `9f 5a 04 f9` | str xzr,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdc0c"></a> `00bcdc0c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdc10"></a> `00bcdc10` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdc14"></a> `00bcdc14` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcdc18"></a> `00bcdc18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdbac`](#insn-00bcdbac) 範囲 `[['00bcdbac', '00bcdbc7']]`
  - `CONDITIONAL_JUMP` [`00bcdbc4`](#insn-00bcdbc4) → [`00bcdc0c`](#insn-00bcdc0c)
  - `FALL_THROUGH` [`00bcdbc4`](#insn-00bcdbc4) → [`00bcdbc8`](#insn-00bcdbc8)
- ブロック [`00bcdbc8`](#insn-00bcdbc8) 範囲 `[['00bcdbc8', '00bcdbd7']]`
  - `CONDITIONAL_JUMP` [`00bcdbd4`](#insn-00bcdbd4) → [`00bcdbec`](#insn-00bcdbec)
  - `FALL_THROUGH` [`00bcdbd4`](#insn-00bcdbd4) → [`00bcdbd8`](#insn-00bcdbd8)
- ブロック [`00bcdbd8`](#insn-00bcdbd8) 範囲 `[['00bcdbd8', '00bcdbeb']]`
  - `FALL_THROUGH` [`00bcdbe8`](#insn-00bcdbe8) → [`00bcdbec`](#insn-00bcdbec)
- ブロック [`00bcdbec`](#insn-00bcdbec) 範囲 `[['00bcdbec', '00bcdc0b']]`
  - `FALL_THROUGH` [`00bcdc08`](#insn-00bcdc08) → [`00bcdc0c`](#insn-00bcdc0c)
- ブロック [`00bcdc0c`](#insn-00bcdc0c) 範囲 `[['00bcdc0c', '00bcdc1b']]`

## 命令位置別の参照

- [`00bcdbac`](#insn-00bcdbac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbb0`](#insn-00bcdbb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbb4`](#insn-00bcdbb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbc0`](#insn-00bcdbc0) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdbc4`](#insn-00bcdbc4) → [`00bcdc0c`](#insn-00bcdc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbcc`](#insn-00bcdbcc) → `011278b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcdbd4`](#insn-00bcdbd4) → [`00bcdbec`](#insn-00bcdbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbe8`](#insn-00bcdbe8) → `011278b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcdbf0`](#insn-00bcdbf0) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbf8`](#insn-00bcdbf8) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdc08`](#insn-00bcdc08) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdc0c`](#insn-00bcdc0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc10`](#insn-00bcdc10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdbac`](#insn-00bcdbac)

~~~json
{
  "source": "00bcdbac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbb0`](#insn-00bcdbb0)

~~~json
{
  "source": "00bcdbb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbb4`](#insn-00bcdbb4)

~~~json
{
  "source": "00bcdbb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbc0`](#insn-00bcdbc0)

~~~json
{
  "source": "00bcdbc0",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdbc4`](#insn-00bcdbc4)

~~~json
{
  "source": "00bcdbc4",
  "target": "00bcdc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbcc`](#insn-00bcdbcc)

~~~json
{
  "source": "00bcdbcc",
  "target": "011278b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdbd4`](#insn-00bcdbd4)

~~~json
{
  "source": "00bcdbd4",
  "target": "00bcdbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbe8`](#insn-00bcdbe8)

~~~json
{
  "source": "00bcdbe8",
  "target": "011278b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdbf0`](#insn-00bcdbf0)

~~~json
{
  "source": "00bcdbf0",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdbf8`](#insn-00bcdbf8)

~~~json
{
  "source": "00bcdbf8",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdc08`](#insn-00bcdc08)

~~~json
{
  "source": "00bcdc08",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdc0c`](#insn-00bcdc0c)

~~~json
{
  "source": "00bcdc0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc10`](#insn-00bcdc10)

~~~json
{
  "source": "00bcdc10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
