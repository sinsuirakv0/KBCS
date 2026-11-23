# 00aecfb4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeceec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeceec.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-37bf33b33588a143b5298182f815119b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aecff8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecff8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-e1cf4a8fa4ed193e87dba13e7e0c8b3a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecfb4",
  "name": "_ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12b72df829ba056551d279b88bc7be10dd4af87a171595b9f7eb2f86b8b0d940",
  "source_text_sha256": "12b72df829ba056551d279b88bc7be10dd4af87a171595b9f7eb2f86b8b0d940",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecfb4",
        "00aed023"
      ]
    ],
    "bytes_sha256": "3726a5d680635a4970940b4df81313912c9cbe2a6d2bef3510c7929eb3777a33",
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
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 598 bytes

~~~c

void _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0988 == 0) {
    DAT_010a0988 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0988,&PTR_s_iterator_00c10548,1,&DAT_010a0998,"java/util/Set");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecfb4"></a> `00aecfb4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecfb8"></a> `00aecfb8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecfbc"></a> `00aecfbc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecfc0"></a> `00aecfc0` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecfc4"></a> `00aecfc4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aecfc8"></a> `00aecfc8` | `81 c6 44 f9` | ldr x1,[x20, #0x988] | `FALL_THROUGH`
<a id="insn-00aecfcc"></a> `00aecfcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecfd0"></a> `00aecfd0` | `41 01 00 b5` | cbnz x1,0x00aecff8 | `CONDITIONAL_JUMP`
<a id="insn-00aecfd4"></a> `00aecfd4` | `83 bd ff f0` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00aecfd8"></a> `00aecfd8` | `63 fc 3e 91` | add x3,x3,#0xfbf | `FALL_THROUGH`
<a id="insn-00aecfdc"></a> `00aecfdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecfe0"></a> `00aecfe0` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aecfe4"></a> `00aecfe4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aecfe8"></a> `00aecfe8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aecfec"></a> `00aecfec` | `15 c4 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aecff0"></a> `00aecff0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aecff4"></a> `00aecff4` | `80 c6 04 f9` | str x0,[x20, #0x988] | `FALL_THROUGH`
<a id="insn-00aecff8"></a> `00aecff8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecffc"></a> `00aecffc` | `22 09 00 90` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aed000"></a> `00aed000` | `84 2d 00 f0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed004"></a> `00aed004` | `85 bd ff d0` | adrp x5,0x29f000 | `FALL_THROUGH`
<a id="insn-00aed008"></a> `00aed008` | `42 20 15 91` | add x2,x2,#0x548 | `FALL_THROUGH`
<a id="insn-00aed00c"></a> `00aed00c` | `84 60 26 91` | add x4,x4,#0x998 | `FALL_THROUGH`
<a id="insn-00aed010"></a> `00aed010` | `a5 fc 3e 91` | add x5,x5,#0xfbf | `FALL_THROUGH`
<a id="insn-00aed014"></a> `00aed014` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aed018"></a> `00aed018` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed01c"></a> `00aed01c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed020"></a> `00aed020` | `10 c4 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecfb4`](#insn-00aecfb4) 範囲 `[['00aecfb4', '00aecfd3']]`
  - `CONDITIONAL_JUMP` [`00aecfd0`](#insn-00aecfd0) → [`00aecff8`](#insn-00aecff8)
  - `FALL_THROUGH` [`00aecfd0`](#insn-00aecfd0) → [`00aecfd4`](#insn-00aecfd4)
- ブロック [`00aecfd4`](#insn-00aecfd4) 範囲 `[['00aecfd4', '00aecff7']]`
  - `FALL_THROUGH` [`00aecff4`](#insn-00aecff4) → [`00aecff8`](#insn-00aecff8)
- ブロック [`00aecff8`](#insn-00aecff8) 範囲 `[['00aecff8', '00aed023']]`

## 命令位置別の参照

- [`00aecfb4`](#insn-00aecfb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecfb8`](#insn-00aecfb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecfc8`](#insn-00aecfc8) → `010a0988`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecfd0`](#insn-00aecfd0) → [`00aecff8`](#insn-00aecff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecfd8`](#insn-00aecfd8) → `0029ffbf`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecfec`](#insn-00aecfec) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aecff4`](#insn-00aecff4) → `010a0988`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecff8`](#insn-00aecff8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed008`](#insn-00aed008) → `00c10548`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aed00c`](#insn-00aed00c) → `010a0998`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed010`](#insn-00aed010) → `0029ffbf`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aed020`](#insn-00aed020) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecfb4`](#insn-00aecfb4)

~~~json
{
  "source": "00aecfb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecfb8`](#insn-00aecfb8)

~~~json
{
  "source": "00aecfb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecfc8`](#insn-00aecfc8)

~~~json
{
  "source": "00aecfc8",
  "target": "010a0988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0988",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecfd0`](#insn-00aecfd0)

~~~json
{
  "source": "00aecfd0",
  "target": "00aecff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecfd8`](#insn-00aecfd8)

~~~json
{
  "source": "00aecfd8",
  "target": "0029ffbf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ffbf",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "0029ffbf",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecfec`](#insn-00aecfec)

~~~json
{
  "source": "00aecfec",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecff4`](#insn-00aecff4)

~~~json
{
  "source": "00aecff4",
  "target": "010a0988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0988",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecff8`](#insn-00aecff8)

~~~json
{
  "source": "00aecff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed008`](#insn-00aed008)

~~~json
{
  "source": "00aed008",
  "target": "00c10548",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10548",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aed00c`](#insn-00aed00c)

~~~json
{
  "source": "00aed00c",
  "target": "010a0998",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0998",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed010`](#insn-00aed010)

~~~json
{
  "source": "00aed010",
  "target": "0029ffbf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ffbf",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "0029ffbf",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aed020`](#insn-00aed020)

~~~json
{
  "source": "00aed020",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
