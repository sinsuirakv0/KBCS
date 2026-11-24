# 00b4afcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4af30`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-8914ec4984fa90cef4a733f4df96556b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b4bfc0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bfc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-b213e544ec20cbb3520d6ab0ea85dee2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4afcc",
  "name": "_ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d858d16aa5a9850159f2ac06a5824871f5d0c6c8ee901b99baa266402ea5aff",
  "source_text_sha256": "1d858d16aa5a9850159f2ac06a5824871f5d0c6c8ee901b99baa266402ea5aff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4afcc",
        "00b4b00f"
      ]
    ],
    "bytes_sha256": "8a00c8712fe5f38de5361318b5b642dba9f1a1816ccd49b2780916425c8ef8a0",
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
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 421 bytes

~~~c

long _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01125c10 == 0) {
    DAT_01125c10 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/HashMap",0);
  }
  return DAT_01125c10;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4afcc"></a> `00b4afcc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4afd0"></a> `00b4afd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4afd4"></a> `00b4afd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4afd8"></a> `00b4afd8` | `d3 2e 00 f0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4afdc"></a> `00b4afdc` | `68 0a 46 f9` | ldr x8,[x19, #0xc10] | `FALL_THROUGH`
<a id="insn-00b4afe0"></a> `00b4afe0` | `08 01 00 b5` | cbnz x8,0x00b4b000 | `CONDITIONAL_JUMP`
<a id="insn-00b4afe4"></a> `00b4afe4` | `e3 ba ff 90` | adrp x3,0x2a6000 | `FALL_THROUGH`
<a id="insn-00b4afe8"></a> `00b4afe8` | `63 28 1e 91` | add x3,x3,#0x78a | `FALL_THROUGH`
<a id="insn-00b4afec"></a> `00b4afec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4aff0"></a> `00b4aff0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4aff4"></a> `00b4aff4` | `fb 3f 04 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4aff8"></a> `00b4aff8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4affc"></a> `00b4affc` | `60 0a 06 f9` | str x0,[x19, #0xc10] | `FALL_THROUGH`
<a id="insn-00b4b000"></a> `00b4b000` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4b004"></a> `00b4b004` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4b008"></a> `00b4b008` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4b00c"></a> `00b4b00c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4afcc`](#insn-00b4afcc) 範囲 `[['00b4afcc', '00b4afe3']]`
  - `CONDITIONAL_JUMP` [`00b4afe0`](#insn-00b4afe0) → [`00b4b000`](#insn-00b4b000)
  - `FALL_THROUGH` [`00b4afe0`](#insn-00b4afe0) → [`00b4afe4`](#insn-00b4afe4)
- ブロック [`00b4afe4`](#insn-00b4afe4) 範囲 `[['00b4afe4', '00b4afff']]`
  - `FALL_THROUGH` [`00b4affc`](#insn-00b4affc) → [`00b4b000`](#insn-00b4b000)
- ブロック [`00b4b000`](#insn-00b4b000) 範囲 `[['00b4b000', '00b4b00f']]`

## 命令位置別の参照

- [`00b4afcc`](#insn-00b4afcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4afd0`](#insn-00b4afd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4afdc`](#insn-00b4afdc) → `01125c10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4afe0`](#insn-00b4afe0) → [`00b4b000`](#insn-00b4b000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4afe8`](#insn-00b4afe8) → `002a678a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4aff4`](#insn-00b4aff4) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00b4affc`](#insn-00b4affc) → `01125c10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4b000`](#insn-00b4b000) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4afcc`](#insn-00b4afcc)

~~~json
{
  "source": "00b4afcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4afd0`](#insn-00b4afd0)

~~~json
{
  "source": "00b4afd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4afdc`](#insn-00b4afdc)

~~~json
{
  "source": "00b4afdc",
  "target": "01125c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4afe0`](#insn-00b4afe0)

~~~json
{
  "source": "00b4afe0",
  "target": "00b4b000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4afe8`](#insn-00b4afe8)

~~~json
{
  "source": "00b4afe8",
  "target": "002a678a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a678a",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "002a678a",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4aff4`](#insn-00b4aff4)

~~~json
{
  "source": "00b4aff4",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4affc`](#insn-00b4affc)

~~~json
{
  "source": "00b4affc",
  "target": "01125c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4b000`](#insn-00b4b000)

~~~json
{
  "source": "00b4b000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
