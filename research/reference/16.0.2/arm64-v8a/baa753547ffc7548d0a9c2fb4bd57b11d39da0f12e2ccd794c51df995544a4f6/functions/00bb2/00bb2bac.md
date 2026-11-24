# 00bb2bac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb2b10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2b10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-e4322aae82520c02edc418e9d7cb1a8e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb3ba0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3ba0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-cae41d574db5844793fc5c99a9d6c6f8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb2bac",
  "name": "_ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e69b3f3ae5656ee822b49a48234c2efa13be03e785e304766e36a4bd976ca8a4",
  "source_text_sha256": "e69b3f3ae5656ee822b49a48234c2efa13be03e785e304766e36a4bd976ca8a4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb2bac",
        "00bb2bcf"
      ]
    ],
    "bytes_sha256": "5a3f1e8e457f17332c004ccf4c09f24b18f2a18fdc968922c09f76593632cec3",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
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

## 疑似コード / UTF-8 377 bytes

~~~c

undefined * _ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE(code *param_1)

{
  code *pcVar1;
  undefined *puVar2;
  
                    /* try { // try from 00bb2bac to 00cb2ea7 has its CatchHandler @ 00bb2b48 */
  pcVar1 = FUN_00bb2bd0;
  if (param_1 != (code *)0x0) {
    pcVar1 = param_1;
  }
  puVar2 = PTR_FUN_00ca4780;
  PTR_FUN_00ca4780 = pcVar1;
  return puVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb2bac"></a> `00bb2bac` | `89 07 00 d0` | adrp x9,0xca4000 | `FALL_THROUGH`
<a id="insn-00bb2bb0"></a> `00bb2bb0` | `28 c1 43 f9` | ldr x8,[x9, #0x780] | `FALL_THROUGH`
<a id="insn-00bb2bb4"></a> `00bb2bb4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bb2bb8"></a> `00bb2bb8` | `ca 00 00 10` | adr x10,0xbb2bd0 | `FALL_THROUGH`
<a id="insn-00bb2bbc"></a> `00bb2bbc` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bb2bc0"></a> `00bb2bc0` | `4a 01 80 9a` | csel x10,x10,x0,eq | `FALL_THROUGH`
<a id="insn-00bb2bc4"></a> `00bb2bc4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bb2bc8"></a> `00bb2bc8` | `2a c1 03 f9` | str x10,[x9, #0x780] | `FALL_THROUGH`
<a id="insn-00bb2bcc"></a> `00bb2bcc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb2bac`](#insn-00bb2bac) 範囲 `[['00bb2bac', '00bb2bcf']]`

## 命令位置別の参照

- [`00bb2bb0`](#insn-00bb2bb0) → `00ca4780`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb2bc4`](#insn-00bb2bc4) → [`00bb2bd0`](00bb2bd0.md) · `DATA` · `ANALYSIS` · 関数 `00bb2bd0` · 推定シンボル `None` · 推定型 `None`
- [`00bb2bc8`](#insn-00bb2bc8) → `00ca4780`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb2bc8`](#insn-00bb2bc8) → [`00bb2bd0`](00bb2bd0.md) · `DATA` · `ANALYSIS` · 関数 `00bb2bd0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb2bb0`](#insn-00bb2bb0)

~~~json
{
  "source": "00bb2bb0",
  "target": "00ca4780",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4780",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb2bc4`](#insn-00bb2bc4)

~~~json
{
  "source": "00bb2bc4",
  "target": "00bb2bd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb2bc8`](#insn-00bb2bc8)

~~~json
{
  "source": "00bb2bc8",
  "target": "00ca4780",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4780",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb2bc8`](#insn-00bb2bc8)

~~~json
{
  "source": "00bb2bc8",
  "target": "00bb2bd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
