# 00bdcfb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdd060`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd060.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0015.md#compare-3938b20599e23e1adbffd3e9ebda37fd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfb0",
  "name": "_ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7_ISE_EEEENS1_6chrono10time_pointINSJ_12system_clockENSJ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81159988e6d9291fae76616c39a295ba8d8e6d5f2eace1d5fc1b4413ab14d219",
  "source_text_sha256": "81159988e6d9291fae76616c39a295ba8d8e6d5f2eace1d5fc1b4413ab14d219",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfb0",
        "00bdcfbf"
      ]
    ],
    "bytes_sha256": "29ce979ceef3f6e87a87d80a3d473ccb5037b10b1fafbac963c751b75e5dfb8f",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005060a8](../00506/005060a8.md)

## 呼び出し先

- [005054cc](../00505/005054cc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 656 bytes

~~~c

void _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7_ISE_EEEENS1_6chrono10time_pointINSJ_12system_clockENSJ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE
               (void)

{
                    /* try { // try from 00bdcfb0 to 00cdd21b has its CatchHandler @ 00bdcbcc */
  (*(code *)
    PTR__ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7_ISE_EEEENS1_6chrono10time_pointINSJ_12system_clockENSJ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE_00c1d010
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfb0"></a> `00bdcfb0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfb4"></a> `00bdcfb4` | `11 0a 40 f9` | ldr x17,[x16, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcfb8"></a> `00bdcfb8` | `10 42 00 91` | add x16,x16,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcfbc"></a> `00bdcfbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfb0`](#insn-00bdcfb0) 範囲 `[['00bdcfb0', '00bdcfbf']]`

## 命令位置別の参照

- [`00bdcfb4`](#insn-00bdcfb4) → `00c1d010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfbc`](#insn-00bdcfbc) → [`005054cc`](../00505/005054cc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `005054cc` · 推定シンボル `_ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7_ISE_EEEENS1_6chrono10time_pointINSJ_12system_clockENSJ_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfb4`](#insn-00bdcfb4)

~~~json
{
  "source": "00bdcfb4",
  "target": "00c1d010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfbc`](#insn-00bdcfbc)

~~~json
{
  "source": "00bdcfbc",
  "target": "005054cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
