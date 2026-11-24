# 00b6dfdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6df98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0074.md#compare-b9bd3151979249fe9d7c92ca8579b74f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd4dc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd4dc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-ee2286f4e7ab713beac57664b046a1f4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6dfdc",
  "name": "_ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "329f406b9b8c23df7f02b610d49a97e84db7e72033dae4aa7f5ef2f6c55f44a2",
  "source_text_sha256": "329f406b9b8c23df7f02b610d49a97e84db7e72033dae4aa7f5ef2f6c55f44a2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6dfdc",
        "00b6e047"
      ]
    ],
    "bytes_sha256": "522aad0b451ea3ac6fda5b33956a8358d1e4f976d32755122a4eef08a0e12961",
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

- [00bde0e0](../00bde/00bde0e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 483 bytes

~~~c

bool _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_010a1b00 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a1af8,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_010a1b00 = iVar2 == 0;
    bVar1 = (bool)DAT_010a1b00;
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
<a id="insn-00b6dfdc"></a> `00b6dfdc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6dfe0"></a> `00b6dfe0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6dfe4"></a> `00b6dfe4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6dfe8"></a> `00b6dfe8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6dfec"></a> `00b6dfec` | `b5 29 00 90` | adrp x21,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6dff0"></a> `00b6dff0` | `a8 02 6c 39` | ldrb w8,[x21, #0xb00] | `FALL_THROUGH`
<a id="insn-00b6dff4"></a> `00b6dff4` | `68 00 00 34` | cbz w8,0x00b6e000 | `CONDITIONAL_JUMP`
<a id="insn-00b6dff8"></a> `00b6dff8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b6dffc"></a> `00b6dffc` | `0f 00 00 14` | b 0x00b6e038 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6e000"></a> `00b6e000` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6e004"></a> `00b6e004` | `89 29 00 f0` | adrp x9,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6e008"></a> `00b6e008` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00b6e00c"></a> `00b6e00c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00b6e010"></a> `00b6e010` | `21 7d 45 f9` | ldr x1,[x9, #0xaf8] | `FALL_THROUGH`
<a id="insn-00b6e014"></a> `00b6e014` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00b6e018"></a> `00b6e018` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6e01c"></a> `00b6e01c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6e020"></a> `00b6e020` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b6e024"></a> `00b6e024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6e028"></a> `00b6e028` | `2e c0 01 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6e02c"></a> `00b6e02c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00b6e030"></a> `00b6e030` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00b6e034"></a> `00b6e034` | `a0 02 2c 39` | strb w0,[x21, #0xb00] | `FALL_THROUGH`
<a id="insn-00b6e038"></a> `00b6e038` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6e03c"></a> `00b6e03c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6e040"></a> `00b6e040` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6e044"></a> `00b6e044` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6dfdc`](#insn-00b6dfdc) 範囲 `[['00b6dfdc', '00b6dff7']]`
  - `CONDITIONAL_JUMP` [`00b6dff4`](#insn-00b6dff4) → [`00b6e000`](#insn-00b6e000)
  - `FALL_THROUGH` [`00b6dff4`](#insn-00b6dff4) → [`00b6dff8`](#insn-00b6dff8)
- ブロック [`00b6dff8`](#insn-00b6dff8) 範囲 `[['00b6dff8', '00b6dfff']]`
  - `UNCONDITIONAL_JUMP` [`00b6dffc`](#insn-00b6dffc) → [`00b6e038`](#insn-00b6e038)
- ブロック [`00b6e000`](#insn-00b6e000) 範囲 `[['00b6e000', '00b6e037']]`
  - `FALL_THROUGH` [`00b6e034`](#insn-00b6e034) → [`00b6e038`](#insn-00b6e038)
- ブロック [`00b6e038`](#insn-00b6e038) 範囲 `[['00b6e038', '00b6e047']]`

## 命令位置別の参照

- [`00b6dfdc`](#insn-00b6dfdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dfe0`](#insn-00b6dfe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dfe4`](#insn-00b6dfe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dff0`](#insn-00b6dff0) → `010a1b00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b6dff4`](#insn-00b6dff4) → [`00b6e000`](#insn-00b6e000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dffc`](#insn-00b6dffc) → [`00b6e038`](#insn-00b6e038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6e010`](#insn-00b6e010) → `010a1af8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6e028`](#insn-00b6e028) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00b6e034`](#insn-00b6e034) → `010a1b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b6e038`](#insn-00b6e038) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6e03c`](#insn-00b6e03c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6dfdc`](#insn-00b6dfdc)

~~~json
{
  "source": "00b6dfdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dfe0`](#insn-00b6dfe0)

~~~json
{
  "source": "00b6dfe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dfe4`](#insn-00b6dfe4)

~~~json
{
  "source": "00b6dfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dff0`](#insn-00b6dff0)

~~~json
{
  "source": "00b6dff0",
  "target": "010a1b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1b00",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dff4`](#insn-00b6dff4)

~~~json
{
  "source": "00b6dff4",
  "target": "00b6e000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dffc`](#insn-00b6dffc)

~~~json
{
  "source": "00b6dffc",
  "target": "00b6e038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6e010`](#insn-00b6e010)

~~~json
{
  "source": "00b6e010",
  "target": "010a1af8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1af8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6e028`](#insn-00b6e028)

~~~json
{
  "source": "00b6e028",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6e034`](#insn-00b6e034)

~~~json
{
  "source": "00b6e034",
  "target": "010a1b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1b00",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6e038`](#insn-00b6e038)

~~~json
{
  "source": "00b6e038",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6e03c`](#insn-00b6e03c)

~~~json
{
  "source": "00b6e03c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
