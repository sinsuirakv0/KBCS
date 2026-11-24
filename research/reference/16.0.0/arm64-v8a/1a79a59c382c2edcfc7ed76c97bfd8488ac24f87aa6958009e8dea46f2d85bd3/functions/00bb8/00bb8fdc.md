# 00bb8fdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4b2b8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b2b8.md) · 移動量 `+0x6dd24`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0016.md#compare-dd357ecc7d809a1404aa278acc6521cb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb9404`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9404.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-f21108229e99fbe9440266f08a62baab)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb8fdc",
  "name": "_ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90f248f19b20b70e1d29361fb1fd9b7f3113da3b1f7b36329b0f8a868d9c8682",
  "source_text_sha256": "90f248f19b20b70e1d29361fb1fd9b7f3113da3b1f7b36329b0f8a868d9c8682",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb8fdc",
        "00bb9047"
      ]
    ],
    "bytes_sha256": "c5b97acc3d0cd07a9f50ebd6629373ecc2d18f966b717a32158a0d605e51a971",
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

## 疑似コード / UTF-8 701 bytes

~~~c

bool _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01125f40 == '\0') {
                    /* try { // try from 00bb9010 to 00cb9017 has its CatchHandler @ 00bb9060 */
                    /* try { // try from 00bb9018 to 00cb9057 has its CatchHandler @ 00bb8fbc */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01125f38,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01125f40 = iVar2 == 0;
    bVar1 = (bool)DAT_01125f40;
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
<a id="insn-00bb8fdc"></a> `00bb8fdc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bb8fe0"></a> `00bb8fe0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8fe4"></a> `00bb8fe4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb8fe8"></a> `00bb8fe8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bb8fec"></a> `00bb8fec` | `75 2b 00 b0` | adrp x21,0x1125000 | `FALL_THROUGH`
<a id="insn-00bb8ff0"></a> `00bb8ff0` | `a8 02 7d 39` | ldrb w8,[x21, #0xf40] | `FALL_THROUGH`
<a id="insn-00bb8ff4"></a> `00bb8ff4` | `68 00 00 34` | cbz w8,0x00bb9000 | `CONDITIONAL_JUMP`
<a id="insn-00bb8ff8"></a> `00bb8ff8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bb8ffc"></a> `00bb8ffc` | `0f 00 00 14` | b 0x00bb9038 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb9000"></a> `00bb9000` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bb9004"></a> `00bb9004` | `69 2b 00 90` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00bb9008"></a> `00bb9008` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bb900c"></a> `00bb900c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bb9010"></a> `00bb9010` | `21 9d 47 f9` | ldr x1,[x9, #0xf38] | `FALL_THROUGH`
<a id="insn-00bb9014"></a> `00bb9014` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bb9018"></a> `00bb9018` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb901c"></a> `00bb901c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb9020"></a> `00bb9020` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bb9024"></a> `00bb9024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb9028"></a> `00bb9028` | `ce 86 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bb902c"></a> `00bb902c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bb9030"></a> `00bb9030` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bb9034"></a> `00bb9034` | `a0 02 3d 39` | strb w0,[x21, #0xf40] | `FALL_THROUGH`
<a id="insn-00bb9038"></a> `00bb9038` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb903c"></a> `00bb903c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb9040"></a> `00bb9040` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bb9044"></a> `00bb9044` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb8fdc`](#insn-00bb8fdc) 範囲 `[['00bb8fdc', '00bb8ff7']]`
  - `CONDITIONAL_JUMP` [`00bb8ff4`](#insn-00bb8ff4) → [`00bb9000`](#insn-00bb9000)
  - `FALL_THROUGH` [`00bb8ff4`](#insn-00bb8ff4) → [`00bb8ff8`](#insn-00bb8ff8)
- ブロック [`00bb8ff8`](#insn-00bb8ff8) 範囲 `[['00bb8ff8', '00bb8fff']]`
  - `UNCONDITIONAL_JUMP` [`00bb8ffc`](#insn-00bb8ffc) → [`00bb9038`](#insn-00bb9038)
- ブロック [`00bb9000`](#insn-00bb9000) 範囲 `[['00bb9000', '00bb900f']]`
  - `FALL_THROUGH` [`00bb900c`](#insn-00bb900c) → [`00bb9010`](#insn-00bb9010)
- ブロック [`00bb9010`](#insn-00bb9010) 範囲 `[['00bb9010', '00bb9017']]`
  - `FALL_THROUGH` [`00bb9014`](#insn-00bb9014) → [`00bb9018`](#insn-00bb9018)
- ブロック [`00bb9018`](#insn-00bb9018) 範囲 `[['00bb9018', '00bb9037']]`
  - `FALL_THROUGH` [`00bb9034`](#insn-00bb9034) → [`00bb9038`](#insn-00bb9038)
- ブロック [`00bb9038`](#insn-00bb9038) 範囲 `[['00bb9038', '00bb9047']]`

## 命令位置別の参照

- [`00bb8fdc`](#insn-00bb8fdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8fe0`](#insn-00bb8fe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8fe4`](#insn-00bb8fe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8ff0`](#insn-00bb8ff0) → `01125f40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8ff4`](#insn-00bb8ff4) → [`00bb9000`](#insn-00bb9000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8ffc`](#insn-00bb8ffc) → [`00bb9038`](#insn-00bb9038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9010`](#insn-00bb9010) → `01125f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb9028`](#insn-00bb9028) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bb9034`](#insn-00bb9034) → `01125f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb9038`](#insn-00bb9038) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb903c`](#insn-00bb903c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb8fdc`](#insn-00bb8fdc)

~~~json
{
  "source": "00bb8fdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8fe0`](#insn-00bb8fe0)

~~~json
{
  "source": "00bb8fe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8fe4`](#insn-00bb8fe4)

~~~json
{
  "source": "00bb8fe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8ff0`](#insn-00bb8ff0)

~~~json
{
  "source": "00bb8ff0",
  "target": "01125f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f40",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8ff4`](#insn-00bb8ff4)

~~~json
{
  "source": "00bb8ff4",
  "target": "00bb9000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8ffc`](#insn-00bb8ffc)

~~~json
{
  "source": "00bb8ffc",
  "target": "00bb9038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9010`](#insn-00bb9010)

~~~json
{
  "source": "00bb9010",
  "target": "01125f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9028`](#insn-00bb9028)

~~~json
{
  "source": "00bb9028",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9034`](#insn-00bb9034)

~~~json
{
  "source": "00bb9034",
  "target": "01125f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f40",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9038`](#insn-00bb9038)

~~~json
{
  "source": "00bb9038",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb903c`](#insn-00bb903c)

~~~json
{
  "source": "00bb903c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
