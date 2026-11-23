# 00aeb1ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeb274`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb274.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-fe76539d5ba20e60b7fe094223113509)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeb1ac",
  "name": "_ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26a601e3a61544d234144c63e30e6582f863f1c6848a879b0051b3a7555304a6",
  "source_text_sha256": "26a601e3a61544d234144c63e30e6582f863f1c6848a879b0051b3a7555304a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeb1ac",
        "00aeb21b"
      ]
    ],
    "bytes_sha256": "982e0e7c91217010b55250e6bcb5ffc1714e599c812f7f86cff199cda305b855",
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
"java/lang/Integer"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 809 bytes

~~~c

void _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0770 == 0) {
                    /* try { // try from 00aeb1cc to 00beb207 has its CatchHandler @ 00af1a20 */
    DAT_010a0770 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Integer",0);
  }
                    /* try { // try from 00aeb208 to 00beb21b has its CatchHandler @ 00af18c0 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0770,&PTR_s_<init>_00c102d0,2,&DAT_010a0780,"java/lang/Integer");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeb1ac"></a> `00aeb1ac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeb1b0"></a> `00aeb1b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb1b4"></a> `00aeb1b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeb1b8"></a> `00aeb1b8` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb1bc"></a> `00aeb1bc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aeb1c0"></a> `00aeb1c0` | `81 ba 43 f9` | ldr x1,[x20, #0x770] | `FALL_THROUGH`
<a id="insn-00aeb1c4"></a> `00aeb1c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeb1c8"></a> `00aeb1c8` | `41 01 00 b5` | cbnz x1,0x00aeb1f0 | `CONDITIONAL_JUMP`
<a id="insn-00aeb1cc"></a> `00aeb1cc` | `63 bd ff b0` | adrp x3,0x298000 | `FALL_THROUGH`
<a id="insn-00aeb1d0"></a> `00aeb1d0` | `63 48 18 91` | add x3,x3,#0x612 | `FALL_THROUGH`
<a id="insn-00aeb1d4"></a> `00aeb1d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb1d8"></a> `00aeb1d8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeb1dc"></a> `00aeb1dc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeb1e0"></a> `00aeb1e0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeb1e4"></a> `00aeb1e4` | `6b cb 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb1e8"></a> `00aeb1e8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeb1ec"></a> `00aeb1ec` | `80 ba 03 f9` | str x0,[x20, #0x770] | `FALL_THROUGH`
<a id="insn-00aeb1f0"></a> `00aeb1f0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb1f4"></a> `00aeb1f4` | `22 09 00 b0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aeb1f8"></a> `00aeb1f8` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb1fc"></a> `00aeb1fc` | `65 bd ff b0` | adrp x5,0x298000 | `FALL_THROUGH`
<a id="insn-00aeb200"></a> `00aeb200` | `42 40 0b 91` | add x2,x2,#0x2d0 | `FALL_THROUGH`
<a id="insn-00aeb204"></a> `00aeb204` | `84 00 1e 91` | add x4,x4,#0x780 | `FALL_THROUGH`
<a id="insn-00aeb208"></a> `00aeb208` | `a5 48 18 91` | add x5,x5,#0x612 | `FALL_THROUGH`
<a id="insn-00aeb20c"></a> `00aeb20c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aeb210"></a> `00aeb210` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb214"></a> `00aeb214` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeb218"></a> `00aeb218` | `66 cb 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeb1ac`](#insn-00aeb1ac) 範囲 `[['00aeb1ac', '00aeb1cb']]`
  - `CONDITIONAL_JUMP` [`00aeb1c8`](#insn-00aeb1c8) → [`00aeb1f0`](#insn-00aeb1f0)
  - `FALL_THROUGH` [`00aeb1c8`](#insn-00aeb1c8) → [`00aeb1cc`](#insn-00aeb1cc)
- ブロック [`00aeb1cc`](#insn-00aeb1cc) 範囲 `[['00aeb1cc', '00aeb1ef']]`
  - `FALL_THROUGH` [`00aeb1ec`](#insn-00aeb1ec) → [`00aeb1f0`](#insn-00aeb1f0)
- ブロック [`00aeb1f0`](#insn-00aeb1f0) 範囲 `[['00aeb1f0', '00aeb207']]`
  - `FALL_THROUGH` [`00aeb204`](#insn-00aeb204) → [`00aeb208`](#insn-00aeb208)
- ブロック [`00aeb208`](#insn-00aeb208) 範囲 `[['00aeb208', '00aeb21b']]`

## 命令位置別の参照

- [`00aeb1ac`](#insn-00aeb1ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb1b0`](#insn-00aeb1b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb1c0`](#insn-00aeb1c0) → `010a0770`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb1c8`](#insn-00aeb1c8) → [`00aeb1f0`](#insn-00aeb1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb1d0`](#insn-00aeb1d0) → `00298612`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb1e4`](#insn-00aeb1e4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeb1ec`](#insn-00aeb1ec) → `010a0770`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb1f0`](#insn-00aeb1f0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb200`](#insn-00aeb200) → `00c102d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aeb204`](#insn-00aeb204) → `010a0780`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb208`](#insn-00aeb208) → `00298612`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb218`](#insn-00aeb218) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeb1ac`](#insn-00aeb1ac)

~~~json
{
  "source": "00aeb1ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb1b0`](#insn-00aeb1b0)

~~~json
{
  "source": "00aeb1b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb1c0`](#insn-00aeb1c0)

~~~json
{
  "source": "00aeb1c0",
  "target": "010a0770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0770",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb1c8`](#insn-00aeb1c8)

~~~json
{
  "source": "00aeb1c8",
  "target": "00aeb1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb1d0`](#insn-00aeb1d0)

~~~json
{
  "source": "00aeb1d0",
  "target": "00298612",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298612",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f496e746567657200",
  "capture_start": "00298612",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb1e4`](#insn-00aeb1e4)

~~~json
{
  "source": "00aeb1e4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb1ec`](#insn-00aeb1ec)

~~~json
{
  "source": "00aeb1ec",
  "target": "010a0770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0770",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb1f0`](#insn-00aeb1f0)

~~~json
{
  "source": "00aeb1f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb200`](#insn-00aeb200)

~~~json
{
  "source": "00aeb200",
  "target": "00c102d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c102d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeb204`](#insn-00aeb204)

~~~json
{
  "source": "00aeb204",
  "target": "010a0780",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb208`](#insn-00aeb208)

~~~json
{
  "source": "00aeb208",
  "target": "00298612",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298612",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f496e746567657200",
  "capture_start": "00298612",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb218`](#insn-00aeb218)

~~~json
{
  "source": "00aeb218",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
