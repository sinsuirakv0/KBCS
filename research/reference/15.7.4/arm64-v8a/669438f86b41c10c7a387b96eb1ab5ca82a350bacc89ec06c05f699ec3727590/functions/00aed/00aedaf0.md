# 00aedaf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedaac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedaac.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-52061bc9526a74e20225d69405663b5a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4d874`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d874.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-88b37f79c93ae820af7496704f248d50)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedaf0",
  "name": "_ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67122c64638a5a3f5c6424c9d82bee4bf089939e8491e4ad36773d7eb62bad83",
  "source_text_sha256": "67122c64638a5a3f5c6424c9d82bee4bf089939e8491e4ad36773d7eb62bad83",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedaf0",
        "00aedb5f"
      ]
    ],
    "bytes_sha256": "5f1f06788c7d7040f963d6a74296595f8d182e0d16b25f3a12b0d699bd2f1d72",
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

- [00bde090](../00bde/00bde090.md)
- [00bde0b0](../00bde/00bde0b0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Throwable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 835 bytes

~~~c

void _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aedaf8 to 00bedb33 has its CatchHandler @ 00af1b1c */
  if (DAT_010a0a30 == 0) {
    DAT_010a0a30 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
                    /* try { // try from 00aedb34 to 00beed6b has its CatchHandler @ 00aeae0c */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0a30,&PTR_s_getLocalizedMessage_00c105f8,3,&DAT_010a0a40,
             "java/lang/Throwable");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedaf0"></a> `00aedaf0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedaf4"></a> `00aedaf4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedaf8"></a> `00aedaf8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedafc"></a> `00aedafc` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedb00"></a> `00aedb00` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aedb04"></a> `00aedb04` | `81 1a 45 f9` | ldr x1,[x20, #0xa30] | `FALL_THROUGH`
<a id="insn-00aedb08"></a> `00aedb08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedb0c"></a> `00aedb0c` | `41 01 00 b5` | cbnz x1,0x00aedb34 | `CONDITIONAL_JUMP`
<a id="insn-00aedb10"></a> `00aedb10` | `c3 bd ff f0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aedb14"></a> `00aedb14` | `63 90 32 91` | add x3,x3,#0xca4 | `FALL_THROUGH`
<a id="insn-00aedb18"></a> `00aedb18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedb1c"></a> `00aedb1c` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aedb20"></a> `00aedb20` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedb24"></a> `00aedb24` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aedb28"></a> `00aedb28` | `5a c1 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb2c"></a> `00aedb2c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aedb30"></a> `00aedb30` | `80 1a 05 f9` | str x0,[x20, #0xa30] | `FALL_THROUGH`
<a id="insn-00aedb34"></a> `00aedb34` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedb38"></a> `00aedb38` | `02 09 00 f0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aedb3c"></a> `00aedb3c` | `84 2d 00 f0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedb40"></a> `00aedb40` | `c5 bd ff f0` | adrp x5,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aedb44"></a> `00aedb44` | `42 e0 17 91` | add x2,x2,#0x5f8 | `FALL_THROUGH`
<a id="insn-00aedb48"></a> `00aedb48` | `84 00 29 91` | add x4,x4,#0xa40 | `FALL_THROUGH`
<a id="insn-00aedb4c"></a> `00aedb4c` | `a5 90 32 91` | add x5,x5,#0xca4 | `FALL_THROUGH`
<a id="insn-00aedb50"></a> `00aedb50` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-00aedb54"></a> `00aedb54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedb58"></a> `00aedb58` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedb5c"></a> `00aedb5c` | `55 c1 03 14` | b 0x00bde0b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedaf0`](#insn-00aedaf0) 範囲 `[['00aedaf0', '00aedaf7']]`
  - `FALL_THROUGH` [`00aedaf4`](#insn-00aedaf4) → [`00aedaf8`](#insn-00aedaf8)
- ブロック [`00aedaf8`](#insn-00aedaf8) 範囲 `[['00aedaf8', '00aedb0f']]`
  - `CONDITIONAL_JUMP` [`00aedb0c`](#insn-00aedb0c) → [`00aedb34`](#insn-00aedb34)
  - `FALL_THROUGH` [`00aedb0c`](#insn-00aedb0c) → [`00aedb10`](#insn-00aedb10)
- ブロック [`00aedb10`](#insn-00aedb10) 範囲 `[['00aedb10', '00aedb33']]`
  - `FALL_THROUGH` [`00aedb30`](#insn-00aedb30) → [`00aedb34`](#insn-00aedb34)
- ブロック [`00aedb34`](#insn-00aedb34) 範囲 `[['00aedb34', '00aedb5f']]`

## 命令位置別の参照

- [`00aedaf0`](#insn-00aedaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedaf4`](#insn-00aedaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb04`](#insn-00aedb04) → `010a0a30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedb0c`](#insn-00aedb0c) → [`00aedb34`](#insn-00aedb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb14`](#insn-00aedb14) → `002a8ca4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedb28`](#insn-00aedb28) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aedb30`](#insn-00aedb30) → `010a0a30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedb34`](#insn-00aedb34) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb44`](#insn-00aedb44) → `00c105f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aedb48`](#insn-00aedb48) → `010a0a40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedb4c`](#insn-00aedb4c) → `002a8ca4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedb5c`](#insn-00aedb5c) → [`00bde0b0`](../00bde/00bde0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedaf0`](#insn-00aedaf0)

~~~json
{
  "source": "00aedaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedaf4`](#insn-00aedaf4)

~~~json
{
  "source": "00aedaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb04`](#insn-00aedb04)

~~~json
{
  "source": "00aedb04",
  "target": "010a0a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedb0c`](#insn-00aedb0c)

~~~json
{
  "source": "00aedb0c",
  "target": "00aedb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb14`](#insn-00aedb14)

~~~json
{
  "source": "00aedb14",
  "target": "002a8ca4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8ca4",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002a8ca4",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedb28`](#insn-00aedb28)

~~~json
{
  "source": "00aedb28",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb30`](#insn-00aedb30)

~~~json
{
  "source": "00aedb30",
  "target": "010a0a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedb34`](#insn-00aedb34)

~~~json
{
  "source": "00aedb34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb44`](#insn-00aedb44)

~~~json
{
  "source": "00aedb44",
  "target": "00c105f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c105f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedb48`](#insn-00aedb48)

~~~json
{
  "source": "00aedb48",
  "target": "010a0a40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedb4c`](#insn-00aedb4c)

~~~json
{
  "source": "00aedb4c",
  "target": "002a8ca4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8ca4",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002a8ca4",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedb5c`](#insn-00aedb5c)

~~~json
{
  "source": "00aedb5c",
  "target": "00bde0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
