# 00b4aeac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4aa84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0072.md#compare-4f8b0731fb7147da3cbfac2377557d2f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4af48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-7aed6bc6e5ee5f05ff034d893db2ce82)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4aeac",
  "name": "_ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea5d03800fd8224d09c3827345a5928832597a24492d9a305589aa6b30bce0be",
  "source_text_sha256": "ea5d03800fd8224d09c3827345a5928832597a24492d9a305589aa6b30bce0be",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4aeac",
        "00b4aeeb"
      ]
    ],
    "bytes_sha256": "7e7552228348b4e2a19c1a64b793ecd8ebf6c692ac0528c29902ba5d42e80c2c",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 524 bytes

~~~c

long _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
                    /* try { // try from 00b4aeb4 to 00c4b2d3 has its CatchHandler @ 00b47f00 */
  if (DAT_01125b10 == 0) {
    DAT_01125b10 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01125b10;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4aeac"></a> `00b4aeac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4aeb0"></a> `00b4aeb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4aeb4"></a> `00b4aeb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4aeb8"></a> `00b4aeb8` | `d3 2e 00 f0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4aebc"></a> `00b4aebc` | `68 8a 45 f9` | ldr x8,[x19, #0xb10] | `FALL_THROUGH`
<a id="insn-00b4aec0"></a> `00b4aec0` | `e8 00 00 b5` | cbnz x8,0x00b4aedc | `CONDITIONAL_JUMP`
<a id="insn-00b4aec4"></a> `00b4aec4` | `e3 ba ff 90` | adrp x3,0x2a6000 | `FALL_THROUGH`
<a id="insn-00b4aec8"></a> `00b4aec8` | `63 98 1f 91` | add x3,x3,#0x7e6 | `FALL_THROUGH`
<a id="insn-00b4aecc"></a> `00b4aecc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4aed0"></a> `00b4aed0` | `10 40 04 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4aed4"></a> `00b4aed4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4aed8"></a> `00b4aed8` | `60 8a 05 f9` | str x0,[x19, #0xb10] | `FALL_THROUGH`
<a id="insn-00b4aedc"></a> `00b4aedc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4aee0"></a> `00b4aee0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4aee4"></a> `00b4aee4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4aee8"></a> `00b4aee8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4aeac`](#insn-00b4aeac) 範囲 `[['00b4aeac', '00b4aeb3']]`
  - `FALL_THROUGH` [`00b4aeb0`](#insn-00b4aeb0) → [`00b4aeb4`](#insn-00b4aeb4)
- ブロック [`00b4aeb4`](#insn-00b4aeb4) 範囲 `[['00b4aeb4', '00b4aec3']]`
  - `CONDITIONAL_JUMP` [`00b4aec0`](#insn-00b4aec0) → [`00b4aedc`](#insn-00b4aedc)
  - `FALL_THROUGH` [`00b4aec0`](#insn-00b4aec0) → [`00b4aec4`](#insn-00b4aec4)
- ブロック [`00b4aec4`](#insn-00b4aec4) 範囲 `[['00b4aec4', '00b4aedb']]`
  - `FALL_THROUGH` [`00b4aed8`](#insn-00b4aed8) → [`00b4aedc`](#insn-00b4aedc)
- ブロック [`00b4aedc`](#insn-00b4aedc) 範囲 `[['00b4aedc', '00b4aeeb']]`

## 命令位置別の参照

- [`00b4aeac`](#insn-00b4aeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aeb0`](#insn-00b4aeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aebc`](#insn-00b4aebc) → `01125b10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4aec0`](#insn-00b4aec0) → [`00b4aedc`](#insn-00b4aedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aec8`](#insn-00b4aec8) → `002a67e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4aed0`](#insn-00b4aed0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00b4aed8`](#insn-00b4aed8) → `01125b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4aedc`](#insn-00b4aedc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4aeac`](#insn-00b4aeac)

~~~json
{
  "source": "00b4aeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aeb0`](#insn-00b4aeb0)

~~~json
{
  "source": "00b4aeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aebc`](#insn-00b4aebc)

~~~json
{
  "source": "00b4aebc",
  "target": "01125b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4aec0`](#insn-00b4aec0)

~~~json
{
  "source": "00b4aec0",
  "target": "00b4aedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aec8`](#insn-00b4aec8)

~~~json
{
  "source": "00b4aec8",
  "target": "002a67e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a67e6",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "002a67e6",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4aed0`](#insn-00b4aed0)

~~~json
{
  "source": "00b4aed0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4aed8`](#insn-00b4aed8)

~~~json
{
  "source": "00b4aed8",
  "target": "01125b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4aedc`](#insn-00b4aedc)

~~~json
{
  "source": "00b4aedc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
