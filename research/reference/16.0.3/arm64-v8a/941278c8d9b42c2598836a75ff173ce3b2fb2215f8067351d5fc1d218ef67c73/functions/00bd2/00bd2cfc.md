# 00bd2cfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd1d08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1d08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0082.md#compare-c0426595dd18ea1eb21c1c30116858f9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2cfc",
  "name": "_ZN8firebase4auth29invalid_credentials_exception14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5415799626dbbe73e62b500b2dd1afdb062c2dd6faf0979464be1199ccdc3b98",
  "source_text_sha256": "5415799626dbbe73e62b500b2dd1afdb062c2dd6faf0979464be1199ccdc3b98",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2cfc",
        "00bd2d6b"
      ]
    ],
    "bytes_sha256": "3ee844c0b973a82d8d5e95290b58dc69db56ce74d19824a24e0a970c629f08a5",
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
"%PG%com/google/firebase/auth/FirebaseAuthInvalidCredentialsException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 761 bytes

~~~c

void _ZN8firebase4auth29invalid_credentials_exception14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011279e8 == 0) {
    DAT_011279e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/FirebaseAuthInvalidCredentialsException",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_011279e8,&DAT_0030fe58,1,&DAT_011279f8,
             "com/google/firebase/auth/FirebaseAuthInvalidCredentialsException");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2cfc"></a> `00bd2cfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd2d00"></a> `00bd2d00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2d04"></a> `00bd2d04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd2d08"></a> `00bd2d08` | `b4 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd2d0c"></a> `00bd2d0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bd2d10"></a> `00bd2d10` | `81 f6 44 f9` | ldr x1,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd2d14"></a> `00bd2d14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd2d18"></a> `00bd2d18` | `41 01 00 b5` | cbnz x1,0x00bd2d40 | `CONDITIONAL_JUMP`
<a id="insn-00bd2d1c"></a> `00bd2d1c` | `23 b7 ff f0` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bd2d20"></a> `00bd2d20` | `63 60 34 91` | add x3,x3,#0xd18 | `FALL_THROUGH`
<a id="insn-00bd2d24"></a> `00bd2d24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd2d28"></a> `00bd2d28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bd2d2c"></a> `00bd2d2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd2d30"></a> `00bd2d30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd2d34"></a> `00bd2d34` | `9f 24 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2d38"></a> `00bd2d38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bd2d3c"></a> `00bd2d3c` | `80 f6 04 f9` | str x0,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd2d40"></a> `00bd2d40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2d44"></a> `00bd2d44` | `e2 b9 ff b0` | adrp x2,0x30f000 | `FALL_THROUGH`
<a id="insn-00bd2d48"></a> `00bd2d48` | `a4 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd2d4c"></a> `00bd2d4c` | `25 b7 ff f0` | adrp x5,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bd2d50"></a> `00bd2d50` | `42 60 39 91` | add x2,x2,#0xe58 | `FALL_THROUGH`
<a id="insn-00bd2d54"></a> `00bd2d54` | `84 e0 27 91` | add x4,x4,#0x9f8 | `FALL_THROUGH`
<a id="insn-00bd2d58"></a> `00bd2d58` | `a5 60 34 91` | add x5,x5,#0xd18 | `FALL_THROUGH`
<a id="insn-00bd2d5c"></a> `00bd2d5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2d60"></a> `00bd2d60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd2d64"></a> `00bd2d64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2d68"></a> `00bd2d68` | `9a 24 02 14` | b 0x00c5bfd0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2cfc`](#insn-00bd2cfc) 範囲 `[['00bd2cfc', '00bd2d1b']]`
  - `CONDITIONAL_JUMP` [`00bd2d18`](#insn-00bd2d18) → [`00bd2d40`](#insn-00bd2d40)
  - `FALL_THROUGH` [`00bd2d18`](#insn-00bd2d18) → [`00bd2d1c`](#insn-00bd2d1c)
- ブロック [`00bd2d1c`](#insn-00bd2d1c) 範囲 `[['00bd2d1c', '00bd2d3f']]`
  - `FALL_THROUGH` [`00bd2d3c`](#insn-00bd2d3c) → [`00bd2d40`](#insn-00bd2d40)
- ブロック [`00bd2d40`](#insn-00bd2d40) 範囲 `[['00bd2d40', '00bd2d6b']]`

## 命令位置別の参照

- [`00bd2cfc`](#insn-00bd2cfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d00`](#insn-00bd2d00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d10`](#insn-00bd2d10) → `011279e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2d18`](#insn-00bd2d18) → [`00bd2d40`](#insn-00bd2d40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d20`](#insn-00bd2d20) → `002b9d18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2d34`](#insn-00bd2d34) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d3c`](#insn-00bd2d3c) → `011279e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2d40`](#insn-00bd2d40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d50`](#insn-00bd2d50) → `0030fe58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d54`](#insn-00bd2d54) → `011279f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d58`](#insn-00bd2d58) → `002b9d18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2d68`](#insn-00bd2d68) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2cfc`](#insn-00bd2cfc)

~~~json
{
  "source": "00bd2cfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d00`](#insn-00bd2d00)

~~~json
{
  "source": "00bd2d00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d10`](#insn-00bd2d10)

~~~json
{
  "source": "00bd2d10",
  "target": "011279e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011279e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2d18`](#insn-00bd2d18)

~~~json
{
  "source": "00bd2d18",
  "target": "00bd2d40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d20`](#insn-00bd2d20)

~~~json
{
  "source": "00bd2d20",
  "target": "002b9d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9d14",
  "offset": 4,
  "size": 69,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002b9d14",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd2d34`](#insn-00bd2d34)

~~~json
{
  "source": "00bd2d34",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2d3c`](#insn-00bd2d3c)

~~~json
{
  "source": "00bd2d3c",
  "target": "011279e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011279e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2d40`](#insn-00bd2d40)

~~~json
{
  "source": "00bd2d40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d50`](#insn-00bd2d50)

~~~json
{
  "source": "00bd2d50",
  "target": "0030fe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d54`](#insn-00bd2d54)

~~~json
{
  "source": "00bd2d54",
  "target": "011279f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d58`](#insn-00bd2d58)

~~~json
{
  "source": "00bd2d58",
  "target": "002b9d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9d14",
  "offset": 4,
  "size": 69,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002b9d14",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd2d68`](#insn-00bd2d68)

~~~json
{
  "source": "00bd2d68",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
