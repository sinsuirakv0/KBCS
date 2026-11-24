# 00bddfbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdcfc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcfc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-ef732619f02b16b789a9e00a792e9c02)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfbc",
  "name": "_ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43b821af1af99eb52146465a3be034f8d714106c70fa6d916676a10e9d6cf493",
  "source_text_sha256": "43b821af1af99eb52146465a3be034f8d714106c70fa6d916676a10e9d6cf493",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfbc",
        "00bde027"
      ]
    ],
    "bytes_sha256": "33c0245b3cf6df27d4beaef57110b045c0531eb8cb5ad2125f59c1739970f5c3",
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

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 487 bytes

~~~c

bool _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01127dc8 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01127dc0,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01127dc8 = iVar2 == 0;
    bVar1 = (bool)DAT_01127dc8;
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
<a id="insn-00bddfbc"></a> `00bddfbc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bddfc0"></a> `00bddfc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddfc4"></a> `00bddfc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddfc8"></a> `00bddfc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddfcc"></a> `00bddfcc` | `55 2a 00 d0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bddfd0"></a> `00bddfd0` | `a8 22 77 39` | ldrb w8,[x21, #0xdc8] | `FALL_THROUGH`
<a id="insn-00bddfd4"></a> `00bddfd4` | `68 00 00 34` | cbz w8,0x00bddfe0 | `CONDITIONAL_JUMP`
<a id="insn-00bddfd8"></a> `00bddfd8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bddfdc"></a> `00bddfdc` | `0f 00 00 14` | b 0x00bde018 | `UNCONDITIONAL_JUMP`
<a id="insn-00bddfe0"></a> `00bddfe0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bddfe4"></a> `00bddfe4` | `49 2a 00 d0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bddfe8"></a> `00bddfe8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bddfec"></a> `00bddfec` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bddff0"></a> `00bddff0` | `21 e1 46 f9` | ldr x1,[x9, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bddff4"></a> `00bddff4` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bddff8"></a> `00bddff8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddffc"></a> `00bddffc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bde000"></a> `00bde000` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bde004"></a> `00bde004` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde008"></a> `00bde008` | `fe f7 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bde00c"></a> `00bde00c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bde010"></a> `00bde010` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bde014"></a> `00bde014` | `a0 22 37 39` | strb w0,[x21, #0xdc8] | `FALL_THROUGH`
<a id="insn-00bde018"></a> `00bde018` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde01c"></a> `00bde01c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde020"></a> `00bde020` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde024"></a> `00bde024` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfbc`](#insn-00bddfbc) 範囲 `[['00bddfbc', '00bddfd7']]`
  - `CONDITIONAL_JUMP` [`00bddfd4`](#insn-00bddfd4) → [`00bddfe0`](#insn-00bddfe0)
  - `FALL_THROUGH` [`00bddfd4`](#insn-00bddfd4) → [`00bddfd8`](#insn-00bddfd8)
- ブロック [`00bddfd8`](#insn-00bddfd8) 範囲 `[['00bddfd8', '00bddfdf']]`
  - `UNCONDITIONAL_JUMP` [`00bddfdc`](#insn-00bddfdc) → [`00bde018`](#insn-00bde018)
- ブロック [`00bddfe0`](#insn-00bddfe0) 範囲 `[['00bddfe0', '00bde017']]`
  - `FALL_THROUGH` [`00bde014`](#insn-00bde014) → [`00bde018`](#insn-00bde018)
- ブロック [`00bde018`](#insn-00bde018) 範囲 `[['00bde018', '00bde027']]`

## 命令位置別の参照

- [`00bddfbc`](#insn-00bddfbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddfc0`](#insn-00bddfc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddfc4`](#insn-00bddfc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddfd0`](#insn-00bddfd0) → `01127dc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddfd4`](#insn-00bddfd4) → [`00bddfe0`](#insn-00bddfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddfdc`](#insn-00bddfdc) → [`00bde018`](#insn-00bde018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddff0`](#insn-00bddff0) → `01127dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde008`](#insn-00bde008) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bde014`](#insn-00bde014) → `01127dc8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bde018`](#insn-00bde018) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde01c`](#insn-00bde01c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfbc`](#insn-00bddfbc)

~~~json
{
  "source": "00bddfbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddfc0`](#insn-00bddfc0)

~~~json
{
  "source": "00bddfc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddfc4`](#insn-00bddfc4)

~~~json
{
  "source": "00bddfc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddfd0`](#insn-00bddfd0)

~~~json
{
  "source": "00bddfd0",
  "target": "01127dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddfd4`](#insn-00bddfd4)

~~~json
{
  "source": "00bddfd4",
  "target": "00bddfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddfdc`](#insn-00bddfdc)

~~~json
{
  "source": "00bddfdc",
  "target": "00bde018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddff0`](#insn-00bddff0)

~~~json
{
  "source": "00bddff0",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde008`](#insn-00bde008)

~~~json
{
  "source": "00bde008",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde014`](#insn-00bde014)

~~~json
{
  "source": "00bde014",
  "target": "01127dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde018`](#insn-00bde018)

~~~json
{
  "source": "00bde018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde01c`](#insn-00bde01c)

~~~json
{
  "source": "00bde01c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
