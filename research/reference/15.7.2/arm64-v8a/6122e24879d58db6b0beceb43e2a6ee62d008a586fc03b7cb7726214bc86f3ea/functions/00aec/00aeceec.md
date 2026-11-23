# 00aeceec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecfb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-37bf33b33588a143b5298182f815119b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeceec",
  "name": "_ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb607c5c64be3697534b81a67304c303bce48e3268806769de7a442c9b8bc19e",
  "source_text_sha256": "fb607c5c64be3697534b81a67304c303bce48e3268806769de7a442c9b8bc19e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeceec",
        "00aecf5b"
      ]
    ],
    "bytes_sha256": "f99c0402283de27f3fa3667950d05e9900fbd1e6b2875b9b469cabf40373ff55",
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

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 598 bytes

~~~c

void _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08c8 == 0) {
    DAT_010a08c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a08c8,&PTR_s_iterator_00c10498,1,&DAT_010a08d8,"java/util/Set");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeceec"></a> `00aeceec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecef0"></a> `00aecef0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecef4"></a> `00aecef4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecef8"></a> `00aecef8` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecefc"></a> `00aecefc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aecf00"></a> `00aecf00` | `81 66 44 f9` | ldr x1,[x20, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecf04"></a> `00aecf04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecf08"></a> `00aecf08` | `41 01 00 b5` | cbnz x1,0x00aecf30 | `CONDITIONAL_JUMP`
<a id="insn-00aecf0c"></a> `00aecf0c` | `83 bd ff f0` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00aecf10"></a> `00aecf10` | `63 c8 3c 91` | add x3,x3,#0xf32 | `FALL_THROUGH`
<a id="insn-00aecf14"></a> `00aecf14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecf18"></a> `00aecf18` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aecf1c"></a> `00aecf1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aecf20"></a> `00aecf20` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aecf24"></a> `00aecf24` | `1b c4 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aecf28"></a> `00aecf28` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aecf2c"></a> `00aecf2c` | `80 66 04 f9` | str x0,[x20, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecf30"></a> `00aecf30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecf34"></a> `00aecf34` | `22 09 00 90` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aecf38"></a> `00aecf38` | `a4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecf3c"></a> `00aecf3c` | `85 bd ff f0` | adrp x5,0x29f000 | `FALL_THROUGH`
<a id="insn-00aecf40"></a> `00aecf40` | `42 60 12 91` | add x2,x2,#0x498 | `FALL_THROUGH`
<a id="insn-00aecf44"></a> `00aecf44` | `84 60 23 91` | add x4,x4,#0x8d8 | `FALL_THROUGH`
<a id="insn-00aecf48"></a> `00aecf48` | `a5 c8 3c 91` | add x5,x5,#0xf32 | `FALL_THROUGH`
<a id="insn-00aecf4c"></a> `00aecf4c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aecf50"></a> `00aecf50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecf54"></a> `00aecf54` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecf58"></a> `00aecf58` | `16 c4 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeceec`](#insn-00aeceec) 範囲 `[['00aeceec', '00aecf0b']]`
  - `CONDITIONAL_JUMP` [`00aecf08`](#insn-00aecf08) → [`00aecf30`](#insn-00aecf30)
  - `FALL_THROUGH` [`00aecf08`](#insn-00aecf08) → [`00aecf0c`](#insn-00aecf0c)
- ブロック [`00aecf0c`](#insn-00aecf0c) 範囲 `[['00aecf0c', '00aecf2f']]`
  - `FALL_THROUGH` [`00aecf2c`](#insn-00aecf2c) → [`00aecf30`](#insn-00aecf30)
- ブロック [`00aecf30`](#insn-00aecf30) 範囲 `[['00aecf30', '00aecf5b']]`

## 命令位置別の参照

- [`00aeceec`](#insn-00aeceec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecef0`](#insn-00aecef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf00`](#insn-00aecf00) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecf08`](#insn-00aecf08) → [`00aecf30`](#insn-00aecf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf10`](#insn-00aecf10) → `0029ff32`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecf24`](#insn-00aecf24) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aecf2c`](#insn-00aecf2c) → `010a08c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecf30`](#insn-00aecf30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf40`](#insn-00aecf40) → `00c10498`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aecf44`](#insn-00aecf44) → `010a08d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecf48`](#insn-00aecf48) → `0029ff32`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecf58`](#insn-00aecf58) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeceec`](#insn-00aeceec)

~~~json
{
  "source": "00aeceec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecef0`](#insn-00aecef0)

~~~json
{
  "source": "00aecef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf00`](#insn-00aecf00)

~~~json
{
  "source": "00aecf00",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecf08`](#insn-00aecf08)

~~~json
{
  "source": "00aecf08",
  "target": "00aecf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf10`](#insn-00aecf10)

~~~json
{
  "source": "00aecf10",
  "target": "0029ff32",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff32",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "0029ff32",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecf24`](#insn-00aecf24)

~~~json
{
  "source": "00aecf24",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecf2c`](#insn-00aecf2c)

~~~json
{
  "source": "00aecf2c",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecf30`](#insn-00aecf30)

~~~json
{
  "source": "00aecf30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf40`](#insn-00aecf40)

~~~json
{
  "source": "00aecf40",
  "target": "00c10498",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10498",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecf44`](#insn-00aecf44)

~~~json
{
  "source": "00aecf44",
  "target": "010a08d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecf48`](#insn-00aecf48)

~~~json
{
  "source": "00aecf48",
  "target": "0029ff32",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff32",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "0029ff32",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecf58`](#insn-00aecf58)

~~~json
{
  "source": "00aecf58",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
