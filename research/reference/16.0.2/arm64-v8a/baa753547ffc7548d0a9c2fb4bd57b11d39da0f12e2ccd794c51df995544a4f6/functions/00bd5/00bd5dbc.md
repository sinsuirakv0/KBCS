# 00bd5dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd5d20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5d20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0083.md#compare-e82339183564d50f9931927a3cb0422b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd6db0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd6/00bd6db0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-7099bdf4115dbd6fa84b3486b31385ba)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd5dbc",
  "name": "_ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e09abc1f6546c77e96b1972e47d79522dfae1940c7168ab8baa23a1e6ab6446",
  "source_text_sha256": "6e09abc1f6546c77e96b1972e47d79522dfae1940c7168ab8baa23a1e6ab6446",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd5dbc",
        "00bd5e2b"
      ]
    ],
    "bytes_sha256": "7efc0bbe01c2bb649c2038b47d4c0b875bb33ceb4502acb03a242125852d2b5b",
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

## 疑似コード / UTF-8 385 bytes

~~~c

void _ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126bc8 != 0) {
    if (DAT_01126bd0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126bd0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126bc8);
    DAT_01126bc8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd5dbc"></a> `00bd5dbc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd5dc0"></a> `00bd5dc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5dc4"></a> `00bd5dc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd5dc8"></a> `00bd5dc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd5dcc"></a> `00bd5dcc` | `94 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd5dd0"></a> `00bd5dd0` | `81 e6 45 f9` | ldr x1,[x20, #0xbc8] | `FALL_THROUGH`
<a id="insn-00bd5dd4"></a> `00bd5dd4` | `41 02 00 b4` | cbz x1,0x00bd5e1c | `CONDITIONAL_JUMP`
<a id="insn-00bd5dd8"></a> `00bd5dd8` | `95 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd5ddc"></a> `00bd5ddc` | `a8 42 6f 39` | ldrb w8,[x21, #0xbd0] | `FALL_THROUGH`
<a id="insn-00bd5de0"></a> `00bd5de0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd5de4"></a> `00bd5de4` | `c8 00 00 34` | cbz w8,0x00bd5dfc | `CONDITIONAL_JUMP`
<a id="insn-00bd5de8"></a> `00bd5de8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd5dec"></a> `00bd5dec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd5df0"></a> `00bd5df0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd5df4"></a> `00bd5df4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd5df8"></a> `00bd5df8` | `bf 42 2f 39` | strb wzr,[x21, #0xbd0] | `FALL_THROUGH`
<a id="insn-00bd5dfc"></a> `00bd5dfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd5e00"></a> `00bd5e00` | `8c 14 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5e04"></a> `00bd5e04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd5e08"></a> `00bd5e08` | `81 e6 45 f9` | ldr x1,[x20, #0xbc8] | `FALL_THROUGH`
<a id="insn-00bd5e0c"></a> `00bd5e0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd5e10"></a> `00bd5e10` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd5e14"></a> `00bd5e14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd5e18"></a> `00bd5e18` | `9f e6 05 f9` | str xzr,[x20, #0xbc8] | `FALL_THROUGH`
<a id="insn-00bd5e1c"></a> `00bd5e1c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd5e20"></a> `00bd5e20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5e24"></a> `00bd5e24` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd5e28"></a> `00bd5e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd5dbc`](#insn-00bd5dbc) 範囲 `[['00bd5dbc', '00bd5dd7']]`
  - `CONDITIONAL_JUMP` [`00bd5dd4`](#insn-00bd5dd4) → [`00bd5e1c`](#insn-00bd5e1c)
  - `FALL_THROUGH` [`00bd5dd4`](#insn-00bd5dd4) → [`00bd5dd8`](#insn-00bd5dd8)
- ブロック [`00bd5dd8`](#insn-00bd5dd8) 範囲 `[['00bd5dd8', '00bd5de7']]`
  - `CONDITIONAL_JUMP` [`00bd5de4`](#insn-00bd5de4) → [`00bd5dfc`](#insn-00bd5dfc)
  - `FALL_THROUGH` [`00bd5de4`](#insn-00bd5de4) → [`00bd5de8`](#insn-00bd5de8)
- ブロック [`00bd5de8`](#insn-00bd5de8) 範囲 `[['00bd5de8', '00bd5dfb']]`
  - `FALL_THROUGH` [`00bd5df8`](#insn-00bd5df8) → [`00bd5dfc`](#insn-00bd5dfc)
- ブロック [`00bd5dfc`](#insn-00bd5dfc) 範囲 `[['00bd5dfc', '00bd5e1b']]`
  - `FALL_THROUGH` [`00bd5e18`](#insn-00bd5e18) → [`00bd5e1c`](#insn-00bd5e1c)
- ブロック [`00bd5e1c`](#insn-00bd5e1c) 範囲 `[['00bd5e1c', '00bd5e2b']]`

## 命令位置別の参照

- [`00bd5dbc`](#insn-00bd5dbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dc0`](#insn-00bd5dc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dc4`](#insn-00bd5dc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dd0`](#insn-00bd5dd0) → `01126bc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd5dd4`](#insn-00bd5dd4) → [`00bd5e1c`](#insn-00bd5e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5ddc`](#insn-00bd5ddc) → `01126bd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd5de4`](#insn-00bd5de4) → [`00bd5dfc`](#insn-00bd5dfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5df8`](#insn-00bd5df8) → `01126bd0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd5e00`](#insn-00bd5e00) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd5e08`](#insn-00bd5e08) → `01126bc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd5e18`](#insn-00bd5e18) → `01126bc8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd5e1c`](#insn-00bd5e1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5e20`](#insn-00bd5e20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd5dbc`](#insn-00bd5dbc)

~~~json
{
  "source": "00bd5dbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dc0`](#insn-00bd5dc0)

~~~json
{
  "source": "00bd5dc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dc4`](#insn-00bd5dc4)

~~~json
{
  "source": "00bd5dc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dd0`](#insn-00bd5dd0)

~~~json
{
  "source": "00bd5dd0",
  "target": "01126bc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126bc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5dd4`](#insn-00bd5dd4)

~~~json
{
  "source": "00bd5dd4",
  "target": "00bd5e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5ddc`](#insn-00bd5ddc)

~~~json
{
  "source": "00bd5ddc",
  "target": "01126bd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126bd0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5de4`](#insn-00bd5de4)

~~~json
{
  "source": "00bd5de4",
  "target": "00bd5dfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5df8`](#insn-00bd5df8)

~~~json
{
  "source": "00bd5df8",
  "target": "01126bd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126bd0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5e00`](#insn-00bd5e00)

~~~json
{
  "source": "00bd5e00",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5e08`](#insn-00bd5e08)

~~~json
{
  "source": "00bd5e08",
  "target": "01126bc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126bc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5e18`](#insn-00bd5e18)

~~~json
{
  "source": "00bd5e18",
  "target": "01126bc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126bc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5e1c`](#insn-00bd5e1c)

~~~json
{
  "source": "00bd5e1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5e20`](#insn-00bd5e20)

~~~json
{
  "source": "00bd5e20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
