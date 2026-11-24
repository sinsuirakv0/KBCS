# 00bcdaac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccab8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccab8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-aeb76842fed595bb6d0a0142689e7304)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdaac",
  "name": "_ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb41f8a3bc7debb800db68b24f281b00be55975e8cc19a5a8fa42d69c187c7fb",
  "source_text_sha256": "eb41f8a3bc7debb800db68b24f281b00be55975e8cc19a5a8fa42d69c187c7fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdaac",
        "00bcdaef"
      ]
    ],
    "bytes_sha256": "c4733fde12471962b471359b2daee81a417f44eaed603e1b84591bc632005eea",
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

## 疑似コード / UTF-8 549 bytes

~~~c

long _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",param_3);
  }
  return DAT_011278b0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdaac"></a> `00bcdaac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdab0"></a> `00bcdab0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdab4"></a> `00bcdab4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdab8"></a> `00bcdab8` | `d3 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdabc"></a> `00bcdabc` | `68 5a 44 f9` | ldr x8,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdac0"></a> `00bcdac0` | `08 01 00 b5` | cbnz x8,0x00bcdae0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdac4"></a> `00bcdac4` | `43 b7 ff 90` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcdac8"></a> `00bcdac8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00bcdacc"></a> `00bcdacc` | `63 a4 33 91` | add x3,x3,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcdad0"></a> `00bcdad0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcdad4"></a> `00bcdad4` | `37 39 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdad8"></a> `00bcdad8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcdadc"></a> `00bcdadc` | `60 5a 04 f9` | str x0,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdae0"></a> `00bcdae0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdae4"></a> `00bcdae4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcdae8"></a> `00bcdae8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdaec"></a> `00bcdaec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdaac`](#insn-00bcdaac) 範囲 `[['00bcdaac', '00bcdac3']]`
  - `CONDITIONAL_JUMP` [`00bcdac0`](#insn-00bcdac0) → [`00bcdae0`](#insn-00bcdae0)
  - `FALL_THROUGH` [`00bcdac0`](#insn-00bcdac0) → [`00bcdac4`](#insn-00bcdac4)
- ブロック [`00bcdac4`](#insn-00bcdac4) 範囲 `[['00bcdac4', '00bcdadf']]`
  - `FALL_THROUGH` [`00bcdadc`](#insn-00bcdadc) → [`00bcdae0`](#insn-00bcdae0)
- ブロック [`00bcdae0`](#insn-00bcdae0) 範囲 `[['00bcdae0', '00bcdaef']]`

## 命令位置別の参照

- [`00bcdaac`](#insn-00bcdaac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdab0`](#insn-00bcdab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdabc`](#insn-00bcdabc) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdac0`](#insn-00bcdac0) → [`00bcdae0`](#insn-00bcdae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdacc`](#insn-00bcdacc) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdad4`](#insn-00bcdad4) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdadc`](#insn-00bcdadc) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdae0`](#insn-00bcdae0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdaac`](#insn-00bcdaac)

~~~json
{
  "source": "00bcdaac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdab0`](#insn-00bcdab0)

~~~json
{
  "source": "00bcdab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdabc`](#insn-00bcdabc)

~~~json
{
  "source": "00bcdabc",
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
- 参照命令 [`00bcdac0`](#insn-00bcdac0)

~~~json
{
  "source": "00bcdac0",
  "target": "00bcdae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdacc`](#insn-00bcdacc)

~~~json
{
  "source": "00bcdacc",
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
- 参照命令 [`00bcdad4`](#insn-00bcdad4)

~~~json
{
  "source": "00bcdad4",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdadc`](#insn-00bcdadc)

~~~json
{
  "source": "00bcdadc",
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
- 参照命令 [`00bcdae0`](#insn-00bcdae0)

~~~json
{
  "source": "00bcdae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
