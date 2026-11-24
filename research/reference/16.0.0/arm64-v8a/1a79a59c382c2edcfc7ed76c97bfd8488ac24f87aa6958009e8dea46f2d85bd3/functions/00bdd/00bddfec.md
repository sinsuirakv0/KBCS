# 00bddfec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6eaec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eaec.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-9f7de7c36ed6f0b3b0347b1f9721a01d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bde414`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde414.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-acd43e7884af35af68a5f20185e39df4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfec",
  "name": "_ZNK8firebase4auth4User12display_nameEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d5e7575c9620e99d8694337e2e82afd9cf73616c72f42254cba4a35bf0eeaf2",
  "source_text_sha256": "4d5e7575c9620e99d8694337e2e82afd9cf73616c72f42254cba4a35bf0eeaf2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfec",
        "00bde08f"
      ]
    ],
    "bytes_sha256": "8fd5015520119fc61df4c85aa030897dd187c6ee37ce7f5ede734effbe637799",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5af90](../00c5a/00c5af90.md)
- [00c5b1c0](../00c5b/00c5b1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 797 bytes

~~~c

void _ZNK8firebase4auth4User12display_nameEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002a630e);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
  lVar4 = FUN_004977f4(uVar1,lVar4,DAT_011269d0);
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfec"></a> `00bddfec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bddff0"></a> `00bddff0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddff4"></a> `00bddff4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddff8"></a> `00bddff8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddffc"></a> `00bddffc` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bde000"></a> `00bde000` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bde004"></a> `00bde004` | `c9 02 00 b4` | cbz x9,0x00bde05c | `CONDITIONAL_JUMP`
<a id="insn-00bde008"></a> `00bde008` | `35 01 41 f9` | ldr x21,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bde00c"></a> `00bde00c` | `95 02 00 b4` | cbz x21,0x00bde05c | `CONDITIONAL_JUMP`
<a id="insn-00bde010"></a> `00bde010` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bde014"></a> `00bde014` | `1b f3 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bde018"></a> `00bde018` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bde01c"></a> `00bde01c` | `02 e9 44 f9` | ldr x2,[x8, #0x9d0] | `FALL_THROUGH`
<a id="insn-00bde020"></a> `00bde020` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bde024"></a> `00bde024` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bde028"></a> `00bde028` | `f3 e5 e2 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bde02c"></a> `00bde02c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bde030"></a> `00bde030` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bde034"></a> `00bde034` | `cb f2 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bde038"></a> `00bde038` | `15 02 00 b4` | cbz x21,0x00bde078 | `CONDITIONAL_JUMP`
<a id="insn-00bde03c"></a> `00bde03c` | `e0 01 00 37` | tbnz w0,#0x0,0x00bde078 | `CONDITIONAL_JUMP`
<a id="insn-00bde040"></a> `00bde040` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bde044"></a> `00bde044` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bde048"></a> `00bde048` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde04c"></a> `00bde04c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde050"></a> `00bde050` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bde054"></a> `00bde054` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde058"></a> `00bde058` | `ce f3 01 14` | b 0x00c5af90 | `CALL_TERMINATOR`
<a id="insn-00bde05c"></a> `00bde05c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde060"></a> `00bde060` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde064"></a> `00bde064` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde068"></a> `00bde068` | `41 b6 ff 90` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bde06c"></a> `00bde06c` | `21 38 0c 91` | add x1,x1,#0x30e | `FALL_THROUGH`
<a id="insn-00bde070"></a> `00bde070` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde074"></a> `00bde074` | `53 f4 01 14` | b 0x00c5b1c0 | `CALL_TERMINATOR`
<a id="insn-00bde078"></a> `00bde078` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bde07c"></a> `00bde07c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bde080"></a> `00bde080` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde084"></a> `00bde084` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde088"></a> `00bde088` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde08c"></a> `00bde08c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfec`](#insn-00bddfec) 範囲 `[['00bddfec', '00bde007']]`
  - `CONDITIONAL_JUMP` [`00bde004`](#insn-00bde004) → [`00bde05c`](#insn-00bde05c)
  - `FALL_THROUGH` [`00bde004`](#insn-00bde004) → [`00bde008`](#insn-00bde008)
- ブロック [`00bde008`](#insn-00bde008) 範囲 `[['00bde008', '00bde00f']]`
  - `CONDITIONAL_JUMP` [`00bde00c`](#insn-00bde00c) → [`00bde05c`](#insn-00bde05c)
  - `FALL_THROUGH` [`00bde00c`](#insn-00bde00c) → [`00bde010`](#insn-00bde010)
- ブロック [`00bde010`](#insn-00bde010) 範囲 `[['00bde010', '00bde03b']]`
  - `CONDITIONAL_JUMP` [`00bde038`](#insn-00bde038) → [`00bde078`](#insn-00bde078)
  - `FALL_THROUGH` [`00bde038`](#insn-00bde038) → [`00bde03c`](#insn-00bde03c)
- ブロック [`00bde03c`](#insn-00bde03c) 範囲 `[['00bde03c', '00bde03f']]`
  - `CONDITIONAL_JUMP` [`00bde03c`](#insn-00bde03c) → [`00bde078`](#insn-00bde078)
  - `FALL_THROUGH` [`00bde03c`](#insn-00bde03c) → [`00bde040`](#insn-00bde040)
- ブロック [`00bde040`](#insn-00bde040) 範囲 `[['00bde040', '00bde05b']]`
- ブロック [`00bde05c`](#insn-00bde05c) 範囲 `[['00bde05c', '00bde077']]`
- ブロック [`00bde078`](#insn-00bde078) 範囲 `[['00bde078', '00bde08f']]`

## 命令位置別の参照

- [`00bddfec`](#insn-00bddfec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddff0`](#insn-00bddff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddff4`](#insn-00bddff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde004`](#insn-00bde004) → [`00bde05c`](#insn-00bde05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde00c`](#insn-00bde00c) → [`00bde05c`](#insn-00bde05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde014`](#insn-00bde014) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bde01c`](#insn-00bde01c) → `011269d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde028`](#insn-00bde028) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bde034`](#insn-00bde034) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bde038`](#insn-00bde038) → [`00bde078`](#insn-00bde078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde03c`](#insn-00bde03c) → [`00bde078`](#insn-00bde078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde048`](#insn-00bde048) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde04c`](#insn-00bde04c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde058`](#insn-00bde058) → [`00c5af90`](../00c5a/00c5af90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af90` · 推定シンボル `None` · 推定型 `None`
- [`00bde060`](#insn-00bde060) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde064`](#insn-00bde064) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde06c`](#insn-00bde06c) → `002a630e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bde074`](#insn-00bde074) → [`00c5b1c0`](../00c5b/00c5b1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bde080`](#insn-00bde080) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde084`](#insn-00bde084) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfec`](#insn-00bddfec)

~~~json
{
  "source": "00bddfec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddff0`](#insn-00bddff0)

~~~json
{
  "source": "00bddff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddff4`](#insn-00bddff4)

~~~json
{
  "source": "00bddff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde004`](#insn-00bde004)

~~~json
{
  "source": "00bde004",
  "target": "00bde05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde00c`](#insn-00bde00c)

~~~json
{
  "source": "00bde00c",
  "target": "00bde05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde014`](#insn-00bde014)

~~~json
{
  "source": "00bde014",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde01c`](#insn-00bde01c)

~~~json
{
  "source": "00bde01c",
  "target": "011269d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde028`](#insn-00bde028)

~~~json
{
  "source": "00bde028",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde034`](#insn-00bde034)

~~~json
{
  "source": "00bde034",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde038`](#insn-00bde038)

~~~json
{
  "source": "00bde038",
  "target": "00bde078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde03c`](#insn-00bde03c)

~~~json
{
  "source": "00bde03c",
  "target": "00bde078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde048`](#insn-00bde048)

~~~json
{
  "source": "00bde048",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde04c`](#insn-00bde04c)

~~~json
{
  "source": "00bde04c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde058`](#insn-00bde058)

~~~json
{
  "source": "00bde058",
  "target": "00c5af90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde060`](#insn-00bde060)

~~~json
{
  "source": "00bde060",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde064`](#insn-00bde064)

~~~json
{
  "source": "00bde064",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde06c`](#insn-00bde06c)

~~~json
{
  "source": "00bde06c",
  "target": "002a630e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a630e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a630e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bde074`](#insn-00bde074)

~~~json
{
  "source": "00bde074",
  "target": "00c5b1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde080`](#insn-00bde080)

~~~json
{
  "source": "00bde080",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde084`](#insn-00bde084)

~~~json
{
  "source": "00bde084",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
