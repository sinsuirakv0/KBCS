# 00aec4bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aec3f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec3f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-f3a63e1e076620154114106c2474659e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aec500`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-c94191c7f0358356ddead34d0110cc90)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec4bc",
  "name": "_ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ffdb3100fd459c48e3eb4e18786c791c703d9b880853494d5174f7f21f52b36",
  "source_text_sha256": "7ffdb3100fd459c48e3eb4e18786c791c703d9b880853494d5174f7f21f52b36",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec4bc",
        "00aec52b"
      ]
    ],
    "bytes_sha256": "982221cbe4335088aad14148ef0a14c4a44b9ec001e82133f9115febf4eb3ab6",
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
"java/lang/Long"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 606 bytes

~~~c

void _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0910 == 0) {
    DAT_010a0910 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Long",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0910,&PTR_s_<init>_00c104b8,2,&DAT_010a0920,"java/lang/Long");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec4bc"></a> `00aec4bc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aec4c0"></a> `00aec4c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec4c4"></a> `00aec4c4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aec4c8"></a> `00aec4c8` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec4cc"></a> `00aec4cc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aec4d0"></a> `00aec4d0` | `81 8a 44 f9` | ldr x1,[x20, #0x910] | `FALL_THROUGH`
<a id="insn-00aec4d4"></a> `00aec4d4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aec4d8"></a> `00aec4d8` | `41 01 00 b5` | cbnz x1,0x00aec500 | `CONDITIONAL_JUMP`
<a id="insn-00aec4dc"></a> `00aec4dc` | `c3 bd ff f0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aec4e0"></a> `00aec4e0` | `63 58 35 91` | add x3,x3,#0xd56 | `FALL_THROUGH`
<a id="insn-00aec4e4"></a> `00aec4e4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec4e8"></a> `00aec4e8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aec4ec"></a> `00aec4ec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aec4f0"></a> `00aec4f0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aec4f4"></a> `00aec4f4` | `d3 c6 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aec4f8"></a> `00aec4f8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aec4fc"></a> `00aec4fc` | `80 8a 04 f9` | str x0,[x20, #0x910] | `FALL_THROUGH`
<a id="insn-00aec500"></a> `00aec500` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec504"></a> `00aec504` | `22 09 00 90` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aec508"></a> `00aec508` | `a4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec50c"></a> `00aec50c` | `c5 bd ff f0` | adrp x5,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aec510"></a> `00aec510` | `42 e0 12 91` | add x2,x2,#0x4b8 | `FALL_THROUGH`
<a id="insn-00aec514"></a> `00aec514` | `84 80 24 91` | add x4,x4,#0x920 | `FALL_THROUGH`
<a id="insn-00aec518"></a> `00aec518` | `a5 58 35 91` | add x5,x5,#0xd56 | `FALL_THROUGH`
<a id="insn-00aec51c"></a> `00aec51c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aec520"></a> `00aec520` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec524"></a> `00aec524` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec528"></a> `00aec528` | `ce c6 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec4bc`](#insn-00aec4bc) 範囲 `[['00aec4bc', '00aec4db']]`
  - `CONDITIONAL_JUMP` [`00aec4d8`](#insn-00aec4d8) → [`00aec500`](#insn-00aec500)
  - `FALL_THROUGH` [`00aec4d8`](#insn-00aec4d8) → [`00aec4dc`](#insn-00aec4dc)
- ブロック [`00aec4dc`](#insn-00aec4dc) 範囲 `[['00aec4dc', '00aec4ff']]`
  - `FALL_THROUGH` [`00aec4fc`](#insn-00aec4fc) → [`00aec500`](#insn-00aec500)
- ブロック [`00aec500`](#insn-00aec500) 範囲 `[['00aec500', '00aec52b']]`

## 命令位置別の参照

- [`00aec4bc`](#insn-00aec4bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4c0`](#insn-00aec4c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4d0`](#insn-00aec4d0) → `010a0910`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec4d8`](#insn-00aec4d8) → [`00aec500`](#insn-00aec500) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4e0`](#insn-00aec4e0) → `002a7d56`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec4f4`](#insn-00aec4f4) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aec4fc`](#insn-00aec4fc) → `010a0910`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec500`](#insn-00aec500) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec510`](#insn-00aec510) → `00c104b8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aec514`](#insn-00aec514) → `010a0920`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec518`](#insn-00aec518) → `002a7d56`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec528`](#insn-00aec528) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec4bc`](#insn-00aec4bc)

~~~json
{
  "source": "00aec4bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4c0`](#insn-00aec4c0)

~~~json
{
  "source": "00aec4c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4d0`](#insn-00aec4d0)

~~~json
{
  "source": "00aec4d0",
  "target": "010a0910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0910",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec4d8`](#insn-00aec4d8)

~~~json
{
  "source": "00aec4d8",
  "target": "00aec500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4e0`](#insn-00aec4e0)

~~~json
{
  "source": "00aec4e0",
  "target": "002a7d56",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7d56",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4c6f6e6700",
  "capture_start": "002a7d56",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aec4f4`](#insn-00aec4f4)

~~~json
{
  "source": "00aec4f4",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec4fc`](#insn-00aec4fc)

~~~json
{
  "source": "00aec4fc",
  "target": "010a0910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0910",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec500`](#insn-00aec500)

~~~json
{
  "source": "00aec500",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec510`](#insn-00aec510)

~~~json
{
  "source": "00aec510",
  "target": "00c104b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c104b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aec514`](#insn-00aec514)

~~~json
{
  "source": "00aec514",
  "target": "010a0920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec518`](#insn-00aec518)

~~~json
{
  "source": "00aec518",
  "target": "002a7d56",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7d56",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4c6f6e6700",
  "capture_start": "002a7d56",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aec528`](#insn-00aec528)

~~~json
{
  "source": "00aec528",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
