# 00b4eadc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4dae8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dae8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0076.md#compare-dcac4dd4701956f8d25171b6cf0c3178)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4eadc",
  "name": "_ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67ff8e9bbfd2bcb07c06d177cc8dd75d42e5a79af4fd1303a3c1d34c8700af5c",
  "source_text_sha256": "67ff8e9bbfd2bcb07c06d177cc8dd75d42e5a79af4fd1303a3c1d34c8700af5c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4eadc",
        "00b4eb1b"
      ]
    ],
    "bytes_sha256": "1927347583331755469aff12e5d8266a127a5e4f3ce6c71bf9a6004d99081df4",
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
"java/lang/Throwable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 451 bytes

~~~c

long _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_01126db0 == 0) {
    DAT_01126db0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126db0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4eadc"></a> `00b4eadc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4eae0"></a> `00b4eae0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4eae4"></a> `00b4eae4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4eae8"></a> `00b4eae8` | `d3 2e 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4eaec"></a> `00b4eaec` | `68 da 46 f9` | ldr x8,[x19, #0xdb0] | `FALL_THROUGH`
<a id="insn-00b4eaf0"></a> `00b4eaf0` | `e8 00 00 b5` | cbnz x8,0x00b4eb0c | `CONDITIONAL_JUMP`
<a id="insn-00b4eaf4"></a> `00b4eaf4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00b4eaf8"></a> `00b4eaf8` | `43 bb ff f0` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00b4eafc"></a> `00b4eafc` | `63 dc 28 91` | add x3,x3,#0xa37 | `FALL_THROUGH`
<a id="insn-00b4eb00"></a> `00b4eb00` | `2c 35 04 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4eb04"></a> `00b4eb04` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4eb08"></a> `00b4eb08` | `60 da 06 f9` | str x0,[x19, #0xdb0] | `FALL_THROUGH`
<a id="insn-00b4eb0c"></a> `00b4eb0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4eb10"></a> `00b4eb10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4eb14"></a> `00b4eb14` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4eb18"></a> `00b4eb18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4eadc`](#insn-00b4eadc) 範囲 `[['00b4eadc', '00b4eaf3']]`
  - `CONDITIONAL_JUMP` [`00b4eaf0`](#insn-00b4eaf0) → [`00b4eb0c`](#insn-00b4eb0c)
  - `FALL_THROUGH` [`00b4eaf0`](#insn-00b4eaf0) → [`00b4eaf4`](#insn-00b4eaf4)
- ブロック [`00b4eaf4`](#insn-00b4eaf4) 範囲 `[['00b4eaf4', '00b4eb0b']]`
  - `FALL_THROUGH` [`00b4eb08`](#insn-00b4eb08) → [`00b4eb0c`](#insn-00b4eb0c)
- ブロック [`00b4eb0c`](#insn-00b4eb0c) 範囲 `[['00b4eb0c', '00b4eb1b']]`

## 命令位置別の参照

- [`00b4eadc`](#insn-00b4eadc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eae0`](#insn-00b4eae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eaec`](#insn-00b4eaec) → `01126db0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4eaf0`](#insn-00b4eaf0) → [`00b4eb0c`](#insn-00b4eb0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eafc`](#insn-00b4eafc) → `002b9a37`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4eb00`](#insn-00b4eb00) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00b4eb08`](#insn-00b4eb08) → `01126db0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4eb0c`](#insn-00b4eb0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4eadc`](#insn-00b4eadc)

~~~json
{
  "source": "00b4eadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eae0`](#insn-00b4eae0)

~~~json
{
  "source": "00b4eae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eaec`](#insn-00b4eaec)

~~~json
{
  "source": "00b4eaec",
  "target": "01126db0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126db0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4eaf0`](#insn-00b4eaf0)

~~~json
{
  "source": "00b4eaf0",
  "target": "00b4eb0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eafc`](#insn-00b4eafc)

~~~json
{
  "source": "00b4eafc",
  "target": "002b9a37",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9a37",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002b9a37",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4eb00`](#insn-00b4eb00)

~~~json
{
  "source": "00b4eb00",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4eb08`](#insn-00b4eb08)

~~~json
{
  "source": "00b4eb08",
  "target": "01126db0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126db0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4eb0c`](#insn-00b4eb0c)

~~~json
{
  "source": "00b4eb0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
