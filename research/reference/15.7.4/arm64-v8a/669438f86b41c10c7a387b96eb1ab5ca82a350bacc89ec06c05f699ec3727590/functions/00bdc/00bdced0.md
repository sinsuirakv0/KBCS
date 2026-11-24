# 00bdced0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-e280f79ba33b3d9f4a4e3232e7814100)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59920`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59920.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0021.md#compare-9648441b50bc1abc6a2b73d1cab1c8ed)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdced0",
  "name": "_ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e45d01be62f49d0d9610d9635b6e340880827b8b74c2880caeb793e1c121f17c",
  "source_text_sha256": "e45d01be62f49d0d9610d9635b6e340880827b8b74c2880caeb793e1c121f17c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdced0",
        "00bdcedf"
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

- [004ec8c8](../004ec/004ec8c8.md)
- [004fdfd8](../004fd/004fdfd8.md)

## 呼び出し先

- [004eca70](../004ec/004eca70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 282 bytes

~~~c

void _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv(void)

{
                    /* try { // try from 00bdced4 to 00cdceeb has its CatchHandler @ 00bdd2ac */
  (*(code *)PTR__ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv_00c1d020)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdced0"></a> `00bdced0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdced4"></a> `00bdced4` | `11 12 40 f9` | ldr x17,[x16, #0x20] | `FALL_THROUGH`
<a id="insn-00bdced8"></a> `00bdced8` | `10 82 00 91` | add x16,x16,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcedc"></a> `00bdcedc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdced0`](#insn-00bdced0) 範囲 `[['00bdced0', '00bdced3']]`
  - `FALL_THROUGH` [`00bdced0`](#insn-00bdced0) → [`00bdced4`](#insn-00bdced4)
- ブロック [`00bdced4`](#insn-00bdced4) 範囲 `[['00bdced4', '00bdcedf']]`

## 命令位置別の参照

- [`00bdced4`](#insn-00bdced4) → `00c1d020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcedc`](#insn-00bdcedc) → [`004eca70`](../004ec/004eca70.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004eca70` · 推定シンボル `_ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdced4`](#insn-00bdced4)

~~~json
{
  "source": "00bdced4",
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
- 参照命令 [`00bdcedc`](#insn-00bdcedc)

~~~json
{
  "source": "00bdcedc",
  "target": "004eca70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
