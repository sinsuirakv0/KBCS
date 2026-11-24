# 00bde5fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdd608`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd608.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-2837c3def7b5d1b55878d47dd83651e0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bde5fc",
  "name": "_ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52560c4f479f46361746b8f655d7b8b472533f873d66d53d8fc3c0d21a491759",
  "source_text_sha256": "52560c4f479f46361746b8f655d7b8b472533f873d66d53d8fc3c0d21a491759",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bde5fc",
        "00bde63f"
      ]
    ],
    "bytes_sha256": "2b5395b438face6e073b360a4d181b741793329a15d3e07b718bad5fbfda6f57",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserInfo"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 437 bytes

~~~c

long _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127e70 == 0) {
    DAT_01127e70 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/UserInfo",0);
  }
  return DAT_01127e70;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bde5fc"></a> `00bde5fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bde600"></a> `00bde600` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde604"></a> `00bde604` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bde608"></a> `00bde608` | `53 2a 00 b0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bde60c"></a> `00bde60c` | `68 3a 47 f9` | ldr x8,[x19, #0xe70] | `FALL_THROUGH`
<a id="insn-00bde610"></a> `00bde610` | `08 01 00 b5` | cbnz x8,0x00bde630 | `CONDITIONAL_JUMP`
<a id="insn-00bde614"></a> `00bde614` | `83 b6 ff f0` | adrp x3,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bde618"></a> `00bde618` | `63 dc 1f 91` | add x3,x3,#0x7f7 | `FALL_THROUGH`
<a id="insn-00bde61c"></a> `00bde61c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bde620"></a> `00bde620` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bde624"></a> `00bde624` | `63 f6 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bde628"></a> `00bde628` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bde62c"></a> `00bde62c` | `60 3a 07 f9` | str x0,[x19, #0xe70] | `FALL_THROUGH`
<a id="insn-00bde630"></a> `00bde630` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde634"></a> `00bde634` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bde638"></a> `00bde638` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bde63c"></a> `00bde63c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bde5fc`](#insn-00bde5fc) 範囲 `[['00bde5fc', '00bde613']]`
  - `CONDITIONAL_JUMP` [`00bde610`](#insn-00bde610) → [`00bde630`](#insn-00bde630)
  - `FALL_THROUGH` [`00bde610`](#insn-00bde610) → [`00bde614`](#insn-00bde614)
- ブロック [`00bde614`](#insn-00bde614) 範囲 `[['00bde614', '00bde62f']]`
  - `FALL_THROUGH` [`00bde62c`](#insn-00bde62c) → [`00bde630`](#insn-00bde630)
- ブロック [`00bde630`](#insn-00bde630) 範囲 `[['00bde630', '00bde63f']]`

## 命令位置別の参照

- [`00bde5fc`](#insn-00bde5fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde600`](#insn-00bde600) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde60c`](#insn-00bde60c) → `01127e70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde610`](#insn-00bde610) → [`00bde630`](#insn-00bde630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde618`](#insn-00bde618) → `002b17f7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde624`](#insn-00bde624) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bde62c`](#insn-00bde62c) → `01127e70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde630`](#insn-00bde630) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bde5fc`](#insn-00bde5fc)

~~~json
{
  "source": "00bde5fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde600`](#insn-00bde600)

~~~json
{
  "source": "00bde600",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde60c`](#insn-00bde60c)

~~~json
{
  "source": "00bde60c",
  "target": "01127e70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde610`](#insn-00bde610)

~~~json
{
  "source": "00bde610",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde618`](#insn-00bde618)

~~~json
{
  "source": "00bde618",
  "target": "002b17f7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b17f3",
  "offset": 4,
  "size": 38,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002b17f3",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bde624`](#insn-00bde624)

~~~json
{
  "source": "00bde624",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde62c`](#insn-00bde62c)

~~~json
{
  "source": "00bde62c",
  "target": "01127e70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde630`](#insn-00bde630)

~~~json
{
  "source": "00bde630",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
