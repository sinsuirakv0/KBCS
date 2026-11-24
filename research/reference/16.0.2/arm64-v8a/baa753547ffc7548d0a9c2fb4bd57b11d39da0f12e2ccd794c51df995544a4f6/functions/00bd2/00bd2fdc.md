# 00bd2fdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd2f40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2f40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0083.md#compare-2118df6d284e2caf40d13867b9eaf0df)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd3fd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd3/00bd3fd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0083.md#compare-d87a5de3e1132e6e9ffe9bc7694b5753)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2fdc",
  "name": "_ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d80b7c224b0ab5161f7996b41271e1df56a72781815525e0222a447029b1bfa",
  "source_text_sha256": "1d80b7c224b0ab5161f7996b41271e1df56a72781815525e0222a447029b1bfa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2fdc",
        "00bd3047"
      ]
    ],
    "bytes_sha256": "67c5f7813c3d29f8368374afa29ed220b4af899170dbc93b61b0eeee09d137f2",
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

## 疑似コード / UTF-8 502 bytes

~~~c

bool _ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
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
<a id="insn-00bd2fdc"></a> `00bd2fdc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd2fe0"></a> `00bd2fe0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2fe4"></a> `00bd2fe4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2fe8"></a> `00bd2fe8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd2fec"></a> `00bd2fec` | `b5 2a 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd2ff0"></a> `00bd2ff0` | `a8 c2 6b 39` | ldrb w8,[x21, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bd2ff4"></a> `00bd2ff4` | `68 00 00 34` | cbz w8,0x00bd3000 | `CONDITIONAL_JUMP`
<a id="insn-00bd2ff8"></a> `00bd2ff8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bd2ffc"></a> `00bd2ffc` | `0f 00 00 14` | b 0x00bd3038 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd3000"></a> `00bd3000` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd3004"></a> `00bd3004` | `89 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3008"></a> `00bd3008` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bd300c"></a> `00bd300c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bd3010"></a> `00bd3010` | `21 75 45 f9` | ldr x1,[x9, #0xae8] | `FALL_THROUGH`
<a id="insn-00bd3014"></a> `00bd3014` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bd3018"></a> `00bd3018` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd301c"></a> `00bd301c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3020"></a> `00bd3020` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bd3024"></a> `00bd3024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3028"></a> `00bd3028` | `02 20 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd302c"></a> `00bd302c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bd3030"></a> `00bd3030` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bd3034"></a> `00bd3034` | `a0 c2 2b 39` | strb w0,[x21, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bd3038"></a> `00bd3038` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd303c"></a> `00bd303c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3040"></a> `00bd3040` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd3044"></a> `00bd3044` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2fdc`](#insn-00bd2fdc) 範囲 `[['00bd2fdc', '00bd2ff7']]`
  - `CONDITIONAL_JUMP` [`00bd2ff4`](#insn-00bd2ff4) → [`00bd3000`](#insn-00bd3000)
  - `FALL_THROUGH` [`00bd2ff4`](#insn-00bd2ff4) → [`00bd2ff8`](#insn-00bd2ff8)
- ブロック [`00bd2ff8`](#insn-00bd2ff8) 範囲 `[['00bd2ff8', '00bd2fff']]`
  - `UNCONDITIONAL_JUMP` [`00bd2ffc`](#insn-00bd2ffc) → [`00bd3038`](#insn-00bd3038)
- ブロック [`00bd3000`](#insn-00bd3000) 範囲 `[['00bd3000', '00bd3037']]`
  - `FALL_THROUGH` [`00bd3034`](#insn-00bd3034) → [`00bd3038`](#insn-00bd3038)
- ブロック [`00bd3038`](#insn-00bd3038) 範囲 `[['00bd3038', '00bd3047']]`

## 命令位置別の参照

- [`00bd2fdc`](#insn-00bd2fdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fe0`](#insn-00bd2fe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fe4`](#insn-00bd2fe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ff0`](#insn-00bd2ff0) → `01126af0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd2ff4`](#insn-00bd2ff4) → [`00bd3000`](#insn-00bd3000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ffc`](#insn-00bd2ffc) → [`00bd3038`](#insn-00bd3038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3010`](#insn-00bd3010) → `01126ae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3028`](#insn-00bd3028) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd3034`](#insn-00bd3034) → `01126af0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3038`](#insn-00bd3038) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd303c`](#insn-00bd303c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2fdc`](#insn-00bd2fdc)

~~~json
{
  "source": "00bd2fdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fe0`](#insn-00bd2fe0)

~~~json
{
  "source": "00bd2fe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fe4`](#insn-00bd2fe4)

~~~json
{
  "source": "00bd2fe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ff0`](#insn-00bd2ff0)

~~~json
{
  "source": "00bd2ff0",
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
- 参照命令 [`00bd2ff4`](#insn-00bd2ff4)

~~~json
{
  "source": "00bd2ff4",
  "target": "00bd3000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ffc`](#insn-00bd2ffc)

~~~json
{
  "source": "00bd2ffc",
  "target": "00bd3038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3010`](#insn-00bd3010)

~~~json
{
  "source": "00bd3010",
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
- 参照命令 [`00bd3028`](#insn-00bd3028)

~~~json
{
  "source": "00bd3028",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3034`](#insn-00bd3034)

~~~json
{
  "source": "00bd3034",
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
- 参照命令 [`00bd3038`](#insn-00bd3038)

~~~json
{
  "source": "00bd3038",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd303c`](#insn-00bd303c)

~~~json
{
  "source": "00bd303c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
