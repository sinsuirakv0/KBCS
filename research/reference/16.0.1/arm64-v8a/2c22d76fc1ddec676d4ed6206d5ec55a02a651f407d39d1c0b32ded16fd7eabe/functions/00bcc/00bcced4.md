# 00bcced4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bccaac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-34bafbd4e25f16cae3d2f8358ec8872c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccf70`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccf70.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-e8add7a85af243993fbae24fe8f98070)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcced4",
  "name": "_ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e9b4525a4da721ef1081499118fa9636ba485d15d3d737f85cdfeef90dbd178",
  "source_text_sha256": "6e9b4525a4da721ef1081499118fa9636ba485d15d3d737f85cdfeef90dbd178",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcced4",
        "00bccf43"
      ]
    ],
    "bytes_sha256": "47335da907cd485424cdd5d34ceee03a44fb0e18fc72a6ca1f7afb15683af534",
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

- [00c5af10](../00c5a/00c5af10.md)
- [00c5af30](../00c5a/00c5af30.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 746 bytes

~~~c

void _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126818 == 0) {
    DAT_01126818 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126818,&PTR_s_<init>_00c91b80,2,&DAT_01126828,
             "com/google/firebase/auth/internal/cpp/JniIdTokenListener");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcced4"></a> `00bcced4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcced8"></a> `00bcced8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccedc"></a> `00bccedc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccee0"></a> `00bccee0` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccee4"></a> `00bccee4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bccee8"></a> `00bccee8` | `81 0e 44 f9` | ldr x1,[x20, #0x818] | `FALL_THROUGH`
<a id="insn-00bcceec"></a> `00bcceec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccef0"></a> `00bccef0` | `41 01 00 b5` | cbnz x1,0x00bccf18 | `CONDITIONAL_JUMP`
<a id="insn-00bccef4"></a> `00bccef4` | `e3 b6 ff d0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bccef8"></a> `00bccef8` | `63 28 26 91` | add x3,x3,#0x98a | `FALL_THROUGH`
<a id="insn-00bccefc"></a> `00bccefc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccf00"></a> `00bccf00` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bccf04"></a> `00bccf04` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bccf08"></a> `00bccf08` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bccf0c"></a> `00bccf0c` | `01 38 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bccf10"></a> `00bccf10` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bccf14"></a> `00bccf14` | `80 0e 04 f9` | str x0,[x20, #0x818] | `FALL_THROUGH`
<a id="insn-00bccf18"></a> `00bccf18` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccf1c"></a> `00bccf1c` | `22 06 00 b0` | adrp x2,0xc91000 | `FALL_THROUGH`
<a id="insn-00bccf20"></a> `00bccf20` | `c4 2a 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccf24"></a> `00bccf24` | `e5 b6 ff d0` | adrp x5,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bccf28"></a> `00bccf28` | `42 00 2e 91` | add x2,x2,#0xb80 | `FALL_THROUGH`
<a id="insn-00bccf2c"></a> `00bccf2c` | `84 a0 20 91` | add x4,x4,#0x828 | `FALL_THROUGH`
<a id="insn-00bccf30"></a> `00bccf30` | `a5 28 26 91` | add x5,x5,#0x98a | `FALL_THROUGH`
<a id="insn-00bccf34"></a> `00bccf34` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bccf38"></a> `00bccf38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccf3c"></a> `00bccf3c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccf40"></a> `00bccf40` | `fc 37 02 14` | b 0x00c5af30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcced4`](#insn-00bcced4) 範囲 `[['00bcced4', '00bccef3']]`
  - `CONDITIONAL_JUMP` [`00bccef0`](#insn-00bccef0) → [`00bccf18`](#insn-00bccf18)
  - `FALL_THROUGH` [`00bccef0`](#insn-00bccef0) → [`00bccef4`](#insn-00bccef4)
- ブロック [`00bccef4`](#insn-00bccef4) 範囲 `[['00bccef4', '00bccf17']]`
  - `FALL_THROUGH` [`00bccf14`](#insn-00bccf14) → [`00bccf18`](#insn-00bccf18)
- ブロック [`00bccf18`](#insn-00bccf18) 範囲 `[['00bccf18', '00bccf43']]`

## 命令位置別の参照

- [`00bcced4`](#insn-00bcced4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcced8`](#insn-00bcced8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccee8`](#insn-00bccee8) → `01126818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccef0`](#insn-00bccef0) → [`00bccf18`](#insn-00bccf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccef8`](#insn-00bccef8) → `002aa98a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccf0c`](#insn-00bccf0c) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bccf14`](#insn-00bccf14) → `01126818`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccf18`](#insn-00bccf18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf28`](#insn-00bccf28) → `00c91b80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bccf2c`](#insn-00bccf2c) → `01126828`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccf30`](#insn-00bccf30) → `002aa98a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccf40`](#insn-00bccf40) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcced4`](#insn-00bcced4)

~~~json
{
  "source": "00bcced4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcced8`](#insn-00bcced8)

~~~json
{
  "source": "00bcced8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccee8`](#insn-00bccee8)

~~~json
{
  "source": "00bccee8",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccef0`](#insn-00bccef0)

~~~json
{
  "source": "00bccef0",
  "target": "00bccf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccef8`](#insn-00bccef8)

~~~json
{
  "source": "00bccef8",
  "target": "002aa98a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa98a",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa98a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccf0c`](#insn-00bccf0c)

~~~json
{
  "source": "00bccf0c",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccf14`](#insn-00bccf14)

~~~json
{
  "source": "00bccf14",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccf18`](#insn-00bccf18)

~~~json
{
  "source": "00bccf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf28`](#insn-00bccf28)

~~~json
{
  "source": "00bccf28",
  "target": "00c91b80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91b80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bccf2c`](#insn-00bccf2c)

~~~json
{
  "source": "00bccf2c",
  "target": "01126828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccf30`](#insn-00bccf30)

~~~json
{
  "source": "00bccf30",
  "target": "002aa98a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa98a",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa98a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccf40`](#insn-00bccf40)

~~~json
{
  "source": "00bccf40",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
