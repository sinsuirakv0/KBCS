# 00bcd3dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcc3e8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc3e8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-a7c7b25bfb7d4280297f88018011cd8f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcd3dc",
  "name": "_ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "379df259bfdad57585f1cc82b93d6755bb661210d82bd880718e800c96eaaadd",
  "source_text_sha256": "379df259bfdad57585f1cc82b93d6755bb661210d82bd880718e800c96eaaadd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcd3dc",
        "00bcd41b"
      ]
    ],
    "bytes_sha256": "423d806aa2ddd0710cdbdbde5d52b4083d2550955f79dfb98aeb9e9727306928",
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
"%PG%com/google/firebase/auth/FirebaseAuth"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 520 bytes

~~~c

long _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_011277e8 == 0) {
                    /* try { // try from 00bcd3f8 to 00ccd47f has its CatchHandler @ 00bcd564 */
    DAT_011277e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_011277e8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcd3dc"></a> `00bcd3dc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcd3e0"></a> `00bcd3e0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd3e4"></a> `00bcd3e4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcd3e8"></a> `00bcd3e8` | `d3 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcd3ec"></a> `00bcd3ec` | `68 f6 43 f9` | ldr x8,[x19, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bcd3f0"></a> `00bcd3f0` | `e8 00 00 b5` | cbnz x8,0x00bcd40c | `CONDITIONAL_JUMP`
<a id="insn-00bcd3f4"></a> `00bcd3f4` | `e3 b6 ff f0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcd3f8"></a> `00bcd3f8` | `63 b4 0a 91` | add x3,x3,#0x2ad | `FALL_THROUGH`
<a id="insn-00bcd3fc"></a> `00bcd3fc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcd400"></a> `00bcd400` | `ec 3a 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd404"></a> `00bcd404` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcd408"></a> `00bcd408` | `60 f6 03 f9` | str x0,[x19, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bcd40c"></a> `00bcd40c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd410"></a> `00bcd410` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcd414"></a> `00bcd414` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcd418"></a> `00bcd418` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcd3dc`](#insn-00bcd3dc) 範囲 `[['00bcd3dc', '00bcd3f3']]`
  - `CONDITIONAL_JUMP` [`00bcd3f0`](#insn-00bcd3f0) → [`00bcd40c`](#insn-00bcd40c)
  - `FALL_THROUGH` [`00bcd3f0`](#insn-00bcd3f0) → [`00bcd3f4`](#insn-00bcd3f4)
- ブロック [`00bcd3f4`](#insn-00bcd3f4) 範囲 `[['00bcd3f4', '00bcd3f7']]`
  - `FALL_THROUGH` [`00bcd3f4`](#insn-00bcd3f4) → [`00bcd3f8`](#insn-00bcd3f8)
- ブロック [`00bcd3f8`](#insn-00bcd3f8) 範囲 `[['00bcd3f8', '00bcd40b']]`
  - `FALL_THROUGH` [`00bcd408`](#insn-00bcd408) → [`00bcd40c`](#insn-00bcd40c)
- ブロック [`00bcd40c`](#insn-00bcd40c) 範囲 `[['00bcd40c', '00bcd41b']]`

## 命令位置別の参照

- [`00bcd3dc`](#insn-00bcd3dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd3e0`](#insn-00bcd3e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd3ec`](#insn-00bcd3ec) → `011277e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcd3f0`](#insn-00bcd3f0) → [`00bcd40c`](#insn-00bcd40c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd3f8`](#insn-00bcd3f8) → `002ac2ad`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd400`](#insn-00bcd400) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd408`](#insn-00bcd408) → `011277e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcd40c`](#insn-00bcd40c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcd3dc`](#insn-00bcd3dc)

~~~json
{
  "source": "00bcd3dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd3e0`](#insn-00bcd3e0)

~~~json
{
  "source": "00bcd3e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd3ec`](#insn-00bcd3ec)

~~~json
{
  "source": "00bcd3ec",
  "target": "011277e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcd3f0`](#insn-00bcd3f0)

~~~json
{
  "source": "00bcd3f0",
  "target": "00bcd40c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd3f8`](#insn-00bcd3f8)

~~~json
{
  "source": "00bcd3f8",
  "target": "002ac2ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac2a9",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ac2a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcd400`](#insn-00bcd400)

~~~json
{
  "source": "00bcd400",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd408`](#insn-00bcd408)

~~~json
{
  "source": "00bcd408",
  "target": "011277e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcd40c`](#insn-00bcd40c)

~~~json
{
  "source": "00bcd40c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
