# 00bdcff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdd0a0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0a0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0015.md#compare-4ef03c01dc19b8519c55f9311e16f584)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcff0",
  "name": "_ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS_17Certificate_StoreENS3_ISC_EEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS3_IcEEEENS_10Usage_TypeENS0_6chrono10time_pointINSP_12system_clockENSP_8durationIxNS0_5ratioILl1ELl1000000EEEEEEENSS_IxNST_ILl1ELl1000EEEEERKNS1_INS0_10shared_ptrIKNS_4OCSP8ResponseEEENS3_IS13_EEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "503aff3f1dd6f2b898daaf0337dfc35c0dfcdd6d4cadd14d72786bde9c71b473",
  "source_text_sha256": "503aff3f1dd6f2b898daaf0337dfc35c0dfcdd6d4cadd14d72786bde9c71b473",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcff0",
        "00bdcfff"
      ]
    ],
    "bytes_sha256": "097faca9c438f6d4cbca07fc748d8dc08ebbd2ee93e58dbe8467fdebe3b02ee9",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00509740](../00509/00509740.md)
- [0050986c](../00509/0050986c.md)
- [0050995c](../00509/0050995c.md)

## 呼び出し先

- [00508860](../00508/00508860.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 913 bytes

~~~c

void _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS_17Certificate_StoreENS3_ISC_EEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS3_IcEEEENS_10Usage_TypeENS0_6chrono10time_pointINSP_12system_clockENSP_8durationIxNS0_5ratioILl1ELl1000000EEEEEEENSS_IxNST_ILl1ELl1000EEEEERKNS1_INS0_10shared_ptrIKNS_4OCSP8ResponseEEENS3_IS13_EEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS_17Certificate_StoreENS3_ISC_EEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS3_IcEEEENS_10Usage_TypeENS0_6chrono10time_pointINSP_12system_clockENSP_8durationIxNS0_5ratioILl1ELl1000000EEEEEEENSS_IxNST_ILl1ELl1000EEEEERKNS1_INS0_10shared_ptrIKNS_4OCSP8ResponseEEENS3_IS13_EEEE_00c1d030
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcff0"></a> `00bdcff0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcff4"></a> `00bdcff4` | `11 1a 40 f9` | ldr x17,[x16, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcff8"></a> `00bdcff8` | `10 c2 00 91` | add x16,x16,#0x30 | `FALL_THROUGH`
<a id="insn-00bdcffc"></a> `00bdcffc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcff0`](#insn-00bdcff0) 範囲 `[['00bdcff0', '00bdcfff']]`

## 命令位置別の参照

- [`00bdcff4`](#insn-00bdcff4) → `00c1d030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcffc`](#insn-00bdcffc) → [`00508860`](../00508/00508860.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00508860` · 推定シンボル `_ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS_17Certificate_StoreENS3_ISC_EEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS3_IcEEEENS_10Usage_TypeENS0_6chrono10time_pointINSP_12system_clockENSP_8durationIxNS0_5ratioILl1ELl1000000EEEEEEENSS_IxNST_ILl1ELl1000EEEEERKNS1_INS0_10shared_ptrIKNS_4OCSP8ResponseEEENS3_IS13_EEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcff4`](#insn-00bdcff4)

~~~json
{
  "source": "00bdcff4",
  "target": "00c1d030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcffc`](#insn-00bdcffc)

~~~json
{
  "source": "00bdcffc",
  "target": "00508860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
