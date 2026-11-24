# 00af1fbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0082.md#review-301f76c1bc1c2c9fe08283b6ca2eedca)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af1fbc",
  "name": "FUN_00af1fbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f0b5381d6ecbf1920abedd87bb2466d8ef552dba9ca4d78266ae8c6f4aca43d",
  "source_text_sha256": "6f0b5381d6ecbf1920abedd87bb2466d8ef552dba9ca4d78266ae8c6f4aca43d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af1fbc",
        "00af1fcf"
      ]
    ],
    "bytes_sha256": "31862a31869ee0dbb947ff9bfd6e0964c3ecb5f4d2290250a0607922b717e9d3",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 625 bytes

~~~c

void FUN_00af1fbc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
                    /* catch() { ... } // from try @ 00af1e20 with catch @ 00af1fbc
                       try { // try from 00af1fbc to 00bf2047 has its CatchHandler @ 00af1d34 */
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* catch() { ... } // from try @ 00af1de0 with catch @ 00af1fc4 */
  *param_2 = &PTR_FUN_00c8f818;
  param_2[1] = uVar1;
                    /* catch() { ... } // from try @ 00af1e44 with catch @ 00af1fcc
                       catch() { ... } // from try @ 00af1fb8 with catch @ 00af1fcc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af1fbc"></a> `00af1fbc` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af1fc0"></a> `00af1fc0` | `e9 0c 00 d0` | adrp x9,0xc8f000 | `FALL_THROUGH`
<a id="insn-00af1fc4"></a> `00af1fc4` | `29 61 20 91` | add x9,x9,#0x818 | `FALL_THROUGH`
<a id="insn-00af1fc8"></a> `00af1fc8` | `29 20 00 a9` | stp x9,x8,[x1] | `FALL_THROUGH`
<a id="insn-00af1fcc"></a> `00af1fcc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af1fbc`](#insn-00af1fbc) 範囲 `[['00af1fbc', '00af1fc3']]`
  - `FALL_THROUGH` [`00af1fc0`](#insn-00af1fc0) → [`00af1fc4`](#insn-00af1fc4)
- ブロック [`00af1fc4`](#insn-00af1fc4) 範囲 `[['00af1fc4', '00af1fcb']]`
  - `FALL_THROUGH` [`00af1fc8`](#insn-00af1fc8) → [`00af1fcc`](#insn-00af1fcc)
- ブロック [`00af1fcc`](#insn-00af1fcc) 範囲 `[['00af1fcc', '00af1fcf']]`

## 命令位置別の参照

- [`00af1fc8`](#insn-00af1fc8) → `00c8f818`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af1fc8`](#insn-00af1fc8)

~~~json
{
  "source": "00af1fc8",
  "target": "00c8f818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8f818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
