# 00bdccb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcc00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-3f6a47cc59e0df10460ec46265fe5b52)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcd00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-482337d07687ad326549f9b00fab1f9a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccb0",
  "name": "_ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "197a2825c02ae8a81b0a5f51dfc4779c5ce3446826db1858cc588bfbead852f1",
  "source_text_sha256": "197a2825c02ae8a81b0a5f51dfc4779c5ce3446826db1858cc588bfbead852f1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccb0",
        "00bdccbf"
      ]
    ],
    "bytes_sha256": "396b0e5f8a2f1b772a9c00ed929f5f58e04404dec40cf89952ae2ca5be6a0356",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004f8244](../004f8/004f8244.md)

## 呼び出し先

- [004e4494](../004e4/004e4494.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 171 bytes

~~~c

void _ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE(void)

{
  (*(code *)PTR__ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE_00c1cee8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccb0"></a> `00bdccb0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdccb4"></a> `00bdccb4` | `11 76 47 f9` | ldr x17,[x16, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdccb8"></a> `00bdccb8` | `10 a2 3b 91` | add x16,x16,#0xee8 | `FALL_THROUGH`
<a id="insn-00bdccbc"></a> `00bdccbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccb0`](#insn-00bdccb0) 範囲 `[['00bdccb0', '00bdccbf']]`

## 命令位置別の参照

- [`00bdccb4`](#insn-00bdccb4) → `00c1cee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdccbc`](#insn-00bdccbc) → [`004e4494`](../004e4/004e4494.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e4494` · 推定シンボル `_ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccb4`](#insn-00bdccb4)

~~~json
{
  "source": "00bdccb4",
  "target": "00c1cee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cee8",
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
  "target": "004e4494",
  "target_space": "ram",
  "resolution": "function"
}
~~~
