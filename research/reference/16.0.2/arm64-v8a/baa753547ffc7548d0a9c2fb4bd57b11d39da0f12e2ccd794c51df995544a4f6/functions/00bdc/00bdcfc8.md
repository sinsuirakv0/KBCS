# 00bdcfc8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdcf2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf2c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-fe08098407ec6299e071fd17e4ec8427)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bddfbc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddfbc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-ef732619f02b16b789a9e00a792e9c02)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfc8",
  "name": "_ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f72c9caf1397654ee871b127c62fb144abaea16526ce45e0031d69390d90e045",
  "source_text_sha256": "f72c9caf1397654ee871b127c62fb144abaea16526ce45e0031d69390d90e045",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfc8",
        "00bdd033"
      ]
    ],
    "bytes_sha256": "4a99cd814923f927b2d487983e1a13abda6e0f189fdf73f5edf0915130c298ef",
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

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 487 bytes

~~~c

bool _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126e08 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126e00,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126e08 = iVar2 == 0;
    bVar1 = (bool)DAT_01126e08;
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
<a id="insn-00bdcfc8"></a> `00bdcfc8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdcfcc"></a> `00bdcfcc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcfd0"></a> `00bdcfd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcfd4"></a> `00bdcfd4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcfd8"></a> `00bdcfd8` | `55 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcfdc"></a> `00bdcfdc` | `a8 22 78 39` | ldrb w8,[x21, #0xe08] | `FALL_THROUGH`
<a id="insn-00bdcfe0"></a> `00bdcfe0` | `68 00 00 34` | cbz w8,0x00bdcfec | `CONDITIONAL_JUMP`
<a id="insn-00bdcfe4"></a> `00bdcfe4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdcfe8"></a> `00bdcfe8` | `0f 00 00 14` | b 0x00bdd024 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcfec"></a> `00bdcfec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdcff0"></a> `00bdcff0` | `49 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcff4"></a> `00bdcff4` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bdcff8"></a> `00bdcff8` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bdcffc"></a> `00bdcffc` | `21 01 47 f9` | ldr x1,[x9, #0xe00] | `FALL_THROUGH`
<a id="insn-00bdd000"></a> `00bdd000` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bdd004"></a> `00bdd004` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd008"></a> `00bdd008` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdd00c"></a> `00bdd00c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bdd010"></a> `00bdd010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd014"></a> `00bdd014` | `07 f8 01 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd018"></a> `00bdd018` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bdd01c"></a> `00bdd01c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bdd020"></a> `00bdd020` | `a0 22 38 39` | strb w0,[x21, #0xe08] | `FALL_THROUGH`
<a id="insn-00bdd024"></a> `00bdd024` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd028"></a> `00bdd028` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd02c"></a> `00bdd02c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdd030"></a> `00bdd030` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfc8`](#insn-00bdcfc8) 範囲 `[['00bdcfc8', '00bdcfe3']]`
  - `CONDITIONAL_JUMP` [`00bdcfe0`](#insn-00bdcfe0) → [`00bdcfec`](#insn-00bdcfec)
  - `FALL_THROUGH` [`00bdcfe0`](#insn-00bdcfe0) → [`00bdcfe4`](#insn-00bdcfe4)
- ブロック [`00bdcfe4`](#insn-00bdcfe4) 範囲 `[['00bdcfe4', '00bdcfeb']]`
  - `UNCONDITIONAL_JUMP` [`00bdcfe8`](#insn-00bdcfe8) → [`00bdd024`](#insn-00bdd024)
- ブロック [`00bdcfec`](#insn-00bdcfec) 範囲 `[['00bdcfec', '00bdd023']]`
  - `FALL_THROUGH` [`00bdd020`](#insn-00bdd020) → [`00bdd024`](#insn-00bdd024)
- ブロック [`00bdd024`](#insn-00bdd024) 範囲 `[['00bdd024', '00bdd033']]`

## 命令位置別の参照

- [`00bdcfc8`](#insn-00bdcfc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcfcc`](#insn-00bdcfcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcfd0`](#insn-00bdcfd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcfdc`](#insn-00bdcfdc) → `01126e08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdcfe0`](#insn-00bdcfe0) → [`00bdcfec`](#insn-00bdcfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcfe8`](#insn-00bdcfe8) → [`00bdd024`](#insn-00bdd024) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcffc`](#insn-00bdcffc) → `01126e00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd014`](#insn-00bdd014) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bdd020`](#insn-00bdd020) → `01126e08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdd024`](#insn-00bdd024) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd028`](#insn-00bdd028) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfc8`](#insn-00bdcfc8)

~~~json
{
  "source": "00bdcfc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcfcc`](#insn-00bdcfcc)

~~~json
{
  "source": "00bdcfcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcfd0`](#insn-00bdcfd0)

~~~json
{
  "source": "00bdcfd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcfdc`](#insn-00bdcfdc)

~~~json
{
  "source": "00bdcfdc",
  "target": "01126e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcfe0`](#insn-00bdcfe0)

~~~json
{
  "source": "00bdcfe0",
  "target": "00bdcfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcfe8`](#insn-00bdcfe8)

~~~json
{
  "source": "00bdcfe8",
  "target": "00bdd024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcffc`](#insn-00bdcffc)

~~~json
{
  "source": "00bdcffc",
  "target": "01126e00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd014`](#insn-00bdd014)

~~~json
{
  "source": "00bdd014",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd020`](#insn-00bdd020)

~~~json
{
  "source": "00bdd020",
  "target": "01126e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd024`](#insn-00bdd024)

~~~json
{
  "source": "00bdd024",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd028`](#insn-00bdd028)

~~~json
{
  "source": "00bdd028",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
