# 00bcbff8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5caf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caf8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-ddf9f18b667b32122232a941be88aa03)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc420`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-1bc29e9b53687bb22d253a9c967370f2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbff8",
  "name": "_ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09fc2edf170cb9ebfe3d4bbeab9a0dc740f8b6044d7fbe427f59bf64f050789b",
  "source_text_sha256": "09fc2edf170cb9ebfe3d4bbeab9a0dc740f8b6044d7fbe427f59bf64f050789b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbff8",
        "00bcc063"
      ]
    ],
    "bytes_sha256": "0c2376b589a2a12b088bd41b9472635c47c8ce13f4986615cf727cc169e43bda",
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

- [00c5ab60](../00c5a/00c5ab60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 566 bytes

~~~c

bool _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126330 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126328,param_2,param_3);
                    /* catch() { ... } // from try @ 00bcc220 with catch @ 00bcc044 */
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126330 = iVar2 == 0;
    bVar1 = (bool)DAT_01126330;
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
<a id="insn-00bcbff8"></a> `00bcbff8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbffc"></a> `00bcbffc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc000"></a> `00bcc000` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc004"></a> `00bcc004` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcc008"></a> `00bcc008` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc00c"></a> `00bcc00c` | `a8 c2 4c 39` | ldrb w8,[x21, #0x330] | `FALL_THROUGH`
<a id="insn-00bcc010"></a> `00bcc010` | `68 00 00 34` | cbz w8,0x00bcc01c | `CONDITIONAL_JUMP`
<a id="insn-00bcc014"></a> `00bcc014` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bcc018"></a> `00bcc018` | `0f 00 00 14` | b 0x00bcc054 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcc01c"></a> `00bcc01c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcc020"></a> `00bcc020` | `c9 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc024"></a> `00bcc024` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bcc028"></a> `00bcc028` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bcc02c"></a> `00bcc02c` | `21 95 41 f9` | ldr x1,[x9, #0x328] | `FALL_THROUGH`
<a id="insn-00bcc030"></a> `00bcc030` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bcc034"></a> `00bcc034` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcc038"></a> `00bcc038` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcc03c"></a> `00bcc03c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcc040"></a> `00bcc040` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc044"></a> `00bcc044` | `c7 3a 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc048"></a> `00bcc048` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bcc04c"></a> `00bcc04c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bcc050"></a> `00bcc050` | `a0 c2 0c 39` | strb w0,[x21, #0x330] | `FALL_THROUGH`
<a id="insn-00bcc054"></a> `00bcc054` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc058"></a> `00bcc058` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc05c"></a> `00bcc05c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcc060"></a> `00bcc060` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbff8`](#insn-00bcbff8) 範囲 `[['00bcbff8', '00bcc013']]`
  - `CONDITIONAL_JUMP` [`00bcc010`](#insn-00bcc010) → [`00bcc01c`](#insn-00bcc01c)
  - `FALL_THROUGH` [`00bcc010`](#insn-00bcc010) → [`00bcc014`](#insn-00bcc014)
- ブロック [`00bcc014`](#insn-00bcc014) 範囲 `[['00bcc014', '00bcc01b']]`
  - `UNCONDITIONAL_JUMP` [`00bcc018`](#insn-00bcc018) → [`00bcc054`](#insn-00bcc054)
- ブロック [`00bcc01c`](#insn-00bcc01c) 範囲 `[['00bcc01c', '00bcc043']]`
  - `FALL_THROUGH` [`00bcc040`](#insn-00bcc040) → [`00bcc044`](#insn-00bcc044)
- ブロック [`00bcc044`](#insn-00bcc044) 範囲 `[['00bcc044', '00bcc053']]`
  - `FALL_THROUGH` [`00bcc050`](#insn-00bcc050) → [`00bcc054`](#insn-00bcc054)
- ブロック [`00bcc054`](#insn-00bcc054) 範囲 `[['00bcc054', '00bcc063']]`

## 命令位置別の参照

- [`00bcbff8`](#insn-00bcbff8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbffc`](#insn-00bcbffc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc000`](#insn-00bcc000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc00c`](#insn-00bcc00c) → `01126330`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcc010`](#insn-00bcc010) → [`00bcc01c`](#insn-00bcc01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc018`](#insn-00bcc018) → [`00bcc054`](#insn-00bcc054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc02c`](#insn-00bcc02c) → `01126328`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc044`](#insn-00bcc044) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcc050`](#insn-00bcc050) → `01126330`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcc054`](#insn-00bcc054) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc058`](#insn-00bcc058) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbff8`](#insn-00bcbff8)

~~~json
{
  "source": "00bcbff8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbffc`](#insn-00bcbffc)

~~~json
{
  "source": "00bcbffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc000`](#insn-00bcc000)

~~~json
{
  "source": "00bcc000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc00c`](#insn-00bcc00c)

~~~json
{
  "source": "00bcc00c",
  "target": "01126330",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126330",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc010`](#insn-00bcc010)

~~~json
{
  "source": "00bcc010",
  "target": "00bcc01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc018`](#insn-00bcc018)

~~~json
{
  "source": "00bcc018",
  "target": "00bcc054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc02c`](#insn-00bcc02c)

~~~json
{
  "source": "00bcc02c",
  "target": "01126328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126328",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc044`](#insn-00bcc044)

~~~json
{
  "source": "00bcc044",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc050`](#insn-00bcc050)

~~~json
{
  "source": "00bcc050",
  "target": "01126330",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126330",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc054`](#insn-00bcc054)

~~~json
{
  "source": "00bcc054",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc058`](#insn-00bcc058)

~~~json
{
  "source": "00bcc058",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
