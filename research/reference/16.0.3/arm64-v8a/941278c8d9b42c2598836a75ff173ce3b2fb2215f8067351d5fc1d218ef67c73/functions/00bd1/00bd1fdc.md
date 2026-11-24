# 00bd1fdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd0fe8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd0fe8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0082.md#compare-d6cd9f29a8d70a2de5664274749af934)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1fdc",
  "name": "_ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "318d0e10861e39da27fd9d1c9718f50fe1dcaa553a0f6cb94c483f13e3b0b7ef",
  "source_text_sha256": "318d0e10861e39da27fd9d1c9718f50fe1dcaa553a0f6cb94c483f13e3b0b7ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1fdc",
        "00bd204b"
      ]
    ],
    "bytes_sha256": "a2983a06fad926a1b87cf41818b2d352e161264a84ac73a074813dc9b3dd45b5",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/FirebaseApiNotAvailableException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 929 bytes

~~~c

void _ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bd1fe0 to 00cd1fe3 has its CatchHandler @ 00bd77ac */
  if (DAT_01127968 == 0) {
    DAT_01127968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/FirebaseApiNotAvailableException",0);
                    /* try { // try from 00bd2018 to 00cd205f has its CatchHandler @ 00bd7898 */
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01127968,&DAT_0030fdb0,1,&DAT_01127978,
             "com/google/firebase/FirebaseApiNotAvailableException");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1fdc"></a> `00bd1fdc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd1fe0"></a> `00bd1fe0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1fe4"></a> `00bd1fe4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1fe8"></a> `00bd1fe8` | `b4 2a 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd1fec"></a> `00bd1fec` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bd1ff0"></a> `00bd1ff0` | `81 b6 44 f9` | ldr x1,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00bd1ff4"></a> `00bd1ff4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd1ff8"></a> `00bd1ff8` | `41 01 00 b5` | cbnz x1,0x00bd2020 | `CONDITIONAL_JUMP`
<a id="insn-00bd1ffc"></a> `00bd1ffc` | `a3 b6 ff d0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bd2000"></a> `00bd2000` | `63 30 15 91` | add x3,x3,#0x54c | `FALL_THROUGH`
<a id="insn-00bd2004"></a> `00bd2004` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd2008"></a> `00bd2008` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bd200c"></a> `00bd200c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd2010"></a> `00bd2010` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd2014"></a> `00bd2014` | `e7 27 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2018"></a> `00bd2018` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bd201c"></a> `00bd201c` | `80 b6 04 f9` | str x0,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00bd2020"></a> `00bd2020` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2024"></a> `00bd2024` | `e2 b9 ff b0` | adrp x2,0x30f000 | `FALL_THROUGH`
<a id="insn-00bd2028"></a> `00bd2028` | `a4 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd202c"></a> `00bd202c` | `a5 b6 ff b0` | adrp x5,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bd2030"></a> `00bd2030` | `42 c0 36 91` | add x2,x2,#0xdb0 | `FALL_THROUGH`
<a id="insn-00bd2034"></a> `00bd2034` | `84 e0 25 91` | add x4,x4,#0x978 | `FALL_THROUGH`
<a id="insn-00bd2038"></a> `00bd2038` | `a5 30 15 91` | add x5,x5,#0x54c | `FALL_THROUGH`
<a id="insn-00bd203c"></a> `00bd203c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2040"></a> `00bd2040` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd2044"></a> `00bd2044` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2048"></a> `00bd2048` | `e2 27 02 14` | b 0x00c5bfd0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1fdc`](#insn-00bd1fdc) 範囲 `[['00bd1fdc', '00bd1fdf']]`
  - `FALL_THROUGH` [`00bd1fdc`](#insn-00bd1fdc) → [`00bd1fe0`](#insn-00bd1fe0)
- ブロック [`00bd1fe0`](#insn-00bd1fe0) 範囲 `[['00bd1fe0', '00bd1ffb']]`
  - `CONDITIONAL_JUMP` [`00bd1ff8`](#insn-00bd1ff8) → [`00bd2020`](#insn-00bd2020)
  - `FALL_THROUGH` [`00bd1ff8`](#insn-00bd1ff8) → [`00bd1ffc`](#insn-00bd1ffc)
- ブロック [`00bd1ffc`](#insn-00bd1ffc) 範囲 `[['00bd1ffc', '00bd2017']]`
  - `FALL_THROUGH` [`00bd2014`](#insn-00bd2014) → [`00bd2018`](#insn-00bd2018)
- ブロック [`00bd2018`](#insn-00bd2018) 範囲 `[['00bd2018', '00bd201f']]`
  - `FALL_THROUGH` [`00bd201c`](#insn-00bd201c) → [`00bd2020`](#insn-00bd2020)
- ブロック [`00bd2020`](#insn-00bd2020) 範囲 `[['00bd2020', '00bd204b']]`

## 命令位置別の参照

- [`00bd1fdc`](#insn-00bd1fdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1fe0`](#insn-00bd1fe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ff0`](#insn-00bd1ff0) → `01127968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1ff8`](#insn-00bd1ff8) → [`00bd2020`](#insn-00bd2020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2000`](#insn-00bd2000) → `002a754c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2014`](#insn-00bd2014) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd201c`](#insn-00bd201c) → `01127968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2020`](#insn-00bd2020) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2030`](#insn-00bd2030) → `0030fdb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2034`](#insn-00bd2034) → `01127978`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2038`](#insn-00bd2038) → `002a754c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2048`](#insn-00bd2048) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1fdc`](#insn-00bd1fdc)

~~~json
{
  "source": "00bd1fdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1fe0`](#insn-00bd1fe0)

~~~json
{
  "source": "00bd1fe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1ff0`](#insn-00bd1ff0)

~~~json
{
  "source": "00bd1ff0",
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
- 参照命令 [`00bd1ff8`](#insn-00bd1ff8)

~~~json
{
  "source": "00bd1ff8",
  "target": "00bd2020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2000`](#insn-00bd2000)

~~~json
{
  "source": "00bd2000",
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
- 参照命令 [`00bd2014`](#insn-00bd2014)

~~~json
{
  "source": "00bd2014",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd201c`](#insn-00bd201c)

~~~json
{
  "source": "00bd201c",
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
- 参照命令 [`00bd2020`](#insn-00bd2020)

~~~json
{
  "source": "00bd2020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2030`](#insn-00bd2030)

~~~json
{
  "source": "00bd2030",
  "target": "0030fdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2034`](#insn-00bd2034)

~~~json
{
  "source": "00bd2034",
  "target": "01127978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2038`](#insn-00bd2038)

~~~json
{
  "source": "00bd2038",
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
- 参照命令 [`00bd2048`](#insn-00bd2048)

~~~json
{
  "source": "00bd2048",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
