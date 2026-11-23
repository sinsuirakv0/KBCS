# 00bdcab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-994fdac4c1d5cf4cd0694bc9a013de4b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcab0",
  "name": "_ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9741a720212e3644ba2b2a2015db31b02cb76d57633f95dfd8b73aaf92eb27b",
  "source_text_sha256": "e9741a720212e3644ba2b2a2015db31b02cb76d57633f95dfd8b73aaf92eb27b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcab0",
        "00bdcabf"
      ]
    ],
    "bytes_sha256": "42920a2e6cb303129063b6f8776c990b6bd64ab101a6eb7583b28b93eda98b47",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0050645c](../00506/0050645c.md)

## 呼び出し先

- [004de9a8](../004de/004de9a8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 293 bytes

~~~c

void _ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE
               (void)

{
  (*(code *)
    PTR__ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE_00c1cd90
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcab0"></a> `00bdcab0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcab4"></a> `00bdcab4` | `11 ca 46 f9` | ldr x17,[x16, #0xd90] | `FALL_THROUGH`
<a id="insn-00bdcab8"></a> `00bdcab8` | `10 42 36 91` | add x16,x16,#0xd90 | `FALL_THROUGH`
<a id="insn-00bdcabc"></a> `00bdcabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcab0`](#insn-00bdcab0) 範囲 `[['00bdcab0', '00bdcabf']]`

## 命令位置別の参照

- [`00bdcab4`](#insn-00bdcab4) → `00c1cd90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcabc`](#insn-00bdcabc) → [`004de9a8`](../004de/004de9a8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004de9a8` · 推定シンボル `_ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcab4`](#insn-00bdcab4)

~~~json
{
  "source": "00bdcab4",
  "target": "00c1cd90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cd90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcabc`](#insn-00bdcabc)

~~~json
{
  "source": "00bdcabc",
  "target": "004de9a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
