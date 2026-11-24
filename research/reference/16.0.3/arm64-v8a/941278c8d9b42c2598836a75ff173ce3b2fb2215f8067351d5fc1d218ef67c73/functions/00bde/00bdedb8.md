# 00bdedb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdddc4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-b9af46344420b71a5bf8188f4c8b4383)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdedb8",
  "name": "_ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "249c37bf7efd91d005bdf89cd4b9381284d5c28dd4ceafb9c1406838f5e134d3",
  "source_text_sha256": "249c37bf7efd91d005bdf89cd4b9381284d5c28dd4ceafb9c1406838f5e134d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdedb8",
        "00bdee27"
      ]
    ],
    "bytes_sha256": "2e50c36e2e2ed805c591792fdbdc20a9a5b236ab0a667bccc63ca0ff1b0d06c1",
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

- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 745 bytes

~~~c

void _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127ee8 == 0) {
    DAT_01127ee8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01127ee8,&PTR_s_<init>_00c938d8,4,&DAT_01127ef8,
             "com/google/firebase/auth/UserProfileChangeRequest$Builder");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdedb8"></a> `00bdedb8` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdedbc"></a> `00bdedbc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdedc0"></a> `00bdedc0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdedc4"></a> `00bdedc4` | `54 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdedc8"></a> `00bdedc8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdedcc"></a> `00bdedcc` | `81 76 47 f9` | ldr x1,[x20, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdedd0"></a> `00bdedd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdedd4"></a> `00bdedd4` | `41 01 00 b5` | cbnz x1,0x00bdedfc | `CONDITIONAL_JUMP`
<a id="insn-00bdedd8"></a> `00bdedd8` | `63 b6 ff f0` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdeddc"></a> `00bdeddc` | `63 e4 13 91` | add x3,x3,#0x4f9 | `FALL_THROUGH`
<a id="insn-00bdede0"></a> `00bdede0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdede4"></a> `00bdede4` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdede8"></a> `00bdede8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdedec"></a> `00bdedec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdedf0"></a> `00bdedf0` | `70 f4 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdedf4"></a> `00bdedf4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdedf8"></a> `00bdedf8` | `80 76 07 f9` | str x0,[x20, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdedfc"></a> `00bdedfc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdee00"></a> `00bdee00` | `a2 05 00 b0` | adrp x2,0xc93000 | `FALL_THROUGH`
<a id="insn-00bdee04"></a> `00bdee04` | `44 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdee08"></a> `00bdee08` | `65 b6 ff f0` | adrp x5,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdee0c"></a> `00bdee0c` | `42 60 23 91` | add x2,x2,#0x8d8 | `FALL_THROUGH`
<a id="insn-00bdee10"></a> `00bdee10` | `84 e0 3b 91` | add x4,x4,#0xef8 | `FALL_THROUGH`
<a id="insn-00bdee14"></a> `00bdee14` | `a5 e4 13 91` | add x5,x5,#0x4f9 | `FALL_THROUGH`
<a id="insn-00bdee18"></a> `00bdee18` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00bdee1c"></a> `00bdee1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdee20"></a> `00bdee20` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdee24"></a> `00bdee24` | `6b f4 01 14` | b 0x00c5bfd0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdedb8`](#insn-00bdedb8) 範囲 `[['00bdedb8', '00bdedd7']]`
  - `CONDITIONAL_JUMP` [`00bdedd4`](#insn-00bdedd4) → [`00bdedfc`](#insn-00bdedfc)
  - `FALL_THROUGH` [`00bdedd4`](#insn-00bdedd4) → [`00bdedd8`](#insn-00bdedd8)
- ブロック [`00bdedd8`](#insn-00bdedd8) 範囲 `[['00bdedd8', '00bdedfb']]`
  - `FALL_THROUGH` [`00bdedf8`](#insn-00bdedf8) → [`00bdedfc`](#insn-00bdedfc)
- ブロック [`00bdedfc`](#insn-00bdedfc) 範囲 `[['00bdedfc', '00bdee27']]`

## 命令位置別の参照

- [`00bdedb8`](#insn-00bdedb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedbc`](#insn-00bdedbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedcc`](#insn-00bdedcc) → `01127ee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdedd4`](#insn-00bdedd4) → [`00bdedfc`](#insn-00bdedfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeddc`](#insn-00bdeddc) → `002ad4f9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdedf0`](#insn-00bdedf0) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdedf8`](#insn-00bdedf8) → `01127ee8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdedfc`](#insn-00bdedfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee0c`](#insn-00bdee0c) → `00c938d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdee10`](#insn-00bdee10) → `01127ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdee14`](#insn-00bdee14) → `002ad4f9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdee24`](#insn-00bdee24) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdedb8`](#insn-00bdedb8)

~~~json
{
  "source": "00bdedb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedbc`](#insn-00bdedbc)

~~~json
{
  "source": "00bdedbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedcc`](#insn-00bdedcc)

~~~json
{
  "source": "00bdedcc",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdedd4`](#insn-00bdedd4)

~~~json
{
  "source": "00bdedd4",
  "target": "00bdedfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeddc`](#insn-00bdeddc)

~~~json
{
  "source": "00bdeddc",
  "target": "002ad4f9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad4f5",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad4f5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdedf0`](#insn-00bdedf0)

~~~json
{
  "source": "00bdedf0",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdedf8`](#insn-00bdedf8)

~~~json
{
  "source": "00bdedf8",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdedfc`](#insn-00bdedfc)

~~~json
{
  "source": "00bdedfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee0c`](#insn-00bdee0c)

~~~json
{
  "source": "00bdee0c",
  "target": "00c938d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c938d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdee10`](#insn-00bdee10)

~~~json
{
  "source": "00bdee10",
  "target": "01127ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ef8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdee14`](#insn-00bdee14)

~~~json
{
  "source": "00bdee14",
  "target": "002ad4f9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad4f5",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad4f5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdee24`](#insn-00bdee24)

~~~json
{
  "source": "00bdee24",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
