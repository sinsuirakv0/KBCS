# 00acbac8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acba58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba58.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-fd731a4df7a9343c3e33401e6b8e37bc)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00accabc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accabc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-b90ad4d51af0ebcc9bcd9c9acdf6d490)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbac8",
  "name": "FUN_00acbac8",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4da900e1450aeeb0affa86612031bc974aac8a1c9bf375257154a4ff5c354f91",
  "source_text_sha256": "4da900e1450aeeb0affa86612031bc974aac8a1c9bf375257154a4ff5c354f91",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbac8",
        "00acbaf7"
      ]
    ],
    "bytes_sha256": "9e294b0932679777c1a08ef725d24cecec26e8fedafb71c101893437a35b9820",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00731f1c](../00731/00731f1c.md)
- [009355f0](../00935/009355f0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 399 bytes

~~~c

void FUN_00acbac8(undefined8 *param_1,undefined4 param_2,undefined4 param_3)

{
  *param_1 = &PTR_FUN_00c8d990;
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
<a id="insn-00acbac8"></a> `00acbac8` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00acbacc"></a> `00acbacc` | `08 0e 00 d0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00acbad0"></a> `00acbad0` | `08 41 26 91` | add x8,x8,#0x990 | `FALL_THROUGH`
<a id="insn-00acbad4"></a> `00acbad4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbad8"></a> `00acbad8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acbadc"></a> `00acbadc` | `01 08 01 29` | stp w1,w2,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acbae0"></a> `00acbae0` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00acbae4"></a> `00acbae4` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acbae8"></a> `00acbae8` | `08 a0 00 39` | strb w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acbaec"></a> `00acbaec` | `00 80 01 ad` | stp q0,q0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00acbaf0"></a> `00acbaf0` | `1f 28 00 f9` | str xzr,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00acbaf4"></a> `00acbaf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbac8`](#insn-00acbac8) 範囲 `[['00acbac8', '00acbaf7']]`

## 命令位置別の参照

- [`00acbad4`](#insn-00acbad4) → `00c8d990`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbad4`](#insn-00acbad4)

~~~json
{
  "source": "00acbad4",
  "target": "00c8d990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d990",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
