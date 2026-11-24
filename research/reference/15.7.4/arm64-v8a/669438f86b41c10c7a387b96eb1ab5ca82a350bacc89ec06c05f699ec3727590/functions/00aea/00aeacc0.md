# 00aeacc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeac7c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac7c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-9b92b0169bbc66d218e74754acb25e88)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4aa44`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa44.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-f2f4307e68836c0922400c466cf6171c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeacc0",
  "name": "_ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e7aa5c7fc6eab887df3f8acdbd8dce7d1a01f6e831dba8a57001a08ee6ebe3f2",
  "source_text_sha256": "e7aa5c7fc6eab887df3f8acdbd8dce7d1a01f6e831dba8a57001a08ee6ebe3f2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeacc0",
        "00aeacff"
      ]
    ],
    "bytes_sha256": "b984aad03e6c10de0b6be089b646cfbecd3c993418114a4ea71635c652c77e87",
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

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 450 bytes

~~~c

long _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0850 == 0) {
    DAT_010a0850 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0850;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeacc0"></a> `00aeacc0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeacc4"></a> `00aeacc4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeacc8"></a> `00aeacc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeaccc"></a> `00aeaccc` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeacd0"></a> `00aeacd0` | `68 2a 44 f9` | ldr x8,[x19, #0x850] | `FALL_THROUGH`
<a id="insn-00aeacd4"></a> `00aeacd4` | `e8 00 00 b5` | cbnz x8,0x00aeacf0 | `CONDITIONAL_JUMP`
<a id="insn-00aeacd8"></a> `00aeacd8` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aeacdc"></a> `00aeacdc` | `63 bd ff 90` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00aeace0"></a> `00aeace0` | `63 54 2f 91` | add x3,x3,#0xbd5 | `FALL_THROUGH`
<a id="insn-00aeace4"></a> `00aeace4` | `eb cc 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aeace8"></a> `00aeace8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeacec"></a> `00aeacec` | `60 2a 04 f9` | str x0,[x19, #0x850] | `FALL_THROUGH`
<a id="insn-00aeacf0"></a> `00aeacf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeacf4"></a> `00aeacf4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeacf8"></a> `00aeacf8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeacfc"></a> `00aeacfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeacc0`](#insn-00aeacc0) 範囲 `[['00aeacc0', '00aeacd7']]`
  - `CONDITIONAL_JUMP` [`00aeacd4`](#insn-00aeacd4) → [`00aeacf0`](#insn-00aeacf0)
  - `FALL_THROUGH` [`00aeacd4`](#insn-00aeacd4) → [`00aeacd8`](#insn-00aeacd8)
- ブロック [`00aeacd8`](#insn-00aeacd8) 範囲 `[['00aeacd8', '00aeacef']]`
  - `FALL_THROUGH` [`00aeacec`](#insn-00aeacec) → [`00aeacf0`](#insn-00aeacf0)
- ブロック [`00aeacf0`](#insn-00aeacf0) 範囲 `[['00aeacf0', '00aeacff']]`

## 命令位置別の参照

- [`00aeacc0`](#insn-00aeacc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeacc4`](#insn-00aeacc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeacd0`](#insn-00aeacd0) → `010a0850`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeacd4`](#insn-00aeacd4) → [`00aeacf0`](#insn-00aeacf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeace0`](#insn-00aeace0) → `00296bd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeace4`](#insn-00aeace4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aeacec`](#insn-00aeacec) → `010a0850`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeacf0`](#insn-00aeacf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeacc0`](#insn-00aeacc0)

~~~json
{
  "source": "00aeacc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeacc4`](#insn-00aeacc4)

~~~json
{
  "source": "00aeacc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeacd0`](#insn-00aeacd0)

~~~json
{
  "source": "00aeacd0",
  "target": "010a0850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeacd4`](#insn-00aeacd4)

~~~json
{
  "source": "00aeacd4",
  "target": "00aeacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeace0`](#insn-00aeace0)

~~~json
{
  "source": "00aeace0",
  "target": "00296bd5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296bd5",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296bd5",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeace4`](#insn-00aeace4)

~~~json
{
  "source": "00aeace4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeacec`](#insn-00aeacec)

~~~json
{
  "source": "00aeacec",
  "target": "010a0850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeacf0`](#insn-00aeacf0)

~~~json
{
  "source": "00aeacf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
