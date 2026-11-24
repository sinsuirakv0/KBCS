# 00bd5ffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd5bd4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5bd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-0b1ebd9310a91e6b29b6f7639ed574c1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd6098`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6098.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0083.md#compare-a6ec60e2675e86cbe30f0930c8feca77)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd5ffc",
  "name": "_ZN8firebase4auth13playgamescred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a9d0c5f178c421b430a6dd9cdaaf719eaf5e7b451093776403e5915d6d147f0a",
  "source_text_sha256": "a9d0c5f178c421b430a6dd9cdaaf719eaf5e7b451093776403e5915d6d147f0a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd5ffc",
        "00bd6067"
      ]
    ],
    "bytes_sha256": "61135dc47e9ad9ccab939466ee4873b1f393f8c6401f94ff90e4389fea9e6aa7",
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

## 疑似コード / UTF-8 489 bytes

~~~c

bool _ZN8firebase4auth13playgamescred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126af0 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126ae8,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126af0 = iVar2 == 0;
    bVar1 = (bool)DAT_01126af0;
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
<a id="insn-00bd5ffc"></a> `00bd5ffc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd6000"></a> `00bd6000` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6004"></a> `00bd6004` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd6008"></a> `00bd6008` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd600c"></a> `00bd600c` | `95 2a 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd6010"></a> `00bd6010` | `a8 c2 6b 39` | ldrb w8,[x21, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bd6014"></a> `00bd6014` | `68 00 00 34` | cbz w8,0x00bd6020 | `CONDITIONAL_JUMP`
<a id="insn-00bd6018"></a> `00bd6018` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bd601c"></a> `00bd601c` | `0f 00 00 14` | b 0x00bd6058 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd6020"></a> `00bd6020` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd6024"></a> `00bd6024` | `89 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd6028"></a> `00bd6028` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bd602c"></a> `00bd602c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bd6030"></a> `00bd6030` | `21 75 45 f9` | ldr x1,[x9, #0xae8] | `FALL_THROUGH`
<a id="insn-00bd6034"></a> `00bd6034` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bd6038"></a> `00bd6038` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd603c"></a> `00bd603c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd6040"></a> `00bd6040` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bd6044"></a> `00bd6044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd6048"></a> `00bd6048` | `c6 13 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd604c"></a> `00bd604c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bd6050"></a> `00bd6050` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bd6054"></a> `00bd6054` | `a0 c2 2b 39` | strb w0,[x21, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bd6058"></a> `00bd6058` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd605c"></a> `00bd605c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6060"></a> `00bd6060` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd6064"></a> `00bd6064` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd5ffc`](#insn-00bd5ffc) 範囲 `[['00bd5ffc', '00bd6017']]`
  - `CONDITIONAL_JUMP` [`00bd6014`](#insn-00bd6014) → [`00bd6020`](#insn-00bd6020)
  - `FALL_THROUGH` [`00bd6014`](#insn-00bd6014) → [`00bd6018`](#insn-00bd6018)
- ブロック [`00bd6018`](#insn-00bd6018) 範囲 `[['00bd6018', '00bd601f']]`
  - `UNCONDITIONAL_JUMP` [`00bd601c`](#insn-00bd601c) → [`00bd6058`](#insn-00bd6058)
- ブロック [`00bd6020`](#insn-00bd6020) 範囲 `[['00bd6020', '00bd6057']]`
  - `FALL_THROUGH` [`00bd6054`](#insn-00bd6054) → [`00bd6058`](#insn-00bd6058)
- ブロック [`00bd6058`](#insn-00bd6058) 範囲 `[['00bd6058', '00bd6067']]`

## 命令位置別の参照

- [`00bd5ffc`](#insn-00bd5ffc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6000`](#insn-00bd6000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6004`](#insn-00bd6004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6010`](#insn-00bd6010) → `01126af0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd6014`](#insn-00bd6014) → [`00bd6020`](#insn-00bd6020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd601c`](#insn-00bd601c) → [`00bd6058`](#insn-00bd6058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6030`](#insn-00bd6030) → `01126ae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6048`](#insn-00bd6048) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bd6054`](#insn-00bd6054) → `01126af0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd6058`](#insn-00bd6058) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd605c`](#insn-00bd605c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd5ffc`](#insn-00bd5ffc)

~~~json
{
  "source": "00bd5ffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6000`](#insn-00bd6000)

~~~json
{
  "source": "00bd6000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6004`](#insn-00bd6004)

~~~json
{
  "source": "00bd6004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6010`](#insn-00bd6010)

~~~json
{
  "source": "00bd6010",
  "target": "01126af0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126af0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6014`](#insn-00bd6014)

~~~json
{
  "source": "00bd6014",
  "target": "00bd6020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd601c`](#insn-00bd601c)

~~~json
{
  "source": "00bd601c",
  "target": "00bd6058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6030`](#insn-00bd6030)

~~~json
{
  "source": "00bd6030",
  "target": "01126ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6048`](#insn-00bd6048)

~~~json
{
  "source": "00bd6048",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd6054`](#insn-00bd6054)

~~~json
{
  "source": "00bd6054",
  "target": "01126af0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126af0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6058`](#insn-00bd6058)

~~~json
{
  "source": "00bd6058",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd605c`](#insn-00bd605c)

~~~json
{
  "source": "00bd605c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
