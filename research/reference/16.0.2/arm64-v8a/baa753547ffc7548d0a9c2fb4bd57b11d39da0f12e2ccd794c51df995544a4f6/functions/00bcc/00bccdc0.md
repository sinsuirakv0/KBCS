# 00bccdc0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccd24`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-97890a588425e90afada7be11e8b1747)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcddb4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcddb4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-408b95e3ced48c9c88e71eb2a465c154)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccdc0",
  "name": "_ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b61102fe00c1412a8d9d5344382ef5bdb110eb4b7d7e91bb5d4ef3bb79066387",
  "source_text_sha256": "b61102fe00c1412a8d9d5344382ef5bdb110eb4b7d7e91bb5d4ef3bb79066387",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccdc0",
        "00bccdff"
      ]
    ],
    "bytes_sha256": "7ff9d955470bb73b45d0a6d0b642e657ee6c9e06ac2e0e604b72485a93197f8f",
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

- [00c5afe0](../00c5a/00c5afe0.md)

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
  if (DAT_01126918 == 0) {
    DAT_01126918 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126918;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccdc0"></a> `00bccdc0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccdc4"></a> `00bccdc4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccdc8"></a> `00bccdc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccdcc"></a> `00bccdcc` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccdd0"></a> `00bccdd0` | `68 8e 44 f9` | ldr x8,[x19, #0x918] | `FALL_THROUGH`
<a id="insn-00bccdd4"></a> `00bccdd4` | `e8 00 00 b5` | cbnz x8,0x00bccdf0 | `CONDITIONAL_JUMP`
<a id="insn-00bccdd8"></a> `00bccdd8` | `e3 b6 ff d0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bccddc"></a> `00bccddc` | `63 b8 24 91` | add x3,x3,#0x92e | `FALL_THROUGH`
<a id="insn-00bccde0"></a> `00bccde0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bccde4"></a> `00bccde4` | `7f 38 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccde8"></a> `00bccde8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bccdec"></a> `00bccdec` | `60 8e 04 f9` | str x0,[x19, #0x918] | `FALL_THROUGH`
<a id="insn-00bccdf0"></a> `00bccdf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccdf4"></a> `00bccdf4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bccdf8"></a> `00bccdf8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccdfc"></a> `00bccdfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccdc0`](#insn-00bccdc0) 範囲 `[['00bccdc0', '00bccdd7']]`
  - `CONDITIONAL_JUMP` [`00bccdd4`](#insn-00bccdd4) → [`00bccdf0`](#insn-00bccdf0)
  - `FALL_THROUGH` [`00bccdd4`](#insn-00bccdd4) → [`00bccdd8`](#insn-00bccdd8)
- ブロック [`00bccdd8`](#insn-00bccdd8) 範囲 `[['00bccdd8', '00bccdef']]`
  - `FALL_THROUGH` [`00bccdec`](#insn-00bccdec) → [`00bccdf0`](#insn-00bccdf0)
- ブロック [`00bccdf0`](#insn-00bccdf0) 範囲 `[['00bccdf0', '00bccdff']]`

## 命令位置別の参照

- [`00bccdc0`](#insn-00bccdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccdc4`](#insn-00bccdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccdd0`](#insn-00bccdd0) → `01126918`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccdd4`](#insn-00bccdd4) → [`00bccdf0`](#insn-00bccdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccddc`](#insn-00bccddc) → `002aa92e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccde4`](#insn-00bccde4) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bccdec`](#insn-00bccdec) → `01126918`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccdf0`](#insn-00bccdf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccdc0`](#insn-00bccdc0)

~~~json
{
  "source": "00bccdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccdc4`](#insn-00bccdc4)

~~~json
{
  "source": "00bccdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccdd0`](#insn-00bccdd0)

~~~json
{
  "source": "00bccdd0",
  "target": "01126918",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126918",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccdd4`](#insn-00bccdd4)

~~~json
{
  "source": "00bccdd4",
  "target": "00bccdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccddc`](#insn-00bccddc)

~~~json
{
  "source": "00bccddc",
  "target": "002aa92e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa92e",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa92e",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccde4`](#insn-00bccde4)

~~~json
{
  "source": "00bccde4",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccdec`](#insn-00bccdec)

~~~json
{
  "source": "00bccdec",
  "target": "01126918",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126918",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccdf0`](#insn-00bccdf0)

~~~json
{
  "source": "00bccdf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
