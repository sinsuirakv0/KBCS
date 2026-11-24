# 00bbcff8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbc004`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc004.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-061d951015cae620badd84e0771b7246)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcff8",
  "name": "_ZN8firebase9messaging34SetDeliveryMetricsExportToBigQueryEb",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28da93111c5b057f822badcea7f6e619a4e3f224a9e7924d2a3ee3bcd188b6ba",
  "source_text_sha256": "28da93111c5b057f822badcea7f6e619a4e3f224a9e7924d2a3ee3bcd188b6ba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcff8",
        "00bbd05b"
      ]
    ],
    "bytes_sha256": "9a061633737dd7f8e98eb55ae1a5ef83abab0593e5c40b643f4fbce9f962dcb2",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0057504c](../00575/0057504c.md)
- [00c5c120](../00c5c/00c5c120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 454 bytes

~~~c

void _ZN8firebase9messaging34SetDeliveryMetricsExportToBigQueryEb(uint param_1)

{
  undefined8 uVar1;
  
  if (DAT_01127420 != 0) {
                    /* try { // try from 00bbd014 to 00cbd01f has its CatchHandler @ 00bbd7dc */
    uVar1 = _ZNK8firebase3App9GetJNIEnvEv(DAT_01127420);
    FUN_0057504c(uVar1,DAT_01127458,DAT_011273a8,param_1 & 1);
    return;
  }
  DAT_011274c4 = 1;
  if ((param_1 & 1) == 0) {
    DAT_011274c4 = 2;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcff8"></a> `00bbcff8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbcffc"></a> `00bbcffc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd000"></a> `00bbd000` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbd004"></a> `00bbd004` | `48 2b 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbd008"></a> `00bbd008` | `08 11 42 f9` | ldr x8,[x8, #0x420] | `FALL_THROUGH`
<a id="insn-00bbd00c"></a> `00bbd00c` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bbd010"></a> `00bbd010` | `68 01 00 b4` | cbz x8,0x00bbd03c | `CONDITIONAL_JUMP`
<a id="insn-00bbd014"></a> `00bbd014` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbd018"></a> `00bbd018` | `42 7c 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd01c"></a> `00bbd01c` | `48 2b 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbd020"></a> `00bbd020` | `49 2b 00 d0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbd024"></a> `00bbd024` | `01 2d 42 f9` | ldr x1,[x8, #0x458] | `FALL_THROUGH`
<a id="insn-00bbd028"></a> `00bbd028` | `22 d5 41 f9` | ldr x2,[x9, #0x3a8] | `FALL_THROUGH`
<a id="insn-00bbd02c"></a> `00bbd02c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd030"></a> `00bbd030` | `63 02 00 12` | and w3,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd034"></a> `00bbd034` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbd038"></a> `00bbd038` | `05 e0 e6 17` | b 0x0057504c | `CALL_TERMINATOR`
<a id="insn-00bbd03c"></a> `00bbd03c` | `7f 02 00 72` | tst w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd040"></a> `00bbd040` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd044"></a> `00bbd044` | `08 15 88 1a` | cinc w8,w8,eq | `FALL_THROUGH`
<a id="insn-00bbd048"></a> `00bbd048` | `49 2b 00 d0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbd04c"></a> `00bbd04c` | `28 c5 04 b9` | str w8,[x9, #0x4c4] | `FALL_THROUGH`
<a id="insn-00bbd050"></a> `00bbd050` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd054"></a> `00bbd054` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbd058"></a> `00bbd058` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcff8`](#insn-00bbcff8) 範囲 `[['00bbcff8', '00bbd013']]`
  - `CONDITIONAL_JUMP` [`00bbd010`](#insn-00bbd010) → [`00bbd03c`](#insn-00bbd03c)
  - `FALL_THROUGH` [`00bbd010`](#insn-00bbd010) → [`00bbd014`](#insn-00bbd014)
- ブロック [`00bbd014`](#insn-00bbd014) 範囲 `[['00bbd014', '00bbd03b']]`
- ブロック [`00bbd03c`](#insn-00bbd03c) 範囲 `[['00bbd03c', '00bbd05b']]`

## 命令位置別の参照

- [`00bbcff8`](#insn-00bbcff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcffc`](#insn-00bbcffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd008`](#insn-00bbd008) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbd010`](#insn-00bbd010) → [`00bbd03c`](#insn-00bbd03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd018`](#insn-00bbd018) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bbd024`](#insn-00bbd024) → `01127458`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbd028`](#insn-00bbd028) → `011273a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbd02c`](#insn-00bbd02c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd038`](#insn-00bbd038) → [`0057504c`](../00575/0057504c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057504c` · 推定シンボル `None` · 推定型 `None`
- [`00bbd04c`](#insn-00bbd04c) → `011274c4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbd050`](#insn-00bbd050) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcff8`](#insn-00bbcff8)

~~~json
{
  "source": "00bbcff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcffc`](#insn-00bbcffc)

~~~json
{
  "source": "00bbcffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd008`](#insn-00bbd008)

~~~json
{
  "source": "00bbd008",
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
- 参照命令 [`00bbd010`](#insn-00bbd010)

~~~json
{
  "source": "00bbd010",
  "target": "00bbd03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd018`](#insn-00bbd018)

~~~json
{
  "source": "00bbd018",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd024`](#insn-00bbd024)

~~~json
{
  "source": "00bbd024",
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
- 参照命令 [`00bbd028`](#insn-00bbd028)

~~~json
{
  "source": "00bbd028",
  "target": "011273a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbd02c`](#insn-00bbd02c)

~~~json
{
  "source": "00bbd02c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd038`](#insn-00bbd038)

~~~json
{
  "source": "00bbd038",
  "target": "0057504c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd04c`](#insn-00bbd04c)

~~~json
{
  "source": "00bbd04c",
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
- 参照命令 [`00bbd050`](#insn-00bbd050)

~~~json
{
  "source": "00bbd050",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
