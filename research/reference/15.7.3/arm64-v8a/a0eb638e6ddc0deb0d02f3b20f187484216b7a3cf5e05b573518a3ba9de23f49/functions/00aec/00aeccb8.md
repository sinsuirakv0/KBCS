# 00aeccb8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aecbf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbf0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-7e5cc80c4527c8adf6bf612f9b6e5f31)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeccfc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-4b0006e55cc754d206928f2d76083132)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeccb8",
  "name": "_ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe67cdd8914196c3f972636bacb9f4d104007aa86cb2c21c0cf5e9059787549d",
  "source_text_sha256": "fe67cdd8914196c3f972636bacb9f4d104007aa86cb2c21c0cf5e9059787549d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeccb8",
        "00aecd27"
      ]
    ],
    "bytes_sha256": "37a67db7035fe59c538e3b369d98f49f124c21a0076da484511344ce7af48137",
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

- [00bde020](../00bde/00bde020.md)
- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 732 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aeccbc to 00becd27 has its CatchHandler @ 00af1a38 */
  if (DAT_010a0968 == 0) {
    DAT_010a0968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0968,&DAT_002f5d88,1,&DAT_010a0980,"android/os/ParcelFileDescriptor");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeccb8"></a> `00aeccb8` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeccbc"></a> `00aeccbc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeccc0"></a> `00aeccc0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeccc4"></a> `00aeccc4` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeccc8"></a> `00aeccc8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aecccc"></a> `00aecccc` | `81 b6 44 f9` | ldr x1,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00aeccd0"></a> `00aeccd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeccd4"></a> `00aeccd4` | `41 01 00 b5` | cbnz x1,0x00aeccfc | `CONDITIONAL_JUMP`
<a id="insn-00aeccd8"></a> `00aeccd8` | `43 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00aeccdc"></a> `00aeccdc` | `63 80 09 91` | add x3,x3,#0x260 | `FALL_THROUGH`
<a id="insn-00aecce0"></a> `00aecce0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecce4"></a> `00aecce4` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aecce8"></a> `00aecce8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeccec"></a> `00aeccec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeccf0"></a> `00aeccf0` | `d4 c4 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aeccf4"></a> `00aeccf4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeccf8"></a> `00aeccf8` | `80 b6 04 f9` | str x0,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00aeccfc"></a> `00aeccfc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecd00"></a> `00aecd00` | `42 c0 ff b0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aecd04"></a> `00aecd04` | `a4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecd08"></a> `00aecd08` | `45 bd ff 90` | adrp x5,0x294000 | `FALL_THROUGH`
<a id="insn-00aecd0c"></a> `00aecd0c` | `42 20 36 91` | add x2,x2,#0xd88 | `FALL_THROUGH`
<a id="insn-00aecd10"></a> `00aecd10` | `84 00 26 91` | add x4,x4,#0x980 | `FALL_THROUGH`
<a id="insn-00aecd14"></a> `00aecd14` | `a5 80 09 91` | add x5,x5,#0x260 | `FALL_THROUGH`
<a id="insn-00aecd18"></a> `00aecd18` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aecd1c"></a> `00aecd1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecd20"></a> `00aecd20` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecd24"></a> `00aecd24` | `bf c4 03 14` | b 0x00bde020 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeccb8`](#insn-00aeccb8) 範囲 `[['00aeccb8', '00aeccbb']]`
  - `FALL_THROUGH` [`00aeccb8`](#insn-00aeccb8) → [`00aeccbc`](#insn-00aeccbc)
- ブロック [`00aeccbc`](#insn-00aeccbc) 範囲 `[['00aeccbc', '00aeccd7']]`
  - `CONDITIONAL_JUMP` [`00aeccd4`](#insn-00aeccd4) → [`00aeccfc`](#insn-00aeccfc)
  - `FALL_THROUGH` [`00aeccd4`](#insn-00aeccd4) → [`00aeccd8`](#insn-00aeccd8)
- ブロック [`00aeccd8`](#insn-00aeccd8) 範囲 `[['00aeccd8', '00aeccfb']]`
  - `FALL_THROUGH` [`00aeccf8`](#insn-00aeccf8) → [`00aeccfc`](#insn-00aeccfc)
- ブロック [`00aeccfc`](#insn-00aeccfc) 範囲 `[['00aeccfc', '00aecd27']]`

## 命令位置別の参照

- [`00aeccb8`](#insn-00aeccb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccbc`](#insn-00aeccbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecccc`](#insn-00aecccc) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeccd4`](#insn-00aeccd4) → [`00aeccfc`](#insn-00aeccfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccdc`](#insn-00aeccdc) → `00294260`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeccf0`](#insn-00aeccf0) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aeccf8`](#insn-00aeccf8) → `010a0968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeccfc`](#insn-00aeccfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd0c`](#insn-00aecd0c) → `002f5d88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd10`](#insn-00aecd10) → `010a0980`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd14`](#insn-00aecd14) → `00294260`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecd24`](#insn-00aecd24) → [`00bde020`](../00bde/00bde020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde020` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeccb8`](#insn-00aeccb8)

~~~json
{
  "source": "00aeccb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccbc`](#insn-00aeccbc)

~~~json
{
  "source": "00aeccbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecccc`](#insn-00aecccc)

~~~json
{
  "source": "00aecccc",
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
- 参照命令 [`00aeccd4`](#insn-00aeccd4)

~~~json
{
  "source": "00aeccd4",
  "target": "00aeccfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccdc`](#insn-00aeccdc)

~~~json
{
  "source": "00aeccdc",
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
- 参照命令 [`00aeccf0`](#insn-00aeccf0)

~~~json
{
  "source": "00aeccf0",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeccf8`](#insn-00aeccf8)

~~~json
{
  "source": "00aeccf8",
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
- 参照命令 [`00aeccfc`](#insn-00aeccfc)

~~~json
{
  "source": "00aeccfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd0c`](#insn-00aecd0c)

~~~json
{
  "source": "00aecd0c",
  "target": "002f5d88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd10`](#insn-00aecd10)

~~~json
{
  "source": "00aecd10",
  "target": "010a0980",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd14`](#insn-00aecd14)

~~~json
{
  "source": "00aecd14",
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
- 参照命令 [`00aecd24`](#insn-00aecd24)

~~~json
{
  "source": "00aecd24",
  "target": "00bde020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
