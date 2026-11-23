# 00bdcfa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdd050`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd050.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0015.md#compare-2415921482225d851322925b7b6189f3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfa0",
  "name": "_ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8ResponseEEENS7_ISF_EEEERKNS2_IPNS_17Certificate_StoreENS7_ISL_EEEENS1_6chrono10time_pointINSQ_12system_clockENSQ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d47cbd379fd22c2a7a2683ebea32a6a0ef5b45029b7ba6f549c41a2ed1a9d841",
  "source_text_sha256": "d47cbd379fd22c2a7a2683ebea32a6a0ef5b45029b7ba6f549c41a2ed1a9d841",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfa0",
        "00bdcfaf"
      ]
    ],
    "bytes_sha256": "d20c56700dd87c9c04d095950c1c8f7215d28bffae199db21d4ab851eacf6d71",
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

- [00504f50](../00504/00504f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 659 bytes

~~~c

void _ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8ResponseEEENS7_ISF_EEEERKNS2_IPNS_17Certificate_StoreENS7_ISL_EEEENS1_6chrono10time_pointINSQ_12system_clockENSQ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8ResponseEEENS7_ISF_EEEERKNS2_IPNS_17Certificate_StoreENS7_ISL_EEEENS1_6chrono10time_pointINSQ_12system_clockENSQ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE_00c1d008
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfa0"></a> `00bdcfa0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfa4"></a> `00bdcfa4` | `11 06 40 f9` | ldr x17,[x16, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcfa8"></a> `00bdcfa8` | `10 22 00 91` | add x16,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcfac"></a> `00bdcfac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfa0`](#insn-00bdcfa0) 範囲 `[['00bdcfa0', '00bdcfaf']]`

## 命令位置別の参照

- [`00bdcfa4`](#insn-00bdcfa4) → `00c1d008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfac`](#insn-00bdcfac) → [`00504f50`](../00504/00504f50.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00504f50` · 推定シンボル `_ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8ResponseEEENS7_ISF_EEEERKNS2_IPNS_17Certificate_StoreENS7_ISL_EEEENS1_6chrono10time_pointINSQ_12system_clockENSQ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfa4`](#insn-00bdcfa4)

~~~json
{
  "source": "00bdcfa4",
  "target": "00c1d008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfac`](#insn-00bdcfac)

~~~json
{
  "source": "00bdcfac",
  "target": "00504f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
