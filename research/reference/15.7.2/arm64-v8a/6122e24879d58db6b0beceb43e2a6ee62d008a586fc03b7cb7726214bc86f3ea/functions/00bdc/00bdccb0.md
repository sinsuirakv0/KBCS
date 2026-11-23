# 00bdccb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-d8f6e955f0e8cb888a2eb4a80daa63a1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccb0",
  "name": "_ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b6e2ffbc34932c38736e6ceb0cccd9a2d25fcea300bd1a0ef209b93e9fa53c22",
  "source_text_sha256": "b6e2ffbc34932c38736e6ceb0cccd9a2d25fcea300bd1a0ef209b93e9fa53c22",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccb0",
        "00bdccbf"
      ]
    ],
    "bytes_sha256": "5fa22da4e411d94880f85782defe73343917b60ea91928a119ba1af58a765505",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e8a14](../004e8/004e8a14.md)

## 呼び出し先

- [004e85ec](../004e8/004e85ec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 193 bytes

~~~c

void _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE(void)

{
  (*(code *)PTR__ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE_00c1ce90)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccb0"></a> `00bdccb0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdccb4"></a> `00bdccb4` | `11 4a 47 f9` | ldr x17,[x16, #0xe90] | `FALL_THROUGH`
<a id="insn-00bdccb8"></a> `00bdccb8` | `10 42 3a 91` | add x16,x16,#0xe90 | `FALL_THROUGH`
<a id="insn-00bdccbc"></a> `00bdccbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccb0`](#insn-00bdccb0) 範囲 `[['00bdccb0', '00bdccbf']]`

## 命令位置別の参照

- [`00bdccb4`](#insn-00bdccb4) → `00c1ce90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdccbc`](#insn-00bdccbc) → [`004e85ec`](../004e8/004e85ec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e85ec` · 推定シンボル `_ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccb4`](#insn-00bdccb4)

~~~json
{
  "source": "00bdccb4",
  "target": "00c1ce90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdccbc`](#insn-00bdccbc)

~~~json
{
  "source": "00bdccbc",
  "target": "004e85ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
