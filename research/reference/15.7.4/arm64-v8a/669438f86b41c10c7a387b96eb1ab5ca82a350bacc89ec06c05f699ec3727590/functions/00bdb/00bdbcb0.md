# 00bdbcb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-c85ff1aea69e70683e5457db927ef54d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58700`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58700.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-0c6843a6c8fe262811e106d9930400e1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcb0",
  "name": "_ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b872dda676a8a74b301a8e6ef365ee99e832c5919c7248439cd80d87339f3db0",
  "source_text_sha256": "b872dda676a8a74b301a8e6ef365ee99e832c5919c7248439cd80d87339f3db0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcb0",
        "00bdbcbf"
      ]
    ],
    "bytes_sha256": "d82c882184d9a879da171abf53764d206d03217c077188a47c32f12d2bcc32b2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048fc00](../0048f/0048fc00.md)
- [00493850](../00493/00493850.md)
- [004bb3f0](../004bb/004bb3f0.md)
- [004bb59c](../004bb/004bb59c.md)
- [004bb70c](../004bb/004bb70c.md)
- [004ccf4c](../004cc/004ccf4c.md)
- [004cd86c](../004cd/004cd86c.md)
- [004fc6ac](../004fc/004fc6ac.md)

## 呼び出し先

- [004d7c34](../004d7/004d7c34.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 277 bytes

~~~c

void _ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE_00c1c710
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcb0"></a> `00bdbcb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcb4"></a> `00bdbcb4` | `11 8a 43 f9` | ldr x17,[x16, #0x710] | `FALL_THROUGH`
<a id="insn-00bdbcb8"></a> `00bdbcb8` | `10 42 1c 91` | add x16,x16,#0x710 | `FALL_THROUGH`
<a id="insn-00bdbcbc"></a> `00bdbcbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcb0`](#insn-00bdbcb0) 範囲 `[['00bdbcb0', '00bdbcbf']]`

## 命令位置別の参照

- [`00bdbcb4`](#insn-00bdbcb4) → `00c1c710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcbc`](#insn-00bdbcbc) → [`004d7c34`](../004d7/004d7c34.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004d7c34` · 推定シンボル `_ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcb4`](#insn-00bdbcb4)

~~~json
{
  "source": "00bdbcb4",
  "target": "00c1c710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c710",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcbc`](#insn-00bdbcbc)

~~~json
{
  "source": "00bdbcbc",
  "target": "004d7c34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
