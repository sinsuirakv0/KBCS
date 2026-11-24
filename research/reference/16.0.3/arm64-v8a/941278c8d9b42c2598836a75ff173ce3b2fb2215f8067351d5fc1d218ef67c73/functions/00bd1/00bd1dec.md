# 00bd1dec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd0df8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd0df8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0082.md#compare-06cc3815a6c44c69f2971edc24506281)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1dec",
  "name": "_ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ec244bc63b24376b9603e01dce62f3056682785fd1e7ccf3144e021992fcac9",
  "source_text_sha256": "9ec244bc63b24376b9603e01dce62f3056682785fd1e7ccf3144e021992fcac9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1dec",
        "00bd1e2b"
      ]
    ],
    "bytes_sha256": "54aea226778f5b95dd1a74ce7998192a8ca469448b65a469f367f3f90287eb17",
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
"%PG%com/google/firebase/FirebaseApiNotAvailableException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 571 bytes

~~~c

long _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
                    /* try { // try from 00bd1dec to 00cd1ed7 has its CatchHandler @ 00bd19bc */
  if (DAT_01127968 == 0) {
    DAT_01127968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01127968;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1dec"></a> `00bd1dec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd1df0"></a> `00bd1df0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1df4"></a> `00bd1df4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1df8"></a> `00bd1df8` | `b3 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd1dfc"></a> `00bd1dfc` | `68 b6 44 f9` | ldr x8,[x19, #0x968] | `FALL_THROUGH`
<a id="insn-00bd1e00"></a> `00bd1e00` | `e8 00 00 b5` | cbnz x8,0x00bd1e1c | `CONDITIONAL_JUMP`
<a id="insn-00bd1e04"></a> `00bd1e04` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bd1e08"></a> `00bd1e08` | `a3 b6 ff d0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bd1e0c"></a> `00bd1e0c` | `63 30 15 91` | add x3,x3,#0x54c | `FALL_THROUGH`
<a id="insn-00bd1e10"></a> `00bd1e10` | `68 28 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1e14"></a> `00bd1e14` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd1e18"></a> `00bd1e18` | `60 b6 04 f9` | str x0,[x19, #0x968] | `FALL_THROUGH`
<a id="insn-00bd1e1c"></a> `00bd1e1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1e20"></a> `00bd1e20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd1e24"></a> `00bd1e24` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd1e28"></a> `00bd1e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1dec`](#insn-00bd1dec) 範囲 `[['00bd1dec', '00bd1e03']]`
  - `CONDITIONAL_JUMP` [`00bd1e00`](#insn-00bd1e00) → [`00bd1e1c`](#insn-00bd1e1c)
  - `FALL_THROUGH` [`00bd1e00`](#insn-00bd1e00) → [`00bd1e04`](#insn-00bd1e04)
- ブロック [`00bd1e04`](#insn-00bd1e04) 範囲 `[['00bd1e04', '00bd1e1b']]`
  - `FALL_THROUGH` [`00bd1e18`](#insn-00bd1e18) → [`00bd1e1c`](#insn-00bd1e1c)
- ブロック [`00bd1e1c`](#insn-00bd1e1c) 範囲 `[['00bd1e1c', '00bd1e2b']]`

## 命令位置別の参照

- [`00bd1dec`](#insn-00bd1dec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1df0`](#insn-00bd1df0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1dfc`](#insn-00bd1dfc) → `01127968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1e00`](#insn-00bd1e00) → [`00bd1e1c`](#insn-00bd1e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1e0c`](#insn-00bd1e0c) → `002a754c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd1e10`](#insn-00bd1e10) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd1e18`](#insn-00bd1e18) → `01127968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1e1c`](#insn-00bd1e1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1dec`](#insn-00bd1dec)

~~~json
{
  "source": "00bd1dec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1df0`](#insn-00bd1df0)

~~~json
{
  "source": "00bd1df0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1dfc`](#insn-00bd1dfc)

~~~json
{
  "source": "00bd1dfc",
  "target": "01127968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1e00`](#insn-00bd1e00)

~~~json
{
  "source": "00bd1e00",
  "target": "00bd1e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1e0c`](#insn-00bd1e0c)

~~~json
{
  "source": "00bd1e0c",
  "target": "002a754c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7548",
  "offset": 4,
  "size": 57,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002a7548",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd1e10`](#insn-00bd1e10)

~~~json
{
  "source": "00bd1e10",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1e18`](#insn-00bd1e18)

~~~json
{
  "source": "00bd1e18",
  "target": "01127968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1e1c`](#insn-00bd1e1c)

~~~json
{
  "source": "00bd1e1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
