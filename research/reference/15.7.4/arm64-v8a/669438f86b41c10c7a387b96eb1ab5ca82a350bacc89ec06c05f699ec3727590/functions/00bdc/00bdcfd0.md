# 00bdcfd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcf80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-fd3a4bfa6067128e8358d46da3f95875)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59a20`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a20.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0010.md#compare-e1cfec64a66432674da38342ccace9fa)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfd0",
  "name": "_ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "30927952a5bc82217fde4d2f290cf64c3e7d2e6bd5eebead922211eead9a002f",
  "source_text_sha256": "30927952a5bc82217fde4d2f290cf64c3e7d2e6bd5eebead922211eead9a002f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfd0",
        "00bdcfdf"
      ]
    ],
    "bytes_sha256": "a5d197fd55aabc7d70c54e24fc2db7b88437057bf87827f53c9f2bafc1b6d20c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004fdfd8](../004fd/004fdfd8.md)

## 呼び出し先

- [004f4e50](../004f4/004f4e50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 171 bytes

~~~c

void _ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_(void)

{
  (*(code *)PTR__ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2__00c1d0a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfd0"></a> `00bdcfd0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfd4"></a> `00bdcfd4` | `11 52 40 f9` | ldr x17,[x16, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdcfd8"></a> `00bdcfd8` | `10 82 02 91` | add x16,x16,#0xa0 | `FALL_THROUGH`
<a id="insn-00bdcfdc"></a> `00bdcfdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfd0`](#insn-00bdcfd0) 範囲 `[['00bdcfd0', '00bdcfdf']]`

## 命令位置別の参照

- [`00bdcfd4`](#insn-00bdcfd4) → `00c1d0a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfdc`](#insn-00bdcfdc) → [`004f4e50`](../004f4/004f4e50.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f4e50` · 推定シンボル `_ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfd4`](#insn-00bdcfd4)

~~~json
{
  "source": "00bdcfd4",
  "target": "00c1d0a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d0a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfdc`](#insn-00bdcfdc)

~~~json
{
  "source": "00bdcfdc",
  "target": "004f4e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
