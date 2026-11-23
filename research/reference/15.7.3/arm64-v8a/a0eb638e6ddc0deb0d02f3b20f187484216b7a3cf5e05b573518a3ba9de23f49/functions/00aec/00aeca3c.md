# 00aeca3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aec974`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec974.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-709e855c2edf2715475a5adda01ec7a1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeca80`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-b64c2970ab820b71fc3a9c8ec523dae9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeca3c",
  "name": "_ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f489dc50192cf4083a41a4d14ef01ce8e2b52d056f35fbdbf33a94ff7fdec14",
  "source_text_sha256": "9f489dc50192cf4083a41a4d14ef01ce8e2b52d056f35fbdbf33a94ff7fdec14",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeca3c",
        "00aeca7f"
      ]
    ],
    "bytes_sha256": "6619b3ecba8a236f0759ef702347b744fa3c600d79b6cd1467b6f7a393751216",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 692 bytes

~~~c

long _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00aeca48 to 00beca57 has its CatchHandler @ 00af1aec */
  if (DAT_010a0968 == 0) {
                    /* try { // try from 00aeca58 to 00becacb has its CatchHandler @ 00aeadc8 */
    DAT_010a0968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",param_3);
  }
  return DAT_010a0968;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeca3c"></a> `00aeca3c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeca40"></a> `00aeca40` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeca44"></a> `00aeca44` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeca48"></a> `00aeca48` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeca4c"></a> `00aeca4c` | `68 b6 44 f9` | ldr x8,[x19, #0x968] | `FALL_THROUGH`
<a id="insn-00aeca50"></a> `00aeca50` | `08 01 00 b5` | cbnz x8,0x00aeca70 | `CONDITIONAL_JUMP`
<a id="insn-00aeca54"></a> `00aeca54` | `43 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00aeca58"></a> `00aeca58` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aeca5c"></a> `00aeca5c` | `63 80 09 91` | add x3,x3,#0x260 | `FALL_THROUGH`
<a id="insn-00aeca60"></a> `00aeca60` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeca64"></a> `00aeca64` | `77 c5 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aeca68"></a> `00aeca68` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeca6c"></a> `00aeca6c` | `60 b6 04 f9` | str x0,[x19, #0x968] | `FALL_THROUGH`
<a id="insn-00aeca70"></a> `00aeca70` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeca74"></a> `00aeca74` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeca78"></a> `00aeca78` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeca7c"></a> `00aeca7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeca3c`](#insn-00aeca3c) 範囲 `[['00aeca3c', '00aeca47']]`
  - `FALL_THROUGH` [`00aeca44`](#insn-00aeca44) → [`00aeca48`](#insn-00aeca48)
- ブロック [`00aeca48`](#insn-00aeca48) 範囲 `[['00aeca48', '00aeca53']]`
  - `CONDITIONAL_JUMP` [`00aeca50`](#insn-00aeca50) → [`00aeca70`](#insn-00aeca70)
  - `FALL_THROUGH` [`00aeca50`](#insn-00aeca50) → [`00aeca54`](#insn-00aeca54)
- ブロック [`00aeca54`](#insn-00aeca54) 範囲 `[['00aeca54', '00aeca57']]`
  - `FALL_THROUGH` [`00aeca54`](#insn-00aeca54) → [`00aeca58`](#insn-00aeca58)
- ブロック [`00aeca58`](#insn-00aeca58) 範囲 `[['00aeca58', '00aeca6f']]`
  - `FALL_THROUGH` [`00aeca6c`](#insn-00aeca6c) → [`00aeca70`](#insn-00aeca70)
- ブロック [`00aeca70`](#insn-00aeca70) 範囲 `[['00aeca70', '00aeca7f']]`

## 命令位置別の参照

- [`00aeca3c`](#insn-00aeca3c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca40`](#insn-00aeca40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca4c`](#insn-00aeca4c) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeca50`](#insn-00aeca50) → [`00aeca70`](#insn-00aeca70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca5c`](#insn-00aeca5c) → `00294260`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeca64`](#insn-00aeca64) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aeca6c`](#insn-00aeca6c) → `010a0968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeca70`](#insn-00aeca70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeca3c`](#insn-00aeca3c)

~~~json
{
  "source": "00aeca3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca40`](#insn-00aeca40)

~~~json
{
  "source": "00aeca40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca4c`](#insn-00aeca4c)

~~~json
{
  "source": "00aeca4c",
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
- 参照命令 [`00aeca50`](#insn-00aeca50)

~~~json
{
  "source": "00aeca50",
  "target": "00aeca70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca5c`](#insn-00aeca5c)

~~~json
{
  "source": "00aeca5c",
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
- 参照命令 [`00aeca64`](#insn-00aeca64)

~~~json
{
  "source": "00aeca64",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeca6c`](#insn-00aeca6c)

~~~json
{
  "source": "00aeca6c",
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
- 参照命令 [`00aeca70`](#insn-00aeca70)

~~~json
{
  "source": "00aeca70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
