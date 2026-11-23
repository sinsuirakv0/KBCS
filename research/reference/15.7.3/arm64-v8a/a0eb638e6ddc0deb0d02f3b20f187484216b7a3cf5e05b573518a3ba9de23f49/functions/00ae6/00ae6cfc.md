# 00ae6cfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae6c34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6c34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0059.md#compare-0f5cd94db18507fa81a8f5da13b7ddd8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae6d40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0062.md#compare-f1ddee5be31ec8e2c1a6fc4f7585e387)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae6cfc",
  "name": "_ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ffb5b954a2dd3d1aeb86665cf8b0437af8db8da463eda00d7ba58ad13554818",
  "source_text_sha256": "7ffb5b954a2dd3d1aeb86665cf8b0437af8db8da463eda00d7ba58ad13554818",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae6cfc",
        "00ae6d6b"
      ]
    ],
    "bytes_sha256": "387253eb7881fab0b1891d37a86ad64a00e2dbbbe851aa83e87dfaf2d110a853",
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
"%PG%dalvik/system/DexClassLoader"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 945 bytes

~~~c

void _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00ae6d0c to 00be6d13 has its CatchHandler @ 00ae878c */
                    /* try { // try from 00ae6d14 to 00be6d27 has its CatchHandler @ 00ae89d4 */
  if (DAT_010a0480 == 0) {
    DAT_010a0480 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"dalvik/system/DexClassLoader",0);
  }
                    /* try { // try from 00ae6d40 to 00be6d47 has its CatchHandler @ 00ae89a0 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0480,&PTR_s_<init>_00c0fdc8,2,&DAT_010a0490,
             "dalvik/system/DexClassLoader");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae6cfc"></a> `00ae6cfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae6d00"></a> `00ae6d00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6d04"></a> `00ae6d04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae6d08"></a> `00ae6d08` | `d4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae6d0c"></a> `00ae6d0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ae6d10"></a> `00ae6d10` | `81 42 42 f9` | ldr x1,[x20, #0x480] | `FALL_THROUGH`
<a id="insn-00ae6d14"></a> `00ae6d14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae6d18"></a> `00ae6d18` | `41 01 00 b5` | cbnz x1,0x00ae6d40 | `CONDITIONAL_JUMP`
<a id="insn-00ae6d1c"></a> `00ae6d1c` | `03 be ff b0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ae6d20"></a> `00ae6d20` | `63 00 34 91` | add x3,x3,#0xd00 | `FALL_THROUGH`
<a id="insn-00ae6d24"></a> `00ae6d24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae6d28"></a> `00ae6d28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00ae6d2c"></a> `00ae6d2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae6d30"></a> `00ae6d30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae6d34"></a> `00ae6d34` | `c3 dc 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00ae6d38"></a> `00ae6d38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ae6d3c"></a> `00ae6d3c` | `80 42 02 f9` | str x0,[x20, #0x480] | `FALL_THROUGH`
<a id="insn-00ae6d40"></a> `00ae6d40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6d44"></a> `00ae6d44` | `42 09 00 b0` | adrp x2,0xc0f000 | `FALL_THROUGH`
<a id="insn-00ae6d48"></a> `00ae6d48` | `c4 2d 00 d0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae6d4c"></a> `00ae6d4c` | `05 be ff b0` | adrp x5,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ae6d50"></a> `00ae6d50` | `42 20 37 91` | add x2,x2,#0xdc8 | `FALL_THROUGH`
<a id="insn-00ae6d54"></a> `00ae6d54` | `84 40 12 91` | add x4,x4,#0x490 | `FALL_THROUGH`
<a id="insn-00ae6d58"></a> `00ae6d58` | `a5 00 34 91` | add x5,x5,#0xd00 | `FALL_THROUGH`
<a id="insn-00ae6d5c"></a> `00ae6d5c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00ae6d60"></a> `00ae6d60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae6d64"></a> `00ae6d64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae6d68"></a> `00ae6d68` | `be dc 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae6cfc`](#insn-00ae6cfc) 範囲 `[['00ae6cfc', '00ae6d0b']]`
  - `FALL_THROUGH` [`00ae6d08`](#insn-00ae6d08) → [`00ae6d0c`](#insn-00ae6d0c)
- ブロック [`00ae6d0c`](#insn-00ae6d0c) 範囲 `[['00ae6d0c', '00ae6d13']]`
  - `FALL_THROUGH` [`00ae6d10`](#insn-00ae6d10) → [`00ae6d14`](#insn-00ae6d14)
- ブロック [`00ae6d14`](#insn-00ae6d14) 範囲 `[['00ae6d14', '00ae6d1b']]`
  - `CONDITIONAL_JUMP` [`00ae6d18`](#insn-00ae6d18) → [`00ae6d40`](#insn-00ae6d40)
  - `FALL_THROUGH` [`00ae6d18`](#insn-00ae6d18) → [`00ae6d1c`](#insn-00ae6d1c)
- ブロック [`00ae6d1c`](#insn-00ae6d1c) 範囲 `[['00ae6d1c', '00ae6d3f']]`
  - `FALL_THROUGH` [`00ae6d3c`](#insn-00ae6d3c) → [`00ae6d40`](#insn-00ae6d40)
- ブロック [`00ae6d40`](#insn-00ae6d40) 範囲 `[['00ae6d40', '00ae6d6b']]`

## 命令位置別の参照

- [`00ae6cfc`](#insn-00ae6cfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6d00`](#insn-00ae6d00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6d10`](#insn-00ae6d10) → `010a0480`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6d18`](#insn-00ae6d18) → [`00ae6d40`](#insn-00ae6d40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6d20`](#insn-00ae6d20) → `002a7d00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae6d34`](#insn-00ae6d34) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00ae6d3c`](#insn-00ae6d3c) → `010a0480`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6d40`](#insn-00ae6d40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6d50`](#insn-00ae6d50) → `00c0fdc8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ae6d54`](#insn-00ae6d54) → `010a0490`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6d58`](#insn-00ae6d58) → `002a7d00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae6d68`](#insn-00ae6d68) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae6cfc`](#insn-00ae6cfc)

~~~json
{
  "source": "00ae6cfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6d00`](#insn-00ae6d00)

~~~json
{
  "source": "00ae6d00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6d10`](#insn-00ae6d10)

~~~json
{
  "source": "00ae6d10",
  "target": "010a0480",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0480",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6d18`](#insn-00ae6d18)

~~~json
{
  "source": "00ae6d18",
  "target": "00ae6d40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6d20`](#insn-00ae6d20)

~~~json
{
  "source": "00ae6d20",
  "target": "002a7d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7cfc",
  "offset": 4,
  "size": 33,
  "datatype": "string",
  "bytes": "2550472564616c76696b2f73797374656d2f446578436c6173734c6f61646572",
  "capture_start": "002a7cfc",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae6d34`](#insn-00ae6d34)

~~~json
{
  "source": "00ae6d34",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae6d3c`](#insn-00ae6d3c)

~~~json
{
  "source": "00ae6d3c",
  "target": "010a0480",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0480",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6d40`](#insn-00ae6d40)

~~~json
{
  "source": "00ae6d40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6d50`](#insn-00ae6d50)

~~~json
{
  "source": "00ae6d50",
  "target": "00c0fdc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0fdc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae6d54`](#insn-00ae6d54)

~~~json
{
  "source": "00ae6d54",
  "target": "010a0490",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0490",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6d58`](#insn-00ae6d58)

~~~json
{
  "source": "00ae6d58",
  "target": "002a7d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7cfc",
  "offset": 4,
  "size": 33,
  "datatype": "string",
  "bytes": "2550472564616c76696b2f73797374656d2f446578436c6173734c6f61646572",
  "capture_start": "002a7cfc",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae6d68`](#insn-00ae6d68)

~~~json
{
  "source": "00ae6d68",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
