# 00b4cddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4bde8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bde8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-e3cd2b42ecd81b3001a4aca778341e73)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cddc",
  "name": "_ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a31f1cc227dd51b9d3314ef0519f0f5eec19ba4a659b2823f7e25b4de501248b",
  "source_text_sha256": "a31f1cc227dd51b9d3314ef0519f0f5eec19ba4a659b2823f7e25b4de501248b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4cddc",
        "00b4ce1b"
      ]
    ],
    "bytes_sha256": "c6617698f28d4822773dcf3293a1b83ce9e1eac9c83657514e045fd2432cc9e2",
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
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 427 bytes

~~~c

long _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_01126c78 == 0) {
    DAT_01126c78 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126c78;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4cddc"></a> `00b4cddc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4cde0"></a> `00b4cde0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cde4"></a> `00b4cde4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4cde8"></a> `00b4cde8` | `d3 2e 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4cdec"></a> `00b4cdec` | `68 3e 46 f9` | ldr x8,[x19, #0xc78] | `FALL_THROUGH`
<a id="insn-00b4cdf0"></a> `00b4cdf0` | `e8 00 00 b5` | cbnz x8,0x00b4ce0c | `CONDITIONAL_JUMP`
<a id="insn-00b4cdf4"></a> `00b4cdf4` | `c3 ba ff f0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00b4cdf8"></a> `00b4cdf8` | `63 4c 09 91` | add x3,x3,#0x253 | `FALL_THROUGH`
<a id="insn-00b4cdfc"></a> `00b4cdfc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4ce00"></a> `00b4ce00` | `6c 3c 04 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce04"></a> `00b4ce04` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4ce08"></a> `00b4ce08` | `60 3e 06 f9` | str x0,[x19, #0xc78] | `FALL_THROUGH`
<a id="insn-00b4ce0c"></a> `00b4ce0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ce10"></a> `00b4ce10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4ce14"></a> `00b4ce14` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4ce18"></a> `00b4ce18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4cddc`](#insn-00b4cddc) 範囲 `[['00b4cddc', '00b4cdf3']]`
  - `CONDITIONAL_JUMP` [`00b4cdf0`](#insn-00b4cdf0) → [`00b4ce0c`](#insn-00b4ce0c)
  - `FALL_THROUGH` [`00b4cdf0`](#insn-00b4cdf0) → [`00b4cdf4`](#insn-00b4cdf4)
- ブロック [`00b4cdf4`](#insn-00b4cdf4) 範囲 `[['00b4cdf4', '00b4ce0b']]`
  - `FALL_THROUGH` [`00b4ce08`](#insn-00b4ce08) → [`00b4ce0c`](#insn-00b4ce0c)
- ブロック [`00b4ce0c`](#insn-00b4ce0c) 範囲 `[['00b4ce0c', '00b4ce1b']]`

## 命令位置別の参照

- [`00b4cddc`](#insn-00b4cddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cde0`](#insn-00b4cde0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cdec`](#insn-00b4cdec) → `01126c78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cdf0`](#insn-00b4cdf0) → [`00b4ce0c`](#insn-00b4ce0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cdf8`](#insn-00b4cdf8) → `002a7253`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ce00`](#insn-00b4ce00) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce08`](#insn-00b4ce08) → `01126c78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ce0c`](#insn-00b4ce0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4cddc`](#insn-00b4cddc)

~~~json
{
  "source": "00b4cddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cde0`](#insn-00b4cde0)

~~~json
{
  "source": "00b4cde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cdec`](#insn-00b4cdec)

~~~json
{
  "source": "00b4cdec",
  "target": "01126c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cdf0`](#insn-00b4cdf0)

~~~json
{
  "source": "00b4cdf0",
  "target": "00b4ce0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cdf8`](#insn-00b4cdf8)

~~~json
{
  "source": "00b4cdf8",
  "target": "002a7253",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7253",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002a7253",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4ce00`](#insn-00b4ce00)

~~~json
{
  "source": "00b4ce00",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce08`](#insn-00b4ce08)

~~~json
{
  "source": "00b4ce08",
  "target": "01126c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ce0c`](#insn-00b4ce0c)

~~~json
{
  "source": "00b4ce0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
