# 00bdcad0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-a37204a66ba7b9a8812612fe10ada21e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcad0",
  "name": "_ZNK5Botan7X509_DN14get_attributesEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3519dfe4a362defc7a68b82aeaad5ba5495d557282200be3fd0e22c2df08ac5",
  "source_text_sha256": "e3519dfe4a362defc7a68b82aeaad5ba5495d557282200be3fd0e22c2df08ac5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcad0",
        "00bdcadf"
      ]
    ],
    "bytes_sha256": "d6789b70b8f254eaae2783a93e1e3ff8226a3c555c19e0a459142a35b7b0d4bf",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004deb5c](../004de/004deb5c.md)
- [004e50d0](../004e5/004e50d0.md)
- [004f1c30](../004f1/004f1c30.md)
- [004f1ecc](../004f1/004f1ecc.md)
- [00503af8](../00503/00503af8.md)

## 呼び出し先

- [004e5c34](../004e5/004e5c34.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZNK5Botan7X509_DN14get_attributesEv(void)

{
  (*(code *)PTR__ZNK5Botan7X509_DN14get_attributesEv_00c1cda0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcad0"></a> `00bdcad0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcad4"></a> `00bdcad4` | `11 d2 46 f9` | ldr x17,[x16, #0xda0] | `FALL_THROUGH`
<a id="insn-00bdcad8"></a> `00bdcad8` | `10 82 36 91` | add x16,x16,#0xda0 | `FALL_THROUGH`
<a id="insn-00bdcadc"></a> `00bdcadc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcad0`](#insn-00bdcad0) 範囲 `[['00bdcad0', '00bdcadf']]`

## 命令位置別の参照

- [`00bdcad4`](#insn-00bdcad4) → `00c1cda0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcadc`](#insn-00bdcadc) → [`004e5c34`](../004e5/004e5c34.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e5c34` · 推定シンボル `_ZNK5Botan7X509_DN14get_attributesEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcad4`](#insn-00bdcad4)

~~~json
{
  "source": "00bdcad4",
  "target": "00c1cda0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cda0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcadc`](#insn-00bdcadc)

~~~json
{
  "source": "00bdcadc",
  "target": "004e5c34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
