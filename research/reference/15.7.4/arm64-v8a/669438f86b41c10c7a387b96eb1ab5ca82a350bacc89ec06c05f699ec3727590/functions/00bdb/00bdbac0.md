# 00bdbac0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdba70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-0897549e2bd677981085cbaa5809ec30)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58510`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58510.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-dfd936c52d0f5a06f35ae22239ed9a6b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbac0",
  "name": "_ZNK5Botan9X509_Time15readable_stringEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "159f546fff79315d8c71466a0c22f6bbec30bade000a58135908ffa9a38b668d",
  "source_text_sha256": "159f546fff79315d8c71466a0c22f6bbec30bade000a58135908ffa9a38b668d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbac0",
        "00bdbacf"
      ]
    ],
    "bytes_sha256": "10e205378ca1258239718c5c5bdab784b947e03eb2e7e01a581aa98c974c12ec",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00485f54](../00485/00485f54.md)
- [0048b804](../0048b/0048b804.md)
- [00501b08](../00501/00501b08.md)

## 呼び出し先

- [0048930c](../00489/0048930c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 137 bytes

~~~c

void _ZNK5Botan9X509_Time15readable_stringEv(void)

{
  (*(code *)PTR__ZNK5Botan9X509_Time15readable_stringEv_00c1c618)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbac0"></a> `00bdbac0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbac4"></a> `00bdbac4` | `11 0e 43 f9` | ldr x17,[x16, #0x618] | `FALL_THROUGH`
<a id="insn-00bdbac8"></a> `00bdbac8` | `10 62 18 91` | add x16,x16,#0x618 | `FALL_THROUGH`
<a id="insn-00bdbacc"></a> `00bdbacc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbac0`](#insn-00bdbac0) 範囲 `[['00bdbac0', '00bdbacf']]`

## 命令位置別の参照

- [`00bdbac4`](#insn-00bdbac4) → `00c1c618`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbacc`](#insn-00bdbacc) → [`0048930c`](../00489/0048930c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048930c` · 推定シンボル `_ZNK5Botan9X509_Time15readable_stringEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbac4`](#insn-00bdbac4)

~~~json
{
  "source": "00bdbac4",
  "target": "00c1c618",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c618",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbacc`](#insn-00bdbacc)

~~~json
{
  "source": "00bdbacc",
  "target": "0048930c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
