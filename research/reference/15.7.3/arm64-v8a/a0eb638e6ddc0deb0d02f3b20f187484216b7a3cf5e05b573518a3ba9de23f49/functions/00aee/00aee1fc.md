# 00aee1fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aee134`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee134.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-767807b94f1c0ca301554d204598f45d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aee240`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee240.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-80481a15140f1919ecdd24b0913d0cd2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aee1fc",
  "name": "_ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a75b76cc5ad61eb931ace26c15c93aa3663b798962420f9506a581bf371db45d",
  "source_text_sha256": "a75b76cc5ad61eb931ace26c15c93aa3663b798962420f9506a581bf371db45d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aee1fc",
        "00aee26b"
      ]
    ],
    "bytes_sha256": "cca187fbc8997e936be59c252bd69695e060e4eb1f439154581aeae8332befc6",
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
"java/lang/Object"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 607 bytes

~~~c

void _ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a48 == 0) {
    DAT_010a0a48 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Object",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0a48,&PTR_s_toString_00c10620,1,&DAT_010a0a58,"java/lang/Object");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aee1fc"></a> `00aee1fc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aee200"></a> `00aee200` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee204"></a> `00aee204` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aee208"></a> `00aee208` | `94 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee20c"></a> `00aee20c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aee210"></a> `00aee210` | `81 26 45 f9` | ldr x1,[x20, #0xa48] | `FALL_THROUGH`
<a id="insn-00aee214"></a> `00aee214` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aee218"></a> `00aee218` | `41 01 00 b5` | cbnz x1,0x00aee240 | `CONDITIONAL_JUMP`
<a id="insn-00aee21c"></a> `00aee21c` | `63 bd ff f0` | adrp x3,0x29d000 | `FALL_THROUGH`
<a id="insn-00aee220"></a> `00aee220` | `63 b0 35 91` | add x3,x3,#0xd6c | `FALL_THROUGH`
<a id="insn-00aee224"></a> `00aee224` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee228"></a> `00aee228` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aee22c"></a> `00aee22c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aee230"></a> `00aee230` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aee234"></a> `00aee234` | `83 bf 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aee238"></a> `00aee238` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aee23c"></a> `00aee23c` | `80 26 05 f9` | str x0,[x20, #0xa48] | `FALL_THROUGH`
<a id="insn-00aee240"></a> `00aee240` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee244"></a> `00aee244` | `02 09 00 d0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aee248"></a> `00aee248` | `84 2d 00 d0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee24c"></a> `00aee24c` | `65 bd ff f0` | adrp x5,0x29d000 | `FALL_THROUGH`
<a id="insn-00aee250"></a> `00aee250` | `42 80 18 91` | add x2,x2,#0x620 | `FALL_THROUGH`
<a id="insn-00aee254"></a> `00aee254` | `84 60 29 91` | add x4,x4,#0xa58 | `FALL_THROUGH`
<a id="insn-00aee258"></a> `00aee258` | `a5 b0 35 91` | add x5,x5,#0xd6c | `FALL_THROUGH`
<a id="insn-00aee25c"></a> `00aee25c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aee260"></a> `00aee260` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee264"></a> `00aee264` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aee268"></a> `00aee268` | `7e bf 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aee1fc`](#insn-00aee1fc) 範囲 `[['00aee1fc', '00aee21b']]`
  - `CONDITIONAL_JUMP` [`00aee218`](#insn-00aee218) → [`00aee240`](#insn-00aee240)
  - `FALL_THROUGH` [`00aee218`](#insn-00aee218) → [`00aee21c`](#insn-00aee21c)
- ブロック [`00aee21c`](#insn-00aee21c) 範囲 `[['00aee21c', '00aee23f']]`
  - `FALL_THROUGH` [`00aee23c`](#insn-00aee23c) → [`00aee240`](#insn-00aee240)
- ブロック [`00aee240`](#insn-00aee240) 範囲 `[['00aee240', '00aee26b']]`

## 命令位置別の参照

- [`00aee1fc`](#insn-00aee1fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee200`](#insn-00aee200) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee210`](#insn-00aee210) → `010a0a48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee218`](#insn-00aee218) → [`00aee240`](#insn-00aee240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee220`](#insn-00aee220) → `0029dd6c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aee234`](#insn-00aee234) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aee23c`](#insn-00aee23c) → `010a0a48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee240`](#insn-00aee240) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee250`](#insn-00aee250) → `00c10620`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aee254`](#insn-00aee254) → `010a0a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee258`](#insn-00aee258) → `0029dd6c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aee268`](#insn-00aee268) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aee1fc`](#insn-00aee1fc)

~~~json
{
  "source": "00aee1fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee200`](#insn-00aee200)

~~~json
{
  "source": "00aee200",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee210`](#insn-00aee210)

~~~json
{
  "source": "00aee210",
  "target": "010a0a48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee218`](#insn-00aee218)

~~~json
{
  "source": "00aee218",
  "target": "00aee240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee220`](#insn-00aee220)

~~~json
{
  "source": "00aee220",
  "target": "0029dd6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029dd6c",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4f626a65637400",
  "capture_start": "0029dd6c",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aee234`](#insn-00aee234)

~~~json
{
  "source": "00aee234",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aee23c`](#insn-00aee23c)

~~~json
{
  "source": "00aee23c",
  "target": "010a0a48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee240`](#insn-00aee240)

~~~json
{
  "source": "00aee240",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee250`](#insn-00aee250)

~~~json
{
  "source": "00aee250",
  "target": "00c10620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aee254`](#insn-00aee254)

~~~json
{
  "source": "00aee254",
  "target": "010a0a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee258`](#insn-00aee258)

~~~json
{
  "source": "00aee258",
  "target": "0029dd6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029dd6c",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4f626a65637400",
  "capture_start": "0029dd6c",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aee268`](#insn-00aee268)

~~~json
{
  "source": "00aee268",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
