# 00bbbfb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbbf14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-09a566895a11a4fe17c67bd16f1ea4b4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbcfa4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcfa4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-cdd9e6a302dc74e88a5476a8fe812c16)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbfb0",
  "name": "_ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "15c3c6e3c8d64060505853443549540936f800898ddbf9858dde16c470c8c9cc",
  "source_text_sha256": "15c3c6e3c8d64060505853443549540936f800898ddbf9858dde16c470c8c9cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbfb0",
        "00bbc003"
      ]
    ],
    "bytes_sha256": "4dd7902024642071a340f70f42f38795b6b64c747d402fa2315a7e59703ba15d",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a88](../00497/00497a88.md)
- [00c5b150](../00c5b/00c5b150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 406 bytes

~~~c

bool _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01126460 != 0) {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00bbbfcc to 00cbbfef has its CatchHandler @ 00bbc808 */
    cVar1 = FUN_00497a88(uVar2,DAT_01126498,DAT_011263e0);
    return cVar1 != '\0';
  }
  return DAT_01126504 == 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbfb0"></a> `00bbbfb0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbbfb4"></a> `00bbbfb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbfb8"></a> `00bbbfb8` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbfbc"></a> `00bbbfbc` | `00 31 42 f9` | ldr x0,[x8, #0x460] | `FALL_THROUGH`
<a id="insn-00bbbfc0"></a> `00bbbfc0` | `60 01 00 b4` | cbz x0,0x00bbbfec | `CONDITIONAL_JUMP`
<a id="insn-00bbbfc4"></a> `00bbbfc4` | `63 7c 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbfc8"></a> `00bbbfc8` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbfcc"></a> `00bbbfcc` | `49 2b 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbfd0"></a> `00bbbfd0` | `01 4d 42 f9` | ldr x1,[x8, #0x498] | `FALL_THROUGH`
<a id="insn-00bbbfd4"></a> `00bbbfd4` | `22 f1 41 f9` | ldr x2,[x9, #0x3e0] | `FALL_THROUGH`
<a id="insn-00bbbfd8"></a> `00bbbfd8` | `ac 6e e3 97` | bl 0x00497a88 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbfdc"></a> `00bbbfdc` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbbfe0"></a> `00bbbfe0` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bbbfe4"></a> `00bbbfe4` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbbfe8"></a> `00bbbfe8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbfec"></a> `00bbbfec` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbff0"></a> `00bbbff0` | `08 05 45 b9` | ldr w8,[x8, #0x504] | `FALL_THROUGH`
<a id="insn-00bbbff4"></a> `00bbbff4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbff8"></a> `00bbbff8` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbbffc"></a> `00bbbffc` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbc000"></a> `00bbc000` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbfb0`](#insn-00bbbfb0) 範囲 `[['00bbbfb0', '00bbbfc3']]`
  - `CONDITIONAL_JUMP` [`00bbbfc0`](#insn-00bbbfc0) → [`00bbbfec`](#insn-00bbbfec)
  - `FALL_THROUGH` [`00bbbfc0`](#insn-00bbbfc0) → [`00bbbfc4`](#insn-00bbbfc4)
- ブロック [`00bbbfc4`](#insn-00bbbfc4) 範囲 `[['00bbbfc4', '00bbbfcb']]`
  - `FALL_THROUGH` [`00bbbfc8`](#insn-00bbbfc8) → [`00bbbfcc`](#insn-00bbbfcc)
- ブロック [`00bbbfcc`](#insn-00bbbfcc) 範囲 `[['00bbbfcc', '00bbbfeb']]`
- ブロック [`00bbbfec`](#insn-00bbbfec) 範囲 `[['00bbbfec', '00bbc003']]`

## 命令位置別の参照

- [`00bbbfb0`](#insn-00bbbfb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfbc`](#insn-00bbbfbc) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbfc0`](#insn-00bbbfc0) → [`00bbbfec`](#insn-00bbbfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfc4`](#insn-00bbbfc4) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfd0`](#insn-00bbbfd0) → `01126498`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbfd4`](#insn-00bbbfd4) → `011263e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbfd8`](#insn-00bbbfd8) → [`00497a88`](../00497/00497a88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a88` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfe4`](#insn-00bbbfe4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbff0`](#insn-00bbbff0) → `01126504`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbbffc`](#insn-00bbbffc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbfb0`](#insn-00bbbfb0)

~~~json
{
  "source": "00bbbfb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfbc`](#insn-00bbbfbc)

~~~json
{
  "source": "00bbbfbc",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbfc0`](#insn-00bbbfc0)

~~~json
{
  "source": "00bbbfc0",
  "target": "00bbbfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfc4`](#insn-00bbbfc4)

~~~json
{
  "source": "00bbbfc4",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbfd0`](#insn-00bbbfd0)

~~~json
{
  "source": "00bbbfd0",
  "target": "01126498",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126498",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbfd4`](#insn-00bbbfd4)

~~~json
{
  "source": "00bbbfd4",
  "target": "011263e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbfd8`](#insn-00bbbfd8)

~~~json
{
  "source": "00bbbfd8",
  "target": "00497a88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbfe4`](#insn-00bbbfe4)

~~~json
{
  "source": "00bbbfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbff0`](#insn-00bbbff0)

~~~json
{
  "source": "00bbbff0",
  "target": "01126504",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126504",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbffc`](#insn-00bbbffc)

~~~json
{
  "source": "00bbbffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
