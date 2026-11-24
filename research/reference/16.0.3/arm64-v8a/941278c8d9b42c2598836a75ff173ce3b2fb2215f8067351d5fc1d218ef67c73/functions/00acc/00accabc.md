# 00accabc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbac8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbac8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-b90ad4d51af0ebcc9bcd9c9acdf6d490)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00accabc",
  "name": "FUN_00accabc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82165e92b1bd63f45e815f18888727750414bae45669282811cd36dc887c9dce",
  "source_text_sha256": "82165e92b1bd63f45e815f18888727750414bae45669282811cd36dc887c9dce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00accabc",
        "00accaeb"
      ]
    ],
    "bytes_sha256": "63a0dbef407e4908f56675596c7125078143f44da1d8401c2b33ea57b8797831",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007322cc](../00732/007322cc.md)
- [0093659c](../00936/0093659c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 399 bytes

~~~c

void FUN_00accabc(undefined8 *param_1,undefined4 param_2,undefined4 param_3)

{
  *param_1 = &PTR_FUN_00c8e960;
  *(undefined4 *)(param_1 + 1) = param_2;
  *(undefined4 *)((long)param_1 + 0xc) = param_3;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  *(undefined1 *)(param_1 + 5) = 1;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[10] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00accabc"></a> `00accabc` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00accac0"></a> `00accac0` | `08 0e 00 d0` | adrp x8,0xc8e000 | `FALL_THROUGH`
<a id="insn-00accac4"></a> `00accac4` | `08 81 25 91` | add x8,x8,#0x960 | `FALL_THROUGH`
<a id="insn-00accac8"></a> `00accac8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00accacc"></a> `00accacc` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00accad0"></a> `00accad0` | `01 08 01 29` | stp w1,w2,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00accad4"></a> `00accad4` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00accad8"></a> `00accad8` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00accadc"></a> `00accadc` | `08 a0 00 39` | strb w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00accae0"></a> `00accae0` | `00 80 01 ad` | stp q0,q0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00accae4"></a> `00accae4` | `1f 28 00 f9` | str xzr,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00accae8"></a> `00accae8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00accabc`](#insn-00accabc) 範囲 `[['00accabc', '00accaeb']]`

## 命令位置別の参照

- [`00accac8`](#insn-00accac8) → `00c8e960`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00accac8`](#insn-00accac8)

~~~json
{
  "source": "00accac8",
  "target": "00c8e960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
