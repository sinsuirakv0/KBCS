# 00bbcfa4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbbfb0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-cdd9e6a302dc74e88a5476a8fe812c16)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcfa4",
  "name": "_ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69756d9228dc769cb36488bb4f810b262950e33dc635b50a27cfce17f69b34d1",
  "source_text_sha256": "69756d9228dc769cb36488bb4f810b262950e33dc635b50a27cfce17f69b34d1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcfa4",
        "00bbcff7"
      ]
    ],
    "bytes_sha256": "7790f420473731ae33d1c81b83b67c55992bf8c7afd89f82fb36e4ca0d84ec82",
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

- [00497da8](../00497/00497da8.md)
- [00c5c120](../00c5c/00c5c120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 406 bytes

~~~c

bool _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01127420 != 0) {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00bbcfc0 to 00cbcfe3 has its CatchHandler @ 00bbd7fc */
    cVar1 = FUN_00497da8(uVar2,DAT_01127458,DAT_011273a0);
    return cVar1 != '\0';
  }
  return DAT_011274c4 == 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcfa4"></a> `00bbcfa4` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbcfa8"></a> `00bbcfa8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbcfac"></a> `00bbcfac` | `48 2b 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcfb0"></a> `00bbcfb0` | `00 11 42 f9` | ldr x0,[x8, #0x420] | `FALL_THROUGH`
<a id="insn-00bbcfb4"></a> `00bbcfb4` | `60 01 00 b4` | cbz x0,0x00bbcfe0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcfb8"></a> `00bbcfb8` | `5a 7c 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfbc"></a> `00bbcfbc` | `48 2b 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcfc0"></a> `00bbcfc0` | `49 2b 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcfc4"></a> `00bbcfc4` | `01 2d 42 f9` | ldr x1,[x8, #0x458] | `FALL_THROUGH`
<a id="insn-00bbcfc8"></a> `00bbcfc8` | `22 d1 41 f9` | ldr x2,[x9, #0x3a0] | `FALL_THROUGH`
<a id="insn-00bbcfcc"></a> `00bbcfcc` | `77 6b e3 97` | bl 0x00497da8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfd0"></a> `00bbcfd0` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbcfd4"></a> `00bbcfd4` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bbcfd8"></a> `00bbcfd8` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbcfdc"></a> `00bbcfdc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbcfe0"></a> `00bbcfe0` | `48 2b 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcfe4"></a> `00bbcfe4` | `08 c5 44 b9` | ldr w8,[x8, #0x4c4] | `FALL_THROUGH`
<a id="insn-00bbcfe8"></a> `00bbcfe8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcfec"></a> `00bbcfec` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbcff0"></a> `00bbcff0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbcff4"></a> `00bbcff4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcfa4`](#insn-00bbcfa4) 範囲 `[['00bbcfa4', '00bbcfb7']]`
  - `CONDITIONAL_JUMP` [`00bbcfb4`](#insn-00bbcfb4) → [`00bbcfe0`](#insn-00bbcfe0)
  - `FALL_THROUGH` [`00bbcfb4`](#insn-00bbcfb4) → [`00bbcfb8`](#insn-00bbcfb8)
- ブロック [`00bbcfb8`](#insn-00bbcfb8) 範囲 `[['00bbcfb8', '00bbcfbf']]`
  - `FALL_THROUGH` [`00bbcfbc`](#insn-00bbcfbc) → [`00bbcfc0`](#insn-00bbcfc0)
- ブロック [`00bbcfc0`](#insn-00bbcfc0) 範囲 `[['00bbcfc0', '00bbcfdf']]`
- ブロック [`00bbcfe0`](#insn-00bbcfe0) 範囲 `[['00bbcfe0', '00bbcff7']]`

## 命令位置別の参照

- [`00bbcfa4`](#insn-00bbcfa4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfb0`](#insn-00bbcfb0) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcfb4`](#insn-00bbcfb4) → [`00bbcfe0`](#insn-00bbcfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfb8`](#insn-00bbcfb8) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfc4`](#insn-00bbcfc4) → `01127458`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcfc8`](#insn-00bbcfc8) → `011273a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcfcc`](#insn-00bbcfcc) → [`00497da8`](../00497/00497da8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497da8` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfd8`](#insn-00bbcfd8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfe4`](#insn-00bbcfe4) → `011274c4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbcff0`](#insn-00bbcff0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcfa4`](#insn-00bbcfa4)

~~~json
{
  "source": "00bbcfa4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfb0`](#insn-00bbcfb0)

~~~json
{
  "source": "00bbcfb0",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcfb4`](#insn-00bbcfb4)

~~~json
{
  "source": "00bbcfb4",
  "target": "00bbcfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfb8`](#insn-00bbcfb8)

~~~json
{
  "source": "00bbcfb8",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfc4`](#insn-00bbcfc4)

~~~json
{
  "source": "00bbcfc4",
  "target": "01127458",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127458",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcfc8`](#insn-00bbcfc8)

~~~json
{
  "source": "00bbcfc8",
  "target": "011273a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcfcc`](#insn-00bbcfcc)

~~~json
{
  "source": "00bbcfcc",
  "target": "00497da8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfd8`](#insn-00bbcfd8)

~~~json
{
  "source": "00bbcfd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfe4`](#insn-00bbcfe4)

~~~json
{
  "source": "00bbcfe4",
  "target": "011274c4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011274c4",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcff0`](#insn-00bbcff0)

~~~json
{
  "source": "00bbcff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
