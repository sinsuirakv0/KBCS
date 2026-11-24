# 00bdceb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6d9b8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d9b8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-e40ec9ed4f8bd65df113d2b0950d51ea)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd2e0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd2e0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-cd9b5320f3245e9f7f93b8a1f9ebdff4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdceb8",
  "name": "_ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cac88589b26842049f81f8fe659552261781168481dd05ad72e9b91397e6470b",
  "source_text_sha256": "cac88589b26842049f81f8fe659552261781168481dd05ad72e9b91397e6470b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdceb8",
        "00bdcf27"
      ]
    ],
    "bytes_sha256": "174ee46db9629103326d795b14b175a44decbadaea88961f4e31a612e82d562c",
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

- [00c5ab60](../00c5a/00c5ab60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 378 bytes

~~~c

void _ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126920 != 0) {
    if (DAT_01126928 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126928 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126920);
    DAT_01126920 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdceb8"></a> `00bdceb8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdcebc"></a> `00bdcebc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcec0"></a> `00bdcec0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcec4"></a> `00bdcec4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcec8"></a> `00bdcec8` | `54 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcecc"></a> `00bdcecc` | `81 92 44 f9` | ldr x1,[x20, #0x920] | `FALL_THROUGH`
<a id="insn-00bdced0"></a> `00bdced0` | `41 02 00 b4` | cbz x1,0x00bdcf18 | `CONDITIONAL_JUMP`
<a id="insn-00bdced4"></a> `00bdced4` | `55 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdced8"></a> `00bdced8` | `a8 a2 64 39` | ldrb w8,[x21, #0x928] | `FALL_THROUGH`
<a id="insn-00bdcedc"></a> `00bdcedc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcee0"></a> `00bdcee0` | `c8 00 00 34` | cbz w8,0x00bdcef8 | `CONDITIONAL_JUMP`
<a id="insn-00bdcee4"></a> `00bdcee4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcee8"></a> `00bdcee8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdceec"></a> `00bdceec` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bdcef0"></a> `00bdcef0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcef4"></a> `00bdcef4` | `bf a2 24 39` | strb wzr,[x21, #0x928] | `FALL_THROUGH`
<a id="insn-00bdcef8"></a> `00bdcef8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcefc"></a> `00bdcefc` | `19 f7 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcf00"></a> `00bdcf00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcf04"></a> `00bdcf04` | `81 92 44 f9` | ldr x1,[x20, #0x920] | `FALL_THROUGH`
<a id="insn-00bdcf08"></a> `00bdcf08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcf0c"></a> `00bdcf0c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdcf10"></a> `00bdcf10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcf14"></a> `00bdcf14` | `9f 92 04 f9` | str xzr,[x20, #0x920] | `FALL_THROUGH`
<a id="insn-00bdcf18"></a> `00bdcf18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcf1c"></a> `00bdcf1c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcf20"></a> `00bdcf20` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdcf24"></a> `00bdcf24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdceb8`](#insn-00bdceb8) 範囲 `[['00bdceb8', '00bdced3']]`
  - `CONDITIONAL_JUMP` [`00bdced0`](#insn-00bdced0) → [`00bdcf18`](#insn-00bdcf18)
  - `FALL_THROUGH` [`00bdced0`](#insn-00bdced0) → [`00bdced4`](#insn-00bdced4)
- ブロック [`00bdced4`](#insn-00bdced4) 範囲 `[['00bdced4', '00bdcee3']]`
  - `CONDITIONAL_JUMP` [`00bdcee0`](#insn-00bdcee0) → [`00bdcef8`](#insn-00bdcef8)
  - `FALL_THROUGH` [`00bdcee0`](#insn-00bdcee0) → [`00bdcee4`](#insn-00bdcee4)
- ブロック [`00bdcee4`](#insn-00bdcee4) 範囲 `[['00bdcee4', '00bdcef7']]`
  - `FALL_THROUGH` [`00bdcef4`](#insn-00bdcef4) → [`00bdcef8`](#insn-00bdcef8)
- ブロック [`00bdcef8`](#insn-00bdcef8) 範囲 `[['00bdcef8', '00bdcf17']]`
  - `FALL_THROUGH` [`00bdcf14`](#insn-00bdcf14) → [`00bdcf18`](#insn-00bdcf18)
- ブロック [`00bdcf18`](#insn-00bdcf18) 範囲 `[['00bdcf18', '00bdcf27']]`

## 命令位置別の参照

- [`00bdceb8`](#insn-00bdceb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcebc`](#insn-00bdcebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcec0`](#insn-00bdcec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcecc`](#insn-00bdcecc) → `01126920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdced0`](#insn-00bdced0) → [`00bdcf18`](#insn-00bdcf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdced8`](#insn-00bdced8) → `01126928`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdcee0`](#insn-00bdcee0) → [`00bdcef8`](#insn-00bdcef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcef4`](#insn-00bdcef4) → `01126928`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdcefc`](#insn-00bdcefc) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf04`](#insn-00bdcf04) → `01126920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcf14`](#insn-00bdcf14) → `01126920`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcf18`](#insn-00bdcf18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf1c`](#insn-00bdcf1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdceb8`](#insn-00bdceb8)

~~~json
{
  "source": "00bdceb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcebc`](#insn-00bdcebc)

~~~json
{
  "source": "00bdcebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcec0`](#insn-00bdcec0)

~~~json
{
  "source": "00bdcec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcecc`](#insn-00bdcecc)

~~~json
{
  "source": "00bdcecc",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdced0`](#insn-00bdced0)

~~~json
{
  "source": "00bdced0",
  "target": "00bdcf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdced8`](#insn-00bdced8)

~~~json
{
  "source": "00bdced8",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcee0`](#insn-00bdcee0)

~~~json
{
  "source": "00bdcee0",
  "target": "00bdcef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcef4`](#insn-00bdcef4)

~~~json
{
  "source": "00bdcef4",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcefc`](#insn-00bdcefc)

~~~json
{
  "source": "00bdcefc",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcf04`](#insn-00bdcf04)

~~~json
{
  "source": "00bdcf04",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcf14`](#insn-00bdcf14)

~~~json
{
  "source": "00bdcf14",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcf18`](#insn-00bdcf18)

~~~json
{
  "source": "00bdcf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf1c`](#insn-00bdcf1c)

~~~json
{
  "source": "00bdcf1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
