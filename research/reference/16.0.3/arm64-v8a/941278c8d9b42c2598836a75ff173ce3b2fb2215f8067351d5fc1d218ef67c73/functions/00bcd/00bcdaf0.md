# 00bcdaf0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccafc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccafc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-624fd929d51a8fe2b6c4e1b628d3f6e1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdaf0",
  "name": "_ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64286d87977ec6eb99b347a841d6870299eba27b3e1b88cce9ed6a14d3a8da0f",
  "source_text_sha256": "64286d87977ec6eb99b347a841d6870299eba27b3e1b88cce9ed6a14d3a8da0f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdaf0",
        "00bcdb33"
      ]
    ],
    "bytes_sha256": "91f1810a2cc6eace66146db855d0cf77d147eaaa0c33f28daa646ae613e8063d",
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
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 497 bytes

~~~c

long _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
  return DAT_011278b0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdaf0"></a> `00bcdaf0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdaf4"></a> `00bcdaf4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdaf8"></a> `00bcdaf8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdafc"></a> `00bcdafc` | `d3 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdb00"></a> `00bcdb00` | `68 5a 44 f9` | ldr x8,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdb04"></a> `00bcdb04` | `08 01 00 b5` | cbnz x8,0x00bcdb24 | `CONDITIONAL_JUMP`
<a id="insn-00bcdb08"></a> `00bcdb08` | `43 b7 ff 90` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcdb0c"></a> `00bcdb0c` | `63 a4 33 91` | add x3,x3,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcdb10"></a> `00bcdb10` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcdb14"></a> `00bcdb14` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcdb18"></a> `00bcdb18` | `26 39 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb1c"></a> `00bcdb1c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcdb20"></a> `00bcdb20` | `60 5a 04 f9` | str x0,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdb24"></a> `00bcdb24` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdb28"></a> `00bcdb28` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcdb2c"></a> `00bcdb2c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdb30"></a> `00bcdb30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdaf0`](#insn-00bcdaf0) 範囲 `[['00bcdaf0', '00bcdb07']]`
  - `CONDITIONAL_JUMP` [`00bcdb04`](#insn-00bcdb04) → [`00bcdb24`](#insn-00bcdb24)
  - `FALL_THROUGH` [`00bcdb04`](#insn-00bcdb04) → [`00bcdb08`](#insn-00bcdb08)
- ブロック [`00bcdb08`](#insn-00bcdb08) 範囲 `[['00bcdb08', '00bcdb23']]`
  - `FALL_THROUGH` [`00bcdb20`](#insn-00bcdb20) → [`00bcdb24`](#insn-00bcdb24)
- ブロック [`00bcdb24`](#insn-00bcdb24) 範囲 `[['00bcdb24', '00bcdb33']]`

## 命令位置別の参照

- [`00bcdaf0`](#insn-00bcdaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdaf4`](#insn-00bcdaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb00`](#insn-00bcdb00) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdb04`](#insn-00bcdb04) → [`00bcdb24`](#insn-00bcdb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb0c`](#insn-00bcdb0c) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdb18`](#insn-00bcdb18) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb20`](#insn-00bcdb20) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdb24`](#insn-00bcdb24) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdaf0`](#insn-00bcdaf0)

~~~json
{
  "source": "00bcdaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdaf4`](#insn-00bcdaf4)

~~~json
{
  "source": "00bcdaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb00`](#insn-00bcdb00)

~~~json
{
  "source": "00bcdb00",
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
- 参照命令 [`00bcdb04`](#insn-00bcdb04)

~~~json
{
  "source": "00bcdb04",
  "target": "00bcdb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb0c`](#insn-00bcdb0c)

~~~json
{
  "source": "00bcdb0c",
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
- 参照命令 [`00bcdb18`](#insn-00bcdb18)

~~~json
{
  "source": "00bcdb18",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb20`](#insn-00bcdb20)

~~~json
{
  "source": "00bcdb20",
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
- 参照命令 [`00bcdb24`](#insn-00bcdb24)

~~~json
{
  "source": "00bcdb24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
