# 00bdd4dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6dfdc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dfdc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-ee2286f4e7ab713beac57664b046a1f4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd904`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd904.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0011.md#compare-9b9ca500cf4f6e700ad3fc39d11a885c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd4dc",
  "name": "_ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6911f5cadc3071c1559ccedb4c755df82aeda7b2e850ec864036afd768ac1d34",
  "source_text_sha256": "6911f5cadc3071c1559ccedb4c755df82aeda7b2e850ec864036afd768ac1d34",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd4dc",
        "00bdd547"
      ]
    ],
    "bytes_sha256": "d33d848df16c5a4372f17c798f1e54ae43b7b17075cb6f5d1e92cd7c13aae63a",
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

## 疑似コード / UTF-8 774 bytes

~~~c

bool _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
                    /* try { // try from 00bdd4f4 to 00cdd4ff has its CatchHandler @ 00bde990 */
  if (DAT_01126a08 == '\0') {
                    /* try { // try from 00bdd514 to 00cdd53f has its CatchHandler @ 00bde9b0 */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126a00,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126a08 = iVar2 == 0;
    bVar1 = (bool)DAT_01126a08;
  }
  else {
    bVar1 = false;
  }
                    /* try { // try from 00bdd540 to 00cdd723 has its CatchHandler @ 00bd6d50 */
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd4dc"></a> `00bdd4dc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdd4e0"></a> `00bdd4e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd4e4"></a> `00bdd4e4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd4e8"></a> `00bdd4e8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdd4ec"></a> `00bdd4ec` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd4f0"></a> `00bdd4f0` | `a8 22 68 39` | ldrb w8,[x21, #0xa08] | `FALL_THROUGH`
<a id="insn-00bdd4f4"></a> `00bdd4f4` | `68 00 00 34` | cbz w8,0x00bdd500 | `CONDITIONAL_JUMP`
<a id="insn-00bdd4f8"></a> `00bdd4f8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdd4fc"></a> `00bdd4fc` | `0f 00 00 14` | b 0x00bdd538 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdd500"></a> `00bdd500` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdd504"></a> `00bdd504` | `49 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd508"></a> `00bdd508` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bdd50c"></a> `00bdd50c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bdd510"></a> `00bdd510` | `21 01 45 f9` | ldr x1,[x9, #0xa00] | `FALL_THROUGH`
<a id="insn-00bdd514"></a> `00bdd514` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bdd518"></a> `00bdd518` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd51c"></a> `00bdd51c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdd520"></a> `00bdd520` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bdd524"></a> `00bdd524` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd528"></a> `00bdd528` | `8e f5 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd52c"></a> `00bdd52c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bdd530"></a> `00bdd530` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bdd534"></a> `00bdd534` | `a0 22 28 39` | strb w0,[x21, #0xa08] | `FALL_THROUGH`
<a id="insn-00bdd538"></a> `00bdd538` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd53c"></a> `00bdd53c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd540"></a> `00bdd540` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdd544"></a> `00bdd544` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd4dc`](#insn-00bdd4dc) 範囲 `[['00bdd4dc', '00bdd4f3']]`
  - `FALL_THROUGH` [`00bdd4f0`](#insn-00bdd4f0) → [`00bdd4f4`](#insn-00bdd4f4)
- ブロック [`00bdd4f4`](#insn-00bdd4f4) 範囲 `[['00bdd4f4', '00bdd4f7']]`
  - `CONDITIONAL_JUMP` [`00bdd4f4`](#insn-00bdd4f4) → [`00bdd500`](#insn-00bdd500)
  - `FALL_THROUGH` [`00bdd4f4`](#insn-00bdd4f4) → [`00bdd4f8`](#insn-00bdd4f8)
- ブロック [`00bdd4f8`](#insn-00bdd4f8) 範囲 `[['00bdd4f8', '00bdd4ff']]`
  - `UNCONDITIONAL_JUMP` [`00bdd4fc`](#insn-00bdd4fc) → [`00bdd538`](#insn-00bdd538)
- ブロック [`00bdd500`](#insn-00bdd500) 範囲 `[['00bdd500', '00bdd513']]`
  - `FALL_THROUGH` [`00bdd510`](#insn-00bdd510) → [`00bdd514`](#insn-00bdd514)
- ブロック [`00bdd514`](#insn-00bdd514) 範囲 `[['00bdd514', '00bdd537']]`
  - `FALL_THROUGH` [`00bdd534`](#insn-00bdd534) → [`00bdd538`](#insn-00bdd538)
- ブロック [`00bdd538`](#insn-00bdd538) 範囲 `[['00bdd538', '00bdd53f']]`
  - `FALL_THROUGH` [`00bdd53c`](#insn-00bdd53c) → [`00bdd540`](#insn-00bdd540)
- ブロック [`00bdd540`](#insn-00bdd540) 範囲 `[['00bdd540', '00bdd547']]`

## 命令位置別の参照

- [`00bdd4dc`](#insn-00bdd4dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd4e0`](#insn-00bdd4e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd4e4`](#insn-00bdd4e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd4f0`](#insn-00bdd4f0) → `01126a08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdd4f4`](#insn-00bdd4f4) → [`00bdd500`](#insn-00bdd500) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd4fc`](#insn-00bdd4fc) → [`00bdd538`](#insn-00bdd538) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd510`](#insn-00bdd510) → `01126a00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd528`](#insn-00bdd528) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdd534`](#insn-00bdd534) → `01126a08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdd538`](#insn-00bdd538) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd53c`](#insn-00bdd53c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd4dc`](#insn-00bdd4dc)

~~~json
{
  "source": "00bdd4dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd4e0`](#insn-00bdd4e0)

~~~json
{
  "source": "00bdd4e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd4e4`](#insn-00bdd4e4)

~~~json
{
  "source": "00bdd4e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd4f0`](#insn-00bdd4f0)

~~~json
{
  "source": "00bdd4f0",
  "target": "01126a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd4f4`](#insn-00bdd4f4)

~~~json
{
  "source": "00bdd4f4",
  "target": "00bdd500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd4fc`](#insn-00bdd4fc)

~~~json
{
  "source": "00bdd4fc",
  "target": "00bdd538",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd510`](#insn-00bdd510)

~~~json
{
  "source": "00bdd510",
  "target": "01126a00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd528`](#insn-00bdd528)

~~~json
{
  "source": "00bdd528",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd534`](#insn-00bdd534)

~~~json
{
  "source": "00bdd534",
  "target": "01126a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd538`](#insn-00bdd538)

~~~json
{
  "source": "00bdd538",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd53c`](#insn-00bdd53c)

~~~json
{
  "source": "00bdd53c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
