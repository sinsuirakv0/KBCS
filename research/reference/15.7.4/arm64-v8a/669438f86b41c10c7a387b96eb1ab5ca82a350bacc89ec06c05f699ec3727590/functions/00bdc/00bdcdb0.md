# 00bdcdb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-65a2f67c31b1f8192fed2791220ff90b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59800`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59800.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-c1047b7340bfbbb2c5a209dd7b39736b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdb0",
  "name": "_ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5244bc4111b04157be017952fe9d706323a19e73b91b1cade6720d855794cd21",
  "source_text_sha256": "5244bc4111b04157be017952fe9d706323a19e73b91b1cade6720d855794cd21",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdb0",
        "00bdcdbf"
      ]
    ],
    "bytes_sha256": "6831154d50b7ce290eb3f7011870e5b754f247f862d0450e64f271d5b4e93634",
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
  (*(code *)PTR__ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE_00c1cf90)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdb0"></a> `00bdcdb0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdb4"></a> `00bdcdb4` | `11 ca 47 f9` | ldr x17,[x16, #0xf90] | `FALL_THROUGH`
<a id="insn-00bdcdb8"></a> `00bdcdb8` | `10 42 3e 91` | add x16,x16,#0xf90 | `FALL_THROUGH`
<a id="insn-00bdcdbc"></a> `00bdcdbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdb0`](#insn-00bdcdb0) 範囲 `[['00bdcdb0', '00bdcdbf']]`

## 命令位置別の参照

- [`00bdcdb4`](#insn-00bdcdb4) → `00c1cf90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdbc`](#insn-00bdcdbc) → [`004e85ec`](../004e8/004e85ec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e85ec` · 推定シンボル `_ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdb4`](#insn-00bdcdb4)

~~~json
{
  "source": "00bdcdb4",
  "target": "00c1cf90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcdbc`](#insn-00bdcdbc)

~~~json
{
  "source": "00bdcdbc",
  "target": "004e85ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
