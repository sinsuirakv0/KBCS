# 00aecc0c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aecb44`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecb44.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-a032e3a8f215d5057b345b63c1ce18a2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aecc50`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-4eb9c499f24c393f8a2fa6d0ba2f8959)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecc0c",
  "name": "_ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42b61f02fbb76f8e40c55c3422b07da9db6d118fc4f04c9c56248b4de9c093cd",
  "source_text_sha256": "42b61f02fbb76f8e40c55c3422b07da9db6d118fc4f04c9c56248b4de9c093cd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecc0c",
        "00aecc7b"
      ]
    ],
    "bytes_sha256": "cb408959f21c82cde52a62b58b38974acf454403d8ec3c2481666752bf941d13",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)
- [00bde060](../00bde/00bde060.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 765 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0968 == 0) {
    DAT_010a0968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
                    /* try { // try from 00aecc64 to 00becc6b has its CatchHandler @ 00af1a3c */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0968,&PTR_s_detachFd_00c10530,1,&DAT_010a0978,
             "android/os/ParcelFileDescriptor");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecc0c"></a> `00aecc0c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecc10"></a> `00aecc10` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecc14"></a> `00aecc14` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecc18"></a> `00aecc18` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecc1c"></a> `00aecc1c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aecc20"></a> `00aecc20` | `81 b6 44 f9` | ldr x1,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00aecc24"></a> `00aecc24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecc28"></a> `00aecc28` | `41 01 00 b5` | cbnz x1,0x00aecc50 | `CONDITIONAL_JUMP`
<a id="insn-00aecc2c"></a> `00aecc2c` | `43 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00aecc30"></a> `00aecc30` | `63 80 09 91` | add x3,x3,#0x260 | `FALL_THROUGH`
<a id="insn-00aecc34"></a> `00aecc34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecc38"></a> `00aecc38` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aecc3c"></a> `00aecc3c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aecc40"></a> `00aecc40` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aecc44"></a> `00aecc44` | `ff c4 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aecc48"></a> `00aecc48` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aecc4c"></a> `00aecc4c` | `80 b6 04 f9` | str x0,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00aecc50"></a> `00aecc50` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecc54"></a> `00aecc54` | `22 09 00 90` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aecc58"></a> `00aecc58` | `a4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecc5c"></a> `00aecc5c` | `45 bd ff 90` | adrp x5,0x294000 | `FALL_THROUGH`
<a id="insn-00aecc60"></a> `00aecc60` | `42 c0 14 91` | add x2,x2,#0x530 | `FALL_THROUGH`
<a id="insn-00aecc64"></a> `00aecc64` | `84 e0 25 91` | add x4,x4,#0x978 | `FALL_THROUGH`
<a id="insn-00aecc68"></a> `00aecc68` | `a5 80 09 91` | add x5,x5,#0x260 | `FALL_THROUGH`
<a id="insn-00aecc6c"></a> `00aecc6c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aecc70"></a> `00aecc70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecc74"></a> `00aecc74` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecc78"></a> `00aecc78` | `fa c4 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecc0c`](#insn-00aecc0c) 範囲 `[['00aecc0c', '00aecc2b']]`
  - `CONDITIONAL_JUMP` [`00aecc28`](#insn-00aecc28) → [`00aecc50`](#insn-00aecc50)
  - `FALL_THROUGH` [`00aecc28`](#insn-00aecc28) → [`00aecc2c`](#insn-00aecc2c)
- ブロック [`00aecc2c`](#insn-00aecc2c) 範囲 `[['00aecc2c', '00aecc4f']]`
  - `FALL_THROUGH` [`00aecc4c`](#insn-00aecc4c) → [`00aecc50`](#insn-00aecc50)
- ブロック [`00aecc50`](#insn-00aecc50) 範囲 `[['00aecc50', '00aecc63']]`
  - `FALL_THROUGH` [`00aecc60`](#insn-00aecc60) → [`00aecc64`](#insn-00aecc64)
- ブロック [`00aecc64`](#insn-00aecc64) 範囲 `[['00aecc64', '00aecc7b']]`

## 命令位置別の参照

- [`00aecc0c`](#insn-00aecc0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc10`](#insn-00aecc10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc20`](#insn-00aecc20) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecc28`](#insn-00aecc28) → [`00aecc50`](#insn-00aecc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc30`](#insn-00aecc30) → `00294260`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecc44`](#insn-00aecc44) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aecc4c`](#insn-00aecc4c) → `010a0968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecc50`](#insn-00aecc50) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc60`](#insn-00aecc60) → `00c10530`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aecc64`](#insn-00aecc64) → `010a0978`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc68`](#insn-00aecc68) → `00294260`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecc78`](#insn-00aecc78) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecc0c`](#insn-00aecc0c)

~~~json
{
  "source": "00aecc0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc10`](#insn-00aecc10)

~~~json
{
  "source": "00aecc10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc20`](#insn-00aecc20)

~~~json
{
  "source": "00aecc20",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecc28`](#insn-00aecc28)

~~~json
{
  "source": "00aecc28",
  "target": "00aecc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc30`](#insn-00aecc30)

~~~json
{
  "source": "00aecc30",
  "target": "00294260",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294260",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "00294260",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecc44`](#insn-00aecc44)

~~~json
{
  "source": "00aecc44",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecc4c`](#insn-00aecc4c)

~~~json
{
  "source": "00aecc4c",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecc50`](#insn-00aecc50)

~~~json
{
  "source": "00aecc50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc60`](#insn-00aecc60)

~~~json
{
  "source": "00aecc60",
  "target": "00c10530",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10530",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecc64`](#insn-00aecc64)

~~~json
{
  "source": "00aecc64",
  "target": "010a0978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc68`](#insn-00aecc68)

~~~json
{
  "source": "00aecc68",
  "target": "00294260",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294260",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "00294260",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecc78`](#insn-00aecc78)

~~~json
{
  "source": "00aecc78",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
