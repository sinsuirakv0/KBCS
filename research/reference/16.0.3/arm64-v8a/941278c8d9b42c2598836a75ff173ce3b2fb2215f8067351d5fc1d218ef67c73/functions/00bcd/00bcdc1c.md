# 00bcdc1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccc28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccc28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-a69130371b12d58fdc5f134e976181a4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdc1c",
  "name": "_ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5f9e6ec1da3372e679310581bc8bd950819dd3081eee0a23a424bc616b90c073",
  "source_text_sha256": "5f9e6ec1da3372e679310581bc8bd950819dd3081eee0a23a424bc616b90c073",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdc1c",
        "00bcdc8b"
      ]
    ],
    "bytes_sha256": "7c64d4687c6a0d79cb782e97c52d759b709a0b753eac1b13d30fd3b1baee57fd",
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
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 934 bytes

~~~c

void _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bcdc20 to 00ccdc37 has its CatchHandler @ 00bcf968 */
                    /* try { // try from 00bcdc38 to 00ccdc93 has its CatchHandler @ 00bcd634 */
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_011278b0,&PTR_s_<init>_00c92bf0,2,&DAT_011278c0,
             "com/google/firebase/auth/internal/cpp/JniAuthStateListener");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdc1c"></a> `00bcdc1c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdc20"></a> `00bcdc20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdc24"></a> `00bcdc24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdc28"></a> `00bcdc28` | `d4 2a 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdc2c"></a> `00bcdc2c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bcdc30"></a> `00bcdc30` | `81 5a 44 f9` | ldr x1,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdc34"></a> `00bcdc34` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcdc38"></a> `00bcdc38` | `41 01 00 b5` | cbnz x1,0x00bcdc60 | `CONDITIONAL_JUMP`
<a id="insn-00bcdc3c"></a> `00bcdc3c` | `43 b7 ff 90` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcdc40"></a> `00bcdc40` | `63 a4 33 91` | add x3,x3,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcdc44"></a> `00bcdc44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdc48"></a> `00bcdc48` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bcdc4c"></a> `00bcdc4c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcdc50"></a> `00bcdc50` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcdc54"></a> `00bcdc54` | `d7 38 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc58"></a> `00bcdc58` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bcdc5c"></a> `00bcdc5c` | `80 5a 04 f9` | str x0,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdc60"></a> `00bcdc60` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdc64"></a> `00bcdc64` | `22 06 00 b0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bcdc68"></a> `00bcdc68` | `c4 2a 00 d0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdc6c"></a> `00bcdc6c` | `45 b7 ff 90` | adrp x5,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcdc70"></a> `00bcdc70` | `42 c0 2f 91` | add x2,x2,#0xbf0 | `FALL_THROUGH`
<a id="insn-00bcdc74"></a> `00bcdc74` | `84 00 23 91` | add x4,x4,#0x8c0 | `FALL_THROUGH`
<a id="insn-00bcdc78"></a> `00bcdc78` | `a5 a4 33 91` | add x5,x5,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcdc7c"></a> `00bcdc7c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bcdc80"></a> `00bcdc80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdc84"></a> `00bcdc84` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdc88"></a> `00bcdc88` | `d2 38 02 14` | b 0x00c5bfd0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdc1c`](#insn-00bcdc1c) 範囲 `[['00bcdc1c', '00bcdc1f']]`
  - `FALL_THROUGH` [`00bcdc1c`](#insn-00bcdc1c) → [`00bcdc20`](#insn-00bcdc20)
- ブロック [`00bcdc20`](#insn-00bcdc20) 範囲 `[['00bcdc20', '00bcdc37']]`
  - `FALL_THROUGH` [`00bcdc34`](#insn-00bcdc34) → [`00bcdc38`](#insn-00bcdc38)
- ブロック [`00bcdc38`](#insn-00bcdc38) 範囲 `[['00bcdc38', '00bcdc3b']]`
  - `CONDITIONAL_JUMP` [`00bcdc38`](#insn-00bcdc38) → [`00bcdc60`](#insn-00bcdc60)
  - `FALL_THROUGH` [`00bcdc38`](#insn-00bcdc38) → [`00bcdc3c`](#insn-00bcdc3c)
- ブロック [`00bcdc3c`](#insn-00bcdc3c) 範囲 `[['00bcdc3c', '00bcdc5f']]`
  - `FALL_THROUGH` [`00bcdc5c`](#insn-00bcdc5c) → [`00bcdc60`](#insn-00bcdc60)
- ブロック [`00bcdc60`](#insn-00bcdc60) 範囲 `[['00bcdc60', '00bcdc8b']]`

## 命令位置別の参照

- [`00bcdc1c`](#insn-00bcdc1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc20`](#insn-00bcdc20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc30`](#insn-00bcdc30) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdc38`](#insn-00bcdc38) → [`00bcdc60`](#insn-00bcdc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc40`](#insn-00bcdc40) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdc54`](#insn-00bcdc54) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc5c`](#insn-00bcdc5c) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdc60`](#insn-00bcdc60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc70`](#insn-00bcdc70) → `00c92bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcdc74`](#insn-00bcdc74) → `011278c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdc78`](#insn-00bcdc78) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdc88`](#insn-00bcdc88) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdc1c`](#insn-00bcdc1c)

~~~json
{
  "source": "00bcdc1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc20`](#insn-00bcdc20)

~~~json
{
  "source": "00bcdc20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc30`](#insn-00bcdc30)

~~~json
{
  "source": "00bcdc30",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdc38`](#insn-00bcdc38)

~~~json
{
  "source": "00bcdc38",
  "target": "00bcdc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc40`](#insn-00bcdc40)

~~~json
{
  "source": "00bcdc40",
  "target": "002b5ce9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5ce9",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5ce9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcdc54`](#insn-00bcdc54)

~~~json
{
  "source": "00bcdc54",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc5c`](#insn-00bcdc5c)

~~~json
{
  "source": "00bcdc5c",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdc60`](#insn-00bcdc60)

~~~json
{
  "source": "00bcdc60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc70`](#insn-00bcdc70)

~~~json
{
  "source": "00bcdc70",
  "target": "00c92bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92bf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcdc74`](#insn-00bcdc74)

~~~json
{
  "source": "00bcdc74",
  "target": "011278c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdc78`](#insn-00bcdc78)

~~~json
{
  "source": "00bcdc78",
  "target": "002b5ce9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5ce9",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5ce9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcdc88`](#insn-00bcdc88)

~~~json
{
  "source": "00bcdc88",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
