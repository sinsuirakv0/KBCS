# 00bcddb4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccdc0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccdc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-408b95e3ced48c9c88e71eb2a465c154)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcddb4",
  "name": "_ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a696389b9af75a63cb1e7e68d98675f6bc04108b8ab096ceed67ddf806f4d87e",
  "source_text_sha256": "a696389b9af75a63cb1e7e68d98675f6bc04108b8ab096ceed67ddf806f4d87e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcddb4",
        "00bcddf3"
      ]
    ],
    "bytes_sha256": "3589a6d026eeda3d07772bf59ffb2c6d39c7dcb386ecd8e9aafdef2689f5aa32",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
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
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 441 bytes

~~~c

long _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_011278d8 == 0) {
    DAT_011278d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_011278d8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcddb4"></a> `00bcddb4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcddb8"></a> `00bcddb8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcddbc"></a> `00bcddbc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcddc0"></a> `00bcddc0` | `d3 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcddc4"></a> `00bcddc4` | `68 6e 44 f9` | ldr x8,[x19, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bcddc8"></a> `00bcddc8` | `e8 00 00 b5` | cbnz x8,0x00bcdde4 | `CONDITIONAL_JUMP`
<a id="insn-00bcddcc"></a> `00bcddcc` | `e3 b6 ff b0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bcddd0"></a> `00bcddd0` | `63 ec 27 91` | add x3,x3,#0x9fb | `FALL_THROUGH`
<a id="insn-00bcddd4"></a> `00bcddd4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcddd8"></a> `00bcddd8` | `76 38 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdddc"></a> `00bcdddc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcdde0"></a> `00bcdde0` | `60 6e 04 f9` | str x0,[x19, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bcdde4"></a> `00bcdde4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdde8"></a> `00bcdde8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcddec"></a> `00bcddec` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcddf0"></a> `00bcddf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcddb4`](#insn-00bcddb4) 範囲 `[['00bcddb4', '00bcddcb']]`
  - `CONDITIONAL_JUMP` [`00bcddc8`](#insn-00bcddc8) → [`00bcdde4`](#insn-00bcdde4)
  - `FALL_THROUGH` [`00bcddc8`](#insn-00bcddc8) → [`00bcddcc`](#insn-00bcddcc)
- ブロック [`00bcddcc`](#insn-00bcddcc) 範囲 `[['00bcddcc', '00bcdde3']]`
  - `FALL_THROUGH` [`00bcdde0`](#insn-00bcdde0) → [`00bcdde4`](#insn-00bcdde4)
- ブロック [`00bcdde4`](#insn-00bcdde4) 範囲 `[['00bcdde4', '00bcddf3']]`

## 命令位置別の参照

- [`00bcddb4`](#insn-00bcddb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddb8`](#insn-00bcddb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddc4`](#insn-00bcddc4) → `011278d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcddc8`](#insn-00bcddc8) → [`00bcdde4`](#insn-00bcdde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddd0`](#insn-00bcddd0) → `002aa9fb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcddd8`](#insn-00bcddd8) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdde0`](#insn-00bcdde0) → `011278d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdde4`](#insn-00bcdde4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcddb4`](#insn-00bcddb4)

~~~json
{
  "source": "00bcddb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddb8`](#insn-00bcddb8)

~~~json
{
  "source": "00bcddb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddc4`](#insn-00bcddc4)

~~~json
{
  "source": "00bcddc4",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcddc8`](#insn-00bcddc8)

~~~json
{
  "source": "00bcddc8",
  "target": "00bcdde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddd0`](#insn-00bcddd0)

~~~json
{
  "source": "00bcddd0",
  "target": "002aa9fb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa9fb",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa9fb",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcddd8`](#insn-00bcddd8)

~~~json
{
  "source": "00bcddd8",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdde0`](#insn-00bcdde0)

~~~json
{
  "source": "00bcdde0",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdde4`](#insn-00bcdde4)

~~~json
{
  "source": "00bcdde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
