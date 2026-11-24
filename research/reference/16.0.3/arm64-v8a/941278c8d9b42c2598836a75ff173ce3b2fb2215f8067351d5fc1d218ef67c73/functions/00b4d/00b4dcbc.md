# 00b4dcbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4ccc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ccc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-0fe1951a00694b47f1bcb98b9f9b6aa6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4dcbc",
  "name": "_ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f8ef49b0f30b2e6696905add74d8e97ad4de50b283701c7497fb349c03c0f1e",
  "source_text_sha256": "1f8ef49b0f30b2e6696905add74d8e97ad4de50b283701c7497fb349c03c0f1e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4dcbc",
        "00b4dcff"
      ]
    ],
    "bytes_sha256": "31c57cb1c7d3a025a45172eac57a221a5bd666632d4601cca700a2b8f5c72268",
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
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 595 bytes

~~~c

long _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00b4dcc4 to 00c4f373 has its CatchHandler @ 00b48f48 */
  if (DAT_01126d28 == 0) {
    DAT_01126d28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",param_3);
  }
  return DAT_01126d28;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4dcbc"></a> `00b4dcbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4dcc0"></a> `00b4dcc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dcc4"></a> `00b4dcc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4dcc8"></a> `00b4dcc8` | `d3 2e 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4dccc"></a> `00b4dccc` | `68 96 46 f9` | ldr x8,[x19, #0xd28] | `FALL_THROUGH`
<a id="insn-00b4dcd0"></a> `00b4dcd0` | `08 01 00 b5` | cbnz x8,0x00b4dcf0 | `CONDITIONAL_JUMP`
<a id="insn-00b4dcd4"></a> `00b4dcd4` | `a3 ba ff d0` | adrp x3,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b4dcd8"></a> `00b4dcd8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00b4dcdc"></a> `00b4dcdc` | `63 b4 2e 91` | add x3,x3,#0xbad | `FALL_THROUGH`
<a id="insn-00b4dce0"></a> `00b4dce0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4dce4"></a> `00b4dce4` | `b3 38 04 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dce8"></a> `00b4dce8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4dcec"></a> `00b4dcec` | `60 96 06 f9` | str x0,[x19, #0xd28] | `FALL_THROUGH`
<a id="insn-00b4dcf0"></a> `00b4dcf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dcf4"></a> `00b4dcf4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4dcf8"></a> `00b4dcf8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4dcfc"></a> `00b4dcfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4dcbc`](#insn-00b4dcbc) 範囲 `[['00b4dcbc', '00b4dcc3']]`
  - `FALL_THROUGH` [`00b4dcc0`](#insn-00b4dcc0) → [`00b4dcc4`](#insn-00b4dcc4)
- ブロック [`00b4dcc4`](#insn-00b4dcc4) 範囲 `[['00b4dcc4', '00b4dcd3']]`
  - `CONDITIONAL_JUMP` [`00b4dcd0`](#insn-00b4dcd0) → [`00b4dcf0`](#insn-00b4dcf0)
  - `FALL_THROUGH` [`00b4dcd0`](#insn-00b4dcd0) → [`00b4dcd4`](#insn-00b4dcd4)
- ブロック [`00b4dcd4`](#insn-00b4dcd4) 範囲 `[['00b4dcd4', '00b4dcef']]`
  - `FALL_THROUGH` [`00b4dcec`](#insn-00b4dcec) → [`00b4dcf0`](#insn-00b4dcf0)
- ブロック [`00b4dcf0`](#insn-00b4dcf0) 範囲 `[['00b4dcf0', '00b4dcff']]`

## 命令位置別の参照

- [`00b4dcbc`](#insn-00b4dcbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dcc0`](#insn-00b4dcc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dccc`](#insn-00b4dccc) → `01126d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4dcd0`](#insn-00b4dcd0) → [`00b4dcf0`](#insn-00b4dcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dcdc`](#insn-00b4dcdc) → `002a3bad`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4dce4`](#insn-00b4dce4) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00b4dcec`](#insn-00b4dcec) → `01126d28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4dcf0`](#insn-00b4dcf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4dcbc`](#insn-00b4dcbc)

~~~json
{
  "source": "00b4dcbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dcc0`](#insn-00b4dcc0)

~~~json
{
  "source": "00b4dcc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dccc`](#insn-00b4dccc)

~~~json
{
  "source": "00b4dccc",
  "target": "01126d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dcd0`](#insn-00b4dcd0)

~~~json
{
  "source": "00b4dcd0",
  "target": "00b4dcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dcdc`](#insn-00b4dcdc)

~~~json
{
  "source": "00b4dcdc",
  "target": "002a3bad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3bad",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002a3bad",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4dce4`](#insn-00b4dce4)

~~~json
{
  "source": "00b4dce4",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dcec`](#insn-00b4dcec)

~~~json
{
  "source": "00b4dcec",
  "target": "01126d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dcf0`](#insn-00b4dcf0)

~~~json
{
  "source": "00b4dcf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
