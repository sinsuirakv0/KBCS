# 00bdcdc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcd10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-3f7ba9198bd7ea5341141c40a47c0a33)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdce10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-b1e563cc5bd64a25e55ebb6dea7647d1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdc0",
  "name": "_ZNK5Botan4OCSP6CertID9is_id_forERKNS_16X509_CertificateES4_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e3364cc9b0bfc9fd44c4700a474f97f06dc86ed73d817bfc8b4432efb057f3a",
  "source_text_sha256": "5e3364cc9b0bfc9fd44c4700a474f97f06dc86ed73d817bfc8b4432efb057f3a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdc0",
        "00bdcdcf"
      ]
    ],
    "bytes_sha256": "577662e8ade29a3df2df5b35889e8cc6bb584e208aa5be15bc0c945994a3c78f",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e9260](../004e9/004e9260.md)

## 呼び出し先

- [004e939c](../004e9/004e939c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 179 bytes

~~~c

void _ZNK5Botan4OCSP6CertID9is_id_forERKNS_16X509_CertificateES4_(void)

{
  (*(code *)PTR__ZNK5Botan4OCSP6CertID9is_id_forERKNS_16X509_CertificateES4__00c1cf70)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdc0"></a> `00bdcdc0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdc4"></a> `00bdcdc4` | `11 ba 47 f9` | ldr x17,[x16, #0xf70] | `FALL_THROUGH`
<a id="insn-00bdcdc8"></a> `00bdcdc8` | `10 c2 3d 91` | add x16,x16,#0xf70 | `FALL_THROUGH`
<a id="insn-00bdcdcc"></a> `00bdcdcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdc0`](#insn-00bdcdc0) 範囲 `[['00bdcdc0', '00bdcdcf']]`

## 命令位置別の参照

- [`00bdcdc4`](#insn-00bdcdc4) → `00c1cf70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdcc`](#insn-00bdcdcc) → [`004e939c`](../004e9/004e939c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e939c` · 推定シンボル `_ZNK5Botan4OCSP6CertID9is_id_forERKNS_16X509_CertificateES4_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdc4`](#insn-00bdcdc4)

~~~json
{
  "source": "00bdcdc4",
  "target": "00c1cf70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcdcc`](#insn-00bdcdcc)

~~~json
{
  "source": "00bdcdcc",
  "target": "004e939c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
