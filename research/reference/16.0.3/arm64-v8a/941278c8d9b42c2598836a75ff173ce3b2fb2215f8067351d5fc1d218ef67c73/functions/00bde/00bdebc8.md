# 00bdebc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddbd4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddbd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-35a5ca1d7cef5bf5e43e2f9cfc0097b9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdebc8",
  "name": "_ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb3b10e39c4986a0daa31af564fbcc97cd2773755a2d9cdb1eb5d8b430219fe4",
  "source_text_sha256": "eb3b10e39c4986a0daa31af564fbcc97cd2773755a2d9cdb1eb5d8b430219fe4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdebc8",
        "00bdec07"
      ]
    ],
    "bytes_sha256": "275ae1be269341a2ae2c052e42fd137f10f72d303565e9ee8d9ae76b81f46c1c",
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
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 465 bytes

~~~c

long _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01127ee8 == 0) {
    DAT_01127ee8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01127ee8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdebc8"></a> `00bdebc8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdebcc"></a> `00bdebcc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdebd0"></a> `00bdebd0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdebd4"></a> `00bdebd4` | `53 2a 00 b0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdebd8"></a> `00bdebd8` | `68 76 47 f9` | ldr x8,[x19, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdebdc"></a> `00bdebdc` | `e8 00 00 b5` | cbnz x8,0x00bdebf8 | `CONDITIONAL_JUMP`
<a id="insn-00bdebe0"></a> `00bdebe0` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bdebe4"></a> `00bdebe4` | `63 b6 ff f0` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdebe8"></a> `00bdebe8` | `63 e4 13 91` | add x3,x3,#0x4f9 | `FALL_THROUGH`
<a id="insn-00bdebec"></a> `00bdebec` | `f1 f4 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdebf0"></a> `00bdebf0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdebf4"></a> `00bdebf4` | `60 76 07 f9` | str x0,[x19, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdebf8"></a> `00bdebf8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdebfc"></a> `00bdebfc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdec00"></a> `00bdec00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdec04"></a> `00bdec04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdebc8`](#insn-00bdebc8) 範囲 `[['00bdebc8', '00bdebdf']]`
  - `CONDITIONAL_JUMP` [`00bdebdc`](#insn-00bdebdc) → [`00bdebf8`](#insn-00bdebf8)
  - `FALL_THROUGH` [`00bdebdc`](#insn-00bdebdc) → [`00bdebe0`](#insn-00bdebe0)
- ブロック [`00bdebe0`](#insn-00bdebe0) 範囲 `[['00bdebe0', '00bdebf7']]`
  - `FALL_THROUGH` [`00bdebf4`](#insn-00bdebf4) → [`00bdebf8`](#insn-00bdebf8)
- ブロック [`00bdebf8`](#insn-00bdebf8) 範囲 `[['00bdebf8', '00bdec07']]`

## 命令位置別の参照

- [`00bdebc8`](#insn-00bdebc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebcc`](#insn-00bdebcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebd8`](#insn-00bdebd8) → `01127ee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdebdc`](#insn-00bdebdc) → [`00bdebf8`](#insn-00bdebf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebe8`](#insn-00bdebe8) → `002ad4f9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdebec`](#insn-00bdebec) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdebf4`](#insn-00bdebf4) → `01127ee8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdebf8`](#insn-00bdebf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdebc8`](#insn-00bdebc8)

~~~json
{
  "source": "00bdebc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebcc`](#insn-00bdebcc)

~~~json
{
  "source": "00bdebcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebd8`](#insn-00bdebd8)

~~~json
{
  "source": "00bdebd8",
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
- 参照命令 [`00bdebdc`](#insn-00bdebdc)

~~~json
{
  "source": "00bdebdc",
  "target": "00bdebf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebe8`](#insn-00bdebe8)

~~~json
{
  "source": "00bdebe8",
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
- 参照命令 [`00bdebec`](#insn-00bdebec)

~~~json
{
  "source": "00bdebec",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdebf4`](#insn-00bdebf4)

~~~json
{
  "source": "00bdebf4",
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
- 参照命令 [`00bdebf8`](#insn-00bdebf8)

~~~json
{
  "source": "00bdebf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
