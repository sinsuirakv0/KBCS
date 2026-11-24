# 00bdcbd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-07ef421e02efa8da29870a615ae46ce2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59620`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59620.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-a00b4478fa40b869a029b9d53fa31a32)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbd0",
  "name": "_ZNK5Botan7X509_DN14get_attributesEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a54df21192fc78057b25298f0a17b9d400289262fa0e000b53521a625023e876",
  "source_text_sha256": "a54df21192fc78057b25298f0a17b9d400289262fa0e000b53521a625023e876",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbd0",
        "00bdcbdf"
      ]
    ],
    "bytes_sha256": "881a43546b58d43982044479fa5c85aabcc925b1f0eb8362fbd3d08804db0a56",
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
  (*(code *)PTR__ZNK5Botan7X509_DN14get_attributesEv_00c1cea0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbd0"></a> `00bdcbd0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbd4"></a> `00bdcbd4` | `11 52 47 f9` | ldr x17,[x16, #0xea0] | `FALL_THROUGH`
<a id="insn-00bdcbd8"></a> `00bdcbd8` | `10 82 3a 91` | add x16,x16,#0xea0 | `FALL_THROUGH`
<a id="insn-00bdcbdc"></a> `00bdcbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbd0`](#insn-00bdcbd0) 範囲 `[['00bdcbd0', '00bdcbdf']]`

## 命令位置別の参照

- [`00bdcbd4`](#insn-00bdcbd4) → `00c1cea0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbdc`](#insn-00bdcbdc) → [`004e5c34`](../004e5/004e5c34.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e5c34` · 推定シンボル `_ZNK5Botan7X509_DN14get_attributesEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbd4`](#insn-00bdcbd4)

~~~json
{
  "source": "00bdcbd4",
  "target": "00c1cea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cea0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbdc`](#insn-00bdcbdc)

~~~json
{
  "source": "00bdcbdc",
  "target": "004e5c34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
