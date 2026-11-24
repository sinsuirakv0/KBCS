# 00bcda2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcca38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca38.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-a70e5bb68d6d52089e5617958472aa3d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcda2c",
  "name": "_ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d73a5b9d16031d14cb2ec468b14e433ea6b644b19be76c3220898145f05207ae",
  "source_text_sha256": "d73a5b9d16031d14cb2ec468b14e433ea6b644b19be76c3220898145f05207ae",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcda2c",
        "00bcda6b"
      ]
    ],
    "bytes_sha256": "05f6ec117cb9436ec82d1fac7741241018b7f3a3c1b6a677b3a1ea1e6d56dfcc",
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
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 458 bytes

~~~c

long _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_011278b0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcda2c"></a> `00bcda2c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcda30"></a> `00bcda30` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcda34"></a> `00bcda34` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcda38"></a> `00bcda38` | `d3 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcda3c"></a> `00bcda3c` | `68 5a 44 f9` | ldr x8,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcda40"></a> `00bcda40` | `e8 00 00 b5` | cbnz x8,0x00bcda5c | `CONDITIONAL_JUMP`
<a id="insn-00bcda44"></a> `00bcda44` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bcda48"></a> `00bcda48` | `43 b7 ff 90` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcda4c"></a> `00bcda4c` | `63 a4 33 91` | add x3,x3,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcda50"></a> `00bcda50` | `58 39 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcda54"></a> `00bcda54` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcda58"></a> `00bcda58` | `60 5a 04 f9` | str x0,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcda5c"></a> `00bcda5c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcda60"></a> `00bcda60` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcda64"></a> `00bcda64` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcda68"></a> `00bcda68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcda2c`](#insn-00bcda2c) 範囲 `[['00bcda2c', '00bcda43']]`
  - `CONDITIONAL_JUMP` [`00bcda40`](#insn-00bcda40) → [`00bcda5c`](#insn-00bcda5c)
  - `FALL_THROUGH` [`00bcda40`](#insn-00bcda40) → [`00bcda44`](#insn-00bcda44)
- ブロック [`00bcda44`](#insn-00bcda44) 範囲 `[['00bcda44', '00bcda5b']]`
  - `FALL_THROUGH` [`00bcda58`](#insn-00bcda58) → [`00bcda5c`](#insn-00bcda5c)
- ブロック [`00bcda5c`](#insn-00bcda5c) 範囲 `[['00bcda5c', '00bcda6b']]`

## 命令位置別の参照

- [`00bcda2c`](#insn-00bcda2c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda30`](#insn-00bcda30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda3c`](#insn-00bcda3c) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcda40`](#insn-00bcda40) → [`00bcda5c`](#insn-00bcda5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda4c`](#insn-00bcda4c) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcda50`](#insn-00bcda50) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcda58`](#insn-00bcda58) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcda5c`](#insn-00bcda5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcda2c`](#insn-00bcda2c)

~~~json
{
  "source": "00bcda2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda30`](#insn-00bcda30)

~~~json
{
  "source": "00bcda30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda3c`](#insn-00bcda3c)

~~~json
{
  "source": "00bcda3c",
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
- 参照命令 [`00bcda40`](#insn-00bcda40)

~~~json
{
  "source": "00bcda40",
  "target": "00bcda5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda4c`](#insn-00bcda4c)

~~~json
{
  "source": "00bcda4c",
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
- 参照命令 [`00bcda50`](#insn-00bcda50)

~~~json
{
  "source": "00bcda50",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcda58`](#insn-00bcda58)

~~~json
{
  "source": "00bcda58",
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
- 参照命令 [`00bcda5c`](#insn-00bcda5c)

~~~json
{
  "source": "00bcda5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
