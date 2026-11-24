# 00bc1fec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc1f50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-2c5dc7a0710cb50d1989cfe078d4d5a7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bc2fe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2fe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0080.md#compare-4624976cfac00af7c829474d5a0efaf7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1fec",
  "name": "_ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "55fcac3e8b2a9914a42096a091da98be5623082a6b0b300b639778f5587bb62b",
  "source_text_sha256": "55fcac3e8b2a9914a42096a091da98be5623082a6b0b300b639778f5587bb62b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc1fec",
        "00bc202f"
      ]
    ],
    "bytes_sha256": "babb56fd8fa24b46fac46273ee3f01ad44ddfb533ab87083ee9886e0738213a2",
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

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigValue"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 711 bytes

~~~c

long _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bc1ff4 to 00cc1ffb has its CatchHandler @ 00bc2214 */
                    /* try { // try from 00bc1ffc to 00cc200f has its CatchHandler @ 00bc21a8 */
  if (DAT_01126620 == 0) {
    DAT_01126620 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/remoteconfig/FirebaseRemoteConfigValue",0);
  }
  return DAT_01126620;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc1fec"></a> `00bc1fec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc1ff0"></a> `00bc1ff0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1ff4"></a> `00bc1ff4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc1ff8"></a> `00bc1ff8` | `33 2b 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc1ffc"></a> `00bc1ffc` | `68 12 43 f9` | ldr x8,[x19, #0x620] | `FALL_THROUGH`
<a id="insn-00bc2000"></a> `00bc2000` | `08 01 00 b5` | cbnz x8,0x00bc2020 | `CONDITIONAL_JUMP`
<a id="insn-00bc2004"></a> `00bc2004` | `e3 b7 ff f0` | adrp x3,0x2c1000 | `FALL_THROUGH`
<a id="insn-00bc2008"></a> `00bc2008` | `63 28 34 91` | add x3,x3,#0xd0a | `FALL_THROUGH`
<a id="insn-00bc200c"></a> `00bc200c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bc2010"></a> `00bc2010` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bc2014"></a> `00bc2014` | `f3 63 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2018"></a> `00bc2018` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc201c"></a> `00bc201c` | `60 12 03 f9` | str x0,[x19, #0x620] | `FALL_THROUGH`
<a id="insn-00bc2020"></a> `00bc2020` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2024"></a> `00bc2024` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc2028"></a> `00bc2028` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc202c"></a> `00bc202c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc1fec`](#insn-00bc1fec) 範囲 `[['00bc1fec', '00bc1ff3']]`
  - `FALL_THROUGH` [`00bc1ff0`](#insn-00bc1ff0) → [`00bc1ff4`](#insn-00bc1ff4)
- ブロック [`00bc1ff4`](#insn-00bc1ff4) 範囲 `[['00bc1ff4', '00bc1ffb']]`
  - `FALL_THROUGH` [`00bc1ff8`](#insn-00bc1ff8) → [`00bc1ffc`](#insn-00bc1ffc)
- ブロック [`00bc1ffc`](#insn-00bc1ffc) 範囲 `[['00bc1ffc', '00bc2003']]`
  - `CONDITIONAL_JUMP` [`00bc2000`](#insn-00bc2000) → [`00bc2020`](#insn-00bc2020)
  - `FALL_THROUGH` [`00bc2000`](#insn-00bc2000) → [`00bc2004`](#insn-00bc2004)
- ブロック [`00bc2004`](#insn-00bc2004) 範囲 `[['00bc2004', '00bc201f']]`
  - `FALL_THROUGH` [`00bc201c`](#insn-00bc201c) → [`00bc2020`](#insn-00bc2020)
- ブロック [`00bc2020`](#insn-00bc2020) 範囲 `[['00bc2020', '00bc202f']]`

## 命令位置別の参照

- [`00bc1fec`](#insn-00bc1fec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ff0`](#insn-00bc1ff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ffc`](#insn-00bc1ffc) → `01126620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2000`](#insn-00bc2000) → [`00bc2020`](#insn-00bc2020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2008`](#insn-00bc2008) → `002c1d0a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc2014`](#insn-00bc2014) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bc201c`](#insn-00bc201c) → `01126620`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2020`](#insn-00bc2020) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc1fec`](#insn-00bc1fec)

~~~json
{
  "source": "00bc1fec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ff0`](#insn-00bc1ff0)

~~~json
{
  "source": "00bc1ff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ffc`](#insn-00bc1ffc)

~~~json
{
  "source": "00bc1ffc",
  "target": "01126620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126620",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc2000`](#insn-00bc2000)

~~~json
{
  "source": "00bc2000",
  "target": "00bc2020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2008`](#insn-00bc2008)

~~~json
{
  "source": "00bc2008",
  "target": "002c1d0a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1d06",
  "offset": 4,
  "size": 63,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f72656d6f7465636f",
  "capture_start": "002c1d06",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc2014`](#insn-00bc2014)

~~~json
{
  "source": "00bc2014",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc201c`](#insn-00bc201c)

~~~json
{
  "source": "00bc201c",
  "target": "01126620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126620",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc2020`](#insn-00bc2020)

~~~json
{
  "source": "00bc2020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
