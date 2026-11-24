# 00bccbb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccb1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb1c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-6843d3a05a28c490c93fd379d3356331)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcdbac`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcdbac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-cb07fb265f339b00de924ced4b0594ff)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccbb8",
  "name": "_ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "337d113a295d567bbc23e8f60d6900aa02ac669f0c349e69d8b076ec4e9d438d",
  "source_text_sha256": "337d113a295d567bbc23e8f60d6900aa02ac669f0c349e69d8b076ec4e9d438d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccbb8",
        "00bccc27"
      ]
    ],
    "bytes_sha256": "d1476499263f9ebdb1ea076ce66e2a81fb5b7af332c3d64d660129d6f9439704",
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

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 386 bytes

~~~c

void _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011268f0 != 0) {
    if (DAT_011268f8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011268f8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011268f0);
    DAT_011268f0 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccbb8"></a> `00bccbb8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bccbbc"></a> `00bccbbc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccbc0"></a> `00bccbc0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccbc4"></a> `00bccbc4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bccbc8"></a> `00bccbc8` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccbcc"></a> `00bccbcc` | `81 7a 44 f9` | ldr x1,[x20, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bccbd0"></a> `00bccbd0` | `41 02 00 b4` | cbz x1,0x00bccc18 | `CONDITIONAL_JUMP`
<a id="insn-00bccbd4"></a> `00bccbd4` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccbd8"></a> `00bccbd8` | `a8 e2 63 39` | ldrb w8,[x21, #0x8f8] | `FALL_THROUGH`
<a id="insn-00bccbdc"></a> `00bccbdc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccbe0"></a> `00bccbe0` | `c8 00 00 34` | cbz w8,0x00bccbf8 | `CONDITIONAL_JUMP`
<a id="insn-00bccbe4"></a> `00bccbe4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bccbe8"></a> `00bccbe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccbec"></a> `00bccbec` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bccbf0"></a> `00bccbf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccbf4"></a> `00bccbf4` | `bf e2 23 39` | strb wzr,[x21, #0x8f8] | `FALL_THROUGH`
<a id="insn-00bccbf8"></a> `00bccbf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccbfc"></a> `00bccbfc` | `0d 39 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bccc00"></a> `00bccc00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bccc04"></a> `00bccc04` | `81 7a 44 f9` | ldr x1,[x20, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bccc08"></a> `00bccc08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccc0c"></a> `00bccc0c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bccc10"></a> `00bccc10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccc14"></a> `00bccc14` | `9f 7a 04 f9` | str xzr,[x20, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bccc18"></a> `00bccc18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccc1c"></a> `00bccc1c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccc20"></a> `00bccc20` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bccc24"></a> `00bccc24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccbb8`](#insn-00bccbb8) 範囲 `[['00bccbb8', '00bccbd3']]`
  - `CONDITIONAL_JUMP` [`00bccbd0`](#insn-00bccbd0) → [`00bccc18`](#insn-00bccc18)
  - `FALL_THROUGH` [`00bccbd0`](#insn-00bccbd0) → [`00bccbd4`](#insn-00bccbd4)
- ブロック [`00bccbd4`](#insn-00bccbd4) 範囲 `[['00bccbd4', '00bccbe3']]`
  - `CONDITIONAL_JUMP` [`00bccbe0`](#insn-00bccbe0) → [`00bccbf8`](#insn-00bccbf8)
  - `FALL_THROUGH` [`00bccbe0`](#insn-00bccbe0) → [`00bccbe4`](#insn-00bccbe4)
- ブロック [`00bccbe4`](#insn-00bccbe4) 範囲 `[['00bccbe4', '00bccbf7']]`
  - `FALL_THROUGH` [`00bccbf4`](#insn-00bccbf4) → [`00bccbf8`](#insn-00bccbf8)
- ブロック [`00bccbf8`](#insn-00bccbf8) 範囲 `[['00bccbf8', '00bccc17']]`
  - `FALL_THROUGH` [`00bccc14`](#insn-00bccc14) → [`00bccc18`](#insn-00bccc18)
- ブロック [`00bccc18`](#insn-00bccc18) 範囲 `[['00bccc18', '00bccc27']]`

## 命令位置別の参照

- [`00bccbb8`](#insn-00bccbb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbbc`](#insn-00bccbbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbc0`](#insn-00bccbc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbcc`](#insn-00bccbcc) → `011268f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccbd0`](#insn-00bccbd0) → [`00bccc18`](#insn-00bccc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbd8`](#insn-00bccbd8) → `011268f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccbe0`](#insn-00bccbe0) → [`00bccbf8`](#insn-00bccbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbf4`](#insn-00bccbf4) → `011268f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccbfc`](#insn-00bccbfc) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bccc04`](#insn-00bccc04) → `011268f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccc14`](#insn-00bccc14) → `011268f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccc18`](#insn-00bccc18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccc1c`](#insn-00bccc1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccbb8`](#insn-00bccbb8)

~~~json
{
  "source": "00bccbb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbbc`](#insn-00bccbbc)

~~~json
{
  "source": "00bccbbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbc0`](#insn-00bccbc0)

~~~json
{
  "source": "00bccbc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbcc`](#insn-00bccbcc)

~~~json
{
  "source": "00bccbcc",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccbd0`](#insn-00bccbd0)

~~~json
{
  "source": "00bccbd0",
  "target": "00bccc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbd8`](#insn-00bccbd8)

~~~json
{
  "source": "00bccbd8",
  "target": "011268f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccbe0`](#insn-00bccbe0)

~~~json
{
  "source": "00bccbe0",
  "target": "00bccbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbf4`](#insn-00bccbf4)

~~~json
{
  "source": "00bccbf4",
  "target": "011268f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccbfc`](#insn-00bccbfc)

~~~json
{
  "source": "00bccbfc",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccc04`](#insn-00bccc04)

~~~json
{
  "source": "00bccc04",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccc14`](#insn-00bccc14)

~~~json
{
  "source": "00bccc14",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccc18`](#insn-00bccc18)

~~~json
{
  "source": "00bccc18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccc1c`](#insn-00bccc1c)

~~~json
{
  "source": "00bccc1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
