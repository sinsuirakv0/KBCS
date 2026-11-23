# 00bdcfd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdd080`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd080.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0015.md#compare-b75303e08076369be15b58268f0ac48a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfd0",
  "name": "_ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEERKSB_SE_bb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f65c0dfadf5aca6dcfd5f872fba4101c0450439c2cc197c929468b0bf598f72f",
  "source_text_sha256": "f65c0dfadf5aca6dcfd5f872fba4101c0450439c2cc197c929468b0bf598f72f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfd0",
        "00bdcfdf"
      ]
    ],
    "bytes_sha256": "5ec02e9576689fe7458cdd77b12e13e8556ae5ad7201484a2dbec439302fec37",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00508860](../00508/00508860.md)

## 呼び出し先

- [00508250](../00508/00508250.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 395 bytes

~~~c

void _ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEERKSB_SE_bb
               (void)

{
  (*(code *)
    PTR__ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEERKSB_SE_bb_00c1d020
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfd0"></a> `00bdcfd0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfd4"></a> `00bdcfd4` | `11 12 40 f9` | ldr x17,[x16, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcfd8"></a> `00bdcfd8` | `10 82 00 91` | add x16,x16,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcfdc"></a> `00bdcfdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfd0`](#insn-00bdcfd0) 範囲 `[['00bdcfd0', '00bdcfdf']]`

## 命令位置別の参照

- [`00bdcfd4`](#insn-00bdcfd4) → `00c1d020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfdc`](#insn-00bdcfdc) → [`00508250`](../00508/00508250.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00508250` · 推定シンボル `_ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEERKSB_SE_bb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfd4`](#insn-00bdcfd4)

~~~json
{
  "source": "00bdcfd4",
  "target": "00c1d020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d020",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfdc`](#insn-00bdcfdc)

~~~json
{
  "source": "00bdcfdc",
  "target": "00508250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
