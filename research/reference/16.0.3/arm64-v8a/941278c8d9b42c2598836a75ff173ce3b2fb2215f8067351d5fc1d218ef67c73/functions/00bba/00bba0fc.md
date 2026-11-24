# 00bba0fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb9108`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9108.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-a07b234913308de84c725493539c6f48)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba0fc",
  "name": "_ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "306dab41f782aee7f8d8494ff37003f746be6660f1b287b3fc248da2bc475948",
  "source_text_sha256": "306dab41f782aee7f8d8494ff37003f746be6660f1b287b3fc248da2bc475948",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba0fc",
        "00bba13f"
      ]
    ],
    "bytes_sha256": "4f8ff82f523aaeec7cd8acc8784e9cfb41a25367fa33c7b3d35084e8b64b74de",
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
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 954 bytes

~~~c

long _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* catch() { ... } // from try @ 00bb9f90 with catch @ 00bba100 */
  if (DAT_011273d8 == 0) {
                    /* catch() { ... } // from try @ 00bb9968 with catch @ 00bba118 */
                    /* catch() { ... } // from try @ 00bb9950 with catch @ 00bba11c */
                    /* catch() { ... } // from try @ 00bb9a08 with catch @ 00bba124 */
    DAT_011273d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",0);
  }
                    /* catch() { ... } // from try @ 00bb9ec4 with catch @ 00bba13c */
  return DAT_011273d8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba0fc"></a> `00bba0fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bba100"></a> `00bba100` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba104"></a> `00bba104` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bba108"></a> `00bba108` | `73 2b 00 b0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bba10c"></a> `00bba10c` | `68 ee 41 f9` | ldr x8,[x19, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bba110"></a> `00bba110` | `08 01 00 b5` | cbnz x8,0x00bba130 | `CONDITIONAL_JUMP`
<a id="insn-00bba114"></a> `00bba114` | `e3 b7 ff f0` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bba118"></a> `00bba118` | `63 04 30 91` | add x3,x3,#0xc01 | `FALL_THROUGH`
<a id="insn-00bba11c"></a> `00bba11c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bba120"></a> `00bba120` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bba124"></a> `00bba124` | `a3 87 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba128"></a> `00bba128` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bba12c"></a> `00bba12c` | `60 ee 01 f9` | str x0,[x19, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bba130"></a> `00bba130` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba134"></a> `00bba134` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bba138"></a> `00bba138` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bba13c"></a> `00bba13c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba0fc`](#insn-00bba0fc) 範囲 `[['00bba0fc', '00bba0ff']]`
  - `FALL_THROUGH` [`00bba0fc`](#insn-00bba0fc) → [`00bba100`](#insn-00bba100)
- ブロック [`00bba100`](#insn-00bba100) 範囲 `[['00bba100', '00bba113']]`
  - `CONDITIONAL_JUMP` [`00bba110`](#insn-00bba110) → [`00bba130`](#insn-00bba130)
  - `FALL_THROUGH` [`00bba110`](#insn-00bba110) → [`00bba114`](#insn-00bba114)
- ブロック [`00bba114`](#insn-00bba114) 範囲 `[['00bba114', '00bba117']]`
  - `FALL_THROUGH` [`00bba114`](#insn-00bba114) → [`00bba118`](#insn-00bba118)
- ブロック [`00bba118`](#insn-00bba118) 範囲 `[['00bba118', '00bba11b']]`
  - `FALL_THROUGH` [`00bba118`](#insn-00bba118) → [`00bba11c`](#insn-00bba11c)
- ブロック [`00bba11c`](#insn-00bba11c) 範囲 `[['00bba11c', '00bba123']]`
  - `FALL_THROUGH` [`00bba120`](#insn-00bba120) → [`00bba124`](#insn-00bba124)
- ブロック [`00bba124`](#insn-00bba124) 範囲 `[['00bba124', '00bba12f']]`
  - `FALL_THROUGH` [`00bba12c`](#insn-00bba12c) → [`00bba130`](#insn-00bba130)
- ブロック [`00bba130`](#insn-00bba130) 範囲 `[['00bba130', '00bba13b']]`
  - `FALL_THROUGH` [`00bba138`](#insn-00bba138) → [`00bba13c`](#insn-00bba13c)
- ブロック [`00bba13c`](#insn-00bba13c) 範囲 `[['00bba13c', '00bba13f']]`

## 命令位置別の参照

- [`00bba0fc`](#insn-00bba0fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba100`](#insn-00bba100) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba10c`](#insn-00bba10c) → `011273d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bba110`](#insn-00bba110) → [`00bba130`](#insn-00bba130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba118`](#insn-00bba118) → `002b9c01`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba124`](#insn-00bba124) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bba12c`](#insn-00bba12c) → `011273d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bba130`](#insn-00bba130) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba0fc`](#insn-00bba0fc)

~~~json
{
  "source": "00bba0fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba100`](#insn-00bba100)

~~~json
{
  "source": "00bba100",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba10c`](#insn-00bba10c)

~~~json
{
  "source": "00bba10c",
  "target": "011273d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bba110`](#insn-00bba110)

~~~json
{
  "source": "00bba110",
  "target": "00bba130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba118`](#insn-00bba118)

~~~json
{
  "source": "00bba118",
  "target": "002b9c01",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9bfd",
  "offset": 4,
  "size": 64,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002b9bfd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bba124`](#insn-00bba124)

~~~json
{
  "source": "00bba124",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba12c`](#insn-00bba12c)

~~~json
{
  "source": "00bba12c",
  "target": "011273d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bba130`](#insn-00bba130)

~~~json
{
  "source": "00bba130",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
