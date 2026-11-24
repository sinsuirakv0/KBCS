# 00bcda6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcca78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca78.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-b118bb48b69cae52a933aa31411d5e23)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcda6c",
  "name": "_ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e1889dfeb3a461339eac84093206cf3bb2af156834b09e9e91ae90c61b7b15e",
  "source_text_sha256": "3e1889dfeb3a461339eac84093206cf3bb2af156834b09e9e91ae90c61b7b15e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcda6c",
        "00bcdaab"
      ]
    ],
    "bytes_sha256": "e38a7c4489979becb0f2aa909145fd15c7a8ea52268a256ee62078fb9e9cd81b",
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

## 疑似コード / UTF-8 625 bytes

~~~c

long _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_011278b0 == 0) {
                    /* try { // try from 00bcda88 to 00ccda9f has its CatchHandler @ 00bcf970 */
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
                    /* try { // try from 00bcdaa0 to 00ccdb53 has its CatchHandler @ 00bcd634 */
  return DAT_011278b0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcda6c"></a> `00bcda6c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcda70"></a> `00bcda70` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcda74"></a> `00bcda74` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcda78"></a> `00bcda78` | `d3 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcda7c"></a> `00bcda7c` | `68 5a 44 f9` | ldr x8,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcda80"></a> `00bcda80` | `e8 00 00 b5` | cbnz x8,0x00bcda9c | `CONDITIONAL_JUMP`
<a id="insn-00bcda84"></a> `00bcda84` | `43 b7 ff 90` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcda88"></a> `00bcda88` | `63 a4 33 91` | add x3,x3,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcda8c"></a> `00bcda8c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcda90"></a> `00bcda90` | `48 39 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcda94"></a> `00bcda94` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcda98"></a> `00bcda98` | `60 5a 04 f9` | str x0,[x19, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcda9c"></a> `00bcda9c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdaa0"></a> `00bcdaa0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcdaa4"></a> `00bcdaa4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdaa8"></a> `00bcdaa8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcda6c`](#insn-00bcda6c) 範囲 `[['00bcda6c', '00bcda83']]`
  - `CONDITIONAL_JUMP` [`00bcda80`](#insn-00bcda80) → [`00bcda9c`](#insn-00bcda9c)
  - `FALL_THROUGH` [`00bcda80`](#insn-00bcda80) → [`00bcda84`](#insn-00bcda84)
- ブロック [`00bcda84`](#insn-00bcda84) 範囲 `[['00bcda84', '00bcda87']]`
  - `FALL_THROUGH` [`00bcda84`](#insn-00bcda84) → [`00bcda88`](#insn-00bcda88)
- ブロック [`00bcda88`](#insn-00bcda88) 範囲 `[['00bcda88', '00bcda9b']]`
  - `FALL_THROUGH` [`00bcda98`](#insn-00bcda98) → [`00bcda9c`](#insn-00bcda9c)
- ブロック [`00bcda9c`](#insn-00bcda9c) 範囲 `[['00bcda9c', '00bcda9f']]`
  - `FALL_THROUGH` [`00bcda9c`](#insn-00bcda9c) → [`00bcdaa0`](#insn-00bcdaa0)
- ブロック [`00bcdaa0`](#insn-00bcdaa0) 範囲 `[['00bcdaa0', '00bcdaab']]`

## 命令位置別の参照

- [`00bcda6c`](#insn-00bcda6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda70`](#insn-00bcda70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda7c`](#insn-00bcda7c) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcda80`](#insn-00bcda80) → [`00bcda9c`](#insn-00bcda9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda88`](#insn-00bcda88) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcda90`](#insn-00bcda90) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcda98`](#insn-00bcda98) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcda9c`](#insn-00bcda9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcda6c`](#insn-00bcda6c)

~~~json
{
  "source": "00bcda6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda70`](#insn-00bcda70)

~~~json
{
  "source": "00bcda70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda7c`](#insn-00bcda7c)

~~~json
{
  "source": "00bcda7c",
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
- 参照命令 [`00bcda80`](#insn-00bcda80)

~~~json
{
  "source": "00bcda80",
  "target": "00bcda9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda88`](#insn-00bcda88)

~~~json
{
  "source": "00bcda88",
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
- 参照命令 [`00bcda90`](#insn-00bcda90)

~~~json
{
  "source": "00bcda90",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcda98`](#insn-00bcda98)

~~~json
{
  "source": "00bcda98",
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
- 参照命令 [`00bcda9c`](#insn-00bcda9c)

~~~json
{
  "source": "00bcda9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
